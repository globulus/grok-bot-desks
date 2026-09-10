---
name: repro-from-ticket
description: Turns a bug ticket (GitHub, Linear, or paste) into a reproduction attempt plan using staging and a fresh test account. Use when given an issue URL or ticket body. Never uses production customer data and never posts back without an explicit yes.
---

# Repro from ticket

## When to use

The input is an issue URL or pasted ticket. Goal: enough to attempt a repro, then hand off to `write-repro-pack`.

## Approval bar

- Never production customer data, dumps, or live user accounts.
- Never create accounts on production.
- Never post comments to GitHub/Linear/Slack without an explicit yes.
- Test credentials only via secure handoff, never in chat.

## Sequence

1. Extract: summary, expected, actual, env (OS, app version, device), steps, attachments.
2. Mark missing fields; do not invent them.
3. Choose surface: web, Flutter iOS, Flutter Android, desktop. Prefer staging URLs the user named in first-run.
4. Write an attempt plan: account type (fresh test), data fixtures, first action, stop condition.
5. If you can run it on the cloud computer (browser or simulator), do so on **staging only**. Stop on CAPTCHA/login and ask for takeover.
6. Capture notes for `write-repro-pack` (what you tried, what happened, screenshots paths under `/workspace`).

## Output format

```markdown
# Repro attempt

Ticket: [url or id]
Environment allowed: staging / local / unknown (stop if unknown)

## Known
- Expected / actual / env / steps (quoted from ticket)

## Missing
- Fields not in the ticket

## Attempt plan
1.

## Result
Reproduced / cannot reproduce / blocked
Evidence: [screenshot or log path]
```

## Failure

If the ticket has no steps and no screenshot, ask for one of those before spending computer time. If only production is named, refuse and ask for staging.
