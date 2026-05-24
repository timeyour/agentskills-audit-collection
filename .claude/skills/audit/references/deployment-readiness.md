# Deployment Readiness

Use this reference when auditing whether a website or app is production-ready.

## Checklist

| Requirement | What To Check |
| --- | --- |
| Domain + SSL | Canonical domain, redirects, HTTPS, www/non-www behavior. |
| Environment variables | Required keys, safe defaults, missing `.env` docs, secrets exposure risk. |
| Backend/API | Routes exist, errors are handled, auth is enforced, rate limits when relevant. |
| Database | Persistence, schema, migrations, backup/export, seed/demo data separation. |
| Auth/session | Login, logout, protected routes, expired sessions, roles/admin boundaries. |
| Email/SMS | Provider configured, sender domain, delivery, error handling, spam risk. |
| Storage | Upload, download, file type/size limits, permissions, cleanup. |
| Payment | Checkout, webhooks, tax, refunds, test/live mode separation. |
| CMS/admin | Content model, editor roles, preview, publish, rollback. |
| Analytics | Product events, conversion events, privacy. |
| Error monitoring | Client/server errors, alerts, source maps. |
| SEO | Title/meta, Open Graph, sitemap, robots, canonical, crawlability. |
| Performance | First load, image weight, script weight, caching. |
| Legal/compliance | Privacy, terms, cookies, consent, data deletion/export where relevant. |
| Rollback | How to undo a bad release or bad content publish. |

## Output Row

```markdown
| Requirement | Status | Evidence | Missing/Risk | Fix |
| --- | --- | --- | --- | --- |
```

Status:

- `READY`
- `PARTIAL`
- `MISSING`
- `UNKNOWN`
- `NOT APPLICABLE`

## Common Deployment Gaps

- Form exists but no backend or confirmation state.
- Auth button exists but protected routes are untested.
- Blog/articles are hard-coded and need CMS.
- Email provider mentioned but env vars are not documented.
- Database is claimed but persistence is not tested.
- Product flow is auth-gated and no demo path exists.
- Site looks complete but no analytics/error monitoring is visible.
