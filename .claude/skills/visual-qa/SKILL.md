---
name: visual-qa
description: Audit visual quality, aesthetic craft, UI consistency, layout, responsive behavior, typography, spacing, trust signals, and AI slop patterns in a website, app, screenshot, or generated UI.
---

# Visual QA

Use this skill when the user wants to know whether a page feels designed, credible, consistent, and conversion-ready.

## Do

1. Identify product category and intended user scenario.
2. Inspect first viewport, hierarchy, spacing, typography, color, imagery, components, and responsive behavior.
3. Inventory visible media, document links, embeds, and product screenshots when they affect trust or layout.
4. Flag AI slop: generic gradients, repeated icon cards, fake proof, vague copy, mismatched components, irrelevant imagery.
5. Separate screenshot-backed findings from source-only findings.
6. Compare against the right product pattern: local service, SaaS, portfolio, directory, dashboard, lifestyle commerce, etc.
7. Produce section-level issue cards and copyable design-fix prompts.
8. Use `S0-S4` severity and include regression checks for visual fixes.
9. For multi-section reviews, emit progress updates after each major page section or viewport group.

## References

- `references/aesthetic-quality-audit.md`
- `references/webpage-audit-rubric.md`
- `../audit/references/progressive-reporting.md` for long visual audits
- `../audit/references/web-surface-discovery.md` when media, documents, or embeds need inventory

## Output

- Aesthetic audit summary.
- Visual score with evidence level.
- Pattern fit table.
- AI slop signals.
- S0-S4 severity.
- Issue cards.
- Copyable fix pack.
- Regression checks.
- Lessons.
