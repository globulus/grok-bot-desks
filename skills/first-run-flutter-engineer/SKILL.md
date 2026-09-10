---
name: first-run-flutter-engineer
description: Walks first-run setup for the Flutter Mobile Engineer desk (GitHub plugin, FVM, target repo). Use on the first chat after install or when the installer says they just added this bot. Never clones private repos or stores tokens in the shared template.
---

# First-run: Flutter Mobile Engineer

## When to use

First message after the Bot is added, or the user says "set up" / "first run".

## Approval bar

- Do not assume GitHub, FVM, or a repo exists.
- Do not paste PATs into chat. Use the plugin connect card or a secure handoff.
- Do not clone unless the user names a **public** repo or confirms a private remote they already connected.
- Remember setup facts on **their** computer only; they must not appear in a public share template.

## Sequence

1. State the job in one sentence: review Flutter PRs, write FVM-first test plans, flag release hygiene; never open a PR without them.
2. Ask for the target: public Git URL, already-connected GitHub repo, or a pasted diff for this session only.
3. Check FVM on the cloud computer (`fvm --version`). If missing, offer to install FVM **after yes**, then stop.
4. If they want GitHub: Settings → Plugins → GitHub (or `@` the GitHub connector). Wait; do not scrape credentials.
5. Confirm skills enabled: `flutter-pr-review`, `flutter-test-plan`, `mobile-release-hygiene`.
6. Run a tiny dry task on **their** tree or `fixtures/sample-flutter-issue.md` from this plugin if they have no repo yet.
7. Tell them standing rules live in the Bot description; tasks go in chat.

## Output

A short checklist of what is connected, what is still missing, and the next command they can give (e.g. "review PR #12").

## Failure

If the computer cannot install FVM, list the blocker and continue in paste-diff mode.
