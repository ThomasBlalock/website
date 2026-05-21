# thomasblalock.com

A single tabbed website. The repo is organized so each tab is built independently by a fresh AI agent from a short contract in its own subdirectory. This top-level README is the architecture overview; the design pattern is documented in [`.claude/skills/hierarchical-agents/SKILL.md`](.claude/skills/hierarchical-agents/SKILL.md).

## Tabs

| URL | Subdirectory | Contract |
| --- | --- | --- |
| `/`          | `src/home/`     | [src/home/README.md](src/home/README.md) |
| `/resume/`   | `src/resume/`   | [src/resume/README.md](src/resume/README.md) |
| `/projects/` | `src/projects/` | [src/projects/README.md](src/projects/README.md) |
| `/essays/`   | `src/essays/`   | [src/essays/README.md](src/essays/README.md) |
| `/contact/`  | `src/contact/`  | [src/contact/README.md](src/contact/README.md) |

Each subdirectory's `README.md` is the contract for the sub-agent that fills it in. Sub-agents only need their own directory plus `src/shared/`.

## What lives where

```
.
├── src/
│   ├── shared/                  # shared design language — the only "code" the top-level agent writes
│   │   ├── styles.css           # design tokens + layout primitives (top nav, .block, .tag, etc.)
│   │   ├── STYLE.md             # design language doc — sub-agents MUST read this first
│   │   ├── nav.html             # the top-nav snippet, injected by shell.js
│   │   ├── shell.js             # mounts nav.html into <header id="site-nav"></header>
│   │   └── BOILERPLATE.html     # starter template — sub-agents replace its <main>
│   ├── home/        README.md   # contract; sub-agent delivers index.html (+ optional page.css)
│   ├── resume/      README.md   # contract; sub-agent delivers index.html (+ optional page.css)
│   ├── projects/    README.md   # contract
│   ├── essays/      README.md   # contract; ALSO contains essays/ — drop new .md files here
│   │   └── essays/
│   │       └── web4.md          # the inaugural essay; do not edit the prose
│   └── contact/     README.md   # contract
│
├── images/                      # photos exposed at /images/ via a sibling mount
├── profile.json                 # source-of-truth content dump — every tab reads this
├── Blalock_resume.pdf           # OUTDATED reference for the resume tab's structure
├── nginx.conf                   # route map: / → home/, /resume/, /projects/, /essays/, /contact/
└── docker-compose.yml           # one container; mounts src/, images/, nginx.conf
```

## Run it

```bash
docker compose up -d              # starts nginx on http://localhost:8080
docker compose ps                 # see status
docker compose logs -f site       # tail logs
docker compose down               # stop
```

Tabs whose sub-agents have not yet delivered will return a friendly "Not built yet" page until their `index.html` exists.

Edits to any file in `src/`, `images/`, or `nginx.conf` are picked up live (mounts are read-through). After editing `nginx.conf`, run `docker compose restart site`.

## Dispatching sub-agents

To build a tab, hand its `README.md` to a fresh agent with no other context. Suggested prompt:

> Read `src/<tab>/README.md` end-to-end, then `src/shared/STYLE.md`, then `src/shared/BOILERPLATE.html`. You may also read `/profile.json` and anything else the README points at. Deliver the files the contract describes, in this directory. Do not modify anything outside `src/<tab>/`. Do not modify `src/shared/`. Do not modify any other tab's directory.

For the essays tab specifically: the README permits a build step (e.g. `build.py`); if you produce one, place it in `src/essays/` and document how to run it at the top of the file.

## Hierarchical agents

The decomposition pattern used here is documented as a project-level skill at [`.claude/skills/hierarchical-agents/SKILL.md`](.claude/skills/hierarchical-agents/SKILL.md). Read it before adding a new tab — there's a contract template, a `BOILERPLATE.html` pattern, and a set of heuristics for when to use this approach vs. just doing the work inline.
