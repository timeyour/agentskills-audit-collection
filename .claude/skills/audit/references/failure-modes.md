# Failure Modes Library

Use this reference when auditing AI-built products, vibe-coded sites, generated code, or agent-produced delivery claims.

The goal is not to collect scary examples. The goal is to turn repeated failure patterns into evidence-backed checks that can be located, fixed, and retested.

## Evidence Policy

Separate each finding by evidence type:

| Evidence Type | Meaning |
| --- | --- |
| Source evidence | Code, config, docs, tests, dependencies, templates, or committed files show the issue. |
| Live/browser evidence | A real page, workflow, request, console log, network trace, screenshot, or user-provided artifact shows the issue. |
| Execution evidence | Tests, scripts, CI, Playwright traces, logs, or command output show the issue. |
| Assumption | The issue is plausible but not yet proven. Label it as an assumption and do not treat it as a finding. |

Do not promote a failure mode into a finding unless it has source, live, or execution evidence.

## Severity Mapping

| Severity | Failure Mode Trigger |
| --- | --- |
| `S0` | Core workflow blocked, data loss risk, serious security exposure, destructive production risk, hardcoded production secrets, missing backend dependency for launch-critical flow. |
| `S1` | Major correctness, privacy, trust, auth, payment, reliability, or conversion risk. |
| `S2` | Noticeable functional, UX, performance, validation, accessibility, or deployment issue that can launch only with known risk. |
| `S3` | Refinement (打磨/润色): copy, layout, maintainability, or small edge-case gap. |
| `S4` | Future hardening, benchmark idea, or non-blocking improvement. |

## Core AI Delivery Failure Modes

### 1. Validation Checks Only Presence, Not Meaning

Trigger signals:
- Required fields are checked, but format, length, range, enum, ownership, or unsafe content is not checked.
- Form accepts invalid email, phone, URL, date, file type, or script-like content.
- API validates that a field exists but not whether it is valid for the business rule.

Evidence requirements:
- Source: validation code, schema, route handler, form component, or test gap.
- Live/browser: invalid input accepted, unclear error, or unsafe content rendered.

Check:
- Test empty, malformed, too long, wrong type, boundary value, duplicate, and script-like inputs.
- Verify both client-side and server-side validation when source is available.

Default severity:
- `S1` when invalid data enters a core workflow or can create security/privacy risk.
- `S2` when it harms UX or data quality without immediate security impact.

Fix prompt:

```text
Fix input validation for [flow/field]. Add server-side semantic validation for [format/range/length/ownership], keep client-side feedback aligned, return clear user-facing errors, and add regression tests for invalid, boundary, and malicious-looking inputs.
```

### 2. Concurrency or State Mutation Has No Guardrail

Trigger signals:
- Read-check-write flow without transaction, lock, idempotency key, optimistic concurrency, or unique constraint.
- Duplicate submit creates duplicate orders, bookings, messages, credits, or tasks.
- State changes depend on stale client state.

Evidence requirements:
- Source: mutation flow, missing transaction/lock/constraint, missing duplicate-submit protection.
- Execution/live: repeated click, refresh, or parallel request creates inconsistent state.

Check:
- Attempt safe duplicate submissions in staging or demo data only.
- Inspect whether critical mutations have idempotency, transactions, or constraints.

Default severity:
- `S0` for payment, inventory, account, permission, or destructive data flows.
- `S1` for important non-destructive workflow inconsistency.

Fix prompt:

```text
Harden [mutation flow] against duplicate and concurrent execution. Add idempotency or transaction protection, enforce a server-side uniqueness/ownership constraint, disable duplicate client submits, and add a regression test that sends repeated requests.
```

### 3. N+1 Query or Unbounded Fetch

Trigger signals:
- Loop performs database/API calls per item.
- List page loads all records before filtering or pagination.
- Dashboard works for sample data but will slow down with production data.

Evidence requirements:
- Source: looped query/API calls, missing pagination, missing batch load.
- Execution/live: request waterfall, slow list load, repeated endpoints, high query count.

Check:
- Search for per-row fetches and list endpoints with no limit/page cursor.
- Use network waterfall or logs to count repeated calls.

Default severity:
- `S1` if it can take down a core dashboard, marketplace, search, or admin flow.
- `S2` for non-core pages or small-data tools.

Fix prompt:

```text
Replace the N+1/unbounded fetch in [route/component] with batched loading and server-side pagination. Add limits, indexes if needed, and a regression test or fixture with enough rows to expose repeated queries.
```

### 4. Exception Handling Silently Swallows Real Failures

Trigger signals:
- Broad `catch Exception`, empty catch block, generic fallback, or log-only error.
- User sees success even when backend request failed.
- Console/network shows errors but UI keeps a false success state.

Evidence requirements:
- Source: broad catch, missing rethrow, no user error state, no telemetry.
- Live/browser: failed request, console error, no visible failure state.

Check:
- Inspect error branches and simulate failed network/API response when safe.
- Confirm loading, retry, user-facing error, and recovery behavior.

