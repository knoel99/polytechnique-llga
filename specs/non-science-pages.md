# Contrat — pages non scientifiques (lot A)

## Intent
Créer des pages de **cadrage** (voix Extrapolons) pour les lignes brochure **non scientifiques** encore `.nc` dans l’index : management, transversal (sports / humanités / langues), stages, séminaire éthique, projet transverse.

## Hors scope
- Pas de pages pour les options brochure « Machine and Deep Learning » / « Found. of ML » déjà couvertes par les cours ML/DL liés → laisser `.nc` + `title` hint.
- Pas de redesign accueil, pas de refonte cours scientifiques, pas de « cohérence 2 ans » hors liens de positionnement.

## Voix
- OK : Extrapolons / notes extrapolées, place dans le parcours 2 ans, lien industrie/recherche
- KO : voix équipe pédagogique / institutionnelle ; faux codes UE

## Pages (FR + miroir EN)
| ID | Index |
|---|---|
| `m1p1-strategy-marketing` | M1 P1 management |
| `m1-sports` | M1 + M2 (page partagée) |
| `m1-humanites` | M1 + M2 (page partagée) |
| `m1-langues` | M1 + M2 (page partagée) |
| `m1p2-startup-entrepreneurship` | M1 P2 management |
| `m1p3-research-internship` | M1 P3 stage 20 ECTS |
| `m2-ethical-issues-ai` | M2 séminaire 6 ECTS |
| `m2-projet-transverse` | M2 projet 8 ECTS |
| `m2-internship` | M2 stage 24 ECTS |

## Preuves « done »
- [x] `courses/<id>/index.html` + `en/courses/<id>/index.html` (×9)
- [x] Liens `index.html` + `en/index.html` ; retrait `nc` sur cibles
- [x] FOUC + `theme.js` + `paper.css` ; TOC
- [x] 2 `.nc` restants (options ML brochure)
