# Design Principles

## Design Intent

The audit workbench should feel precise, calm, and diagnostic. It should help a user see complexity at a glance without making the page feel like a spreadsheet dump.

## Visual Personality

- Clear over flashy.
- Dense but readable.
- Productive, not decorative.
- Evidence-first.
- Calm severity signaling.
- Craft-oriented language.

## UI Principles

- Show issues as actionable cards with exact location and copyable fixes.
- Put workflow maps and deployment gaps in tables.
- Make severity visible without turning the interface into an alarm wall.
- Keep source evidence separate from live evidence.
- Keep visual findings separate from functional findings, then summarize what to fix first.
- Use screenshots, DOM locators, route paths, and element labels as anchors.

## Aesthetic Audit Vocabulary

Use specific terms:

- hierarchy
- rhythm
- spacing
- alignment
- contrast
- density
- affordance
- proportion
- focal point
- visual weight
- component consistency
- brand coherence
- motion restraint
- trust cue
- conversion friction

Avoid vague terms:

- nice
- modern
- clean
- make it pop
- polish it
- looks off

## AI Slop Signals

Flag these when observed:

- generic gradient hero with vague headline;
- oversized cards that do not map to real tasks;
- repeated icon-card sections with no business purpose;
- purple/blue SaaS sameness;
- mismatched border radius, shadows, or icon styles;
- decorative imagery unrelated to the product;
- weak first viewport offer;
- fake-looking testimonials or social proof;
- CTA labels that do not describe action;
- beautiful but disconnected sections;
- mobile text overlap or cropped controls;
- hidden form errors or missing success states.

## Output Shape

Each audit page should make these questions answerable in under 30 seconds:

1. Is this site usable?
2. Is it visually credible?
3. Which workflow is broken?
4. Where exactly is the problem?
5. What dependency is missing?
6. What should I paste into an AI builder to fix it?

For harness plans, the page should also make these questions answerable:

1. What are the business stages?
2. Which execution units are prompt, skill, Dify, RPA, code, human, or external system?
3. Where are the automatic checkpoints?
4. Where must a human intervene?
5. What gets retried, what falls back, and what stops?

For process-agent plans, it should also make these questions answerable:

1. What real business bottleneck is being removed?
2. What is the business flow and node map?
3. What data template makes each node executable?
4. Which know-how is now explicit rather than hidden in a person's head?
5. What field signals prove the agent is improving the process?
6. What root cause was fixed, and how was the reduction verified?

Use the shared report shape:

```text
Scope -> Evidence -> Findings -> Severity -> Reproduction -> Fix Suggestion -> Regression Check -> Lessons
```

Severity should use `S0-S4`, not vague urgency labels:

- `S0`: blocks launch or delivery.
- `S1`: serious trust, conversion, correctness, privacy, or reliability risk.
- `S2`: noticeable issue; temporary launch possible with known risk.
- `S3`: polish.
- `S4`: future enhancement.
