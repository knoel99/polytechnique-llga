# Contrat — clarté cours scientifiques (lot D4 / D4a / D4b)

## Intent
Lot **D4** : purge globale de la voix institutionnelle (« équipe pédagogique » / « teaching team ») + clarification empirique du **reste** du catalogue scientifique hors D1–D3. Voix Extrapolons ; public ingénieur ~10 ans XP.

## Découpage
| Sous-lot | Contenu | Statut |
|---|---|---|
| **D4a** | Purge voix **globale** FR+EN + clarté fort/moyen sur moitié cœur restante | ✅ mergé (PR #12) |
| **D4b** (ce PR) | Clarté empirique modules sci restants | → merge |

## D4a — clarté modules (FR+EN) — done
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

## D4b — clarté modules restants (FR+EN)
Ajout seulement : **Public** ingénieur ~10 ans · **Empirique d'abord** · **Ce qui casse / What breaks** (ch.1) · **Note Extrapolons** si manquant — sans monolithe opaque.

| ID | Notes |
|---|---|
| `m1p1-shapes` | |
| `m1p1-tda` | |
| `m1p1-signal-processing` | |
| `m1p1-dbms` | |
| `m1p1-computer-animation` | |
| `m1p2-image-synthesis` | + tag → Note Extrapolons |
| `m1p2-optimization-ai` | + tag → Note Extrapolons |
| `m1p2-statistics-in-action` | |
| `m1p2-social-media-probabilistic` | |
| `m1p2-responsible-ai-sustainability` | + tag → Note Extrapolons |
| `m1p2-computer-vision-applications` | |
| `m1p2-deep-learning-p2` | + tag → Note Extrapolons |
| `m2-boosting-foundation-tabular` | + Note Extrapolons |
| `m2-control-generative-ai` | + Note Extrapolons |
| `m2-graph-generative-models` | + Note Extrapolons |
| `m2-explainability-security-privacy-llms` | + tag → Note Extrapolons |
| `m2-advanced-topics-llms` | + Note Extrapolons |

### Micro-fix inclus
- EN RL : TOC/h2 « Course research notes (Jesse Read): Jesse Read » → « Course research notes (Jesse Read) » (doublon nom).

### Micro-fix post-D4b
- `m1p2-realtime-ai-videogames` FR+EN : Public/Audience · Empirique/Empirical first · Ce qui casse/What breaks · Note Extrapolons (`feature/clarity-realtime-videogames`).

## Hors scope D4b
- paper.css / theme.js / TOC `ul` / dark-mobile (inchangés)
- Lot E (déjà mergé)
- Réécriture encyclopédique des chapitres

## Preuves « done »
### D4a
- [x] Spec `specs/clarity-lot-d4-rest.md`
- [x] Purge voix globale → 0 hits
- [x] 9 modules × FR+EN clarifiés
- [x] Branche `feature/clarity-d4-rest` → PR #12 → merge

### D4b
- [x] 17 modules × FR+EN (Public / Empirique / Ce qui casse / Note Extrapolons)
- [x] Fix doublon Jesse Read EN
- [x] Voix toujours 0 hits
- [x] Branche `feature/clarity-d4b` → PR → merge
