# Batch Retest: Live Position-Aware Website Audit

Date: 2026-05-18

## Purpose

Retest the priority vibe-coded website set with explicit detection positions. The goal is to make every finding traceable to a URL, page area, element, workflow step, or deployment dependency.

This is the format needed for a real audit workbench: users should be able to see where the issue is, what workflow it belongs to, and copy a fix prompt directly.

## Position Fields

- URL: inspected page or source page.
- Page area: hero, form, dashboard, source description, project metadata, etc.
- Element label: visible button, form, link, or UI text.
- Locator: text match, source page claim, page section, or known route.
- Workflow step: the step where the finding appears.
- Status: works / partial / broken / unknown.
- Confidence: high / medium / low.

## Retest Summary

| Case | Platform | Detected Position | Workflow/Deployment Signal | Verdict |
| --- | --- | --- | --- | --- |
| QuickTables | Lovable | `https://madewithlovable.com/projects/quicktables` -> project summary -> "mobile-friendly websites", "direct ordering", "SMS marketing", "loyalty programs" | Clear business workflow claim; live page text extraction is sparse, so visual CTA/form mapping still needs browser pass. | `PASS WITH NOTES` |
| LovableHTML | Lovable | `https://lovablehtml.com/` and project page -> SEO/product promise; docs route `/docs/quickstart/cloudflare-workers` -> setup/deployment instructions | Strong deployment workflow: API key, verified domain, Cloudflare Worker, prerender route. | `PASS` |
| Heavy DOOTY | Lovable | Made with Lovable websites category -> project card -> family-owned yard cleanup service | Strong local-service positioning, but individual workflow positions need live visual pass. | `PASS WITH NOTES` |
| API Checker | v0 | `https://www.apichecker.io/` -> `Test Your API` -> `Request Configuration` -> `Test API` button; `Code Generator` -> cURL/JavaScript/Python buttons | Clear interactive tool workflow: endpoint, method, auth, params, headers, test, response, history, code generation. | `PASS` |
| CBT Therapist / psicjazmin | v0 | Vercel Community source -> production project claim -> custom contact form with Resend -> dashboard using Neon and Vercel Blob -> live site link | Strong production workflow and deployment dependency map; live UI position needs browser pass. | `PASS WITH NOTES` |
| Committed Citizens | v0 | Vercel Community source -> launched v0 consulting site -> `/insights` -> 9 hard-coded articles -> future CMS need; form capture uses Resend | Excellent "missing CMS" deployment/workflow gap. | `PASS` |
| RevCrew.ai | Replit | Replit Gallery page -> description -> multiple pages, contact forms, blog, user/admin auth, backend database; View App link | Strong full-stack workflow map: marketing pages + forms + blog + auth/admin + database. | `PASS` |
| Event RSVP template | Replit | Replit Gallery page -> public event pages, RSVP forms, admin dashboard, guest lists, React/Express/PostgreSQL; template/remix metadata | Strong reusable workflow skeleton, but not validated as a production business. | `PASS WITH NOTES` |
| Paperfolio template | v0 | Vercel Community source -> template/layout recreation claim | Useful for layout replication only; not a business workflow. | `LOW PRIORITY` |
| Bolt | Bolt | Supplied link points to `bolt.eu`, not Bolt.new gallery or project page | Wrong source family for vibe-coded site cases. | `EXCLUDE` |

## Position-Aware Issue Cards

### HIGH - QuickTables Live Workflow Cannot Be Fully Mapped From Text Crawl

- Area: interaction/workflow.
- URL: `https://quicktables.info/`
- Live position: homepage, expected restaurant ordering or CTA flow.
- Locator: live domain opens, but crawler text is sparse; source evidence is on Made with Lovable project summary.
- Workflow step: `1. Open site -> 2. Identify ordering CTA -> 3. Follow order/SMS/loyalty path`.
- Evidence: project page claims direct ordering, SMS marketing, and loyalty programs.
- Problem: A user cannot see from the current text evidence which button starts each workflow.
- Likely cause: JavaScript-heavy page or limited crawl extraction.
- Fix: Run a browser/visual pass and record CTA labels, target URLs, form fields, and broken states.
- Copy prompt: `Audit https://quicktables.info/ visually. Map every CTA related to ordering, SMS marketing, and loyalty. For each button, record label, section, destination, backend dependency, and whether it works.`
- Validation: A workflow table exists with at least primary CTA, order flow, SMS opt-in, and loyalty signup/status.

