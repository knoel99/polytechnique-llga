# Contrat — refonte accueil + illustrations (lot C)

## Intent
Refonte sobre de `index.html` (FR) et `en/index.html` (EN) : hero court, structure scannable (cartes / timeline par période), illustrations discrètes Graph×LLM, sans framework CSS lourd.

## Hors scope
- Lot D (clarté cours scientifiques)
- Lot E (cohérence parcours 2 ans)
- Changement de contenu pédagogique des pages cours

## UI (à respecter)
- Hero : titre court, 2–3 lignes pitch, lien EN/FR, CTA Année 1 / track recommandé, lien capacités-sortie / exit-capabilities
- Remplacer le mur de tables par cartes M1-P1 · M1-P2 · M1-P3 · M2-P1 · M2-P2 · suite
- Conservations : tous les liens cours existants (y compris pages non-sci) ; 2 `.nc` options ML brochure en hint discret
- Fond pédagogique Graph+LLM + hints brochure vs curriculum, plus léger
- Typo/espacement `paper.css` ; dark/mobile renforcés si besoin
- Illustrations discrètes, cohérentes light/dark ; licence claire dans `assets/`

## Voix
- OK : Extrapolons / notes de travail
- KO : voix équipe pédagogique / institutionnelle

## Fichiers
| Fichier | Rôle |
|---|---|
| `index.html` / `en/index.html` | Accueil refondu |
| `assets/paper.css` (+ miroir `en/`) | Styles hero, cartes, illu |
| `assets/illu-*.svg` (+ attribution) | Illustrations |
| `specs/homepage-redesign.md` | Ce contrat |

## Preuves « done »
- [x] Contrats + README specs
- [x] FR + EN index scannables (cartes)
- [x] Liens cours + non-sci OK ; 2 `.nc` conservés
- [x] Dark / mobile / theme.js smoke
- [x] Licences images documentées
- [x] PR mergée sur `main`
