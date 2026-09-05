# AGENTS.md — gates Spec-Driven / BMAD (léger) pour polytechnique-llga

Ce dépôt est un **site de supports HTML** (GitHub Pages), pas un monorepo applicatif.
On encode ici une base **Spec Kit–compatible** et **BMAD-inspired** (spec → plan → implement → prove), sans installer obligatoirement la CLI Spec Kit / bmad-speckit-sdd-flow.

## Principes

1. **Contrat avant gros rewrite** — tout nouveau module ou refonte majeure commence par un contrat dans `specs/` (voir modèle).
2. **Preuves avant « done »** — une PR n’est « done » que si les gates ci-dessous sont cochées dans la description de PR.
3. **Pas d’invention de codes UE** — hors brochure = badge explicite, pas de faux code SynapseS.
4. **Parité FR/EN** — chaque page de cours ajoutée ou profondément modifiée a son miroir `en/…`.
5. **Look papier** — `assets/paper.css` (et `en/assets/paper.css`) restent la source de vérité visuelle ; le light mode « LaTeX » ne doit pas régresser.

## Gates obligatoires (Definition of Done)

Avant de merger un module / une refonte CSS :

- [ ] **Contrat** : `specs/<module-id>.md` présent (ou mise à jour) pour un nouveau cours / rewrite > ~screen.
- [ ] **Pages** : `courses/<id>/index.html` **et** `en/courses/<id>/index.html`.
- [ ] **Index** : liens dans `index.html` et `en/index.html` (zone P1/P2/M2 correcte ; statut honnête).
- [ ] **CSS** : dark (`prefers-color-scheme` / `data-theme`) + mobile (pas d’overflow horizontal bloquant ; tableaux / code / KaTeX scrollables) vérifiés sur une page cours + l’index.
- [ ] **Thème** : `assets/theme.js` (+ miroir `en/assets/`) chargé ; toggle localStorage OK.
- [ ] **Pédagogie** : ≥ 6 exercices ; NumPy primaire si module NN/ML ; ton phrases complètes FR/EN.
- [ ] **Smoke** : ouvrir FR + EN en local (ou Pages preview) ; KaTeX et encadrés `.def`/`.thm`/`.note` lisibles en dark.

## Activer Spec Kit / BMAD (optionnel)

Ce dépôt **n’installe pas** automatiquement Spec Kit. Pour un flux SDD outillé sur une machine de dev :

```bash
# Spec Kit (GitHub / specify CLI) — si vous l’utilisez déjà ailleurs
# https://github.com/github/spec-kit  (ou distribution Spec Kit de votre org)
# Exemple indicatif :
#   uvx --from git+https://github.com/github/spec-kit.git specify init
# Puis pointer les artefacts vers specs/ de ce repo.

# Variante BMAD + Spec Kit SDD flow (si package dispo dans votre environnement) :
#   npx bmad-speckit-sdd-flow   # ou l’installateur documenté par votre équipe
```

Si la CLI n’est pas installée, **les gates de ce fichier + le contrat `specs/` suffisent** : c’est le mode par défaut pour les agents Cursor travaillant sur ce repo.

## Workflow agent recommandé (BMAD light)

| Phase | Sortie |
|---|---|
| **Spec** | Remplir / amender `specs/<id>.md` (objectifs, hors-brochure?, outline, preuves). |
| **Plan** | Lister fichiers touchés (FR, EN, index×2, CSS/JS si besoin). |
| **Implement** | Écrire HTML + liens ; pas de CloudAgent sauf demande explicite. |
| **Prove** | Cocher les gates ; coller le résumé de preuves dans la PR. |

## Fichiers clés

- `assets/paper.css` / `en/assets/paper.css` — style papier, dark, mobile
- `assets/theme.js` / `en/assets/theme.js` — toggle thème persistant
- `specs/README.md` — index des contrats
- `specs/_template-module.md` — modèle de contrat
