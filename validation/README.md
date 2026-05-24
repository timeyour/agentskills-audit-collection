# Validation Directory

Three-layer layout for v0.1 (templates → cases → artifacts).

## Structure

```text
validation/
  templates/     # Standard report shells (copy for new audits)
  cases/         # Golden case briefs (benchmark stories)
  artifacts/     # Runtime evidence from browser/tool runs
  golden/        # Machine + human examples for schema and public reports
  *.md           # Historical batch audits (preserved, not moved)
```

## Templates (`templates/`)

| File | Use |
| --- | --- |
| [public-website-audit-report-template.md](templates/public-website-audit-report-template.md) | Customer-facing report |
| [live-functional-audit-template.md](templates/live-functional-audit-template.md) | Feature + flow testing |
| [five-pass-acceptance-template.md](templates/five-pass-acceptance-template.md) | Five-pass acceptance |
| [vibe-coded-site-verification-template.md](templates/vibe-coded-site-verification-template.md) | 14-point vibe scoring |

Canonical copies live in `templates/`. Root-level files with the same names remain for backward links.

## Cases (`cases/`)

Structured briefs for the four primary benchmarks:

- [index.json](cases/index.json) — machine catalog for `benchmarkRefs` / `benchmarkCaseId`
- [api-checker.md](cases/api-checker.md)
- [phonevalidation.md](cases/phonevalidation.md)
- [committed-citizens.md](cases/committed-citizens.md)
- [impeccable-style.md](cases/impeccable-style.md)

## Golden (`golden/`)

- [audit-report.example.json](golden/audit-report.example.json) — schema example for workbench UI
- [audit-report.merged.example.json](golden/audit-report.merged.example.json) — after `audit_report_merge_run.py` (includes `auditProgress`)
- [audit-run.example.json](golden/audit-run.example.json) — live workbench demo state
- [run-state.json](golden/run-state.json) — same shape as production `run-state.json` (merge demo)
- [public-report.example.md](golden/public-report.example.md) — public report example

## Artifacts (`artifacts/`)

Store screenshots, traces, HAR, console logs, and `result.json` from physical runs. See [artifacts/README.md](artifacts/README.md).

## M3 capture runs

```bash
./scripts/audit_capture.py https://example.com
# → validation/artifacts/<runId>/result.json, logs/, screenshots/
```

See [docs/m3-capture-workflow.md](../docs/m3-capture-workflow.md).

## Related

- [docs/v0.1-scope.md](../docs/v0.1-scope.md)
- [schemas/audit-report.schema.json](../schemas/audit-report.schema.json)
- [CASE_STUDIES.md](../CASE_STUDIES.md)
