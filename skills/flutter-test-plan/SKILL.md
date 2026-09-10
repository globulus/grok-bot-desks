---
name: flutter-test-plan
description: Writes an FVM-first Flutter test plan (unit, widget, golden, integration) with commands the installer can run. Use when asked for Flutter tests, coverage, or a test plan. Never runs destructive git or publishes artifacts without an explicit yes.
---

# Flutter test plan

## When to use

Someone wants tests for a Flutter change, a failing test map, or a plan before writing tests.

## Approval bar

- Prefix `flutter` and `dart` with `fvm` when `.fvm/` or `.fvmrc` exists.
- Do not add goldens to a repo that does not already use them unless asked.
- Do not commit, push, or change CI config without an explicit yes.
- Do not record integration tests against production.

## Sequence

1. Detect toolchain: `fvm flutter --version` or report that FVM is missing.
2. Classify the change: pure Dart, widget, platform channel, navigation, network.
3. Pick the cheapest layer that would catch the bug:
   - Unit: logic, parsing, cubit/bloc
   - Widget: UI state, semantics, callbacks
   - Golden: only if the project already has golden tests
   - Integration/`integration_test`: multi-screen or platform plugin paths
4. Name tests after behavior, not implementation.
5. List exact commands, one per line.

## Commands

```text
fvm dart analyze
fvm flutter test
fvm flutter test test/path/to_test.dart
fvm flutter test --update-goldens   # only when goldens already exist and the user asked
```

If the project has no FVM files, use `flutter`/`dart` and state that in the plan.

## Output format

```markdown
# Test plan

Toolchain: fvm | system flutter (reason)
Change under test: [one sentence]

## Tests to add
| Layer | File | Test name | Asserts |
| unit | | | |
| widget | | | |

## Commands
```

## Commands the installer can run

(plain fenced list)

## Out of scope
Goldens / integration / production data
```

## Failure

If you cannot see the source, ask for the file or a paste. Do not invent APIs that are not in the tree.
