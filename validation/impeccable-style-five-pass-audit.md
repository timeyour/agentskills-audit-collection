# Five-Pass Acceptance Audit: impeccable.style

Date: 2026-05-19

Target: `https://impeccable.style/#why`

Audit level: source + safe link-click pass. Browser screenshot coordinates and real extension installation were not executed in this environment.

## Pass 1: Baseline

| Check | Result | Evidence | Unknowns |
| --- | --- | --- | --- |
| URL loads | PASS | `https://impeccable.style/#why` returned the Impeccable homepage content. | Exact scroll position for `#why` needs browser visual pass. |
| Product category identified | PASS | AI design skill + CLI + Chrome extension for design fluency and anti-pattern detection. | None. |
| Main user scenario clear | PASS | User wants AI harnesses to produce less generic UI by teaching design vocabulary and detecting AI slop. | None. |
| Main pages/routes listed | PASS | Home, Designing, Docs, Slop, Live, GitHub, Chrome extension, Neo Mirai live build. | Some direct route aliases need checking. |
| Feature inventory complete | PASS WITH NOTES | Feature inventory below. | Browser extension and CLI cannot be executed here. |
| Happy path mapped | PASS | Landing -> Get Started -> Install skill/extension/CLI -> Use commands or Live Mode. | Actual install/run requires local project. |

## Feature Inventory

| Feature | Start URL | Live Position | Locator | Dependency | Safe To Execute | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Home landing | `https://impeccable.style/` | hero | `Impeccable`, `Design fluency for AI harnesses` | public site | yes | PASS |
| Top nav Docs | homepage | nav | `Docs` | route `/docs/` | yes | PASS |
| Top nav Slop | homepage | nav | `Slop` | route `/slop/` | yes | PASS |
| Top nav Live | homepage | nav | `Live` | route `/live-mode/` | yes | PASS |
| Get Started | homepage | hero/install CTA | `Get Started`, install section | same page anchor | yes | PASS |
| Case live build | homepage | case section | `Open the live build` | route `/neo-mirai/` | yes | PASS |
| Chrome extension install | homepage/get started | extension CTA | Chrome Web Store listing | external store | safe to open only | PASS |
| GitHub source | homepage/header | `27k` GitHub link | `pbakaus/impeccable` repo | GitHub | yes | PASS |
| CLI usage | homepage/docs/GitHub | install/CLI sections | `npx impeccable detect` | npm/local project | no execution | UNKNOWN |
| Browser detector overlay | Slop/Chrome store | slop/live extension claim | extension installation | Chrome extension | no execution | UNKNOWN |
| Live Mode variants | `/live-mode/` | interactive demo text | pick/generate/accept flow | local dev server + HMR | no execution | UNKNOWN |

## Pass 2: Functional Flow Execution

| Feature | Steps Run | Expected | Actual | Evidence | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Homepage load | Open `https://impeccable.style/#why` | Page loads and explains product | Loaded homepage; hero states product and value proposition | Homepage content includes hero, skill, CLI, extension, docs links | LOW | PASS |
| Docs nav | Open Docs | Command reference loads | `/docs/` loads with command categories | Docs page lists Create/Evaluate/Refine/Simplify/Harden/System commands | LOW | PASS |
| Slop nav | Open Slop | Anti-pattern catalog loads | `/slop/` loads catalog and synthetic examples | Slop page lists patterns and detector modes | LOW | PASS |
| Live nav | Open top Live link | Live Mode page loads | Header link resolves to `/live-mode/` and loads | Live Mode page explains pick/generate/accept flow | LOW | PASS |
| Direct Live alias | Open `https://impeccable.style/live` | Should redirect or load Live Mode | This fetch returned an internal error in the web tool | Direct route alias inconsistent in this pass | MEDIUM | PARTIAL |
| Case link | Open live build | Neo Mirai live build loads | `/neo-mirai/` loads conference page with nav, agenda, speakers, tickets | Case page has nav, ticket CTAs, section links | LOW | PASS |
| Chrome extension CTA | Open extension listing | Extension listing loads | Chrome Web Store page loads with rating/users/overview | Store page confirms local detection, click-to-inspect, no data sent | LOW | PASS |
| GitHub link | Open GitHub repo | Repo loads | GitHub repo loads with folders, README, stars/forks | Repo exposes source, CLI, extension, tests, site | LOW | PASS |

