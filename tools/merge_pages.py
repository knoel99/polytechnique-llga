#!/usr/bin/env python3
"""Fusionne chaque module en une page unique (style Wikipédia).

Pour chaque dossier courses/<mod>/ (FR) et en/courses/<mod>/ (EN) :
  intro.html + ch*.html + ex.html + refs.html  ->  index.html
Gabarit minimal (paper.css, KaTeX), sommaire par ancres, suppression
des sidebars/pagers/breadcrumbs. Les anciens fichiers sont supprimés.
"""
import os, re, sys

ROOTS = [('courses', 'fr', 'Sommaire', 'Programme du master',
          'MSc&amp;T LLGA · Supports de cours'),
         ('en/courses', 'en', 'Contents', "Master's program",
          'MSc&amp;T LLGA · Course notes')]

def page_order(f):
    m = re.match(r'ch(\d+)\.html$', f)
    if f == 'intro.html': return (0, 0)
    if m: return (1, int(m.group(1)))
    if f == 'ex.html': return (2, 0)
    if f == 'code.html': return (3, 0)   # annexe code (ex. image-synthesis)
    if f == 'refs.html': return (4, 0)
    return (9, 0)

def extract(f):
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<main class="content">\s*(.*?)\s*(?:<nav class="pager">|</main>)', s, re.S)
    return m.group(1) if m else ''

def fix_links(body):
    # liens intra-module vers une autre page -> ancre de la page fusionnée
    body = re.sub(r'href="(intro|ex|refs|ch\d+)\.html(#[\w-]*)?"', r'href="#\2"', body)
    # liens inter-modules vers l'intro -> dossier (index.html)
    body = re.sub(r'href="(\.\./m[^"/]+)/intro\.html(#[\w-]*)?"', r'href="\1/\2"', body)
    return body

TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — LLGA</title>
<link rel="stylesheet" href="../../assets/paper.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}]}});"></script>
</head>
<body>
<p class="crumb"><a href="../../index.html">{brand}</a></p>
<main class="paper">
<h1>{title}</h1>
<p class="subtitle">{subtitle}</p>
<nav class="toc">
<p class="toc-title">{toc_title}</p>
<ol>
{toc_items}
</ol>
</nav>
{sections}
</main>
<footer class="foot">
<p><a href="../../index.html">← {back}</a></p>
</footer>
</body>
</html>
'''

def merge_module(d, lang, toc_title, back, brand):
    files = sorted((f for f in os.listdir(d) if f.endswith('.html')
                    and re.fullmatch(r'intro|ch\d+|ex|code|refs', f[:-5])), key=page_order)
    if not files or 'intro.html' not in files:
        return None
    intro = open(os.path.join(d, 'intro.html'), encoding='utf-8').read()
    mh = re.search(r'<a class="sidebar-home"[^>]*><span class="code-mini">([^<]*)</span>([^<]*)</a>', intro)
    code, title = (mh.group(1).strip(), mh.group(2).strip()) if mh else ('', os.path.basename(d))
    mt = re.search(r'<div class="t2">([^<]*)</div>', intro)
    period = mt.group(1).strip() if mt else ''

    sections, toc = [], []
    for f in files:
        body = fix_links(extract(os.path.join(d, f)))
        sid = re.search(r'<section[^>]*\bid="([\w-]+)"', body)
        sid = sid.group(1) if sid else f[:-5]
        if f == 'ex.html':  # promouvoir le titre h3 en h2 pour l'homogénéité
            body = re.sub(r'<h3>(Exercis[^<]*)</h3>', r'<h2>\1</h2>', body, count=1)
        lab = re.search(r'<h[23][^>]*>([^<]+)</h[23]>', body)
        toc.append((sid, lab.group(1) if lab else f[:-5]))
        sections.append(body)

    subtitle = ' · '.join(x for x in (code, period) if x)
    toc_items = '\n'.join(f'<li><a href="#{i}">{l}</a></li>' for i, l in toc)
    page = TEMPLATE.format(lang=lang, title=title, subtitle=subtitle, brand=brand,
                           toc_title=toc_title, toc_items=toc_items,
                           back=back, sections='\n'.join(sections))
    out = os.path.join(d, 'index.html')
    open(out, 'w', encoding='utf-8').write(page)
    for f in files:
        os.remove(os.path.join(d, f))
    return (out, len(files))

if __name__ == '__main__':
    total = 0
    for root, lang, toc_title, back, brand in ROOTS:
        n = 0
        for mod in sorted(os.listdir(root)):
            r = merge_module(os.path.join(root, mod), lang, toc_title, back, brand)
            if r: n += 1; total += 1
        print(f'{root}: {n} modules fusionnes')
    print(f'TOTAL: {total} pages uniques creees')
