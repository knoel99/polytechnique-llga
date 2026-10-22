# polytechnique-llga

Supports de cours (tutoriels HTML) pour le master **MSc&T « Large Language Models, Graphs and Applications » (LLGA)** de l'École Polytechnique.

**Site (EN only)** : <https://knoel99.github.io/polytechnique-llga/>  
Former `/en/` URLs redirect to the root (homepage stub); deeper `/en/courses/…` paths are retired (404). Former FR paths `capacites-sortie/` and `coherence-2ans/` redirect to `exit-capabilities/` and `coherence-2years/`.

Chaque module est aligné sur la **fiche officielle SynapseS 2026-2027** (code UE, volume horaire, équipe pédagogique, objectifs et programme officiel avec tableau de correspondance vers nos sections, évaluation, prérequis).

## Objectif

Reconstituer, module par module, un **cours complet et auto-contenu** correspondant au *track recommandé* du master LLGA, destiné à un étudiant ayant **un bon niveau L3 de mathématiques**. Chaque module contient :

- les **rappels** de niveau L3 nécessaires (probabilités, algèbre linéaire, analyse, algorithmique…) ;
- le **cours proprement dit** (définitions, théorèmes, démonstrations, schémas) ;
- une section **« Travaux de l'équipe pédagogique »** intégrant les publications réelles des enseignants du master ;
- des **extraits de code Python** exécutables (NumPy / PyTorch / networkx…) ;
- des **exercices corrigés ou guidés** (≥ 8 par module) ;
- les **références** (livres et articles) réellement utilisées par les enseignants du master.

**L'index recense par ailleurs l'intégralité des cours de la brochure et du curriculum officiel** (options P1/P2, cours M2, management, transversal) ; les modules non rédigés dans ce dépôt y apparaissent en cartes grises « non couverts ». Les cours scientifiques (mathématiques et informatique) sont rédigés en profondeur ; les pages management / transversal / stages / séminaire éthique sont des **cadrages Extrapolons** (pas des polycopiés complets).

## Le track recommandé

La sélection suit le **« profil équilibré » recommandé** pour ce master (analyse du curriculum officiel) :

| Période | Modules |
|---|---|
| **M1 · P1** | Refresher Statistics · Refresher CS · **Machine Learning** (obligatoire) · **Deep Learning** · **Signal Processing** · **Emerging Subjects in ML & Collaborative Learning** |
| **M1 · P2** | **RL & Autonomous Agents** (obligatoire) · **Graph ML & DL for Generative AI** (obligatoire, cours central) · **Text Mining & NLP** (obligatoire) · **Computational Optimal Transport** · **Multimodal Generative AI** |
| **M2** | **Large Language Models** · **Advanced Graph Neural Networks** · **Analysis & Deep Learning on Geometric Data** |

Cette sélection correspond aux tracks *« Graph AI / Structured Generative AI »* et *« Hybrid Neuro-Symbolic / GraphRAG »* — le cœur du master : **faire cohabiter LLMs et données structurées en graphes**.

## Volume horaire et progression (programme 2026-2027)

- La page d'accueil contient un tableau **« Programme 2026–2027 : course units and hours »** : chaque UE de la liste SynapseS du parcours LLGA (année 1, semestres S1 et S2), son code, sa période, son volume officiel, et la façon dont nos notes s'y ajustent. Une liste « What changed » résume les évolutions du catalogue (nouveau *Refresher in Computer Graphics*, *Optimisation and Responsible AI* passé en période 1 sous `CSC_51076_EP`, liste S2 à neuf UE, codes des UE de management et de culture, année 2 pas encore publiée).
- Chaque cours scientifique a un **plan de séances** (`#sessions`) dont les heures totalisent le volume officiel (12 × 3 h pour 36 h, 4 × 3 h pour un refresher de 12 h, 8 × 3 h pour un cours de M2), avec un niveau 1/2/3 qui ne redescend jamais. Les chapitres qui dépassent ce volume (notes de recherche, approfondissements) sont listés en travail personnel avec une durée estimée.
- Règles et preuves : `specs/hours-and-progression.md`, contrôle `python3 tools/check_progression.py` (lancé aussi par `tools/check_gates.py`).
- Outils : `tools/render.py` (rendu Quarto 1.7.32 + empreinte KaTeX), `tools/renumber_chapters.py`, `tools/grade_exercises.py`, `tools/cross_refs.py`, `tools/programme_table.py`.

## Utilisation

Ouvrir `index.html` dans un navigateur, ou tout simplement consulter la liste des modules ci-dessous. Les formules mathématiques sont rendues par [KaTeX](https://katex.org) 0.19.0, chargé depuis jsDelivr avec une empreinte d'intégrité (une connexion internet reste utile ; le texte reste lisible hors ligne).

## Structure

```
index.html                 English homepage (canonical GitHub Pages root)
assets/paper.css           Single stylesheet (high contrast, light/dark, mobile)
assets/theme.js            Theme button, side contents, tables (English UI)
exit-capabilities/         Exit capabilities synthesis
coherence-2years/          Two-year pedagogical coherence
courses/<module>/index.html  One long page per module
specs/                     Spec contracts (EN-only policy: specs/en-only.md)
tools/                     Replayable scripts
```

Chaque cours est **une longue page unique** (comme un article Wikipédia) : sommaire en tête, sections numérotées N.k., encadrés définitions/théorimes style LaTeX, formules rendues par KaTeX. Le clic sur un cours dans l'index mène directement à cette page.

## Sources

- Programme officiel : [curriculum MScT LLGA](https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum)
- Brochure : MSc&T Prospectus (École Polytechnique)
- Page programme : [LLGA | Polytechnique Program](https://programmes.polytechnique.edu/en/master/all-msct-specializations/large-language-models-graphs-and-applications-llga)

> Ces supports sont des **reconstitutions pédagogiques** rédigées à partir du programme public et des références standard de chaque domaine ; ils ne remplacent pas les cours officiels de l'École Polytechnique.


## Apparence (dark mode & mobile)

- `assets/paper.css` : thème à **fort contraste** (texte ≥ 7:1, lisible au vidéoprojecteur), **dark** via `prefers-color-scheme` et `data-theme`, encadrés colorés par type, styles **responsive** (code, tableaux, KaTeX). Règles : `specs/front-redesign.md`.
- `assets/theme.js` : barre supérieure (bouton *Contents*, section en cours, bouton *Dark/Light* avec persistance `localStorage` `llga-theme`), sommaire latéral toujours visible sur grand écran et en tiroir sur mobile, tableaux défilants.
- `tools/check_airiness.py` : contrôle d'aération du texte (paragraphe ≤ 100 mots, ≤ 6 formules en ligne, formule en ligne ≤ 50 caractères TeX, sinon formule centrée sur sa propre ligne).

## Gouvernance Spec-Driven / BMAD (légère)

Ce n’est pas un monorepo app : on garde un flux **spec → implement → prove** adapté aux cours HTML.

- **`AGENTS.md`** — gates obligatoires (contrat, EN-only root, index, dark/mobile, preuves PR).
- **`specs/`** — contrats de module (modèle `_template-module.md`).
- Installation **optionnelle** de Spec Kit / `bmad-speckit-sdd-flow` : instructions dans `AGENTS.md`. Sans CLI, les gates + `specs/` suffisent.
