# Browser extension — optional second model (narration)

The extension **never** runs `/audit` or assigns severity. An optional LLM only transforms text already written by the IDE/terminal agent into `run-state.json` → `activeAnnotation`.

Policy context: [runtime-surfaces.md](runtime-surfaces.md).

## Data flow

```text
IDE agent (any model)  →  activeAnnotation in run-state.json
                                    ↓ poll (background)
                         narration/enhance.js  (optional)
                                    ↓
                         ASW_RUN_STATE { state, displayAnnotation }
                                    ↓
                         content/overlay.js  (shows displayAnnotation)
```

| Field | Writer | Reader |
| --- | --- | --- |
| `activeAnnotation` | Agent / Skills | Source of truth; never overwritten by extension |
| `displayAnnotation` | Extension broadcast only | Overlay caption (may be translated/summarized) |

## Config (`chrome.storage.local`)

Stored under key `narration` (see `schemas/extension-narration-config.schema.json`).

| Field | Default | Meaning |
| --- | --- | --- |
| `enabled` | `false` | Master switch |
| `mode` | `passthrough` | `passthrough` \| `relay` \| `direct` |
| `task` | `none` | `none` \| `translate` \| `summarize` |
| `targetLocale` | `zh` | BCP-47 target (`zh`, `en`, …) |
| `relayUrl` | same as evidence relay | `POST /api/narrate` |
| `direct.endpoint` | `""` | OpenAI-compatible URL (user-provided) |
| `direct.model` | `""` | e.g. `gpt-4o-mini` |
| `direct.apiKey` | `""` | **Local only** — never committed |

### Mode matrix

| mode | Where the model runs | API key location |
| --- | --- | --- |
| `passthrough` | Nowhere | — |
| `relay` | Your machine via `browser-relay.py` | Env: `ASW_NARRATE_URL`, `ASW_NARRATE_API_KEY`, `ASW_NARRATE_MODEL` |
| `direct` | Provider from extension popup | `chrome.storage.local` (user paste) |

**Recommended:** `relay` so secrets stay out of the MV3 bundle and match terminal CI patterns.

## Relay API — `POST /api/narrate`

Implemented in `scripts/browser-relay.py` (v0.2 stub: passthrough unless env is set).

### Request

```json
{
  "text": "正在检测首页 Primary CTA…",
  "task": "translate",
  "targetLocale": "zh",
  "sourceLocale": "auto",
  "context": {
    "runId": "20260524T120000Z-demo",
    "stageId": "live-functional",
    "stepId": "cta-primary",
    "status": "running"
  }
}
```

### Response

```json
{
  "ok": true,
  "mode": "passthrough",
  "text": "正在检测首页 Primary CTA…",
  "provider": null,
  "model": null
}
```

When `ASW_NARRATE_URL` + `ASW_NARRATE_API_KEY` are set, relay forwards to an OpenAI-compatible `chat/completions` call and returns `mode: "llm"`.

### Env (terminal / relay host)

```bash
export ASW_NARRATE_URL="https://api.openai.com/v1/chat/completions"
export ASW_NARRATE_API_KEY="sk-…"
export ASW_NARRATE_MODEL="gpt-4o-mini"
python3 scripts/browser-relay.py
```

## Direct API (extension → provider)

`narration/enhance.js` → `POST {endpoint}` with:

```json
{
  "model": "<from config>",
  "messages": [
    { "role": "system", "content": "You translate audit narration. Keep technical IDs. Output only the translation." },
    { "role": "user", "content": "<text>" }
  ],
  "max_tokens": 256
}
```

Errors fall back to `text` unchanged and set `displayAnnotationSource: "passthrough"`.

## Caching

Background caches by hash `(runId, stageId, stepId, activeAnnotation, task, targetLocale)` for 60s to avoid hammering the model on 1s poll.

## Security

- No API keys in repo, manifest, or workbench HTML
- Relay binds `127.0.0.1` only
- Extension must not send page DOM or screenshots to narrate endpoint unless a future opt-in `includePageContext` flag is added and documented

## Not in scope

- Choosing or running the **audit** model (stays in IDE)
- Editing `findingsPreview` or S0–S4 in the extension
- Chrome Web Store packaging

## Files

| Path | Role |
| --- | --- |
| `browser-extension/narration/enhance.js` | `ASW_enhanceCaption()` |
| `browser-extension/background.js` | Poll + enhance + broadcast |
| `schemas/extension-narration-config.schema.json` | Config contract |
| `scripts/browser-relay.py` | `/api/narrate` |
