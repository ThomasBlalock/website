# resume — the resume tab

## What you're building

A webpage version of Thomas's resume, served at `/resume/`. **Not** a download of the PDF and **not** an embedded PDF viewer. The PDF in the repo root (`/Blalock_resume.pdf`) is *outdated*; treat it only as a section-structure reference. The current information lives in `/profile.json`.

## Deliverable contract

Place a single `index.html` (plus an optional `page.css`) in this directory.

When nginx serves `/resume/`, it returns this `index.html`. The page must:

- Use the shared top nav and footer pattern (see Style integration).
- Print cleanly on Letter paper (add a `@media print` block so the nav and footer hide, links print as black, the layout reflows to a single column).
- Be a real webpage, not a PDF clone. Use the site's typography and spacing rhythm.
- Read top-to-bottom as a resume — the visitor should be able to scan it in 30 seconds.

## Inputs

- `/profile.json` — source of truth. Use:
  - `person` (name, location, status — note: now Air Force Operations Research Analyst + MS Data Science at UVA + founder of two companies)
  - `contact`
  - `education` (UVA + USAFA + NMMI + UCO)
  - `research` (FINs, Informed ML, NATO Space Deterrence)
  - `projects` (BCI, Rover, ACH, Facial Recognition)
  - `awards` (highlight Outstanding Cadet in CS, NRO scholarship, the two #1 USAFA research awards, Goldwater finalist)
  - `leadership` (Squadron Commander, Wing Academics NCOIC, Cadet Space Ops Sq Exec, Data Comp Team founder, etc.)
  - `skills_and_interests`
- `/Blalock_resume.pdf` — **outdated** but useful as a structural reference for what sections to include and the canonical ordering. Updates this version must reflect:
  - Current status: 2nd Lt + USAF Operations Research Analyst
  - MS Data Science at UVA (2025–2026, 4.0)
  - Founder of Agent Service Index (May 2026)
  - Founder of Sidequest Local (December 2025)
  - Outstanding Cadet in Computer Science award (USAFA 2025, #1 of CS class) — missing from the PDF
  - Updated phone/email if any (none changed; email is still `blalockthomasm@gmail.com`)
  - Add a top "Now" line with the current role/affiliation
- `/images/` — generally not needed on a resume; you may use the headshot (`IMGM3501.JPG`) at most.

## Style integration

Include `/shared/styles.css` via `<link rel="stylesheet" href="/shared/styles.css">`. Read `/shared/STYLE.md` *before* you start — it defines the typography scale, the spacing rhythm, the accent color, and the section-block primitive used across the site. Mount the shared nav by including the empty `<header id="site-nav"></header>` slot and `<script src="/shared/shell.js" defer></script>` — the script fetches `/shared/nav.html` and injects it (and marks the current tab). Use `/shared/BOILERPLATE.html` as your starting `index.html` and replace its `<main>`.

## Constraints / guidance

- **Section ordering** (suggested, matches the PDF): Contact → Education → Research → Projects → Leadership → Awards. You may insert a "Ventures" section near the top to surface ASI and Sidequest above Education — that's important since they're the centerpiece of the site.
- **Density:** the PDF is one page. This page can be longer because there's no paper limit, but don't pad. Each bullet should earn its line.
- **Dates** in `.mono` style on the right side; achievements on the left. The `.entry-grid` pattern from STYLE.md is a good fit (date column + content column).
- **Honors:** lead each with what was won, then a short clause on what it was. Strip the bureaucratic phrasing.
- **GitHub links** belong inline on the relevant entries (FINs, BCI, Rover, Facial Recognition).
- **Print:** include a Download CV link to `/Blalock_resume.pdf` ONLY if you also note (in small italic mono text) that the PDF lags this page. Or skip the link entirely — the print stylesheet is the better download mechanism.

## Out of scope

- Adding new facts the user has not provided in `profile.json`. If you find a gap, leave it; don't invent.
- The full essay content of web4 (link to `/essays/web4/` if you want to mention it).
- Project deep dives — link to `/projects/`.
- Decoration. A resume page is type and hierarchy.
