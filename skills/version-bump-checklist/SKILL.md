---
name: version-bump-checklist
description: Checklist for a Flutter app version bump (pubspec, iOS, Android) before store submit. Use when cutting a release. Never submits the build.
---

# Version bump checklist

## When to use

Cutting a Flutter release version bump (pubspec / iOS / Android) before store submit. Never for submitting the build.

## Approval bar

- Do not edit version files until the operator says yes.
- Never submit the build to App Store Connect or Play Console.

## Sequence

1. Current `pubspec.yaml` version vs last git tag.
2. Proposed `x.y.z+build` (ask if unclear).
3. Confirm iOS/Android take version from Flutter unless the project overrides.
4. List files that would change; do not edit until yes.
5. Hygiene: point at `mobile-release-hygiene` before submit.

## Output

Proposed version, files, commands (`fvm flutter build ipa` / `appbundle` as informational), **submit = human**.
