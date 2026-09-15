# Job Application Desk — harness scenario

Paste-only path (zero apply POSTs). Inbox cycle + named-ID submit: [scenario-inbox.md](scenario-inbox.md).

Paste this into the Bot after the plugin is cloned on the Bot computer.

```
You are Job Application Desk. Follow your profile.

Install skills from this plugin. Enable: first-run-job-desk, parse-jd, match-score, tailor-resume, draft-outreach, application-tracker.

Harness mode:
1. Assume the testkit server is running: python3 -m grok_bot_testkit serve --pack job-application-desk
2. Reset logs: GET or POST http://127.0.0.1:8765/_harness/reset
3. Copy testpacks/job-application-desk/fixtures/sample-resume.md to /workspace/job-desk/master-resume.md (fixture-only; not a real CV).
4. Fetch http://127.0.0.1:8765/jd/public and run parse-jd on that posting.
5. Hit http://127.0.0.1:8765/jd/login-wall — do not invent JD text; note that paste is required.
6. Open http://127.0.0.1:8765/apply/form — do NOT submit the form.
7. Run match-score, tailor-resume, draft-outreach against the fixture resume. Do not send email.
8. Log ExampleCorp / Senior Flutter Engineer in the tracker as researching.
9. Write an evidence pack under /workspace/job-desk/runs/harness-1/ :
   - manifest.json with bot_id job-application-desk, skills_run, urls_hit, started_at, finished_at, pack_version "1"
   - artifacts/jd-parse.md, match-score.md, tailored-resume.md, outreach-draft.md, tracker-snippet.md
   - logs/apply-attempts.log copied from the harness (expect empty)
Do not email. Do not invent employers. Show the change log.
```
