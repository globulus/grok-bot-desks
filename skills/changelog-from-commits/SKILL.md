---
name: changelog-from-commits
description: Turns git history since the last store version into a user-facing What's New draft. Use before an App Store or Play release. Never submits to a store.
---

# Changelog from commits

## When to use

App Store Ship Desk needs What's New copy from commits, PRs, or a version bump.

## Approval bar

- Do not tag, push, or submit store listings.
- Do not mention internal tickets, coworker names, or unreleased partner code.
- User-facing language only. Calendar meetings stay "meetings" if that copy appears.

## Sequence

1. Find last shipped version (git tag, pubspec, or user-stated).
2. Collect commits/PR titles since then.
3. Group: new, improved, fixed, other. Drop chore/deps unless user-visible.
4. Draft store-length What's New (App Store ~4000 chars, keep a 170-char short option).

## Output

```markdown
# What's New (draft)

Version:
Range:

## Short
## Full
## Dropped (internal)
```
