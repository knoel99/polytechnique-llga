# Contrat — Encadrement normé def/thm + preuves aérées

## Intent
Demande utilisateur 2026-09-07 : appliquer des **normes d'encadrement** aux définitions et théorèmes (corps nu auparavant), et **aérer les preuves** (interligne, sauts de ligne entre étapes).

## Périmètre
- `assets/paper.css` (partagé par toutes les pages de cours) :
  - `.def` = fond grisé (`--toc-bg`) + filet fin (`--hair`), padding `.75–.8rem` ;
  - `.thm` / `.prop` = encadré `--rule` + **liseré gauche 3px encré** (`--ink`), corps italique conservé ;
  - `.ex` = barre gauche 3px `--rule` (hiérarchie légère, sans cadre) ;
  - `.proof` = non encadré (tradition) mais **aéré** : `line-height: 1.75`, marges `1.2/1.5rem`, `p { margin: .7rem }` ;
  - marges générales des encadrés 1.15 → 1.4rem ; adaptation mobile (padding réduit ≤ 40rem) ;
  - variables existantes uniquement → dark mode et impression suivent automatiquement.
- `courses/m1p1-refresher-statistics/index.qmd` : sauts de ligne (paragraphes) entre les étapes des preuves multi-étapes (1.3, 2.3, 2.4, 4.2, 4.3, 4.4, 6.2, 7.1, 7.2, 7.3, 10.1, 10.4) ; les preuves courtes ou déjà structurées par des maths affichées restent inchangées.

## Hors scope
- Contenu mathématique (aucune modification d'énoncé), autres pages que la page stats (le CSS les stylera automatiquement, qmd inchangés).

## Preuves « done »
- [x] `check_gates.py` 622/622 après re-rendu Quarto 1.7.32 de la page stats.
- [x] Spécimen HTML réel (`paper.css`) rendu en PNG via WeasyPrint : mode clair (fond gris + filet sur `.def`, liseré encré sur `.thm`/`.prop`, barre sur `.ex`, paragraphes de preuve séparés) et mode sombre (`data-theme="dark"` : lisible, bordures visibles) — verdicts PASS.
- [x] Ancres et énoncés inchangés (diff limité aux preuves).
