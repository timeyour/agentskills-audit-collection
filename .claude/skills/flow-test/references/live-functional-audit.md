# Live Functional Audit

Use this reference when the user wants an agent to test every feature of a website, web app, open-source project, vibe-coded site, or deployed prototype.

## Goal

Walk the product like a real user. Do not only inspect screenshots or source claims. Execute each visible workflow as far as safely possible, record exactly where it works or fails, and produce copyable fixes.

## Scope

Audit these feature types when present:

- Navigation and routing.
- CTA buttons.
- Contact, booking, lead, newsletter, signup, login, checkout, RSVP, upload, search, filter, sort, copy, export, and share flows.
- Forms, including validation, required fields, success states, error states, loading states, and empty states.
- Auth-gated or admin-gated routes.
- Dashboards and CRUD actions.
- Data persistence after refresh or navigation.
- Email, SMS, payment, storage, CMS, database, and analytics dependencies.
- Mobile and desktop behavior.
- Visual style, brand consistency, accessibility, performance, SEO, and trust signals.

## Execution Order

1. Discover the web surface
   - Use `web-surface-discovery.md` for websites and web apps before detailed clicking.
   - Map pages, controls, media, documents, network/API, storage/session, and security-sensitive surfaces.
   - Prioritize surfaces as `P0`, `P1`, `P2`, `skip-safe`, or `unknown`.

2. Apply permission boundary
   - Use `permission-model.md` before any live interaction.
   - Record whether the run is public read-only, safe click/navigation, test account, staging authorized, or production guarded.
   - Mark payment, deletion, private data, production mutation, or unclear high-risk actions as `SKIPPED-SAFE`.

3. Inventory features
   - Crawl or inspect navigation, visible buttons, forms, routes, modals, footer links, dashboard actions, and public docs.
   - Create a feature map before clicking deeply.

4. Define expected behavior
   - For each feature, state what should happen.
   - Mark external, destructive, payment, or private actions as "safe boundary" before executing.

5. Execute safe flows
   - Use browser automation or manual browser steps when available.
   - Capture URL, viewport, page area, element label, selector/text locator, and step number.
   - Record actual result, console/network errors, visual state, and confirmation/error messages.

6. Test edge states
   - Empty form.
   - Invalid email/phone/password.
   - Duplicate submission.
   - Back/refresh.
   - Deep links and route aliases, including old shared URLs and redirects.
   - Mobile viewport.
   - Slow/loading state if observable.
   - Auth-required route without login.

7. Inspect visual quality
   - First viewport clarity.
   - Layout, spacing, alignment, typography, colors, components, images, icon style, and mobile fit.
   - Look for inconsistent sections, template-clone artifacts, broken responsive behavior, and weak trust/conversion cues.

8. Inspect deployment readiness
   - Domain and SSL.
   - Environment variables.
   - Backend/API.
   - Database.
   - Auth/session.
   - Email/SMS/payment/storage providers.
   - CMS/admin editing.
   - Analytics and error monitoring.
   - SEO metadata, sitemap, robots, Open Graph.
   - Privacy, terms, compliance, and data export/backup when relevant.

9. Produce issue cards
   - Use one issue card per actionable problem.
   - Include copyable prompts for fixes.

## Optional Open-Source Tooling

Use available open-source tools as evidence generators:

- Playwright: browser flows, screenshots, locators, console and network logs.
- axe-core: accessibility violations.
- Lighthouse: performance, SEO, best practices, accessibility signals.
- Link checkers: dead links and redirect chains.
- HTML/CSS linters: malformed markup or style issues.
- Screenshot diff tools: visual regressions across viewports.

If tools are unavailable, clearly mark the audit as manual/source-level and list what a tool pass must verify.

## Feature Row Format

```markdown
| Feature | Start URL | Live Position | Steps Run | Expected | Actual | Evidence | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Status values:

- `PASS`: works as expected.
- `PARTIAL`: usable but has gaps.
- `FAIL`: broken or blocks the user.
- `UNKNOWN`: source evidence exists but live execution was not possible.
- `SKIPPED-SAFE`: destructive, payment, private, or requires credentials.

## Issue Card Format

```markdown
### <S0-S4> - <Feature or Visual Issue>

- Area:
- URL:
- Live position:
- Locator:
- Workflow step:
- Expected:
- Actual:
- Evidence:
- Problem:
- Likely cause:
- Fix:
- Copy prompt:
- Validation:
```

Severity:

- `S0`: blocks launch or delivery; core workflow unavailable, data/security risk, or production dependency missing.
- `S1`: seriously hurts conversion, trust, correctness, privacy, or operational reliability.
- `S2`: noticeable UX, workflow, visual, accessibility, or deployment issue; temporary launch possible with known risk.
- `S3`: polish, copy, layout, or minor interaction improvement.
- `S4`: future enhancement or benchmark idea.

## Visual Score Rubric

Score 0-100:

- 20: first viewport clarity and conversion focus.
- 20: layout, spacing, alignment, and responsive behavior.
- 15: typography, color, component consistency, and style polish.
- 15: content hierarchy, copy clarity, and trust signals.
- 15: visual asset relevance and loading quality.
- 15: accessibility basics, contrast, keyboard focus, and readable states.

## Functional Score Rubric

Score 0-100:

- 20: navigation/routing works.
- 20: primary CTA and conversion flow works.
- 20: forms and validation work.
- 15: data persistence, auth, or backend behavior works when applicable.
- 15: error/loading/empty states are clear.
- 10: mobile flow remains usable.

## Anti-Patterns

- Saying "looks good" without checking flows.
- Clicking only the primary CTA and ignoring forms, footer links, errors, and mobile.
- Treating source claims as live behavior.
- Running tools but failing to translate results into user-visible issues.
- Reporting a problem without exact location and copyable fix text.
