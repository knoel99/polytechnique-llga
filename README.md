# polytechnique-llga

Notes de cours indépendantes et open source pour le master **MScT « Large Language Models, Graphs and Applications » (LLGA)** de l'École Polytechnique.

**Site (en anglais)** : <https://knoel99.github.io/polytechnique-llga/>

> Ce site n'est ni créé, ni maintenu, ni validé par l'École Polytechnique ou ses enseignants. Il reconstitue ce qui peut être enseigné dans le master à partir du programme public et de l'état de l'art. Pour les inscriptions, les ECTS et les listes officielles de cours, la référence reste la documentation officielle (liens en bas de la page d'accueil).

## Ce que contient le site

- **Page d'accueil** (`index.html`), qui contient :
  - la description officielle du master ;
  - l'arbre du cursus (obligatoires, « Choose N », créneaux annoncés), avec deux parcours conseillés :
    - *Graph × LLM* ;
    - *AI systems* ;
  - la manière dont les cours servent les objectifs du master ;
  - le tableau du programme 2026–2027 (codes, volumes horaires, statut dans le catalogue SynapseS) ;
  - la documentation officielle et les débouchés.
- **Une page par module** (`courses/<module>/index.html`). Chaque cours scientifique contient :
  - la fiche officielle SynapseS 2026–2027 (code, équipe, volume, évaluation, prérequis) et un tableau de correspondance entre le programme officiel et les chapitres ;
  - un plan de séances qui totalise le volume officiel, avec des niveaux 1 → 3 qui ne redescendent jamais ;
  - des chapitres numérotés : définitions, théorèmes et démonstrations, exemples travaillés, code Python (NumPy / PyTorch / networkx…) ;
  - des encadrés de rappel quand une notion vient d'un cours qu'un étudiant peut ne pas avoir suivi ;
  - des exercices corrigés, gradués ★ / ★★ / ★★★ ;
  - une section **Projects and assessment** qui propose :
    - une évaluation classique cohérente avec la modalité officielle (barème, sujets types avec éléments de correction) ;
    - 3 à 5 projets individuels ou en groupe, sur données publiques et avec un calcul modeste ;
  - les références.
- **Projets de fin d'année** :
  - [Year-1 integrative projects](courses/m1-integrative-projects/index.html) : huit projets d'équipe qui combinent les cours de la première année ;
  - le catalogue de [capstones](courses/m2-projet-transverse/index.html#capstones) du projet transverse de M2.
- **Pages de cadrage** pour les modules non scientifiques :
  - management, langues, humanités, sport ;
  - stages ;
  - séminaire d'éthique, avec une carte des sujets de confiance et une page sur le droit (AI Act, RGPD).

Le site est en anglais uniquement (`specs/en-only.md`). L'ancien chemin `/en/` redirige vers la racine.

## Structure du dépôt

```
index.html                    Page d'accueil (racine GitHub Pages)
assets/paper.css              Feuille de style unique : fort contraste, clair / sombre, mobile
assets/theme.js               Barre supérieure, sommaire latéral, thème, tableaux
courses/<module>/index.qmd    Source Quarto d'un module
courses/<module>/index.html   Page rendue (publiée)
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
4. Mettre à jour le tableau du programme de l'accueil si un plan de séances a changé : `python3 tools/programme_table.py`.

Un nouveau module ou une refonte importante commence par un contrat dans `specs/` (modèle : `specs/_template-module.md`). Les gates de `AGENTS.md` doivent être cochées avant la fusion.

## Contrats principaux

| Contrat | Objet |
|---|---|
| `specs/competency-tree.md` | source structurelle unique (wiki LLGA + catalogue SynapseS de l'année) |
| `specs/hours-and-progression.md` | volumes, plans de séances, progression de la difficulté |
| `specs/front-redesign.md` | contraste projecteur, mode sombre, sommaire, texte aéré |
| `specs/curriculum-coherence.md` | cohérence avec les objectifs du master, projets et évaluations, projets de fin d'année |
| `specs/en-only.md` | site en anglais uniquement |

## Sources officielles

- [Page du programme LLGA](https://programmes.polytechnique.edu/en/master/all-msct-specializations/large-language-models-graphs-and-applications-llga) (École Polytechnique)
- [Wiki du master, page curriculum](https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum)
- [Catalogue SynapseS 2026–2027](https://synapses.polytechnique.fr/catalogue/2026-2027)

## Licence

Le code et les notes de cours de ce dépôt sont distribués sous la [licence Apache 2.0](LICENSE). Copyright 2026 knoel99 et les contributeurs.

Exceptions :
- **Textes officiels cités** : les descriptions du programme, les fiches SynapseS et le wiki restent la propriété de leurs auteurs. Ils sont cités pour information, avec leur source.
- **Ressources tierces** : KaTeX (licence MIT) est chargé depuis jsDelivr. Les jeux de données cités dans les projets ont leurs propres licences, indiquées sur chaque fiche de projet.
