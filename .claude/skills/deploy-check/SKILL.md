---
name: deploy-check
description: Check whether a website, web app, or AI-built product is actually production-ready: domain, SSL, env vars, backend/API, database, auth, email/SMS, storage, payment, CMS, analytics, monitoring, SEO, privacy, backup, and rollback.
---

# Deploy Check

Use this skill to expose what is missing before a site or app can be called production-ready.

## Do

1. Identify the product's runtime dependencies.
2. Separate visible proof from source claims.
3. Inventory deployment-relevant public surfaces: forms, auth, uploads, payment, documents, third-party scripts, APIs, storage, analytics, and security headers.
4. Apply the permission model before testing production dependencies or authenticated paths.
5. Check every deployment readiness row.
6. Mark unknown dependencies as `UNKNOWN`, not pass.
7. Flag fake-complete demos where UI exists but backend, persistence, auth, or email is unproven.
8. Produce a deployment readiness table and blocker list.
9. Use `S0-S4` severity; production blockers are usually `S0` or `S1`.
10. Emit progress updates after major dependency groups when the check spans more than a few items.

## Reference

Read `references/deployment-readiness.md`.
For broad production reviews, also read `../audit/references/web-surface-discovery.md`, `../audit/references/permission-model.md`, and `../audit/references/progressive-reporting.md`.

## Output

- Deployment readiness table.
- Production blockers.
- Unknown dependency list.
- S0-S4 severity.
- Copyable setup/fix prompts.
- Regression checks.
- Lessons.
- Final readiness verdict.
