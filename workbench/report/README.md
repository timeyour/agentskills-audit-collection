# Audit Report Workbench (M2)

Static, **scoped** HTML viewer for final reports conforming to [schemas/audit-report.schema.json](../../schemas/audit-report.schema.json).

## Quick start

From the repository root:

```bash
python3 -m http.server 8765
```

Open:

```text
http://localhost:8765/workbench/report/?demo=1
```

Or load any report path:

```text
http://localhost:8765/workbench/report/?report=validation/golden/audit-report.example.json
```

## Components rendered

| Contract | UI region |
| --- | --- |
| `AuditHeader` | Top header + scorecard |
| `FeatureInventoryTable` | Left column |
| `FlowExecutionTimeline` | Center column |
| `IssueCard` + `SeverityBadge` | Right column |
| `CopyPromptBox` | Per issue + fix pack |
| `RegressionChecklist` | Right column (read-only checkboxes) |
| `EvidenceTable` | Footer |

All styles live under `.asw-workbench` — see [docs/workbench-ui-spec.md](../../docs/workbench-ui-spec.md).

## Related

- Live in-progress runs: [../live/](../live/)
- Public customer report style: [../../reports/demo-site-audit.html](../../reports/demo-site-audit.html)
- Golden JSON: [../../validation/golden/audit-report.example.json](../../validation/golden/audit-report.example.json)
