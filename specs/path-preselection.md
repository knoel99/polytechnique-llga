# Contract — path preselection on the home tree + de-branding

## Intent

Three decisions, applied at once:

1. **"Extrapolons" is not an app name** — the word disappears from every published page.
   The site presents itself as *independent study notes for the LLGA track*. Internal
   `specs/` documents keep the historical voice vocabulary; published HTML never does.
2. **The full curriculum tree lives on the homepage, in one column.** `curriculum.html`
   is deleted; the homepage is the single structural view.
3. **Three buttons preselect the tree:**
   - **Full curriculum** — every option visible (default, no-JS fallback).
   - **Graph × LLM route** (existed) — generative spine: Deep Learning (P1), Probability
     for ML, Statistical Learning Theory; P2 elective Multimodal Generative AI; M2
     Advanced GNN, Control in Generative AI, Advanced Topics in LLMs, Graph Generative
     Models + shared MLOps / Security / Explainability.
   - **AI systems route** (new) — deployment spine: Signal Processing, Computer Vision,
     DBMS (P1); Deep Learning via the P2 variant; P2 elective Optimization for AI; M2
     Speech Technology, Computer Vision Applications, Real-time AI + shared MLOps /
     Security / Explainability.

Officially mandatory items are never dimmed: a path preselects inside the official
`Choose N` groups and the TBC slots, it never overrides requirements. Paths are this
site's reading guidance; the badge legend says so.

## Mechanics

- Elective tree items carry `data-p` (space-separated route tags; `data-p=""` marks an
  elective in no route — it dims under every route). Selecting a path sets `data-path`
  on the tree container; non-matching elective items dim to 30 % opacity. **Every `li`
  inside a choice group carries a marker** (gated), so the bright count per group can
  never exceed the official quota. Pure CSS + a 10-line inline script; without JS the
  full tree shows.
- Both routes include Deep Learning, in different periods (P1 route 1, P2 variant route 2)
  so each preselection stays feasible against the official `Choose 3` / `Choose 1` rules.
- `Mandatory (brochure)`-style conflicts stay settled per `specs/competency-tree.md`.

## Revision 2 (2026-09-07) — exact quotas, refreshers, official docs

- **Quota fix**: in the first version, unmarked electives stayed bright on every route
  (inflating the visible count beyond `Choose N`), and the AI-systems route preselected
  2 items in the `Choose 1` group. Now: every elective in a choice group carries
  `data-p` (empty = in no route); gates enforce **exactly 3** bright per route in P1
  choose-3 and **exactly 1** in P2 choose-1. AI systems: P2 choice = Deep Learning
  (P2 variant); Optimization for AI demoted to no-route.
- **Refreshers in the tree**: Refresher in Statistics + Refresher in Computer Science
  (official pre-programme, badge “Pre-programme”) and Refresher Neural Nets
  (independent, “Off-curriculum support”), at the top of M1 · P1.
- **Official documentation section on the home page**: programme page, course content,
  LLGA wiki + curriculum page (single structural source), SynapseS catalog 2026–2027,
  application procedure — all URLs verified HTTP 200.

## Plan (files)

| File | Change |
|---|---|
| `index.html` | Full one-column tree + 3 path buttons + inline preselection script |
| `curriculum.html` | Deleted |
| `catalogue.html` | De-branded; curriculum links → home tree |
| `coherence-2years/`, `exit-capabilities/`, `assets/ATTRIBUTION.md` | De-branded |
| `courses/*` (.html + .qmd) | Phrase map: "Extrapolons …" → neutral wording (ids renamed too) |
| `assets/paper.css` | `.tree-nav` button styles + `data-path` dim rules; `.tree-cols` removed |
| `tools/check_gates.py` | Published pages `Extrapolons`-free; curriculum.html absent; home has tree + 3 buttons |

## “Done” proofs (check)

- [x] No “Extrapolons” in any published HTML/QMD (mechanical gate)
- [x] `curriculum.html` gone; no internal link targets it; full tree on home, one column
- [x] 3 path buttons; each path preselects a feasible set (Choose 3 / Choose 1 respected;
      DL-once satisfied via P1 for Graph × LLM, via the P2 variant for AI systems)
- [x] Mandatory items never dimmed; no-JS shows the full tree
- [x] `python3 tools/check_gates.py` passes (353/353); static link/HTML checks pass
- [x] Rev 2: quotas exact — both routes show exactly 3 bright in P1 choose-3 and 1 in P2 choose-1, 0 unmarked electives (gated)
- [x] Rev 2: refreshers listed in the tree; official documentation section with 5 verified links
- [x] Rev 3: TBC glossed on its own line before the Slot TBC legend entry; catalogue.html deleted with zero remaining links; one line per non-scientific module (gated, 402/402)
- [ ] Dark/mobile smoke (browser) — pending post-merge check (no browser in the build
      environment; dim/badge styles use theme variables only)

## Revision 3 (2026-09-07) — TBC glossary, catalogue deleted, one module per line

- Legend: new line before the Slot TBC explanation — “TBC = ‘to be confirmed’”.
- `catalogue.html` deleted (last duplicate structure page): the home tree is the full module
  index; coherence / exit maps remain the only satellite pages.
- Non-scientific modules get one line each in the tree: M1 · P1 sub-list
  (Strategy/Marketing, Sports, Humanities, Languages) and M2 transverse split
  (Humanities — 8 ECTS total with languages and sports / Languages / Sports).
