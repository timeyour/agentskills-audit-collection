---
version: alpha
name: AgentSkills Audit Workbench
description: >
  A precise, calm, evidence-first design system for auditing AI-built products.
  The interface should feel diagnostic and trustworthy: dense enough for serious
  QA work, restrained enough to avoid alarm fatigue, and structured enough for
  agents to generate consistent audit pages.
colors:
  primary: "#12324A"
  primary-active: "#0B2538"
  on-primary: "#FFFFFF"
  accent: "#2F7D68"
  accent-soft: "#DDF2EA"
  canvas: "#F6F8FA"
  surface: "#FFFFFF"
  surface-soft: "#EEF3F7"
  ink: "#17202A"
  body: "#344054"
  muted: "#667085"
  border: "#D8E0E7"
  border-strong: "#B8C4CF"
  code-bg: "#101828"
  code-text: "#EAECF0"
  success: "#1F8F4D"
  warning: "#B7791F"
  error: "#B42318"
  severity-s0: "#7A1E1E"
  severity-s1: "#B42318"
  severity-s2: "#92400E"
  severity-s3: "#3B5B73"
  severity-s4: "#475467"
typography:
  display-lg:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "48px"
    fontWeight: 650
    lineHeight: 1.08
    letterSpacing: "0px"
  title-lg:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "0px"
  title-md:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 650
    lineHeight: 1.3
    letterSpacing: "0px"
  body-md:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0px"
  body-sm:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0px"
  label:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0px"
  code:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "13px"
    fontWeight: 450
    lineHeight: 1.5
    letterSpacing: "0px"
rounded:
  xs: "3px"
  sm: "4px"
  md: "6px"
  lg: "8px"
  full: "9999px"
spacing:
  xxs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "72px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "10px 14px"
    height: "40px"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "10px 14px"
    height: "40px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "10px 14px"
    height: "40px"
  issue-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "20px"
  evidence-table:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "12px"
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.code-text}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "16px"
  severity-badge-s0:
    backgroundColor: "{colors.severity-s0}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  severity-badge-s1:
    backgroundColor: "{colors.severity-s1}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  severity-badge-s2:
    backgroundColor: "{colors.severity-s2}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  severity-badge-s3:
    backgroundColor: "{colors.severity-s3}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  severity-badge-s4:
    backgroundColor: "{colors.severity-s4}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
---

# AgentSkills Audit Workbench Design System

## Overview

The audit workbench should feel precise, calm, and diagnostic. It helps a user see complexity at a glance without turning the page into a spreadsheet dump.

The visual personality is evidence-first and productive. It should feel more like a launch-readiness console than a marketing site: clear over flashy, dense but readable, calm in its severity signaling, and careful with language.

## Colors

- **Primary (#12324A):** Deep diagnostic blue for primary actions, navigation, and durable structure.
- **Accent (#2F7D68):** Muted green for constructive next actions, regression checks, and verified pass states.
- **Canvas (#F6F8FA):** Quiet application background that lets evidence cards and tables remain readable.
- **Surface (#FFFFFF):** Main content surface for issue cards, reports, and forms.
- **Ink (#17202A):** Strong text for headings and core findings.
- **Muted (#667085):** Metadata, timestamps, labels, and secondary explanations.
- **Severity colors:** S0/S1 use restrained reds, S2 uses a dark amber, S3 uses neutral blue-gray, and S4 uses gray. Severity should be legible without turning the interface into an alarm wall.

## Typography

Use one modern sans family for the product surface and one monospace family for locators, route paths, logs, commands, and code.

- **Display:** Reserved for page-level summaries and final verdicts only.
- **Titles:** Used for issue groups, workflow stages, and evidence sections.
- **Body:** Optimized for long audit explanations, not marketing copy.
- **Labels:** Used for severity, evidence level, route names, and compact metadata.
- **Code:** Used for selectors, commands, stack traces, JSON snippets, and fix prompts.

## Layout

Use constrained widths, clear sectioning, and dense but breathable spacing.

- Reports should answer the most important launch question in the first viewport.
- Workflow maps and deployment gaps belong in tables when comparison matters.
- Issue cards should be scannable, with location, evidence, severity, reproduction, and fix suggestion visible without hunting.
- Keep source evidence separate from live evidence.
- Keep visual findings separate from functional findings, then summarize what to fix first.
- Use screenshots, DOM locators, route paths, network requests, and element labels as anchors.

## Elevation & Depth

Use borders and tonal layers before shadows. The system should feel crisp, not floaty.

- Default cards use a light border on white.
- Critical findings can use a stronger left rule or severity badge, not heavy glow.
- Avoid glassmorphism, bokeh, decorative gradients, and visual noise.

## Shapes

Use small radii. Cards and panels should usually stay at `8px` or below. Pills are reserved for compact metadata such as severity, evidence level, and status.

## Components

- **Issue cards:** Must include exact location, evidence, severity, reproduction, fix suggestion, and regression check.
- **Evidence tables:** Use compact rows for expected vs actual behavior, source vs live proof, dependency status, and workflow checkpoints.
- **Severity badges:** Always use `S0-S4`; never replace severity with vague labels like "urgent" or "minor".
- **Fix prompts:** Use code blocks or copyable prompt surfaces with clear boundaries.
- **Workflow maps:** Prefer tables or step lists over decorative diagrams when the goal is operational clarity.

## Do's and Don'ts

Do:

- Make every finding reproducible, located, fixable, and retestable.
- Use specific visual language: hierarchy, rhythm, spacing, alignment, contrast, density, affordance, proportion, focal point, visual weight, component consistency, brand coherence, motion restraint, trust cue, conversion friction.
- Preserve the shared report shape: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons.
- Use observable acceptance criteria instead of intent descriptions.

Don't:

- Use vague critique words like "nice", "modern", "clean", "make it pop", "polish it", or "looks off".
- Hide evidence gaps behind confident prose.
- Use generic purple/blue SaaS sameness, oversized feature cards, fake social proof, or decorative imagery unrelated to the product.
- Let mobile text overlap, controls crop, form errors disappear, or success states remain unverified.
- Treat docs, marketing copy, source code, or screenshots as proof of working behavior when physical execution is required.

## Responsive Behavior

Desktop layouts can use two-column evidence views when comparison is useful. Mobile layouts should collapse into a single column with the severity, location, and action visible before the long explanation.

Touch targets should be at least `40px` high. Long locators, URLs, commands, and code snippets must wrap or scroll inside their own block without covering adjacent content.

## Agent Prompt Guide

When generating UI for this project, follow this prompt:

```text
Use DESIGN.md as the visual source of truth. Build a calm diagnostic audit interface, not a marketing page. Prioritize evidence density, clear severity, exact locations, reproducible steps, and copyable fix prompts. Avoid decorative gradients, glass cards, vague feature blocks, and oversized hero styling.
```

Each audit page should make these questions answerable in under 30 seconds:

1. Is this product usable?
2. Is it visually credible?
3. Which workflow is broken?
4. Where exactly is the problem?
5. What dependency is missing?
6. What should I paste into an AI builder to fix it?
7. What regression check proves the fix worked?
