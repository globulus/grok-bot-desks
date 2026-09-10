---
name: mobile-release-hygiene
description: Checks Flutter iOS/Android release hygiene (versions, permissions, Podfile.lock vs Gradle, store-facing risk). Use before a store build or release. Never submits to App Store Connect or Play Console and never handles signing secrets.
---

# Mobile release hygiene

## When to use

A Flutter app is about to ship, bump a version, or someone asks whether iOS/Android release config looks safe.

## Approval bar

- Do not submit builds, notarize, or upload to stores.
- Do not read or copy signing keys, `google-services.json` contents, or provisioning profiles into chat.
- Do not run `pod install` or Gradle writes on the installer's machine unless they explicitly ask.
- Flag store-facing risk; do not "fix" privacy nutrition labels here (see wave-2 privacy desk).

## Sequence

1. Read `pubspec.yaml` version (`x.y.z+build`).
2. iOS: `ios/Podfile.lock` vs `pubspec.lock`, `Info.plist` usage strings, `CFBundleShortVersionString` / `CFBundleVersion` if not derived, ATS exceptions, background modes.
3. Android: `minSdk`/`targetSdk`, `AndroidManifest` permissions, `applicationId`, versionName/versionCode source of truth.
4. Permissions: every plist/manifest permission should have a user-facing reason somewhere; flag extras.
5. Lockfiles: note if Podfile.lock or Gradle hashes look stale relative to pubspec (do not regenerate unless asked).
6. Store risk: new tracking SDKs, camera/mic/photo, local network, background location.

## Output format

```markdown
# Release hygiene

App version: [from pubspec]
Platforms checked: iOS / Android / both

## Blockers
- Item, file, why it can fail store review or the build

## Should fix before ship
-

## Informational
- Lockfile freshness, permission inventory

## Not done
- Store submit, signing, privacy nutrition (needs you)
```

## Failure

If `ios/` or `android/` is missing, say which platform you could not check. If this is a package rather than an app, stop after pubspec/version notes.
