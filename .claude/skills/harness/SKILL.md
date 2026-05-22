---
name: harness
description: >
  Build an engineering delivery harness for AI-assisted work: decompose business goals
  into multi-level steps, route each step to prompt, AgentSkill, Dify workflow, RPA,
  code, manual human intervention, or external tool, and define automatic checkpoints,
  retry strategy, escalation paths, evidence gates, and acceptance criteria.
  Use before implementing, auditing, or operationalizing a complex workflow.
---

# Harness

Use this skill to turn a messy business objective into an executable delivery harness.

The goal is to prevent AI work from becoming one giant prompt. Break the work into business stages, substeps, execution units, checkpoints, retries, and human decision points.

```text
business objective -> stage tree -> execution router -> checkpoints -> retries/escalations -> acceptance harness
```

## Core Rules

- Start from the business process, not from the tool.
- Decompose in layers until each unit has one clear owner, input, output, tool mode, checkpoint, and retry rule.
- Route each unit to the right execution mode: prompt, AgentSkill, Dify workflow, RPA, code task, manual human decision, or external system.
- Insert automatic checkpoints after every unit that can fail silently.
- Insert human checkpoints where judgment, permissions, money, private data, or irreversible actions appear.
- Define retry limits and escalation paths before execution.
- Keep source evidence, live evidence, tool evidence, and human decisions separate.
- Feed final outputs into `/audit`, `/flow-test`, `/deploy-check`, or `/accept-five` for verification.

## Workflow

1. Scope the objective
   - Name the business goal.
   - Identify user/customer, operator, system, and decision owner.
   - Define done, blocked, and out-of-scope.

2. Build the stage tree
   - Split into business stages.
   - Split each stage into substeps.
   - Continue until each unit is small enough to execute and verify independently.
   - Use `references/business-decomposition.md`.
   - If the goal is to convert a manual business process into a process agent, also use `references/process-agent-pattern.md`.

3. Route execution modes
   - Choose the lightest reliable mode for each unit:
     - `PROMPT`: one-off reasoning or drafting.
     - `SKILL`: repeatable agent workflow.
     - `DIFY`: structured multi-step LLM workflow, API chain, or business automation.
     - `RPA`: brittle UI-only workflow with no API or direct integration.
     - `CODE`: deterministic transform, parser, test, or integration.
     - `HUMAN`: judgment, approval, credential entry, payment, legal, brand, or safety decision.
     - `EXTERNAL`: SaaS/API/platform action outside the agent.
   - Use `references/execution-router.md`.

4. Add checkpoints
   - Define automatic checkpoint after each unit.
   - Define human checkpoint before irreversible, private, paid, or high-judgment actions.
   - Each checkpoint needs expected evidence, pass/fail condition, and owner.
   - For process agents, add a signal ledger and iteration loop: collect signals, diagnose root cause, test change, verify reduction.

5. Add retry and escalation
   - Define retryable failures, retry count, backoff, fallback mode, and escalation owner.
   - Never retry destructive actions blindly.
   - Use `references/checkpoint-retry-policy.md`.

6. Output the harness
   - Produce stage tree, execution matrix, checkpoint table, retry table, human-intervention map, risk register, and acceptance handoff.
   - For process-agent work, also produce lifecycle and signal/iteration tables.

7. Verify the harness
   - Run `/audit` for overall readiness.
   - Run `/flow-test` for user-visible workflows.
   - Run `/deploy-check` for production dependencies.
   - Run `/accept-five` for important workflows.

## Output Format

```markdown
## Harness Summary

- Business goal:
- Scope:
- Done:
- Out of scope:
- Main risk:

## Stage Tree

| Level | Stage | Step | Input | Output | Owner | Dependency |
| --- | --- | --- | --- | --- | --- | --- |

## Execution Matrix

| Step | Mode | Why this mode | Tool/Skill/Workflow | Evidence | Fallback |
| --- | --- | --- | --- | --- | --- |

## Checkpoints

| Step | Checkpoint | Automatic/Human | Pass condition | Fail condition | Evidence | Owner |
| --- | --- | --- | --- | --- | --- | --- |

## Retry And Escalation

| Failure | Retryable | Retry limit | Backoff/Fallback | Human escalation | Stop condition |
| --- | --- | --- | --- | --- | --- |

## Acceptance Handoff

| Target | Next skill | What to verify |
| --- | --- | --- |

## Process Agent Lifecycle

| Stage | Business Question | Output | Checkpoint | Owner |
| --- | --- | --- | --- | --- |

## Signal And Iteration Loop

| Signal | Root Cause | Change Tried | Verification | Result |
| --- | --- | --- | --- | --- |
```

## Anti-Patterns

- One giant prompt for a multi-stage business process.
- Choosing Dify, RPA, or skills before mapping the business steps.
- No checkpoint between AI output and real-world action.
- Retrying the same bad prompt without changing input, context, or mode.
- Building a process agent before defining the business flow and data templates.
- Optimizing symptoms instead of diagnosing root causes from repeated signals.
- Treating RPA as robust when an API or deterministic code path exists.
- Letting the agent approve its own high-risk action.
- Hiding manual steps instead of marking them as human checkpoints.
