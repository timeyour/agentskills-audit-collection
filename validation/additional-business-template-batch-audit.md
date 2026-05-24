# Additional Batch Validation: Business, Template, and Live Workflow Evidence

Date: 2026-05-19

## Audit Summary

- Target: Newly supplied vibe-coded / AI-built website case list
- Target type: Source pages, live websites, template galleries, open-source or remix examples
- Audit level: Source pass + safe live URL text pass where available
- Verdict: `PASS WITH NOTES`
- Biggest blocker: Several cases have strong source claims but missing or failing live evidence in this environment.
- Fix first: Separate `true live business`, `workflow skeleton`, `template`, and `source-only candidate` before adding them to the 200-site benchmark.

## Evidence Split

| Case | Platform | Source Locator | Live Evidence | Confidence | Verdict |
| --- | --- | --- | --- | --- | --- |
| LovableHTML | Lovable | `https://madewithlovable.com/projects/lovablehtml` says it makes Lovable sites SEO-friendly with crawlable HTML, Cloudflare Workers, fast global delivery, and 50+ users. | `https://lovablehtml.com/` exposes a clear product landing page, CTA, docs, and deployment-oriented SEO workflow. | High | `PASS` |
| GitFolio | v0 / Vercel Community | `https://community.vercel.com/t/gitfolio-github-to-portfolio-in-seconds/37367` describes GitHub username -> hosted portfolio. | `https://gitfolio.in/` exposes GitHub username input and portfolio generation CTA. | High | `PASS` |
| Jobs | v0 / Vercel Community | `https://community.vercel.com/t/jobs-ai-powered-job-matching-platform/32747` describes `jobs.md`, resume upload, AI matching, live site, and source repo. | Live URL from source page did not resolve in current fetch pass. | Medium | `PASS WITH NOTES`, live retest required |
| Telegram Photography Portfolio | v0 / Vercel Community | `https://community.vercel.com/t/telegram-as-a-storage-completely-zero-cost-photography-portfolio/30230` describes Telegram as storage, Firebase config, FireCMS, MVP status, live site, and repo. | Live URL from source page did not resolve in current fetch pass. | Medium | `PASS WITH NOTES`, live retest required |
| RevCrew.ai | Replit | `https://replit.com/gallery/work/marketing-and-sales/revcrew-ai` describes a production-ready company site with pages, contact forms, blog, user/admin auth, and backend database. | Gallery gives a View App path, but a full clicked-flow pass still needs browser execution. | High source, medium live | `PASS WITH NOTES` |
| Event RSVP Template | Replit | `https://replit.com/gallery/life/productivity/event-rsvp-template` describes public event pages, RSVP forms, admin dashboard, guest lists, React/Express/PostgreSQL. | It is a remix template, not proof of a real event business. | High as template | `WORKFLOW SKELETON` |
| Simple Portfolio Template | v0 / Vercel Community | `https://community.vercel.com/t/simple-portfolio-template-made-with-v0/15855` presents a simple portfolio template made with v0 prompts. | Template/demo evidence only. | High as template | `LOW PRIORITY` |
| Paperfolio | v0 / Vercel Community | `https://community.vercel.com/t/cooked-this-paperfolio-template-with-v0/28655` presents a Paperfolio-inspired template created through prompts. | Template/layout recreation evidence only. | High as template | `LOW PRIORITY` |
| Lovable Templates | Lovable | `https://lovable.dev/templates` is an official template library. | Useful prompt/layout reference, not proof of operated businesses. | High as template library | `REFERENCE ONLY` |
| Made with Lovable Websites | Lovable | `https://madewithlovable.com/categories/websites` is a high-density gallery for website examples including service and brand sites. | Individual project cards need per-site live workflow passes. | High as discovery source | `DISCOVERY SOURCE` |
| Bolt Gallery | Bolt | `https://bolt.new/gallery` exists as a gallery entry point. | Public text evidence is thinner than Lovable/v0/Replit for this batch. | Medium | `DISCOVERY SOURCE`, not priority |

## Priority Classification

