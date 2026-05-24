# Vibe-Coded Site Verification Template

Date: 2026-05-21

## Purpose

Use this table when a user brings a list of vibe-coded websites and wants to know which ones are real businesses, working products, useful references, or polished shells.

The goal is not to judge whether a site looks cool. The goal is to verify:

```text
clear offer -> real CTA -> executable flow -> operational signals -> reusable pattern
```

## Evidence Levels

| Level | Meaning |
| --- | --- |
| `SOURCE-ONLY` | A gallery, project page, community post, or author claim links the site to Lovable, v0, Replit, Bolt, or another AI builder. |
| `LIVE-OPENS` | The live site opens, but no important workflow has been tested. |
| `FLOW-OBSERVED` | A human clicked through the main CTA, form, login, upload, or app path and recorded expected vs actual behavior. |
| `PHYSICAL-PROVEN` | A real browser test produced trace, screenshot, HAR, console, video, or result artifacts. |
| `REJECTED` | The live site is dead, attribution is too weak, or no meaningful business/product flow exists. |

Do not call a case "real" unless it reaches at least `FLOW-OBSERVED`. Use `/physical-flow-test` for `PHYSICAL-PROVEN`.

## 14-Point Scoring Rubric

Score each row `0`, `1`, or `2`.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Offer clarity | Empty slogan or buzzwords. | Roughly understandable. | Obvious who it serves, what it solves, and what result it creates. |
| CTA clarity | No main action. | Button exists but destination is vague. | CTA leads directly to trial, booking, upload, signup, demo, or purchase. |
| Real flow | Homepage only. | Form or app path exists but may not work. | At least one core flow closes the loop. |
| Business pages | No pricing/contact/privacy. | One or two supporting pages. | Formal set of pricing, contact, FAQ, privacy, terms, docs, or help pages. |
| Backend/data signal | No login, upload, integration, output, or dashboard. | Login or integration is hinted. | Dashboard, auth, upload, integration, generated output, admin, or data flow is visible. |
| Production signal | Default domain and demo-like copy. | Semi-formal. | Custom domain, mature copy, complete structure, update signs, or operating business evidence. |
| Reuse value | Only interesting visually. | Useful visual reference. | Useful business structure, conversion flow, product skeleton, or workflow pattern. |

Score:

- `12-14`: worth dissecting.
- `8-11`: useful, but do not over-weight.
- `0-7`: likely shell, demo, or low-priority reference.

## Feishu / Notion Copy Table

Copy this table into Feishu, Notion, Airtable, or a spreadsheet.

| Site | Platform | URL | Source Evidence | Live Evidence | Offer Clarity (0-2) | CTA (0-2) | Real Flow (0-2) | Business Pages (0-2) | Backend/Data (0-2) | Production Signal (0-2) | Reuse Value (0-2) | Total (14) | Evidence Level | Verdict | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QuickTables | Lovable | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify online order, booking, SMS, or loyalty flow. |
| Creativable | Lovable | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify CRM, pipeline, booking, team, or AI-agent entry. |
| Pipeline.app | Lovable | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify service packages, case proof, booking, and contact path. |
| Attendflow | Lovable | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify lead capture and event/sales-team workflow. |
| Planoraa | Lovable | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify tasks, guest list, budget, dashboard, or login path. |
| MAtchWise | Lovable | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify resume upload, candidate screening, or team workflow. |
| Vendor Vault | Replit | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify app entry, contract upload/input, risk output, and document generation. |
| User Insights Hub | Replit | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify Notion connection, auth, and analysis output. |
| RedFlag | v0 / Vercel Community | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify upload contract -> risk clauses -> report output. |
| GitFolio | v0 / Vercel Community | TBD | TBD | TBD |  |  |  |  |  |  |  |  | `SOURCE-ONLY` | TBD | First verify GitHub profile input -> generated portfolio output. |

## Five-Minute Manual Verification Flow

Spend no more than five minutes per candidate in the first pass.

1. Open source/gallery/community evidence and record the attribution strength.
2. Open the live site and record whether it loads.
3. Read the first viewport and score offer clarity.
4. Click the primary CTA and record destination.
5. Try the safest core flow: form, signup, upload, search, demo, booking, or dashboard entry.
6. Check for pricing, contact, privacy, terms, FAQ, docs, help, or blog.
7. Look for backend/data signals: login, dashboard, integration, upload, generated output, admin, export, or history.
8. Decide whether the case should be promoted to `/physical-flow-test`.

## Verdict Labels

| Verdict | Use When |
| --- | --- |
| `WORTH-DISSECTING` | Score is `12-14`, live site opens, and at least one core flow is observable. |
| `USEFUL-REFERENCE` | Score is `8-11`; visual or structural value exists, but evidence is partial. |
| `VISUAL-ONLY` | It looks good, but no business/product loop is visible. |
| `SHELL` | It has a polished homepage but no real CTA, flow, or operating signal. |
| `REJECT` | Dead site, broken source claim, unsafe flow, or attribution too weak. |

## Physical Verification Upgrade

Promote a candidate to `/physical-flow-test` when:

- It scores `10+` and has a clickable core workflow.
- It claims upload, auth, dashboard, API, booking, checkout, integration, or document generation.
- Source evidence and live evidence disagree.
- The site is a strong enough reference to influence future design or product decisions.

Physical verification should produce:

- trace
- screenshot
- HAR
- console log
- video when supported
- result JSON
- regression check
- lessons

## Common False Positives

- A beautiful first screen with no second page.
- A `Get Started` CTA that loops back to a waitlist or empty form.
- A fake dashboard screenshot with no login or demo path.
- A pricing page with no purchase, contact, booking, or sales path.
- A tool landing page with no input/output surface.
- A default hosted domain plus no operating pages.
- Broad AI platform copy with no specific user, action, or result.

## Output Shape

Use this shape when reporting a verified batch:

```text
Scope
Evidence
Findings
Severity
Reproduction
Fix Suggestion
Regression Check
Lessons
```

For inspiration lists, include only `WORTH-DISSECTING` and strong `USEFUL-REFERENCE` cases. Exclude `SHELL` and `REJECT` from headline examples.
