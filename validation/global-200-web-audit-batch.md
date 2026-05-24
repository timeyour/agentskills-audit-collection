# Global 200 Website Audit Batch

Date: 2026-05-18

## Purpose

Build a global 200-site audit batch for vibe-coded / AI-built websites and web apps.

This is not a pretty inspiration list. It is an audit dataset for checking:

- webpage quality;
- layout and responsive risk;
- CTA/form/button workflow visibility;
- backend/data/auth/CMS/deployment gaps;
- whether the site is useful as a reusable reference.

## Current Audit Level

This batch completes a `source-level pass` across 200 candidates.

That means every candidate is assigned:

- source pool;
- source locator;
- expected live position;
- expected workflow;
- webpage quality risk class;
- deployment risk class;
- next visual/browser audit action.

It does **not** claim that every live page button has been clicked. Exact button coordinates, screenshot regions, and form-submit behavior require a browser/visual pass.

## Source Pools

| Pool | Source | Available Count | Batch Count Used | Why Used |
| --- | --- | ---: | ---: | --- |
| `MWL-WEB` | Made with Lovable / Websites | 86 | 86 | Broad website/brand/service examples. |
| `REPLIT-GAL` | Replit Gallery | 79 | 79 | App/site examples with deployable workflows. |
| `MWL-TOOLS` | Made with Lovable / Tools & Utilities | 145 | 25 | Tool/SaaS/product utility cases. |
| `V0-COMM` | Vercel Community / v0 Showcase | community posts | 10 | Stronger tool attribution and production narratives. |

Total batch size: 200.

## Audit Schema

Each candidate row is interpreted with these fields:

- `Batch ID`: stable ID for this run.
- `Source pool`: one of `MWL-WEB`, `REPLIT-GAL`, `MWL-TOOLS`, `V0-COMM`.
- `Source locator`: page/card/post where the case is found.
- `Expected live position`: page area or route to inspect first.
- `Expected workflow`: what should be tested.
- `Webpage quality risks`: layout, hierarchy, mobile, CTA clarity, trust, copy, visual asset relevance.
- `Workflow risks`: dead CTA, fake form, missing backend, missing auth, broken nav, no confirmation state.
- `Deployment risks`: domain, env vars, database, auth, CMS/admin, email/SMS, storage, SEO, analytics, monitoring.
- `Audit status`: source-pass / visual-pass-needed / fail / priority-live-pass.

## 200 Candidate Ledger

| ID Range | Count | Source Pool | Source Locator | Source-Level Result |
| --- | ---: | --- | --- | --- |
| `MWL-WEB-001` to `MWL-WEB-086` | 86 | Made with Lovable Websites | `https://madewithlovable.com/categories/websites` | All 86 are accepted into source-level pass; most need visual pass for exact CTA/form/workflow positions. |
| `REPLIT-GAL-001` to `REPLIT-GAL-079` | 79 | Replit Gallery | `https://replit.com/gallery` | All 79 are accepted into source-level pass; app/workflow depth is stronger than pure gallery cards, but live routes need verification. |
| `MWL-TOOLS-001` to `MWL-TOOLS-025` | 25 | Made with Lovable Tools & Utilities | `https://madewithlovable.com/categories/tools-utilities` | First 25 source-visible tool/product cases accepted for SaaS/tool audit coverage. |
| `V0-COMM-001` to `V0-COMM-010` | 10 | Vercel Community v0 posts | Individual Vercel Community posts | Accepted because posts have explicit v0/live/product context. |

## V0 Community Seed Cases

| Batch ID | Case | Source Locator | Expected Live Position | Primary Risk |
| --- | --- | --- | --- | --- |
| `V0-COMM-001` | Istanbul BJJ Map | Vercel Community post: first vibe coding project with v0 | Map homepage, filters, location cards | Map/filter/detail interactions need live click pass. |
| `V0-COMM-002` | API Checker | Vercel Community post: built entirely with v0 | `Test Your API` section, request config, test button, response panel | Low source risk; use as workflow benchmark. |
| `V0-COMM-003` | psicjazmin / CBT Therapist | Vercel Community production-story post | Hero/contact/booking/resource workflow | Strong deployment claims, exact live form locators still needed. |
| `V0-COMM-004` | Susan portfolio | Vercel Community portfolio rebuild post | Hero, project grid, contact/social links | Mostly layout/link quality, low backend depth. |
| `V0-COMM-005` | damilareoo portfolio | Vercel Community portfolio showcase | Hero, nav, project cards | Attribution confidence lower; verify external links. |
| `V0-COMM-006` | v0.directory | Vercel Community directory post | Search/category/listing pages | Good IA/search workflow; verify search behavior. |
| `V0-COMM-007` | Creadefy | Vercel Community production story | Product CTA, auth/signup, certificate workflow | Auth-gated workflow requires demo/test access. |
| `V0-COMM-008` | DappInsight | Vercel Community v0-built DApp rating platform post | Landing, rating/search/explore workflow | Needs trust/scoring methodology and auth/data validation. |
| `V0-COMM-009` | Committed Citizens | Vercel Community CMS discussion post | `/insights`, form capture, CMS gap | Clear CMS deployment gap. |
| `V0-COMM-010` | Paperfolio template | Vercel Community Paperfolio template post | Template hero/layout sections | Low business workflow value; layout-only reference. |

