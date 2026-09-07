# Contrat — Interligne des équations affichées corrigé

## Intent
Demande utilisateur 2026-09-07 : « est-ce normal que les interlignes d'équations isolées soient aussi larges ? » — Non. Deux causes cumulées dans `assets/paper.css` :
1. `margin: 2.6rem 0` sur `.math.display, .katex-display` (réglage généreux datant de l'époque où `$$` restait collé en milieu de paragraphe) ;
2. après auto-render KaTeX, `.katex-display` est **imbriqué dans** `.math.display` : les deux sélecteurs s'appliquent, et les marges parent/enfant ne fusionnent pas → ~5,2rem (≈83px) cumulés au-dessus et en dessous, ~190px d'espace vertical par équation.

## Changement
- Marge unique `1.15rem 0` (proche du `\abovedisplayskip` LaTeX) + `padding: 0.25rem`.
- Nouvelle règle `.math.display > .katex-display { margin: 0; padding: 0; }` pour neutraliser la double application (le cas `.katex-display` seul, sans wrapper, garde ses marges).
- Site-wide (toutes les pages de cours) ; aucun re-rendu HTML requis (CSS lié, non embarqué).

## Preuves « done »
- [x] Mesure programmatique WeasyPrint sur spécimen avec structure post-KaTeX (`span.math.display > span.katex-display`) : le bloc imbriqué rend avec `margin:0` ; l'espace vertical total autour d'une équation passe de ~190px à ~45px (≈ 4×).
- [x] `check_gates.py` 623/623 après changement.
- [x] Défilement horizontal mobile conservé (`overflow-x: auto` inchangé).