| Priority | Cases | Why |
| --- | --- | --- |
| P1 true workflow candidates | LovableHTML, GitFolio, Jobs, Telegram Photography Portfolio, RevCrew.ai | These have clear product/workflow claims beyond a static marketing page. |
| P2 reusable app skeletons | Event RSVP Template | Strong form/admin/database pattern, but it is a template/remix case. |
| P3 visual/layout references | Simple Portfolio Template, Paperfolio, Lovable Templates | Useful for layout and prompt study; weak for business-loop validation. |
| P4 discovery sources | Made with Lovable Websites, Bolt Gallery | Good places to find candidates; not single-site proof. |

## Feature Inventory

| Case | Feature / Workflow | Start URL | Live Position | Dependency | Safe To Execute | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LovableHTML | SEO prerender / crawlable HTML conversion | `https://lovablehtml.com/` | Hero CTA, docs, Cloudflare Workers setup | Domain verification, API key, Cloudflare Worker, prerender endpoint | Yes, until account/API key boundary | `PARTIAL-PASS` |
| GitFolio | GitHub username -> portfolio generation | `https://gitfolio.in/` | Hero input: GitHub username; CTA: create portfolio | GitHub public API, route generation, hosted portfolio pages | Yes, with public usernames | `PARTIAL-PASS` |
| Jobs | Resume upload -> AI job match | Source page live link | Source claim: upload resume and match against `jobs.md` postings | File upload, AI matching, storage, privacy, repo/job schema | Yes with dummy resume if live opens | `UNKNOWN-LIVE` |
| Telegram Photography Portfolio | Gallery content from Telegram storage | Source page live link | Source claim: Telegram image storage + Firebase / FireCMS | Telegram media access, Firebase config, FireCMS admin, image optimization | Public gallery yes; admin no | `UNKNOWN-LIVE` |
| RevCrew.ai | Marketing site + contact + blog + auth/admin | Replit View App / `https://revcrew.ai/` | Gallery description: pages, forms, blog, auth, database | Backend DB, auth/session, contact delivery, blog admin | Public pages/forms yes; admin no | `SOURCE-PASS` |
| Event RSVP Template | Create/share event -> RSVP -> admin guest list | Replit gallery app/template | Gallery description: public pages, RSVP forms, admin dashboard | Express API, PostgreSQL, admin auth, optional email | Template safe; production proof absent | `TEMPLATE-PASS` |
| Simple Portfolio Template | Portfolio layout | Community post | Template preview/remix | Static frontend | Yes | `LAYOUT-ONLY` |
| Paperfolio | Portfolio layout recreation | Community post | Template/remix | Static frontend | Yes | `LAYOUT-ONLY` |

## Position-Aware Issue Cards

### HIGH - Jobs Has Strong Product Logic But No Live Pass Yet

- Area: source/live mismatch.
- URL: `https://community.vercel.com/t/jobs-ai-powered-job-matching-platform/32747`
- Live position: source post -> live app link.
- Locator: `jobs.md`, resume upload, AI-powered job matching, open-source repo.
- Workflow step: `1. Employer writes jobs.md -> 2. Candidate uploads resume -> 3. AI ranks matches -> 4. Candidate sees matched jobs`.
- Expected: Live site opens and accepts a safe dummy resume test.
- Actual: Live URL did not resolve in current fetch pass.
- Evidence: Source page describes the full product loop; live execution is missing.
- Problem: It cannot be counted as live-verified until upload, matching, empty state, invalid file, and result page are tested.
- Likely cause: Deployment unavailable, domain down, bot-blocking, or environment-specific network failure.
- Fix: Browser retest the live URL and, if unavailable, clone/open-source repo pass to inspect upload/matching implementation.
- Copy prompt: `Audit Jobs as a resume-matching flow. Test live availability, dummy PDF upload, invalid file upload, empty jobs.md state, match result quality, privacy copy, and repo deployment requirements.`
- Validation: A workflow table contains upload field, submit button, loading state, match result, invalid-file error, and data/privacy dependency.

### HIGH - Telegram Portfolio Storage Architecture Is Interesting But Fragile

