# Analyse des PR #43 et #45

Analyse rédigée le 24 octobre 2026, faite sur `main` = `484e977` (après #44 et #46).

## Recommandation

| PR | Recommandation | Raison principale |
|---|---|---|
| [#43](https://github.com/knoel99/polytechnique-llga/pull/43) (Cursor, `cursor/coherence-objectives-dbc9`) | **Fermer sans fusionner.** | Partie d'un état intermédiaire de #44, elle n'apporte rien que `main` n'ait déjà. Fusionnée, elle ferait régresser le site, et elle est en conflit sur 82 fichiers. |
| [#45](https://github.com/knoel99/polytechnique-llga/pull/45) (Claude, `claude/lucid-edison-imzaab`) | **Fusionner en *squash*.** | Petite (45 fichiers, +369 / −150), fusionnable, tous les contrôles passent. Elle ajoute la licence, le README, les dates de l'AI Act et des corrections factuelles vérifiées. |

## 1. Chronologie

Les trois travaux répondent à la même demande : la cohérence des cours avec les objectifs du master, les projets et évaluations, puis les projets de fin d'année. Ils partent tous de la même base, `10983f2` (#42, 22 octobre).

```
10983f2 (#42) ─┬─ session « ccr » : contrat, archive d'analyse, WIP des pages …
               │      ├─ 23/10 06:01  état intermédiaire « WIP: pages in progress » (179300a)
               │      │     └─ Cursor repart de là → 15 commits → PR #43 (23/10 19:37, ouverte)
               │      └─ … suite du travail → PR #44 fusionnée (24/10, 9fa0b5e)
               │                              → PR #46 fusionnée (24/10, 484e977) = main
               └─ session Claude (cette branche) : version parallèle complète (tag local ours-final)
                      → reprise de main, ajouts ciblés → PR #45
```

PR #43 contient donc les 7 premiers commits de la session qui a produit #44, avec 15 commits de Cursor par-dessus. Son tableau « 22 commits » mélange les deux.

## 2. PR #43 — analyse détaillée

### 2.1 Ce qu'elle annonce

- Un rapport `specs/coherence-objectives-report.md` qui note chaque cours scientifique sur O1–O8, et un contrôle `tools/check_coherence_map.py` qui vérifie que chaque cours figure dans ce tableau.
- La correction des 8 erreurs graves et des 9 conflits de notation relevés par l'archive d'analyse.
- La réparation des phrases de prérequis qui citaient des sections inexistantes.
- Une section *Projects and assessment* sur les 40 pages scientifiques. Elle est **générée par un script**, `tools/projects_section.py` (951 lignes), avec des seuils contrôlés : au moins 2 sujets solo, 2 sujets de groupe, 3 questions d'examen sur 20 points, etc.

### 2.2 État technique

- **Taille.** Base `10983f2`, 22 commits, 101 fichiers, +20 729 / −1 631.
- **Mergeabilité.** GitHub l'indique *dirty* (non fusionnable). Une fusion d'essai avec `main` (`git merge-tree`) donne **82 fichiers en conflit**, dont 35 sources `.qmd`.
- **CI.** Aucune vérification n'est configurée sur le dépôt.

### 2.3 Ce qui est déjà dans `main`

Méthode : pour chaque correction de #43, chercher si le texte erroné qu'elle remplace existe encore mot pour mot dans `main`.

| Commit de #43 | Objet | Texte erroné encore présent dans `main` |
|---|---|---|
| `543913f` | 8 erreurs graves (Metropolis–Hastings, rastérisation, réparation par quantiles, sous-gradient, séparation des boids…) | **0** : déjà corrigées par #44 |
| `41cb2da` | 9 conflits de notation | **0** : déjà alignés par #44 |
| `0d3583e` | renvois de prérequis « vers des sections manquantes » | 18 passages, mais voir 2.4 : ce ne sont pas des corrections pour `main` |
| `798c11c` | session 12 et commentaires redondants | 1 commentaire de code (Monte-Carlo), sans incidence |

Les pages `projects/` et `notation/` et l'archive `specs/coherence-2026-10/` viennent des commits communs avec #44. `main` en a une version plus avancée.

### 2.4 Ce qui régresserait si on la fusionnait

1. **Renvois supprimés à tort (`0d3583e`).** Quand Cursor a travaillé, plusieurs sections n'existaient pas encore. Il a donc retiré les phrases qui les citaient. Elles existent toutes dans `main` aujourd'hui :
   - Machine Learning 4.8 *Subgroup evaluation and group fairness* (`#fairness`) et 6.4 *Explaining tree ensembles* (`#explain-trees`), qui seraient retirées des objectifs et du plan de séances ;
   - NLP 6.4 *Relation extraction* (`#relation-extraction`), qui serait retirée du plan de séances (« Definition 6.1, which names relation extraction ») ;
   - LLM `#icl` (apprentissage en contexte) et 9.6 *Comparing two models honestly*, qui seraient retirés de l'aide à l'étude et du plan ;
   - Deep Learning P2 `#dl-transformer` : #43 écrirait « This page does not define self-attention », alors que la page le définit désormais.
2. **Rapport O1–O8 périmé.** `specs/coherence-objectives-report.md` affirme des lacunes que `main` a comblées. Fusionné tel quel, il publierait des affirmations fausses :
   - « Relation extraction is still only named in NLP chapter 6 » ;
   - « Machine Learning has no group-fairness section and no TreeSHAP » ;
   - « LLM section 7.4 is still one GraphRAG bullet » ;
   - « Deep Learning (P2) still does not define self-attention ».
3. **Sections de projets générées.** Elles remplaceraient celles de `main`, qui sont rédigées à la main et plus riches. Celles de #43 :
   - s'appuient surtout sur des données synthétiques ;
   - ont des critères de réussite parfois triviaux (Speech : « le taux d'erreur avec bruit est le plus élevé ») ;
   - ne proposent que 3 questions d'examen par cours.

   `main` propose des sujets sur données publiques réelles, des études d'articles, un examen blanc et une grille par cours.

### 2.5 Ce qui pourrait être repris

- **L'idée d'une matrice O1–O8 contrôlée par un script.** Il faudrait la refaire sur l'état actuel de `main` plutôt que reprendre le rapport de #43. L'archive `specs/coherence-2026-10/objectives.md` décrit l'état *avant* corrections.
- **Rien d'autre.** Les corrections de fond sont déjà dans `main`.

## 3. PR #45 — analyse détaillée

### 3.1 Contenu

| Élément | Fichiers | Détail |
|---|---|---|
| Licence | `LICENSE` | Texte officiel Apache 2.0 (empreinte SHA-256 identique au fichier d'apache.org). |
| README | `README.md` | Réécrit en français pour le site actuel : pages, structure, rendu et contrôles, contrats, section Licence avec exceptions (textes officiels cités, jeux de données). Les mentions périmées sont retirées : pages supprimées, ancien « track recommandé », brochure. |
| AI Act | pages éthique et ESP | Les dates suivent le règlement modificatif « Digital Omnibus on AI », vérifié dans le texte du Journal officiel : Règlement (UE) 2026/1744 du 8 juillet 2026, publié au JO le 24 juillet 2026 et en vigueur le 27 juillet. Voir le détail ci-dessous. |
| CSS | `assets/paper.css` | Les encadrés étiquetés « Solution » ou « Marking points » n'affichent plus le « Proof. » automatique de Quarto. |
| Corrections factuelles | 21 cours (`.qmd` et `.html`) | Environ 37 erreurs du texte antérieur que `main` contenait encore. |

Détail des dates de l'AI Act :
- obligations « haut risque » au 2 décembre 2027 pour l'annexe III et au 2 août 2028 pour l'annexe I ;
- art. 50(2) : délai jusqu'au 2 décembre 2026 pour les systèmes génératifs déjà sur le marché ;
- nouvelles interdictions de l'art. 5(1)(ba)/(bb) au 2 décembre 2026.

### 3.2 Comment les corrections ont été choisies

1. Un audit indépendant de toutes les pages (session Claude) avait relevé des erreurs dans le texte hérité de `10983f2`.
2. On a retenu les 154 passages corrigés dont le texte erroné existait encore **mot pour mot** dans `main`.
3. Un agent a jugé chaque passage et n'a porté que les **erreurs factuelles** : formule, nombre, signe, citation, lien arXiv, renvoi vers un chapitre qui ne contient pas ce qui est annoncé, bug de code. Les reformulations, les restructurations et les liens vers du contenu absent de `main` ont été écartés. Chaque erreur a été revérifiée sur la rédaction de `main` : calculs refaits en Python, chapitres cibles ouverts, identifiants arXiv interrogés.
4. Un second agent a contrôlé chaque modification. Il en a annulé une, qui relevait du style.

Exemples :
- puissances de la matrice d'adjacence : « marches » et non « chemins » (Graph ML, ch. 0 et preuve du théorème 0.3) ;
- RoPE ne gère pas une longueur illimitée sans remise à l'échelle (DL P1) ;
- renvoi « MC dropout » vers le module qui le traite (Privacy & UQ ch. 8) ;
- résultat *Graph of Words* mal traduit : *classer* au sens de « ranger », pas « classifier » (Graph ML ch. 11) ;
- renvois vers les opérateurs non-backtracking (Social Media → Graph ML 9.2) ;
- liens arXiv et noms d'auteurs erronés dans les références (OT, Optimization for AI, ML, Advanced GNN).

### 3.3 État technique

- **Base et retard.** Base `main`, 0 commit de retard (`main` y a été fusionné après #46).
- **Fusionnabilité.** La fusion d'essai avec `main` (`git merge-tree`) est **propre**.
- **CI.** Aucune vérification configurée sur le dépôt.
- **Contrôles locaux :**
  - `check_gates.py` : 1022/1022 ;
  - `check_progression.py` : 40/40 ;
  - `check_airiness.py` : toutes les pages ;
  - KaTeX : toutes les formules se rendent, aucun `$$` littéral ;
  - liens internes : tous valides, y compris `projects/` et `notation/` ;
  - Playwright : 50 pages × 2 largeurs × 2 thèmes, sans débordement, sans erreur de script, contraste ≥ 7:1.

### 3.4 Points d'attention

- **Historique.** La branche contient la version parallèle complète (53cc956, tag local `ours-final`), une vingtaine de commits intermédiaires et deux commits de fusion avec `main`. Le premier, `d6330df`, reprend exactement le contenu de `main`. Une fusion *squash* donne un seul commit propre sur `main`.
- **Version parallèle.** Après un *squash*, elle ne survivra que tant que la branche `claude/lucid-edison-imzaab` existe : le tag `ours-final` n'est pas poussé. Pour la conserver (sections de projets alternatives, page de projets de M1 à 8 sujets, section « objectifs » de l'accueil), il faut garder la branche ou pousser le tag.
- **Volontairement absent.** Rien de la version parallèle n'est repris en dehors des points listés en 3.1, conformément au choix de conserver #44.
- **Droit.** Les dates de l'AI Act sont exactes au 24 octobre 2026. Le texte invite à vérifier la version consolidée sur EUR-Lex.

## 4. Suite proposée

1. Fermer #43 sans la fusionner, avec un renvoi vers ce rapport. Supprimer ensuite la branche `cursor/coherence-objectives-dbc9`.
2. Fusionner #45 en *squash*.
3. Nettoyer les branches restantes :
   - `ccr-35a7ca30-pszhhr`, identique à `main` ;
   - `cursor/pin-katex-sri-d608`, remplacée par #39.
4. Si besoin, refaire la matrice O1–O8 sur l'état actuel de `main`, avec un contrôle automatique comme dans #43.
