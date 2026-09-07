# AGENTS.md — Spec-Driven / BMAD (light) gates for polytechnique-llga

This repository is an **HTML course-notes site** (GitHub Pages), not an application monorepo.
We encode a **Spec Kit–compatible** and **BMAD-inspired** base (spec → plan → implement → prove), without requiring the Spec Kit / bmad-speckit-sdd-flow CLI.

## Principles

1. **Contract before large rewrite** — any new module or major refactor starts with a contract in `specs/` (see template).
2. **Proofs before “done”** — a PR is “done” only if the gates below are checked in the PR description.
3. **No invented UE codes** — outside the brochure = explicit badge, no fake SynapseS codes.
4. **EN only (until further notice)** — published site source of truth is **English at the repository root**. No FR mirror, no FR/EN language switcher. See `specs/en-only.md`.
5. **Paper look** — `assets/paper.css` is the visual source of truth; light “LaTeX” mode must not regress.

## Mandatory gates (Definition of Done)

Before merging a module / CSS refactor:

- [ ] **Contract**: `specs/<module-id>.md` present (or updated) for a new course / rewrite > ~one screen.
- [ ] **Pages**: `courses/<id>/index.qmd` (Quarto source) + rendered `courses/<id>/index.html` (English, at site root). See `specs/quarto-migration.md`.
- [ ] **Index**: module reachable from root `index.html` — the home links `catalogue.html` for the full per-period list (see `specs/homepage-source-decision.md`); honest status.
- [ ] **CSS**: dark (`prefers-color-scheme` / `data-theme`) + mobile (no blocking horizontal overflow; tables / code / KaTeX scrollable) checked on one course page + the index.
- [ ] **Theme**: `assets/theme.js` loaded; toggle localStorage OK; UI strings in English.
- [ ] **Pedagogy**: ≥ 6 exercises on science modules (non-science pages exempt, see `specs/non-science-pages.md`); NumPy primary if NN/ML module; full sentences in English.
- [ ] **Smoke**: open EN pages locally (or Pages preview); KaTeX and `.def`/`.thm`/`.note` boxes readable in dark.
- [ ] **No FR switcher**: no “Français” / lang-toggle links in published HTML.
- [ ] **Mechanical proof**: `python3 tools/check_gates.py` passes (contract index, Quarto sources, theme, FR links, exercises, index coverage).

## Optional Spec Kit / BMAD tooling

This repo does **not** auto-install Spec Kit. For a tooled SDD flow on a dev machine:

```bash
# Spec Kit (GitHub / specify CLI) — if you already use it elsewhere
# https://github.com/github/spec-kit
# Example:
#   uvx --from git+https://github.com/github/spec-kit.git specify init
# Then point artefacts at this repo’s specs/.

# BMAD + Spec Kit SDD flow (if available in your environment):
#   npx bmad-speckit-sdd-flow
```

If the CLI is not installed, **this file’s gates + `specs/` contracts are enough** — default mode for Cursor agents on this repo.

## Recommended agent workflow (BMAD light)

| Phase | Output |
|---|---|
| **Spec** | Fill / amend `specs/<id>.md` (goals, outside-brochure?, outline, proofs). |
| **Plan** | List files touched (course HTML, root index, CSS/JS if needed). |
| **Implement** | Write HTML + links; no CloudAgent unless explicitly requested. |
| **Prove** | Run `python3 tools/check_gates.py`; check the gates; paste the proof summary in the PR. |

## Key files

- `assets/paper.css` — paper style, dark, mobile
- `assets/theme.js` — persistent theme toggle (English aria-labels)
- `specs/README.md` — contract index (with merged-PR traceability)
- `specs/_template-module.md` — contract template
- `specs/en-only.md` — EN-only site policy
- `tools/check_gates.py` — runnable mechanical gates (BMAD-light “Prove”)
