# Regression Lessons Ledger

Every completed physical test should produce reusable lessons. Lessons are not vague reminders; they are triggerable guardrails for future runs.

## Lesson Categories

- Locator stability.
- Authentication and session setup.
- Network dependency and third-party script behavior.
- Timeout and retry boundaries.
- Mobile viewport behavior.
- File upload, export, and download handling.
- Destructive action safe-skip handling.
- Environment variable and secret handling.
- Artifact redaction and retention.

## Lesson Format

```text
Lesson:
Trigger:
Evidence:
Rule:
Regression Check:
Where To Store:
```

## Example

```text
Lesson: Marketing CTA must be tested with real browser execution when it loads third-party tracking scripts.
Trigger: CTA flow includes analytics, ads, tag managers, or embedded widgets.
Evidence: Trace showed content ready at 1.1s but load blocked for 27s by a third-party script.
Rule: Separate content readiness from full load and report third-party blocking as S2 when conversion is affected.
Regression Check: Add Playwright assertion for CTA visibility before full load plus network timing review.
Where To Store: CLAUDE.md if project-wide, or physical-flow-test reference if reusable across projects.
```

## Promotion Rule

Promote a lesson into `CLAUDE.md` or a skill reference when:

- It recurs across more than one flow.
- It prevents an S0 or S1 issue.
- It changes how future tests should be generated.
- It clarifies safety boundaries for production actions.
