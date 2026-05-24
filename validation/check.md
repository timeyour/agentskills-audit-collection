# /check Validation Output: Engineering Discipline Skills

Historical validation artifact. The `/spec`, `/tdd`, `/review`, `/check`, and `/learn` names below describe the validation sequence used when this report was produced; they are not part of the current shipped `.claude/skills/` set unless explicitly listed in `README.md`.

## Rules Loaded

- Rule count: 9 explicit repository rules plus 2 accepted ADRs.
- Sources: `CLAUDE.md`, supported by nearby skill structure.
- Missing or ambiguous rules:
  - No rule currently states whether validation examples should ship with the skills collection or remain temporary.

Loaded rules:

- Use `/spec`, `/tdd`, `/review`, `/check`, and `/learn` in sequence for this validation.
- Skills are stateless.
- Skills must stay instruction-only unless a future ADR allows scripts.
- `CLAUDE.md` is the governance source.
- References belong in each skill's `references/` directory.
- Skill bodies should stay concise.
- Maintain adversarial posture.
- Do not skip verification for simple changes.
- Guardrails must be specific, triggerable, and reviewable.

## Architecture

- `BLOCKER`: None.
- `WARNING`: None.
- `NOTE`: Validation code is isolated under `examples/`, `tests/`, and `validation/`, outside `.claude/skills/`.

Evidence:

```text
find .claude/skills -type d -name scripts
<no output>
```

```text
.claude/skills/
  spec/SKILL.md + references/spec-template.md
  tdd/SKILL.md + references/commit-checklist.md
  review/SKILL.md + references/adversarial-checklist.md
  check/SKILL.md + references/rules-reference.md
  learn/SKILL.md + references/retro-template.md
```

## Convention

- `BLOCKER`: None.
- `WARNING`: None.
- `NOTE`: Each `SKILL.md` has required frontmatter with `name` and `description`.

Evidence:

```text
name: spec
name: tdd
name: review
name: check
name: learn
```

## Tech Debt

- `BLOCKER`: None.
- `WARNING`: None.
- `NOTE`: Searches for `TODO`, `FIXME`, and `HACK` found domain text such as "TODO CLI", not debt markers.

## Verification

Command:

```bash
python3 -m unittest discover -s tests
```

Result:

```text
Ran 10 tests
OK
```

## Summary

- Overall status: PASS WITH WARNINGS.
- Required fixes: None.
- Recommended follow-ups:
  - Decide whether `examples/`, `tests/`, and `validation/` should be included in the GitHub upload or kept as local proof only.
  - Initialize a Git repository or provide a GitHub target to complete the commit/upload portion.
- Checks run:
  - Skill tree inspection.
  - Script-directory check.
  - Frontmatter check.
  - TODO/FIXME/HACK search.
  - Python unit test suite.
