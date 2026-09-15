---
name: first-run-job-desk
description: Walks first-run setup for Job Application Desk (master resume path, optional voice samples, private tracker, sources, queue). Use on the first chat after install. Never copies the resume into a public template. Never applies unless execute-approved-applications has named queue IDs.
---

# First-run: Job Application Desk

## When to use

First message after install, or "set up".

## Approval bar

- Master resume stays on **their** computer (`/workspace/job-desk/master-resume.md` unless they choose another path).
- Do not put their real CV, email, or phone into skills, this git repo, or Share as template.
- No ATS login required to start. Paste or public URL is enough.
- Never submit Greenhouse/Lever/LinkedIn forms from first-run.
- `sources.md` and `queue.md` are private (same Flora rule as the tracker).
- Do not activate a weekday routine until at least one `public` or `rss` row exists in `sources.md` and they confirm timezone.

## Sequence

1. State the job: JD → match score with evidence → tailored resume → outreach draft; optional weekday `job-inbox-cycle` digest; send/submit only for named queue IDs via `execute-approved-applications`; never invent experience.
2. Ask them to paste or upload a master resume. Save it to `/workspace/job-desk/master-resume.md`. Confirm you will not include it in a template.
3. Optional: 2–3 writing samples for voice (`/workspace/job-desk/voice-samples.md`).
4. Create empty `/workspace/job-desk/tracker.md` via `application-tracker`, empty `/workspace/job-desk/sources.md` via `job-sources`, and empty `/workspace/job-desk/queue.md`.
5. Confirm skills: `parse-jd`, `match-score`, `tailor-resume`, `draft-outreach`, `application-tracker`, `job-sources`, `job-inbox-cycle`, `execute-approved-applications`.
6. Offer a dry run using this plugin's `testpacks/job-application-desk/fixtures/sample-resume.md` + `sample-jd.md` **or** a public JD they paste. Prefer the fixture if they have not given a resume yet so nothing personal is stored.
7. **Harness mode (preferred dogfood):** on this computer run `python3 -m pip install -e ./testkit` (once) then `python3 -m grok_bot_testkit serve --pack job-application-desk`. Follow `testpacks/job-application-desk/scenario.md` (paste path, never POST `/apply`). Optional second paste: `testpacks/job-application-desk/scenario-inbox.md` (inbox cycle then one named-ID submit). Write evidence under `/workspace/job-desk/runs/<run-id>/`.
8. Offer the weekday routine only after a `public` or `rss` source exists. Ask them to paste this (Grok Bot creates the routine in the app; this repo does not):

```
Every weekday at 8:00 AM in my Bot timezone, run job-inbox-cycle against /workspace/job-desk/sources.md. Post the digest here. Do not email or submit. If a source is a login wall or missing, skip it and say so; do not reuse stale JDs.
```

   Do not enable the routine yourself if they have no public/rss source. Execute is not a second schedule — they reply `approve: q-NNN` after a digest.
9. Template reminder: before Share as template, delete resume/tracker/voice/sources/queue files from the Bot's shared config and memories.

## Output

Checklist: resume path (or fixture-only mode), tracker path, sources path, dry-run/harness offer, routine prompt (offered, not auto-enabled), next command ("score this JD" or "add a public source").

## Failure

If they refuse to store a resume on the computer, work paste-per-session and do not persist it.