- Area: deployment/storage.
- URL: `https://community.vercel.com/t/telegram-as-a-storage-completely-zero-cost-photography-portfolio/30230`
- Live position: source post -> live portfolio link and repo link.
- Locator: Telegram as image storage, Firebase, FireCMS, MVP.
- Workflow step: `1. Upload/manage photo -> 2. Store or reference Telegram media -> 3. Render gallery -> 4. Edit metadata in Firebase/FireCMS`.
- Expected: Public gallery loads images reliably, with admin/storage assumptions documented.
- Actual: Live URL did not resolve in current fetch pass.
- Evidence: Source page describes architecture and live/repo links.
- Problem: Telegram-as-storage can break on rate limits, URL expiry, permissions, image optimization, and CDN behavior.
- Likely cause: Low-cost architecture trades operational certainty for simplicity.
- Fix: Require an explicit storage-readiness checklist before treating it as production-ready.
- Copy prompt: `Audit the Telegram portfolio storage flow. Verify public image loading, broken image state, mobile gallery performance, Firebase config, FireCMS admin boundary, backup/export plan, and what happens if Telegram media URLs change.`
- Validation: At least one public gallery page loads, broken-media states are visible, and deployment docs list storage and backup risks.

### MEDIUM - Event RSVP Is A Good Skeleton, Not A Proven Business Case

- Area: classification.
- URL: `https://replit.com/gallery/life/productivity/event-rsvp-template`
- Live position: gallery description and remix/template metadata.
- Locator: public event pages, RSVP forms, admin dashboard, guest lists, PostgreSQL.
- Workflow step: `1. Event page -> 2. Guest RSVP -> 3. Admin sees guest list/statistics`.
- Expected: Treat as reusable workflow skeleton.
- Actual: The supplied conclusion groups it with true business/live examples.
- Evidence: Replit page presents it as a template/remix.
- Problem: It is very useful for learning form/admin/data flow, but not proof that a real deployed event product is operating.
- Likely cause: Gallery templates feel like live products because they have complete app structure.
- Fix: Keep it in the benchmark as `workflow skeleton`, not `true business`.
- Copy prompt: `Use Event RSVP as a reference app skeleton. Before classifying it as production, verify a real event URL, form submission persistence, admin auth, email notification, spam protection, and guest export.`
- Validation: Classification field remains `template/skeleton` until production proof exists.

### MEDIUM - Portfolio Templates Should Not Pollute The Business Benchmark

- Area: benchmark hygiene.
- URL: `https://community.vercel.com/t/simple-portfolio-template-made-with-v0/15855` and `https://community.vercel.com/t/cooked-this-paperfolio-template-with-v0/28655`
- Live position: community post/template preview.
- Locator: made with v0 prompts; Paperfolio-inspired template.
- Workflow step: `1. View template -> 2. Remix/copy layout -> 3. Replace content`.
- Expected: Use for layout/aesthetic references only.
- Actual: These are sometimes mixed with real product cases.
- Evidence: Both source pages frame the work as a template/layout exercise.
- Problem: Templates help page quality study but do not test conversion, backend, deployment, or business workflow.
- Likely cause: Visual polish is being mistaken for product completeness.
- Fix: Put templates in a separate visual-reference lane.
- Copy prompt: `Audit this portfolio template only for layout, hierarchy, typography, responsiveness, and component consistency. Do not score it as a business workflow unless it has live forms, backend, deployment dependencies, or user actions beyond navigation.`
- Validation: Report separates `visual score` from `workflow/deployment score`.

### MEDIUM - LovableHTML Needs Deployment Checklist Treatment

- Area: deployment.
- URL: `https://lovablehtml.com/`
- Live position: homepage CTA and docs links.
- Locator: crawlable HTML, SEO, Cloudflare Workers, API key/domain-style setup.
- Workflow step: `1. Add site/domain -> 2. Generate or configure prerender -> 3. Deploy worker -> 4. Validate crawler output`.
- Expected: Product claims should convert into a deployment checklist.
- Actual: Landing page communicates value, but a buyer still needs dependency-level validation.
- Evidence: Live site and project page both point to SEO/deployment functionality.
- Problem: The audit should test SEO output, not just accept the landing-page claim.
- Likely cause: SEO tools often look correct until crawler output is inspected.
- Fix: Add a dedicated SEO crawler pass: rendered HTML, title/meta, canonical, sitemap, robots, Open Graph, and page speed.
- Copy prompt: `Audit LovableHTML deployment readiness: verified domain, API key, Cloudflare Worker config, prerender endpoint, crawler-visible HTML, sitemap, robots, title/meta, canonical, OG tags, fallback behavior, and rollback.`
- Validation: A before/after crawler comparison proves the target Lovable page became indexable.

## Deployment Gap Table

