# thomasblalock.com — design language

Read this **before** you write a single line in your component. The whole site only feels coherent if every tab speaks the same visual language.

## The one-line read

A printed-magazine voice on warm off-white paper. Fraunces (serif) for display, Inter (sans) for body, JetBrains Mono for metadata. One terra-red accent. Generous spacing. Strong typographic hierarchy. No gradients, no glassmorphism, no decorative shadows, no rounded "card" theming.

## Source of truth

`/shared/styles.css` defines the design tokens. Never redefine these in your component:

| Token | Value | Use for |
| --- | --- | --- |
| `--bg` | `#f7f4ee` | Page background |
| `--paper` | `#fdfbf6` | Cards / panels |
| `--ink` | `#16110b` | Primary text |
| `--ink-soft` | `#4a4339` | Secondary text |
| `--muted` | `#8a8175` | Eyebrows, dates, metadata |
| `--rule` | `#d8d1c2` | Hairlines |
| `--accent` | `#b3331f` | The single accent — links on hover, the live tag, the bottom border of the active nav |
| `--accent-soft` | `#f3dcd5` | Badge backgrounds |
| `--serif` | `Fraunces, …` | Headlines, lede, quoted prose |
| `--sans`  | `Inter, …`   | Body copy, lists, dense info |
| `--mono`  | `JetBrains Mono, …` | Dates, metadata, kickers, nav |

## What's already in styles.css (use these, don't reinvent)

- `.topbar` — handled automatically by `shell.js`
- `.page`   — the max-width container; wrap your `<main>` content
- `.block`, `.block-head`, `.dateline` — section primitive
- `.kicker` — eyebrow text above a heading
- `.tag`, `.tag.live`, `.badge` — small inline labels
- `.muted`, `.quiet`, `.serif`, `.sans`, `.mono`
- `.accent-rule` — left-border quote/callout
- `.site-foot` — bottom footer (in BOILERPLATE.html)

## What goes in *your* component CSS

Anything component-specific. Resume's two-column grid, projects' card layout, contact's link grid — those live in a sibling `page.css` file in your folder, included with `<link rel="stylesheet" href="page.css">`. **Never modify `/shared/styles.css`.**

## Typography rhythm

- H1 hero: `clamp(48px, 7vw, 92px)`, `line-height: 0.94`, `letter-spacing: -0.035em`. Used **once per page**.
- H2 section: `32px`, serif, `font-weight: 700`. Pair with a `.dateline` on the right.
- H3 entry: `22px`, serif, `font-weight: 600`.
- Lede paragraph: serif, `19px`, `line-height: 1.45`, `max-width: 50ch`.
- Body: sans, `16px`, `line-height: 1.55`. Prose blocks: serif, `17–18px`, `line-height: 1.55`.

## Spacing rhythm

Sections are `.block` (32px vertical padding, hairline divider). Big breaks between sections are `padding-bottom: 56px` + `margin-bottom: 56px`. Container padding is the `--pad-x` / `--pad-y` tokens.

## Tone (copy)

- No buzzwords ("synergy", "leverage", "cutting-edge", "passionate about").
- Lead with what was built and what it did. Avoid resume-speak.
- The site is for general public + recruiters + curious internet visitors. Not an investor deck.
- See `/profile.json` → `what_to_avoid_in_copy` for the full list.

## Linking out

- ASI: <https://agentserviceindex.com>
- Sidequest: <https://sidequestlocal.com>
- Email: <mailto:blalockthomasm@gmail.com>
- GitHub: <https://github.com/ThomasBlalock>
- LinkedIn: <https://www.linkedin.com/in/thomas-blalock/>

## The active tab

`shell.js` adds `.active` to the current tab's nav link automatically. Don't reimplement.

## Anti-patterns (do not do)

- Don't import a CSS framework. Tailwind/Bootstrap/MUI are out.
- Don't add a hero blob, glassmorphism card, or 3-column generic "Featured" grid.
- Don't use gradients of any kind.
- Don't add rounded "soft" shadow themes. The site is paper, not iOS.
- Don't add a logo, favicon system, or branding lockup.
- Don't add JS animations beyond very small CSS transitions.
- Don't hardcode the nav HTML; let `shell.js` inject it.
- Don't redefine tokens or copy primitives into your component CSS.
