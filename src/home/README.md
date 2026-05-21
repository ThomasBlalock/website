# home — the landing tab

## What you're building

The page a visitor sees first at `/`. It's the centerpiece. A visitor should leave understanding (1) Thomas's current ventures — ASI and Sidequest — and (2) one or two reasons he's qualified to build them. Other tabs cover everything else; this page is the overview.

## Deliverable contract

Place a single `index.html` (plus an optional `page.css` for component-scoped styles, plus any other static assets) in this directory.

When nginx serves the URL `/`, it returns this directory's `index.html`. Internal links from the home page may target `/resume/`, `/projects/`, `/essays/`, `/contact/` — those routes are guaranteed by the gateway.

The page must:

- Use the shared top nav and footer pattern (see Style integration).
- Be readable at desktop (≥1080px), tablet (~768px), and mobile (~375px).
- Load in under 1s on a fresh visit (no large embedded media unless necessary).

## Inputs

- `/profile.json` — the source-of-truth content dump. Use `person`, `ventures`, `short_bio`, `site_direction`, `skills_and_interests.themes_to_surface`, and `what_to_avoid_in_copy`.
- `/images/` — available portraits and field photos. Pick at most one for the hero if you want one. Headshot: `IMGM3501.JPG`. Cadet salute: `tmp_8999eac4-7e16-431f-9c0b-f99fa4c43e2d.jpeg`. Talk: `B.JPG`. Lt portrait: `_CTB3703.jpg`. The rest are field shots (EEG, parabolic flight, awards) — skip unless they earn their place.

## Style integration

Include `/shared/styles.css` via `<link rel="stylesheet" href="/shared/styles.css">`. Read `/shared/STYLE.md` *before* you start — it defines the typography scale, the spacing rhythm, the accent color, and the section-block primitive used across the site. Mount the shared nav by including the empty `<header id="site-nav"></header>` slot and `<script src="/shared/shell.js" defer></script>` — the script fetches `/shared/nav.html` and injects it (and marks the current tab). Use `/shared/BOILERPLATE.html` as your starting `index.html` and replace its `<main>`.

## Constraints / guidance

- **Centerpiece is the two ventures.** ASI gets first billing (it's the harder idea); Sidequest gets the contrast. Lead with what they do, then why they matter.
- **One short "Now" sentence** (current month, what's actively being built). Read `profile.json` → `open_questions_for_thomas_to_fill_in_later` — this is the "Now" paragraph he wants.
- **One short "Background in three lines"** that hooks recruiters without becoming a resume. Don't list GPAs and ranks here — that's the Background section on /resume.
- **End with one or two clear next steps** — links to /projects, /essays, /contact.
- **Three sections, max.** This page is not the whole site.
- Voice: see `/profile.json.what_to_avoid_in_copy`. No buzzwords. Lead with what was built and what it did.
- It is fine to have a quiet, italic second paragraph in the lede that gives the page personality (see Thomas's "two companies that have approximately nothing to do with each other" framing from `profile.json.fun_facts_and_color`).

## Out of scope

- The full resume (that's `/resume/`).
- Per-project deep dives (that's `/projects/`).
- The web4 essay or any other long-form writing (that's `/essays/`).
- Long contact info (that's `/contact/` — link to it).
- A photo gallery — pick at most one image with intent, or none.
