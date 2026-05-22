# Permission Model

Use this reference before any live audit, flow test, physical browser test, deployment check, or security-adjacent review that can touch a real website, app, account, or data surface.

The goal is simple:

```text
least privilege -> safe execution boundary -> explicit skip or approval -> evidence-backed report
```

Do not let the agent "just click around" without a permission level. Every live action must fit one of the levels below.

## Permission Levels

### L0 Public Read-Only

Allowed:

- Open public pages.
- Read visible text and page structure.
- Inspect source, headers, public network requests, and public assets.
- Capture screenshots of public pages.
- Record non-sensitive console output.

Not allowed:

- Form submission.
- Login attempts.
- Uploads.
- Mutating actions.
- Private account access.

Use for production sites when no explicit test account or safe environment is provided.

### L1 Safe Click And Navigation

Allowed:

- Click public navigation, anchors, tabs, menus, accordions, filters, and non-submitting controls.
- Open public CTA destinations.
- Test route existence and visible error states.
- Use dummy data only in fields that are not submitted.

Not allowed:

- Submit forms that send email, create records, charge money, or mutate production data.
- Accept terms, book appointments, start trials, or create accounts unless explicitly allowed.

Use for most public website audits.

### L2 Test Account Flow

Allowed:

- Use a provided test account.
- Submit safe test forms in a sandbox, preview, local, or explicitly approved test environment.
- Test login, logout, dashboard views, uploads of harmless dummy files, and reversible settings.

Required:

- State the account/environment boundary in the progress update.
- Keep credentials out of reports.
- Use dummy data and clearly mark generated records as test data.

Not allowed:

- Real payment.
- Production account mutation.
- Private user data extraction.
- Admin-only destructive actions.

### L3 Staging Authorized Security Check

Allowed only when the user explicitly identifies the target as staging, preview, local, or a security test sandbox.

Allowed:

- Check auth boundaries with test roles.
- Probe input validation with harmless payloads.
- Verify CSRF, CORS, security headers, and access-control behavior.
- Upload safe dummy files if the flow is designed for uploads.

Required:

- Use minimal payloads.
- Avoid stress, fuzzing, brute force, or denial-of-service behavior.
- Stop immediately if real data appears.

### L4 Production Guarded Audit

Production audits default to L0 or L1 unless the user explicitly grants more scope.

Allowed:

- Public read-only checks.
- Safe public navigation.
- Header, SEO, asset, accessibility, and performance observation.
- Non-mutating authenticated checks with a test account only when approved.

Required:

- Mark high-risk or unclear actions `SKIPPED-SAFE`.
- Ask for staging, a test account, or artifacts before deeper execution.
- Never run destructive or adversarial security tests against production.

## Always SKIPPED-SAFE

Mark these actions `SKIPPED-SAFE` unless the user provides explicit approval and a safe test environment:

- Real payment or checkout completion.
- Deletion, account closure, or irreversible submission.
- Password changes, email changes, permission changes, or admin mutations.
- Sending real email, SMS, webhook, notification, or social post.
- Production data creation, update, import, export, or private data extraction.
- Uploads containing private, regulated, copyrighted, or customer files.
- Rate-limit, brute-force, stress, scraping, or denial-of-service behavior.
- Attempts to bypass access controls outside an authorized staging security check.

## Progress Update Requirements

When a boundary appears, emit a progress update before continuing:

```text
Progress Update [stage N] - Permission boundary
Status: needs confirmation / SKIPPED-SAFE
What I just did: Identified a higher-risk action.
Key findings so far: [the action and why it matters]
Evidence collected: [URL, locator, screenshot, source reference, or none]
Blocked / Skipped: [permission level and reason]
Next step: Continue with safe checks, wait for explicit approval, or request a staging/test account.
```

## Evidence Handling

- Never include raw secrets, passwords, cookies, tokens, session IDs, private account data, or unredacted HAR content in reports.
- Redact screenshots if they contain personal data, customer data, private docs, or payment information.
- Treat console logs and network payloads as potentially sensitive.
- If redaction is not possible, summarize the evidence instead of reproducing it.

## Anti-Patterns

- Clicking destructive controls because they are visible.
- Treating production as a playground.
- Submitting a contact form that sends a real email without approval.
- Calling an action safe because it "probably" has no side effect.
- Hiding skipped actions until the final report.
- Using fake credentials against a real login form repeatedly.
- Running security payloads against production without explicit authorization.
