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
| `path-preselection` | Home = full one-column tree with 3 path buttons (Full / Graph×LLM / AI systems); “Extrapolons” removed from all published pages; `curriculum.html` merged into home | #29 | implemented |
| `coherence-2ans` | Two-year pedagogical coherence (lot E) | #11 | implemented |
| `clarity-lot-d1-refreshers` | Clarity: science refreshers + ML entry (lot D1) | #8 | implemented |
| `clarity-lot-d2-p1` | Clarity: P1 science modules (lot D2) | #9 | implemented |
| `clarity-lot-d3-p2-m2` | Clarity: P2 Graph/NLP/OT + M2 LLM entry (lot D3) | #10 | implemented |
| `clarity-lot-d4-rest` | Voice purge + clarity, remaining science modules (lot D4a/b) | #12, #13, #14 | implemented |
| `quarto-pilot` | Quarto Markdown pilot (refreshers stats + CS) | #16 | implemented |
| `quarto-migration` | Quarto source (`.qmd`) for all remaining courses | #22 | implemented |
