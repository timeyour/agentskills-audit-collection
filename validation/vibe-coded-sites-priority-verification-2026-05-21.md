# Priority Verification: Vibe-Coded Website Candidates

Date: 2026-05-21

## Scope

Verify the user's 14-site candidate set:

- Priority 1: Attendflow, Creativable, RefineAI, Pipeline.app, Vendor Vault, atomical.ai, User Insights Hub, RedFlag.
- Priority 2: Strategly, Simple Forms, Namegator, Markdn, Your Watchlists, SaaStr.ai VC Valuation Calculator.

This pass separates:

```text
source evidence -> live site opens -> browser-rendered surface -> safe CTA probe -> verdict
```

It does not submit private data, upload real documents, create accounts, pay, delete, or trigger destructive actions.

## Evidence Method

- Source pages were checked through Made with Lovable, Replit Gallery, Vercel Community, and v0 template pages.
- Live sites were opened in a real browser using local Chrome via Playwright.
- For safe entries, the main CTA was clicked only far enough to verify destination or visible next-step surface.
- HTTP/static checks were used only as fallback for sites that failed in the browser.

Evidence labels:

- `FLOW-OBSERVED`: a safe CTA or app surface was opened and the next-step flow was visible.
- `LIVE-OPENS`: the site rendered, but the key flow was not clicked or did not complete.
- `SOURCE-ONLY`: source evidence exists, but live evidence is blocked or insufficient.
- `REJECTED`: live site failed or attribution/live link mismatch makes it unsuitable for the shortlist.

## Results

