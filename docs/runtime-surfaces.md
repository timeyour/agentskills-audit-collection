# Runtime surfaces & model policy

AgentSkills separates **what to audit** (skills + schemas) from **who runs the audit** (the host IDE, terminal, or browser layer). The workbench and extension only consume **`run-state.json`** and artifacts — they do not pick or host a model.

## Principle

| Layer | Model choice |
| --- | --- |
| **Audit brain** (`.claude/skills/`, `schemas/`) | **Model-agnostic** — same rubrics, S0–S4, evidence rules for every host |
| **Executor** (where `/audit` actually runs) | **Per surface** — see below |

## Three surfaces

```text
┌─────────────────────────────────────────────────────────────────┐
│  Skills + schemas (fixed contract: run-state, audit-report)      │
└───────────────────────────────┬─────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
   IDE (Cursor /            Terminal /              Browser
   Claude Code)             CLI & scripts           extension
        │                       │                       │
   IDE 自带模型              可用其他模型              可用其他模型
   (用户已在 IDE 里选的        (Codex CLI、自建 Agent、   (仅旁白/截图/relay；
    Agent / 模型)               API、CI 里的模型等)        不替代 /audit 编排)
```

### 1. IDE — use the IDE’s built-in model

- Run `Use /audit on <URL>` in **Cursor** or **Claude Code** with whatever model the user already selected in that IDE.
- This repo does **not** ship a separate model config for IDE runs.
- Live board updates when the IDE agent writes `validation/artifacts/<runId>/run-state.json` per [live-run-protocol.md](../.claude/skills/audit/references/live-run-protocol.md).

**Default path for full delivery audits:** IDE + skills + optional `workbench/live/`.

### 2. Terminal — other models allowed

- `audit-run-init.sh`, `audit_capture.py`, `browser-relay.py`, and future CI jobs are **hosts**, not the audit brain.
- A terminal workflow may call **any** model or tool the operator configures (e.g. Codex CLI, `cursor-agent`, custom OpenAI-compatible endpoint), as long as outputs still conform to:
  - `schemas/audit-run.schema.json`
  - `schemas/audit-report.schema.json`
  - artifact layout under `validation/artifacts/<runId>/`
- Scripts in `scripts/` stay deterministic; **non-deterministic reasoning stays in the agent the user wires in**.

### 3. Browser extension — other models allowed (narrow role)

- The extension is **evidence + in-page narration** only — see [browser-extension.md](browser-extension.md).
- It may poll `run-state.json` and optionally call **another model** later (e.g. summarize `activeAnnotation`, translate captions) **without** redefining S0–S4, issue cards, or stage order.
- Full orchestration remains in IDE or terminal agents running `/audit`.

## What must stay the same everywhere

Regardless of model or surface:

1. **Single severity standard** — [severity-standard.md](severity-standard.md)
2. **Single report schema** — `schemas/audit-report.schema.json`
3. **Live state contract** — `schemas/audit-run.schema.json`
4. **No secrets in client** — API keys for optional extension/terminal models belong in env/CI, not in static HTML or the MV3 bundle

## Workbench behavior

| UI | Model |
| --- | --- |
| `workbench/live/` | **None** — reads JSON only; “应用链接” preview does not call an LLM |
| `workbench/report/` | **None** — renders merged `audit-report.json` |

If the user pastes a URL with no live run, the board shows **preview flow** until an IDE or terminal agent updates `run-state.json`.

## Recommended defaults (v0.1)

| Task | Surface | Model |
| --- | --- | --- |
| Full `/audit` + fix packs | IDE | IDE default |
| Headless capture / relay | Terminal | No model required |
| Batch or custom CI audit | Terminal | Operator’s choice; must emit schema JSON |
| On-site narration while auditing | Extension | Optional; default = display `activeAnnotation` from run-state only |

## Related docs

- [extension-optional-llm.md](extension-optional-llm.md) — plugin second-model API (`/api/narrate`, popup config)  
- [vision-and-flow.md](vision-and-flow.md) — product flow and tool boundaries  
- [browser-extension.md](browser-extension.md) — extension vs skills  
- [live-audit-workflow.md](live-audit-workflow.md) — run-state + polling  
- [skill-routing-map.md](skill-routing-map.md) — `/audit` orchestration  