### MEDIUM - LovableHTML Deployment Dependencies Are Strong But Need Checklist Treatment

- Area: deployment.
- URL: `https://lovablehtml.com/docs/quickstart/cloudflare-workers`
- Live position: docs page -> prerequisites/setup.
- Locator: text match: API key, verified domain, Cloudflare Workers, `/api/prerender/render?url=...`.
- Workflow step: `1. Add domain -> 2. Create API key -> 3. Configure Worker -> 4. Test prerender`.
- Evidence: docs identify API key, domain verification, and edge worker setup.
- Problem: This is a deployment flow, not just a landing page; audits should surface missing keys/domains/workers explicitly.
- Likely cause: Deployment readiness often gets hidden behind marketing copy.
- Fix: Convert deployment docs into a checklist with environment variable and test endpoint rows.
- Copy prompt: `Create a deployment readiness checklist for LovableHTML: domain verification, API key, worker env var, prerender endpoint test, origin fallback, SEO validation, and rollback path.`
- Validation: Checklist marks every dependency as present, missing, or unknown.

### HIGH - API Checker Has The Clearest Real-Time Element Map

- Area: interaction/workflow.
- URL: `https://www.apichecker.io/`
- Live position: `Test Your API` section.
- Locator: `Request Configuration`, `API Endpoint`, `HTTP Method`, `Authentication`, `Query Parameters`, `Test API`, `Response`, `History`, `Code Generator`.
- Workflow step: `1. Enter endpoint -> 2. Select method/auth -> 3. Add params/headers -> 4. Test API -> 5. Inspect response -> 6. Copy generated code`.
- Evidence: live page exposes the full tool UI in crawlable text.
- Problem: This is the model for the audit workbench's desired visibility: every workflow element can be located.
- Likely cause: Tool UI text is crawlable and semantically structured.
- Fix: Use this as the benchmark for future site audits.
- Copy prompt: `For each interactive element in the Test Your API flow, generate an issue/workflow row with label, expected action, dependency, status, and validation step.`
- Validation: Workflow map contains request config, auth, params, test button, response panel, history, and code generator.

### HIGH - CBT Therapist Production Claim Needs Live CTA/Form Position Capture

- Area: interaction/deployment.
- URL: `https://community.vercel.com/t/a-small-v0-project-that-turned-into-a-real-success/28538`
- Live position: source post -> production workflow description.
- Locator: custom contact form with Resend; dashboard with Neon and Vercel Blob; live site `https://www.psicjazmin.com/`.
- Workflow step: `1. Visitor lands -> 2. Contact/booking form -> 3. Resend email capture -> 4. Admin uploads resources -> 5. Neon/Vercel Blob store data/files`.
- Evidence: author states the project became a real production project with custom contact form, domain, dashboard, Neon, and Vercel Blob.
- Problem: Source evidence is strong, but the visual audit still needs exact button/form positions on the live site.
- Likely cause: Community post describes architecture; it does not enumerate DOM/page positions.
- Fix: Browser pass should capture hero CTA, contact form route, resource upload/dashboard entry if public, and confirmation/error states.
- Copy prompt: `Audit psicjazmin.com and locate the appointment/contact CTA, contact form fields, resource area, and any visible admin/dashboard entry. Record section, label, destination, dependency, and missing states.`
- Validation: Issue cards include exact page area and element label for the contact/booking path.

### HIGH - Committed Citizens Has A Clear CMS Gap Location

- Area: content/deployment.
- URL: `https://community.vercel.com/t/adding-a-cms-to-my-new-vibe-coded-website/37898`
- Live position: source post -> `/insights` content system discussion.
- Locator: text match: "9 hard coded articles on the /insights page"; "next step is to integrate a headless CMS"; form captures use Resend.
- Workflow step: `1. Publish consulting site -> 2. Add insights articles -> 3. Need colleagues to add content -> 4. Integrate CMS`.
- Evidence: author explicitly says the CMS is missing and why.
- Problem: This is exactly the type of deployment/workflow gap the audit should expose.
- Likely cause: v0 can generate static content quickly, but editorial workflows need CMS/admin ownership.
- Fix: Add CMS readiness issue card covering content model, editor roles, preview, migration, and publish workflow.
- Copy prompt: `Add a CMS plan for the /insights section: content schema, author/editor roles, migration of existing hard-coded articles, preview flow, deployment env vars, and rollback plan.`
- Validation: New articles can be created without editing source code or relying on a v0 chat.

