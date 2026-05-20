# Original Vibe-Coded Website List: Position-Aware Batch Audit

Date: 2026-05-18

## Purpose

Retest the user's original full list of vibe-coded website sources and live examples using the location-aware audit format.

The goal is not just to say "worth looking at" or "not worth looking at." The goal is to show:

- where the evidence is;
- where the live workflow appears;
- where quality, interaction, or deployment gaps are likely;
- what still needs a visual/browser pass;
- what prompt can be copied to continue the audit.

## Audit Fields

- `Source locator`: where the tool attribution or project claim appears.
- `Live position`: the page area, element, or route to inspect.
- `Workflow signal`: the interaction, backend, form, CTA, or deployment dependency implied by the case.
- `Confidence`: high / medium / low.
- `Next audit action`: what to inspect next to make the case actionable.

## Entry Point Audit

| Entry | Source Locator | Live Position | Workflow Signal | Verdict |
| --- | --- | --- | --- | --- |
| Made with Lovable websites category | `https://madewithlovable.com/categories/websites` -> category count and project cards | Project cards with live links and categories | Good discovery layer for brand/service/site examples; weak for backend proof. | `PASS` |
| Replit Gallery | `https://replit.com/gallery` -> gallery count and project cards | `View App` links on gallery/project pages | Good for deployable app examples with database/auth/deployment claims. | `PASS` |
| Vercel Community / v0 Showcase | Individual Vercel Community posts | Live site links inside posts | Strong when posts explicitly say "built with v0" or describe production architecture. | `PASS WITH NOTES` |
| Bolt Gallery | `https://bolt.new/gallery` | Gallery page only | Entry point exists, but public text extraction is weak in this run. | `PASS WITH NOTES` |

## Lovable Cases

| Case | Source Locator | Live Position | Workflow Signal | Confidence | Verdict |
| --- | --- | --- | --- | --- | --- |
| hoffmannarchitektur | Made with Lovable websites category -> architecture project card | `https://hoffmannarchitektur.live/` -> homepage/hero; text extraction sparse | Brand/service site; likely portfolio/contact workflow, not yet mapped. | low | `PASS WITH NOTES` |
| Heavy DOOTY | Made with Lovable websites category -> family-owned yard cleanup service card | Live site from category card; needs browser pass | Local service acquisition flow: service explanation, trust, contact/quote CTA. | medium | `PASS WITH NOTES` |
| The Odditorium | Made with Lovable websites category -> entertainment/content project card | Live site from category card; needs browser pass | Content/interactive entertainment flow; lower monetization value. | medium | `PASS WITH NOTES` |
| Porsche design system | Made with Lovable websites category -> project card | Live page opens; likely single-page landing | Visual/landing reference; weak business workflow proof. | medium | `PASS WITH NOTES` |
| SportStream | `https://madewithlovable.com/projects/sportstream` -> project summary and live link | Live target currently unavailable/404 in prior check | Sports streaming landing concept; live workflow cannot be inspected. | high | `FAIL` |
| Living Talent Graph | `https://madewithlovable.com/projects/living-talent-graph` -> project summary and live link | `https://livingtalentgraph.ai/`; text extraction sparse | Identity/talent graph concept; workflow needs live UI mapping. | medium | `PASS WITH NOTES` |

### Lovable Issue Cards

#### HIGH - Lovable Category Cards Are Good Discovery But Weak Workflow Evidence

- Area: workflow/source evidence.
- URL: `https://madewithlovable.com/categories/websites`
- Live position: category grid -> individual project card -> live link.
- Locator: card names such as hoffmannarchitektur, Heavy DOOTY, The Odditorium, Porsche design system.
- Workflow step: `1. Open category -> 2. Select project -> 3. Open live site -> 4. Map CTA/form/backend`.
- Evidence: category page provides broad project discovery and project counts.
- Problem: Category pages alone do not prove forms, backends, deployment dependencies, or production readiness.
- Likely cause: Gallery cards optimize for browsing, not audit evidence.
- Fix: Every Lovable card needs one follow-up live-page audit row.
- Copy prompt: `For this Lovable project card, open the live site and map hero CTA, nav links, forms, contact path, external links, mobile layout issues, and deployment/SEO gaps.`
- Validation: The case has at least one exact live URL, one CTA/form locator, and one deployment readiness row.