| Site | Priority | Platform | Source | Live | Score | Evidence | Verdict | Key Evidence |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| Attendflow | P1 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/attendflow) | [Live](https://attendflowio.lovable.app/) | 12 | `LIVE-OPENS` | `WORTH-DISSECTING` | Browser rendered event marketing SaaS with Pricing, Sign In, Start Free, Book a Demo, dashboard-style reporting, CRM/pipeline language, email inputs, and forms. CTA click probe timed out, so do not mark signup as proven yet. |
| Creativable | P1 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/creativable) | [Live](https://creativable.de/) | 12 | `LIVE-OPENS` | `WORTH-DISSECTING` | Browser rendered custom domain with community + CRM + AI agent positioning, Pricing, Start Now, Start Free, contact, and a visible AI prompt input. Good business-system reference, but account flow was not completed. |
| RefineAI | P1 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/refineai) | [Live](https://refined-ai.com/) | 14 | `FLOW-OBSERVED` | `WORTH-DISSECTING` | Demo Audit CTA opened `/audit-demo` and showed a sample portfolio audit report with score, analysis sections, share, and PDF download. Strong input-output product reference. Console showed some 404 resource errors that should be checked separately. |
| Pipeline.app | P1 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/pipelineapp) | [Live](https://pipeline.app/) | 10 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Browser rendered service positioning: AI workflow audit, implementation, ROI, Book AI Audit. CTA did not navigate in the probe, likely a popup/embedded booking or blocked script. Good service-site structure, weaker product-flow proof. |
| Vendor Vault | P1 | Replit | [Replit Gallery](https://replit.com/gallery/work/businesses/vendor-vault) | [Live](https://vendor-vault.ai/) | 14 | `FLOW-OBSERVED` | `WORTH-DISSECTING` | Start Free Trial opened `/app` with login/register, email/password fields, cookie controls, plus pricing/contact/contract-risk positioning. Strongest enterprise workflow candidate in this batch. |
| atomical.ai | P1 | Replit | [Replit Gallery](https://replit.com/gallery/work/businesses/atomical-ai) | [Live](https://atomical.ai/) | 13 | `LIVE-OPENS` | `WORTH-DISSECTING` | Retry after cookie banner rendered demo workspace, nested project hierarchy, Pricing, Sign In, Get Started, docs, privacy, and terms. Good app/product-structure reference. First pass had JS/network instability, so run physical regression before using as a benchmark. |
| User Insights Hub | P1 | Replit | [Replit Gallery](https://replit.com/gallery/work/product/user-insights-hub) | [Live](https://user-insights-hub.replit.app/) | 10 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Live app opened directly into a customer-insights dashboard with chat history, interviews, insights, themes, settings, and a question textarea. Strong product-surface proof, but public default-domain exposure of sample/user-like chat history is a trust/privacy caution. |
| RedFlag / ContractGuard | P1 | v0 / Vercel Community | [Vercel Community](https://community.vercel.com/t/redflag-ai-contract-auditor/40303) | [Source-linked live app](https://v0-contract-audit.vercel.app/) | 11 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Source-linked app opened as ContractGuard with contract textarea, `.txt` upload, Analyze Contract CTA, and legal-disclaimer surface. The separate `redflagcontract.ai` domain returned `ERR_CONNECTION_CLOSED` in Chrome, so use the Vercel app for verification unless that domain recovers. |
| Strategly | P2 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/strategly) | [Live](https://strategly.lovable.app/) | 9 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Start Learning Now opened `/explore` with case-study list, search, filters, learn/quiz/flashcard actions, login/signup. Supabase case-study request produced a fetch error, so treat it as a content-learning app with reliability caveat. |
| Simple Forms | P2 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/simple-forms) | [Live](https://simp1eform.com/) | 2 | `SOURCE-ONLY` | `REJECTED` | Source page opens, but live domain failed in browser with `ERR_CONNECTION_CLOSED`; Python HTTPS also hit SSL EOF. Do not shortlist until the live site recovers. |
| Namegator | P2 | Lovable | [Made with Lovable](https://madewithlovable.com/projects/namegator) | [Live](https://namegator.lovable.app/) | 7 | `LIVE-OPENS` | `VISUAL-ONLY` | SEO landing page rendered with business-name generator positioning and Generate Names CTA, but the CTA probe stayed on the same page and no visible input/output flow was captured. Useful SEO/copy reference, not a verified tool flow yet. |
| Markdn | P2 | v0 | [v0 template](https://v0.app/templates/markdn-a-markdown-editor-qYpR7JYbx09) | [Live](https://markdn.vercel.app/) | 8 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Browser rendered an editor/preview surface with saved-local copy, export/download language, and checkbox content. Good interactive tool demo, but not a business-closure reference. |
| Your Watchlists | P2 | Replit | [Replit Gallery](https://replit.com/gallery/life/entertainment/your-watchlists) | [Live](https://yourwatchlists.com/) | 13 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Sign In / Register opened auth form with Google login, email/password, privacy, terms, contact, and movie tracking proposition. Strong functioning app surface, but lower relevance for B2B/business-closing patterns. |
| SaaStr.ai VC Valuation Calculator | P2 | Replit | [Replit Gallery](https://replit.com/gallery/life/finance/saastr-ai-vc-valuation-calculator) | [Live](https://saastr.ai/valuation-calculator) | 10 | `FLOW-OBSERVED` | `USEFUL-REFERENCE` | Page rendered valuation positioning, authority markers, email form, and Connect flow. Strong authority-building reference, but browser probe reached a Connect/waitlist surface rather than a fully exercised valuation calculation. |

## Priority Shortlist

Best candidates to dissect first:

1. Vendor Vault
2. RefineAI
3. atomical.ai
4. Attendflow
5. Creativable
6. User Insights Hub

Best candidates for actual `/physical-flow-test` next:

1. Vendor Vault: trial/login/contract-analysis path.
2. RefineAI: submit portfolio and demo audit paths.
3. RedFlag / ContractGuard: paste sample contract -> analyze -> report.
4. User Insights Hub: ask question -> generated/returned insight.
5. Attendflow: Start Free / Book Demo / CRM dashboard path.

## Findings

- `S1`: Simple Forms should be rejected from the usable shortlist until the live domain opens reliably.
- `S1`: RedFlag naming/live-link ambiguity must be resolved. The Vercel Community source-linked app works, but `redflagcontract.ai` failed in browser.
- `S2`: Strategly rendered useful content, but its Supabase fetch produced a runtime error during the browser run.
- `S2`: atomical.ai rendered on retry, but the first run saw JS/network instability; use a repeated physical check before treating it as a benchmark.
- `S3`: Pipeline.app has a strong service-site story, but the Book AI Audit CTA did not produce a clear navigated destination in this probe.
- `S3`: Namegator looks like an SEO landing page unless the generator input/output flow can be found and exercised.

## Lessons

- The best "vibe-coded" references are not the prettiest pages; they expose a safe next-step surface.
- Source evidence and live browser evidence can disagree. RedFlag/ContractGuard is the clearest example in this batch.
- Default domains are not automatically bad: User Insights Hub and Markdn expose real product surfaces.
- Custom domains are not automatically good: Simple Forms failed live verification.
- A case should not graduate from inspiration list to benchmark until at least one CTA or workflow is observed.

## Next Regression Checks

Run `/physical-flow-test` against the five strongest candidates with safe demo data:

```text
Vendor Vault: open live site -> Start Free Trial -> login/register surface -> no real registration
RefineAI: open live site -> Demo Audit -> sample report visible -> no account creation
ContractGuard: paste harmless sample clause -> Analyze Contract -> report visible
User Insights Hub: ask harmless public question -> response area updates
Attendflow: Start Free / Book Demo -> destination visible -> no real account creation
```
