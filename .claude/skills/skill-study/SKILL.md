---
name: skill-study
description: >
  Study external skill collections, open-source agent workflows, market skill reports,
  course/job trend lists, and competitor tools to extract reusable AgentSkills patterns,
  benchmark labels, validation rubrics, workflow triggers, anti-patterns, and guardrail updates.
  Use when the user asks the agent to learn from other skills, global skill trends,
  repositories, courses, reports, or examples without turning the project into a basic curriculum.
---

# Skill Study

Use this skill to learn from other people's skills without copying them blindly.

The goal is not to collect generic learning topics. The goal is to convert outside examples into better AgentSkills:

```text
external source -> evidence split -> pattern extraction -> workflow upgrade -> validation rule -> guardrail update
```

## Core Rules

- Separate market demand from executable skill design.
- Do not turn broad skills like AI literacy, SQL, or communication into basic course modules.
- Convert trends into agent capabilities, audit checks, workflow triggers, and benchmark criteria.
- Preserve source evidence and confidence.
- Prefer task workflows over topic lists.
- Treat every external skill as inspiration, not authority.
- Avoid copying another repository's text, structure, or prompts verbatim.
- Use `S0-S4` severity if the external pattern exposes delivery or agent-reliability risk.

## Workflow

1. Intake
   - Identify source type: skill repo, agent framework, trend report, course list, job skill list, tool page, case study, or workflow example.
   - Identify the user's purpose: improve current skills, discover new skills, rank examples, update guardrails, or build a benchmark.

2. Evidence pass
   - Record source locator, claim, date if visible, scope, and confidence.
   - Separate what the source proves from what is inferred.

3. Pattern extraction
   - Extract:
     - trigger phrases;
     - task boundaries;
     - workflow stages;
     - validation steps;
     - output artifacts;
     - anti-patterns;
     - reusable references;
     - evidence requirements.
   - Read `references/skill-benchmark-rubric.md` for the extraction rubric.

4. Trend translation
   - If the source is a global skill trend report, translate skills into agent-audit capabilities.
   - Example: `AI literacy` becomes "detect whether a product actually uses AI in a user-visible workflow."
   - Example: `process optimization` becomes "map workflow bottlenecks, duplicate steps, and missing automation."
   - Read `references/market-skill-radar.md` when handling market skill reports.

5. Fit decision
   - Classify each extracted pattern:
     - `ADOPT`: directly improves an existing skill.
     - `ADAPT`: useful after tailoring to this workflow.
     - `REFERENCE`: useful benchmark, no immediate skill change.
     - `REJECT`: too basic, too vague, too tool-specific, or unsupported by evidence.

6. Update proposal
   - Propose the smallest durable change:
     - update a reference checklist;
     - add a new trigger phrase;
     - add a validation row;
     - add an anti-pattern;
     - add a benchmark label;
     - add an ADR if it changes project governance.

7. Output
   - Produce a learning brief with scope, source evidence, extracted patterns, adoption decisions, rejection reasons, regression checks, lessons, and exact file updates.

## Output Format

```markdown
## Skill Study Brief

## Scope

- Source:
- Purpose:
- Skipped:

| Source | Claim | Evidence | Confidence | Decision |
| --- | --- | --- | --- | --- |

## Extracted Patterns

| Pattern | Convert Into | Target Skill | Decision | Reason |
| --- | --- | --- | --- | --- |

## Anti-Patterns

-

## Guardrail Updates

-

## Regression Checks

-

## Lessons

-

## Copyable Update Prompts

1.
```

## Anti-Patterns

- Building a long list of topics with no workflow.
- Treating popular skills as automatically relevant.
- Adding a new AgentSkill for every trend keyword.
- Copying another skill's instructions verbatim.
- Confusing "what humans should learn" with "what this audit agent should do."
- Accepting trend reports without source/date/confidence.
