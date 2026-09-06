# Spec — Quarto catalog migration (all courses)

## Intent
- Migrate **all** course pages under `courses/` from hand-written HTML to **Quarto Markdown (`.qmd`)** as source of truth, keeping GitHub Pages (legacy `main` / committed `index.html`) working.
- Extends the pilot in `specs/quarto-pilot.md` (refreshers statistics + CS) to the full catalog (~49 courses).
- Audience: agents and maintainers of `polytechnique-llga`.
- Outside brochure? no (tooling + course notes).

## Scope
Every directory under `courses/` with a paper-shell `index.html`. Pilot already done:
- `courses/m1p1-refresher-statistics/`
- `courses/m1p1-refresher-cs/`

All remaining courses (~47) converted in the catalog migration PR.

EN-facing notes; FR language strings in materials lines are normalized by the converter (`FR_FIXES`). Faithful content conversion (no pedagogical rewrite). Paper look via `assets/paper.css` + `assets/theme.js`. KaTeX via Quarto `html-math-method: katex`.

## Workflow (convert → render → commit)

```bash
# 1. Prefer original HTML backups so re-runs stay pure
#    tools/html_to_qmd.py reads /tmp/<slug>-index.html.bak if present
for d in courses/*/; do
  slug=$(basename "$d")
  [ -f "$d/index.qmd" ] && continue
  cp "$d/index.html" "/tmp/${slug}-index.html.bak"
done

# 2. Convert (multiple args OK)
python3 tools/html_to_qmd.py courses/<slug> ...

# 3. Render (batch 4–6 parallel to avoid OOM)
quarto render courses/<slug>/index.qmd

# 4. Commit both index.qmd and rendered index.html
```

Live URLs stay `https://knoel99.github.io/polytechnique-llga/courses/<slug>/` (Pages serves `index.html`).

## Converter (`tools/html_to_qmd.py`)
- Extract title / subtitle / `<main class="paper">`, unwrap `<section class="chapter">`, convert `\(...\)` → `$...$`.
- `quarto pandoc` HTML → Markdown (`markdown-smart+raw_html+pipe_tables-tex_math_dollars`).
- Post-steps: `fix_math_escapes`, `unescape_brackets_in_math`, map `` ``` code `` → `` ```python ``, `balance_check` on fenced divs.
- YAML shell: `theme: none`, `minimal: true`, KaTeX, `highlight-style: github`, injected token-color CSS (light + dark), crumb / `main.paper` / footer / `theme.js`.

## Pitfalls (do not regress)
1. **Pandoc bracket escape in math** — HTML→Markdown escapes literal `[` `]` inside `$...$` as `\[` `\]`. KaTeX then treats them as display-math delimiters (breaks `$\Omega = [0,1]$`, `$\mathbb{E}[X]$`). Fix: `unescape_brackets_in_math()` after pandoc. Display math uses `$$`, not `\[...\]`.
2. **`theme: none` + `minimal: true` highlight CSS** — Quarto emits `code span.*` classes but does **not** link/embed highlight color CSS. Keep `highlight-style: github` for intent; inject compact github-light + dark-mode rules with raised specificity (`div.sourceCode pre.sourceCode code span.*`) in the YAML header `<style>`.
3. **Never `color: unset` / `inherit` on `pre.sourceCode code span` in `paper.css`** — that beats token colors.
4. **`<pre class="code">` → language `code`** — Pandoc names the fence language `code`; Quarto only highlights real languages and would emit unhighlighted `<pre class="code">`. Converter remaps to `` ```python `` (pilot default; some SQL/pseudocode blocks are imperfectly highlighted).
5. **Re-run safety** — After a first render, `index.html` is Quarto output. Always keep `/tmp/<slug>-index.html.bak` (or git history) before converting again; the script prefers the bak when present.
6. **Fenced div balance** — `balance_check` fails the convert if `::: note` / `::: def` / … closers are unbalanced; fix systematically in the converter, do not ship broken `.qmd`.

## Rebuild (single course)
```bash
python3 tools/html_to_qmd.py courses/<slug>   # only if bak/original HTML available
quarto render courses/<slug>/index.qmd
```

## Done proofs
- [x] Every `courses/*/index.qmd` + rendered `courses/*/index.html` on `main`
- [x] Converter pitfalls documented here (+ pilot caveats retained)
- [x] Spot-check: math-heavy (`m1p1-probability-monte-carlo` / `m1p1-statistical-learning-theory`) — no `\[0,1\]` in math; KaTeX + paper crumb
- [x] Spot-check: light non-sci (`m1-sports` / `m1-langues`) — crumb + paper shell
- [x] Code courses: `sourceCode` + token color CSS present
- [x] Live Pages HTTP 200 after merge on sample course URLs

## Caveats / follow-ups
- Quarto GitHub Action **not** wired yet (commits built HTML). A later PR can add `quarto-dev/quarto-actions` and stop committing HTML if desired.
- Custom boxes stay as Pandoc fenced divs (`::: note`) rather than Quarto callouts — preserves `paper.css` class names.
- Some `` ```python `` blocks are SQL or pseudocode (acceptable; matches pilot).
