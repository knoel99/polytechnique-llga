# polytechnique-llga

Notes de cours indépendantes et open source pour le master **MScT « Large Language Models, Graphs and Applications » (LLGA)** de l'École Polytechnique.

**Site (en anglais)** : <https://knoel99.github.io/polytechnique-llga/>

> Ce site n'est ni créé, ni maintenu, ni validé par l'École Polytechnique ou ses enseignants. Il reconstitue ce qui peut être enseigné dans le master à partir du programme public et de l'état de l'art. Pour les inscriptions, les ECTS et les listes officielles de cours, la référence reste la documentation officielle (liens en bas de la page d'accueil).

## Ce que contient le site

- **Page d'accueil** (`index.html`) :
  - description officielle du master ;
  - arbre du cursus (obligatoires, « Choose N », créneaux annoncés) avec deux parcours conseillés, *Graph × LLM* et *AI systems* ;
  - tableau du programme 2026–2027 (codes, volumes horaires, statut dans le catalogue SynapseS) ;
  - projets et évaluations ;
  - documentation officielle et débouchés.
- **Une page par module** (`courses/<module>/index.html`). Chaque cours scientifique contient :
  - la fiche officielle SynapseS 2026–2027 (code, équipe, volume, évaluation, prérequis) et un tableau de correspondance entre le programme officiel et les chapitres ;
  - un plan de séances qui totalise le volume officiel, avec des niveaux 1 → 3 qui ne redescendent jamais ;
  - des chapitres numérotés : définitions, théorèmes et démonstrations, exemples travaillés, code Python (NumPy / PyTorch / networkx…) ;
  - des exercices corrigés, gradués ★ / ★★ / ★★★ ;
  - une section **Projects and assessment** : sujets individuels et en groupe, sujet d'examen écrit avec barème, grille d'évaluation ;
  - les références.
- **Projets de fin d'année** (`projects/`) : 5 projets intégrateurs de fin de M1, rattachés aux projets officiels de la période 2, et 5 projets de M2 au format du projet transverse (8 ECTS).
- **Notations** (`notation/`) : les conventions communes aux cours.
- **Pages de cadrage** pour les modules non scientifiques : management, langues, humanités, sport, stages, projet transverse, séminaire d'éthique (dont un résumé de l'AI Act et du RGPD).

## Relectures (octobre 2026)

- **Analyse de cohérence** : chaque page a été lue en entier, puis analysée selon cinq angles : couverture des objectifs du master O1–O8, chaîne des prérequis, redondances et notations, erreurs, projets intégrateurs. Les corrections ont été appliquées page par page et relues par un second agent. Contrat : `specs/coherence-objectives.md` ; analyse complète : `specs/coherence-2026-10/`.
- **Seconde lecture** : les 49 pages ont été relues par un agent indépendant (mathématiques, faits, références, exécution du code). Sur les 37 dernières pages, 327 points ont été relevés et 278 corrigés sur place ; les autres sont de faible gravité ou sans objet. Les points qui touchent plusieurs pages ont été corrigés ensuite, chacun vérifié à nouveau par un autre agent.
- **Comparaison des PR #43 et #45** : `docs/analyse-pr-43-45.md`.

Le site est en anglais uniquement (`specs/en-only.md`). L'ancien chemin `/en/` redirige vers la racine.

## Structure du dépôt

```
index.html                    Page d'accueil (racine GitHub Pages)
assets/paper.css              Feuille de style unique : fort contraste, clair / sombre, mobile
assets/theme.js               Barre supérieure, sommaire latéral, thème, tableaux
courses/<module>/index.qmd    Source Quarto d'un module
courses/<module>/index.html   Page rendue (publiée)
projects/                     Projets de fin d'année (source .qmd et page rendue)
notation/                     Conventions de notation (source .qmd et page rendue)
specs/                        Contrats « spec → implement → prove » (index : specs/README.md)
tools/                        Scripts de rendu et de contrôle
AGENTS.md                     Règles et gates obligatoires
LICENSE                       Licence Apache 2.0
```

## Travailler sur un module

Prérequis : [Quarto](https://quarto.org) 1.7.32, Python 3, et Node.js pour la vérification KaTeX.

1. Modifier la source `courses/<module>/index.qmd`.
2. Rendre la page : `python3 tools/render.py <module>`. Ce script appelle Quarto puis remet l'empreinte d'intégrité de KaTeX 0.19.0.
3. Lancer les contrôles :
   - `python3 tools/check_gates.py` : contrôles d'ensemble (sources, thème, exercices, sections de projets, arbre de l'accueil, KaTeX épinglé…) ;
   - `python3 tools/check_progression.py` : plan de séances, niveaux, calibrage horaire et exercices gradués (`specs/hours-and-progression.md`) ;
   - `python3 tools/check_airiness.py` : texte aéré, lisible au vidéoprojecteur (`specs/front-redesign.md`).
4. Si un plan de séances a changé, mettre à jour le tableau du programme de l'accueil : `python3 tools/programme_table.py`.

Un nouveau module ou une refonte importante commence par un contrat dans `specs/` (modèle : `specs/_template-module.md`). Les gates de `AGENTS.md` doivent être cochées avant la fusion.

## Contrats principaux

| Contrat | Objet |
|---|---|
| `specs/competency-tree.md` | source structurelle unique (wiki LLGA et catalogue SynapseS de l'année) |
| `specs/hours-and-progression.md` | volumes, plans de séances, progression de la difficulté |
| `specs/front-redesign.md` | contraste projecteur, mode sombre, sommaire, texte aéré |
| `specs/coherence-objectives.md` | cohérence des cours avec les objectifs du master (analyse complète : `specs/coherence-2026-10/`) |
| `specs/projects-and-assessment.md` | projets et évaluations de chaque cours, projets de fin d'année |
| `specs/en-only.md` | site en anglais uniquement |

## Sources officielles

- [Page du programme LLGA](https://programmes.polytechnique.edu/en/master/all-msct-specializations/large-language-models-graphs-and-applications-llga) (École Polytechnique)
- [Wiki du master, page curriculum](https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum)
- [Catalogue SynapseS 2026–2027](https://synapses.polytechnique.fr/catalogue/2026-2027)

## Licence

Le code et les notes de cours de ce dépôt sont distribués sous la [licence Apache 2.0](LICENSE). Copyright 2026 knoel99 et les contributeurs.

Exceptions :
- **Textes officiels cités** : les descriptions du programme, les fiches SynapseS et le wiki restent la propriété de leurs auteurs. Ils sont cités pour information, avec leur source.
- **Ressources tierces** : KaTeX (licence MIT) est chargé depuis jsDelivr. Les jeux de données cités dans les projets ont leurs propres licences, indiquées dans chaque sujet.