#### CRITICAL - SportStream Should Stay Out Of The Recommended Live List

- Area: availability.
- URL: `https://madewithlovable.com/projects/sportstream`
- Live position: project page -> live link.
- Locator: source project exists; live target previously returned 404.
- Workflow step: `1. Open project page -> 2. Click live site -> 3. Verify page loads`.
- Evidence: project source exists but live availability failed.
- Problem: A dead live site cannot be used for direct workflow or quality inspection.
- Likely cause: deployment removed, domain changed, or app unpublished.
- Fix: Mark as dead-link case until live link recovers.
- Copy prompt: `Recheck the SportStream live URL. If it still returns 404, remove it from the curated live-site list and keep only as a gallery-source example.`
- Validation: Live target returns a working page with inspectable CTA/workflow text or screenshot.

## v0 / Vercel Community Cases

| Case | Source Locator | Live Position | Workflow Signal | Confidence | Verdict |
| --- | --- | --- | --- | --- | --- |
| Istanbul BJJ Map | `https://community.vercel.com/t/first-ever-vibe-coding-project-with-v0-istanbul-bjj-map/11947` -> author says they chose v0 after trying alternatives | `https://www.istanbulbjjmap.com/` -> map/directory homepage | Directory/map browsing flow; likely filters/map markers/detail pages. | high | `PASS` |
| API Checker | `https://community.vercel.com/t/api-checker-free-postman-alternative-built-entirely-with-v0/30192` -> "Built entirely with v0" | `https://www.apichecker.io/` -> `Test Your API` -> request config/test/response/code generator | Full tool workflow with visible inputs, auth helpers, test button, response, history, code export. | high | `PASS` |
| psicjazmin / CBT Therapist | `https://community.vercel.com/t/a-small-v0-project-that-turned-into-a-real-success/28538` -> production project architecture | `https://www.psicjazmin.com/` -> hero/contact/booking/resource flow needs exact visual pass | Production service site with custom contact form, Resend, Neon, Vercel Blob, admin dashboard. | high for source, medium for live positions | `PASS WITH NOTES` |
| Susan portfolio | `https://community.vercel.com/t/rebuilt-my-portfolio-with-v0/8274` -> rebuilt portfolio with v0 | live portfolio -> homepage, work/project sections, "Built with v0" footer | Portfolio navigation and project showcase; low backend complexity. | high | `PASS` |
| damilareoo portfolio | `https://community.vercel.com/t/portfolio-website/31091` -> showcase post with live site | live portfolio -> hero and navigation sections | Portfolio reference; explicit v0 build claim weaker than API Checker/Susan. | medium | `PASS WITH NOTES` |
| v0.directory | `https://community.vercel.com/t/v0-directory-curated-v0-prompts-instructions-and-mcps/30956` -> built using v0 claim | `https://v0dotdirectory.vercel.app/` -> directory search/category/listing pages | Directory IA, search, browse, resource listing flow. | high | `PASS` |
| Creadefy | `https://community.vercel.com/t/from-a-2-am-frustration-to-the-google-office-stage-building-creadefy-with-v0-and-vercel/30160.md` -> UI built with v0 and used at Google event | live product site -> hero, login/signup, event certificate/product flow | Production SaaS/platform; credential/certificate workflow and auth. | high | `PASS` |

### v0 Issue Cards

#### HIGH - API Checker Is The Best Position-Aware Benchmark

- Area: interaction/workflow.
- URL: `https://www.apichecker.io/`
- Live position: `Test Your API` section.
- Locator: `Request Configuration`, `API Endpoint`, `HTTP Method`, `Authentication`, `Query Parameters`, `Test API`, `Response`, `History`, `Code Generator`.
- Workflow step: `1. Enter endpoint -> 2. Choose method/auth -> 3. Add query/header/body -> 4. Test -> 5. Read response -> 6. Copy generated code`.
- Evidence: live page exposes the workflow in crawlable text.
- Problem: None for audit visibility; this is a positive benchmark.
- Likely cause: Tool UI has semantic labels and visible state panels.
- Fix: Use this structure as the model for future audit output.
- Copy prompt: `Use API Checker as the benchmark. Generate a workflow map from Request Configuration through Code Generator, including each input, button, response panel, dependency, and validation action.`
- Validation: Workflow map can be filled without guessing button labels.

