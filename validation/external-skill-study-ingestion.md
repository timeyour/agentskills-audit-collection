# External Skill Study Ingestion

Date: 2026-05-19

## Purpose

Validate the new `/skill-study` behavior using the user's supplied global skills trend brief.

The goal is not to add basic course modules. The goal is to turn external skill signals into AgentSkills behavior.

## Source Evidence

| Source | Claim Used | Evidence Type | Confidence | Decision |
| --- | --- | --- | --- | --- |
| LinkedIn Skills on the Rise 2025 | AI literacy, LLM application, communication, adaptability, public speaking, stakeholder management, and process optimization are rising skills. | Platform trend report / blog | Medium-high | `ADAPT` |
| World Economic Forum Future of Jobs Report 2025 | Technology, AI/big data, systems thinking, resilience, and green transition shape future work. | Primary global report | High | `ADAPT` |
| Coursera Job Skills Report 2026 | Data, IT, software/product, and generative AI continue to reshape job skills. | Platform skills report | Medium-high | `ADAPT` |

## Extracted Patterns

| Market Pattern | Converted AgentSkills Pattern | Target Skill | Decision |
| --- | --- | --- | --- |
| AI literacy | Audit whether AI claims are visible, useful, explainable, and connected to a real workflow. | `/audit`, `/agent-diagnose` | `ADAPT` |
| LLM application | Map where LLM output enters the product, where failure states appear, and what guardrails exist. | `/flow-test`, `/agent-diagnose` | `ADAPT` |
| Workflow automation | Identify repeated steps, missing integrations, broken handoffs, and copyable automation opportunities. | `/audit`, `/deploy-check` | `ADAPT` |
| Process optimization | Diagnose workflow bottlenecks, unclear ownership, duplicate actions, and missing acceptance criteria. | `/flow-test`, `/accept-five` | `ADAPT` |
| Data analysis | Require metrics, dashboards, claims, and scores to be backed by evidence. | `/audit`, `/visual-qa` | `ADAPT` |
| Communication | Require findings to be located, severity-ranked, concise, and copyable. | All skills | `ADOPT` |
| Adaptability | Retest after new evidence and update guardrails through learning ledgers. | `/accept-five`, `/skill-study` | `ADOPT` |
| Green / industry transition | Add industry-specific risk checks only when the target domain requires them. | `/deploy-check`, `/audit` | `REFERENCE` |

## Rejected Translation

These were rejected because they would turn the repo into a basic curriculum:

- `AI Literacy` as a generic AI fundamentals course.
- `Python Automation` as a beginner programming module.
- `SQL / Dashboard` as a data bootcamp.
- `Public Speaking` as a presentation lesson.
- `Renewable Energy` as a general industry primer.

## Implemented Updates

- Added `.claude/skills/skill-study/SKILL.md`.
- Added `.claude/skills/skill-study/references/skill-benchmark-rubric.md`.
- Added `.claude/skills/skill-study/references/market-skill-radar.md`.
- Updated `README.md` to include `/skill-study`.
- Updated `REQUIREMENTS.md` with the external skill learning requirement.
- Updated `CLAUDE.md` with a governance rule and ADR for external skill learning.

## Guardrail

External skill learning must produce at least one concrete artifact:

- audit check;
- workflow trigger;
- validation row;
- benchmark label;
- copyable prompt;
- guardrail;
- rejection reason.

If it only produces a list of topics, the pass failed.

## Verdict

Verdict: `PASS`

The collection now has a dedicated way to learn from other skills and market trend sources while preserving its core identity: task-oriented, evidence-based, instruction-only AgentSkills.
