# Market Skill Radar

Use this reference when a source discusses labor-market, course, or global skill trends.

The purpose is to translate market skills into AgentSkills capabilities.

## Trend-To-Agent Translation

| Market skill trend | Do not turn into | Convert into AgentSkill capability |
| --- | --- | --- |
| AI literacy | A generic AI basics course | Check whether AI claims are visible, useful, explainable, and connected to a real workflow. |
| LLM application | Prompt trivia | Audit how LLM output enters product flows, where failure states appear, and what guardrails exist. |
| Workflow automation | Tool list | Map repetitive steps, missing automation, broken handoffs, and copyable automation opportunities. |
| Process optimization | Productivity slogans | Diagnose workflow bottlenecks, duplicate steps, unclear ownership, and missing acceptance criteria. |
| Data analysis | SQL curriculum | Check whether product claims, metrics, dashboards, and decisions are backed by evidence. |
| Software/product skills | Framework shopping | Inspect product loop, feature completeness, deployment dependencies, and user outcomes. |
| Communication | Presentation tips | Require findings to be clear, located, severity-ranked, and copyable. |
| Stakeholder management | Meeting advice | Identify who owns each issue, who is blocked, and what decision is needed. |
| Adaptability | Motivation copy | Add retest loops, learning ledgers, and guardrail updates after new evidence appears. |
| Critical thinking | Generic skepticism | Separate source claims, live evidence, inference, and unknowns. |
| Green / industry transition | Broad industry trend | Add industry-specific compliance, operational, sustainability, or domain-risk checks when relevant. |

## Priority Lanes

For this repository, trend signals map into these lanes:

1. `AI + workflow`: AI claims, LLM features, automation, prompt-to-output products.
2. `Data + proof`: metrics, dashboards, scoring, analytics, evidence-backed recommendations.
3. `Product + deployment`: complete workflows, auth, database, storage, email, CMS, monitoring.
4. `Communication + action`: issue cards, one-click-copy prompts, owner/decision clarity.
5. `Industry context`: vertical-specific constraints such as healthcare, finance, education, energy, logistics, or local services.

## Source Confidence

Use these labels:

- `HIGH`: primary report/source page with date, methodology, and clear claims.
- `MEDIUM`: platform blog, community source, or summary with partial methodology.
- `LOW`: social post, unsourced list, or ambiguous screenshot.

## Output Rule

Every trend ingestion must produce at least one of:

- a new audit check;
- a benchmark label;
- a guardrail;
- a copyable prompt;
- a validation row;
- a rejection reason.

If it only produces a list of topics, it failed.
