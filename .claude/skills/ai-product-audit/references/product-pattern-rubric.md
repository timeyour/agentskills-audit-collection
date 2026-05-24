# Product Pattern Rubric

Use this reference when auditing AI-generated products for pattern fit, scenario clarity, and conversion readiness.

Apply this rubric after the surface-discovery and permission-model checks. Do not say "good product" or "bad product" without explaining the exact pattern mismatch and its business risk.

## Goal

Diagnose whether a product page follows proven patterns for its category. Every finding must include: expected pattern, observed gap, business risk, and a copyable fix prompt.

## Inputs

- Product category (local service, SaaS, portfolio, lifestyle/commerce, creator, dashboard, directory)
- Intended scenario and user self-image
- Business outcome or action the page moves users toward
- Conversion surfaces (CTA, form, booking, checkout, signup)
- Operational depth (backend, database, CMS, auth, content system)

## Audit Dimensions

### 1. Scenario Preparation

- What scenario is this page preparing the user for?
- Does the user see themselves in the scenario?
- Is the scenario specific and believable, or a generic template?
- Can a first-time visitor answer "what is this and why should I care?" in 5 seconds?

**Evidence to collect**: hero headline text, hero subheadline, hero CTA label, first-viewport screenshot.

### 2. Self-Image and Business Outcome

- What self-image, business outcome, or action does the page help the user move toward?
- Is the outcome concrete ("book a same-day plumber") or vague ("get started")?
- Does the page make the outcome feel achievable within 1 click?

**Evidence to collect**: CTA label, next-page URL after CTA click, screenshot of the target page.

### 3. Next-Step Visibility

- Can the user see themselves in the next step?
- Is the primary CTA specific and actionable?
- Does the page convert inspiration into action within 3 clicks?
- Is there a working success state after the CTA (confirmation, dashboard, result)?

**Evidence to collect**: CTA element selector, click result URL, success-state screenshot.

### 4. Page Purpose vs. Inspiration

- Is the page only inspiration (pretty but no path to action), or does it convert inspiration into action?
- Are there real conversion surfaces (CTA, form, booking widget, checkout)?
- Is the page a brochure or a workflow entry point?
- For commerce/creator: can the user save, share, or buy — or only "learn more"?

**Evidence to collect**: list of all CTAs on the page, whether each leads to a real workflow, screenshot of empty states.

### 5. Pattern Fit by Category

Use `category-pattern-catalog.md` for the full pattern list. Quick check:

| Category | Must Have | Dealbreaker if Missing |
| --- | --- | --- |
| Local service | service promise, contact CTA, areas served | no contact CTA |
| SaaS / Tool | problem statement, demo/screenshot, pricing, signup | no signup or demo |
| Portfolio | identity, selected work, contact, process | no contact |
| Lifestyle / Commerce | scenario aspiration, product path, save/buy CTA | no path from inspiration to product |
| Creator | identity, content proof, subscribe/support CTA | no subscribe or support path |
| Dashboard / Admin | data density, actions, filters, clear state | low data density, no actions |
| Directory / Search | search, filters, listing cards, detail pages | no search or listing pages |

### 6. Business Reality Check

- Is this a real business with operational depth, or a visual template?
- Is there a backend, database, CMS, or auth system — or only static pages?
- Is there a monetization path (paid plan, booking fee, affiliate, product sale)?
- Can the business actually deliver the promised outcome?

**Evidence to collect**: robots.txt, `/api/` endpoint probes, pricing page content, "about" or "team" page content.

## Pattern Fit Table Format

| Expected Pattern | Observed | Gap | Business Risk | S0-S4 |
| --- | --- | --- | --- | --- |
| Example: local service site has prominent contact CTA above the fold | CTA present but links to `/waitlist` with no form | No path for the user to actually contact the business | S1 | |

## Issue Card Format

```markdown
### [S0-S4] - [Product-Pattern Issue Title]

- **Area**: [page section, e.g. Hero / Pricing / Contact]
- **URL**: [exact URL]
- **Locator**: [CSS selector, role, or text]
- **Expected pattern**: [what a proven pattern expects]
- **Observed**: [what the page actually does]
- **Business risk**: [how this hurts conversion, trust, or delivery]
- **Fix**: [concrete action]
- **Copy prompt**: [ready-to-copy prompt for AI builder or developer]
- **Regression check**: [how to verify the fix]
```

## Severity

| Level | Meaning |
| --- | --- |
| `S0` | No conversion surface exists; the page is pure inspiration with no path to action. Delivery is not possible. |
| `S1` | Scenario is vague; user cannot see themselves in the next step; value proposition is unrecognizable within 5 seconds. |
| `S2` | Pattern mismatch; page follows the wrong category pattern (e.g. SaaS patterns on a local service site). |
| `S3` | Business outcome is implied but not explicit; CTA is present but_generic ("Learn more"). |
| `S4` | Pattern fit is good; enhance with category-specific best practices or benchmark comparisons. |

## Output Format

```markdown
## Product-Pattern Audit Summary

- **URL**:
- **Product category**:
- **Intended scenario**:
- **Pattern fit score**:
- **Main business risk**:
- **Fix first**:

## Scenario Audit

| Question | Answer | Evidence | Risk |
| --- | --- | --- | --- |
| What scenario is the user being prepared for? | | screenshot + headline text | |
| What is the next actionable step? | | CTA label + target URL | |
| Does the page convert inspiration into action? | | list of conversion surfaces | |

## Pattern Fit

| Expected Pattern | Observed | Gap | Risk | S0-S4 |
| --- | --- | --- | --- | --- |

## Conversion Surface Map

| Surface | Present | Actionable | Evidence |
| --- | --- | --- | --- |
| Primary CTA | | | screenshot + click result |
| Secondary CTA | | | |
| Form | | | submission test result |
| Booking / Checkout | | | |

## Business Reality

| Signal | Present | Evidence |
| --- | --- | --- |
| Backend / API endpoints | | network requests or directory scan |
| Database / CMS | | content editable or static check |
| Pricing / Monetization | | pricing page content |
| Team / About / Contact | | page exists and is specific |

## Issue Cards

[issue cards in the format above]

## Copyable Fix Pack

1. [ready-to-copy prompt for the highest-severity issue]
2. [ready-to-copy prompt for the next issue]
3. [ready-to-copy prompt for pattern-enhancement (S3-S4)]

## Lessons

- Repeated pattern failures:
- Prompt patterns that worked:
- Benchmark examples to keep:
```

## Anti-Patterns

1. Applying the wrong pattern to a category — a local service site does not need a "start free trial" CTA.
3. Judging product quality by visual polish alone — a beautful page with no contact CTA is still an S1.
4. Treating "vibe" or "mood" as a substitute for scenario clarity.
5. Missing the difference between inspiration and conversion — screenshots of food do not sell food if there is no "order" button.
6. Using the wrong benchmark — do not compare a local service site against a SaaS landing page.
7. Batch-auditing without first categorizing each site — mixed-category batches produce misleading summaries.
