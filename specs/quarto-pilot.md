# Spec — Quarto pilot (refresher courses)

## Intent
- Migrate two EN refresher modules from hand-written HTML to **Quarto Markdown (`.qmd`)** as source of truth, while keeping GitHub Pages (legacy `main` /) working.
- Audience: agents and maintainers of `polytechnique-llga`.
- Outside brochure? no (pilot tooling only).

## Scope (pilot)
1. `courses/m1p1-refresher-statistics/`
2. `courses/m1p1-refresher-cs/`

EN only. Faithful content conversion (no pedagogical rewrite). Paper look via `assets/paper.css` + `assets/theme.js`. KaTeX via Quarto `html-math-method: katex`.

## Approach chosen
- **Source**: `index.qmd` per course (Pandoc/Quarto Markdown + fenced divs for `.def` / `.thm` / `.note` / `.proof` / `.ex` / `.sol` / `.recap`).
- **Published artifact**: commit rendered `index.html` next to the `.qmd` (legacy Pages — no Quarto GitHub Action required for the pilot).
- **Converter**: `tools/html_to_qmd.py` (HTML → preprocess math/`section` → `quarto pandoc` → `.qmd`).
- **Render**: `quarto render courses/<id>/index.qmd` (Quarto CLI ≥ 1.7), outputting `index.html` in place with paper shell includes (crumb, `main.paper`, footer, theme toggle).

## Outcomes
- Maintainers edit `.qmd`, then re-render HTML before merge.
- Live URLs unchanged:
  - https://knoel99.github.io/polytechnique-llga/courses/m1p1-refresher-statistics/
  - https://knoel99.github.io/polytechnique-llga/courses/m1p1-refresher-cs/

## Rebuild
```bash
# once: install Quarto CLI (https://quarto.org/docs/get-started/)
quarto render courses/m1p1-refresher-statistics/index.qmd
quarto render courses/m1p1-refresher-cs/index.qmd
```

Optional re-conversion from an HTML snapshot:
```bash
python3 tools/html_to_qmd.py courses/m1p1-refresher-statistics courses/m1p1-refresher-cs
```

## Done proofs
- [x] `.qmd` sources on `main` for both refreshers
- [x] `index.html` regenerated in place (root index links unchanged)
- [x] `assets/paper.css` + `assets/theme.js` wired; no FR/lang switcher
- [x] KaTeX inline + display math present in rendered HTML
- [x] `specs/quarto-pilot.md` present
- [x] Live Pages HTTP 200 after merge

## Caveats / follow-ups
- Quarto GitHub Action **not** wired yet (pilot commits built HTML). A later PR can add `quarto-dev/quarto-actions` and stop committing HTML if desired.
- Custom boxes stay as Pandoc fenced divs (`::: note`) rather than Quarto callouts — preserves `paper.css` class names.
- Code fences default to `python` after conversion; some blocks may be pseudocode.
- Quarto injects a small amount of syntax-highlight CSS; visual source of truth remains `paper.css`.
