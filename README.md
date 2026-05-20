# AgentSkills Audit Collection

A task-oriented Claude Code AgentSkills collection for auditing websites, web apps, open-source projects, and AI-built products.

See [REQUIREMENTS.md](REQUIREMENTS.md) for the purpose and success criteria behind the collection.
See [PRODUCT.md](PRODUCT.md) and [DESIGN.md](DESIGN.md) for the product direction and design principles.

## Positioning

AgentSkills is an acceptance and audit system for AI-generated websites and products.

It turns vibe-coded results from "looks done" into engineering delivery assets that are tested step by step, reproducible, risk-aware, fixable, retestable, and reusable.

This is not a coding skill pack. It is closer to:

```text
QA department + acceptance workflow + risk audit + retrospective memory
```

## Workflow

```text
skill-study
    ↓
harness
    ↓
audit
    ↓
flow-test / visual-qa / deploy-check
    ↓
accept-five
    ↓
agent-diagnose
    ↓
rules memory / benchmark library
```

`/skill-study` is the external-learning entry point. `/harness` is the engineering delivery harness that decomposes business work and routes execution modes. `/audit` is the audit orchestrator. The other skills are focused task tools that can be called directly when a narrower pass is needed.

## Skills

- `/audit`: run the end-to-end website/product audit workflow.
- `/skill-study`: learn from external skills, repositories, market skill reports, and competitor workflows without turning the collection into a basic curriculum.
- `/harness`: decompose business goals into multi-level execution steps with prompt/skill/Dify/RPA/code/human routing, checkpoints, retries, and escalation.
- `/flow-test`: test every visible feature and user workflow.
- `/visual-qa`: audit visual craft, product taste, layout, responsive behavior, and AI slop.
- `/deploy-check`: inspect production readiness and missing runtime dependencies.
- `/accept-five`: run five-pass acceptance and accumulate lessons.
- `/agent-diagnose`: adversarially diagnose AI agent and workflow failure modes.

## Structure

```text
.claude/skills/
  audit/SKILL.md
  audit/references/source-evidence.md
  audit/references/deployment-readiness.md
  audit/references/report-format.md
  audit/references/live-functional-audit.md
  audit/references/webpage-audit-rubric.md
  audit/references/aesthetic-quality-audit.md
  audit/references/five-pass-acceptance.md
  skill-study/SKILL.md
  skill-study/references/skill-benchmark-rubric.md
  skill-study/references/market-skill-radar.md
  harness/SKILL.md
  harness/references/business-decomposition.md
  harness/references/execution-router.md
  harness/references/checkpoint-retry-policy.md
  harness/references/process-agent-pattern.md
  flow-test/SKILL.md
  visual-qa/SKILL.md
  deploy-check/SKILL.md
  accept-five/SKILL.md
  agent-diagnose/SKILL.md
CLAUDE.md
PRODUCT.md
DESIGN.md
examples/todo_cli/       # validation sample, outside the skills payload
tests/                   # validation tests
validation/              # workflow proof artifacts
```

## Design Principles

- Instruction-only skills: no bundled scripts.
- `CLAUDE.md` is the governance source of truth.
- Each skill is task-oriented, stateless, and independently callable.
- Skill names describe real jobs, not basic curriculum.
- The agent should stay skeptical of source claims, weak evidence, broken workflows, visual slop, and deployment theater.
- External skills and trend reports are converted into audit checks, workflow triggers, benchmark labels, and guardrails, not copied as topic lists.
- Every skill must produce evidence that another person can understand, reproduce, fix, and retest.
- If a skill only produces polished command names or vague opinions, it failed.
- Complex workflows must be decomposed into business stages and execution units before choosing prompt, skill, Dify, RPA, code, or human intervention.
- Automatic checkpoints, retry limits, fallbacks, and human escalation rules belong in the plan before execution starts.

## Unified Output Shape

Every skill should preserve this shape when applicable:

```text
1. Scope
2. Evidence
3. Findings
4. Severity
5. Reproduction
6. Fix Suggestion
7. Regression Check
8. Lessons
```

## Severity Scale

| Level | Meaning |
| --- | --- |
| `S0` | Blocks launch or delivery; core workflow unavailable, data/security risk, or production dependency missing. |
| `S1` | Seriously hurts conversion, trust, correctness, privacy, or operational reliability. |
| `S2` | Noticeable UX, workflow, visual, accessibility, or deployment issue; temporary launch possible with known risk. |
| `S3` | Polish, copy, layout, or minor interaction improvement. |
| `S4` | Future enhancement or benchmark idea. |

## Validation

This repository includes completed validation runs under `validation/`, backed by a sample TODO CLI, batch case reviews for vibe-coded website examples, a global 200-site source-level audit batch, and a five-pass audit of `impeccable.style`.
