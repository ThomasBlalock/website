# projects — the projects tab

## What you're building

A page (or set of pages) served at `/projects/` that gives each project enough room to breathe. The resume tab summarizes; this tab tells the actual stories — what was built, what was novel, what was won, links to code / videos / repos. Visitors who care will spend several minutes here.

## Deliverable contract

Place an `index.html` (plus an optional `page.css` and any image references) in this directory.

When nginx serves `/projects/`, it returns this `index.html`. The page must:

- Use the shared top nav and footer pattern (see Style integration).
- Cover every entry from `/profile.json.ventures`, `/profile.json.research`, and `/profile.json.projects`.
- Be navigable: either a long page with an in-page TOC, or `/projects/` as a list plus per-project sub-pages (e.g. `/projects/fins/`, `/projects/bci/`). Either implementation is acceptable. If you choose sub-pages, each lives in its own folder with its own `index.html`.

## Inputs

- `/profile.json` — source of truth. Use the entries in:
  - `ventures` → Agent Service Index, Sidequest Local
  - `research` → Flexible Input Networks, Informed Machine Learning, NATO Alliance Space Deterrence
  - `projects` → Automated Conversational Hijacking, Brain–Computer Interface, Autonomous Rover, Facial Recognition Similarity Query
- `/images/` — useful: `IMG_20230920_223752747_HDR.jpg` (EEG cap), `B.JPG` (giving a talk), `IMG_7440.jpg` (cyber award), `20220607_Steve-Boxall_COS_ZG632_Space-Force_0431.jpg` (parabolic flight), `rover_video.mp4` (rover footage — short, autoplay muted loop is acceptable). Use sparingly; an image must add information, not decoration.
- The web4 essay lives in `/essays/`; if a project links to it, link out — do not duplicate.

## Style integration

Include `/shared/styles.css` via `<link rel="stylesheet" href="/shared/styles.css">`. Read `/shared/STYLE.md` *before* you start — it defines the typography scale, the spacing rhythm, the accent color, and the section-block primitive used across the site. Mount the shared nav by including the empty `<header id="site-nav"></header>` slot and `<script src="/shared/shell.js" defer></script>` — the script fetches `/shared/nav.html` and injects it (and marks the current tab). Use `/shared/BOILERPLATE.html` as your starting `index.html` and replace its `<main>`.

## Constraints / guidance

- **Group by category, with Ventures first.** The site's centerpiece is ASI + Sidequest; they get the most space and the most-prominent placement.
- **Each entry should answer:** what was built, why it was interesting, what role Thomas played (individual / team of N / led N), where it was presented or what it won, and links to code / video / external pages.
- **For research entries:** the awards and presentation venues are part of the story (CORONA, Director of NSA, NATO Paris wargame). Don't bury them.
- **Tone:** see `/profile.json.what_to_avoid_in_copy`. Specifically — "I built malware that phishes your friends" is a great story; lean into the agentic malware piece, don't sanitize it. Same for "won a rover race against other cadets" — concrete is better than generic.
- **For ASI specifically:** the web4 essay at `/essays/web4/` is the long-form pitch. The projects page should give the elevator pitch + the three live services + the cross-link.
- **Length per entry:** 80–200 words of prose, plus a header with dates and affiliations, plus links. Don't write a paper.

## Out of scope

- Reproducing the resume.
- Rendering the web4 essay (that's `/essays/`'s job — link out).
- Inventing projects or claims not in `profile.json`.
- Image galleries / lightboxes / carousels.
