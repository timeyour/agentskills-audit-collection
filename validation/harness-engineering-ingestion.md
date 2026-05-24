# Harness Engineering Ingestion

Date: 2026-05-19

Source: `SS-lec3 FDE course materials (local PDF, not in repo)`

Note: The WeType cache image paths supplied in the message were unavailable in this environment, so this pass used the user's text plus PDF text extraction.

## Purpose

Convert the user's Harness Engineering insight into AgentSkills architecture.

The key addition is that AI product delivery needs an execution harness before audit:

```text
business objective -> multi-level decomposition -> execution routing -> checkpoints -> retry/escalation -> human intervention -> acceptance
```

## Source Evidence From PDF

| Page | Extracted signal | Pattern adopted |
| --- | --- | --- |
| 4 | FDE fills the gap between product capability and customer reality; FDE enters the most critical, chaotic, urgent problem. | AgentSkills should not stay at prompt level; it needs workflow-grounded delivery. |
| 6-8 | AI era shifts weight from technology toward demand; users/customers/PM/design/sales/engineering need a bridge. | Start from business process and demand translation before tool choice. |
| 27 | Practical layer, tool layer, organization layer; product/design/engineering/AI recipe. | Execution units may map to different modes, not one universal tool. |
| 33 | Echo + Delta: demand discovery/communication/translation plus build/iterate/deploy. | `/harness` separates discovery/translation from execution/deployment. |
| 38 | 721 allocation and dynamic adjustment based on demand shape. | Harness plans should route effort dynamically and expose allocation choices. |
| 40 | Enter factory, understand real workflow, build PoC, collaborate continuously, iterate with high-frequency feedback. | Add checkpoints, feedback loops, and retest rather than one-shot output. |
| 41 | Enter organization,梳理 workflow, Target Engineering, build full training/service loop, long-term onsite optimization. | Harness becomes the operational bridge from business steps to repeatable automation. |
| 47 | Everyone should have FDE thinking in AI era. | The repo should teach agents to think like delivery engineers, not only code generators. |

## User Insight Adopted

The user added:

- automatic checkpoints;
- human intervention;
- retry strategy;
- decomposition by business stages;
- multi-layer decomposition;
- execution modes including prompt, skills, Dify, and RPA.

This is accepted as a core architecture layer.

## Implemented Skill

Added:

- `.claude/skills/harness/SKILL.md`
- `.claude/skills/harness/references/business-decomposition.md`
- `.claude/skills/harness/references/execution-router.md`
- `.claude/skills/harness/references/checkpoint-retry-policy.md`

## Harness Output Standard

Every complex workflow can now produce:

1. Harness summary.
2. Stage tree.
3. Execution matrix.
4. Checkpoint table.
5. Retry and escalation table.
6. Human-intervention map.
7. Acceptance handoff.

## Execution Modes

| Mode | Role |
| --- | --- |
| `PROMPT` | One-off reasoning, drafting, classification, or low-risk transformation. |
| `SKILL` | Repeatable AgentSkills workflow. |
| `DIFY` | Structured LLM workflow, API chain, knowledge base, or business automation. |
| `RPA` | UI-only repetitive process when no API or stable integration exists. |
| `CODE` | Deterministic transform, parser, validation, integration, or test. |
| `HUMAN` | Judgment, approval, credential, payment, legal/privacy, brand, or irreversible decision. |
| `EXTERNAL` | SaaS/API/platform step outside direct agent control. |

## Guardrail

Do not choose a tool before mapping the business process.

Bad:

```text
Use Dify/RPA/skills to automate this.
```

Good:

```text
Split the business objective into stages and execution units. For each unit, choose the mode, evidence, checkpoint, retry rule, fallback, and human escalation.
```

## Verdict

Verdict: `PASS`

`/harness` fills the missing layer between external learning and audit execution. The collection now has:

```text
skill-study -> harness -> audit -> flow-test / visual-qa / deploy-check -> accept-five -> agent-diagnose
```

This makes the system closer to engineering delivery practice: enter the real workflow, decompose the messy process, build the smallest reliable path, checkpoint automatically, escalate to humans where needed, retry safely, and only then accept or scale.
