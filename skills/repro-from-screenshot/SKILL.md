---
name: repro-from-screenshot
description: Turns a screenshot or screen recording into a hypothesized repro path (surface, control, data). Use when the bug is an image or clip with little text. Never uses production customer data.
---

# Repro from screenshot

## When to use

The primary artifact is an image, screen recording, or annotated screenshot. Pair with `repro-from-ticket` if a ticket also exists.

## Approval bar

Same as ticket repro: staging/test accounts only, no production data, no posting without yes, no secrets in chat.

## Sequence

1. Describe only what is visible: UI chrome, copy, error text, OS indicators, redactions.
2. Infer surface (iOS/Android/web) from chrome; label inferences as inferences.
3. Hypothesize 1–3 shortest paths that could produce that frame.
4. List what the screenshot does **not** show (account type, locale, network, build).
5. Propose the next staging action or ask for a ticket/steps if the image is insufficient.
6. Pass evidence into `write-repro-pack`; do not claim reproduction until you actually reproduced.

## Output format

```markdown
# Screenshot read

Visible: [factual]
Inferred: [labeled]
Not visible: [list]

## Hypotheses
1. Path — why — how to confirm on staging

## Next
Attempt plan or ask
```

## Failure

If the image is unreadable or is not a product UI, say so and stop. Do not guess personal data from a photo of a person.
