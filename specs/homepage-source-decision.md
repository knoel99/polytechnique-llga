# Homepage source decision (CdC)

1. The published homepage is **Extrapolons-only**: one Graph × LLM reading route.
2. Do **not** put Brochure vs Curriculum reconciliation, dual badges, ECTS debates, or source-key essays on the home page.
3. Official programme links appear once in the footer, labelled “Official programme (École Polytechnique)”, without resolving conflicts between official docs.
4. Links: programmes.polytechnique.edu LLGA page and msct.dix.polytechnique.fr/llga/wiki/.
5. The heavy Year 1 / Year 2 module list lives on `catalogue.html` (Full module index).
6. Catalogue lists Extrapolons note pages by period; it is navigation, not an enrolment catalogue.
7. Tone: open-source Extrapolons notes — never faculty voice; no invented UE codes; English only.
8. Progressive disclosure: hero → Start here → route → Coherence / Exit → Full module index → official footer.
9. `paper.css` / `theme.js` remain the visual and theme source of truth (dark + mobile).
10. This decision supersedes earlier homepage hedging that mixed Extrapolons reading advice with official-status adjudication.

## Post-merge verification (2026-09-07)

Closes the open “after Pages rebuild” test-plan items of PRs #25 and #26:

- [x] Live <https://knoel99.github.io/polytechnique-llga/> serves the single Graph × LLM map home (hero → Start here → route → Maps and index).
- [x] Full module list on `catalogue.html`; official programme links in the footer only.
- [x] No French text and no FR/EN switcher on the published home.

## 2026-09-07 update

`catalogue.html` is deleted; the home curriculum tree (one column, `specs/path-preselection.md`)
is now the single full module list. Items 5–6 above are superseded; item 8's "Full module index"
step is the home tree itself.
