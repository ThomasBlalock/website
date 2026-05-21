#!/usr/bin/env python3
"""
build.py — Static site build for the /essays/ tab of thomasblalock.com.

What it does
------------
1. Walks every `essays/*.md` file in this directory.
2. Parses optional YAML frontmatter (title, date, summary). Falls back to
   inferring title from the first heading or the filename, and date from
   the file's mtime when frontmatter is missing.
3. Renders each markdown file to HTML using python-markdown with the
   `extra`, `attr_list`, `md_in_html`, `sane_lists`, `smarty`, and
   `footnotes` extensions. `md_in_html` is what allows `<aside markdown="1">`
   blocks (the abstract, the TOC, the references) to be parsed correctly.
   `attr_list` is what enables Kramdown-style `{: #id}` and `{: .class}`.
4. Writes the rendered essay to `<slug>/index.html` (slug = file stem).
5. Writes the list page to `./index.html`, newest first.

The output is plain static HTML served by nginx — no runtime renderer.

How to (re-)run
---------------
    cd /home/blalo/side_projects/website/src/essays
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
    .venv/bin/python build.py

Drop a new file into ./essays/<slug>.md and re-run the last command;
the list page and per-essay page appear automatically. Dotfiles
(`.hidden.md`) are ignored.
"""

from __future__ import annotations

import datetime as dt
import html
import os
import re
import sys
from pathlib import Path

import markdown
import yaml


# --- paths -------------------------------------------------------------------

HERE = Path(__file__).resolve().parent
ESSAYS_DIR = HERE / "essays"
SHARED_BOILERPLATE = HERE.parent / "shared" / "BOILERPLATE.html"


# --- frontmatter & metadata helpers -----------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?\n)---\s*(\n|$)", re.DOTALL)

# A first-pass title fallback: pluck the first ATX-style heading from prose.
HEADING_RE = re.compile(r"^\s{0,3}#{1,3}\s+(.+?)\s*(?:\{:[^}]*\})?\s*$", re.MULTILINE)


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (metadata_dict, body_markdown)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as e:
        print(f"  ! frontmatter parse error: {e}", file=sys.stderr)
        data = {}
    return data, text[m.end():]


def infer_title(body: str, fallback: str) -> str:
    m = HEADING_RE.search(body)
    if m:
        return m.group(1).strip()
    return fallback.replace("-", " ").replace("_", " ").strip().title()


def normalize_date(raw, mtime_fallback: float) -> tuple[str, str]:
    """
    Returns (sort_key, display).
    sort_key is an ISO-ish string ("YYYY-MM-DD" padded) usable for lexicographic sort.
    display is what we show in the dateline (e.g. "May 2026").
    """
    if raw is None or raw == "":
        d = dt.datetime.fromtimestamp(mtime_fallback)
        return d.strftime("%Y-%m-%d"), d.strftime("%b %Y")

    # PyYAML may give us a date, datetime, str, or int (year).
    if isinstance(raw, dt.datetime):
        return raw.strftime("%Y-%m-%d"), raw.strftime("%b %Y")
    if isinstance(raw, dt.date):
        return raw.strftime("%Y-%m-%d"), raw.strftime("%b %Y")
    if isinstance(raw, int):
        # bare year
        return f"{raw:04d}-01-01", str(raw)

    s = str(raw).strip()
    # Try common patterns.
    for fmt, display_fmt in [
        ("%Y-%m-%d", "%b %d, %Y"),
        ("%Y-%m", "%b %Y"),
        ("%Y/%m/%d", "%b %d, %Y"),
        ("%B %Y", "%b %Y"),
        ("%b %Y", "%b %Y"),
    ]:
        try:
            d = dt.datetime.strptime(s, fmt)
            sort_key = d.strftime("%Y-%m-%d") if "%d" in fmt else d.strftime("%Y-%m-01")
            return sort_key, d.strftime(display_fmt)
        except ValueError:
            continue
    # Last resort: keep the raw string for display, use mtime for sorting.
    d = dt.datetime.fromtimestamp(mtime_fallback)
    return d.strftime("%Y-%m-%d"), s


def derive_slug(path: Path) -> str:
    """Slug is the file stem, lowercased, with spaces collapsed to dashes.
    Letters, digits, dashes, and underscores are preserved as-is so authors
    can use either `-` or `_` separators in filenames."""
    stem = path.stem.lower()
    stem = re.sub(r"\s+", "-", stem)
    stem = re.sub(r"[^a-z0-9_\-]+", "-", stem).strip("-")
    return stem or "essay"


# --- markdown rendering ------------------------------------------------------

def make_renderer() -> markdown.Markdown:
    return markdown.Markdown(
        extensions=[
            "extra",         # tables, fenced code, def_list, footnotes, attr_list, md_in_html, ...
            "attr_list",     # {: #id .class} on headings/paragraphs (Kramdown)
            "md_in_html",    # parse markdown inside <aside markdown="1"> etc.
            "sane_lists",
            "smarty",        # nice quotes/ellipses
        ],
        output_format="html5",
    )


def render_markdown(body: str) -> str:
    md = make_renderer()
    return md.convert(body)


# --- page templating ---------------------------------------------------------

def load_boilerplate() -> str:
    return SHARED_BOILERPLATE.read_text(encoding="utf-8")


