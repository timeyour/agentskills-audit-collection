# Public Reports

This directory is the public-facing report surface for AgentSkills Audit Collection.

The skills are the internal audit engine. Public reports are what a website owner, client, or teammate should actually see:

```text
problem -> evidence -> impact -> fix suggestion -> regression check
```

## Files

- `demo-site-audit.md`: Markdown version of a shareable audit report.
- `demo-site-audit.html`: Static HTML version that can be opened directly in a browser.
- `screenshots/`: Place report screenshots or redacted physical-test artifacts here.

## Report Rule

Public reports should avoid internal agent jargon. They should preserve:

- target URL
- audit date
- overall risk
- S0-S4 severity
- evidence type
- fix suggestion
- regression check
- lessons

Use `validation/public-website-audit-report-template.md` as the source template.