### HIGH - RevCrew.ai Provides Full-Stack Workflow Positions At Source Level

- Area: workflow/deployment.
- URL: `https://replit.com/gallery/work/marketing-and-sales/revcrew-ai`
- Live position: Replit Gallery description.
- Locator: multiple pages, contact forms, blog component, user/admin auth, backend database, deployed link.
- Workflow step: `1. Marketing page -> 2. Contact form -> 3. Blog read/create/edit -> 4. User/admin auth -> 5. Database persistence`.
- Evidence: Replit Gallery explicitly describes these components.
- Problem: Great source-level workflow map, but live app interaction still needs per-button/route verification.
- Likely cause: Gallery summarizes capabilities, not test results.
- Fix: Run live app pass to locate contact form, blog editor/admin entry, login path, and database-backed content changes.
- Copy prompt: `Audit RevCrew.ai live app. Locate contact form, blog list, blog admin/editor path, login/admin auth entry, and database-backed content evidence. Record exact URLs, labels, and broken/missing states.`
- Validation: Workflow table includes public and admin paths with dependency status.

### MEDIUM - Event RSVP Is A Template Flow, Not A Verified Business

- Area: workflow/classification.
- URL: `https://replit.com/gallery/life/productivity/event-rsvp-template`
- Live position: Replit Gallery description.
- Locator: public event pages, shareable URLs, RSVP forms, admin dashboard, guest lists, React/Express/PostgreSQL, remix template.
- Workflow step: `1. Create event -> 2. Share public URL -> 3. Guest RSVP -> 4. Admin manages guest list`.
- Evidence: Gallery describes the full app structure and template/remix status.
- Problem: It is very useful structurally, but should not be presented as a proven production business.
- Likely cause: Template galleries optimize for remixability rather than live business proof.
- Fix: Label as "workflow skeleton" and require production proof before moving to priority business cases.
- Copy prompt: `Use Event RSVP as a form/admin/data-flow template. Before recommending as a business case, verify a deployed instance, real event page, form submission, admin access model, and persistence.`
- Validation: Recommendation list marks it as template/reference, not production proof.

## At-a-Glance Deployment Gap Table

| Case | Domain | Backend/API | Database | Auth | Email/SMS | CMS/Admin | Monitoring/Analytics | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QuickTables | live domain known | unknown | unknown | unknown | SMS claimed | loyalty/admin unknown | unknown | Needs visual/workflow pass |
| LovableHTML | live domain known | prerender API | dashboard/domain verified | account/API key | not central | dashboard/docs | SEO validation implied | Deployment checklist needed |
| API Checker | live domain known | browser/API request flow | saved requests/history likely client-side | auth helpers for tested APIs | not central | no admin needed | unknown | Strong UI map |
| CBT Therapist | domain claimed | contact/dashboard | Neon claimed | admin dashboard claimed | Resend claimed | resource dashboard claimed | unknown | Needs live UI position pass |
| Committed Citizens | live domain claimed | form capture | unknown | unknown | Resend claimed | CMS missing | Cookiebot mentioned | CMS gap clear |
| RevCrew.ai | deployed link known | backend claimed | database claimed | user/admin auth claimed | contact forms claimed | blog admin claimed | unknown | Needs live route pass |
| Event RSVP | template/app page | Express claimed | PostgreSQL claimed | extension suggested | email extension suggested | admin dashboard claimed | unknown | Template, not production proof |

## Copyable Fix Pack

1. `Create a workflow map for this website. For each CTA, link, form, login, dashboard, and export/copy action, record URL, page area, element label, expected action, actual result, dependency, status, and validation step.`
2. `Create deployment readiness cards for this site covering domain/SSL, env vars, backend/API, database, auth, email/SMS, storage, CMS/admin, analytics, error monitoring, SEO metadata, sitemap, privacy/terms, and rollback path.`
3. `For every audit finding, include live position: URL, viewport, page area, element label, locator, workflow step, evidence, likely cause, fix, and validation.`
4. `Do not classify a template or demo as production-ready unless there is evidence of a real live domain, connected form/backend, persistence, and a user/admin workflow.`

## Result

Verdict: `PASS WITH NOTES`

The retest confirms that the audit workflow needs location-aware evidence. API Checker is the clearest example where the live page exposes exact interactive positions. Committed Citizens is the clearest example of a deployment/workflow gap because the CMS need is explicitly located at `/insights`. RevCrew and CBT Therapist have strong source-level workflow evidence but still need a live visual/browser pass to capture exact button and form locations.
