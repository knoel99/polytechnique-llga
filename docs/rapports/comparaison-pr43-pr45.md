# Comparaison des PR 43 et 45

Lecture faite le 24 octobre 2026 sur `main` à `484e977` (PR 46, après la PR 44). Les deux branches n'ont pas été modifiées, rebasées, commentées ni poussées.

## Verdict

La PR 43 publie un barème O1 à O8, corrige des formules et des notations, et ajoute des projets et un examen sur les 40 pages scientifiques. La PR 45 est déjà contenue dans l'historique au-dessus du `main` actuel. Elle ajoute la licence Apache 2.0, un README réécrit, les dates de l'AI Act après le règlement (UE) 2026/1744, et des corrections factuelles courtes. La PR 45 est plus forte sur ce qui manque encore à `main`. La PR 43 est plus large, mais les formules et les sections de projets qu'elle apporte sont déjà dans `main` par les PR 44 et 46, souvent dans une relecture plus précise, et sa fusion entre en conflit sur 82 fichiers. Il fusionne la PR 45 en fast-forward, de préférence en squash à cause des commits de travail, et il ferme la PR 43 sans la fusionner. Il ne reprend pas les pages de cours de la PR 43. Le contrôle `tools/check_coherence_map.py` n'existe que sur la PR 43. Il ne le reprend qu'après avoir refait le tableau sur `main`. Après la fusion, il réécrit une phrase du cours de formes. Cette phrase pointe la bonne ancre et prête à la section 7.1 un propos qu'elle n'a pas.

## Périmètre et taille

`main` a deux commits que la PR 43 n'a pas. Ce sont `9fa0b5e` (PR 44, fusionnée le 24 octobre 2026 à 07:31 UTC) et `484e977` (PR 46, fusionnée le 24 octobre 2026 à 13:36 UTC). La base commune de la PR 43 et de `main` est `10983f29`. La base commune de la PR 45 et de `main` est `484e977` lui-même.

La PR 43 (`cursor/coherence-objectives-dbc9`, sommet `d8af41e`) est 22 commits devant `main` et 2 commits derrière. Le diff à trois points fait 101 fichiers, 20729 insertions et 1631 suppressions. Sept de ces commits sont signés Claude. Quinze sont signés Cursor Agent. Les sept premiers sont l'historique non écrasé du travail qui a abouti à la PR 44.

La PR 45 (`claude/lucid-edison-imzaab`) a bougé pendant la lecture. À 17:39 UTC, le commit `c69a3dd` a ajouté `docs/analyse-pr-43-45.md`. Le sommet lu ici est `c69a3dd`. La branche est 27 commits devant `main` et 0 derrière. Le diff à trois points fait 46 fichiers, 508 insertions et 150 suppressions. Le commit d'avant, `e2df797`, faisait 45 fichiers, 369 insertions et 150 suppressions. Les 139 lignes nouvelles sont uniquement ce rapport déjà présent dans la PR 45. Les chiffres de ce document sont recalculés sur `c69a3dd`. Ils ne sont pas recopiés depuis `docs/analyse-pr-43-45.md`.

L'intersection des fichiers touchés par les deux diffs à trois points compte 41 chemins. Ce sont `README.md` et 20 paires `index.qmd` plus `index.html`. Cinq fichiers ne sont que dans la PR 45.

- `LICENSE`
- `assets/paper.css`
- `courses/m2-ethical-issues-ai/index.qmd`
- `courses/m2-ethical-issues-ai/index.html`
- `docs/analyse-pr-43-45.md`

Soixante fichiers ne sont que dans la PR 43. GitHub affiche la PR 43 comme `CONFLICTING` et la PR 45 comme `MERGEABLE` et `CLEAN`, avec 508 insertions, 150 suppressions, 46 fichiers et 27 commits.

## Conflits de fusion

