# thomasblalock.com — design brainstorm

The brief from `profile.json`: distinctive, content-dense, opinionated, no devfolio template, no buzzwords, no glassmorphism. Centerpiece is what Thomas is *building right now* — ASI and Sidequest. Everything else (research, awards, military) is supporting evidence. Inspired by personal sites that are unmistakable in one visit: sive.rs, Tufte, Bret Victor's worrydream, Maggie Appleton's garden, gwern.net, Andy Matuschak's notes, brutalist single-pagers, and the old "homepages" of academic legends.

---

## Candidate concepts

### 1. ASI Terminal — the site IS an Agent Service
The whole site is a live well-known document. A visitor lands on what looks like a terminal/agent runtime. They `POST /search` natural-language queries ("AI agent infrastructure", "neural architecture researcher", "someone who built malware"), and the site responds with Thomas-as-callable-service: a JSON-ish card describing the relevant facet of him, plus a `next: tool_calls` block. The footer hosts the actual `/.well-known/mcp.json`-style payload. The site is not *about* Web 4.0 — it's a worked example. Maximal on-brand with his thesis. Memorable in one visit.

### 2. The Range Atlas — a hand-drawn cartographic map of disciplines
The "themes_to_surface" list names *range* as the headline. Visualize it literally. A single-screen old-explorer map with named regions: Hardware Frontier (EEG, rover), Infrastructure Coast (ASI, MCP), Policy Highlands (NATO space deterrence), Consumer Plains (Sidequest), Research Mountains (FINs, Informed ML), Cyber Wilds (agentic malware). Each "city" pin opens a card with the project. Coastlines, compass rose, faux longitude lines. The metaphor sells the range better than any bullet list.

### 3. Editorial single-page
Black & white & one accent. Strong serif headline, monospace metadata, a sharp typographic grid. Sections: now / ventures / research / projects / background. The "creativity" is in restraint — typography, hierarchy, density. Every section has a "what" + "why it mattered" line. The kind of site where the design fades and the content lands.

### 4. Footnote essay (Tufte sidenotes)
One short paragraph in the center of the page does the whole job. The interesting nouns ("Agent Service Index", "spear-phishing malware", "NATO space deterrence wargame", "P300 speller", "Air Force Academy") expand into Tufte-style sidenotes in the margins on hover/tap. The visitor reads at their own depth — the page rewards curiosity instead of demanding scroll. Lo-fi, paper-feeling, monochrome.

### 5. Bootstrap ladder site
A vertical T₁ → T₅ ladder borrowed straight from the web4 essay. Each rung unlocks a piece of the page (his ventures get built in front of you in the order an agent would compose them). Self-compiling site for a self-compiling internet.

### 6. Composition graph
SVG network of all his work as nodes; edges encode actual technical lineage (FINs → Airlift RL → Ops Research role; Informed ML → ASI ranking thesis; BCI hardware → Rover RL → autonomous agent comfort). Hover a node, see the card. The shape of the graph IS the bio.

### 7. Notebook page
Torn-from-a-Moleskine aesthetic. Sketches, scribbles, arrows between ideas. Feels like the inside of his head. Hand-lettered hero. Risk: hard to keep current.

### 8. Now-page (sive.rs)
Single column, monospace, dense, paragraphs. Updates dated. No nav. The least-design-y choice; relies entirely on writing quality.

### 9. Trading-card deck
Each venture / project / research line is a physical-feeling card. Drag, flip, fan. Playful, but risks looking like a portfolio template.

### 10. Brutalist newspaper
NYT-style front page. Thomas as the lede, three columns, ASCII rules. Bold but heavy-handed.

### 11. Talk to Thomas
A chat UI keyed to a small static knowledge base. Visitor types questions, gets canned-but-real answers in his voice. Demos his comfort with agentic systems. Risks feeling like every AI demo site of 2024.

### 12. Inverted dossier
The page reads like a classified intelligence brief on a person. Redaction bars, codenames, headers like CLASSIFICATION / SUMMARY / ASSOCIATES. Plays the Air Force angle straight into the design. Could land or could feel cosplay-y.

---

## Selections to build

Picking four with deliberate spread across the creativity axis:

| # | Slug | Concept | Bucket |
|---|---|---|---|
| 1 | `site-1-asi-terminal/` | **#1 ASI Terminal** — site as an Agent Service | super creative |
| 2 | `site-2-range-atlas/`  | **#2 Range Atlas** — cartographic map of disciplines | creative, different angle |
| 3 | `site-3-editorial/`    | **#3 Editorial** — typographic single-page | normal |
| 4 | `site-4-footnote-essay/` | **#4 Footnote essay** — Tufte sidenote bio | creative yet simple |

Each lives in its own folder and shares `../images/`.