## Pass 3: Edge And Failure

| Edge Case | Feature | Steps | Expected | Actual | Status | Issue ID |
| --- | --- | --- | --- | --- | --- | --- |
| Deep link anchor | `#why` | Open `https://impeccable.style/#why`; search source for `id="why"` | Anchor should target a stable section | No `id="why"` was found in fetched HTML | PARTIAL | IMP-001 |
| Route alias | Live page | Open `/live`; open nav Live | Both should resolve consistently | Nav link resolves to `/live-mode/`; direct `/live` fetch errored in this pass | PARTIAL | IMP-002 |
| External store | Chrome extension | Open Chrome Web Store link | Store page should load | Store page loaded | PASS |  |
| Open source proof | GitHub | Open repo | Repo should be public and relevant | Repo loaded and includes site, extension, CLI, tests, skills | PASS |  |
| Functional install | CLI/skill | Attempt not executed | Should be tested in local project | Not run due environment and safety boundary | UNKNOWN | IMP-003 |
| Browser overlay | Extension | Install not executed | Overlay should highlight DOM issues | Not run due environment and safety boundary | UNKNOWN | IMP-004 |

## Pass 4: Visual And Deployment

### Aesthetic/Product Quality

| Area | Position | Expected | Observed | Severity | Issue ID |
| --- | --- | --- | --- | --- | --- |
| Product intent | homepage hero | Concrete offer and audience | Strong: AI harnesses, design fluency, commands, CLI/extension | LOW |  |
| Pattern specificity | Slop page | Concrete anti-pattern vocabulary | Strong: anti-pattern catalog and deterministic/LLM/browser detection modes | LOW |  |
| Workflow explanation | Live Mode | Clear pick/generate/accept flow | Strong source explanation, but not executable in this pass | MEDIUM | IMP-004 |
| Deep-link polish | `#why` | Shared URL should land on intended section | Anchor target not visible in fetched HTML | MEDIUM | IMP-001 |
| Route consistency | `/live` vs `/live-mode/` | Alias should be stable | Possible direct alias inconsistency | MEDIUM | IMP-002 |
| Visual verification | all pages | Desktop/mobile screenshots and spacing checks | Not available in this pass | MEDIUM | IMP-005 |

### Deployment Readiness

| Requirement | Status | Evidence | Missing/Risk | Issue ID |
| --- | --- | --- | --- | --- |
| Domain + SSL | PASS | `https://impeccable.style/` loads. | None observed. |  |
| Source repository | PASS | GitHub repo is public and contains site, CLI, extension, skill folders, tests. | None observed. |  |
| CLI/package | SOURCE-PASS | Site and repo reference `npx impeccable detect` and npm install. | CLI execution not tested here. | IMP-003 |
| Chrome extension | SOURCE-PASS | Store listing loads and claims local detection/no data sent. | Extension not installed/executed here. | IMP-004 |
| Live Mode | SOURCE-PASS | `/live-mode/` describes local dev server/HMR support. | Requires local repo/HMR test. | IMP-004 |
| SEO/crawlability | PASS WITH NOTES | Text content is crawlable across homepage, docs, slop, live-mode, case page. | Need Lighthouse/browser pass for metadata, OG, mobile. | IMP-005 |
| Monitoring/analytics | UNKNOWN | Not observable from source-level pass. | Needs headers/network/browser pass. |  |

## Issue Cards

### IMP-001 - MEDIUM - `#why` Deep Link Does Not Expose A Matching Anchor In Fetched HTML

