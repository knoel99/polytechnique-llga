#!/usr/bin/env python3
"""Insere une section intro.html en tete de chaque module (fiche + contenu a
remplir), supprime les banniieres course-hero, met a jour sidebars/pagers/liens."""
import re, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def balanced_div(t, start):
    depth = 0
    for m in re.finditer(r"<div\b|</div>", t[start:]):
        depth += 1 if m.group(0).startswith("<div") else -1
        if depth == 0:
            return t[start:start + m.end()]
    raise ValueError("div non ferme")


def first_section(dd):
    sids = [f for f in os.listdir(dd) if f.endswith(".html") and f not in ("index.html", "intro.html")]
    chs = sorted((s for s in sids if s.startswith("ch") and s[2:-5].isdigit()),
                 key=lambda x: int(x[2:-5]))
    return chs[0] if chs else sorted(sids)[0]


HEAD = None  # remplit depuis une page existante du module

changed = 0
for d in sorted(glob.glob("courses/*/")):
    slug = d.rstrip("/").split("/")[-1]
    if os.path.exists(d + "intro.html"):
        continue
    fs = first_section(d)
    fp = d + fs
    t = open(fp, encoding="utf-8").read()
    # extraction hero + parties
    m = re.search(r'<div class="course-hero">', t)
    hero = balanced_div(t, m.start()) if m else ""
    title = re.search(r"<h1>(.*?)</h1>", hero).group(1) if hero else slug
    code = (re.search(r'<div class="code-line">(.*?)</div>', hero).group(1)
            if re.search(r'<div class="code-line">(.*?)</div>', hero) else slug)
    tags = (re.search(r'<div class="tags">(.*?)</div>', hero, re.S).group(1)
            if re.search(r'<div class="tags">(.*?)</div>', hero, re.S) else "")
    facts = (re.search(r'<div class="facts">(.*?)</div>', hero, re.S).group(1)
             if re.search(r'<div class="facts">(.*?)</div>', hero, re.S) else "")
    # squelette commun (header) de la premiere page
    head = t[:t.index("</header>") + len("</header>")]
    # sidebar de la premiere page (sans hero elle commence par tutorial-layout)
    side_m = re.search(r"<aside class=\"sidebar\">.*?</aside>", t, re.S)
    sidebar = side_m.group(0)
    toc_titles = re.findall(r'<a href="([a-z0-9_-]+\.html)"[^>]*>([^<]+)</a>', sidebar)
    # nouvelles entrees sidebar : Introduction en tete
    intro_link = '<a href="intro.html">Introduction et vue d\'ensemble</a>'
    new_sidebar = sidebar.replace('<nav class="sidebar-toc">\n',
                                  '<nav class="sidebar-toc">\n' + intro_link + "\n", 1)
    # page intro
    plan_items = "\n".join(
        '<li><a href="%s">%s</a></li>' % (sid, ttl) for sid, ttl in toc_titles)
    fiche = ('<table class="tbl">\n'
             '<tr><th style="width:160px">Module</th><td>%s</td></tr>\n'
             '<tr><th>Code</th><td>%s</td></tr>\n'
             '<tr><th>Equipe et volume</th><td>%s</td></tr>\n'
             '<tr><th>Statut dans la formation</th><td>%s</td></tr>\n'
             "</table>\n" % (title, code, facts, tags))
    intro_page = head + """
<div class="tutorial-layout">
""" + new_sidebar + """
<main class="content">
<section class="chapter" id="intro">
<h2>Introduction et vue d'ensemble</h2>
""" + fiche + """
<!-- CONTENU_INTRO -->
</section>
<nav class="pager"><a href="../../index.html"><span class="dir">&#8592; Programme</span> Accueil</a><a class="next" href="__FIRST__"><span class="dir">Suivant</span> Premie&#769;re section</a></nav>
</main>
</div>

</body>
</html>
"""
    intro_page = intro_page.replace("__FIRST__", fs)
    intro_page = intro_page.replace("<title>PLACEHOLDER", "<title>" + title)
    # corrige le <title> (head herite de la premiere page : garde le meme, acceptable)
    open(d + "intro.html", "w", encoding="utf-8").write(intro_page)

    # premiere page : retirer le hero, remplacer par un strip, pager prev -> intro
    t2 = t.replace(hero, "")
    strip = ('<div class="section-strip"><a href="../../index.html">Programme</a> &#8250; '
             '<a href="intro.html">%s</a></div>\n' % title)
    t2 = re.sub(r'</header>\s*\n', "</header>\n\n" + strip, t2, count=1)
    t2 = t2.replace('<a href="../../index.html"><span class="dir">&#8592; Programme</span> Accueil</a>',
                    '<a href="intro.html"><span class="dir">&#8592; Introduction</span> Vue d\'ensemble</a>')
    t2 = t2.replace('<aside class="sidebar">\n<nav class="sidebar-toc">' if False else
                    '<nav class="sidebar-toc">\n',
                    '<nav class="sidebar-toc">\n' + intro_link + "\n", 1)
    open(fp, "w", encoding="utf-8").write(t2)

    # autres pages : ajouter l'entree Introduction dans la sidebar
    for f in glob.glob(d + "*.html"):
        if f.endswith("intro.html") or f == fp:
            continue
        p = open(f, encoding="utf-8").read()
        if 'href="intro.html"' in p:
            continue
        p = p.replace('<nav class="sidebar-toc">\n',
                      '<nav class="sidebar-toc">\n' + intro_link + "\n", 1)
        open(f, "w", encoding="utf-8").write(p)
    changed += 1

print("modules avec intro:", changed)

# index racine + liens croises : cible premiere section -> intro.html
t = open("index.html", encoding="utf-8").read()
for d in sorted(glob.glob("courses/*/")):
    slug = d.rstrip("/").split("/")[-1]
    fs = first_section(d)
    t = t.replace("courses/%s/%s" % (slug, fs), "courses/%s/intro.html" % slug)
open("index.html", "w", encoding="utf-8").write(t)

n = 0
for f in glob.glob("courses/*/*.html"):
    if f.endswith("intro.html"):
        continue
    p = open(f, encoding="utf-8").read()
    p2 = p
    for d in sorted(glob.glob("courses/*/")):
        slug = d.rstrip("/").split("/")[-1]
        fs = first_section(d)
        p2 = p2.replace("../%s/%s" % (slug, fs), "../%s/intro.html" % slug)
    if p2 != p:
        open(f, "w", encoding="utf-8").write(p2)
        n += 1
print("pages avec liens croises reecrits:", n)

# verification rapide
bad = []
for f in ["index.html"] + glob.glob("courses/*/*.html"):
    t = open(f, encoding="utf-8").read()
    for h in re.findall(r'href="([^"#][^"]*)"', t):
        if h.startswith(("http", "mailto")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), h))):
            bad.append((f, h))
print("liens casses:", bad or "0")