`git merge-tree --write-tree --name-only origin/main origin/cursor/coherence-objectives-dbc9` sort avec le code 1 et 82 fichiers en conflit. Un `git merge --no-commit --no-ff` dans un worktree jetable de `main` donne la même liste de 82 fichiers non fusionnés. Parmi eux, 35 se terminent par `.qmd` et 41 par `.html`. Le découpage par dossier est 74 sous `courses`, 2 sous `projects`, 5 sous `specs` et 1 sous `tools` (`tools/check_gates.py`).

`git merge-tree` de `main` avec le sommet actuel de la PR 45 sort avec le code 0 et 0 conflit. Un `git merge --ff-only` dans un worktree avance `484e977` jusqu'à `c69a3dd` sans conflit.

Les deux ensemble, dans l'ordre fast-forward de la PR 45 puis merge de la PR 43, laissent 83 fichiers non fusionnés. Le fichier en plus par rapport aux 82 est `README.md`. L'ordre inverse ne produit pas un arbre fusionné, parce que la PR 43 échoue déjà seule contre `main`.

La liste des 82 chemins est dans l'annexe. Elle est aussi la sortie de `python3 docs/rapports/compare_prs.py`.

## Échantillon

L'échantillon regarde des corrections de formules de la PR 43 et des corrections factuelles de la PR 45. Pour la PR 43, la question utile est de savoir si `main` a déjà la correction.

### Acceptation MALA

Commit `543913f` de la PR 43, `courses/m1p1-probability-monte-carlo/index.qmd`. Avant, ancienne ligne du diff.

```
loga = U(x) - U(y) + q(x, y) - q(y, x)
```

Après, ligne 1295 de la branche 43.

```
loga = U(x) - U(y) + q(y, x) - q(x, y)   # log[pi(y) q(y->x)] - log[pi(x) q(x->y)]
```

`main` a déjà cette ligne à `courses/m1p1-probability-monte-carlo/index.qmd:1330`. Le rapport d'acceptation de Metropolis-Hastings est π(y) q(y vers x) sur π(x) q(x vers y). Avec π proportionnelle à exp(-U), le logarithme est U(x) - U(y) plus le log de la proposition inverse moins le log de la proposition directe. Dans le code, `q(a, b)` est le log de la gaussienne centrée en `a - gamma dU(a)`. L'ancien ordre des deux appels à `q` était inversé. La correction est juste, et elle est déjà sur `main`.

### Coût 6ND

Même commit, `courses/m1p2-deep-learning-p2/index.qmd`. Avant, l'exercice 1 annonçait `6ND ≈ 2.2×10^{21}` FLOPs pour GPT-2 small (N ≈ 124 millions, D = 3 milliards de tokens). Après, ligne 1453 de la branche 43, le même exercice annonce `2.2×10^{18}`. Le produit 6 × 1,24×10^8 × 3×10^9 vaut 2,232×10^18. L'ancien exposant est trop grand d'un facteur 1000. `main` a la forme développée à la ligne 1732.

```
6ND \approx 6 \times 1.24\times10^{8} \times 3\times10^{9} \approx 2.2\times10^{18} \ \text{FLOPs},
```

### Sous-différentiel

Avant, la preuve de la condition d'optimalité concluait que tout sous-gradient au minimum est nul. Après, lignes 260 à 264 de `courses/m1p2-optimization-ai/index.qmd` sur la branche 43, le texte dit que 0 appartient au sous-différentiel et qu'un sous-gradient non nul peut rester, avec l'exemple de la valeur absolue en 0 dont le sous-différentiel est [-1, 1]. C'est le bon énoncé pour une fonction convexe. `main` a une preuve plus courte aux lignes 302 à 310, qui lit la définition avec v = 0 et donne le même exemple. Reprendre le texte de la PR 43 remplacerait cette relecture.

