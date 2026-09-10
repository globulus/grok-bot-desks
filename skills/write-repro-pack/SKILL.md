---
name: write-repro-pack
description: Writes a complete bug reproduction pack (steps, expected vs actual, environment, screenshots, minimal test case). Use after a repro attempt or when asked for a repro pack. Never posts the pack to a tracker without an explicit yes.
---

# Write repro pack

## When to use

You have attempted a repro (or the user supplied complete steps) and need a handoff artifact for engineering.

## Approval bar

- Do not include production customer PII, tokens, or raw log dumps with secrets.
- Do not open tracker comments or Slack posts without an explicit yes.
- Prefer `/workspace` screenshot paths over embedding binaries in chat.

## Required sections

Every pack must include all of these. If unknown, write `unknown` — do not invent.

1. Title (one line)
2. Environment: OS, device/simulator, app/build version, staging vs local
3. Account: fresh test / seeded fixture (never a real customer)
4. Preconditions
5. Exact steps (numbered, one action each)
6. Expected
7. Actual
8. Evidence: screenshot/log paths
9. Frequency: always / intermittent / once
10. Minimal test case: widget test, integration step, or "not isolated"
11. Non-goals: what you did not try

## Output format

```markdown
# Repro pack

**Title:**
**Ticket:** (if any)

## Environment
## Account
## Preconditions
## Steps
1.
## Expected
## Actual
## Evidence
## Frequency
## Minimal test case
## Not tried
```

## Quality bar

A stranger should reproduce without asking you a question. If they would need a secret or production row, the pack is invalid — strip it and list the blocker.
