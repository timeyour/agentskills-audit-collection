---
name: accept-five
description: Run five-pass acceptance testing on a website, app, repo, feature, or audit target: baseline, functional, edge/failure, visual/deployment, and retest/experience. Use when one inspection is not enough and repeated findings must become reusable experience.
---

# Accept Five

Use this skill for important audits or releases.

## Passes

1. Baseline: load target, identify product, inventory features, map happy path.
2. Functional: execute safe flows and record expected vs actual.
3. Edge/failure: test invalid, empty, mobile, auth, refresh, loading, and missing-state behavior.
4. Visual/deployment: inspect craft, responsive polish, accessibility, SEO, and production dependencies.
5. Retest/experience: verify blockers, detect repeated patterns, improve prompts, and propose guardrails.
6. Classify findings with `S0-S4` severity and keep reproduction/regression evidence through all passes.

## Reference

Read `references/five-pass-acceptance.md`.

## Output

- Five pass report.
- Issue cards.
- Retest table.
- S0-S4 severity.
- Regression checks.
- Experience ledger.
- Guardrail update proposals.
