# contact — the contact tab

## What you're building

A short page at `/contact/` that shows visitors how to reach Thomas. It is the smallest tab and should feel inviting, not transactional. A visitor who lands here should leave with at least one clear way to start a conversation.

## Deliverable contract

Place a single `index.html` (plus an optional `page.css`) in this directory.

When nginx serves `/contact/`, it returns this `index.html`. The page must:

- Use the shared top nav and footer pattern (see Style integration).
- List, at minimum: email, GitHub, LinkedIn.
- Be readable at desktop, tablet, and mobile.

## Inputs

- `/profile.json.contact` — email, GitHub, LinkedIn.
- `/profile.json.ventures` — ASI and Sidequest URLs if you want to surface them as alternative routes to reach work he leads.
- `/profile.json.person.location` — "Charlottesville, VA" (for the "where" note).

## Style integration

Include `/shared/styles.css` via `<link rel="stylesheet" href="/shared/styles.css">`. Read `/shared/STYLE.md` *before* you start — it defines the typography scale, the spacing rhythm, the accent color, and the section-block primitive used across the site. Mount the shared nav by including the empty `<header id="site-nav"></header>` slot and `<script src="/shared/shell.js" defer></script>` — the script fetches `/shared/nav.html` and injects it (and marks the current tab). Use `/shared/BOILERPLATE.html` as your starting `index.html` and replace its `<main>`.

## Constraints / guidance

- Lead with one short paragraph in Thomas's voice. Something like "Email is the fastest way; I read all of it." Not a contact form.
- Each link gets its own line or card; tap targets must be large on mobile.
- No CAPTCHA, no "send me a message" form. Email is the answer.
- A note about typical response time (e.g. "Replies within 48h on weekdays") is welcome but optional.
- If you want one small piece of personality: a sentence about what kinds of messages are most useful (collaboration on agent infrastructure, founders building for agents, students asking questions about USAFA or research, etc.). Optional.

## Out of scope

- A contact form / mailer.
- Phone number (unless added to `profile.json` later).
- A meeting-scheduler embed.
- A long bio (link to `/` for that).
