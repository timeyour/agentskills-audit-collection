# Five-Pass Acceptance

Use this reference when an audit, implementation, website, open-source app, or workflow needs repeated acceptance testing instead of a single review.

## Goal

Run five focused passes so the agent sees different classes of failure and turns repeated findings into durable experience.

The passes are:

1. Baseline.
2. Functional.
3. Edge and failure.
4. Visual and deployment.
5. Retest and learn.

## Pass 1: Baseline

Purpose: understand what exists.

Check:

- URL loads.
- Product category is identified.
- Primary user scenario is clear.
- Main pages/routes are listed.
- Main features are inventoried.
- Happy path is mapped.
- Source evidence and live evidence are separated.

Output:

- feature inventory;
- page/route map;
- first risk list;
- unknowns.

## Pass 2: Functional

Purpose: execute safe workflows.

Check:

- navigation;
- CTA buttons;
- forms;
- search/filter/sort;
- upload/download/copy/export/share;
- signup/login where safe;
- dashboard/admin if accessible;
- persistence after refresh;
- confirmation/error messages.

Output:

- expected vs actual table;
- pass/partial/fail/unknown status;
- live positions and locators;
- issue cards for broken flows.

## Pass 3: Edge And Failure

Purpose: find what happy-path testing misses.

Check:

- empty fields;
- invalid email/phone/password;
- duplicate submit;
- slow/loading state if observable;
- offline/network failure if safe;
- auth-required routes without login;
- back/refresh behavior;
- mobile viewport;
- long text and small screen overflow.

Output:

- edge-case findings;
- missing state findings;
- validation and error-state issues;
- mobile-specific issues.

## Pass 4: Visual And Deployment

Purpose: inspect craft and production readiness.

Check visual:

- first viewport;
- hierarchy;
- spacing;
- typography;
- color;
- imagery;
- component consistency;
- responsive layout;
- accessibility basics;
- AI slop signals.

Check deployment:

- domain and SSL;
- env vars;
- backend/API;
- database;
- auth/session;
- email/SMS;
- storage;
- payment;
- CMS/admin;
- analytics;
- monitoring;
- SEO/sitemap/robots;
- privacy/terms;
- backup/export/rollback.

Output:

- visual score;
- deployment readiness table;
- craft issue cards;
- production blocker list.

## Pass 5: Retest And Learn

Purpose: verify and accumulate experience.

Check:

- Are previous blockers still present?
- Did fixes create regressions?
- Which issue types repeated?
- Which prompts produced good fixes?
- Which prompts were too vague?
- Which checks should become rules?
- Which examples should become benchmarks?

Output:

- final verdict;
- recurring pattern list;
- false positive list;
- improved copy prompts;
- guardrail updates;
- benchmark examples.

## Experience Ledger Format

```markdown
## Experience Ledger

### Repeated Failure Patterns

- Pattern:
- Seen in:
- Why it matters:
- New guardrail:

### Good Fix Prompts

- Prompt:
- Worked because:
- Reuse when:

### Bad Fix Prompts

- Prompt:
- Failed because:
- Replace with:

### Benchmarks

- Example:
- Good pattern:
- Use as comparison for:

### Rule Updates

- Target file:
- Proposed change:
- Reason:
```

## Acceptance Verdict

- `PASS`: all critical workflows and deployment requirements pass.
- `PASS WITH NOTES`: product is usable, but non-critical gaps remain.
- `FAIL`: critical workflow, visual trust, security, or deployment blocker remains.
- `INCOMPLETE`: fewer than five passes were completed.

## Anti-Patterns

- Repeating the same happy-path test five times.
- Treating pass five as a summary only.
- Collecting findings without updating rules or prompts.
- Fixing visual polish before core workflows work.
- Ignoring repeated failures because each one looks small.
