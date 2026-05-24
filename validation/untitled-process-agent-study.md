# Untitled PDF Process-Agent Study

Date: 2026-05-20

Source: `/Users/liuxin/Downloads/Untitled.pdf`

## Scope

- Source type: image-heavy PDF, 7 pages.
- Purpose: learn process-agent construction patterns and absorb useful rules into AgentSkills.
- Text extraction: pages 5 and 7 contained selectable text; other pages were reviewed via rendered page images.
- Skipped: exact OCR transcription of every small label; this pass extracts operational patterns, not slide notes.

## Evidence Table

| Page | Visible / extracted evidence | Pattern | Decision |
| --- | --- | --- | --- |
| 1 | New product launch process matrix with product/marketing/sales/GTM style rows and stage columns; notes about information synchronization and organization collaboration. | Business process should be represented as multi-role, multi-node stage matrix. | `ADAPT` into `/harness` stage tree and node mapping. |
| 2 | "From human relay to intelligent-agent driven"; steps include defining problem; each node judgement has structural transformation and automatic sync. | Process-agent value begins with replacing manual context relay. | `ADAPT` into process-agent problem definition. |
| 2 | Step 1 defines problem through Q1 customer/who and Q2 value/what is solved; includes trust-chain and experience-dependence issues. | Start with business bottleneck and user/operator roles before building tools. | `ADOPT` into process-agent lifecycle. |
| 3 | Step 2 defines business flow and data templates; messy manual flow becomes stable templates; first-order value is reducing information gap. | Data templates are the bridge between human know-how and executable agent workflow. | `ADOPT` into `/harness/references/process-agent-pattern.md`. |
| 4 | Step 3 builds complete process agent from business know-how, data construction, and tools; every node needs tool support. | A process agent is not one prompt; it combines know-how, data, and tools per node. | `ADOPT`. |
| 5 | Step 4 iterates and optimizes Agent: collect signals, root-cause diagnosis, simulation, repeat verification. | Process agent needs field signal loop and root-cause verification. | `ADOPT`. |
| 5 | Human capability requirements: business architecture, technical implementation, effect validation. | Harness should make these capabilities explicit to lower talent-density needs. | `ADAPT`. |
| 6 | Best path: package into process agent; produced result is still a process agent. "Define problem -> define business flow/data template -> build process agent -> iterate". | AgentSkills should support process-agent packaging, not only audit reports. | `ADOPT`. |
| 6-7 | Customer question and core pain: high capability threshold, no clear path, fragmented channel information; three values include no need for technical background, reproducible waterline, enterprise brain. | Process-agent value should be measured by reduced knowledge burden and reproducibility. | `REFERENCE`, useful for future product positioning. |
| 7 | User note: split business big steps into layers; some are prompt, some skills, some Dify, some RPA. | Add execution router and multi-layer decomposition. | Already implemented in `/harness`. |

## Extracted Patterns

| Pattern | Convert Into | Target Skill | Decision | Reason |
| --- | --- | --- | --- | --- |
| New product launch process matrix | Stage tree with role/node/stage coordinates. | `/harness` | `ADAPT` | Makes complex business workflows inspectable before automation. |
| Human relay -> agent-driven process | Check for manual context handoffs and auto-sync opportunities. | `/harness`, `/audit` | `ADAPT` | Exposes where AI can reduce coordination load. |
| Define problem before agent | Problem statement with customer, pain, success signal. | `/harness` | `ADOPT` | Prevents tool-first automation. |
| Business flow + data templates | Node map with input/output/data template/evidence. | `/harness` | `ADOPT` | Turns tacit know-how into runnable structure. |
| Know-how + data + tools | Process-agent architecture requirements. | `/harness` | `ADOPT` | Prevents one-agent/one-prompt overreach. |
| Signal -> root cause -> simulation -> verification | Iteration loop after deployment. | `/harness`, `/accept-five` | `ADOPT` | Proves whether repeated failures actually decline. |
| Business architecture + technical implementation + effect validation | Capability checklist. | `/harness` | `ADAPT` | Makes talent requirements explicit. |

## Implemented Updates

- Added `.claude/skills/harness/references/process-agent-pattern.md`.
- Updated `.claude/skills/harness/SKILL.md` to reference process-agent lifecycle and signal loop.
- Updated `README.md` to list the new reference.
- Updated `REQUIREMENTS.md` with the process-agent four-stage lifecycle.
- Updated `PRODUCT.md` with process-agent harness questions.
- Updated `DESIGN.md` with process-agent page questions.
- Updated `CLAUDE.md` with governance rules and ADR.

## New Guardrails

- Do not build a process agent before defining the problem.
- Do not build a process agent before mapping business flow and data templates.
- Do not treat every business node as a prompt.
- Do not let one agent own unrelated failure modes.
- Do not optimize symptoms without a signal/root-cause/verification loop.
- Do not call an iteration successful unless repeated questions, handoff failures, cycle time, or manual corrections decreased.

## Regression Checks

- A `/harness` output for process-agent work must include:
  - problem statement;
  - business flow/node map;
  - data templates;
  - know-how/data/tool split;
  - checkpoints;
  - signal ledger;
  - root-cause log;
  - verification metric.
- If any of those are missing, the plan is incomplete.

## Lessons

This source sharpens the product direction:

```text
AgentSkills is not only an audit system after work is done.
It also needs a harness layer that packages messy human workflows into process agents before work starts.
```

The strongest reusable phrase is:

```text
Do not automate the current mess. First turn the work into a node map, data templates, checkpoints, and a signal loop.
```

## Verdict

Verdict: `PASS`

The PDF adds a concrete process-agent construction pattern to the existing Harness Engineering layer. The project now covers both:

- delivery acceptance after AI-generated work exists;
- process-agent harness planning before complex AI-assisted workflow execution.
