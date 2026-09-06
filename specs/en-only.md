# Contract — EN-only published site

## Intent
Make **English the canonical GitHub Pages site** at the repository root. Remove the published French mirror for now (git history keeps FR). No FR/EN language switcher.

## Decisions (Kim priority)
- Source of truth = **EN only until further notice**
- Prefer **clean deletion** of the public FR tree (not a confusing orphaned `en/` tree of full pages)
- Optional thin redirects for a few renamed/moved URLs; deeper old `/en/courses/…` may 404

## File moves
| Before | After |
|---|---|
| `en/index.html` | `index.html` (root) |
| `en/courses/**` | `courses/**` (replaces FR) |
| `en/exit-capabilities/` | `exit-capabilities/` |
| `en/coherence-2years/` | `coherence-2years/` |
| `en/assets/*` | dropped (root `assets/` kept; `theme.js` takes EN aria-labels) |

## Removals (published FR)
- Root FR `index.html`, FR `courses/**`
- FR `capacites-sortie/` content → stub redirect to `exit-capabilities/`
- FR `coherence-2ans/` content → stub redirect to `coherence-2years/`
- Full `en/` mirror pages → removed; `en/index.html` is a **redirect stub** to root only

## UI
- Remove all “Français” / lang switcher links
- `assets/theme.js` aria-label / title in English
- Crumbs / nav copy stay English

## Redirects / old URLs
| Old URL | Behavior |
|---|---|
| `/` and `/courses/…` | EN content (200) |
| `/en/index.html` | redirect → `/index.html` |
| `/en/courses/…` | **404** (documented; no stub tree) |
| `/capacites-sortie/` | redirect → `/exit-capabilities/` |
| `/coherence-2ans/` | redirect → `/coherence-2years/` |

## Out of scope
- Videos
- Large pedagogical rewrites — structure / language policy only

## “Done” proofs
- [x] Root pages are EN (`lang="en"`)
- [x] No remaining “Français” link text in HTML
- [x] `AGENTS.md` + `specs/` say EN-only
- [x] PR merged to `main` for Pages