#### HIGH - CBT Therapist Has Strong Deployment Claims But Needs Exact Live Button/Form Locators

- Area: interaction/deployment.
- URL: `https://community.vercel.com/t/a-small-v0-project-that-turned-into-a-real-success/28538`
- Live position: source post -> production architecture; live site `https://www.psicjazmin.com/`.
- Locator: custom contact form, Resend, Neon, Vercel Blob, admin dashboard, purchased domain.
- Workflow step: `1. Visitor opens live site -> 2. Contact/booking CTA -> 3. Form submit -> 4. Email capture -> 5. Admin/resource workflow`.
- Evidence: author describes a real production site and connected services.
- Problem: Source evidence is strong, but a final audit needs exact live page positions for CTAs and form fields.
- Likely cause: Community post is architecture narrative, not UI map.
- Fix: Run visual/browser pass and record section names, button labels, form field labels, success/error states.
- Copy prompt: `Open psicjazmin.com and locate every appointment/contact/resource workflow. For each, record URL, page area, button or field label, dependency, expected action, actual result, and validation state.`
- Validation: The audit contains at least one exact CTA locator and one form locator from the live site.

#### MEDIUM - Portfolio Cases Are Useful For Layout, Not Deployment Depth

- Area: classification.
- URL: Susan and damilareoo Vercel Community posts plus live portfolio pages.
- Live position: homepage hero, navigation, project cards, footer.
- Locator: portfolio sections and project showcase links.
- Workflow step: `1. Open portfolio -> 2. Navigate projects -> 3. Contact/social link -> 4. Verify external links`.
- Evidence: community posts and live sites show portfolio deployment.
- Problem: They are valid vibe-coded sites, but they do not prove backend, form, CMS, auth, or data flow.
- Likely cause: Portfolio sites are mostly static showcase pages.
- Fix: Keep them in "portfolio/layout reference", not "business workflow" tier.
- Copy prompt: `Audit this portfolio for layout quality, section hierarchy, project cards, contact/social links, mobile responsiveness, and broken external links. Do not classify as backend-ready unless form/CMS/auth evidence exists.`
- Validation: Categorization separates layout value from deployment/workflow value.

#### HIGH - Creadefy Should Be Treated As Production-Workflow Evidence

- Area: product/workflow.
- URL: `https://community.vercel.com/t/from-a-2-am-frustration-to-the-google-office-stage-building-creadefy-with-v0-and-vercel/30160.md`
- Live position: source post -> Google event usage; live product site -> auth/product CTA.
- Locator: UI built with v0; trusted/used at real event; certificate/product platform positioning.
- Workflow step: `1. User lands -> 2. Login/signup -> 3. Create/manage certificate -> 4. Deliver credential`.
- Evidence: source post explicitly connects v0 UI to real-world event use.
- Problem: Live production workflow still needs auth-gated path inspection.
- Likely cause: Core value likely sits behind login.
- Fix: Audit public landing first; mark auth-gated product path as `unknown` until test account or demo access exists.
- Copy prompt: `Audit Creadefy public pages and mark auth-gated certificate workflows separately. Record public CTAs, login/signup routes, required account state, and unknown gated dependencies.`
- Validation: Public vs gated workflow rows are separated.

## Replit Cases

