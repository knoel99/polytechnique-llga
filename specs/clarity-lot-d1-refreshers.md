# Contrat — clarté cours scientifiques (lot D1)

## Intent
Premier lot **atomique** de clarification des supports **scientifiques** P1 : max compréhensibilité pour un·e ingénieur·e ~10 ans d'XP (pas doctorant dès la 1re ligne). Empirique d'abord ; exemples concrets (MNIST-like, chiffres, « ce qui casse »).

## Périmètre
| ID | FR | EN | Intensité |
|---|---|---|---|
| `m1p1-refresher-statistics` | oui | miroir | fort (ouverture + ch.1) |
| `m1p1-refresher-cs` | oui | miroir | fort (ouverture + ch.1) |
| `m1p1-refresher-neural-nets` | oui | miroir | léger (déjà clair) |
| `m1p1-machine-learning` | oui | miroir | moyen (entrée + note voix) |

## Hors scope
- Pas D2/D3 (DL, Graph, NLP, M2…).
- Pas redesign accueil, pas paper.css / theme.js / TOC `ul`.
- Pas réécriture encyclopédique des 10 chapitres — accroches + voix + pièges.

## Voix
- OK : Extrapolons / notes extrapolées, place dans le parcours 2 ans
- KO : « Le mot de l'équipe pédagogique » / teaching-team voice institutionnelle

## Preuves « done »
- [x] Spec `specs/clarity-lot-d1-refreshers.md`
- [x] 4 modules × FR+EN édités
- [x] Branche `feature/clarity-d1-refreshers` → PR → merge

> **EN-only (2026-09):** published FR mirror removed; canonical paths are root EN (`index.html`, `courses/`, `coherence-2years/`, `exit-capabilities/`). See `specs/en-only.md`.
