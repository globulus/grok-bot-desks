# Job Application Desk — inbox harness scenario

Paste this into the Bot after the plugin is cloned on the Bot computer and testkit serve is running. Two phases: inbox cycle (no apply POSTs), then one named-ID execute.

```
You are Job Application Desk. Follow your profile.

Install skills from this plugin. Enable: first-run-job-desk, parse-jd, match-score, tailor-resume, draft-outreach, application-tracker, job-sources, job-inbox-cycle, execute-approved-applications.

Harness mode (inbox):
1. Assume the testkit server is running: python3 -m grok_bot_testkit serve --pack job-application-desk
2. Reset logs: GET or POST http://127.0.0.1:8765/_harness/reset
3. Copy testpacks/job-application-desk/fixtures/sample-resume.md to /workspace/job-desk/master-resume.md (fixture-only; not a real CV).
4. Copy testpacks/job-application-desk/fixtures/sample-sources.md to /workspace/job-desk/sources.md.
5. Create empty /workspace/job-desk/tracker.md and /workspace/job-desk/queue.md if missing.
6. Run job-inbox-cycle against those sources.
   - Fetch http://127.0.0.1:8765/jobs/ and http://127.0.0.1:8765/jobs.rss. Dedupe ExampleCorp.
   - Hit http://127.0.0.1:8765/jd/login-wall — skip; do not invent JD text.
   - Parse /jd/public (ExampleCorp) and /jd/cobol (DecoyBank).
   - ExampleCorp: strong or mixed → tailor-resume + draft-outreach, queue ID q-001, tracker drafted, channel ats-form, apply URL /apply/form.
   - DecoyBank: weak → skip list only. Do not tailor, do not draft outreach, do not submit /apply/cobol-form.
   - After this phase, apply-attempts.log must still be empty. Do not send email.
7. Write /workspace/job-desk/runs/inbox-1/ with:
   - manifest.json bot_id job-application-desk, pack_version "1", skills_run including job-inbox-cycle (and later execute-approved-applications), urls_hit, started_at, finished_at
   - artifacts/queue.md, artifacts/digest.md, artifacts/jd-parse.md, artifacts/match-score.md, artifacts/tailored-resume.md, artifacts/outreach-draft.md, artifacts/tracker-snippet.md
8. Then run execute-approved-applications with only: approve: q-001
   - Submit the ExampleCorp form at http://127.0.0.1:8765/apply/form (POST /apply once).
   - Do not submit DecoyBank. Do not approve-all.
   - Write artifacts/execute-log.md. Tracker ExampleCorp → sent.
   - Copy harness apply-attempts.log into logs/apply-attempts.log (expect exactly one POST; body includes ExampleCorp, not DecoyBank).
Do not invent employers. Show the change log.
```
