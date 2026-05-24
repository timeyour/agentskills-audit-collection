# Aesthetic Metrics

Use this reference when visual QA needs measurable design evidence instead of vague taste claims.

The goal is not to replace human judgment. The goal is to make visual findings concrete enough to locate, fix, and retest.

## Evidence Policy

- Screenshot and browser evidence can support visual findings.
- AI visual judgment can describe a likely issue, but pixel, color, spacing, and Figma fidelity claims need tool evidence when possible.
- If a precise metric was not measured, phrase it as an observed pattern, not a numeric fact.

## AI Slop Signals

Flag these patterns when they appear without product-specific purpose:

| Signal | What To Look For | Typical Severity |
| --- | --- | --- |
| Purple-blue gradient sameness | Generic hero gradients, neon wash, low relationship to product category. | `S2-S3` |
| Glassmorphism overuse | Frosted cards stacked over decorative blur without information value. | `S2-S3` |
| Card pile layout | Repeated icon cards with equal weight, no hierarchy, no decision path. | `S2` |
| Meaningless oversized headline | Large abstract phrase that hides the product, offer, or next action. | `S1-S2` |
| Spacing drift | Similar components use visibly different padding, gaps, or alignment. | `S2-S3` |
| Fake proof | Testimonials, logos, metrics, or badges with no source or trust context. | `S1-S2` |
| Decorative imagery mismatch | Image does not reveal product, place, person, state, or workflow. | `S2-S3` |
| One-note palette | Page is dominated by one hue family with little semantic contrast. | `S2-S3` |
| Mobile squeeze | Text, buttons, cards, or navigation compress rather than reflow. | `S1-S2` |

## Quantitative Heuristics

Use these as audit heuristics, not universal laws. Product category and target user can override them when justified.

### Whitespace Ratio

Question: does the page have enough breathing room for its content density?

Heuristic:
- Content-dense dashboards can be tighter.
- Landing pages, portfolios, and editorial pages need more whitespace.
- First viewport should leave a clear visual path from headline to primary action.

Evidence:
- Screenshot with annotated crowded or underused zones.
- DOM or CSS spacing tokens when source is available.

Finding language:

```text
The first viewport feels crowded because the hero copy, CTA row, and proof badges compete inside the same vertical band. Screenshot evidence shows no clear pause between sections.
```

### Spacing Consistency

Question: do repeated components follow the same gap and padding rhythm?

Heuristic:
- Similar cards, form rows, nav items, and section blocks should share a small spacing scale.
- Avoid many one-off values unless the design system intentionally defines them.

Evidence:
- CSS/Tailwind spacing values.
- Screenshot annotations comparing repeated components.
- Computed styles when available.

Regression check:
- Compare repeated component gaps after fix at desktop and mobile widths.

### Typography Hierarchy

Question: can the reader tell what to read first, second, and third?

Heuristic:
- Use a limited type scale for body, caption, section heading, and hero/display.
- Do not use hero-scale type inside compact panels, cards, sidebars, or tables.
- Line height should support reading, not just visual drama.

Evidence:
- Screenshot of hierarchy conflicts.
- CSS font size, weight, line-height, and container context.

### Color Roles

Question: does color communicate roles consistently?

Heuristic:
- Primary, accent, success, warning, danger, border, muted text, and background roles should not collapse into the same color.
- Severity colors should not conflict with success/failure semantics.
- Contrast should be checked with a contrast tool for text claims.

Evidence:
- Design tokens, CSS variables, screenshots, contrast measurements where possible.

### Visual Weight Distribution

Question: does attention land on the intended product signal or action?

Heuristic:
- Strongest weight should support the product, object, workflow, offer, or primary action.
- Decorative backgrounds should not overpower interactive controls.
- Repeated equal-weight cards create scanning fatigue.

Evidence:
- First viewport screenshot.
- Notes on relative size, contrast, saturation, position, and motion.

### Component Consistency

Question: do buttons, inputs, cards, tabs, modals, tables, and navigation feel like one system?

Heuristic:
- Similar actions use similar affordances.
- States are visible: default, hover/focus, active, disabled, loading, error.
- Components should not change radius, shadow, spacing, or font treatment without reason.

Evidence:
- Component inventory and screenshot examples.
- Source selectors or design tokens if available.

## Figma vs Code Fidelity Workflow

Use this workflow when a design source exists:

```text
Figma frame
  ->
implementation screenshot at matching viewport
  ->
pixel/structural comparison
  ->
difference heatmap or annotated screenshot
  ->
LLM-assisted explanation
  ->
copyable fix prompt
  ->
regression screenshot
```

Recommended tool categories:
- Overlay tools for manual spot checks.
- Pixel comparison libraries such as pixelmatch.
- Visual regression suites such as BackstopJS or Playwright screenshots.
- Design-token checks for colors, spacing, typography, and radius.

Important rule:
- Do not ask an LLM to eyeball exact color or pixel fidelity as the only evidence. Use deterministic comparison when precision matters.

## Output Shape

For each visual metric finding, report:

```text
Metric:
Observed Pattern:
Evidence Level: screenshot / source / computed style / pixel diff / assumption
Severity:
Impact:
Fix Prompt:
Regression Check:
```

## Fix Prompt Templates

Spacing:

```text
Normalize spacing for [component/section]. Use a limited spacing scale, align repeated cards/forms/buttons, preserve mobile wrapping, and provide before/after screenshots for desktop and mobile.
```

Hierarchy:

```text
Rebuild the hierarchy for [section]. Make the primary product signal and CTA the strongest visual elements, reduce competing card weights, use a limited type scale, and verify the first viewport scan path.
```

Color:

```text
Refactor color roles for [page/component]. Separate primary, accent, muted, success, warning, danger, border, and background tokens. Verify text contrast and avoid one-hue palette drift.
```

Figma fidelity:

```text
Compare the implementation screenshot against the provided Figma frame. Fix only the measured differences in spacing, typography, color roles, component states, and responsive behavior, then rerun visual regression.
```
