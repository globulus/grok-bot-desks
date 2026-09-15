# Sample ticket (fixture)

Use this with Bug Repro Desk and as a stand-in "change" for Flutter Mobile Engineer. Not a real product. No production data.

**Title:** Counter text does not update after tapping + on iOS simulator

**App:** Flutter counter sample (local)

**Environment:** iOS Simulator 18, Flutter stable, debug

**Expected:** Tapping the + FAB increments the number on screen by 1.

**Actual:** First tap sometimes does nothing. Log shows `setState` skipped because `!mounted` is false... wait, reporter is unsure. Screenshot: the FAB is visible, the number still reads `0`.

**Steps:**

1. Open the app on iOS simulator.
2. Wait for the home screen with `0`.
3. Tap + once.
4. Observe the number.

**Account:** none (no login)

**Staging:** not connected — fixture only

**Notes:** Do not file this against flutter/flutter. Do not use real user data.
