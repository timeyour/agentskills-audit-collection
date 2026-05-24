# Webpage Audit Rubric

Use this reference when reviewing a website, landing page, web app screen, vibe-coded project, or deployed prototype.

## Goal

Make page quality, workflow problems, and deployment gaps obvious at a glance. Do not only say whether a site looks good. Identify what is broken, why it matters, how to fix it, and what the user can copy into an implementation prompt.

For full feature-by-feature flow execution, also use `live-functional-audit.md`.

## Audit Dimensions

### Visual and Layout Quality

- First viewport communicates the offer or purpose.
- Content hierarchy is clear.
- Typography sizes fit the page role.
- Spacing is consistent.
- Sections do not feel like unrelated templates stitched together.
- Cards, buttons, and forms align cleanly.
- Mobile layout does not overlap, crop, or hide important content.
- Images are relevant, loaded, and not just decorative filler.

### Conversion and Trust

- Primary CTA is visible and specific.
- Secondary CTA is not competing with the primary action.
- Service/product value is concrete.
- Social proof, proof of work, pricing, or credibility signals exist where expected.
- Contact, booking, signup, checkout, or demo flow is reachable.
- Error states and confirmation states are understandable.

### Interaction and Workflow

Map every important interactive element:

- Navigation links.
- CTA buttons.
- Forms.
- Login/signup.
- Booking or checkout.
- Search/filter/sort.
- Upload/download.
- Dashboard/admin actions.
- Copy/share/export buttons.

For each interaction, record:

- Label:
- Live position:
- Source locator:
- Expected action:
- Actual action:
- Connected backend/service:
- Missing dependency:
- Status: works / partial / broken / unknown.

## Live Position Tracking

Every issue or workflow finding should include enough location data for a human to find it quickly.

Use these fields:

- URL: exact inspected page.
- Viewport: desktop, tablet, mobile, or unknown.
- Page area: hero, nav, pricing, contact, footer, dashboard, form, modal, etc.
- Element label: visible button/link/input text.
- Locator: best available selector, role/name, text match, source line, or screenshot coordinate.
- Step: where it appears in the workflow, for example `1. Open page -> 2. Click Book demo`.
- Evidence timestamp: date of the check.
- Confidence: high / medium / low.

When browser automation is unavailable, use source lines from fetched pages as the locator. When a page is JavaScript-heavy and text extraction is sparse, mark locator confidence as low and say what still needs a visual/browser pass.

Visual scores should be marked source-based until desktop and mobile screenshots or equivalent browser evidence exist.

### Content and Copy

- Headline states the actual offer, not vague hype.
- Supporting copy answers who it is for and why it matters.
- CTA text names the action.
- Empty states, errors, and success messages are useful.
- Claims are backed by proof or clearly framed as examples.

### Deployment Readiness

Check what is required before the site can be called production-ready:

- Domain and SSL.
- Environment variables.
- Backend/API routes.
- Database.
- Auth.
- File or image storage.
- Email/SMS provider.
- Payment provider.
- CMS/admin editor.
- Analytics.
- Error monitoring.
- SEO metadata and sitemap.
- Robots/crawlability.
- Privacy policy, terms, and compliance text when needed.
- Backup/export path for user data.

## Issue Card Format

Use one card per actionable issue:

```markdown
### <S0-S4> - <Short Issue Title>

- Area:
- URL:
- Live position:
- Locator:
- Workflow step:
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

## At-a-Glance Output Format

```markdown
## Page Audit Summary

- URL:
- Page type:
- Overall status: PASS / PASS WITH NOTES / FAIL
- Quality score: 0-100
- Main risk:
- Fix first:

## Workflow Map

| Element | Expected | Actual | Dependency | Status |
| --- | --- | --- | --- | --- |

## Deployment Readiness

| Requirement | Status | Notes |
| --- | --- | --- |

## Issues

<issue cards>

## Copyable Fix Pack

1. <ready-to-copy prompt>
2. <ready-to-copy prompt>
3. <ready-to-copy prompt>
```

## Anti-Patterns

- Judging only aesthetics.
- Treating a landing page as production-ready when forms, backend, or deployment dependencies are missing.
- Saying "improve UI" without naming the exact visual or workflow failure.
- Hiding caveats in prose instead of making them visible in tables.
- Recommending a site as inspiration without saying what part is worth copying.
