# Contract — LLGA curriculum tree & single structural source

## Intent

Stop the brochure-vs-official-site ambiguity for good, make the homepage readable at a glance,
and give the track a visible **curriculum tree** (mandatory modules vs choices), as clear as the
official brochure but honest about what is official and what is Extrapolons guidance.

## The decision (single, final — no reconciliation essays anywhere)

1. **One structural source: the official LLGA curriculum wiki**
   (<https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum>), complemented by the
   official programme page (140 ECTS, two years). It is the only authority used for: mandatory
   modules, choice groups (“choose 3 of 10”), periods, internships, ECTS.
2. **The brochure is no longer cited as a competing structure.** Structure pages (home,
   `curriculum.html`, `catalogue.html`, coherence, exit capabilities) never mention the brochure.
   Per-module provenance sections inside course pages keep citing documents factually
   (“announced in the MSc&T brochure, official description not yet published”) — they annotate one
   module, they never define the track.
3. **Where the wiki is silent (M2 · P2), the site says exactly that** — “not yet defined — see the
   wiki” — and Extrapolons coverage of announced themes is labelled as Extrapolons coverage. No
   invention, no hedging.
4. **Badge vocabulary is fixed site-wide:**
   `Mandatory` = official requirement · `Choose N` = official elective group ·
   `Slot TBC` = announced but not yet in the official lists ·
   `Route` = Extrapolons recommended path · `Extrapolons support` = off-curriculum help page.
5. **Homepage shows the tree, not a prose route.** The 7-step reading route moves to
   `curriculum.html`; the homepage keeps: hero → curriculum at a glance (compact tree) →
   Start here (readiness checks) → maps row → footer.

## Official structure (wiki, 2026-09 snapshot)

- **M1 · P1** — Mandatory: Machine Learning. Choose 3 of: DL*, Signal Processing*, Emerging ML*,
  Computer Animation, Image Analysis & Computer Vision, TDA, Shapes, Probability (Monte Carlo),
  DBMS, Statistical Learning Theory (*recommended). Deep Learning is required once, in P1 or P2.
  Non-scientific mandatory: strategy/marketing, sports, humanities, languages.
- **M1 · P2** — Mandatory: Reinforcement Learning & Autonomous Agents; Graph ML for Generative AI;
  Intro to Text Mining & NLP. Choose 1 of: Multimodal GenAI*, Statistics in Action*, Deep Learning
  (P2 variant)*, Optimal Transport*, Optimization for AI, Responsible AI & Sustainability,
  Advanced Deep Learning, Image Synthesis, Social Media (probabilistic). Non-scientific
  mandatory pair: entrepreneurship or innovation case studies.
- **M1 · P3** — Research-oriented internship (20 ECTS). Mandatory.
- **M2 · P1** — Official core: Large Language Models; Analysis & Deep Learning on Geometric Data.
  Announced (slot TBC): Privacy & Uncertainty; Boosting → Foundation Models; Control in Generative AI.
- **M2 · P2** — Official list not yet published. Extrapolons coverage of announced themes:
  ML Ops/LLM Engineering*, Security & Robustness*, Graph Generative Models*, Explainability/
  Security/Privacy of LLMs*, Speech Technology, Advanced Topics in LLMs. Also announced (slot TBC):
  Computer Vision Applications; Real-time AI in Video Games.
- **M2 transverse** — Transverse project (8 ECTS); ethical-issues seminar (6 ECTS); humanities/
  languages/sports (8 ECTS). Mandatory. — **M2 · P3** — End-of-studies internship (24 ECTS). Mandatory.

## Plan (files)

| File | Change |
|---|---|
| `curriculum.html` (new) | Full tree + Extrapolons route (ex-home 7 steps) + common experiment |
| `index.html` | Compact tree replaces the 7-step route; hero tightened |
| `catalogue.html` | Official badges (Mandatory / Choose N / Slot TBC) + single-source lead + legend |
| `coherence-2years/index.html`, `exit-capabilities/index.html` | Leads cite the wiki, not the brochure; `off-brochure` badges retired |
| `courses/*` | Breadcrumb provenance tags normalized: “(brochure)” → “(announced)” |
| `assets/paper.css` | `.tree` styles + `.badge.choice` / `.badge.tbc` (dark + mobile) |
| `AGENTS.md`, `specs/README.md`, `tools/check_gates.py` | Principle 6, index row, mechanical checks |

## “Done” proofs (check)

- [x] Structure pages contain no “brochure” wording (mechanically checked)
- [x] `curriculum.html` exists, linked from home; tree lists every official slot with badges
- [x] M2 · P2 shown as “not yet defined” + Extrapolons coverage labelled
- [x] Homepage: compact tree replaces the 7-step route; hero tightened
- [ ] Dark + mobile smoke (browser) — **pending post-merge check** (no browser available in the build environment; static checks passed: HTML balanced, 0 broken internal links, all badge classes defined in `paper.css`, tree CSS uses theme variables only)
- [x] `python3 tools/check_gates.py` passes (336/336)
