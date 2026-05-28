---
name: accept-five
description: >
  Run five-pass acceptance testing on a website, app, repo, feature, or audit target:
  baseline, functional, edge/failure, visual/deployment, and retest/experience.
  Use when one inspection is not enough and repeated findings must become reusable experience.
---

# Accept Five

Use this skill for important audits or releases.

## Passes

1. Baseline: load target, identify product, inventory features, map happy path.
2. Functional: execute safe flows and record expected vs actual.
3. Edge/failure: test invalid, empty, mobile, auth, refresh, loading, and missing-state behavior.
4. Visual/deployment/product-pattern: inspect craft, responsive polish, accessibility, SEO, production dependencies, and product-pattern fit.
5. Retest/experience: verify blockers, detect repeated patterns, improve prompts, and propose guardrails.
6. Classify findings with `S0-S4` severity and keep reproduction/regression evidence through all passes.
7. Use progressive reporting after every pass, and use the permission model before any live or authenticated action.
8. In the final pass, decide whether lessons stay in the validation report, become a skill-reference update, or deserve promotion to `CLAUDE.md`. Use `docs/roadmap/self-evolving-audit-engine.md` as the roadmap for this decision.
9. If a lesson proposes changing a skill file, apply `../skill-study/references/skill-optimization-protocol.md`: bounded edit, protected slow-state sections, routing test, execution test, and strict validation gate.

## Reference

Read `references/five-pass-acceptance.md`.
For website/app targets, also read `../audit/references/web-surface-discovery.md`, `../audit/references/permission-model.md`, and `../audit/references/progressive-reporting.md`.
For product-pattern or conversion-readiness questions, consult `../ai-product-audit/references/product-pattern-rubric.md`.
For repeated lessons or self-improvement proposals, consult `../../../docs/roadmap/self-evolving-audit-engine.md`.
For skill-edit proposals, consult `../skill-study/references/skill-optimization-protocol.md`.

## Output

- Five pass report.
- Issue cards.
- Retest table.
- S0-S4 severity.
- Regression checks.
- Experience ledger.
- Guardrail update proposals.
