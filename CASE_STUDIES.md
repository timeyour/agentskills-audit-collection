# Case Studies

This page turns the validation directory into a quick project story.

The full reports live in `validation/`. This file highlights the examples that best explain what AgentSkills is trying to prove: AI-built products need evidence, not vibes.

## 1. API Checker

- Type: interactive developer tool.
- Source: v0 / Vercel Community.
- Full report: `validation/top-20-vibe-coded-sites-audit.md`
- Why it matters: the public page exposes a clear, testable workflow.
- Visible workflow: request configuration, endpoint input, HTTP method, auth helpers, query parameters, test action, response panel, history, and code generator.
- Audit value: best benchmark for position-aware workflow mapping.

Issue lesson:

```text
The strongest AI-built product examples are not just visually polished. They expose exact workflow positions an auditor can test.
```

## 2. PhoneValidation.app

- Type: commercial micro-tool.
- Source: Made with Lovable.
- Full report: `validation/top-20-vibe-coded-sites-audit.md`
- Why it matters: it has a visible monetization surface and a concrete user workflow.
- Visible workflow: free credits, phone-number test, CSV upload promise, pricing, credit accounting, and history/export expectations.
- Audit value: a good example of a small tool that may be more useful than broad source-only platform claims.

Issue lesson:

```text
Single-purpose products can be stronger audit targets than large vague platforms because the input, output, and dependencies are easier to test.
```

## 3. Committed Citizens

- Type: consulting website.
- Source: v0 / Vercel Community.
- Full report: `validation/vibe-sites-live-position-retest.md`
- Why it matters: the source clearly exposes a deployment and editorial workflow gap.
- Finding: the `/insights` section had hard-coded articles and needed a headless CMS for team publishing.
- Audit value: best example of turning a vague "needs CMS" idea into a concrete deployment-readiness issue.

Copyable fix pattern:

```text
Add a CMS plan for the /insights section: content schema, author/editor roles, migration of existing hard-coded articles, preview flow, deployment env vars, and rollback plan.
```

## 4. impeccable.style

- Type: AI design tooling site.
- Source: public website and open-source repo.
- Full report: `validation/impeccable-style-five-pass-audit.md`
- Why it matters: it tests the five-pass acceptance model against a real design-tooling product.
- Findings: route/deep-link checks, CLI execution boundaries, extension workflow boundaries, and screenshot-backed visual QA requirements.
- Audit value: proves the system can separate source evidence from runtime proof.

Issue lesson:

```text
Docs can be accurate while runtime claims still need proof. Tool products must be tested through install, execution, browser flow, and visual evidence.
```

## 5. Global 200 Source-Level Batch

- Type: 200-candidate website audit dataset.
- Source pools: Made with Lovable, Replit Gallery, Made with Lovable Tools & Utilities, and Vercel Community.
- Full report: `validation/global-200-web-audit-batch.md`
- Why it matters: it shows the dataset and scoring approach without pretending that every live workflow was clicked.
- Audit value: builds a queue for future live/browser testing.

Important caveat:

```text
This is a source-level pass. Exact button coordinates, screenshot regions, and form-submit behavior still require browser/visual automation.
```

## 6. Vibe-Coded Site Verification Template

- Type: reusable scoring table.
- Full template: `validation/vibe-coded-site-verification-template.md`
- Why it matters: inspiration lists can confuse a polished shell with a working product.
- Audit value: converts "worth copying?" into a 14-point rubric covering offer clarity, CTA, real flow, business pages, backend/data signals, production signals, and reuse value.

Issue lesson:

```text
A vibe-coded site should not be promoted as a reference until source evidence, live evidence, and at least one observable workflow are separated and scored.
```

## 7. GitHub Similar Projects Benchmark

- Type: ecosystem positioning benchmark.
- Full report: `validation/github-similar-projects-benchmark-2026-05-22.md`
- Why it matters: this repository should not be mistaken for a generic skills list, prompt pack, or browser automation wrapper.
- Audit value: compares nearby projects such as VoltAgent agent skills, Trail of Bits security skills, HashiCorp agent skills, SuperClaude, BMAD Method, awesome-design-md, Playwright CLI/MCP, and browser-use.

Positioning lesson:

```text
AgentSkills Audit Collection should own the acceptance layer between vibe-coded output and real product delivery.
```

## What These Cases Prove

- Source evidence and live evidence must be separate.
- A strong first screen is not the same as a working product.
- Templates and production sites need different labels.
- Deployment gaps deserve first-class issue cards.
- Copyable fix prompts are part of the deliverable, not a nice extra.
- Five-pass acceptance turns one-time review into reusable project memory.
- Ecosystem benchmarks keep the repository narrower than a generic skills marketplace and sharper than a browser automation demo.
