# Repro pack

**Title:** Counter text stays at 0 after one tap on iOS simulator
**Ticket:** fixtures/sample-flutter-issue.md

## Environment
unknown / iOS Simulator 18 claimed by reporter / staging-not-connected

## Account
none (fixture)

## Preconditions
Debug Flutter counter sample running on simulator. No production data.

## Steps
1. Launch the counter sample on iOS simulator.
2. Confirm the displayed number is 0.
3. Tap the + FAB once.
4. Read the displayed number.

## Expected
Number is 1.

## Actual
Reporter: number still 0 on first tap (unverified here).

## Evidence
fixtures/sample-screenshot-notes.md (text substitute, no PNG)

## Frequency
intermittent (reporter: "sometimes")

## Minimal test case
not isolated — no app binary in this dry run

## Not tried
Live simulator, production, GitHub comment
