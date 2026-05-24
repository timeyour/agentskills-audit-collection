---
name: ai-product-audit
description: >
  Audit AI-generated products for product-pattern fit, scenario clarity,
  conversion readiness, and business outcome alignment. Use when the user wants
  to know whether a page prepares the user for the right scenario, moves them
  toward a concrete outcome, and converts inspiration into action.
---

# AI Product Audit

Use this skill to diagnose whether an AI-built product follows proven product patterns and converts inspiration into action.

```text
product category + scenario -> pattern matching -> scenario audit -> conversion surface audit -> business reality check -> issue cards -> regression check -> lessons
```

This skill must not judge a product by visual polish alone. It asks whether the page prepares the user for a believable next step and provides a path to reach it.

## When To Use

1. The target is a lifestyle, service, commerce, creator, SaaS, portfolio, directory, or dashboard product.
2. `/audit` or `/visual-qa` flags a pattern mismatch or vague value proposition.
3. The user wants to know whether the page converts inspiration into action.
4. Batch-auditing multiple sites for product-pattern fitness.
5. Before declaring a page "conversion-ready" or "shippable."

## Core Rules

1. Separate product-pattern evidence from visual evidence — a polished page can still have a broken scenario.
2. Compare against the proven pattern for the product category, not personal taste.
3. Every finding needs three things: expected pattern, observed gap, and business risk.
4. Use S0-S4 severity mapped to delivery and conversion risk, not subjective preference.
5. Preserve the shared output shape: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons.
6. For batch audits, emit a summary table first, then progressive per-site details.
7. Mark payment, irreversible submission, and production mutation as `SKIPPED-SAFE` unless explicitly allowed.
8. Never claim a product "understands its user" without citing a specific page element and its failure.

## Workflow

1. **Intake and scope**: identify product category, intended scenario, business outcome, conversion surfaces, and audit depth.
   - Use `references/product-pattern-rubric.md` for the full dimension list.
   - Use `references/category-pattern-catalog.md` for category-specific pattern expectations.

2. **Surface and pattern check**: discover the visible page surface; compare each page against its category pattern.
   - Apply the permission model before any click, form fill, or authenticated action.
   - Mark pages or flows that cannot be safely tested as `SKIPPED-SAFE`.

3. **Scenario audit**: ask the four Viba-inspired questions for each key page:
   - What scenario is this page preparing the user for?
   - What self-image, business outcome, or action does it help the user move toward?
   - Can the user see themselves in the next step?
   - Is the page only inspiration, or does it convert inspiration into action?

4. **Conversion surface audit**: for each identified CTA, form, booking flow, checkout, or signup path:
   - Is the primary CTA specific and actionable?
   - Does the page contain a working conversion surface (not just a brochure)?
   - Is there a visible path from inspiration to action in fewer than 3 clicks?

5. **Business reality check**: distinguish real products from templates.
   - Is there operational depth (backend, database, CMS, auth, content system)?
   - Is there a monetization path or demonstrated usage?
   - Does the evidence (source, live, or physical) support a real business claim?

6. **Evidence assembly and output**: produce issue cards, pattern-fit table, and copyable fix prompts.
   - Use the shared output shape for every finding.
   - Include a Pattern Fit table and a Scenario Audit table.
   - Bundle fix prompts so the user can copy them directly into Claude Code, Lovable, v0, or Bol.

7. **Regression and lessons**: convert repeated pattern failures into guardrail updates or benchmark labels.
   - Propose updates to `CLAUDE.md` only when the pattern appears in 3+ audits with clear evidence.
   - Append lessons to the audit ledger in `validation/` for future five-pass reviews.

## References

- `references/product-pattern-rubric.md`
- `references/category-pattern-catalog.md`
- `../audit/references/progressive-reporting.md` (for batch audits and multi-step runs)
- `../visual-qa/references/aesthetic-quality-audit.md` (for pattern reference and AI slop signals)
- `../audit/references/permission-model.md` (before any live or authenticated action)

## Output Format

```text
AI Product-Pattern Audit Summary
Target:
Product Category:
Intended Scenario:
Pattern Fit Score:
Main Business Risk:
Fix First:

Pattern Fit Table
| Expected Pattern | Observed | Gap | Risk | S0-S4 |
| --- | --- | --- | --- | --- |

Scenario Audit
| Question | Answer | Evidence | Risk |
| --- | --- | --- | --- |

Conversion Surface Map
| Surface | Present | Actionable | Evidence |
| --- | --- | --- | --- |

Business Reality
| Signal | Present | Evidence |
| --- | --- | --- |

Issue Cards
<S0-S4> - <Product Pattern Issue>
- Area:
- URL:
- Live position:
- Expected pattern:
- Observed:
- Business risk:
- Fix:
- Copy prompt:
- Regression check:

Copyable Fix Pack
1. <ready-to-copy prompt>
2. <ready-to-copy prompt>
3. <ready-to-copy prompt>

Lessons
```

## Anti-Patterns

1. Judging product quality by visual polish alone — visual QA and product-pattern audit are different dimensions.
2. Applying SaaS patterns to a local service site, or portfolio patterns to a commerce site.
3. Treating "vibe" or "mood" as a substitute for scenario clarity.
4. Missing the "next step" test — if the user cannot describe what happens after clicking, the scenario is broken.
5. Batch-auditing without first categorizing each site — mixed-category batches produce misleading summaries.
6. Claiming a page "converts" because it has a CTA — the CTA must be specific, actionable, and lead to a working next step.
7. Using product-pattern findings to rewrite copy subjectively — always tie the fix to a pattern mismatch, not a taste preference.
