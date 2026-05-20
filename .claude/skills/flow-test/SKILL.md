---
name: flow-test
description: Test every visible function and user workflow in a website, web app, or open-source project. Use for live QA: navigation, CTAs, forms, auth, search, upload, checkout, dashboards, error states, mobile behavior, expected vs actual results, and issue cards with copyable fixes.
---

# Flow Test

Use this skill to walk a product like a real user.

## Do

1. Inventory every visible feature.
2. Execute every safe public workflow.
3. Record expected vs actual behavior.
4. Test edge states: empty input, invalid input, duplicate submit, back/refresh, mobile, auth boundary.
5. Mark unsafe/payment/private/destructive flows as `SKIPPED-SAFE`.
6. Produce issue cards with exact live positions and copyable fix prompts.
7. Use `S0-S4` severity and include reproduction plus regression checks.

## Reference

Read `references/live-functional-audit.md` before running the audit.

## Output

- Feature inventory.
- Flow execution log.
- Edge/failure table.
- S0-S4 severity.
- Reproduction steps.
- Issue cards.
- Copyable fix pack.
- Regression checks.
- Lessons.
- Final verdict.
