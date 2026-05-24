#!/usr/bin/env python3
"""
Merge live run-state.json (and optional capture result.json) into audit-report.json.

Typical end-of-audit flow:

  ./scripts/audit-run-init.sh https://example.com
  # ... agent runs /audit, updates run-state.json ...
  ./scripts/audit_capture.py https://example.com --run-dir validation/artifacts/<runId>
  # agent fills audit-report.json (or starts from golden template)
  python3 scripts/audit_report_merge_run.py \\
    --run-dir validation/artifacts/<runId> \\
    --report validation/artifacts/<runId>/audit-report.json \\
    --export-html reports/latest-audit.html
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOLDEN_REPORT = ROOT / "validation" / "golden" / "audit-report.example.json"


def rel_to_root(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return str(path)


def audit_progress_from_run(run: dict, run_dir_rel: str) -> dict:
    stages = sorted(run.get("stages") or [], key=lambda s: s.get("order", 0))
    completed: list[str] = []

    for stage in stages:
        if stage.get("status") == "completed":
            label = stage.get("label") or stage.get("id", "")
            if label and label not in completed:
                completed.append(label)
        for step in stage.get("steps") or []:
            if step.get("status") in ("completed", "issue_found"):
                label = step.get("label") or step.get("id", "")
                if label and label not in completed:
                    completed.append(label)

    current_step: str | None = run.get("activeAnnotation")
    if not current_step and run.get("currentStageId"):
        for stage in stages:
            if stage.get("id") != run.get("currentStageId"):
                continue
            for step in stage.get("steps") or []:
                if step.get("status") == "in_progress":
                    current_step = step.get("annotation") or step.get("label")
                    break
            if not current_step:
                current_step = stage.get("label")
            break

    progress = run.get("progress") or {}
    run_status = run.get("status", "partial")
    if run_status == "completed":
        ap_status = "completed"
    elif run_status == "failed":
        ap_status = "failed"
    elif run_status == "running":
        cur, total = progress.get("current", 0), progress.get("total", 1)
        ap_status = "running" if cur < total else "partial"
    else:
        ap_status = "partial"

    return {
        "status": ap_status,
        "label": progress.get("label", ""),
        "completedSteps": completed,
        "currentStep": current_step,
        "runId": run.get("runId"),
        "artifactsPath": run_dir_rel,
        "liveWorkbenchHint": f"workbench/live/?state={run_dir_rel}/run-state.json",
    }


def merge_capture_into_report(report: dict, result: dict) -> None:
    artifacts = result.get("artifacts") or {}
    paths = [p for p in artifacts.values() if isinstance(p, str) and p]
    if not paths:
        return

    evidence = report.setdefault("evidence", {"overallGrade": "UNKNOWN", "items": []})
    items = evidence.setdefault("items", [])
    by_type = {item.get("type"): item for item in items}

    tool = result.get("capture_tool", "unknown")
    capture_status = result.get("status", "partial")

    for level in ("LIVE", "PHYSICAL"):
        item = by_type.get(level)
        if not item:
            item = {"type": level, "status": "missing", "notes": ""}
            items.append(item)
            by_type[level] = item
        if level == "PHYSICAL" and artifacts.get("screenshot"):
            item["status"] = "available" if capture_status == "passed" else "partial"
            item["notes"] = f"Merged from audit_capture ({tool})"
            item["artifactPaths"] = paths
        elif level == "LIVE" and result.get("target_url"):
            item["status"] = "partial" if capture_status != "passed" else "available"
            item["notes"] = f"HTTP/capture probe via {tool}"

    surface = result.get("surface") or {}
    if surface.get("page_title") and surface["page_title"] != "UNKNOWN":
        report.setdefault("scope", {})
        summary = report["scope"].get("summary", "")
        if "capture" not in summary.lower():
            report["scope"]["summary"] = (summary + f" Live capture title: {surface['page_title']}.").strip()


def merge_findings_preview(report: dict, run: dict) -> int:
    """Append run findingsPreview as draft issue cards if id not present."""
    preview = run.get("findingsPreview") or []
    if not preview:
        return 0
    cards = report.setdefault("issueCards", [])
    existing_ids = {c.get("id") for c in cards}
    added = 0
    for i, finding in enumerate(preview, start=1):
        fid = finding.get("id") or f"PREVIEW-{i:03d}"
        if fid in existing_ids:
            continue
        cards.append(
            {
                "id": fid,
                "title": finding.get("title", "Finding from live run"),
                "severity": finding.get("severity", "S3"),
                "area": "workflow",
                "evidence": {
                    "level": finding.get("evidenceLevel", "LIVE"),
                    "summary": finding.get("summary")
                    or f"Stage {finding.get('stageId', '')} during live audit",
                    "artifacts": [],
                },
                "problem": finding.get("title", ""),
                "impact": "Captured during live audit; confirm in final review",
                "fix": "UNKNOWN — complete /audit synthesis",
                "reproduction": f"See {finding.get('stageId', 'live')} in run-state",
                "regressionCheck": "Re-run flow after fix; mark PASS only with evidence",
            }
        )
        added += 1
    return added


def load_or_init_report(report_path: Path, run: dict) -> dict:
    if report_path.is_file():
        return json.loads(report_path.read_text(encoding="utf-8"))
    if GOLDEN_REPORT.is_file():
        report = json.loads(GOLDEN_REPORT.read_text(encoding="utf-8"))
    else:
        report = {"schemaVersion": "0.1.0", "issueCards": [], "regressionChecks": []}
    target = report.setdefault("target", {})
    run_target = run.get("target") or {}
    if run_target.get("url"):
        target["url"] = run_target["url"]
    if run_target.get("label"):
        target.setdefault("label", run_target["label"])
    return report


def patch_run_state_report_path(run_dir: Path, report_rel: str) -> None:
    state_path = run_dir / "run-state.json"
    if not state_path.is_file():
        return
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state["reportPath"] = report_rel
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Merge run-state into audit-report.json")
    parser.add_argument("--run-dir", type=Path, required=True, help="validation/artifacts/<runId>")
    parser.add_argument(
        "--report",
        type=Path,
        help="audit-report.json path (default: <run-dir>/audit-report.json)",
    )
    parser.add_argument("--merge-preview", action="store_true", help="Append findingsPreview as draft issues")
    parser.add_argument("--export-html", type=Path, help="Also write public HTML via export_public_report")
    args = parser.parse_args(argv)

    run_dir = args.run_dir.resolve()
    state_path = run_dir / "run-state.json"
    if not state_path.is_file():
        print(f"error: missing {state_path}", file=sys.stderr)
        return 1

    run = json.loads(state_path.read_text(encoding="utf-8"))
    run_dir_rel = rel_to_root(run_dir)
    report_path = (args.report or run_dir / "audit-report.json").resolve()

    report = load_or_init_report(report_path, run)
    report["auditProgress"] = audit_progress_from_run(run, run_dir_rel)

    result_path = run_dir / "result.json"
    if result_path.is_file():
        merge_capture_into_report(report, json.loads(result_path.read_text(encoding="utf-8")))

    added = 0
    if args.merge_preview:
        added = merge_findings_preview(report, run)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report_rel = rel_to_root(report_path)
    patch_run_state_report_path(run_dir, report_rel)

    print(f"REPORT={report_rel}")
    print(f"auditProgress.status={report['auditProgress'].get('status')}")
    print(f"completedSteps={len(report['auditProgress'].get('completedSteps', []))}")
    if added:
        print(f"previewIssuesAdded={added}")

    if args.export_html:
        sys.path.insert(0, str(ROOT / "scripts"))
        from export_public_report import main as export_main

        export_main(["--input", str(report_path), "--output", str(args.export_html.resolve())])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
