# /learn Validation Output: TODO CLI

## Context

- Request: Start practical validation of the Engineering Discipline Skills workflow.
- Spec: `validation/spec.md`
- Implementation: Minimal Python TODO CLI in `examples/todo_cli/todo.py`
- Review findings: `validation/review.md`
- Check findings: `validation/check.md`
- Tests/checks: 10 Python unit/CLI tests passed.

## What Went Well

- `/spec` produced a small scope with observable acceptance criteria.
- `/tdd` caught the missing module first, then drove the implementation.
- `/review` found a real behavioral gap after tests were green.
- The review-driven regression test failed before the fix and passed after it.
- `/check` confirmed that skill directories stayed instruction-only and no `scripts/` directory was added.

## What Went Wrong

- The initial test set covered corrupt JSON syntax but not invalid JSON item shape.
- Local git commit validation could not run because `git init` was blocked by the sandbox.
- The repository rules did not define whether validation examples should ship with the skills.

## Surprises

- The adversarial review was useful even on a tiny CLI; it found a meaningful boundary problem.
- The environment blocked local `.git` creation even though the project directory is otherwise writable.

## Root Causes

### Issue: Invalid item shape was not rejected

- What happened: A syntactically valid JSON list containing malformed TODO items could load successfully and fail later.
- Why 1: The first implementation validated only top-level JSON shape.
- Why 2: The spec said corrupt JSON should fail clearly, but did not explicitly separate syntax corruption from schema corruption.
- Why 3: The first test set mapped directly to named acceptance criteria and missed an adjacent boundary condition.
- Actionable root cause: Error-path criteria should include both parse failure and valid-but-invalid data shape when persisted data is user-editable.

### Issue: Validation artifact ownership was ambiguous

- What happened: `examples/`, `tests/`, and `validation/` were useful for proof, but the project rules did not say whether they belonged in the repository.
- Why 1: The original product shape focused on `.claude/skills/`.
- Why 2: The validation method mentioned a TODO CLI but not where proof artifacts should live.
- Why 3: `CLAUDE.md` did not yet distinguish skill payload from validation payload.
- Actionable root cause: Add a rule that validation examples may exist, but must stay outside `.claude/skills/` and must not be required by the skills.

## Guardrail Updates

### `CLAUDE.md` ADR Entry

Added:

```markdown
## ADR: Validation Artifacts Stay Outside Skills

- Date: 2026-05-18
- Status: Accepted
- Context: The practical validation run needed a TODO CLI example, tests, and workflow reports. Those artifacts are useful proof, but they should not make the skills stateful or add runtime requirements to `.claude/skills/`.
- Decision: Validation examples may live in `examples/`, `tests/`, and `validation/`. They must not be placed inside `.claude/skills/`, and the skills must remain usable without them.
- Consequences: The repository can include proof of the workflow while preserving portable, instruction-only skills.
```

Also added a rules bullet:

```markdown
- Validation examples may exist, but they must stay outside `.claude/skills/` and must not be required for skill use.
```

### Skill Reference Update

- Skill: None.
- File: None.
- Change: No skill reference update was needed.
- Reason: The lesson is repository governance, not a reusable skill instruction gap.

## Final Summary

- Outcome: The workflow completed end to end with one review-driven fix and one governance update.
- Remaining risks: Local commit validation remains blocked until Git repository initialization is allowed or a GitHub repository target is provided.
- Follow-ups: Decide whether to upload the full repository including validation proof or only the portable skill payload.
