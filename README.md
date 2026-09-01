# polytechnique-llga

Supports de cours (tutoriels HTML) pour le master **MSc&T « Large Language Models, Graphs and Applications » (LLGA)** de l'École Polytechnique.

**Sites** : 🇫🇷 <https://knoel99.github.io/polytechnique-llga/> · 🇬🇧 <https://knoel99.github.io/polytechnique-llga/en/>

Chaque module est aligné sur la **fiche officielle SynapseS 2026-2027** (code UE, volume horaire, équipe pédagogique, objectifs et programme officiel avec tableau de correspondance vers nos sections, évaluation, prérequis).

## Objectif

Reconstituer, module par module, un **cours complet et auto-contenu** correspondant au *track recommandé* du master LLGA, destiné à un étudiant ayant **un bon niveau L3 de mathématiques**. Chaque module contient :

- les **rappels** de niveau L3 nécessaires (probabilités, algèbre linéaire, analyse, algorithmique…) ;
- le **cours proprement dit** (définitions, théorèmes, démonstrations, schémas) ;
- une section **« Travaux de l'équipe pédagogique »** intégrant les publications réelles des enseignants du master ;
- des **extraits de code Python** exécutables (NumPy / PyTorch / networkx…) ;
- des **exercices corrigés ou guidés** (≥ 8 par module) ;
- les **références** (livres et articles) réellement utilisées par les enseignants du master.

**L'index recense par ailleurs l'intégralité des cours de la brochure et du curriculum officiel** (options P1/P2, cours M2, management, transversal) ; les modules non rédigés dans ce dépôt y apparaissent en cartes grises « non couverts ». Les cours de gestion, de langues, de sport et d'humanités ne sont pas rédigés (seuls les cours scientifiques — mathématiques et informatique — le sont).

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
index.html              Page d'accueil (brochure cliquable : tronc commun + moments de choix)
assets/style.css        Feuille de style commune (layout tutoriel : volet sommaire + contenu)
tools/                  Scripts rejouables (découpe par section, insertion intros)
courses/<module>/       Un dossier par module :
  intro.html            Introduction : fiche du cours, objectifs, positionnement dans la formation, plan
  ch1.html … chN.html   Une page par section (rappels, chapitres)
  ex.html, refs.html    Exercices et références
```

Chaque page affiche un **volet sommaire à gauche** (section active surlignée) et le **contenu à droite** avec pager précédent/suivant. Le clic sur un cours dans l'index mène directement à son **introduction** (vue d'ensemble et intégration dans le master), puis à la première section.

## Sources

- Programme officiel : [curriculum MScT LLGA](https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum)
- Brochure : MSc&T Prospectus (École Polytechnique)
- Page programme : [LLGA | Polytechnique Program](https://programmes.polytechnique.edu/en/master/all-msct-specializations/large-language-models-graphs-and-applications-llga)

> Ces supports sont des **reconstitutions pédagogiques** rédigées à partir du programme public et des références standard de chaque domaine ; ils ne remplacent pas les cours officiels de l'École Polytechnique.
