"""Tests for audit_report_merge_run.py"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "scripts"))

from audit_report_merge_run import (  # noqa: E402
    audit_progress_from_run,
    load_or_init_report,
    merge_capture_into_report,
    main,
)


class TestAuditReportMergeRun(unittest.TestCase):
    def test_audit_progress_from_golden_run(self) -> None:
        run = json.loads((ROOT / "validation/golden/audit-run.example.json").read_text())
        progress = audit_progress_from_run(run, "validation/artifacts/demo")
        self.assertEqual(progress["status"], "running")
        self.assertIn("Intake & permissions", progress["completedSteps"])
        self.assertTrue(progress.get("currentStep"))
        self.assertIn("workbench/live/", progress["liveWorkbenchHint"])

    def test_merge_capture_updates_physical_evidence(self) -> None:
        report = {"evidence": {"overallGrade": "LOW", "items": [{"type": "PHYSICAL", "status": "missing"}]}}
        result = {
            "capture_tool": "playwright",
            "status": "passed",
            "artifacts": {"screenshot": "validation/artifacts/x/screenshots/homepage.png"},
        }
        merge_capture_into_report(report, result)
        phys = next(i for i in report["evidence"]["items"] if i["type"] == "PHYSICAL")
        self.assertEqual(phys["status"], "available")

    def test_main_writes_report(self) -> None:
        run = json.loads((ROOT / "validation/golden/audit-run.example.json").read_text())
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            (run_dir / "run-state.json").write_text(json.dumps(run), encoding="utf-8")
            code = main(["--run-dir", str(run_dir)])
            self.assertEqual(code, 0)
            out = run_dir / "audit-report.json"
            self.assertTrue(out.is_file())
            data = json.loads(out.read_text())
            self.assertIn("auditProgress", data)
            self.assertEqual(data["target"]["url"], run["target"]["url"])


if __name__ == "__main__":
    unittest.main()
