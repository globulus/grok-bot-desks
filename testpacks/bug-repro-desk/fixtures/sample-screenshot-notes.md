# Sample screenshot notes (fixture)

Substitute for an actual PNG so the template never ships a photo of a real device or person.

**Visible:** iPhone status bar, Flutter demo home, large `0` centered, tooltip "Increment" over a circular + button, debug banner.

**Not visible:** Account, network errors, crash dialog.

**Inferred (labeled):** iOS, debug build.

**Hypotheses:**

1. `setState` after an async gap without `mounted` check — confirm by reading `lib/main.dart` in a sample counter app.
2. Hit-test miss on the FAB — confirm with a second tap and widget inspector.
3. Reporter looked at a stale screenshot — confirm by reproducing on staging/simulator.

Do not claim reproduced until a real run happens.
