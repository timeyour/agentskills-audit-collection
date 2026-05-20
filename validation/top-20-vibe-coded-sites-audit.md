# Top 20 Vibe-Coded Sites: Audit Validation

Date: 2026-05-19

## Audit Summary

- Target: User-supplied list of 20 vibe-coded / AI-built websites.
- Target type: Live sites, gallery entries, community posts, remix templates, and tool/product pages.
- Audit level: Source evidence pass + safe live text pass where available.
- Verdict: `PASS WITH NOTES`
- Main correction: The list is useful, but the A/B split needs stricter audit labels. Some A-list cases are source-strong but not live-verified; PhoneValidation is stronger than its B-list placement; Event RSVP and Course Platform are templates, not proven live businesses.

## Corrected Classification

| # | Case | Original class | Corrected audit class | Evidence status | Why |
| --- | --- | --- | --- | --- | --- |
| 1 | QuickTables | A | `SOURCE-STRONG, LIVE-THIN` | Source page confirms restaurant growth system; live text only exposes title. | Good business thesis, but direct ordering/SMS/loyalty flow needs browser pass. |
| 2 | LovableHTML / Encited | A | `A1 PRIORITY` | Source and live site both expose SEO/prerender workflow. | Strong micro-SaaS and deployment-readiness benchmark. |
| 3 | hoffmannarchitektur.live | A | `VISUAL/SERVICE REFERENCE` | Lovable card confirms architecture/service positioning; live text sparse. | Useful for premium service-site aesthetics, not yet a workflow benchmark. |
| 4 | Heavy DOOTY | A | `LOCAL SERVICE REFERENCE` | Lovable card and live title confirm pet waste / yard cleanup service. | Useful local service archetype; CTA/form must be mapped visually. |
| 5 | MAtchWise | A | `SOURCE-STRONG, LIVE-THIN` | Lovable card says AI ATS platform; live text sparse. | Promising workflow, but candidate/admin flows are unverified. |
| 6 | Planoraa | A | `SOURCE-STRONG, LIVE-THIN` | Lovable card says tasks, budgets, guest lists, dashboard; live text sparse. | Strong app concept, but dashboard workflow needs click test. |
| 7 | API Checker | A | `A1 PRIORITY` | Source and live page expose full API testing UI. | Best live workflow map in this batch. |
| 8 | Jobs | A | `A1 CANDIDATE, LIVE RETEST` | Vercel source describes resume upload, jobs.md, matching, GitHub/company management. | Very strong product loop, but live site did not resolve in current pass. |
| 9 | GitFolio | A | `A1 PRIORITY` | Source and live page expose GitHub -> portfolio flow. | Clear input/output/productization pattern. |
| 10 | Telegram Photography Portfolio | A | `A1 CANDIDATE, LIVE RETEST` | Source describes Telegram storage, Firebase DB, dashboard, open source. | Strong architecture case, but live site did not resolve in current pass. |
| 11 | RevCrew.ai | A | `A1 SOURCE-STRONG` | Replit source describes pages, contact forms, blog, user/admin auth, backend DB. | Excellent full-stack workflow candidate; clicked live/admin pass still needed. |
| 12 | Event RSVP Template | A | `WORKFLOW SKELETON` | Replit source confirms public event pages, RSVP forms, admin dashboard, PostgreSQL. | Great reusable pattern, but it is a remix template. |
| 13 | PhoneValidation.app | B | `UPGRADE TO A2` | Lovable card and live site expose CSV upload, test number, pricing, credits, history. | More complete commercial tool than several A-list source-only cases. |
| 14 | RAGcanvas | B | `B SOURCE-ONLY` | Lovable card says AI-driven RAG chatbot builder; live text sparse. | Big platform claim; needs actual builder/upload/bot test. |
| 15 | SwiftROI | B | `B TOOL/CALCULATOR` | Replit source confirms ROI calculator, campaign tracking, dynamic calculation engine. | Useful calculator/product pattern, not full business workflow. |
| 16 | SaaStr.ai VC Valuation Calculator | B | `B TOOL/CALCULATOR` | Replit source confirms VC-round dataset, valuation calculator, usage claim. | Strong single-purpose lead magnet, not broad app. |
| 17 | Proudwork.io | B | `B CREATOR PROFILE TOOL` | Replit source confirms creator profiles and embeds from Drive/Dropbox/Instagram. | Useful portfolio/product pattern, lower priority than service/SaaS/admin cases. |
| 18 | GuruQore | B | `B LANDING PAGE` | Replit source confirms course overview, curriculum preview, enrollment flow. | Good course launch page; weaker backend evidence. |
| 19 | Course Platform | B | `TEMPLATE/SKELETON` | Replit source confirms Notion-powered learning platform and remix template. | Good course/product skeleton, but template status must stay visible. |
| 20 | Wayfinder Calculator | B | `B TOOL/CALCULATOR` | Replit source confirms maritime fuel savings calculator with real-time prices and visualizations. | Useful vertical calculator, not first-priority business system. |

