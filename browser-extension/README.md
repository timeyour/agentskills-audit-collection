# AgentSkills Browser Extension (MVP)

**In-page narration + screenshot evidence.** Audit rules stay in `.claude/skills/` (`/audit`); this extension only:

1. Polls `run-state.json` (same contract as `workbench/live/`)
2. Shows `activeAnnotation` on the page you are reviewing
3. Saves viewport PNGs into `validation/artifacts/<runId>/screenshots/` (via local relay)

## Install (unpacked, team use)

1. Chrome → `chrome://extensions` → Developer mode → **Load unpacked**
2. Select this folder: `browser-extension/`
3. In the repo root:

```bash
python3 -m http.server 8765
python3 scripts/browser-relay.py    # optional, port 8766
./scripts/audit-run-init.sh "https://example.com"
```

4. Copy **`STATE_HTTP_URL`** from the init script output into the extension popup → **保存**
5. Open the target site; the overlay appears bottom-right
6. In Cursor/Claude: `Use /audit on …` and update `run-state.json` per `live-run-protocol.md`

## Architecture

```text
Agent (/audit Skills)  →  writes run-state.json
        ↑                          ↓ poll (1s)
Background service worker  →  content script overlay
        ↓ POST /api/evidence (optional)
browser-relay.py  →  validation/artifacts/<runId>/screenshots/
```

| Component | Writes severity / issues? |
| --- | --- |
| Skills + Agent | Yes (schema + S0–S4) |
| Extension | No — read narration, capture PNG + meta |
| workbench/live | No — read-only UI |

## run-state fields used

| Field | Overlay use |
| --- | --- |
| `activeAnnotation` | Main caption (旁白) |
| `progress.label` | Subtitle |
| `status` | Subtitle |
| `findingsPreview[]` | Up to 3 preview chips |
| `target.url` | Hostname match hint |

Full schema: `schemas/audit-run.schema.json`.

## Evidence files

With relay running, **截图留证** creates:

```text
validation/artifacts/<runId>/screenshots/
  ext-<timestamp>.png
  ext-<timestamp>.meta.json
```

`meta.json` includes `url`, `stageId`, `stepId`, `note`. An `evidence_captured` line is appended to `run-events.ndjson` when present.

Without relay, captures are queued in `chrome.storage.local.evidenceQueue` (export manually later).

## Permissions

- `storage` — config + fallback queue
- `activeTab` — `captureVisibleTab` on user click
- `host_permissions` — `127.0.0.1:8765` (run-state + workbench), `8766` (relay)

## Not in MVP

- Console / HAR export
- Chrome Web Store packaging
- In-extension issue editor or S0–S4 picker
- Firefox / Safari

## Related docs

- [live-run-protocol.md](../.claude/skills/audit/references/live-run-protocol.md)
- [workbench/live/README.md](../workbench/live/README.md)
- [docs/vision-and-flow.md](../docs/vision-and-flow.md) §0 item 3