Default severity:
- `S1` when it masks failed saves, auth, payment, upload, export, or delivery-critical operations.
- `S2` when it creates confusing but recoverable UI.

Fix prompt:

```text
Replace silent error handling in [flow] with typed error branches, user-visible failure states, retry or recovery where appropriate, and regression coverage for failed request and timeout cases.
```

### 5. Memory Pagination or Client-Only Data Filtering

Trigger signals:
- Backend returns entire dataset and UI slices locally.
- Search/filter/sort happens only after all records load.
- Export or admin page assumes tiny data.

Evidence requirements:
- Source: `slice`, `subList`, full table load, missing query params, no database pagination.
- Live/browser: large payload, slow first response, memory pressure, frozen UI.

Check:
- Inspect API request/response size and list implementation.
- Verify server-side pagination, filtering, and ordering.

Default severity:
- `S1` for admin, commerce, analytics, CRM, or user-data-heavy flows.
- `S2` for small public lists.

Fix prompt:

```text
Move pagination/filtering/sorting for [list] to the server. Add page size limits, stable ordering, empty states, and regression coverage for large datasets.
```

### 6. Hallucinated API, Method, Import, Field, or Integration

Trigger signals:
- Generated code references missing functions, fake SDK methods, wrong package names, nonexistent env vars, or mismatched API fields.
- Docs claim integration exists but source or runtime cannot prove it.
- Build passes only because the path is not executed.

Evidence requirements:
- Source/execution: missing import, failing build, failing test, route not implemented, dependency mismatch.
- Live/browser: flow dead-ends, integration button has no backend, console shows undefined call.

Check:
- Run tests/build when available.
- Cross-check referenced methods, endpoints, env vars, and fields against actual project definitions.

Default severity:
- `S0` when a launch-critical flow depends on the hallucinated piece.
- `S1` when a major feature claim is false.
- `S2` for non-critical broken helpers.

Fix prompt:

```text
Replace hallucinated [method/API/field/package] with a real implementation available in this project. Verify imports, dependency versions, environment variables, and add a test that executes the affected path.
```

### 7. Hardcoded Secret or Sensitive Data Exposure

Trigger signals:
- API key, password, token, connection string, webhook secret, or private identifier appears in source, frontend bundle, logs, console, HAR, screenshots, or docs.
- Cookies or tokens are stored in localStorage without a clear reason.

Evidence requirements:
- Source: committed secret pattern, env misuse, frontend-exposed credential.
- Live/browser: sensitive data visible in client storage, network payload, console, screenshot, or downloadable artifact.

Check:
- Search source and generated artifacts for secret-like values.
- Inspect storage, cookies, headers, HAR, and logs only within allowed permission boundaries.

Default severity:
- `S0` for production credential or private data exposure.
- `S1` for risky token storage or overly broad client exposure.

Fix prompt:

```text
Remove exposed secret or sensitive data from [location]. Rotate the credential if real, move configuration to server-side environment variables, redact logs/artifacts, and add a regression check that prevents secrets from appearing in source, bundles, storage, or reports.
```

## Product-Surface Failure Modes

### Placeholder Completion

Trigger signals:
- `TODO`, `FIXME`, placeholder copy, fake testimonials, dummy pricing, demo-only data, disabled CTA, mock backend, or "coming soon" hidden in core path.

Default severity:
- `S0` if it blocks promised launch functionality.
- `S1` if it misrepresents production readiness.

### Environment Dependency Drift

Trigger signals:
- Feature depends on missing env var, disabled integration, local-only service, wrong build command, missing database migration, or undocumented third-party account.

Default severity:
- `S0` for launch-critical backend/API/auth/payment/storage/email dependencies.
- `S1` for important but recoverable external services.

### Extreme UI State Breakage

Trigger signals:
- Empty, loading, error, long text, mobile, keyboard, slow network, unauthenticated, expired session, or no-results state is missing or broken.

Default severity:
- `S1` for core conversion or workflow failure.
- `S2` for visible UX quality risk.

## Audit Checklist

Use this compact checklist during `/audit`, `/flow-test`, and `/accept-five`:

- [ ] Inputs validate meaning, not only presence.
- [ ] Mutations are idempotent or protected where needed.
- [ ] Lists use bounded server-side loading when data can grow.
- [ ] Error states are visible, recoverable, and tested.
- [ ] No hallucinated methods, imports, fields, routes, env vars, or dependencies.
- [ ] No hardcoded secrets or sensitive data in source, client storage, logs, or artifacts.
- [ ] Core flows do not rely on placeholders, mock data, or disabled CTAs.
- [ ] Deployment dependencies are explicit and testable.
- [ ] Empty/loading/error/mobile/auth states are covered for launch-critical paths.

## Reporting Rule

When a failure mode is found, report it as:

```text
Failure Mode:
Severity:
Scope:
Evidence Type:
Evidence:
Reproduction:
Fix Suggestion:
Regression Check:
Lesson Candidate:
```

If the issue is only suspected, label it as `Assumption` and define the evidence needed to confirm it.