## Validated A1 Pool

These are the best first-round audit targets because they expose a clear workflow, product promise, or deployment map:

| Case | Why it belongs |
| --- | --- |
| LovableHTML / Encited | SEO/prerender/AI-search platform with visible setup and deployment dependencies. |
| API Checker | Public interactive API testing UI with request config, auth, params, test button, response, history, and code generator. |
| GitFolio | Clear GitHub login / template / hosted portfolio flow. |
| PhoneValidation.app | Clear commercial flow: free credits, test number, CSV upload, validation, download, pricing, history. |
| Jobs | Strong resume/job matching product logic; must retest live availability. |
| Telegram Photography Portfolio | Strong open-source architecture example; must retest live availability and storage reliability. |
| RevCrew.ai | Strong full-stack source evidence: forms, blog, auth/admin, database. |

## Cases That Need Downgrade Labels

| Case | Downgrade label | Reason |
| --- | --- | --- |
| QuickTables | `SOURCE-STRONG, LIVE-THIN` | Source claims direct ordering, SMS, loyalty; live crawl does not expose button/form positions. |
| MAtchWise | `SOURCE-STRONG, LIVE-THIN` | AI ATS claim exists, but no verified candidate/employer/admin flow yet. |
| Planoraa | `SOURCE-STRONG, LIVE-THIN` | Dashboard/task/budget/guest-list claim exists, but no verified workflow positions yet. |
| hoffmannarchitektur.live | `VISUAL/SERVICE REFERENCE` | Good premium service-site candidate, but not a functional workflow case yet. |
| Heavy DOOTY | `LOCAL SERVICE REFERENCE` | Good local-service archetype, but quote/contact flow needs visual click pass. |
| Event RSVP Template | `WORKFLOW SKELETON` | Excellent pattern, but source marks it as remix template. |
| Course Platform | `TEMPLATE/SKELETON` | Good learning-platform skeleton, but source marks it as remix template. |

## Feature Inventory: First Pass

