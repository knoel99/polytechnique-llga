# polytechnique-llga

Supports de cours (tutoriels HTML) pour le master **MSc&T « Large Language Models, Graphs and Applications » (LLGA)** de l'École Polytechnique.

## Objectif

Reconstituer, module par module, un **cours complet et auto-contenu** correspondant au *track recommandé* du master LLGA, destiné à un étudiant ayant **un bon niveau L3 de mathématiques**. Chaque module contient :

- les **rappels** de niveau L3 nécessaires (probabilités, algèbre linéaire, analyse, algorithmique…) ;
- le **cours proprement dit** (définitions, théorèmes, démonstrations clés, schémas) ;
- des **extraits de code Python** exécutables (NumPy / PyTorch / networkx…) ;
- des **exercices corrigés ou guidés** ;
- les **références** (livres et articles) réellement utilisées par les enseignants du master.

Les cours de gestion, de langues, de sport et d'humanités ne sont pas couverts (seuls les cours scientifiques — mathématiques et informatique — le sont).

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
index.html          Page d'accueil (brochure cliquable)
assets/style.css    Feuille de style commune
courses/            Un fichier HTML par module
```

## Sources

- Programme officiel : [curriculum MScT LLGA](https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum)
- Brochure : MSc&T Prospectus (École Polytechnique)
- Page programme : [LLGA | Polytechnique Program](https://programmes.polytechnique.edu/en/master/all-msct-specializations/large-language-models-graphs-and-applications-llga)

> Ces supports sont des **reconstitutions pédagogiques** rédigées à partir du programme public et des références standard de chaque domaine ; ils ne remplacent pas les cours officiels de l'École Polytechnique.
