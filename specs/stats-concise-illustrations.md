# Contrat — Refresher Statistics : concision + illustrations

## Intent
Réduire le « blabla » de `courses/m1p1-refresher-statistics` (demande utilisateur 2026-09-07) : prose d'accueil, notes répétitives, avertissements en double, chapitre 9 (papiers) et section sources condensés. Ajouter des illustrations dans le style SVG papier existant (monochrome #111, system-ui 11px).

## Périmètre
- **Condensé** (≈ -2 800 mots, 17 431 → 14 619) : intro/checks/route, commentaires d'exemples et de notes ch. 1–8, preuves longues resserrées (sans perte d'idée), ch. 9 (mécanismes + 4 papiers), checkpoint de sortie, tableau des suites, sources.
- **Conservé intégralement** : les 10 chapitres, toutes les ancres `{#…}` (identiques, vérifié par diff), définitions/théorèmes/propositions, les **15 exercices + solutions** (gate ≥ 6), tableaux (distributions, tests, ANOVA), blocs de code NumPy/SciPy, honesty sur ECTS/CTD (une occurrence claire au lieu de répétitions).
- **9 nouvelles figures** (4 → 13 au total) : `schema-simpson` (ch. 1), `schema-distributions` + `schema-gaussian-conditioning` (ch. 3), `schema-lln-paths` (ch. 4), `schema-ols-projection` (ch. 7), `schema-bayes-update` + `schema-coverage` (ch. 8), `schema-missing-mechanisms` (ch. 9), `schema-bias-variance` (ch. 10).

## Hors scope
- Autres modules, `paper.css`/`theme.js` (le mode sombre des images passe déjà par la plaque blanche existante), structure de l'accueil.

## Preuves « done »
- [x] Rendu Quarto 1.7.32 (byte-stable vs pipeline du dépôt), `index.html` régénéré.
- [x] `python3 tools/check_gates.py` : 621/621 (contrats, sources Quarto, thème, liens FR, exercices, couverture index).
- [x] Ancres de sections identiques avant/après (diff vide) ; aucune ancre externe cassée (aucune entrante).
- [x] 13 SVG référencés une fois chacun dans le HTML ; rendus PNG via cairosvg sans erreur ; coordonnées revues (pas de débordement de viewBox, grilles 3×36 cellules complètes).