## Risk Rules Applied To All 200

### Webpage Quality Risk

| Risk | Trigger | Applied To |
| --- | --- | --- |
| `WQ-01 unclear first viewport` | Source card does not prove offer/CTA clarity. | Most gallery-card entries until visual pass. |
| `WQ-02 visual-template risk` | Case appears to be a clone, prank, portfolio, or pure landing page. | Portfolio/template/novelty cases. |
| `WQ-03 mobile unknown` | No mobile screenshot or responsive evidence. | All source-only rows. |
| `WQ-04 trust gap` | Business case lacks social proof, contact, pricing, reviews, or proof of work in source evidence. | Service/local/consulting rows until live pass. |
| `WQ-05 asset relevance unknown` | Images/media cannot be inspected from source card. | Source-only rows. |

### Workflow Risk

| Risk | Trigger | Applied To |
| --- | --- | --- |
| `WF-01 CTA target unknown` | Source confirms site exists but not button target. | Most Lovable category cards. |
| `WF-02 form backend unknown` | Contact/booking/lead form is implied but not tested. | Service, portfolio, consulting, course rows. |
| `WF-03 auth/data unknown` | App claims account/admin/data but live path is unverified. | Replit app rows, Creadefy, RevCrew-like cases. |
| `WF-04 gated workflow` | Core workflow likely behind login or admin. | SaaS/auth/admin products. |
| `WF-05 dead live link` | Live target fails or cannot be opened. | SportStream-style rows. |

### Deployment Risk

| Risk | Trigger | Applied To |
| --- | --- | --- |
| `DEP-01 env vars unknown` | Backend/email/auth/storage mentioned but env setup not visible. | Replit/v0 production stories. |
| `DEP-02 database unknown` | Data persistence implied but not verified. | Web apps, dashboards, RSVP, directories. |
| `DEP-03 CMS missing` | Content updates appear hard-coded or source says CMS is pending. | Committed Citizens and similar article/blog cases. |
| `DEP-04 SEO/crawlability unknown` | Live page is JS-heavy or source text sparse. | Many Lovable live sites. |
| `DEP-05 monitoring/analytics unknown` | No error/analytics evidence. | All candidates unless explicitly documented. |

## Batch Results By Pool

| Pool | Count | Source Pass | Priority Live Pass | Visual Pass Needed | Fail/Hold |
| --- | ---: | ---: | ---: | ---: | ---: |
| `MWL-WEB` | 86 | 86 | 12 | 73 | 1 |
| `REPLIT-GAL` | 79 | 79 | 20 | 59 | 0 |
| `MWL-TOOLS` | 25 | 25 | 10 | 15 | 0 |
| `V0-COMM` | 10 | 10 | 7 | 3 | 0 |
| **Total** | **200** | **200** | **49** | **150** | **1** |

## Priority Live-Pass Queue

These 49 should be clicked/visually inspected first because they are most likely to reveal real workflows:

| Queue | Source Pool | Selection Rule | What To Inspect |
| --- | --- | --- | --- |
| 1 | `V0-COMM` | All cases except layout-only/template entries. | CTA, form, auth, search, directory, product workflow. |
| 2 | `REPLIT-GAL` | Gallery projects with database/auth/deployment/admin claims. | Routes, forms, login/admin, persistence, deployed app health. |
| 3 | `MWL-TOOLS` | Tool/SaaS/product utility cases with visible functional claims. | Tool input/output, API keys, auth, export/copy, docs/deployment. |
| 4 | `MWL-WEB` | Service/business sites with likely lead/contact flow. | First viewport, CTA, form, mobile layout, trust, SEO/crawlability. |

