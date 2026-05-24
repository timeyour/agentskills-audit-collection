# Live Run Protocol

Use with `references/progressive-reporting.md` when the user wants to **see the audit happen** in the workbench or when a run has more than five meaningful steps.

## Files Per Run

```text
validation/artifacts/{runId}/
  run-state.json      # overwrite atomically — UI reads this
  run-events.ndjson   # append one JSON object per line
  audit-report.json   # written at end (schema 0.1.0)
  screenshots/        # optional — browser extension + relay (ext-*.png)
```

Optional in-page overlay: `browser-extension/` polls the same `run-state.json`. See `browser-extension/README.md`.

Initialize with host script when available:

```bash
./scripts/audit-run-init.sh "<target-url>"
```

Otherwise create the folder and copy structure from `validation/golden/audit-run.example.json`.

## run-state.json Rules

1. Conform to `schemas/audit-run.schema.json`.
2. Update `updatedAt` on every write (ISO 8601 UTC).
3. Set `activeAnnotation` to a short **present-tense** caption (what you are doing *now*).
4. Set exactly one step to `in_progress` unless paused/blocked.
5. `progress.current` / `progress.total` match completed stages + current stage index in the default 9-stage workflow (or adjusted total if stages skipped).
6. On `needs_confirmation` or `SKIPPED-SAFE`, set step status accordingly; do not silently skip.

## NDJSON Event Types

Append one JSON object per line to `run-events.ndjson`:

| type | When |
| --- | --- |
| `run_started` | Run created |
| `stage_start` | Stage becomes in_progress |
| `stage_complete` | Stage completed or skipped |
| `step_start` | Step in_progress |
| `step_update` | Annotation or evidence change |
| `step_complete` | Step terminal status |
| `finding_added` | New finding preview |
| `safety_pause` | Needs user confirmation |
| `run_complete` | Final report path set |
| `run_failed` | Unrecoverable error |

Example line:

```json
{"ts":"2026-05-24T12:01:00Z","type":"step_update","stageId":"live-functional","stepId":"cta-primary","status":"in_progress","annotation":"Opening homepage; locating Primary CTA","evidenceLevel":"LIVE"}
```

## Chat Sync

Every `run-state.json` update that changes stage or step should have a matching:

```text
Progress Update [current/total] - [stage label]
Status: in progress | completed | issue found | blocked | needs confirmation
What I just did: ...
Key findings so far: ...
Evidence collected: ...
Next step: ...
```

Keep chat and `activeAnnotation` aligned.

## Default Stages

Use workflow id `audit-default-v1` with stages:

`intake` → `surface-discovery` → `source-pass` → `feature-inventory` → `live-functional` → `visual-qa` → `deploy-check` → `synthesis` → `accept-five` (optional skip)

Each stage should list 2–6 concrete `steps` (e.g. under `live-functional`: homepage load, primary CTA, lead form, auth boundary).

## Completion

1. Set `status: completed` on run-state.
2. Write `audit-report.json` beside run files.
3. Append `run_complete` event with `reportPath`.
4. Deliver final report in chat; do not dump full NDJSON unless asked.

## Anti-Patterns

- Updating chat but not `run-state.json` (workbench stays frozen).
- Leaving multiple steps `in_progress`.
- Setting `completed` on a step without evidence label.
- Writing secrets into run-state or events.
