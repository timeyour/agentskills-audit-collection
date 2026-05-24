# Validation Artifacts

Store **reproducible evidence** from audit runs here (or link from project-local `artifacts/` paths recorded in the report JSON).

## Expected Layout

```text
validation/artifacts/
  {audit-id}/
    screenshots/
    traces/
    har/
    logs/
    result.json
```

Naming follows `.claude/skills/physical-flow-test/references/artifact-schema.md`.

## What Belongs Here

| Artifact | Purpose |
| --- | --- |
| `screenshots/*.png` | Visual proof, failure states |
| `traces/trace.zip` | Playwright trace |
| `har/network.redacted.har` | Network (redact secrets before commit) |
| `logs/console.log` | Console errors |
| `result.json` | Step-level pass/fail summary |

## Rules

1. **Redact** tokens, cookies, PII, and API keys before committing.
2. **Reference** paths from `audit-report.schema.json` → `issueCards[].evidence.artifacts`.
3. Do not commit large videos by default; link externally or use `.gitkeep` placeholders.
4. Missing artifacts → report `UNKNOWN`, not inferred PASS.

## Git

**`validation/artifacts/*` run folders are gitignored** — they exist only on the machine that ran the audit. To view BarrierLens (or any past run) on another clone, use the checked-in golden snapshot:

- Live workbench: `http://127.0.0.1:8765/workbench/live/?barrierlens=1`
- File: `validation/golden/barrierlens-run-state.json`

Re-create a local run: `./scripts/audit-run-init.sh "https://yoursite.com"`.

Do not commit secrets inside artifact folders.
