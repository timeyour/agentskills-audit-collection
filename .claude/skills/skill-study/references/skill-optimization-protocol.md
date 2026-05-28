# Skill Optimization Protocol

Use this reference when improving an existing `SKILL.md`, skill description, or skill reference file from execution evidence.

This protocol is inspired by source-linked research on treating skill documents as trainable external state for frozen agents, including SkillOpt. It is not a claim that this repository implements the full SkillOpt optimizer.

## Core Idea

Do not rewrite skills because a new idea sounds good. Improve skills only when a validation gate shows that the change improves task behavior.

```text
task traces -> proposed bounded edit -> held-out validation gate -> accept or reject -> lessons ledger
```

## Optimization Rules

1. Keep the target model and task harness stable while evaluating a skill edit.
2. Change only a small bounded part of the skill at a time.
3. Prefer add/delete/replace edits over full rewrites.
4. Accept only edits that strictly improve held-out validation behavior.
5. Reject ties. A change that only feels nicer is not enough.
6. Preserve slow-state sections unless the evidence proves they are the problem.
7. Store rejected edits as negative feedback so the same direction is not retried blindly.

## Edit Budget

Treat text changes like a learning rate.

| Edit Size | Use When | Risk |
| --- | --- | --- |
| 1-3 small edits | Tight bugfix, typo, broken route, missing trigger phrase. | May underfit if the failure is structural. |
| 4-8 bounded edits | Normal skill optimization pass. | Preferred range for most skill updates. |
| 9+ edits | Major redesign or new skill architecture. | High risk; requires stronger validation and a separate PR. |

If the proposed diff touches multiple concepts, split it into separate optimization passes.

## Validation Gate

Every skill edit needs a gate.

Minimum gate:

```text
before behavior:
after behavior:
test task:
held-out task:
accepted because:
rejected because:
```

Good gates:

- Same task, improved evidence quality.
- Same task, fewer hallucinated claims.
- Same task, better routing from description.
- Held-out task, same or better output quality.
- No regression in source/live/physical evidence labeling.

Bad gates:

- The new wording sounds more advanced.
- The skill file is longer.
- The average score improves but the affected skill gets worse.
- The edit helps one demo but breaks the general trigger.

## Description vs Body

Skill routing and skill execution are different layers.

| Layer | Reader | Failure Mode |
| --- | --- | --- |
| `description` frontmatter | Router / skill selector | Skill is not activated, or activates for the wrong task. |
| Markdown body | Agent after activation | Skill activates but performs the wrong workflow. |

Test both:

- Routing test: does the description activate the right skill for a realistic user request?
- Execution test: after activation, does the body produce the expected workflow and evidence?

Do not judge a skill only by overall corpus accuracy. Track per-skill effect size, especially for edited descriptions.

## Fast and Slow State

Protect stable policy from fast learning.

| State | Examples | Update Rule |
| --- | --- | --- |
| Slow state | Core workflow, severity scale, permission rules, evidence taxonomy. | Edit rarely, with strong evidence and review. |
| Fast state | Examples, lessons ledger, recent corrections, task-specific candidate prompts. | Edit often, but keep scoped and reversible. |

Fast edits must not overwrite slow-state invariants such as:

- source/live/physical evidence separation;
- S0-S4 delivery severity;
- least-privilege live testing;
- no risky production actions without explicit permission;
- candidate materials must not become case studies without validation.

## Skill Edit Proposal Format

Use this when proposing a skill optimization:

```text
Skill:
Current failure:
Evidence:
Proposed bounded edit:
Edit count:
Protected sections:
Validation task:
Held-out task:
Acceptance threshold:
Rollback plan:
Decision: accept / reject / needs more evidence
```

## Anti-Patterns

- Accepting most self-proposed edits.
- Rewriting a skill from scratch after one failure.
- Making broad style changes without a validation gate.
- Optimizing for a single demo and breaking general use.
- Letting fast lessons overwrite governance rules.
- Treating source-reported benchmark numbers as locally reproduced results.
- Expanding skills until the high-signal workflow is buried.
