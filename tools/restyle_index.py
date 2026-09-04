#!/usr/bin/env python3
"""Restyle les pages d'index (FR + EN) en minimaliste paper.css.

Construit un arbre DOM léger (html.parser + offsets du source) pour
extraire fidèlement : h1, lead, track-box, légende, bandes d'année,
périodes, groupes (titres, moments de choix avec hint, cartes).
Émet une page sobre : h2/h3/h4, listes de cours, sommaire par ancres.
"""
import html.parser, re

class N:
    __slots__ = ('tag', 'attrs', 'start', 'end', 'children', 'parent')
    def __init__(s, tag, attrs, start, end, parent):
        s.tag, s.attrs, s.start, s.end, s.children, s.parent = tag, attrs, start, end, [], parent
    def cls(s): return s.attrs.get('class', '')
    def kid(s, tag, cls=None):
        for c in s.children:
            if c.tag == tag and (cls is None or cls in c.cls().split()):
                return c
    def inner(s, src):
        if s.tag == '#text': return ''
        gt = src.find('>', s.start)
        return src[gt + 1:s.end - (3 + len(s.tag))] if gt >= 0 else ''
    def text(s, src):
        return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s.inner(src))).strip()

VOID = {'br', 'img', 'meta', 'link', 'hr', 'input', 'col', 'area', 'base',
        'embed', 'source', 'track', 'wbr'}

def parse(src):
    offs = [0]
    for line in src.split('\n'):
        offs.append(offs[-1] + len(line) + 1)
    off = lambda row, col: offs[row - 1] + col
    root = N('#root', {}, 0, len(src), None)
    stack = [root]
    class P(html.parser.HTMLParser):
        def handle_starttag(self, tag, attrs):
            n = N(tag, dict(attrs), off(*self.getpos()), len(src), stack[-1])
            stack[-1].children.append(n)
            if tag not in VOID:
                stack.append(n)
        def handle_endtag(self, tag):
            for i in range(len(stack) - 1, 0, -1):
                if stack[i].tag == tag:
                    stack[i].end = off(*self.getpos()) + 3 + len(tag)
                    del stack[i:]
                    return
    p = P(convert_charrefs=True); p.feed(src); p.close()
    return root

