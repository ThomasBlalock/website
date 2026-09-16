# thomasblalock.com — design language

Read this **before** you write a single line in your component. The whole site only feels coherent if every tab speaks the same visual language.

## The one-line read

An **operations board**. The work on this site is all routing and allocation under constraints — airlift logistics, an agent service registry, a rover finding a line, an app matching people to plans, EEG signals routed to characters — so the site looks like the board an analyst reads: a pale plotting surface with a faint grid, a dark dispatch strip across the top, chart-style section titles, indexed rows, and mono telemetry everywhere. Archivo (expanded, heavy) for display, Newsreader for prose, IBM Plex Mono for every piece of metadata. Deep signal green is the structural accent; burnt orange is a status light — LIVE, NOW, awards — and appears a handful of times a page at most.

## Source of truth

`/shared/styles.css` defines the design tokens. Never redefine these in your component:

| Token | Value | Use for |
| --- | --- | --- |
| `--bg` | `#e7e8e3` | Page ground (carries the plot grid) |
| `--paper` | `#f2f3ef` | Panels |
| `--paper-lift` | `#f8f9f5` | Panel hover |
| `--ink` | `#121517` | Primary text |
| `--ink-soft` | `#3c444a` | Secondary text |
| `--muted` | `#767f86` | Eyebrows, dates, metadata |
| `--rule` | `#c4c9c3` | Hairlines |
| `--rule-soft` | `#d5d9d3` | Fainter hairlines (inside panels) |
| `--grid` | `rgba(18,21,23,.075)` | The plot grid on `body` |
| `--accent` | `#0d5c3c` | Signal green — structure, node markers, links on hover, active state |
| `--accent-soft` | `#d7e4dc` | Accent wash |
| `--signal` | `#b34a18` | Burnt orange — status only: the LIVE pill, the NOW marker, award citations. Never decorative. |
| `--bar` / `--bar-ink` | `#14181a` / `#e7e8e3` | The dispatch strip |
| `--display` / `--sans` | `Archivo` | Headlines and body sans |
| `--serif` | `Newsreader` | Prose, ledes, taglines |
| `--mono` | `IBM Plex Mono` | Dates, metadata, kickers, nav, labels |

Archivo is variable on the width axis. Display type is set at `font-stretch: 112%`–`115%` with tight negative tracking — that expanded, heavy cut is the site's signature. Set it with `font-stretch`, not `font-variation-settings`.

## What's already in styles.css (use these, don't reinvent)

- `.topbar` — the dispatch strip, mounted automatically by `shell.js`
- `.page` — the max-width container; wrap your `<main>` content
- `.block`, `.block-head`, `.dateline` — section primitive. The head is a chart title: label on the left, a hairline running to the right margin, a mono dateline pinned to the edge. The rule is a `::after` pinned to `grid-row: 1` — if you build your own head, pin the row explicitly or sparse auto-placement will drop the rule onto a second line.
- `.kicker` — mono eyebrow above a heading
- `.tag`, `.tag.live`, `.badge` — small inline labels. `.tag.live` carries a pulsing status dot (disabled under `prefers-reduced-motion`).
- `.manifest` — a mono key/value block, the flight-ops card (`<dl><dt>Role</dt><dd>…</dd></dl>`)
- `.route` — stations on a line; the "range" motif. Collapses to a two-column legend under 940px.
- `.muted`, `.quiet`, `.serif`, `.sans`, `.mono`
- `.accent-rule` — left-border callout
- `.site-foot` — bottom footer (in BOILERPLATE.html)

## What goes in *your* component CSS

Anything component-specific. Resume's date rail, projects' node rail, contact's panel rows — those live in a sibling `page.css` file in your folder, included with `<link rel="stylesheet" href="page.css">`. **Never modify `/shared/styles.css`.**

## Typography rhythm

- H1 hero: `clamp(40px, 10vw, 98px)`, `font-weight: 800`, `font-stretch: 115%`, `line-height: .92`, `letter-spacing: -.04em`. Used **once per page**.
- H2 section: `30px`, display, `font-weight: 700`. Pair with a `.dateline` on the right.
- H3 entry: `19–26px`, display, `font-weight: 600`.
- Lede paragraph: serif, `19–20px`, `line-height: 1.5`, `max-width: 58ch`.
- Body: sans, `16px`, `line-height: 1.55`. Prose blocks: serif, `17–18px`, `line-height: 1.6–1.65`.
- Metadata: mono, `10.5–12px`, uppercase, `letter-spacing: .1–.16em`.

## Spacing rhythm

Sections are `.block` (40px vertical padding, hairline divider), tightening to 32px at 880 and 26px at 620. Container padding is the `--pad-x` / `--pad-y` tokens, which step down at 880 → 720 → 620 → 400. Never hardcode page padding.

## Mobile is not an afterthought

The site is read on phones. Non-negotiable:

- **Nothing scrolls sideways at 320px.** `/tmp`-style spot checks are not enough — long mono strings, URLs, and headlines are the usual culprits. Give long values `overflow-wrap: anywhere` and let headlines wrap at real spaces (do **not** join a whole headline with `&nbsp;` — it forces a mid-word break).
- Any grid narrower than three comfortable columns collapses to one.
- Interactive rows are at least 44px tall.
- The nav becomes a two-row instrument panel under 720px: brand on top, a five-cell tab strip below. Adding a tab means updating `repeat(5, 1fr)` in the mobile `.topbar .tabs` rule.

## Tone (copy)

- No buzzwords ("synergy", "leverage", "cutting-edge", "passionate about").
- Lead with what was built and what it did. Avoid resume-speak.
- The site is for general public + recruiters + curious internet visitors. Not an investor deck.
- **Do not rewrite Thomas's prose.** The paragraphs are his voice; edit them only when a fact goes stale.
- See `/profile.json` → `what_to_avoid_in_copy` for the full list.

## Linking out

- ASI: <https://agentserviceindex.com>
- Sidequest: <https://sidequestlocal.com>
- Email: <mailto:blalockthomasm@gmail.com>
- GitHub: <https://github.com/ThomasBlalock>
- LinkedIn: <https://www.linkedin.com/in/thomas-blalock/>

## The active tab

`shell.js` adds `.active` and `aria-current="page"` to the current tab's nav link automatically. Don't reimplement.

## Anti-patterns (do not do)

- Don't import a CSS framework. Tailwind/Bootstrap/MUI are out.
- Don't add a hero blob, glassmorphism card, or generic 3-column "Featured" grid.
- Don't use colour gradients. The only gradients in the stylesheet draw the plot grid.
- Don't add rounded corners or soft shadows. Panels are flat paper with square corners and one hairline.
- Don't spend the orange. It marks live status, the NOW line, and award citations — nothing else.
- Don't add JS animations beyond the small CSS transitions already here.
- Don't hardcode the nav HTML; let `shell.js` inject it.
- Don't redefine tokens or copy primitives into your component CSS.