Trois autres corrections du même paquet sont déjà sur `main` dans une forme au moins aussi précise. Le pixel (2, 2) du cours de synthèse d'images est à la ligne 397 de `main`, avec le croisement de l'hypoténuse. Le code de réparation par quantiles du transport optimal est aux lignes 993 à 1008 de `main`, avec un test `lambda = 0`. La guidance sans classifieur du cours d'advanced deep learning est aux lignes 1052 à 1058 de `main`, qui explique le décalage `w' = w - 1` par rapport à Ho et Salimans. La branche 43 a la formule, sans cette phrase.

Le corollaire de VC est un cas du même genre. La branche 43, ligne 549 de `courses/m1p1-statistical-learning-theory/index.qmd`, dit que l'ERM sur une classe de VC finie est consistant relativement à H, pas universellement consistant. `main`, lignes 557 à 563, dit la même chose et ajoute le crible croissant. Les deux corrigent l'ancienne phrase qui appelait cette classe universellement consistante.

### Marches et chemins

PR 45, `courses/m1p2-graph-ml/index.qmd`, ligne 191. Avant, sur `main`, la même ligne dit que (A^k)_ij compte les chemins de longueur k. Après, la ligne dit que (A^k)_ij compte les marches de longueur k de i vers j, les sommets pouvant se répéter. C'est la définition du produit de matrices d'adjacence. La phrase d'après, sur les marches fermées de longueur 3 et les triangles, est alignée sur le même mot.

### Auteurs et identifiants

`courses/m1p1-machine-learning/index.qmd`, ligne 2169. Avant, `main` attribue *Classifier Chains* à J. Read, B. Pfahringer, G. Holmes, R. Kirkby. Après, la PR 45 écrit E. Frank à la place de R. Kirkby. La page du PDF de Waikato nomme Jesse Read, Bernhard Pfahringer, Geoff Holmes et Eibe Frank (consultation du 24 octobre 2026, https://ml.cms.waikato.ac.nz/publications/2009/chains.pdf). La fiche Research Commons donne les mêmes quatre noms (https://researchcommons.waikato.ac.nz/entities/publication/27355ae3-0654-443d-9425-4c1585d16685).

`courses/m1p2-optimal-transport/index.qmd`, ligne 1283. L'ancien lien `1810.11477` devient `1810.08278`. arXiv titre cet identifiant *Interpolating between Optimal Transport and MMD using Sinkhorn Divergences*, Jean Feydy et coauteurs (https://arxiv.org/abs/1810.08278, consulté le 24 octobre 2026).

`courses/m1p2-optimization-ai/index.qmd`, ligne 1690. L'ancien lien `1204.1438` devient `1204.3982`. arXiv titre cet identifiant *Adaptive Restart for Accelerated Gradient Schemes*, Brendan O'Donoghue et Emmanuel Candes (https://arxiv.org/abs/1204.3982, consulté le 24 octobre 2026).

### Théorème ergodique

`courses/m1p2-reinforcement-learning/index.qmd`, lignes 237 à 243. Avant, le théorème 0.2 affirmait une vitesse géométrique pour toute chaîne ergodique, liée au module de la deuxième valeur propre. Après, la convergence en variation totale reste vraie pour tout état initial. La vitesse géométrique est restreinte à un espace d'états fini. Le texte ajoute qu'une chaîne ergodique sur un espace dénombrable peut converger plus lentement que toute vitesse géométrique. C'est le bon partage entre le cas fini et le cas dénombrable.

### Point de Slater

`courses/m1p1-machine-learning/index.qmd`, ligne 842. Avant, la preuve disait que Slater s'applique si C est assez grand ou si les variables d'écart le sont. Après, le point θ = 0, b = 0, ξ_i = 2 est donné comme strictement réalisable pour tout C. Pour la contrainte y_i (θ·x_i + b) ≥ 1 - ξ_i et ξ_i ≥ 0, ce point donne 0 ≥ -1, donc une inégalité stricte. La correction enlève une condition inutile sur C.

### Formule de Kaplan

`courses/m1p2-deep-learning-p2/index.qmd`, lignes 718 à 722. `main` écrit la somme (N_c/N) à la puissance α_N, plus (D_c/D) à la puissance α_D, plus L_∞. La PR 45 écrit le crochet [(N_c/N) à la puissance α_N/α_D, plus D_c/D] à la puissance α_D. La phrase qui suit, « enlarging the model helps more than enlarging the data », ne change pas. Le paragraphe Chinchilla qui vient après non plus. Je n'ai pas rouvert le PDF de Kaplan 2020 dans cette lecture. Les deux écritures circulent comme formes de Kaplan. Le changement reste compatible avec la phrase qui suit. Je le laisse hors des erreurs introduites.

### Renvoi du cours de formes

PR 45, `courses/m1p1-shapes/index.qmd`, ligne 245. Avant, la ligne 245 de `main` dit que les algorithmes sont écrits d'abord sur la combinatoire, puis plongés dans les positions, « the same discipline as for the graphs of the Machine Learning module ». Après, la même phrase renvoie à la section 7.1 du refresher d'informatique, ancre `representations-lists-matrix-csr`. L'ancre existe. Le HTML de la branche, ligne 1714, a `id="representations-lists-matrix-csr"`. Le titre, ligne 1646 du `.qmd`, est « 7.1. Representations: lists, matrix, CSR ». Le corps montre trois stockages d'un graphe. Il ne dit pas qu'on écrit l'algorithme sur la combinatoire puis qu'on le plonge dans des positions. L'ancre est la bonne. La phrase attribue à la section un propos qu'elle n'a pas. C'est une erreur introduite par la PR 45.

### RoPE

Ligne 1165 de `courses/m1p1-deep-learning/index.qmd` sur la PR 45 remplace « with unbounded length support » par « a model does not generalize beyond its training context unless the angles are rescaled », avec un renvoi au chapitre 3 du cours advanced topics. La proposition 3.2, ligne 383 de ce cours, dit que prolonger le contexte revient à reparamétrer les angles. La section 3.2 ajoute un affinage après l'interpolation. Le renvoi tombe au bon chapitre. La nécessité écrite dans la phrase est plus forte que le chapitre, qui parle aussi d'un affinage.

### Deux phrases fausses dans le barème de la PR 43

Le fichier `specs/coherence-objectives-report.md` n'existe que sur la PR 43. Deux de ses raisons sont fausses sur cette branche elle-même. La ligne 36 dit que la section 7.4 des LLM est encore une seule puce GraphRAG. Sur la même branche, `courses/m2-large-language-models/index.qmd`, lignes 739 à 743, a trois puces, HyDE, GraphRAG et les requêtes structurées, plus un bloc de code. La ligne 40 dit que le chapitre 10 de Graph ML est encore de la prose. Le chapitre, lignes 1452 à 1505, a deux encadrés, un pseudo-code et un labo. L'échelle de la ligne 5 compte un labo sur la page comme profondeur 3. La note O5 égale à 2 de cette page contredit cette échelle. `tools/check_coherence_map.py` lit le tableau. Il ne lit pas les pages. Il ne voit pas ces deux phrases.

## Dates de l'AI Act dans la PR 45

Le texte nouveau est dans `courses/m2-ethical-issues-ai/index.qmd`, lignes 128 à 132, et il est repris en plus court dans `courses/m2-explainability-security-privacy-llms/index.qmd`. Source lue le 24 octobre 2026.

https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng

Le Journal officiel dit ceci, et la page du cours le suit.

Le règlement (UE) 2026/1744 est daté du 8 juillet 2026 (« Done at Strasbourg, 8 July 2026 »). Il est publié au Journal officiel du 24 juillet 2026. L'article d'entrée en vigueur dit que le règlement entre en vigueur le troisième jour suivant cette publication. Le troisième jour après le 24 juillet 2026 est le 27 juillet 2026. Le même règlement utilise la date du 27 juillet 2026 pour l'application des articles 102 à 110 (article 1, point 40, c). La phrase « in force on 27 July 2026 » est donc le calcul de la clause d'entrée en vigueur, pas une date écrite telle quelle dans cette clause.

L'article 1, point 40, b, remplace le point c de l'article 113. Les sections 1, 2 et 3 du chapitre III, sauf l'article 6, paragraphe 5, s'appliquent le 2 décembre 2027 pour les systèmes à haut risque de l'article 6, paragraphe 2, et de l'annexe III, et le 2 août 2028 pour ceux de l'article 6, paragraphe 1, et de l'annexe I. La page nomme les sections 1, 2 et 3 du chapitre III et les deux dates. Elle omet l'exception de l'article 6, paragraphe 5. Les dates principales sont justes. L'exception manque.

L'article 111, paragraphe 4, ajouté par l'article 1, point 39, dit que les fournisseurs de systèmes qui génèrent du contenu synthétique audio, image, vidéo ou texte, déjà mis sur le marché avant le 2 août 2026, se conforment à l'article 50, paragraphe 2, au plus tard le 2 décembre 2026. La page parle de « generative systems » et de marquage des sorties. Le sujet juridique est le fournisseur. Le délai et l'article sont les bons.

L'article 1, point 40, a, fait appliquer les points (ba) et (bb) de l'article 5, paragraphe 1, et les paragraphes 1a et 1b, à partir du 2 décembre 2026. L'article 1, point 7, insère ces deux interdictions (images intimes non consenties, et matériel d'abus sexuel sur enfant au sens de la directive 2011/93/UE). La page cite les bons points et la bonne date.

Le paragraphe « Dates » de la ligne 128 garde les dates du texte de 2024, y compris le 2 août 2026 pour l'annexe III, et il les présente comme les dates du texte adopté en 2024. Le paragraphe suivant donne les dates modifiées. Lu seul, le premier paragraphe est périmé. Lu avec le second, il est étiqueté.

Je n'ai pas ouvert une page séparée de la Commission. Le texte contrôlé est celui du Journal officiel sur EUR-Lex.

## Contrôles du dépôt et CI GitHub

Les trois commandes ont été lancées dans des worktrees détachés, sans toucher au checkout de travail ni aux branches des PR.

| Arbre | `check_gates.py` | `check_progression.py` | `check_airiness.py` | `check_coherence_map.py` |
|---|---|---|---|---|
| `main` `484e977` | 1022 sur 1022, code 0 | 40 sur 40, code 0 | 49 lignes `ok`, code 0 | fichier absent |
| PR 43 `d8af41e` | 1059 sur 1059, code 0 | 40 sur 40, code 0 | 49 lignes `ok`, code 0 | 40 cours, code 0 |
| PR 45 `c69a3dd` | 1022 sur 1022, code 0 | 40 sur 40, code 0 | 49 lignes `ok`, code 0 | fichier absent |

La PR 43 a 37 contrôles de plus. Son `tools/check_gates.py` n'est pas celui de `main`. Ce fichier est dans la liste des 82 conflits. Le contrôle de carte n'existe que sur cette branche. Il annonce 40 cours scientifiques, des notes de 0 à 3, NLP en O2 à 2, et le refresher de réseaux de neurones en O7 à 2.

`gh pr checks` répond « no checks reported » pour les deux PR, avec le code de sortie 1. L'API des check-runs donne `total_count` 0 pour `d8af41e` et pour `c69a3dd`. `main` n'a aucun fichier sous `.github` (0 chemin). Le dépôt ne lance pas de workflow GitHub sur ces branches.

Le suivi de tickets est activé et compte 0 ticket (`gh repo view` et `gh issue list --state all`).

## Tableau

| Critère | PR 43 | PR 45 |
|---|---|---|
| Portée | 101 fichiers, 20729 insertions, 1631 suppressions, 22 commits. Barème, formules, notations, projets et examens. | 46 fichiers, 508 insertions, 150 suppressions, 27 commits. Licence, README, AI Act, corrections courtes, plus un rapport de 139 lignes ajouté le 24 octobre. |
| Correction | Les formules relues ici sont justes, et `main` les a déjà, souvent mieux écrites. Deux raisons du barème sont fausses sur la branche elle-même. | Les marches, les auteurs, les identifiants arXiv, Slater et le théorème ergodique corrigent des erreurs encore sur `main`. L'AI Act suit le Journal officiel, avec l'oubli de l'article 6, paragraphe 5. Le renvoi du cours de formes tombe sur la bonne ancre et attribue à la section 7.1 un propos qu'elle n'a pas. |
| Cohérence avec O1 à O8 | Seule branche qui note chaque cours et qui échoue si un cours manque au tableau. Le tableau décrit cette branche, pas `main` après la PR 46. | Ne note pas les cours. Elle s'appuie sur la cohérence déjà fusionnée par les PR 44 et 46. |
| Pédagogie | Projets, examen et barème sur les 40 pages, générés puis rendus. `main` a déjà ces sections, relues par la PR 46. | Peu de pédagogie nouvelle. Elle répare des renvois et une phrase de théorème. Le CSS retire le mot Proof devant une boîte qui porte déjà son nom. |
| Maintenabilité | `projects_section.py` et `check_coherence_map.py` sont des leviers, mais le premier réécrirait les pages déjà relues. Historique mélangé Claude puis Cursor, basé avant la PR 44. | Diff petit et fast-forward. Vingt-sept commits, dont beaucoup sont des « work in progress ». Un squash laisse un commit lisible. Le README reste en français, comme le fichier qu'il remplace. Les contrôles ne le rejettent pas. |
| Risque | 82 conflits. Une résolution naïve peut effacer la relecture de la PR 46. | 0 conflit avec `main`. 83 conflits si on tente ensuite la PR 43. Risque faible si la PR 43 reste fermée. |

## Ce que l'une a et pas l'autre

La PR 43 a, et la PR 45 n'a pas, `specs/coherence-objectives-report.md`, `tools/check_coherence_map.py` et `tools/projects_section.py`. Elle a aussi ses propres textes de projets. Ces textes ne sont pas absents de `main`. Ils y sont dans une autre rédaction.

La PR 45 a, et la PR 43 n'a pas, `LICENSE`, la règle CSS de la ligne 289 de `assets/paper.css`, les paragraphes d'AI Act, les corrections factuelles mesurées contre le `main` d'après la PR 46, et `docs/analyse-pr-43-45.md`.

La PR 45 ne répare pas une formule que la PR 46 aurait laissée fausse dans l'échantillon relu ici. La PR 43 ne contient pas la licence ni le règlement 2026/1744.

## Plan de fusion

1. Il fusionne la PR 45 en fast-forward. Un squash évite de poser sur `main` les commits de travail. Le squash emporte aussi `docs/analyse-pr-43-45.md`. Ce fichier est la note de Claude. Il peut le garder ou le retirer au moment du squash. Après la fusion, il réécrit la phrase du cours de formes, ligne 245, pour qu'elle ne prête plus à la section 7.1 du refresher un propos que cette section n'a pas. Le reste des pages de cours de la PR 45 peut rester.
2. Il ferme la PR 43 sans la fusionner. Les 82 conflits opposeraient sa rédaction à la PR 46. Les corrections de formules de l'échantillon sont déjà sur `main`.
3. Il ne cherry-pick pas de page de cours depuis la PR 43.
4. S'il veut le contrôle de carte, il réécrit le tableau contre les pages de `main`, puis il ajoute le script. Reprendre le tableau de la branche 43 noterait un texte que `main` n'a plus. Deux raisons de ce tableau sont déjà fausses sur la branche 43. Une recherche Notion et une recherche Drive, le 24 octobre 2026, ne trouvent aucune note de Kim qui choisisse entre ces deux PR. La phrase « The owner chose » du corps de la PR 45 est celle du commit `d6330df`, signé Claude. Ce n'est pas un message enregistré de Kim.
5. Il ne lance pas `projects_section.py` de la PR 43 sur `main`. Le script réécrirait les sections déjà relues.

## Annexe. Commandes

Les comptes du corps viennent des commandes suivantes, relancées après l'arrivée de `c69a3dd`. Le script `docs/rapports/compare_prs.py` refait le diff, l'intersection et les deux essais de fusion.

```
git fetch origin main cursor/coherence-objectives-dbc9 claude/lucid-edison-imzaab
git rev-parse origin/main origin/cursor/coherence-objectives-dbc9 origin/claude/lucid-edison-imzaab
git rev-list --left-right --count origin/main...origin/cursor/coherence-objectives-dbc9
git rev-list --left-right --count origin/main...origin/claude/lucid-edison-imzaab
git diff --shortstat origin/main...origin/cursor/coherence-objectives-dbc9
git diff --shortstat origin/main...origin/claude/lucid-edison-imzaab
git log --format='%h %an %s' e2df797..origin/claude/lucid-edison-imzaab
python3 docs/rapports/compare_prs.py
```

Sortie utile du script, sommet `c69a3dd`.

```
left ahead/behind 2	22
right ahead/behind 0	27
left shortstat 101 files changed, 20729 insertions(+), 1631 deletions(-)
right shortstat 46 files changed, 508 insertions(+), 150 deletions(-)
overlap 41
only right 5
merge-tree left exit 1 conflicts 82
merge-tree right exit 0 conflicts 0
sequential ff origin/claude/lucid-edison-imzaab: exit 0
sequential unmerged: 83
```

Le fichier en plus dans les 83 est `README.md`. Les 82 conflits de la PR 43 seule sont ceux-ci.

```
courses/m1p1-computer-animation/index.html
courses/m1p1-computer-animation/index.qmd
courses/m1p1-computer-vision/index.html
courses/m1p1-dbms/index.html
courses/m1p1-dbms/index.qmd
courses/m1p1-deep-learning/index.html
courses/m1p1-deep-learning/index.qmd
courses/m1p1-emerging-ml/index.html
courses/m1p1-emerging-ml/index.qmd
courses/m1p1-machine-learning/index.html
courses/m1p1-machine-learning/index.qmd
courses/m1p1-probability-monte-carlo/index.html
courses/m1p1-probability-monte-carlo/index.qmd
courses/m1p1-refresher-cs/index.html
courses/m1p1-refresher-cs/index.qmd
courses/m1p1-refresher-neural-nets/index.html
courses/m1p1-refresher-neural-nets/index.qmd
courses/m1p1-refresher-statistics/index.html
courses/m1p1-refresher-statistics/index.qmd
courses/m1p1-shapes/index.html
courses/m1p1-shapes/index.qmd
courses/m1p1-signal-processing/index.html
courses/m1p1-signal-processing/index.qmd
courses/m1p1-statistical-learning-theory/index.html
courses/m1p1-statistical-learning-theory/index.qmd
courses/m1p1-tda/index.html
courses/m1p2-advanced-deep-learning/index.html
courses/m1p2-advanced-deep-learning/index.qmd
courses/m1p2-computer-vision-applications/index.html
courses/m1p2-computer-vision-applications/index.qmd
courses/m1p2-deep-learning-p2/index.html
courses/m1p2-deep-learning-p2/index.qmd
courses/m1p2-graph-ml/index.html
courses/m1p2-graph-ml/index.qmd
courses/m1p2-image-synthesis/index.html
courses/m1p2-image-synthesis/index.qmd
courses/m1p2-multimodal-genai/index.html
courses/m1p2-multimodal-genai/index.qmd
courses/m1p2-nlp-text-mining/index.html
courses/m1p2-nlp-text-mining/index.qmd
courses/m1p2-optimal-transport/index.html
courses/m1p2-optimal-transport/index.qmd
courses/m1p2-optimization-ai/index.html
courses/m1p2-optimization-ai/index.qmd
courses/m1p2-realtime-ai-videogames/index.html
courses/m1p2-realtime-ai-videogames/index.qmd
courses/m1p2-reinforcement-learning/index.html
courses/m1p2-reinforcement-learning/index.qmd
courses/m1p2-responsible-ai-sustainability/index.html
courses/m1p2-responsible-ai-sustainability/index.qmd
courses/m1p2-social-media-probabilistic/index.html
courses/m1p2-social-media-probabilistic/index.qmd
courses/m1p2-statistics-in-action/index.html
courses/m1p2-statistics-in-action/index.qmd
courses/m2-advanced-gnn/index.html
courses/m2-advanced-gnn/index.qmd
courses/m2-advanced-topics-llms/index.html
courses/m2-boosting-foundation-tabular/index.html
courses/m2-control-generative-ai/index.html
courses/m2-control-generative-ai/index.qmd
courses/m2-explainability-security-privacy-llms/index.html
courses/m2-explainability-security-privacy-llms/index.qmd
courses/m2-geometric-deep-learning/index.html
courses/m2-geometric-deep-learning/index.qmd
courses/m2-graph-generative-models/index.html
courses/m2-graph-generative-models/index.qmd
courses/m2-large-language-models/index.html
courses/m2-large-language-models/index.qmd
courses/m2-mlops-llm-engineering/index.html
courses/m2-mlops-llm-engineering/index.qmd
courses/m2-privacy-uncertainty/index.html
courses/m2-privacy-uncertainty/index.qmd
courses/m2-security-robustness/index.html
courses/m2-speech-technology/index.html
projects/index.html
projects/index.qmd
specs/README.md
specs/coherence-2026-10/capstones.md
specs/coherence-2026-10/report.md
specs/coherence-objectives.md
specs/projects-and-assessment.md
tools/check_gates.py
```

Contrôles, chacun dans un worktree détaché.

```
python3 tools/check_gates.py
python3 tools/check_progression.py
python3 tools/check_airiness.py
python3 tools/check_coherence_map.py
```

CI et tickets.

```
gh pr checks 43 --repo knoel99/polytechnique-llga
gh pr checks 45 --repo knoel99/polytechnique-llga
gh api repos/knoel99/polytechnique-llga/commits/d8af41e0d4fa7ef111c765b81aea2888baa8bd24/check-runs --jq .total_count
gh api repos/knoel99/polytechnique-llga/commits/c69a3dde558df6c4ea0f2a8b85360eaff81193b9/check-runs --jq .total_count
gh pr view 43 --repo knoel99/polytechnique-llga --json mergeable,mergeStateStatus,additions,deletions,changedFiles
gh pr view 45 --repo knoel99/polytechnique-llga --json mergeable,mergeStateStatus,additions,deletions,changedFiles,commits
gh repo view knoel99/polytechnique-llga --json hasIssuesEnabled,issues
gh issue list --repo knoel99/polytechnique-llga --state all --limit 5
git ls-tree -r --name-only origin/main .github
```

Les lignes citées viennent de `git show <ref>:<path>` et de `git grep -n`. Les essais de fusion manuels, avant le script, étaient des `git worktree add --detach` sous `/tmp/pr-compare`, suivis de `git merge --no-commit --no-ff` ou `--ff-only`, puis `git merge --abort` et `git worktree remove --force`. Ils ont donné les mêmes 82, 0 et 83 fichiers.

Le renvoi de formes, RoPE et le barème ont été relus après coup avec ces commandes.

```
git show origin/claude/lucid-edison-imzaab:courses/m1p1-shapes/index.qmd
git show origin/main:courses/m1p1-shapes/index.qmd
git grep -n 'id="representations-lists-matrix-csr"' origin/claude/lucid-edison-imzaab -- courses/m1p1-refresher-cs/index.html
git show origin/claude/lucid-edison-imzaab:courses/m1p1-deep-learning/index.qmd
git show origin/claude/lucid-edison-imzaab:courses/m2-advanced-topics-llms/index.qmd
git show origin/cursor/coherence-objectives-dbc9:specs/coherence-objectives-report.md
git show origin/cursor/coherence-objectives-dbc9:courses/m2-large-language-models/index.qmd
git show origin/cursor/coherence-objectives-dbc9:courses/m1p2-graph-ml/index.qmd
git log -1 --format='%h %an %s%n%b' d6330df
```
