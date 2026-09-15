---
name: first-run-app-store-ship
description: First-run for App Store Ship Desk. Use when enabling the wave-2 store-listing bot. Never submits; 2FA is a computer takeover.
---

# First-run: App Store Ship

## When to use

First message after enabling the App Store Ship desk (wave 2), or the user says "set up".

## Approval bar

- Do not store App Store Connect or Play Console passwords in chat, skills, or a public template.
- Browser login for 2FA = computer takeover, never paste codes into chat.
- Never click Save/Submit in the store consoles without an explicit yes.

## Sequence

1. Ask for: app repo, last shipped version, whether they want What's New only or full listing.
2. Confirm skills: `changelog-from-commits`, `listing-copy`, `screenshot-spec`, `version-bump-checklist`.
3. Offer a dry draft of What's New from recent commits if a public repo is connected; do not submit.

## Output

Checklist: repo, last version, listing scope, next command ("draft What's New").
