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

## Utilisation

Ouvrir `index.html` dans un navigateur, ou tout simplement consulter la liste des modules ci-dessous. Les formules mathématiques sont rendues par [KaTeX](https://katex.org) (chargé via CDN — une connexion internet est donc utile, le contenu reste lisible hors ligne).

## Structure

```
index.html                 English homepage (canonical GitHub Pages root)
assets/paper.css           Single stylesheet (minimal, LaTeX/Wikipedia-like)
assets/theme.js            Theme toggle (English UI)
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

- `assets/paper.css` : thème clair « papier / LaTeX », **dark** via `prefers-color-scheme` et `data-theme`, plus styles **responsive** (TOC, code, tableaux, KaTeX).
- `assets/theme.js` : bouton de bascule clair/sombre avec persistance `localStorage` (`llga-theme`).

## Gouvernance Spec-Driven / BMAD (légère)

Ce n’est pas un monorepo app : on garde un flux **spec → implement → prove** adapté aux cours HTML.

- **`AGENTS.md`** — gates obligatoires (contrat, EN-only root, index, dark/mobile, preuves PR).
- **`specs/`** — contrats de module (modèle `_template-module.md`).
- Installation **optionnelle** de Spec Kit / `bmad-speckit-sdd-flow` : instructions dans `AGENTS.md`. Sans CLI, les gates + `specs/` suffisent.
