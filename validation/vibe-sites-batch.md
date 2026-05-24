# Batch Validation: Vibe-Coded Website Case Set

Date: 2026-05-18

## Purpose

Use the supplied vibe-coded website list as a real-world validation set for the Engineering Discipline Skills workflow. This is a batch version of `/spec -> /review -> /check -> /learn`: define criteria, verify evidence, reject weak cases, and record what should change in the workflow.

## Validation Criteria

Each case is checked against four questions:

1. Source evidence: Is there a project page, gallery page, or community post that connects the case to Lovable, v0, Replit, or Bolt?
2. Live evidence: Does the linked live site open?
3. Realness signal: Does the case look like a real site/app rather than only a toy demo?
4. Reuse value: Is it worth studying for layout, copy, product flow, or business use?

Statuses:

- `PASS`: source evidence and live evidence are both present.
- `PASS WITH NOTES`: usable, but evidence or crawlability is partial.
- `FAIL`: source exists but the live site is unavailable, or the tool attribution is too weak.

## Entry Points

| Entry | Result | Notes |
| --- | --- | --- |
| Made with Lovable websites category | `PASS` | Category page exposes a batchable website catalog and currently reports 86 website projects. |
| Replit Gallery | `PASS` | Gallery page exposes 79 projects and positions the examples around building apps/sites from natural language. |
| Vercel Community / v0 showcase posts | `PASS WITH NOTES` | Strong source evidence lives in individual community posts rather than one clean official index. |
| Bolt Gallery | `PASS WITH NOTES` | Gallery entry exists, but public text extraction is limited in this run, so no individual Bolt cases were validated. |

## Batch Results

| Case | Platform | Source Evidence | Live Evidence | Verdict | Reuse Value |
| --- | --- | --- | --- | --- | --- |
| hoffmannarchitektur | Lovable | Listed on Made with Lovable website category. | Live domain opens, but extracted content is sparse. | `PASS WITH NOTES` | Good architectural/brand site reference. |
| Heavy DOOTY | Lovable | Listed on Made with Lovable website category. | Live site opens. | `PASS` | Strong local service website reference. |
| The Odditorium | Lovable | Listed on Made with Lovable website category. | Live site opens, but extracted content is sparse. | `PASS WITH NOTES` | Useful for entertainment/content-style inspiration. |
| Porsche design system | Lovable | Listed on Made with Lovable website category. | Live site opens. | `PASS WITH NOTES` | Strong visual landing-page reference, weaker as a real business case. |
| SportStream | Lovable | Project page exists and links to a live site. | Live site currently returns 404. | `FAIL` | Reject from the final recommended set unless live link recovers. |
| Living Talent Graph | Lovable | Project page exists and links to live site. | Live domain opens, but extracted content is sparse. | `PASS WITH NOTES` | Useful for personal identity / talent graph concepts. |
| Istanbul BJJ Map | v0 | Vercel Community post explicitly describes it as a vibe-coding project with v0. | Live map site opens. | `PASS` | Strong niche directory/map reference. |
| API Checker | v0 | Vercel Community post says it was built entirely with v0. | Live tool site opens. | `PASS` | Strong tool/SaaS reference. |
| psicjazmin | v0 | Vercel Community post says the v0 project became a production site. | Live therapy site opens. | `PASS` | Strong service-provider production site reference. |
| Susan portfolio | v0 | Vercel Community post says the portfolio was rebuilt with v0. | Live portfolio opens and includes v0 attribution text. | `PASS` | Good portfolio/reference site. |
| damilareoo portfolio | v0 | Vercel Community showcase post is tagged for v0, but explicit build claim is weaker. | Live portfolio opens. | `PASS WITH NOTES` | Useful portfolio reference; tool attribution confidence is lower. |
| v0.directory | v0 | Vercel Community post says it was built using v0. | Live directory opens and includes v0-related positioning. | `PASS` | Strong directory/information-architecture reference. |
| Creadefy | v0 | Vercel Community post says the UI was built with v0 and used in real events. | Live product site opens. | `PASS` | Strong production SaaS / credential-platform reference. |
| RevCrew.ai | Replit | Replit Gallery page says the company website was built, designed, and hosted from scratch using Replit Agent. | Live Replit-hosted site opens. | `PASS` | Strong AI/company marketing site reference. |
| Invites Page | Replit | Replit Gallery project page exists and links to an app. | Live app opens, but extracted content is sparse. | `PASS WITH NOTES` | Good RSVP/ticketing product reference. |
| GuruQore | Replit | Replit Gallery project page exists and says it was built for speed on Replit. | Live app opens, but extracted content is sparse. | `PASS WITH NOTES` | Useful course/landing-page reference. |

## Findings

- `CRITICAL`: None.
- `MEDIUM`: SportStream should be removed from any "directly usable live site" list until its live URL works again.
- `MEDIUM`: Bolt should not be represented with specific project claims until individual live examples are verified.
- `LOW`: Some live sites are JavaScript-heavy, so crawler text is sparse even when the site opens.
- `LOW`: Vercel Community cases vary in source strength; prefer posts that explicitly state "built with v0" over posts that are only tagged as showcase.

## Recommended Curated Set

Use these as the cleaner batch for future reference:

1. Heavy DOOTY: local service website.
2. Istanbul BJJ Map: niche map/directory.
3. API Checker: tool/SaaS.
4. psicjazmin: real service-provider production site.
5. Susan portfolio: personal portfolio.
6. v0.directory: curated directory.
7. Creadefy: production credential platform.
8. RevCrew.ai: AI/company marketing site.
9. Invites Page: event/RSVP product.
10. GuruQore: course/landing page.

## Workflow Lessons

- Batch validation needs a "source evidence" column and a separate "live evidence" column; otherwise dead live links hide behind still-valid gallery pages.
- "Built with tool X" should be graded by evidence strength:
  - Strong: explicit page/post claim.
  - Medium: official gallery listing or tag.
  - Weak: inference from hosting or visual style.
- For inspiration lists, include only `PASS` and carefully selected `PASS WITH NOTES`; exclude `FAIL` cases from the headline examples.

## Outcome

Verdict: `PASS WITH NOTES`

The supplied website list is good enough as a real-world batch validation set, but it should be cleaned before being presented as a recommended case library. The biggest correction is to drop SportStream from the live-site shortlist and treat Bolt as an entry point, not a verified case set, until individual examples are checked.
