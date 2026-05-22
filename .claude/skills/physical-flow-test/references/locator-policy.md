# Locator Policy

Stable locators make physical tests useful as regression checks instead of brittle recordings.

## Locator Priority

Prefer locators in this order:

1. `get_by_role`
2. `get_by_label`
3. `get_by_placeholder`
4. `get_by_test_id`
5. Visible text
6. Stable CSS selector
7. XPath only as a last resort

## Examples

```python
page.get_by_role("link", name="Get Started").click()
page.get_by_label("Email").fill("person@example.com")
page.get_by_placeholder("Search").fill("invoice")
page.get_by_test_id("upload-dropzone").set_input_files("sample.csv")
```

## Rules

- Prefer user-facing accessibility locators because they test the interface the user experiences.
- Add a fallback note when the locator may be unstable.
- Do not rely on generated class names, animation wrappers, or deep DOM shape.
- Use `data-testid` for controls without stable accessible names, especially dashboards and repeated rows.
- Avoid fixed sleeps. Use assertions, URL waits, network waits, or visible state waits.
- Every action should have a checkpoint assertion immediately after it.

## Locator Finding Format

When a generated test requires a brittle selector, report it as a lesson:

```text
Finding: Login submit button lacks a stable accessible name.
Impact: Physical regression test must use brittle text/CSS selector.
Fix Suggestion: Add role-compatible button text or aria-label="Sign in".
Regression Check: Replace CSS selector with get_by_role("button", name="Sign in").
```