| Case | Source Locator | Live Position | Workflow Signal | Confidence | Verdict |
| --- | --- | --- | --- | --- | --- |
| RevCrew.ai | `https://replit.com/gallery/work/marketing-and-sales/revcrew-ai` -> project description | View App / deployed company site -> homepage/contact/blog/admin/login needs live pass | Multi-page site, contact forms, blog, user/admin auth, backend database. | high | `PASS` |
| Invites Page | `https://replit.com/gallery/life/productivity/invites-page` -> gallery project | View App -> invite/RSVP/ticketing flow needs live pass | Event invitation, ticketing, RSVP, guest flow. | medium | `PASS WITH NOTES` |
| GuruQore | `https://replit.com/gallery/work/human-resources/guruqore` -> gallery project | View App -> course/landing page flow needs live pass | AI + Vibe Marketing course landing, likely lead capture or course CTA. | medium | `PASS WITH NOTES` |

### Replit Issue Cards

#### HIGH - RevCrew.ai Has The Strongest Full-Stack Source Map

- Area: workflow/deployment.
- URL: `https://replit.com/gallery/work/marketing-and-sales/revcrew-ai`
- Live position: gallery description and View App link.
- Locator: multiple pages, contact forms, blog, user/admin auth, backend database.
- Workflow step: `1. Marketing page -> 2. Contact form -> 3. Blog -> 4. User/admin auth -> 5. Database persistence`.
- Evidence: Replit Gallery project page describes a full-stack workflow.
- Problem: Gallery evidence must be paired with live route/button verification.
- Likely cause: Gallery is a source summary, not an interaction test.
- Fix: Run a live route pass over homepage, contact, blog, login/admin, and form success/error states.
- Copy prompt: `Audit RevCrew.ai live app. Locate homepage CTA, contact form fields, blog routes, login/admin entry, and any database-backed content. Mark exact URL, element label, dependency, and status.`
- Validation: Live workflow map includes contact form and auth/admin routes.

#### MEDIUM - Invites Page Needs RSVP/Ticketing Positions

- Area: interaction/workflow.
- URL: `https://replit.com/gallery/life/productivity/invites-page`
- Live position: Replit project page -> View App -> event invitation/RSVP/ticketing UI.
- Locator: project description and View App link.
- Workflow step: `1. Open event page -> 2. RSVP or buy ticket -> 3. Submit guest data -> 4. Organizer sees response`.
- Evidence: gallery identifies event invitation/ticketing/RSVP purpose.
- Problem: The exact form fields and organizer/admin view are not verified from source text alone.
- Likely cause: live interaction details are inside the app.
- Fix: Browser pass should locate guest CTA, RSVP/ticket form fields, payment/ticketing dependency, and organizer dashboard if visible.
- Copy prompt: `Audit Invites Page by mapping guest RSVP/ticket purchase flow and organizer/admin flow. Record every field, CTA, dependency, confirmation state, and broken path.`
- Validation: The report distinguishes guest flow from organizer flow.

#### MEDIUM - GuruQore Is A Landing/Course Case, Not Full App Proof Yet

- Area: classification/conversion.
- URL: `https://replit.com/gallery/work/human-resources/guruqore`
- Live position: project page -> View App -> course landing.
- Locator: AI + Vibe Marketing course positioning.
- Workflow step: `1. Open landing page -> 2. Identify course CTA -> 3. Submit/checkout/register -> 4. Confirm enrollment path`.
- Evidence: gallery project exists and links to app.
- Problem: Course landing pages need lead capture or checkout proof before being called business-complete.
- Likely cause: public landing evidence does not guarantee payment/enrollment backend.
- Fix: Map CTA and any form/payment/enrollment dependency.
- Copy prompt: `Audit GuruQore as a course landing page. Locate primary CTA, signup/enrollment form, checkout/payment route, email capture, content preview, and missing trust or compliance elements.`
- Validation: Landing-page conversion flow is explicitly marked as works/partial/broken/unknown.

## Bolt Case

| Case | Source Locator | Live Position | Workflow Signal | Confidence | Verdict |
| --- | --- | --- | --- | --- | --- |
| Bolt Gallery | `https://bolt.new/gallery` | Gallery page; public extraction limited | Potential source for Bolt-built examples, but individual case data not verified. | low | `PASS WITH NOTES` |

### Bolt Issue Card

#### MEDIUM - Bolt Needs Individual Project Verification Before Ranking

