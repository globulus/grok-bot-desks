---
name: parse-jd
description: Parses a job description paste or public posting URL into must-haves, nice-to-haves, keywords, and company signals with citations. Use when starting a job application. Never applies or emails anyone.
---

# Parse job description

## When to use

The user pastes a JD or a public posting link. First step before `match-score`.

## Approval bar

- Do not log into LinkedIn, Greenhouse, Lever, or email.
- If the posting requires login, ask the user to paste the text.
- Cite quotes from the posting; do not invent requirements.

## Sequence

1. Capture source: URL and retrieval date, or "pasted".
2. Split requirements into must-have vs nice-to-have. If the posting does not distinguish, say so and treat listed qualifications as must-have only when they use "required"/"must".
3. Extract keywords (skills, tools, domains) for resume alignment — still no fabrication later.
4. Company/team signals: product, stage, location, visa, salary if present.
5. Red flags: unpaid, credential mill, "task before interview" unpaid work — flag, do not moralize at length.

## Output format

```markdown
# JD parse

Source: [url or paste] as of [date]
Role title:
Company:

## Must-haves
- Quote or close paraphrase + where it appeared

## Nice-to-haves
-

## Keywords
-

## Signals
Location / employment type / salary / visa / team

## Unknowns
What the posting does not say

## Raw quotes worth keeping
> …
```

## Failure

If the URL is behind a wall, stop and request a paste. If the text is not a job posting, say so.