| Case | Primary workflow to test next | First live/source position | Key dependency | Current status |
| --- | --- | --- | --- | --- |
| QuickTables | Restaurant site -> direct ordering -> SMS/loyalty signup | Made with Lovable summary + `quicktables.info` | Ordering backend, SMS, loyalty DB | `UNKNOWN-LIVE` |
| LovableHTML / Encited | Site/domain setup -> prerender -> crawler-visible HTML -> SEO/AI citation tracking | `lovablehtml.com` redirects to Encited page with docs/pricing/CTA | DNS, prerender proxy/API, crawler output, SEO metadata | `PARTIAL-PASS` |
| hoffmannarchitektur.live | Premium service page -> project/service CTA -> contact | Lovable category card + live title | Contact form, portfolio/case sections | `UNKNOWN-LIVE` |
| Heavy DOOTY | Local service page -> service details -> quote/contact | Lovable category card + live title | Lead form, local trust, service-area info | `UNKNOWN-LIVE` |
| MAtchWise | HR team -> job/candidate flow -> shortlist/dashboard | Lovable category card + live title | Auth, candidate data, ATS workflow | `UNKNOWN-LIVE` |
| Planoraa | Event plan -> tasks/budget/guests/dashboard | Lovable category card + live title | Dashboard persistence, auth, CRUD | `UNKNOWN-LIVE` |
| API Checker | Configure request -> test API -> inspect response -> copy code/export | Live API Checker page | Browser storage, outbound request, code generator | `SOURCE+LIVE-PASS` |
| Jobs | Resume upload -> database/web search -> ranked matches -> apply links | Vercel community source | PDF parsing, AI matching, jobs source, privacy | `LIVE-RETEST` |
| GitFolio | GitHub login/URL -> template -> hosted portfolio | Live GitFolio page | GitHub OAuth/API, template generation, hosting | `PARTIAL-PASS` |
| Telegram Portfolio | Upload/manage photos -> Telegram storage -> Firebase gallery -> dashboard edits | Vercel community source | Telegram media, Firebase DB, FireCMS/admin | `LIVE-RETEST` |
| RevCrew.ai | Marketing pages -> contact form -> blog/admin auth -> DB persistence | Replit Gallery source | Contact backend, auth, database | `SOURCE-PASS` |
| Event RSVP | Public event page -> RSVP form -> admin guest list | Replit Gallery source | Express, PostgreSQL, admin auth | `TEMPLATE-PASS` |
| PhoneValidation.app | Test number -> signup -> CSV upload -> validate -> download results | Live PhoneValidation page | Credits, phone validation provider, CSV processing, account history | `PARTIAL-PASS` |
| RAGcanvas | Create RAG chatbot -> train on content -> deploy/chat | Lovable category card + live title | File/content ingestion, embeddings/vector DB, chat widget | `SOURCE-ONLY` |
| SwiftROI | Enter campaign metrics -> calculate ROI -> track results | Replit Gallery source | Dynamic calculator engine, persistence unknown | `SOURCE-PASS` |
| SaaStr.ai | Enter startup metrics -> calculate valuation | Replit Gallery source | VC-round data source, formula/model freshness | `SOURCE-PASS` |
| Proudwork.io | Create profile -> embed media -> share profile link | Replit Gallery source | Drive/Dropbox/Instagram embeds, account/profile storage | `SOURCE-PASS` |
| GuruQore | Course landing -> curriculum preview -> enrollment/community CTA | Replit Gallery source | Enrollment/payment/community link | `SOURCE-PASS` |
| Course Platform | Notion modules -> access control -> learner progress | Replit Gallery source | Notion, auth/access, progress tracking | `TEMPLATE-PASS` |
| Wayfinder Calculator | Vessel/fuel inputs -> savings + CO2 visualization | Replit Gallery source | Fuel price feed, vessel data, calculator logic | `SOURCE-PASS` |

## Issue Cards

### HIGH - A-list Contains Source-Only Cases

- Area: classification.
- URL: `https://madewithlovable.com/categories/websites`
- Live position: gallery cards for QuickTables-adjacent service/app cases and individual sparse live pages.
- Locator: QuickTables, MAtchWise, Planoraa, hoffmannarchitektur.live, Heavy DOOTY.
- Workflow step: `source card -> live site -> primary CTA/form/dashboard`.
- Expected: A-list cases should expose a verified workflow or at least clickable live positions.
- Actual: Several A-list cases only have source/card evidence or sparse live text.
- Problem: This can make the benchmark look stronger than it is.
- Likely cause: Gallery cards summarize product intent, not working flows.
- Fix: Split A into `A1 live-verifiable`, `A2 source-strong`, and `visual/service reference`.
- Copy prompt: `For this Made with Lovable case, open the live site and map every CTA, form, dashboard entry, pricing link, contact route, and backend dependency. Do not mark PASS until the workflow has URL, page area, element label, expected behavior, actual behavior, and status.`
- Validation: Each A-list row has `source_status`, `live_status`, `workflow_status`, and `deployment_status`.

### HIGH - Jobs And Telegram Portfolio Need Live Availability Retest

- Area: live execution.
- URL: `https://community.vercel.com/t/jobs-ai-powered-job-matching-platform/32747` and `https://community.vercel.com/t/telegram-as-a-storage-completely-zero-cost-photography-portfolio/30230`
- Live position: source post live demo links.
- Locator: Jobs live demo; Telegram portfolio live demo.
- Workflow step: `open live site -> execute safe primary flow`.
- Expected: Jobs should allow safe dummy resume flow; Telegram portfolio should load a public gallery.
- Actual: Live URLs did not resolve in this current pass.
- Problem: Both are strong examples, but cannot count as live-passed.
- Likely cause: domain outage, app downtime, bot blocking, or network environment.
- Fix: Retest with browser and, if still down, use open-source repo pass.
- Copy prompt: `Retest the live site. If it opens, execute the public happy path and one failure state. If it does not open, capture status, DNS/SSL/HTTP evidence, and inspect the repo or source post for deployment dependencies.`
- Validation: The report contains either a live workflow log or a deployment failure card.

### MEDIUM - PhoneValidation Should Move Up

