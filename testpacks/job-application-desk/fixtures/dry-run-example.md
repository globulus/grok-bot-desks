# JD parse

Source: fixtures/sample-jd.md as of 2026-09-10
Role title: Senior Flutter Engineer
Company: ExampleCorp

## Must-haves
- 4+ years shipping iOS or Android apps
- Production Flutter on iOS and Android
- Automated tests (unit and widget)
- Platform channels or native plugins
- PR review and FVM coaching

## Nice-to-haves
- Shorebird / code-push
- Store listing experience
- GraphQL

## Keywords
Flutter, Dart, FVM, widget tests, method channels, iOS, Android, code review

## Signals
Remote US, full-time, no salary/visa in posting

## Unknowns
Team size, interview loop, sponsorship

# Match score

Role: Senior Flutter Engineer — ExampleCorp
Resume source: fixtures/sample-resume.md

## Must-haves
| Requirement | Verdict | Evidence |
| 4+ years mobile | FOR | Android 2018–2021 + Flutter 2021–present |
| Production Flutter iOS and Android | FOR | "Shipped a Flutter iOS/Android app" at Northwind Labs |
| Unit and widget tests | FOR | "Wrote widget tests and a small integration_test path" |
| Platform channels / plugins | FOR | "method channels for a barcode scanner plugin" |
| PR review / FVM coaching | FOR | "documented the FVM workflow for the team" (coach); PR review not explicit → weak FOR |

## Overall
strong
Screen-fail risk: posting asks to "review PRs"; resume documents FVM coaching more clearly than reviews.

## Gaps to be honest about
- Shorebird, GraphQL, store listing: not on resume — omit from claims
- No user-count metrics on resume (correctly absent)

## Questions to ask them
- App size and release cadence
- How FVM is enforced in CI

## What I did not do
Invent experience, submit, email

# Tailored resume (draft)

Target role: Senior Flutter Engineer — ExampleCorp
Source: fixtures/sample-resume.md

## Resume

Alex Rivera — Senior mobile engineer, Austin TX (remote). Fixture email only.

Northwind Labs (2021–present) — Mobile Engineer
- Shipped production Flutter iOS and Android inventory-count app for internal staff.
- Wrote widget tests and an integration_test path for the count flow.
- Documented the team FVM workflow and owned CocoaPods upgrades when plugins lagged.
- Used method channels for a barcode scanner plugin.

Contoso Retail (2018–2021) — Android Engineer
- Maintained Kotlin/Java store companion app and camera permission rationale copy.

Education: B.S. Computer Science, State University (2018)
Skills: Flutter, Dart, FVM, widget tests, method channels, iOS/Android release hygiene

## Change log
| Original | New | Why | Source |
| Shipped a Flutter iOS/Android app used by internal staff for inventory counts | Shipped production Flutter iOS and Android inventory-count app for internal staff | JD: Production Flutter iOS and Android | Northwind bullet 1 |
| Owned CocoaPods upgrades… documented the FVM workflow | Documented the team FVM workflow and owned CocoaPods upgrades… | JD: FVM workflows | Northwind bullet 3 |

## Refused to add
Shorebird, GraphQL, store listing, any metric not on the master resume

# Outreach draft

Channel: email
To: hiring manager / jobs inbox they control
Do not send.

## Draft

I am applying for Senior Flutter Engineer. I have shipped production Flutter on iOS and Android (inventory-count app at Northwind Labs), with widget tests, an integration_test path, method channels for a scanner plugin, and an FVM-based plugin upgrade workflow. I have not used Shorebird or GraphQL; happy to discuss how you handle those. I can send a tailored resume — I will not submit through an ATS until you want that.

## Why these claims are allowed
- Production Flutter iOS/Android → Northwind bullet
- Tests → Northwind tests bullet
- Channels → scanner plugin bullet
- FVM → documented workflow bullet

## Not in this draft
Send action, invented awards

# Tracker (private in real use; fixture row only)

| Company | Role | Source | Date | Status | Next action | Notes |
| ExampleCorp | Senior Flutter Engineer | fixtures/sample-jd.md | 2026-09-10 | researching | operator sends if they want | fixture |
