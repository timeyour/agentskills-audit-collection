# Safe Execution Policy

Physical tests can expose or mutate real user data. Apply this policy before generating or executing browser tests.

## Default Safe-Skip Actions

Mark these actions as `SKIPPED-SAFE` unless the user explicitly authorizes them and provides a safe test environment:

- Real payment, purchase, renewal, refund, or billing changes.
- Deletion, account closure, irreversible archive, or data purge.
- Production email, SMS, push notification, webhook, or social post sending.
- Uploading sensitive files to third-party storage.
- Changing passwords, API keys, roles, permissions, or MFA settings.
- Submitting legal, medical, financial, government, or identity forms.

## Credential Rules

- Never hardcode passwords, cookies, tokens, session IDs, or API keys.
- Use `.env.example` with placeholder names such as `TEST_USERNAME`.
- Require real `.env` files to stay local and out of git.
- Prefer test accounts with limited permissions.
- For production checks, use read-only accounts whenever possible.

## Artifact Redaction

Before sharing artifacts, redact:

- Cookies and `Set-Cookie` headers.
- `Authorization`, `Proxy-Authorization`, and bearer tokens.
- API keys, session IDs, CSRF tokens, OAuth codes, and signed URLs.
- Emails, phone numbers, addresses, account IDs, payment data, and order IDs.
- Private dashboard content visible in screenshots or videos.

## HAR Redaction Pattern

Generated packages may include a HAR redaction helper. It must remove sensitive headers and obvious secrets before artifacts are shared.

```python
SENSITIVE_HEADERS = {
    "authorization",
    "proxy-authorization",
    "cookie",
    "set-cookie",
    "x-api-key",
    "x-csrf-token",
}


def redact_headers(headers):
    redacted = []
    for header in headers:
        name = header.get("name", "")
        if name.lower() in SENSITIVE_HEADERS:
            redacted.append({"name": name, "value": "[REDACTED]"})
        else:
            redacted.append(header)
    return redacted
```

## Retention

- Local artifacts: keep only as long as needed for review, usually 7 days.
- CI artifacts: set an explicit retention period, usually 7 to 30 days.
- Never commit raw physical-test artifacts to git.
- If artifacts contain sensitive data, prefer summarizing findings instead of uploading files.