- Area: prioritization.
- URL: `https://phonevalidation.app/`
- Live position: hero, free credits CTA, phone number test, pricing, CSV upload claims.
- Locator: `Start with 100 Free Credits`, `Give it a try`, `Upload a CSV`, `Credit System`, pricing cards.
- Workflow step: `test one number -> signup -> upload CSV -> validate -> download -> review history`.
- Expected: B-list cases should be lower priority than A-list cases.
- Actual: PhoneValidation has clearer monetization, workflow, pricing, and tool UI than several A-list source-only cases.
- Problem: It was under-ranked.
- Likely cause: Single-function tools were treated as less valuable than broad platform claims.
- Fix: Promote to A2 and use it as a commercial micro-tool benchmark.
- Copy prompt: `Audit PhoneValidation.app as a commercial tool flow: test free phone input, signup boundary, CSV upload promise, validation states, pricing conversion, credit accounting, history/export, privacy, and data retention.`
- Validation: Primary tool flow has issue cards for input validation, CSV upload, pricing, and data/privacy dependencies.

### MEDIUM - Templates Must Stay In Their Own Lane

- Area: benchmark hygiene.
- URL: `https://replit.com/gallery/life/productivity/event-rsvp-template` and `https://replit.com/gallery/work/human-resources/course-platform`
- Live position: Replit Gallery source pages.
- Locator: `Remix Template`.
- Workflow step: `template -> remix -> customize -> production deployment`.
- Expected: Templates should be scored as skeletons.
- Actual: Event RSVP is listed among A-list "true business" examples.
- Problem: A template can teach workflow structure, but it is not a real operated business until a deployed instance is verified.
- Likely cause: Template pages contain complete product descriptions.
- Fix: Keep `template/skeleton` separate from `true live business`.
- Copy prompt: `Use this Replit template as a workflow skeleton. Before calling it production-ready, verify a real deployed app, form submission persistence, admin access model, email/payment integrations if relevant, and data export.`
- Validation: Benchmark row keeps `case_type=template` until production proof exists.

## 5-Pass Acceptance Plan For The First 6 Sites

| Pass | QuickTables | LovableHTML / Encited | API Checker | Jobs | RevCrew.ai | Event RSVP |
| --- | --- | --- | --- | --- | --- | --- |
| 1 Source | Confirm business claim and target live site. | Confirm LovableHTML -> Encited rebrand and SEO promise. | Confirm v0 build/source claims. | Confirm resume/jobs.md/search modes. | Confirm forms/blog/auth/database claims. | Confirm template status and stack. |
| 2 Functional | Find ordering, SMS, loyalty CTAs. | Check signup/docs/prerender setup boundary. | Test public GET request and code generator. | Upload dummy PDF if site opens. | Test contact form boundary and blog route. | Run guest RSVP on template/demo if available. |
| 3 Edge | Invalid order path, missing menu, SMS consent. | Missing domain/API key, crawler before/after. | Invalid URL, bad auth, empty endpoint. | Invalid file, no jobs, duplicate upload. | Empty form, invalid email, admin gate. | Duplicate RSVP, invalid email, refresh persistence. |
| 4 Visual/deploy | Mobile restaurant CTA visibility. | SEO audit output, docs clarity, pricing trust. | Dense tool UI mobile fit and copy buttons. | Privacy, upload trust, result explanations. | Service trust, admin/blog boundaries. | Template mobile/admin/data persistence. |
| 5 Retest/learn | Mark as true business or source-only. | Add deployment checklist benchmark. | Add as best workflow benchmark. | Keep or downgrade based on live result. | Keep as full-stack benchmark if live works. | Keep as skeleton unless production proof appears. |

## Revised Shortlist

Use this order for the next deep live/browser pass:

1. API Checker
2. PhoneValidation.app
3. GitFolio
4. LovableHTML / Encited
5. RevCrew.ai
6. Jobs
7. Telegram Photography Portfolio
8. Event RSVP Template
9. QuickTables
10. Planoraa

Reason: this order prioritizes cases where the workflow is visible, testable, monetizable, or architecturally useful.

## Final Verdict

Verdict: `PASS WITH NOTES`

The supplied 20-site list is good as a discovery batch, but it is not yet a clean validation batch. The strongest first-round examples are API Checker, PhoneValidation.app, GitFolio, LovableHTML / Encited, RevCrew.ai, Jobs, and Telegram Photography Portfolio. The biggest correction is to stop treating all A-list items as equally verified: some are only source-card promises, and templates must stay labeled as templates.