- Area: source quality.
- URL: `https://bolt.new/gallery`
- Live position: gallery page.
- Locator: gallery entry point, no validated individual project rows in this run.
- Workflow step: `1. Open Bolt gallery -> 2. Select project -> 3. Open live site -> 4. Map workflow/deployment`.
- Evidence: gallery exists, but public searchable/crawlable data is limited.
- Problem: Without individual project source/live pairs, Bolt should not be mixed into the same confidence tier as Lovable, v0, and Replit examples.
- Likely cause: public extraction limitations and ambiguous search results for "Bolt".
- Fix: Collect individual Bolt.new project URLs and live URLs first.
- Copy prompt: `Build a Bolt-only validation set. For each Bolt.new gallery project, capture project URL, live URL, category, visible CTA/form/workflow, deployment dependencies, and confidence level.`
- Validation: At least 5 Bolt projects have source + live evidence before ranking Bolt.

## Deployment/Workflow Gap Matrix

| Case | Exact Live UI Position Available Now | Source Workflow Evidence | Needs Visual Pass | Main Gap |
| --- | --- | --- | --- | --- |
| hoffmannarchitektur | no | medium | yes | CTA/contact/portfolio workflow unknown |
| Heavy DOOTY | no | medium | yes | quote/contact flow unknown |
| The Odditorium | no | medium | yes | interactive behavior unknown |
| Porsche design system | partial | medium | yes | business workflow weak |
| SportStream | no | high source, failed live | yes if recovered | live site unavailable |
| Living Talent Graph | no | high source | yes | talent/profile workflow unknown |
| Istanbul BJJ Map | partial | high | yes | map markers/filter/detail paths need pass |
| API Checker | yes | high | optional | best workflow map |
| psicjazmin | partial | high | yes | exact CTA/form positions needed |
| Susan portfolio | partial | high | optional | layout/contact links only |
| damilareoo portfolio | partial | medium | optional | attribution weaker |
| v0.directory | yes | high | optional | directory search/category workflow |
| Creadefy | partial public, gated product | high | yes | auth-gated workflow unknown |
| RevCrew.ai | source-level | high | yes | live routes/forms/admin need pass |
| Invites Page | source-level | medium | yes | RSVP/ticketing form positions |
| GuruQore | source-level | medium | yes | enrollment/lead capture proof |
| Bolt Gallery | no | low | yes | individual cases missing |

## Copyable Audit Prompts

1. `For this website, create a position-aware audit. For every CTA, nav link, form, login, dashboard action, copy/export button, and deployment dependency, record URL, page area, element label, locator, workflow step, expected action, actual result, status, and validation.`
2. `Separate source evidence from live evidence. Source evidence proves the site was built with Lovable/v0/Replit/Bolt; live evidence proves the workflow actually works. Mark confidence high/medium/low.`
3. `If a page is JavaScript-heavy or crawler text is sparse, mark live position confidence low and require a visual browser pass with screenshot coordinates or accessibility locators.`
4. `Do not recommend a case as production-ready unless source evidence, live availability, CTA/form path, backend/data dependency, and deployment readiness have been checked.`

## Final Ranking For This Original List

Best for live workflow mapping:

1. API Checker
2. v0.directory
3. Creadefy public site, with gated caveat
4. RevCrew.ai, after live route pass
5. psicjazmin, after live CTA/form pass

Best for inspiration/layout:

1. hoffmannarchitektur
2. Porsche design system
3. Susan portfolio
4. damilareoo portfolio
5. The Odditorium

Best for local/service/business structure:

1. Heavy DOOTY
2. psicjazmin
3. RevCrew.ai
4. Invites Page
5. GuruQore

Exclude or hold:

- SportStream: hold until live site works.
- Bolt: hold until individual Bolt.new project/live pairs are collected.

## Result

Verdict: `PASS WITH NOTES`

The original list is valid as a broad discovery set, but not all entries are equally usable for the audit-workbench goal. The strongest position-aware cases are API Checker, v0.directory, Creadefy, RevCrew.ai, and psicjazmin. The Lovable category is valuable for inspiration discovery, but most cases need a visual browser pass before their buttons, forms, layout issues, and deployment gaps can be pinned to exact live positions.
