# Contrat — fix double numérotation des sommaires (TOC)

## Intent
Corriger l’affichage `1. 1. …` dans les sommaires de **tous** les cours FR+EN.

## Cause
`<nav class="toc"><ol>` auto-numérote **et** le texte des liens contient déjà `0. 1. 2. …` (numéros de chapitre intentionnels).

## Décision
Passer les TOC des pages cours à `<ul>` (sans numéros auto) et conserver les numéros dans le texte des liens — cohérent avec le style papier / chapitres `ch0`, `ch1`, ….  
Les TOC d’index (`index.html` / `en/index.html`) gardent `<ol>` (liens sans numéros préfixés).

## Fichiers
- `courses/**/index.html`, `en/courses/**/index.html` (80 pages)
- `assets/paper.css`, `en/assets/paper.css` (`.toc ul`)

## Preuves « done »
- [ ] Aucun `nav.toc` cours ne contient `<ol>`
- [ ] Extrait avant/après sur un cours FR + EN
- [ ] Dark/mobile : styles `.toc ul` présents
- [ ] Pas de régression sur les TOC index (`<ol>` conservé)
