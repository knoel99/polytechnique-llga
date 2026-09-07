# Contrat — Stats : prose en phrases complètes, une équation par ligne

## Intent
Demande utilisateur 2026-09-07 : « une équation par ligne avec des parties interlignes quand c'est dans le même fil logique » et « toujours des phrases complètes et claires, pas de la prise de note ». La condensation précédente (#35) avait produit un style télégraphique (étiquettes + fragments, chaînes d'équations en ligne) ; ce contrat restaure une prose de manuel sans revenir au verbeux d'origine.

## Périmètre
- `courses/m1p1-refresher-statistics/index.qmd` uniquement (aucun CSS, aucune autre page).
- **Une équation par ligne** : les chaînes inline deviennent des maths affichées séparées, reliées par des phrases de liaison — dérivations MLE (3.0b, 5.0b, 5.3, 5.9–5.12), transformations (2.5), Markov/Chebyshev numérique (2.10b), delta method, somme gaussienne (3.4), théorème 10.4 (les trois pertes spécialisées).
- **Phrases complètes** : preuves à étiquettes reformulées en phrases (« For the **complement**, write … »), checks de positionnement, réponses, introductions d'exemples (6.1b, 6.3b, 6.6, 8.3, 9.2, 9.3), définitions 2.9/5.13/5.14/9.1, prop 2.14/7.6, note « What breaks », solutions 4 et 7, et les 10 encadrés « Key takeaways » réécrits avec verbes conjugués.
- Équilibre : 14 619 → ~15 750 mots (l'original pré-condensation était à 17 431) ; concision conservée, grammaire restaurée.

## Hors scope
- Énoncés mathématiques inchangés (mêmes théorèmes, mêmes hypothèses), ancres identiques, 15 exercices conservés, tableaux laissés terses par nature.

## Preuves « done »
- [x] `check_gates.py` 623/623 après re-rendu Quarto 1.7.32.
- [x] Ancres de sections identiques avant/après (diff vide).
- [x] Scan anti-fragments (grep « ⇒ », « (i)/(a) » orphelins, étiquettes + maths sans verbe) : aucun reste hors mathématiques.
