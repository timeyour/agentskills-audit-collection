---
name: flow-test
description: >
  Test every visible function and user workflow in a website, web app, or open-source project.
  Use for live QA: navigation, CTAs, forms, auth, search, upload, checkout, dashboards,
  error states, mobile behavior, expected vs actual results, and issue cards with copyable fixes.
---

# Flow Test

Use this skill to walk a product like a real user.

## Do

1. Inventory every visible feature.
2. Map visible pages, controls, media, documents, auth/payment/upload/admin boundaries, and unknown surfaces before detailed clicking.
3. Determine the permission level before live interaction; production defaults to public read-only or safe navigation unless the user grants a test scope.
4. Execute every safe public workflow.
5. Record expected vs actual behavior.
6. Test edge states: empty input, invalid input, duplicate submit, back/refresh, mobile, auth boundary.
7. Mark unsafe/payment/private/destructive flows as `SKIPPED-SAFE`.
8. Produce issue cards with exact live positions and copyable fix prompts.
9. Use `S0-S4` severity and include reproduction plus regression checks.
10. For multi-step live testing, emit progress updates after each major route, CTA group, form, auth boundary, or blocker.

## Reference

Read `references/live-functional-audit.md` before running the audit.
For long runs, also read `../audit/references/progressive-reporting.md` and use its update format.
For broad website tests, read `../audit/references/web-surface-discovery.md` before clicking.
For any live interaction, read `../audit/references/permission-model.md` and apply its least-privilege levels.

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
