# Contrat — clarté cours scientifiques (lot D4 / D4a)

## Intent
Lot **D4** : purge globale de la voix institutionnelle (« équipe pédagogique » / « teaching team ») + clarification empirique du **reste** du catalogue scientifique hors D1–D3. Voix Extrapolons ; public ingénieur ~10 ans XP.

## Découpage
| Sous-lot | Contenu | Statut |
|---|---|---|
| **D4a** (ce PR) | Purge voix **globale** FR+EN + clarté fort/moyen sur moitié cœur restante | → merge |
| **D4b** (suivant) | Clarté empirique modules sci restants (shapes, TDA, signal, DBMS, animation, image synthesis, opt AI, stats in action, social media, responsible AI, CV apps, DL P2, boosting, control genAI, graph generative, explainability, advanced topics LLMs, …) | à faire |

## D4a — clarté modules (FR+EN)
| ID | Intensité |
|---|---|
| `m1p2-reinforcement-learning` | fort (ouverture + ch.1) + soft lab Jesse Read |
| `m1p2-multimodal-genai` | fort + soft Kalogeiton |
| `m1p2-advanced-deep-learning` | fort + soft Kalogeiton/Lutzeyer/Zhu |
| `m2-geometric-deep-learning` | fort + soft GDA Ovsjanikov |
| `m1p1-emerging-ml` | fort + soft CMAP |
| `m2-mlops-llm-engineering` | fort |
| `m2-privacy-uncertainty` | fort |
| `m2-security-robustness` | fort |
| `m2-speech-technology` | fort |

## D4a — purge voix (tous `courses/**` + `en/courses/**`)
- Titres / TOC / plan / h2 : « Travaux de l'équipe pédagogique » / « Research of the teaching team » → lab nommé (DaSciM, CMAP, CEDAR, Datashapes, ORAILIX, GDA, …) ou « Travaux / recherche (équipe du cours) » / « Course research notes »
- Tags : « Le mot de l'équipe pédagogique » / « A word from the teaching team » / « Le positionnement LLGA » → **Note Extrapolons**
- Soft staff tables : « équipe d'ingénierie pédagogique » → « intervenants » ; EN « teaching team » → « instructors » / « course instructors »
- Cible : hits « équipe pédagogique » / « teaching team » → **0**

## Hors scope D4a
- Modules sci listés en D4b (clarté Empirique / Ce qui casse)
- paper.css / theme.js / TOC `ul` / dark-mobile (inchangés)
- Lot E (déjà mergé)

## Preuves « done » D4a
- [x] Spec `specs/clarity-lot-d4-rest.md`
- [x] Purge voix globale → 0 hits
- [x] 9 modules × FR+EN clarifiés (Public / Empirique / Ce qui casse / Note Extrapolons)
- [x] Branche `feature/clarity-d4-rest` → PR → merge
