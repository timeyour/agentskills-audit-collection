# Public Website Audit Report Template

> **Canonical copy:** [templates/public-website-audit-report-template.md](templates/public-website-audit-report-template.md) (v0.1). This root file is kept for backward links.

Use this template when turning an AgentSkills audit into a shareable report for a website owner, client, teammate, or public benchmark.

The public report should hide internal agent mechanics. It should show the user:

```text
what is broken -> why it matters -> evidence -> how to fix -> how to retest
```

## Report Metadata

```text
Title:
Target URL:
Date:
Auditor:
Audit Mode: source / live / physical-browser / mixed
Overall Risk: S0 / S1 / S2 / S3 / S4
Report URL:
Artifacts:
```

## Executive Summary

Write 3-5 short bullets:

- What is the site trying to do?
- Can the core workflow be trusted today?
- What are the highest-risk findings?
- What should be fixed first?
- What evidence is missing, if any?

## Scorecard

| Area | Status | Notes |
| --- | --- | --- |
| Offer clarity | PASS / WARN / FAIL | |
| Primary CTA | PASS / WARN / FAIL | |
| Core workflow | PASS / WARN / FAIL | |
| Mobile layout | PASS / WARN / FAIL | |
| Visual trust | PASS / WARN / FAIL | |
| Performance | PASS / WARN / FAIL | |
| Accessibility | PASS / WARN / FAIL | |
| SEO basics | PASS / WARN / FAIL | |
| Deployment readiness | PASS / WARN / FAIL | |
| Evidence quality | PASS / WARN / FAIL | |

## Top Findings

Use one card per issue.

```text
Finding:
Severity:
Scope:
Evidence:
Impact:
Fix Suggestion:
Regression Check:
Owner:
Status:
```

## Finding Card Format

### [S1] Primary CTA does not complete a useful workflow

| Field | Detail |
| --- | --- |
| Scope | Homepage hero CTA |
| Evidence | Screenshot, click trace, or route URL |
| Impact | Visitors cannot reach the intended next step, reducing conversion and trust. |
| Fix Suggestion | Route the CTA to a specific signup, booking, upload, or contact flow. Add a success state after completion. |
| Regression Check | Click the CTA in a real browser and verify the expected page or form appears within 3 seconds. |

## Evidence

Separate evidence types clearly:

| Evidence Type | Example | Status |
| --- | --- | --- |
| SOURCE | repository file, HTML, config, docs | available / missing |
| LIVE | live URL, route, page text, public network behavior | available / missing |
| PHYSICAL | Playwright trace, screenshot, HAR, console log, video | available / missing |
| INFERRED | reasonable conclusion from partial evidence | label clearly |
| UNKNOWN | not checked or blocked | label clearly |

## Fix Priority

| Priority | Action | Reason |
| --- | --- | --- |
| P0 | Fix S0 blockers | Site cannot be delivered safely. |
| P1 | Fix S1 trust/conversion/workflow risks | Core business result is at risk. |
| P2 | Fix S2 usability/performance issues | Launch may be possible with known risk. |
| P3 | Address S3/S4 refinements | Improve copy, layout, and minor interaction after core risks are handled (S3 = 打磨/润色, not 波兰语). |

## Copyable Fix Prompt

Include a prompt the site owner can paste into an AI coding agent:

```text
Fix the following website issue:

Issue:
[plain-language issue]

Evidence:
[screenshot/route/log/source detail]

Expected behavior:
[observable expected result]

Constraints:
- Preserve existing brand and layout system.
- Do not change unrelated routes.
- Add or update tests where practical.
- Provide a regression check.
```

## Regression Check

```text
After fixes are applied:
1. Re-open the target URL.
2. Repeat each failing workflow.
3. Capture screenshot or trace evidence.
4. Confirm expected behavior.
5. Mark each finding as fixed, still failing, or needs more evidence.
```

## Lessons

Capture reusable guardrails:

- A landing page is not shippable until the primary CTA reaches a real next step.
- A public report must separate source, live, and physical evidence.
- A fix suggestion is incomplete unless it includes a regression check.
- A good audit report should be understandable without reading the skill implementation.

## Anti-Patterns

- Publishing vague opinions without evidence.
- Showing internal agent reasoning instead of user-facing findings.
- Calling a site broken without reproduction steps.
- Reporting screenshots without explaining impact.
- Giving fixes without a retest plan.
- Mixing source-only findings with real-browser findings without labels.
