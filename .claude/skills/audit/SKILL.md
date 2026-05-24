---
name: audit
description: >
  End-to-end agent skill for auditing websites, web apps, open-source projects,
  AI-built products, and vibe-coded examples. Use when the user wants a full workflow
  covering source evidence, live feature testing, visual/aesthetic quality,
  deployment readiness, five-pass acceptance, issue cards, copyable fixes, and accumulated learning.
---

# Audit

Use this skill as the single entry point for the full audit workflow.

The goal is to make a product or website testable, visible, and fixable:

```text
target -> intake -> surface discovery -> permission boundary -> source pass -> live flow test -> visual/aesthetic audit -> product-pattern audit -> deployment audit -> five-pass acceptance -> issue cards -> copyable fixes -> learning ledger
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
- For multi-step audits, emit progressive updates so the user can see the audit trail before the final report.
- When the user wants live step visibility or a workbench view, follow `references/live-run-protocol.md` and update `run-state.json` plus `run-events.ndjson` under `validation/artifacts/{runId}/`.
- Discover the web surface before detailed testing: pages, interactions, media, documents, network/API, storage, and security surfaces.
- Use the permission model before any live interaction; never perform risky production actions silently.
- For AI-built products, generated code, and product acceptance reviews, use `references/failure-modes.md` to check common hidden failures before declaring readiness.
- Use the shared output shape when applicable: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons.
- Use `S0-S4` severity for delivery impact.

## Workflow

1. Intake
   - Identify target type: URL, repo, batch list, local app, design artifact, or tool.
   - Determine permission level using `references/permission-model.md`: public read-only, safe click/navigation, test account flow, staging authorized, or production guarded.
   - If destructive/payment/private actions appear, mark them `SKIPPED-SAFE`.
   - For audits with more than five meaningful steps, load `references/progressive-reporting.md` and announce the planned stages.
   - If the user wants real-time workbench visibility, run `scripts/audit-run-init.sh` (or create `validation/artifacts/{runId}/` manually) and load `references/live-run-protocol.md`.

2. Web surface discovery
   - Before detailed testing, map pages, interaction controls, media assets, documents/downloads, network/API surfaces, storage/session surfaces, and security-sensitive entry points.
   - Use `references/web-surface-discovery.md`.
   - Prioritize surfaces as `P0`, `P1`, `P2`, `skip-safe`, or `unknown`.
   - Emit a progress update summarizing the discovered surface and permission boundaries.

3. Source pass
   - Collect source claims, docs, gallery metadata, repo files, community posts, and product promises.
   - Record source locator and confidence.
   - Use `references/source-evidence.md`.
   - For AI-built or agent-built work, also scan for failure modes from `references/failure-modes.md`: weak validation, unsafe mutations, N+1 or unbounded loading, swallowed exceptions, hallucinated APIs, secrets, placeholders, dependency drift, and missing extreme states.
   - Emit a progress update after completing the source pass when live or visual work remains.

4. Feature inventory
   - List every visible or documented feature.
   - Include navigation, CTA, forms, auth, dashboards, search, upload, copy/export/share, checkout/payment, admin/CMS, and deployment tools.
   - Reconcile this inventory with the web surface discovery map.

5. Live functional audit
   - Execute every safe flow as far as possible.
   - Record URL, live position, locator, steps, expected result, actual result, evidence, risk, and status.
   - Use `references/live-functional-audit.md`, or invoke `/flow-test` for a dedicated pass.
   - Emit progress updates after each major route, form, CTA group, auth boundary, or blocker.

6. Visual and aesthetic audit
   - Inspect layout, hierarchy, spacing, typography, color, images, component consistency, responsiveness, trust, and AI slop signals.
   - Use `references/webpage-audit-rubric.md` and `references/aesthetic-quality-audit.md`, or invoke `/visual-qa` for a dedicated pass.

6.5. Product-pattern audit
   - For lifestyle, service, commerce, creator, and SaaS products, check scenario preparation, pattern fit, and conversion readiness.
   - Use `../ai-product-audit/references/product-pattern-rubric.md`, or invoke `/ai-product-audit` for a dedicated pass.

7. Deployment readiness
   - Check domain, SSL, env vars, backend/API, database, auth, email/SMS, storage, payment, CMS/admin, analytics, monitoring, SEO, privacy, backup, and rollback.
   - Use `references/deployment-readiness.md`.

8. Five-pass acceptance
   - For important targets, run baseline, functional, edge/failure, visual/deployment, and retest/experience passes.
   - Use `references/five-pass-acceptance.md`, or invoke `/accept-five` for a dedicated pass.

9. Output
   - Produce scope, evidence split, findings, severity, reproduction, fix suggestions, regression checks, lessons, feature maps, issue cards, deployment table, copyable fix pack, final verdict, and experience ledger.
   - Use `references/report-format.md`.
   - Convert progress updates into the final report instead of pasting a raw running log.

10. Learn
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
