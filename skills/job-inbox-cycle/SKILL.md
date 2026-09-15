---
name: job-inbox-cycle
description: Weekday job-inbox routine: fetch public sources, parse and score new JDs, draft materials for strong or mixed matches, write queue.md, and post a digest. Never emails, never submits ATS forms, never logs into LinkedIn or Greenhouse. Use on a schedule or when the operator asks to pull the inbox.
---

# Job inbox cycle

## When to use

Scheduled weekday routine, or "pull new jobs" / "run the inbox". Orchestrates `job-sources`, `parse-jd`, `match-score`, `tailor-resume`, `draft-outreach`, and `application-tracker`.

## Approval bar

- **Never** send email, LinkedIn messages, or POST an apply form in this skill — even if a mailbox or ATS session exists.
- **Never** log into LinkedIn, Greenhouse, Lever, or any `login` source. Skip and list as paste-needed.
- Do not invent titles, dates, employers, degrees, or metrics.
- Do not reuse a stale JD when the source is missing or returns an error; report the failure.
- Cap **5 new preps** (tailor + outreach) per run. Remaining new URLs go to the skip list as `over-cap`.
- Master resume, sources, queue, and tracker stay on this computer (`/workspace/job-desk/`). Not for templates.

## Sequence

1. Read `/workspace/job-desk/sources.md` via `job-sources`. If there is no `public` or `rss` row, stop and say the routine is not ready.
2. Read `/workspace/job-desk/tracker.md` and `/workspace/job-desk/queue.md` (create empty queue via the format below if missing).
3. Fetch each `public` and `rss` source. Follow posting links on listing pages. Skip `login` rows without fetching behind the wall.
4. Dedupe by canonical URL, then by company+role against the tracker and existing queue. Ignore already-seen postings.
5. For each new posting, up to the cap: run `parse-jd`. If the page is a login wall or not a JD, skip (do not invent text).
6. Run `match-score` against `/workspace/job-desk/master-resume.md` (or the fixture resume in harness/fixture-only mode).
   - **weak** → skip list only (no tailor, no outreach).
   - **strong** or **mixed** → `tailor-resume` + `draft-outreach`. Assign the next `q-NNN` ID. Tracker status `drafted`. Proposed channel: `ats-form` if a public apply URL exists, `email` if the posting gives a mailto they already control, else `draft-only`.
7. Write `/workspace/job-desk/queue.md`. Copy a digest into chat and into the evidence pack when running the harness.
8. Stop. Do not call `execute-approved-applications`.

## Queue file format

Default path: `/workspace/job-desk/queue.md`

```markdown
# Job inbox queue

Last cycle: [date]
Cap: 5 new preps

## Ready for approval

| ID | Company | Role | Score | Channel | Apply URL | Artifacts | Status |
|----|---------|------|-------|---------|-----------|-----------|--------|
| q-001 | | | strong or mixed | ats-form or email or draft-only | | | drafted |

## Skipped this cycle

| Company | Role | Source | Why |
|---------|------|--------|-----|
| | | | weak or login wall or over-cap or not a JD or fetch failed |

Reply `approve: q-001 q-002` (named IDs only) to run execute-approved-applications.
There is no approve-all.
```

IDs are `q-` plus three digits, monotonic, never reused in this file.

## Digest format (chat)

```markdown
# Job inbox digest

[date] — [N] ready, [M] skipped. Not sent. Not submitted.

## Ready
- q-001 — [Company] [Role] — [strong|mixed] — [channel] — approve this ID to send/submit

## Skipped
- [reason]: [source or company]

To execute, reply with named IDs only, e.g. `approve: q-001`.
```

## Failure

If every source fails or is a wall, post that and leave queue otherwise unchanged. If there is no master resume, run `first-run-job-desk` instead of guessing a career.