- Area: navigation/routing.
- URL: `https://impeccable.style/#why`
- Live position: incoming deep link.
- Locator: `#why`; fetched page search found no `id="why"`.
- Workflow step: `1. Open shared URL -> 2. Expect target section -> 3. Verify anchor exists`.
- Expected: The shared URL lands on a stable "why" section or equivalent.
- Actual: The page content loads, but no `id="why"` was visible in fetched HTML.
- Evidence: `find id="why"` returned no match.
- Problem: Shared links may not scroll users to the intended section, which weakens reference/share workflows.
- Likely cause: Anchor changed, generated heading id differs, or old URL fragment remains.
- Fix: Add a stable alias anchor for `why`, or redirect users to the current section id.
- Copy prompt: `Add backward-compatible deep-link support for #why on impeccable.style. Locate the intended section, add id="why" or a hidden anchor, and verify that https://impeccable.style/#why scrolls to the correct section on desktop and mobile.`
- Validation: Opening `/#why` lands at the intended section and source/DOM contains a stable anchor.
- Retest pass: pending.

### IMP-002 - MEDIUM - Direct `/live` Route Needs Alias Verification

- Area: routing.
- URL: `https://impeccable.style/live`
- Live position: Live Mode route.
- Locator: top nav `Live` resolves to `/live-mode/`.
- Workflow step: `1. Open /live -> 2. Open nav Live -> 3. Compare final route`.
- Expected: `/live` redirects cleanly to `/live-mode/` or serves the same content.
- Actual: The nav link works, but direct `/live` returned an internal error in this pass.
- Evidence: top nav click loaded `/live-mode/`; direct `/live` fetch was not usable.
- Problem: Route aliases that fail create broken shared links and reduce reliability.
- Likely cause: missing redirect, tool-specific fetch issue, or route mismatch.
- Fix: Add/verify a server redirect from `/live` to `/live-mode/`.
- Copy prompt: `Verify the /live route. If it does not redirect to /live-mode, add a permanent redirect and test direct navigation, top-nav click, and mobile nav.`
- Validation: `/live` and nav `Live` both resolve to the same Live Mode page.
- Retest pass: pending.

### IMP-003 - HIGH - CLI Claims Need Local Execution Evidence

- Area: deployment/tooling.
- URL: `https://impeccable.style/`
- Live position: Get Started / CLI install section.
- Locator: `npm i -g impeccable`, `npx impeccable detect src/`.
- Workflow step: `1. Install or npx CLI -> 2. Run detect -> 3. Inspect JSON/exit code`.
- Expected: CLI runs deterministically and returns findings/exit code.
- Actual: Not executed in this environment.
- Evidence: Site and GitHub document CLI usage, but no local execution log exists in this audit.
- Problem: For tool-audit acceptance, install/run must be proven separately from marketing/docs.
- Likely cause: Source-level pass boundary.
- Fix: Add a local fixture page with known slop issues, run `npx impeccable detect --json`, and record output.
- Copy prompt: `Create a fixture page with gradient text, nested cards, low contrast, and long line length. Run npx impeccable detect --json against it and record detected rules, exit code, and false positives.`
- Validation: CLI output catches expected rules and returns documented exit behavior.
- Retest pass: pending.

### IMP-004 - HIGH - Browser Extension And Live Mode Need Real Browser Flow Testing

- Area: functional/browser workflow.
- URL: `https://impeccable.style/live-mode/` and Chrome Web Store listing.
- Live position: Live Mode demo and extension install/use flow.
- Locator: `Pick`, `Generate`, `Accept`, Chrome extension overview.
- Workflow step: `1. Install/start tool -> 2. Open page -> 3. Pick element -> 4. Generate variants/detect issues -> 5. Accept/jump to element`.
- Expected: Extension overlays issues; Live Mode writes accepted variant to source.
- Actual: Source pages load, but extension/live execution was not run.
- Evidence: Chrome listing and Live Mode docs describe the workflows.
- Problem: These are core product claims and need clicked-flow proof.
- Likely cause: Requires Chrome extension install or local dev server/HMR.
- Fix: Run Playwright/manual browser test with a local fixture app and capture screenshots/logs.
- Copy prompt: `Run a browser acceptance test for Impeccable Live Mode and extension. Use a local fixture app, pick a visible element, generate variants, accept one, verify source changed, then run extension detection and record highlighted DOM elements.`
- Validation: Screenshots, source diff, and detector results are attached.
- Retest pass: pending.

