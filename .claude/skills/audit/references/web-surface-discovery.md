# Web Surface Discovery

Use this reference before detailed live testing. A good audit first discovers the product surface, then decides what to test, skip, verify physically, or report as unknown.

```text
entry point -> surface map -> permission boundary -> test priority map -> live/physical checks
```

The goal is to stop the agent from only testing what the user happened to mention. The agent should inventory what the website exposes.

## When To Use

Use web surface discovery when:

- The target is a website, web app, landing page, SaaS, portfolio, directory, marketplace, dashboard, or documentation site.
- The user asks to test "everything", "all functions", "the site", or "whether it works".
- The audit includes real browser interaction, visual QA, deployment checks, rich media, documents, or security-adjacent review.
- Source evidence and live behavior may disagree.

For tiny source-only checks, record only the relevant surface instead of a full map.

## Surface Maps

### 1. Page Map

Record:

- Entry URL.
- Page title and main heading.
- Header, navigation, main content, sidebars, footer, modals, cookie banners, and overlays.
- Important routes and deep links discovered from navigation or source.
- Error pages, empty states, loading states, and gated pages.

### 2. Interaction Map

Record visible and reachable:

- Buttons.
- Links.
- CTAs.
- Forms.
- Inputs.
- Selects.
- Tabs.
- Accordions.
- Dropdowns.
- Menus.
- Search.
- Filters.
- Sort controls.
- Pagination.
- Copy/export/share actions.
- Upload controls.
- Auth and account controls.
- Checkout, booking, payment, or destructive controls.

For each item, capture:

- User-facing label.
- Locator strategy.
- Expected destination or result.
- Permission level from `permission-model.md`.
- Test priority: `P0`, `P1`, `P2`, or `skip-safe`.

### 3. Media Map

Record:

- Images and background images.
- Video and audio.
- Embeds and iframes.
- Icons and logos that carry meaning.
- Hero media and product screenshots.

For each asset, note:

- URL or source path.
- Locator or page section.
- Alt text or accessible name.
- Visible dimensions and obvious distortion.
- Loading state or failure.
- Relevance to the product promise.
- Whether it needs screenshot-backed visual QA.

### 4. Document And Download Map

Record:

- PDF, DOCX, XLSX, CSV, ZIP, and other downloads.
- Whitepapers, resumes, menus, reports, policies, decks, and legal docs.
- File name, link text, destination URL, and whether it opens or downloads.
- Whether the document is user-critical, legal/compliance-critical, or purely supplemental.

Flag broken, vague, private, oversized, or untrusted document links.

### 5. Network And API Map

Record observable:

- First-party API endpoints.
- Third-party APIs.
- Analytics, tracking, ads, chat widgets, maps, payments, auth providers, and CDN assets.
- Failed requests.
- Slow blocking requests.
- CORS and auth-related behavior visible from the browser.

Do not paste sensitive payloads. Summarize and redact.

### 6. Storage And Session Map

Record presence of:

- Cookies.
- Local storage.
- Session storage.
- IndexedDB.
- Service workers.
- Cache behavior.
- Auth/session indicators.

Do not expose secret values. Report keys and risk patterns only when safe.

### 7. Security Surface Map

Record observable:

- HTTPS and certificate state.
- Security headers.
- CSP presence.
- Mixed content.
- Public admin routes.
- Login, password reset, invite, upload, checkout, and account settings surfaces.
- Third-party scripts and embeds that expand risk.

Use `permission-model.md` before interacting with security-sensitive surfaces.

## Test Priority Map

After discovery, classify the surface:

- `P0`: Core promise, primary CTA, auth boundary, checkout/booking, data upload, dashboard action, or launch blocker candidate.
- `P1`: Important conversion, trust, or workflow support path.
- `P2`: Secondary content, footer, documentation, settings, or polish.
- `skip-safe`: Payment, deletion, private data, production mutation, admin mutation, or any action outside the current permission level.
- `unknown`: Not enough evidence or blocked by auth/tool access.

## Progress Update Requirement

After discovery, emit a progress update:

```text
Progress Update [stage N] - Web surface discovery
Status: completed / issue found / blocked
What I just did: Mapped pages, interactions, media, documents, network surfaces, and permission boundaries.
Key findings so far: [P0/P1 surfaces, obvious blockers, unknowns]
Evidence collected: [URL, locators, screenshot/source/network summary]
Blocked / Skipped: [SKIPPED-SAFE or unknown areas]
Next step: [highest-priority safe flow or physical test package]
```

## Anti-Patterns

- Jumping straight to a form or CTA without mapping the page.
- Only testing the homepage.
- Treating decorative links and core workflow controls as equal priority.
- Ignoring media, documents, downloads, storage, or third-party scripts.
- Missing auth, payment, upload, or admin boundaries.
- Reporting "everything works" when major surfaces were never inventoried.