def render_page(*, title: str, head_extra: str, main_html: str) -> str:
    """Fill in the boilerplate. Title is HTML-escaped."""
    tpl = load_boilerplate()
    safe_title = html.escape(title, quote=True)
    tpl = tpl.replace("__SET_TITLE__", safe_title)

    # Inject the component CSS link before </head>.
    tpl = tpl.replace("</head>", f"  {head_extra}\n</head>")

    # Replace the entire <main> ... </main> block.
    tpl = re.sub(
        r"<main[^>]*>.*?</main>",
        main_html,
        tpl,
        count=1,
        flags=re.DOTALL,
    )
    return tpl


# --- per-essay HTML ----------------------------------------------------------

def render_essay_page(meta: dict, body_html: str) -> str:
    title = meta["title"]
    display_date = meta["date_display"]

    main = (
        '<main class="page essay-page">\n'
        '  <article class="essay">\n'
        '    <header class="essay-head">\n'
        f'      <div class="kicker">Essay · {html.escape(display_date)}</div>\n'
        f'      <h1 class="essay-title">{html.escape(title)}</h1>\n'
        '      <p class="essay-back"><a href="/essays/">← all essays</a></p>\n'
        '    </header>\n'
        '    <div class="essay-prose">\n'
        f'{body_html}\n'
        '    </div>\n'
        '  </article>\n'
        '</main>'
    )
    return render_page(
        title=title,
        head_extra='<link rel="stylesheet" href="/essays/page.css" />',
        main_html=main,
    )


# --- list page ---------------------------------------------------------------

def render_list_page(entries: list[dict]) -> str:
    items = []
    if not entries:
        items.append(
            '<li class="essay-entry essay-entry--empty">'
            '<p class="muted">No essays yet.</p>'
            '</li>'
        )
    else:
        for e in entries:
            summary = e.get("summary") or ""
            summary_html = (
                f'<p class="essay-summary">{html.escape(summary)}</p>'
                if summary else ""
            )
            items.append(
                '<li class="essay-entry">\n'
                f'  <div class="essay-dateline">{html.escape(e["date_display"])}</div>\n'
                '  <h3 class="essay-entry-title">'
                f'<a href="/essays/{e["slug"]}/">{html.escape(e["title"])}</a>'
                '</h3>\n'
                f'  {summary_html}\n'
                '</li>'
            )

    main = (
        '<main class="page essays-index">\n'
        '  <section class="block">\n'
        '    <header class="block-head">\n'
        '      <h2>Essays</h2>\n'
        '      <span class="dateline">writing</span>\n'
        '    </header>\n'
        '    <p class="essays-lede">'
        'Long-form notes on infrastructure for autonomous agents, '
        'and adjacent topics.'
        '</p>\n'
        '    <ol class="essay-list" reversed>\n'
        f'{chr(10).join(items)}\n'
        '    </ol>\n'
        '  </section>\n'
        '</main>'
    )
    return render_page(
        title="Essays",
        head_extra='<link rel="stylesheet" href="/essays/page.css" />',
        main_html=main,
    )


# --- main --------------------------------------------------------------------

def collect_essays() -> list[dict]:
    if not ESSAYS_DIR.is_dir():
        return []
    entries: list[dict] = []
    for path in sorted(ESSAYS_DIR.glob("*.md")):
        name = path.name
        # Skip dotfiles only. Every other *.md file is published.
        if name.startswith("."):
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        slug = derive_slug(path)
        title = (meta.get("title") or infer_title(body, path.stem)).strip()
        summary = (meta.get("summary") or "").strip()
        sort_key, display = normalize_date(meta.get("date"), path.stat().st_mtime)
        entries.append({
            "path": path,
            "slug": slug,
            "title": title,
            "summary": summary,
            "date_sort": sort_key,
            "date_display": display,
            "body": body,
        })
    # Newest first.
    entries.sort(key=lambda e: e["date_sort"], reverse=True)
    return entries


def remove_stale_dirs(keep_slugs: set[str]) -> None:
    """Remove previously-built <slug>/ subdirectories that are no longer present."""
    for child in HERE.iterdir():
        if not child.is_dir():
            continue
        if child.name in {"essays", ".venv", "__pycache__"}:
            continue
        # Only treat it as ours if it contains an index.html.
        if (child / "index.html").exists() and child.name not in keep_slugs:
            try:
                (child / "index.html").unlink()
                # Remove the directory if empty.
                try:
                    child.rmdir()
                    print(f"  - cleaned stale essay output: {child.name}/")
                except OSError:
                    # Non-empty (someone dropped extra files); leave the dir.
                    print(f"  - emptied stale essay output but dir not empty: {child.name}/")
            except OSError as e:
                print(f"  ! could not clean {child}: {e}", file=sys.stderr)


def main() -> int:
    print(f"build.py — scanning {ESSAYS_DIR}")
    entries = collect_essays()
    print(f"  found {len(entries)} essay(s)")

    keep = {e["slug"] for e in entries}
    remove_stale_dirs(keep)

    for e in entries:
        body_html = render_markdown(e["body"])
        page = render_essay_page(e, body_html)
        out_dir = HERE / e["slug"]
        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"  wrote {e['slug']}/index.html  ({e['title']!r}, {e['date_display']})")

    index_html = render_list_page(entries)
    (HERE / "index.html").write_text(index_html, encoding="utf-8")
    print(f"  wrote index.html (list page, {len(entries)} entries)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