| Case | Domain / SSL | Backend/API | Database | Auth | Upload/Storage | Email/SMS | CMS/Admin | SEO/Analytics | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LovableHTML | Live domain seen | Prerender/API implied | Unknown | Account/API key likely | Not central | Not central | Dashboard/docs likely | Core value | Needs deployment proof |
| GitFolio | Live domain seen | GitHub API likely | Unknown | Probably optional | GitHub profile data | Not central | Portfolio generation/admin unknown | Portfolio SEO unknown | Needs generated portfolio retest |
| Jobs | Source live link only | AI matching claimed | Unknown | Unknown | Resume upload | Unknown | Employer job source via `jobs.md` | Unknown | Live unavailable in fetch |
| Telegram Portfolio | Source live link only | Firebase claimed | Firebase claimed | FireCMS/admin boundary | Telegram image storage | Not central | FireCMS claimed | Image SEO/perf unknown | Live unavailable in fetch |
| RevCrew.ai | Gallery deployed app | Backend claimed | Database claimed | User/admin auth claimed | Unknown | Contact form likely | Blog/admin claimed | Unknown | Needs clicked live pass |
| Event RSVP | Replit template/app | Express claimed | PostgreSQL claimed | Admin dashboard claimed | Guest list data | Optional extension | Admin dashboard | Unknown | Template only |

## Five-Pass Acceptance Plan For This Batch

| Pass | What To Do | Must Produce |
| --- | --- | --- |
| 1. Source pass | Verify source page, live link, repo link, author claim, platform classification. | Evidence table with confidence. |
| 2. Functional pass | Open live site, click primary CTA, forms, uploads, generated outputs, and admin/login boundary. | Feature execution log with exact page positions. |
| 3. Edge/failure pass | Test invalid username, invalid resume file, empty form, broken image, missing route, mobile. | Error-state issue cards. |
| 4. Visual/deployment pass | Score first viewport, hierarchy, spacing, trust, mobile, domain, backend, DB, auth, email, storage, CMS. | Visual score + deployment gap table. |
| 5. Retest/learning pass | Re-run fixes or reclassify cases; update benchmark labels. | Learning ledger and benchmark update. |

## Updated Verdict On Supplied Conclusion

The conclusion is directionally correct, but needs stricter labels:

- `True priority`: LovableHTML, GitFolio, Jobs, Telegram Photography Portfolio, RevCrew.ai.
- `Priority but source/live gap`: Jobs and Telegram Photography Portfolio need live retest before being counted as passed.
- `Workflow skeleton`: Event RSVP Template.
- `Visual/template reference`: Simple Portfolio Template, Paperfolio, Lovable official templates.
- `Discovery source`: Made with Lovable Websites and Bolt Gallery.

## Copyable Fix Pack

1. `For each site, create a source-vs-live evidence table. Do not mark PASS unless the live URL opens and at least the primary workflow can be executed or safely bounded.`
2. `For every CTA, form, upload, generated output, login/admin boundary, dashboard, copy/share/export action, record URL, page area, element label, expected behavior, actual behavior, dependency, and status.`
3. `Separate cases into true business, workflow skeleton, visual template, source-only candidate, and discovery source. Never mix templates into production benchmarks.`
4. `For AI-built product cases, add deployment cards for domain/SSL, env vars, backend/API, database, auth, email/SMS, file storage, CMS/admin, analytics, SEO, privacy, backup, and rollback.`

## Experience Ledger

- Repeated failure pattern: Community/gallery claims often describe product scope, but live sites may be unavailable or untested.
- Repeated classification trap: Templates with polished UI are easy to mistake for business workflows.
- Good benchmark examples: LovableHTML for deployment/SEO product workflow; GitFolio for input-to-output generation; Event RSVP for form/admin/database skeleton.
- Guardrail update: Every 200-site benchmark row needs `source_status`, `live_status`, `workflow_status`, `visual_status`, and `deployment_status` separately.

## Final Verdict

Verdict: `PASS WITH NOTES`

This batch is useful and should be added to the benchmark, but not all rows are equal. LovableHTML and GitFolio can enter the priority pool immediately. Jobs and Telegram Photography Portfolio are strong candidates but need live browser retesting. Event RSVP should be used as a workflow skeleton. Portfolio templates and official template libraries belong in the visual-reference lane, not the true-business lane.
