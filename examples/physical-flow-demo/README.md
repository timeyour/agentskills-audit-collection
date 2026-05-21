# Physical Flow Demo

This is a tiny dependency-free web app for exercising `/physical-flow-test`.

It includes:

- Homepage CTA.
- Fake login.
- Dashboard auth guard.
- Form submission.
- Success page.
- Failure states.
- A destructive action route that physical tests should mark `SKIPPED-SAFE` unless explicitly allowed.

## Run

```bash
cd examples/physical-flow-demo
python app.py
```

Open:

```text
http://localhost:5000
```

Test credentials:

```text
username: test_user
password: test_pass
```

## Suggested Physical Flow

```text
Homepage -> Get Started -> Login -> Dashboard -> Add Task -> Success -> Dashboard
```

Failure checks:

- Login with wrong credentials.
- Add a task containing the word `fail`.
- Visit `/dashboard` before signing in.
