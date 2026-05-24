# Aesthetic Quality Audit

Use this reference when reviewing visual craft, product taste, design-system quality, or whether a site feels intentionally designed rather than merely generated.

## Goal

Diagnose the quality of the visual/product experience with evidence. Do not say "good design" or "bad design" without explaining the exact visual, interaction, or product reason.

## Inputs

- `PRODUCT.md` when available.
- `DESIGN.md` when available.
- The target URL or screenshots.
- Source evidence from galleries, docs, or community posts.
- Reference patterns from real products when available.

## Aesthetic Dimensions

### 1. Intent and Scenario

- What is the user's situation?
- What future state or identity is the page inviting them into?
- Does the visual direction match the product category?
- Does the page turn inspiration into action?

For lifestyle, fashion, travel, creator, local service, or consumer-commerce products, score whether the page creates a believable scene.

### 2. First Viewport

- The offer is immediately clear.
- The user knows who it is for.
- The primary CTA is specific.
- Supporting proof appears near the claim.
- Visual assets reveal the actual product, outcome, or scenario.

### 3. Hierarchy and Rhythm

- Headings, body copy, cards, and controls have clear levels.
- Spacing creates rhythm instead of random gaps.
- Important actions have appropriate visual weight.
- Sections connect logically.
- The page is scannable without reading every sentence.

### 4. Component Consistency

- Buttons, inputs, cards, badges, navigation, modals, tables, and empty states follow one system.
- Radius, shadows, borders, icon style, color, and spacing are consistent.
- Interactive states are visible.
- Form errors and success states are designed, not default browser leftovers.

### 5. Visual Trust

- Imagery is relevant and specific.
- Social proof is credible.
- Claims are backed by evidence.
- Pricing, contact, privacy, and terms appear where expected.
- Brand voice feels coherent.

### 6. AI Slop Detection

Flag these explicitly:

- Vague hero headline with no concrete offer.
- Decorative gradient or abstract background carrying the page.
- Repeated icon-card sections that say little.
- Generic testimonials or logos.
- Too many unrelated visual styles.
- One-note color palette.
- Missing real product screenshots.
- Unclear CTA labels.
- Content sections that feel stitched together from templates.
- Mobile text overlap, cropped buttons, or hidden CTA.

## Pattern Reference

When possible, compare the page against known patterns:

- Local service site: service promise, proof, areas served, quote/contact CTA.
- Professional service site: expertise, trust, booking/contact, case proof.
- Tool/SaaS: problem, demo, feature proof, docs, pricing/signup.
- Directory/search app: search, filters, listing cards, detail pages, empty states.
- Portfolio: identity, selected work, process, contact.
- Lifestyle/commerce: scenario, aspiration, product path, save/share/buy.
- Admin/dashboard: data density, actions, state, filters, table readability.

Use pattern references to diagnose mismatches, not to force every site into one template.

## Score Rubric

Score 0-100:

- 15: product intent and scenario clarity.
- 15: first viewport offer and CTA.
- 15: hierarchy, spacing, rhythm, and scanability.
- 15: component consistency and interaction states.
- 15: visual trust, proof, and content specificity.
- 10: mobile and responsive polish.
- 10: accessibility basics and contrast.
- 5: distinctive craft beyond a template.

## Issue Card Format

```markdown
### <S0-S4> - <Aesthetic/Product Quality Issue>

- Area:
- URL:
- Live position:
- Locator:
- Pattern expected:
- Observed:
- Problem:
- Likely cause:
- Fix:
- Copy prompt:
- Validation:
```

Severity:

- `S0`: blocks launch or delivery because visual/interaction trust failure prevents safe use.
- `S1`: seriously hurts conversion, trust, accessibility, or product credibility.
- `S2`: noticeable craft, responsive, hierarchy, or workflow issue; temporary launch possible with known risk.
- `S3`: polish, copy, layout, or minor interaction improvement.
- `S4`: future enhancement or benchmark idea.

## Copy Prompt Examples

```text
Improve the first viewport so it states the concrete offer, audience, and primary action. Replace vague aspirational copy with a specific product promise, place proof near the claim, and make the primary CTA describe the next step.
```

```text
Reduce AI slop in this section. Remove generic icon cards, combine overlapping claims, use one component pattern, tighten spacing rhythm, and replace decorative imagery with product- or scenario-specific visuals.
```

```text
Audit this page against its product category. Identify the expected pattern, where the page diverges, whether the divergence helps or hurts, and produce exact section-level fixes.
```

## Output Format

```markdown
## Aesthetic Audit Summary

- URL:
- Product category:
- Intended scenario:
- Aesthetic score:
- Main craft risk:
- Fix first:

## Pattern Fit

| Expected Pattern | Observed | Gap | Risk |
| --- | --- | --- | --- |

## AI Slop Signals

| Signal | Position | Evidence | Fix |
| --- | --- | --- | --- |

## Issues

<issue cards>
```

## Anti-Patterns

- Mistaking personal taste for diagnosis.
- Saying "make it modern" without a target pattern.
- Overvaluing visual novelty while ignoring conversion and workflow.
- Copying reference sites without preserving the target product's intent.
- Treating generated polish as real craft when states, hierarchy, and workflow are broken.
