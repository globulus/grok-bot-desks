---
name: execute-approved-applications
description: Sends or submits only the job-inbox queue IDs the operator named (e.g. approve: q-003 q-004). Use after a digest, never on a schedule. Unknown IDs are refused. LinkedIn Easy Apply and login ATS stay draft-only. CAPTCHA and 2FA are takeovers.
---

# Execute approved applications

## When to use

The operator replies with named queue IDs after a `job-inbox-cycle` digest, or asks to run this skill with an explicit ID list. Not a routine. Not "approve all."

## Approval bar

- Parse IDs from the operator message (`approve: q-001 q-002`, or a list of `q-NNN`). **No ID → do nothing.**
- Each run requires IDs that exist in the current `/workspace/job-desk/queue.md`. There is no standing "always apply" permission.
- Unknown or stale IDs: refuse those, continue known ones, list refusals.
- IDs not named in this message: do not send or submit, even if they are `drafted` in the queue.
- `draft-only` (LinkedIn Easy Apply, login ATS): do not submit; say what is already drafted.
- `email`: send the existing outreach draft only if a mail connector is connected. If not, stop for that ID and say mailbox missing. Do not invent a recipient address.
- `ats-form`: computer-use the public apply URL and submit **only** named IDs.
- CAPTCHA / 2FA / passkey: stop that ID, ask for takeover, mark it blocked, continue the rest.
- Never invent resume facts. Use the tailored draft already on disk.
- Never copy queue, tracker, or resume into a template.

## Sequence

1. Read `/workspace/job-desk/queue.md`. If missing or empty, stop.
2. Extract `q-NNN` IDs from the operator message. Reject "approve all", "all of them", or a bare "yes" with no IDs.
3. For each named ID that exists and is `drafted` (or equivalent not-yet-sent):
   - `ats-form`: open the apply URL, fill from the tailored resume and fixture/operator contact already on disk, submit. Record the POST.
   - `email`: send only with a connected mailbox and a recipient they provided or that the posting listed as a public jobs@ address they confirmed.
   - `draft-only` or login wall remaining: skip submit; report prepared artifacts.
4. Update `application-tracker`: `sent` on success; leave `drafted` if blocked or mailbox missing. Note the queue ID.
5. Update queue status for those IDs (`sent` or `blocked`).
6. Write an execute log (chat + `/workspace/job-desk/runs/<run-id>/artifacts/execute-log.md` in harness mode).

## Output format

```markdown
# Execute log

Approved IDs: q-001
Unknown IDs refused:
Not named (left untouched):

## q-001
Channel: ats-form | email | draft-only
Result: submitted | sent | blocked | draft-only | mailbox missing
Tracker: sent | drafted
Notes: takeover needed / none
```

## Failure

If the apply page is a login wall or CAPTCHA, do not invent a successful submit. If they named no IDs, do not guess.
