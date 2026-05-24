# AgentSkills Audit Workbench

Local diagnostic UI for rendering `schemas/audit-report.schema.json` — **no framework required** for v0.1 static viewers.

## Goal

Let auditors and stakeholders **see what is being tested** while an agent runs `/audit`:

- feature inventory
- flow timeline
- issue cards with severity
- evidence and fix prompts
- regression checklist

## Quick Start

```bash
# From repo root — serves workbench + golden JSON
python3 -m http.server 8765
```

| Viewer | URL |
| --- | --- |
| **Final report** (M2) | http://localhost:8765/workbench/report/?demo=1 |
| **Live run** (in progress) | http://localhost:8765/workbench/live/?demo=1 |

Future: optional `workbench/app/` (Next.js/Vite) for richer interactions.

## v0.1 Artifacts

| File | Purpose |
| --- | --- |
| [spec.md](spec.md) | Page layout, data binding, scoped CSS rules |
| [components/README.md](components/README.md) | Per-component contracts |
| [../validation/golden/audit-report.example.json](../validation/golden/audit-report.example.json) | Golden render payload |
| [../docs/workbench-ui-spec.md](../docs/workbench-ui-spec.md) | Engineering rules |
| [../DESIGN.md](../DESIGN.md) | Design tokens |

## Viewers

| Surface | Path | Audience |
| --- | --- | --- |
| Report workbench | [report/](report/) | Auditor — schema-driven, DESIGN tokens, scoped `.asw-workbench` |
| Live workbench | [live/](live/) | Auditor — polls `run-state.json` during `/audit` |
| Public report demo | [reports/demo-site-audit.html](../reports/demo-site-audit.html) | Client / stakeholder — marketing-style layout |

## Principles

1. Data-driven from schema — no hand-wired issue lists in UI code.
2. Scoped styles only — see `docs/workbench-ui-spec.md`.
3. Customer report export is a separate template, not a stripped workbench.