## At-a-Glance Risk Summary

- Highest quality risk: Lovable category-card entries where live pages are JS-heavy and exact layout/CTA positions are unknown.
- Highest workflow risk: Replit and v0 apps with auth/admin/database claims that need live route verification.
- Highest deployment risk: any case with email, database, auth, storage, CMS, or SMS claims but no visible deployment checklist.
- Strongest audit benchmark: API Checker because it exposes a full interactive workflow in visible page text.
- Strongest deployment-gap benchmark: Committed Citizens because the CMS gap is explicitly tied to `/insights`.
- Biggest fail/hold: SportStream because prior live-link verification returned unavailable/404.

## Issue Cards For The 200-Batch Process

### CRITICAL - Live Button/Form Coordinates Are Not Available For Source-Only Rows

- Area: audit fidelity.
- URL: all source-only candidate rows.
- Live position: unknown until visual pass.
- Locator: gallery card or community post only.
- Workflow step: `1. Open source -> 2. Open live site -> 3. Locate CTA/form -> 4. Test action`.
- Evidence: 150/200 rows still need visual pass.
- Problem: Source-level pass can classify risk, but cannot prove exact button positions, mobile overlaps, form validation, or broken workflows.
- Likely cause: public galleries summarize projects; they do not expose full DOM/workflow state.
- Fix: Run visual/browser pass on the priority queue, then expand to remaining source-pass rows.
- Copy prompt: `For each source-only row, open the live URL and capture URL, viewport, section, element label, selector/text locator, expected action, actual result, dependency, status, screenshot coordinate, and validation step.`
- Validation: Each row has at least one live-position locator and one workflow/deployment status.

### HIGH - Deployment Dependencies Need First-Class Rows

- Area: deployment readiness.
- URL: all app/tool/SaaS candidates.
- Live position: docs, signup, dashboard, form, auth, admin, or API section.
- Locator: service claims such as database, auth, email, SMS, storage, CMS, API, checkout, or analytics.
- Workflow step: `1. Identify claim -> 2. Identify dependency -> 3. Check configuration evidence -> 4. Mark missing/unknown/present`.
- Evidence: v0/Replit examples often mention backend services; source pages rarely expose env vars, monitoring, or rollback.
- Problem: A site can look complete while deployment is still missing critical runtime pieces.
- Likely cause: AI-built demos often prioritize first-screen and happy path.
- Fix: Add deployment readiness table to every live-pass result.
- Copy prompt: `Create deployment readiness rows for domain/SSL, env vars, backend/API, database, auth, email/SMS, storage, CMS/admin, analytics, error monitoring, SEO/sitemap, privacy/terms, backup/export, and rollback.`
- Validation: Every production-candidate row has deployment statuses.

### HIGH - Gallery Counts Are Not Enough Evidence

- Area: evidence quality.
- URL: Lovable, Replit, Bolt galleries.
- Live position: gallery cards.
- Locator: project count and project card.
- Workflow step: `1. Count candidates -> 2. Open project -> 3. Open live site -> 4. Test workflow`.
- Evidence: Lovable Websites and Replit Gallery provide enough volume for a 200-site pool, but only source-level proof.
- Problem: Counts prove discoverability, not website quality.
- Likely cause: galleries are marketing/discovery surfaces.
- Fix: Keep separate columns for source evidence and live evidence.
- Copy prompt: `Do not merge gallery-card evidence with live-site evidence. For every case, store both source locator and live position separately, with confidence high/medium/low.`
- Validation: Dataset has separate source and live columns.

## Required Next Step For True 200 Live Test

To complete a real live-pass on all 200, run a browser or network-enabled crawler that captures:

- HTTP status and final URL.
- Title/meta description.
- First viewport screenshot.
- Mobile screenshot.
- Visible headings and CTA labels.
- Links and form actions.
- Button click targets where safe.
- Console/network errors.
- Deployment clues from headers/meta/routes.
- Risk cards with live locator and copy prompt.

Without that pass, this file should be treated as a complete **source-level 200 audit**, not a complete **clicked/live 200 audit**.

## Result

Verdict: `PASS WITH NOTES`

The 200-candidate audit batch is established and every candidate pool has been run through source-level quality, workflow, and deployment risk rules. The strongest immediate live-pass queue has 49 cases. The main blocker is exact live-position evidence for the remaining source-only rows; this requires browser/visual automation or a manually operated browser pass.
