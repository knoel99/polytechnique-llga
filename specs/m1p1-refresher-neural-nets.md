# Contrat module — `m1p1-refresher-neural-nets`

## Intent
- **Public** : ingénieur·e ~10 ans, NumPy MLP MNIST déjà fait (`knoel99/MNIST`), pas de nanoGPT/LLM training.
- **Période** : M1 · P1 — on-ramp avant Deep Learning / Graph ML / LLMs.
- **Hors brochure** : **oui** — support pédagogique du dépôt, **aucun code UE SynapseS**.

## Outcomes
- Diagnostiquer un train loop MLP (forward, CE, SGD) qui casse.
- Backprop à la main + NumPy ; init He/Xavier ; SGD→Adam.
- Toy attention → intuition transformer/LLM sans cloner nanoGPT.
- Carte mentale LLGA (refreshers → ML → DL → Graph/NLP → M2 LLM).

## Outline
1. Relire le MLP MNIST (empirique)
2. Forward / loss / pannes
3. Rétropropagation
4. Activations & initialisation
5. Optimisation pratique
6. Toy-transformer / attention
7. Insertion parcours LLGA
8. Exercices (≥ 6) + références

## Preuves « done »
- [x] `courses/m1p1-refresher-neural-nets/index.html`
- [x] `en/courses/m1p1-refresher-neural-nets/index.html`
- [x] Liens index FR + EN (statut hors brochure)
- [x] ≥ 6 exercices (8)
- [x] Dark/mobile via `assets/paper.css` + `theme.js` (miroirs `en/assets/`)
- [x] Light mode papier préservé (`:root` inchangé en light)
