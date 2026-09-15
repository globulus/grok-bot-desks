# Flutter Mobile Engineer — harness scenario

```
You are the Flutter Mobile Engineer desk. Follow your profile description.

Install skills from this plugin. Enable: first-run-flutter-engineer, flutter-pr-review, flutter-test-plan, mobile-release-hygiene.

Harness mode:
1. Assume testkit is serving: python3 -m grok_bot_testkit serve --pack flutter-mobile-engineer
2. Reset: http://127.0.0.1:8766/_harness/reset
3. Open http://127.0.0.1:8766/pr/sample (fixture PR page) and/or use testpacks/flutter-mobile-engineer/fixtures/sample-flutter-issue.md plus testpacks/flutter-mobile-engineer/fixtures/sample-diff.md.
4. Dry-run flutter-pr-review. Prefer fvm-prefixed commands when discussing Flutter tooling. Do not push or open a PR. Do not POST to /github/comment.
5. Optionally draft a short flutter-test-plan for the counter increment case.
6. Write evidence under /workspace/flutter-desk/runs/harness-1/ :
   - manifest.json (bot_id flutter-mobile-engineer, skills_run, urls_hit, timestamps, pack_version "1")
   - artifacts/pr-review.md (and artifacts/test-plan.md if produced)
   - logs/github-posts.log from the harness (expect empty)
```
