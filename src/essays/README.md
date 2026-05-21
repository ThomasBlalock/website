# essays — the essays tab

## What you're building

A reading surface for Thomas's long-form writing, served at `/essays/`. Currently one essay exists (`essays/web4.md`); the system must accept new markdown files dropped into `essays/` without code changes. The web4 essay is the launch piece; this tab is built to host many more.

## Deliverable contract

This subdirectory must deliver:

1. **A list page** served at `/essays/`. It auto-discovers every `*.md` file in `./essays/` and renders a list of them, newest first. Each list entry shows: title, date, one-sentence summary, and a link to the per-essay reader page.

2. **A per-essay reader page** at `/essays/<slug>/` (or `/essays/<slug>.html` if your routing requires it — the gateway tolerates both). The slug is derived from the markdown filename (e.g. `web4.md` → `/essays/web4/`). It must render the markdown faithfully (headings, lists, links, blockquotes, inline `<aside>`/`<div>`/`<pre>` HTML, footnotes if present, code blocks) and look at home in the site's design language.

3. A working route for `/essays/web4/` today, since `essays/web4.md` is in this directory.

You may implement this any way you like — static-site build step, server-side renderer, or client-side markdown rendering. **Whatever you pick, the final delivered files must be servable by the project's static `nginx.conf` without additional sidecar containers.** Acceptable approaches:

- **Static build:** a `build.py` (or `build.sh`, `build.js`) that walks `essays/*.md`, writes a list `index.html` and per-essay HTML files. Document how to run it in a short note at the top of your build script. The output of the build is what nginx serves.
- **Client-side render:** a static `index.html` for the list page that fetches a manifest (which you may also generate at build time, or hand-write the discovery logic into JS via `fetch('/essays/essays/')` directory listing — note: nginx does not enable autoindex, so a manifest file is required). A single static `reader.html` (or per-essay folders) that reads `?slug=foo` and fetches + renders `/essays/essays/foo.md` via a small markdown lib.

Prefer the **static build** approach — it's the most robust, the cheapest at runtime, and the easiest to debug. Document how to re-run it whenever an essay is added. If you go with a build, the build is part of your deliverable.

## Inputs

- `essays/` (this directory) — currently contains `web4.md`. New essays will be dropped here.
- Each markdown file *may* have YAML frontmatter:
  ```yaml
  ---
  title: The Path to Web 4.0
  date: 2026-05
  summary: A self-reinforcing discovery layer for autonomous agents.
  ---
  ```
  If frontmatter is missing, infer the title from the first `<h1>`/`<h2>` heading or the filename, and the date from filesystem mtime as a fallback.
- The current `web4.md` does NOT have frontmatter — it opens with an `<aside class="abstract">` block. **Add frontmatter to `essays/web4.md` if you need it for sorting/discovery**, but do not otherwise modify the essay text. The user explicitly asked to render the essay's content as-is, not rewrite it.
- `/profile.json` if you need bio info to introduce the essays list page (optional — keep the list page restrained).

## Style integration

Include `/shared/styles.css` via `<link rel="stylesheet" href="/shared/styles.css">`. Read `/shared/STYLE.md` *before* you start — it defines the typography scale, the spacing rhythm, the accent color, and the section-block primitive used across the site. Mount the shared nav by including the empty `<header id="site-nav"></header>` slot and `<script src="/shared/shell.js" defer></script>` — the script fetches `/shared/nav.html` and injects it (and marks the current tab). Use `/shared/BOILERPLATE.html` as your starting `index.html` and replace its `<main>`.

## Constraints / guidance

- **Reader page typography:** the essay reader is the *one* place on the site where prose width should be tight (~65ch), line-height generous (~1.65), serif. Treat it like a printed essay page. The default `.page` container is too wide; constrain inside your own component CSS.
- **Honor the inline HTML in `web4.md`.** It contains `<aside class="abstract">`, `<nav class="toc">`, a `<div class="ladder">`, `<pre class="cite-block">`, and `<section class="refs">`. Style these in your component CSS to look intentional — your CSS should provide rules for `.abstract`, `.toc`, `.ladder`, `.pullquote`, `.refs`, and `.cite-block`.
- **Footnote-style references:** the essay uses Markdown extensions like `{: #s1}` (Kramdown ID syntax) on headings. If your markdown library doesn't support that, either swap libraries or post-process to add IDs.
- **Table of contents:** the essay author already wrote a TOC inside the markdown. Render it as-is; do not generate an additional one.
- **List page:** restrained. Title, date, one-sentence summary, link. No card grid, no thumbnails. Sorted newest first.
- **One essay today, more to come.** The system must work the day a second essay lands. Test by dropping a second tiny `test.md` in `essays/`, verifying it shows up, then removing it.
- **Don't paraphrase or rewrite essay content.** Markdown → HTML, faithfully. The user was explicit about this.

## Out of scope

- Comments / likes / share buttons.
- Search across essays (defer until there's more than one).
- An RSS feed (nice-to-have, not required).
- Authentication / drafts.
- Modifying the prose of `web4.md` (adding frontmatter at the very top is fine; touching the body is not).
