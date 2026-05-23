# Category Pattern Catalog

Use this reference to diagnose pattern mismatches during product-pattern audits.

Each category has four things: what the page must promise, where conversion happens, what counts as a successful business outcome, and which red flags mean the page is a template, not a working product.

---

## Local Service Site

**Expected pattern**: service promise above the fold, proof of work, areas served, quote/contact CTA, trust signals (reviews, certifications).

**Conversion surface**: contact form, phone number, booking CTA, "get a quote" button.

**Business outcome**: booked appointment, quote request with contact info, or direct phone call.

**Red flags**:
- no service area or service list on the homepage
- no proof (photos of past work, reviews, case summaries)
- no contact CTA above the fold
- phone number is a placeholder or `123-456-7890`
- form submits but no success state or confirmation message

---

## SaaS / Tool

**Expected pattern**: problem statement, demo (screenshot or interactive), feature proof, docs link, pricing page, signup or "start free" CTA.

**Conversion surface**: signup page, pricing page, demo request form, "start free trial" CTA.

**Business outcome**: signed-up user who can use the core feature, or a demo booking with confirmed attendance.

**Red flags**:
- no pricing page or pricing is "contact us"
- no demo, no screenshots of the actual product
- signup CTA leads to a waitlist with no confirmation
- feature list is generic and not specific to a use case
- no docs or help content

---

## Portfolio

**Expected pattern**: clear identity (name or brand), selected work with context, process or approach explanation, contact CTA, resume/CV download.

**Conversion surface**: contact CTA (email or form), resume download, project inquiry form.

**Business outcome**: contact message from a potential client or employer, or a downloaded resume leading to an interview.

**Red flags**:
- no contact information or contact form does not submit
- "selected work" has no context (what was the problem, what was our role?)
- no explanation of process or how the person works
- placeholder project images or `lorem ipsum` descriptions

---

## Lifestyle / Commerce

**Expected pattern**: scenario or aspiration set-up, product path (browse → view → save/buy), social proof, clear brand voice, mobile-friendly layout.

**Conversion surface**: "add to cart", "save", "share", "buy now", checkout flow, wishlist.

**Business outcome**: saved item, started checkout, or completed purchase with confirmation.

**Red flags**:
- no product path — the page is only inspiration images with no "buy" or "save" action
- "add to cart" or "buy" buttons are decorative (not connected to a cart or checkout)
- no reviews, no shipping info, no return policy
- price is missing or shows `$0` / `N/A`
- mobile layout breaks the CTA (button not tappable at 375px)

---

## Creator

**Expected pattern**: identity and niche, content samples (posts, videos, articles), audience proof (follower count or engagement examples), subscribe/support CTA.

**Conversion surface**: subscribe button, support/ donate CTA, follow links, newsletter signup.

**Business outcome**: subscriber, supporter, or follower who receives future content.

**Red flags**:
- no subscribe or support CTA
- "follow me" links go to empty or inactive accounts
- no content samples (only a bio with no work to consume)
- audience proof looks fabricated (round numbers like "100K followers" with no engagement)

---

## Dashboard / Admin

**Expected pattern**: data density without clutter, clear actions (filters, bulk actions, create/edit/delete), visible state (loading, empty, error, success), table or card readability.

**Conversion surface**: N/A (this is an internal tool, not a public conversion flow).

**Business outcome**: completed task (filtered data, created record, exported report, approved item).

**Red flags**:
- low data density (too much whitespace for a data tool)
- missing actions (no way to create, edit, or delete from the dashboard)
- unclear state (loading forever, no empty-state message)
- tables not sortable or filterable
- no confirmation for destructive actions (delete without confirm)

---

## Directory / Search

**Expected pattern**: search input (visible above the fold), filters (category, location, price), listing cards with key info, detail pages, empty-state handling.

**Conversion surface**: search button, filter controls, contact/book/message CTA on listing detail, share button.

**Business outcome**: found result with enough info to contact or book, or a submitted contact/booking request.

**Red flags**:
- no search input or search does not return results
- no filters, or filters do not actually filter the results
- listing cards have no detail page link
- detail page has no contact or booking CTA
- empty search state shows no message (confusing blank page)

---

## How to Use This Catalog

1. **Identify the category** before auditing. If the page claims to be two categories at once (e.g. "SaaS + Portfolio"), flag it as a pattern conflict.
2. **Check red flags first** — they are the fastest way to find S0-S1 issues.
3. **Compare the conversion surface** against the expected pattern. If the category expects a booking CTA and the page only has "Learn more", that is an S1 finding.
4. **Do not apply one category's pattern to another** — critique a local service site by local-service patterns, not by SaaS patterns.
