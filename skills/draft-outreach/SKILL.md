---
name: draft-outreach
description: Drafts a cover note, LinkedIn message, or email in the user's voice from examples they paste. Use when they need first-message copy for a role. Never sends unless execute-approved-applications is running with named queue IDs.
---

# Draft outreach

## When to use

After a match score (and usually a tailored resume). Channel: email, LinkedIn, or cover letter field.

## Approval bar

- Never send, never CC, never use a connected mailbox to deliver **unless** `execute-approved-applications` is the active skill and the operator named this role's queue ID (`q-NNN`).
- Do not invent a referral, mutual, or metric.
- Voice comes from optional samples they paste; if none, use plain professional English and say so.
- Stop at the draft when used from chat, `job-inbox-cycle`, or any path without named IDs.

## Sequence

1. Channel and recipient role (recruiter / hiring manager / unknown).
2. Three facts from the JD they actually match (from match-score FOR rows).
3. One honest gap if it would otherwise look evasive.
4. Ask + next step (they send, or they reply `approve: q-NNN` so `execute-approved-applications` can send).
5. Keep it short: email ≤ 150 words, LinkedIn ≤ 300 characters unless they ask longer.

## Output format

```markdown
# Outreach draft

Channel:
To: [role, not a harvested personal address unless they provided it]
Do not send.

## Draft

## Why these claims are allowed
- Fact → resume evidence

## Not in this draft
Claims without evidence, send action
```
