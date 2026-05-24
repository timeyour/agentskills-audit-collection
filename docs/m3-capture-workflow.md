# M3 Capture Workflow

Semi-automated evidence capture for live URL audits. Output lands in `validation/artifacts/<runId>/`.

## Quick start

```bash
# 1. Start a live run (optional — creates run-state.json for workbench/live)
./scripts/audit-run-init.sh https://example.com

# 2. Capture evidence into that run dir (use RUN_DIR from step 1)
./scripts/audit_capture.py https://example.com --run-dir validation/artifacts/<runId>

# Or one-shot (creates a new runId automatically)
./scripts/audit_capture.py https://example.com
```

## With Playwright (screenshot + console)

```bash
pip install playwright
playwright install chromium
./scripts/audit_capture.py https://example.com --run-dir validation/artifacts/<runId>
```

## Outputs

| Path | Content |
| --- | --- |
| `result.json` | Step summary, surface counts, artifact paths |
| `screenshots/homepage.png` | Viewport screenshot (Playwright only) |
| `logs/console.log` | Browser console lines (Playwright) or HTTP probe note |
| `run-events.ndjson` | Appended if run dir from `audit-run-init.sh` |

## Rules

- Failed HTTP → `status: failed`; do not infer PASS on workflows.
- No Playwright → screenshot `SKIPPED-SAFE` in `result.json`.
- Redact secrets before committing artifacts.
- Reference paths from `audit-report.json` → `issueCards[].evidence.artifacts`.

## Merge run → audit report

After `/audit` and optional capture, sync **auditProgress** (and capture evidence) into the report:

```bash
python3 scripts/audit_report_merge_run.py \
  --run-dir validation/artifacts/<runId> \
  --report validation/artifacts/<runId>/audit-report.json \
  --merge-preview \
  --export-html reports/latest-audit.html
```

This sets:

- `auditProgress` from `run-state.json` (completed steps, label, live workbench link)
- `evidence` PHYSICAL/LIVE notes from `result.json` when present
- `run-state.json` → `reportPath` pointer

## View results

```bash
python3 -m http.server 8765
# Live:  http://localhost:8765/workbench/live/?state=validation/artifacts/<runId>/run-state.json
# Report JSON: validation/artifacts/<runId>/audit-report.json
# Workbench:   http://localhost:8765/workbench/report/?report=validation/artifacts/<runId>/audit-report.json
# Public HTML: reports/latest-audit.html (after --export-html)
```
