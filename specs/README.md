# specs/ — module contracts (light Spec-Driven)

Each **new course** or **major rewrite** adds or updates `specs/<module-id>.md` before (or in the same PR as) the HTML.

See also `AGENTS.md` (BMAD / Spec Kit gates) and `specs/_template-module.md`.

**Language policy:** published site is **English only at repository root** until further notice (`specs/en-only.md`). Do not add a FR mirror.

## Contracts present

Every contract maps to merged PR(s) — the "Prove" half of the BMAD-light loop. Mechanical gates are runnable: `python3 tools/check_gates.py`.

| ID | Title | PRs | Status |
|---|---|---|---|
| `en-only` | Promote EN to root; remove published FR | #15 | implemented |
| `m1p1-refresher-neural-nets` | Refresher Neural Nets (outside brochure) | #1 | implemented |
| `toc-double-numbering-fix` | Fix double TOC numbering on course pages | #2 | implemented |
| `exit-capabilities` | Exit capabilities / industry synthesis questions | #3, #4, #5 | implemented |
| `non-science-pages` | Non-science pages (management, transversal, internships, ethics) | #6 | implemented |
| `homepage-redesign` | Homepage redesign + illustrations | #7 | implemented |
| `homepage-source-decision` | Extrapolons-only home; catalogue off home; official links in footer | #25, #26 | implemented |
| `competency-tree` | Curriculum tree (mandatory vs choices); wiki = single structural source; brochure retired from structure pages | #28 | implemented |
| `path-preselection` | Home = official identity header (LLGA MScT title/subtitle, sommaire, official description + “What is this website?”), full one-column tree with 3 path buttons + justifications, official documentation, “After the master” careers overview; satellite pages merged into home; ATTRIBUTION.md deleted | #29–#34 | implemented |
| `coherence-2ans` | Two-year pedagogical coherence (lot E) | #11 | implemented |
| `clarity-lot-d1-refreshers` | Clarity: science refreshers + ML entry (lot D1) | #8 | implemented |
| `clarity-lot-d2-p1` | Clarity: P1 science modules (lot D2) | #9 | implemented |
| `clarity-lot-d3-p2-m2` | Clarity: P2 Graph/NLP/OT + M2 LLM entry (lot D3) | #10 | implemented |
| `clarity-lot-d4-rest` | Voice purge + clarity, remaining science modules (lot D4a/b) | #12, #13, #14 | implemented |
| `quarto-pilot` | Quarto Markdown pilot (refreshers stats + CS) | #16 | implemented |
| `quarto-migration` | Quarto source (`.qmd`) for all remaining courses | #22 | implemented |
| `stats-concise-illustrations` | Refresher Statistics: prose condensed (~-16% words), 9 new SVG illustrations (13 total) | #35 | implemented |
| `theorem-box-framing` | Normed box framing (def tinted, thm/prop ink-left frame, ex bar) + aerated proofs (site-wide CSS + stats qmd) | #36 | implemented |
| `stats-clear-prose` | Stats page: full sentences everywhere (no note-taking style) + one equation per line with connecting prose | #37 | implemented |
| `display-math-spacing` | Fix doubled display-math margins (nested .katex-display in .math.display); 2.6rem → 1.15rem | #38 | implemented |
| `hours-and-progression` | Session plan per science module summing to the official hours, non-decreasing levels, in-class prose calibrated to 100–320 words/h, graded exercises (★/★★/★★★); tools `check_progression.py`, `renumber_chapters.py`, `grade_exercises.py`, `render.py`, `programme_table.py`, `cross_refs.py`; home programme table 2026–2027 | — | implemented |
| `front-redesign` | Projector contrast (text ≥ 7:1 light and dark), colour-coded boxes, top bar + side contents always reachable, mobile drawer and stacked fiche tables, airy prose gate `check_airiness.py` (A1–A3) applied to every page | — | implemented |
| `coherence-objectives` | Coherence of all 49 pages with the master's objectives O1–O8: per-page reading, five-lens analysis (objectives, prerequisites, redundancy/notation, errors, capstones). October archive in `specs/coherence-2026-10/`. Current scores in `specs/coherence-objectives-report.md` | — | report shipped; large rewrites backlogged |
| `coherence-objectives-report` | O1 to O8 score matrix for the 40 science courses, fix register, and backlog. Checked by `tools/check_coherence_map.py` | — | report shipped; large rewrites backlogged |
| `projects-and-assessment` | Projects and assessment section on every science page (≥ 2 solo, ≥ 2 group subjects, written-exam proposal, rubric); end-of-year projects page `projects/` (Year 1 and Year 2); notation page `notation/` | — | implemented |
