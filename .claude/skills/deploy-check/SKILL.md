---
name: deploy-check
description: Check whether a website, web app, or AI-built product is actually production-ready: domain, SSL, env vars, backend/API, database, auth, email/SMS, storage, payment, CMS, analytics, monitoring, SEO, privacy, backup, and rollback.
---

# Deploy Check

Use this skill to expose what is missing before a site or app can be called production-ready.

## Do

1. Identify the product's runtime dependencies.
2. Separate visible proof from source claims.
3. Check every deployment readiness row.
4. Mark unknown dependencies as `UNKNOWN`, not pass.
5. Flag fake-complete demos where UI exists but backend, persistence, auth, or email is unproven.
6. Produce a deployment readiness table and blocker list.
7. Use `S0-S4` severity; production blockers are usually `S0` or `S1`.

## Reference

Read `references/deployment-readiness.md`.

## Output

- Deployment readiness table.
- Production blockers.
- Unknown dependency list.
- S0-S4 severity.
- Copyable setup/fix prompts.
- Regression checks.
- Lessons.
- Final readiness verdict.
