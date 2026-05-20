---
name: audit
description: End-to-end agent skill for auditing websites, web apps, open-source projects, AI-built products, and vibe-coded examples. Use when the user wants a full workflow covering source evidence, live feature testing, visual/aesthetic quality, deployment readiness, five-pass acceptance, issue cards, copyable fixes, and accumulated learning.
---

# Audit

Use this skill as the single entry point for the full audit workflow.

The goal is to make a product or website testable, visible, and fixable:

```text
target -> source pass -> live flow test -> visual/aesthetic audit -> deployment audit -> five-pass acceptance -> issue cards -> copyable fixes -> learning ledger
```

## When To Use

Use `/audit` when the user gives:

- a live website URL;
- a web app;
- an open-source repository;
- a vibe-coded project;
- a design tool/resource;
- a batch of sites;
- a request to test every function;
- a request to judge page quality, visual style, deployment gaps, or workflow breakage.

## Core Rules

- Separate source evidence from live evidence.
- Do not treat gallery claims, docs, or marketing copy as proof that a workflow works.
- Every issue needs a live position or source locator.
- Every important feature needs expected vs actual behavior.
- Visual scores are source-based until screenshots or browser evidence exist.
- Tool claims require execution evidence before full acceptance.
- Repeat important audits through five passes and record what was learned.
- Use the shared output shape when applicable: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons.
- Use `S0-S4` severity for delivery impact.

## Workflow

1. Intake
   - Identify target type: URL, repo, batch list, local app, design artifact, or tool.
   - Determine safe execution level: source-only, visual, clicked public flow, authenticated flow, or local tool execution.
   - If destructive/payment/private actions appear, mark them `SKIPPED-SAFE`.

2. Source pass
   - Collect source claims, docs, gallery metadata, repo files, community posts, and product promises.
   - Record source locator and confidence.
   - Use `references/source-evidence.md`.

3. Feature inventory
   - List every visible or documented feature.
   - Include navigation, CTA, forms, auth, dashboards, search, upload, copy/export/share, checkout/payment, admin/CMS, and deployment tools.

4. Live functional audit
   - Execute every safe flow as far as possible.
   - Record URL, live position, locator, steps, expected result, actual result, evidence, risk, and status.
   - Use `references/live-functional-audit.md`, or invoke `/flow-test` for a dedicated pass.

5. Visual and aesthetic audit
   - Inspect layout, hierarchy, spacing, typography, color, images, component consistency, responsiveness, trust, and AI slop signals.
   - Use `references/webpage-audit-rubric.md` and `references/aesthetic-quality-audit.md`, or invoke `/visual-qa` for a dedicated pass.

6. Deployment readiness
   - Check domain, SSL, env vars, backend/API, database, auth, email/SMS, storage, payment, CMS/admin, analytics, monitoring, SEO, privacy, backup, and rollback.
   - Use `references/deployment-readiness.md`.

7. Five-pass acceptance
   - For important targets, run baseline, functional, edge/failure, visual/deployment, and retest/experience passes.
   - Use `references/five-pass-acceptance.md`, or invoke `/accept-five` for a dedicated pass.

8. Output
   - Produce scope, evidence split, findings, severity, reproduction, fix suggestions, regression checks, lessons, feature maps, issue cards, deployment table, copyable fix pack, final verdict, and experience ledger.
   - Use `references/report-format.md`.

9. Learn
   - Convert repeated findings into guardrails, checklist items, better prompts, or benchmark examples.
   - If durable, update `CLAUDE.md` or relevant skill references.

## Verdicts

- `PASS`: core flows, visual quality, and deployment requirements are acceptable.
- `PASS WITH NOTES`: usable or useful, but gaps remain.
- `FAIL`: critical workflow, visual trust, security, or deployment blocker remains.
- `INCOMPLETE`: source pass happened, but live/visual/tool execution evidence is missing.

## Anti-Patterns

- Calling a source-level pass a live audit.
- Reviewing only the homepage.
- Judging only aesthetics.
- Testing only the happy path.
- Ignoring mobile.
- Missing route aliases, deep links, and shared URLs.
- Reporting vague fixes like "improve UI".
- Failing to create copyable prompts.
- Running five passes without accumulating new experience.
