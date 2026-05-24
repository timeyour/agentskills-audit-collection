# /spec Validation Output: TODO CLI

## Problem

- User/problem statement: Validate that the Engineering Discipline Skills workflow produces structured, actionable outputs on a real implementation task.
- Current behavior: The repository contains the skills collection but no executed proof that `/spec -> /tdd -> /review -> /check -> /learn` works end to end.
- Desired observable behavior: A small TODO CLI exists with tests, and each skill produces a concrete validation artifact.
- Evidence or context: The collection's README names TODO list CLI as the validation example.

## Solution

- Proposed approach: Build a minimal Python standard-library TODO CLI with testable pure functions and a CLI entrypoint.
- Smallest viable change: Support `add`, `list`, and `done` over a JSON file path supplied by `--file`.
- Alternatives considered: A shell script or Node CLI; Python is chosen because it needs no dependency install.
- Assumptions: The validation code can live outside `.claude/skills/`; the "no scripts" rule only applies to bundled skill implementation.

## Scope

- In scope:
  - `examples/todo_cli/todo.py`
  - `tests/test_todo_cli.py`
  - Validation notes under `validation/`
- Out of scope:
  - Packaging, installation, sync, deletion, priorities, due dates, or interactive UI.
  - Adding scripts inside any skill directory.
- Blast radius: Low; validation artifacts only.
- Files/modules likely touched: README/CLAUDE may be updated only if `/learn` finds a durable guardrail gap.

## Constraints

- Must not change: Existing skill command names or skill directory structure.
- Compatibility: Python 3 standard library only.
- Performance: TODO file is small; no optimization needed.
- Security/privacy: CLI must only read/write the explicitly provided file path.
- Data/migration: JSON file should be initialized if missing.
- Existing rules from `CLAUDE.md`: Use `/spec`, `/tdd`, `/review`, `/check`, `/learn`; keep skills stateless and instruction-only.

## Acceptance Criteria

- Happy path:
  - `add` stores a pending item and prints its id.
  - `list` shows pending/done state and titles.
  - `done` marks an existing item complete.
- Edge cases:
  - Empty titles are rejected.
  - Marking a missing id returns a non-zero CLI exit.
  - Missing JSON file behaves as an empty TODO list.
- Error paths:
  - Corrupt JSON returns a clear error rather than silently overwriting data.
- Regression coverage:
  - Unit tests cover store loading, add, list formatting, done, missing id, and corrupt JSON.
- Manual verification:
  - Run CLI commands against a temporary JSON file.

## Risks

- Behavioral risks: CLI and pure functions can diverge if tests only cover one layer.
- Architecture risks: Validation code could clutter the skill collection if not isolated.
- Test gaps: CLI subprocess behavior may need a smoke test beyond pure functions.
- Rollback or mitigation: Remove `examples/`, `tests/`, and `validation/` if validation artifacts should not ship.