def flatten(n, src):
    """Titre de groupe : texte principal conservé, span en/fr retiré,
    chips (tronc commun, curriculum) mises entre parenthèses."""
    h = n.inner(src)
    h = re.sub(r'<span class="en"[^>]*>.*?</span>', ' ', h, flags=re.S)
    h = re.sub(r'<span class="(?:core-chip|choice-tag)"[^>]*>(.*?)</span>', r'(\1)', h, flags=re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()

def card(n, src):
    ghost = 'ghost' in n.cls().split()
    code = n.kid('span', 'code'); h3 = n.kid('h3'); meta = n.kid('div', 'meta')
    desc = n.kid('div', 'desc'); foot = n.kid('div', 'foot')
    marks = []
    if foot:
        for sp in foot.children:
            if sp.tag == 'span' and ('badge' in sp.cls() or 'chip' in sp.cls()):
                marks.append(sp.text(src))
    return dict(ghost=ghost,
                href=None if ghost else n.attrs.get('href'),
                code=None if ghost else (code.text(src) if code else ''),
                title=h3.text(src) if h3 else '?',
                meta=meta.text(src) if meta else '',
                desc=re.sub(r'\s+', ' ', desc.inner(src)).strip() if desc else '',
                marks=[re.sub(r'\s+', ' ', m).strip() for m in marks])

def li(c):
    href = c['href'].rstrip('/') + '/index.html' if c['href'] else None
    t = f'<a href="{href}">{c["title"]}</a>' if href else c['title']
    bits = ' · '.join(x for x in [c['code'], c['meta']] if x)
    head = f'{t} <span class="code-mini">{bits}</span>' if bits else t
    if c['marks']:
        head += f' — <em>{" · ".join(c["marks"])}</em>'
    body = f'\n<span class="d">{c["desc"]}</span>' if c['desc'] else ''
    return f'<li{" class=\"nc\"" if c["ghost"] else ""}>{head}{body}</li>'

def period_body(per, src, repls):
    out, cards_n = [], 0
    cur_title, cur_hint = None, None
    def flush():
        nonlocal cur_title, cur_hint
        if cur_title is None: return
        out.append(f'<h4>{cur_title}</h4>')
        if cur_hint:
            out.append(f'<p class="hint">{cur_hint}</p>')
        cur_title, cur_hint = None, None
    def emit_grid(g):
        nonlocal cards_n, cur_title
        cards = [card(k, src) for k in g.children
                 if k.tag in ('a', 'div') and 'card' in k.cls().split()]
        cards_n += len(cards)
        if cur_title is None: cur_title = 'Cours'
        flush()
        out.append('<ul class="courses">\n' + '\n'.join(li(x) for x in cards) + '\n</ul>')
    for c in per.children:
        if c.tag == 'div' and 'group-title' in c.cls().split():
            flush(); cur_title = flatten(c, src)
        elif c.tag == 'div' and 'choice-group' in c.cls().split():
            h = c.kid('div', 'choice-head')
            sp = h.kid('span', 'hint') if h else None
            cur_hint = apply_repls(re.sub(r'\s+', ' ', sp.inner(src)).strip().replace('&nbsp;', ' '), repls) if sp else ''
            for k in c.children:
                if k.tag == 'div' and 'grid' in k.cls().split():
                    emit_grid(k)
        elif c.tag == 'div' and 'grid' in c.cls().split():
            emit_grid(c)
    flush()
    return out, cards_n

TOC_LABELS = {
    'fr': {'a2suite': 'Séminaire · Apprentissage transversal · Stage'},
    'en': {'a2suite': 'Seminar · Transverse learning · Internship'},
}

def apply_repls(s, repls):
    for a, b in repls:
        s = s.replace(a, b)
    return s

def build(path, lang, css, other_href, other_label, brand, repls):
    src = open(path, encoding='utf-8').read()
    root = parse(src)
    def find_rec(n, tag, cls=None):
        if n.tag == tag and (cls is None or cls in n.cls().split()):
            return n
        for c in n.children:
            r = find_rec(c, tag, cls)
            if r: return r
    body = find_rec(root, 'body')

    def one(sel):
        n = find_rec(body, *sel)
        return re.sub(r'\s+', ' ', n.inner(src)).strip()

    h1 = one(('h1',)); lead = one(('p', 'lead'))
    legend = one(('div', 'legend'))
    tb = find_rec(body, 'div', 'track-box')
    track_title = tb.kid('h2').text(src)
    track_html = re.sub(r'\s+', ' ', tb.inner(src)).strip()
    track_html = track_html[len(re.search(r'^<h2>.*?</h2>', track_html).group(0)):] if track_html.startswith('<h2>') else track_html
    foot = re.sub(r'\s+', ' ', find_rec(body, 'footer').kid('p').inner(src)).strip()
    lead, legend, foot = (apply_repls(x.replace('&nbsp;', ' '), repls) for x in (lead, legend, foot))

    toc, out = [], []
    out.append(f'<h2 id="track">{track_title}</h2>\n{track_html}')
    toc.append(f'<li><a href="#track">{track_title}</a></li>')
    total = 0
    depth = False
    for c in body.children:
        if c.tag == 'div' and 'year-band' in c.cls().split():
            if depth: toc.append('</ol></li>')
            y = c.kid('span', 'y'); s_ = c.kid('span', 's')
            ylab = y.text(src)
            ylab = ylab.capitalize() if ylab.isupper() else ylab
            out.append(f'<h2 id="{c.attrs.get("id","")}">{ylab} '
                       f'<span class="sub">— {s_.text(src)}</span></h2>')
            toc.append(f'<li><a href="#{c.attrs.get("id","")}">{ylab}</a><ol>')
            depth = True
        elif c.tag == 'section' and 'period' in c.cls().split():
            pid = c.attrs.get('id', '')
            h2 = c.kid('h2')
            title_raw = re.sub(r'<span class="sub">.*?</span>', '', h2.inner(src), flags=re.S)
            sub = h2.kid('span', 'sub')
            subh = f' <span class="sub">— {re.sub(r"<[^>]+>", " ", sub.inner(src))}</span>' if sub else ''
            t = re.sub(r'\s+', ' ', title_raw).strip()
            label = TOC_LABELS[lang].get(pid) or (t.capitalize() if t.isupper() else t)
            toc.append(f'<li><a href="#{pid}">{label}</a></li>')
            out.append(f'<h3 id="{pid}">{t}{subh}</h3>')
            blocks, n = period_body(c, src, repls)
            out.extend(blocks); total += n
    if depth:
        toc.append('</ol></li>')

    page = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{re.sub(r"<[^>]+>", "", h1)} — LLGA</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<p class="crumb">{brand} · <a href="{other_href}" lang="{'fr' if lang == 'en' else 'en'}">{other_label}</a></p>
<main class="paper">
<h1>{h1}</h1>
<p class="lead">{lead}</p>
<nav class="toc">
<p class="toc-title">{'Contents' if lang == 'en' else 'Sommaire'}</p>
<ol>
{chr(10).join(toc)}
</ol>
</nav>
{chr(10).join(out)}
</main>
<footer class="foot">
<p>{foot}</p>
</footer>
</body>
</html>
'''
    open(path, 'w', encoding='utf-8').write(page)
    return total, len(legend)

REPLS_FR = [
    ("sont rédigés en profondeur (cartes blanches cliquables) :",
     "sont rédigés en profondeur (liens) :"),
    ("Les autres cours de la brochure sont listés en cartes grises « non couverts ».",
     "Les autres cours de la brochure (management, langues, sport, stages) sont listés sans lien."),
    ("Les <strong>encadrés en pointillés</strong> matérialisent les <strong>moments de choix</strong> : il faut y sélectionner le nombre indiqué de cours. Les cartes blanches cliquables mènent au support rédigé ; les cartes grises ne le sont pas.",
     "Les groupes « <em>Choisir n cours parmi</em> » matérialisent les <strong>moments de choix</strong> : il faut y sélectionner le nombre indiqué de cours. Les liens mènent aux supports rédigés."),
    ("Cartes blanches : supports rédigés ; cartes grises : cours listés non rédigés.",
     "Avec lien : support rédigé ; sans lien : cours listé non rédigé."),
    ("signalé par les pastilles oranges", "signalé dans les intitulés de groupes"),
    ("Les cartes blanches sont les choix du track recommandé",
     "Les liens sont les choix du track recommandé"),
]
REPLS_EN = [
    ("are written up in depth (clickable white cards):",
     "are written up in depth (links):"),
    ("The other courses of the brochure are listed as gray \"not covered\" cards.",
     "The other courses of the brochure (management, languages, sports, internships) are listed without links."),
    ("The <strong>dashed boxes</strong> mark the <strong>choice points</strong>: you must select the indicated number of courses there. Clickable white cards lead to the written material; gray cards do not.",
     "The \"<em>Choose n courses from</em>\" groups mark the <strong>choice points</strong>: you must select the indicated number of courses there. Links lead to the written materials."),
    ("White cards: written materials; gray cards: listed courses not written up.",
     "With a link: written material; without: listed course not written up."),
    ("flagged by the orange chips", "flagged in the group headings"),
    ("The white cards are the recommended track's choices",
     "The links are the recommended track's choices"),
]

if __name__ == '__main__':
    n = build('index.html', 'fr', 'assets/paper.css', 'en/index.html', 'English',
              'MSc&amp;T LLGA · Supports de cours', REPLS_FR)
    print('index.html :', n, 'cartes')
    n = build('en/index.html', 'en', 'assets/paper.css', '../index.html', 'Français',
              'MSc&amp;T LLGA · Course notes', REPLS_EN)
    print('en/index.html :', n, 'cartes')
