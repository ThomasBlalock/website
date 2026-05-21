---
name: hierarchical-agents
description: Decompose a build into independent contract-driven subdirectories, each handed to a fresh AI agent. Use when a task has 2–7 clearly separable parts (tabs of a site, microservices, modules of a CLI) so that downstream agents can work in parallel with only the context they need. The top-level agent writes shared scaffolding (routing, shared styles, contracts) — never the component implementations.
---

# Hierarchical agents

A pattern for handing big tasks off to smaller, parallel coding agents while keeping the whole tree coherent.

## When to use this

You're about to build something with multiple roughly-independent parts — tabs of a site, microservices behind a gateway, modules behind a CLI, plugins behind a host, levels of a game. The parts share style and routing but don't need to know each other's internals.

**Trigger if all four are true:**

1. The work decomposes into **2–7 parts** that can be specified independently.
2. Each part has a **clear contract** (URL, file output, function signature) the rest of the tree depends on.
3. The parts are **roughly independent** — they share assets and conventions, not logic.
4. Each part is large enough to **earn its own context window** — i.e., enough work that loading the entire codebase into one agent's context would be wasteful.

If any of those fails, just do the task inline. This pattern has overhead — don't pay it for a task you could finish in one pass.

## What the top-level agent writes

Only the *stitching*. Everything else is a contract a downstream agent fulfills.

| Top-level agent writes | Top-level agent does NOT write |
| --- | --- |
| Routing / gateway / dispatcher config | The component implementations |
| Shared assets (CSS tokens, design language docs, nav snippets, base layouts) | Component-specific HTML/CSS/JS |
| Per-subdirectory `README.md` contracts | The deliverables those contracts describe |
| A boilerplate / starter template if helpful | Anything beyond the boilerplate |
| Build orchestration (docker-compose, Makefile) | Component-specific build steps |
| Root-level README explaining the architecture | Component documentation |

When you're tempted to "just fill in the home page real quick," stop. That's the exact context-pollution this pattern is built to prevent.

## Directory shape

```
repo/
  shared/                # everything every component depends on
    styles.css           # design tokens, layout primitives
    STYLE.md             # design language doc, written for the next agent
    nav.html             # snippets components include
    BOILERPLATE.html     # starter template (optional)
  componentA/
    README.md            # the contract — see "Contract format" below
    (downstream agent delivers the rest)
  componentB/
    README.md
    (...)
  componentC/
    README.md
    (...)
  <gateway-config>       # nginx.conf, gateway.yml, Makefile — whatever routes/dispatches
  README.md              # arch overview, points at the skill
```

## Contract format

Each subdirectory's `README.md` is the only thing a downstream agent should need to read. Write it like you're commissioning a freelancer who's never seen the codebase before.

A contract has six sections. Keep each short.

```markdown
# <Component name>

## What you're building
The one-paragraph deliverable. What it is, what URL/path it serves, who reads it.

## Deliverable contract
Exactly which files must exist where, what URLs must work after delivery,
and which absolute paths or function signatures the rest of the tree expects.

## Inputs
The files and data you may read. Be specific: `../profile.json`, `./essays/*.md`,
`../shared/styles.css`. Include outdated/secondary sources but mark them as such.

## Style integration
How to inherit the visual language. "Include `/shared/styles.css`. Read
`../shared/STYLE.md` first. Use the nav snippet at `/shared/nav.html` via the
pattern in `/shared/BOILERPLATE.html`." Keep this paragraph identical across
components so the global look stays coherent.

## Constraints / guidance
Anything specific to *this* component — length, tone, edge cases, what NOT
to do, what to surface, what to hide. This is where the contract earns its
keep.

## Out of scope
What this component must NOT do. Prevents bleed (e.g., "do not render
markdown — that's the essays component's job").
```

## Style integration (write this once, paste everywhere)

The shared paragraph that goes in every contract's "Style integration" section. Keeps designs from drifting:

> Include `/shared/styles.css` via `<link rel="stylesheet" href="/shared/styles.css">`. Read `/shared/STYLE.md` *before* you start — it defines the typography scale, the spacing rhythm, the accent color, and the section-block primitive used across the site. Mount the shared nav by including the empty `<header id="site-nav"></header>` slot and `<script src="/shared/shell.js" defer></script>` — the script fetches `/shared/nav.html` and injects it (and marks the current tab). Use `/shared/BOILERPLATE.html` as your starting `index.html` and replace its `<main>`.

## Boilerplate as the contract's binding interface

If your shared assets include a `BOILERPLATE.html`, downstream agents become much more reliable: they start from a known-good file and edit a single region rather than reconstructing the page from prose. Write the boilerplate to include:

- All shared `<link>` and `<script>` tags pre-wired
- The nav slot pre-placed
- A footer slot pre-placed
- A `<main>` (or equivalent) with one comment line: `<!-- replace this block -->`
- The minimum metadata (`<title>` placeholder, viewport, charset)

This turns "make a webpage" into "fill in one element," which is much harder to get wrong.

## Why this pattern beats one big agent

- **Token economy.** Each subagent loads only the component's slice plus shared/. The top agent never reads component internals. A 50-file repo becomes five 10-file working sets.
- **Parallelism.** Independent subagents can run concurrently.
- **Documentation as a byproduct.** The README.md contracts *are* the architectural documentation. They don't drift because the agent reads them every time.
- **Failure isolation.** A broken component blocks only its own tab; the rest of the tree stays green.
- **Quality.** Each agent gets to focus. No one component is competing with the others for attention.

## Why it can backfire

- **Contract churn.** If the contracts keep changing, downstream agents keep rebuilding. Lock the contracts before dispatching.
- **Hidden coupling.** Components that "should be independent" sometimes aren't. Watch for shared mutable state, shared schema, hidden ordering requirements — surface those into `shared/` or the contract or the architecture has lied to you.
- **Premature decomposition.** If a component is small enough that you could finish it in the same context window as the stitching, do it inline. The pattern is for size, not as a default.
- **Over-elaborate contracts.** A contract that takes longer to read than the component takes to build is overhead. Keep contracts tight.

## A worked example: a tabbed website

```
src/
  shared/
    styles.css      STYLE.md      nav.html      shell.js      BOILERPLATE.html
  home/      README.md → "deliver /home/index.html that renders at /, using profile.json"
  resume/    README.md → "deliver /resume/index.html that renders at /resume from profile.json"
  projects/  README.md → "deliver /projects/index.html with per-project detail from profile.json"
  essays/    README.md → "deliver /essays/index.html (list) + /essays/<slug>/index.html (rendered)
                          from markdown files in ./essays/. Auto-discover; do not hardcode the list."
  contact/   README.md → "deliver /contact/index.html from profile.json contact{}"
nginx.conf            # routes / → /home/, plus the other tabs
docker-compose.yml    # one nginx container, mounts src/ and images/
```

The top-level agent writes `styles.css`, `STYLE.md`, `nav.html`, `shell.js`, `BOILERPLATE.html`, the six README contracts, the nginx config, and the docker-compose file. Then five fresh agents — one per tab — fill in the components in parallel.

## Heuristics

- **2 ≤ N ≤ 7.** Fewer than 2, just write it. More than 7, group into nested hierarchies (each subdirectory may itself contain a hierarchy).
- **A subagent should be able to deliver its component with only the contents of its own subdirectory plus `shared/`.** If it needs to read peer components, you've drawn the lines in the wrong place.
- **Same style integration paragraph in every contract.** Drift here breaks visual coherence.
- **When in doubt, push specificity into the contract**, not into the prose someone might read once.
