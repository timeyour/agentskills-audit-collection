# Progressive Reporting

Use progressive reporting when an audit, flow test, visual QA pass, deploy check, or five-pass acceptance run takes more than a few discrete steps. The goal is to make the agent's work observable while it is happening, not only after the final report.

```text
intake -> step execution -> progress update -> evidence checkpoint -> next step -> final report
```

Progressive reporting does not replace the final audit report. It creates a live trail that helps the user see what was checked, what evidence exists, what is still unknown, and where the audit is heading.

When the user wants a **visual workbench** (not only chat), also follow `live-run-protocol.md`: update `validation/artifacts/{runId}/run-state.json` and append `run-events.ndjson` so `workbench/live/` can poll progress in real time.

## When To Use

Use progressive reporting when:

- The user asks to test a whole website, app, repo, or batch.
- The workflow has more than five meaningful steps.
- The audit includes live browsing, real clicks, screenshots, Playwright traces, console/network review, or deployment checks.
- The run may take long enough that the user needs status before the final report.
- A critical issue appears and the next action could change the scope, safety level, or priority.
- The user explicitly asks for transparent, step-by-step, or "what are you doing now" reporting.

For tiny source-only checks, use a concise final answer instead of progress noise.

## Core Rules

1. Report progress after each meaningful audit stage or every three to five important actions.
2. Keep progress updates short and factual.
3. Separate confirmed evidence from early observations.
4. Do not turn partial observations into final verdicts.
5. If a blocker appears, report it immediately with the current evidence and the next safe option.
6. If a step touches auth, payment, deletion, private data, or production mutation, pause and mark the action `NEEDS-USER-CONFIRMATION`.
7. Do not leak secrets, raw cookies, tokens, unredacted HAR content, private account data, or sensitive screenshots in progress updates.
8. The final report must still use the shared output shape: Scope, Evidence, Findings, Severity, Reproduction, Fix Suggestion, Regression Check, Lessons.

## Progress Update Format

Use this exact shape unless the user asks for a different format:

```text
Progress Update [current/total] - [stage name]
Status: [in progress / completed / issue found / blocked / needs confirmation]
What I just did: [one or two concrete actions]
Key findings so far: [confirmed facts only, or "none yet"]
Evidence collected: [source file, URL, screenshot, trace, console, network, test output, or "none yet"]
Next step: [the next action]
```

If the total number of steps is unknown, use:

```text
Progress Update [stage N] - [stage name]
```

## Evidence Labels

Use the strongest truthful label:

- `SOURCE`: repo file, docs, config, package metadata, or source code.
- `LIVE`: opened page, clicked flow, browser screenshot, DOM locator, network request, or console output.
- `PHYSICAL`: Playwright trace, screenshot, HAR, video, console log, or result JSON from real execution.
- `INFERRED`: reasoned from available evidence, not directly proven.
- `UNKNOWN`: not checked, blocked, or not enough evidence.

Do not promote `SOURCE` or `INFERRED` evidence into `LIVE` or `PHYSICAL`.

## Safety Pause Format

Use this when the next action could mutate real data or expose private information:

```text
Progress Update [stage N] - Safety pause
Status: needs confirmation
What I just did: Identified a high-risk action.
Key findings so far: [what the action is and why it matters]
Evidence collected: [locator, URL, screenshot, source reference, or none]
Next step: Waiting for explicit permission, test account, sandbox URL, or safe-skip decision.
```

High-risk actions include real payment, deletion, account closure, email/SMS sending, webhook dispatch, permission changes, admin access, production data mutation, and uploads containing private files.

## Final Report Handoff

At the end of the run, convert progress updates into a clean final report. Do not paste every progress update verbatim unless the user asks for a full log.

The final report should include:

- Scope.
- Evidence summary.
- Findings.
- Severity.
- Reproduction.
- Fix Suggestion.
- Regression Check.
- Lessons.

If progress updates revealed an evidence gap, preserve it in the final report instead of smoothing it over.

## Example

```text
Progress Update [2/7] - Live functional audit
Status: issue found
What I just did: Opened the homepage, clicked the primary Get Started CTA, and checked the destination route.
Key findings so far: The CTA is visible, but it opens a waitlist form instead of the promised dashboard demo.
Evidence collected: LIVE: homepage URL, CTA text, destination URL, screenshot.
Next step: Test the waitlist form with safe dummy data and verify success/error states.
```

## Anti-Patterns

- Staying silent during a long audit and only delivering a final verdict.
- Reporting "looks good" without evidence.
- Treating a progress update as the final audit.
- Flooding the user after every minor click or file read.
- Hiding blockers until the end.
- Claiming a flow works before real execution evidence exists.
- Sharing unredacted network, auth, or user data in a progress update.
