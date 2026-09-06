# Contrat — cohérence pédagogique 2 ans (lot E)

## Intent
Livrable transversal : une page (FR + miroir EN) qui analyse la **cohérence pédagogique** du parcours LLGA sur M1+M2, pour un·e ingénieur·e ~10 ans d’XP. Empirique d’abord (cartes / tableaux scannables) ; liens vers pages cours réelles ; ton **Extrapolons** (notes de parcours inférées), pas voix équipe pédagogique / diplôme officiel.

## Périmètre
| Artefact | Chemin |
|---|---|
| Page (EN canonical) | `coherence-2years/index.html` |
| Legacy FR path | `coherence-2ans/index.html` (redirect stub) |
| Index link | root `index.html` |
| Spec | ce fichier + entrée `specs/README.md` |

## Contenu attendu
- Place des refreshers → ML → DL → Graph ML / NLP / OT → M2 LLM / GNN / geometric / privacy…
- Prérequis croisés, trous éventuels, redondances, ponts (y compris refresher neural-nets hors brochure + capacités-sortie)
- Tableaux / cartes paper.css ; pas de redesign CSS global

## Hors scope
- Ne pas rouvrir D1–D3 sauf lien cassé bloquant
- Pas de faux codes UE ; hors brochure = badge explicite
- Pas de voix « mot de l’équipe pédagogique »

## Voix
- OK : Extrapolons / notes extrapolées, place dans le parcours 2 ans
- KO : exigences officielles du diplôme, « teaching team voice »

## Preuves « done »
- [x] Spec + README specs
- [x] Pages FR + EN
- [x] Liens depuis index FR/EN
- [x] Branche `feature/coherence-2ans` → PR → **merge immédiat**

> **EN-only (2026-09):** published FR mirror removed; canonical paths are root EN (`index.html`, `courses/`, `coherence-2years/`, `exit-capabilities/`). See `specs/en-only.md`.
