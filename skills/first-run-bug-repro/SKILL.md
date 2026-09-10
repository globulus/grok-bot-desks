---
name: first-run-bug-repro
description: Walks first-run setup for Bug Repro Desk (GitHub/Linear, staging URL, test-account handoff). Use on the first chat after install. Never stores passwords in chat or in a public template.
---

# First-run: Bug Repro Desk

## When to use

First message after install, or the user says "set up".

## Approval bar

- Staging URL required before any computer-use against a product.
- Test credentials via secure handoff only.
- No production URL as the default target.
- Do not write secrets into skills, memory that might be shared, or this plugin's repo.

## Sequence

1. State the job: ticket or screenshot → repro pack; staging + fresh test account; never production customer data; never post back without yes.
2. Ask for tracker: GitHub, Linear, paste-only.
3. Ask for staging base URL. If they only have production, refuse automated login and offer paste-of-steps mode.
4. Ask how test accounts work (shared staging user vs you create). For passwords: "use the secure secret request / take over the computer — do not paste the password here."
5. Confirm skills: `repro-from-ticket`, `repro-from-screenshot`, `write-repro-pack`.
6. Offer a dry run against `fixtures/sample-flutter-issue.md` in this plugin (no live login).
7. Remind them: Bot description holds standing rules; their staging URL is local memory, strip it before Share as template.

## Output

Checklist: tracker, staging, credential method, dry-run result, next command ("repro issue #…").

## Failure

If they cannot name staging, stay in paste/screenshot mode and do not drive a browser to production.
