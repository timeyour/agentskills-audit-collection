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

This folder may stay empty in the repo; use `.gitkeep` per audit folder when needed. Do not commit secrets.
