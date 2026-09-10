---
name: flutter-pr-review
description: Reviews a Flutter/Dart pull request or pasted diff for widget lifecycle, state, platform channels, tests, and analysis nits. Use when reviewing a Flutter PR, Dart diff, or mobile UI change. Never opens a PR or pushes without an explicit yes.
---

# Flutter PR review

## When to use

A Flutter/Dart PR, branch, or pasted diff is the input. Output a merge-ready review, not a rewrite of the whole change.

## Approval bar

- Do not `git push`, open a PR, merge, or force-push.
- Do not run `pod install`, Gradle writes, or signing commands.
- Do not request secrets, keystores, or CI tokens.
- Stop and ask before any write to a remote.

## Inputs

Need one of: repo + PR number, branch, or a pasted diff. If the repo uses FVM, prefix Flutter/Dart commands with `fvm`. If FVM is missing, say so and use PATH `flutter`/`dart` only after stating that.

## Sequence

1. Identify the change set (files, tests, platform folders).
2. Review in this order:
   - Correctness: null-safety, async gaps, dispose/cancel, `mounted` after await
   - Widgets: rebuild cost, keys, `const`, InheritedWidget/`Provider` misuse
   - State: Cubit/Bloc/Riverpod leaks, event storms, context after unmount
   - Platform: method channels, permission strings, iOS vs Android parity
   - Tests: missing widget/unit coverage for new branches; goldens only if the repo already uses them
   - Analysis: `analysis_options.yaml` violations the change introduces
3. Prefer evidence: file + line, failing mental path, or a command the installer can run.
4. Skip style nits that the linter already owns unless they hide a bug.

## Output format

```markdown
# Flutter PR review

Scope: [PR/branch/diff]
Commands used: [e.g. fvm dart analyze, fvm flutter test]

## Blockers
- [file:line] What is wrong, why it breaks, how to verify

## Should fix
- [file:line] Issue and a concrete fix

## Nits
- Optional, only if they aid review

## Test gaps
- Scenario not covered, suggested test name

## Verdict
Approve / request changes / needs more context
What more context: [blank if none]
```

## Failure

If there is no Dart/Flutter code in the change, say so and stop. If the PR is too large, review the riskiest files first and list what you skipped.