### IMP-005 - MEDIUM - Visual Pixel QA Was Not Completed

- Area: visual quality.
- URL: all inspected pages.
- Live position: desktop/mobile viewports.
- Locator: screenshots unavailable in this pass.
- Workflow step: `1. Capture desktop -> 2. Capture mobile -> 3. Check layout, spacing, contrast, overflow`.
- Expected: Visual score based on screenshot evidence.
- Actual: Score is source-based, not pixel-based.
- Evidence: Text crawl shows strong IA/copy, but no screenshots or computed contrast logs.
- Problem: Aesthetic judgement needs viewport evidence for layout, mobile, spacing, contrast, and motion.
- Likely cause: Browser/screenshot tool was not used in this pass.
- Fix: Run browser screenshot pass and attach visual findings.
- Copy prompt: `Capture desktop and mobile screenshots for homepage, docs, slop, live-mode, and neo-mirai. Score first viewport, hierarchy, spacing, typography, responsive behavior, contrast, and AI slop signals.`
- Validation: Each page has screenshot-backed visual issue cards or explicit PASS notes.
- Retest pass: pending.

## Pass 5: Retest And Learn

| Prior Issue | Retest Step | Previous Status | Current Status | Regression? | Lesson |
| --- | --- | --- | --- | --- | --- |
| IMP-001 | Re-open `/#why` and inspect DOM anchor | new | pending | unknown | Deep links need first-class acceptance checks. |
| IMP-002 | Re-open `/live` and nav Live | new | pending | unknown | Route aliases should be tested separately from nav clicks. |
| IMP-003 | Run CLI against fixture | new | pending | unknown | Tool products need execution evidence, not only docs. |
| IMP-004 | Run extension/live browser flow | new | pending | unknown | Browser-integrated claims need browser-level proof. |
| IMP-005 | Capture screenshots | new | pending | unknown | Aesthetic audits need screenshot evidence. |

## Experience Ledger

### Repeated Failure Patterns

| Pattern | Seen In | Why It Matters | New Guardrail |
| --- | --- | --- | --- |
| Source evidence mistaken for live behavior | CLI, extension, Live Mode | Docs can be accurate while runtime still fails. | Mark tool claims as source-pass until executed. |
| Deep links and route aliases skipped | `#why`, `/live` | Shared URLs break even when nav works. | Add route/deep-link checks to live functional audit. |
| Visual score without screenshots | all inspected pages | Taste claims need viewport evidence. | Mark visual score as source-based until screenshots exist. |

### Good Fix Prompts

| Prompt | Worked Because | Reuse When |
| --- | --- | --- |
| `Verify the /live route. If it does not redirect to /live-mode, add a permanent redirect and test direct navigation, top-nav click, and mobile nav.` | Names exact route, expected redirect, and validation. | Route alias issues. |
| `Add backward-compatible deep-link support for #why...` | Names exact fragment and desired behavior. | Broken anchors/shared links. |

### Guardrail Updates Proposed

| Target File | Proposed Change | Reason |
| --- | --- | --- |
| `live-functional-audit.md` | Add explicit route alias and deep-link validation. | Real audit found route/anchor risks. |
| `webpage-audit-rubric.md` | Require screenshot-backed visual scoring. | Prevent source-only visual claims. |

## Final Verdict

- Verdict: PASS WITH NOTES.
- Functional score: 74/100 source + safe-link pass.
- Visual score: 78/100 source-based only; screenshot pass required.
- Deployment readiness: PARTIAL.
- Critical blockers: none confirmed.
- High blockers before full acceptance: CLI execution, extension overlay test, Live Mode local flow test.
- Fix first: route/deep-link consistency, then browser-level execution proof.
- Ready for next pass: yes, with browser automation or manual Chrome test.
