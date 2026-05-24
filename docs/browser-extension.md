# Browser Extension (v0.3 MVP)

See [browser-extension/README.md](../browser-extension/README.md) for install steps.

## Why it exists

Founder goal #3: **show what is being checked while auditing**, on the site under review — not only in a separate `localhost` tab.

## Coexistence with Skills

| Layer | Location |
| --- | --- |
| Orchestration & rubrics | `.claude/skills/audit` and sub-skills |
| Live state contract | `schemas/audit-run.schema.json` |
| Full workbench | `workbench/live/`, `workbench/report/` |
| Browser overlay + capture | `browser-extension/` + `scripts/browser-relay.py` |

The extension must not redefine `S0–S4` or issue cards. Agents merge extension screenshots into `audit-report.json` evidence paths manually or in a future script.

## Quick start

```bash
python3 -m http.server 8765 &
python3 scripts/browser-relay.py &
./scripts/audit-run-init.sh "https://yoursite.com"
# → paste STATE_HTTP_URL into extension popup
```
