#!/usr/bin/env python3
"""Supprime les pages intermediaires courses/<slug>/index.html : le hero du module
passe sur la premiere page de section, tous les liens sont reecrits en consequence."""
import re, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ARROW = "\u2190"  # fleche gauche


def balanced_div(t, start):
    depth = 0
    for m in re.finditer(r"<div\b|</div>", t[start:]):
        depth += 1 if m.group(0).startswith("<div") else -1
        if depth == 0:
            return t[start:start + m.end()]
    raise ValueError("div non ferme")


def first_section(dd):
    sids = [f for f in os.listdir(dd) if f.endswith(".html") and f != "index.html"]
    chs = sorted((s for s in sids if s.startswith("ch") and s[2:-5].isdigit()),
                 key=lambda x: int(x[2:-5]))
    return chs[0] if chs else sorted(sids)[0]


changed = 0
for d in sorted(glob.glob("courses/*/")):
    idx = os.path.join(d, "index.html")
    if not os.path.exists(idx):
        continue
    t = open(idx, encoding="utf-8").read()
    m = re.search(r'<div class="course-hero">', t)
    hero = balanced_div(t, m.start())
    m2 = re.search(r'<nav class="toc">.*?<a href="([^"]+)"', t, re.S)
    first_sid = m2.group(1)  # ex: ch1.html
    # toutes les pages du module : home/strip pointent vers la premiere section
    for f in glob.glob(d + "*.html"):
        if f.endswith("index.html"):
            continue
        p = open(f, encoding="utf-8").read()
        p = p.replace('<a class="sidebar-home" href="index.html">',
                      '<a class="sidebar-home" href="%s">' % first_sid)
        p = p.replace('<a href="index.html">', '<a href="%s">' % first_sid)
        open(f, "w", encoding="utf-8").write(p)
    # premiere page : strip remplace par le hero du module, pager prev corrige
    fp = d + first_sid
    p = open(fp, encoding="utf-8").read()
    strip = re.search(r'<div class="section-strip">.*?</div>\n', p, re.S)
    if strip:
        p = p[:strip.start()] + hero + "\n\n" + p[strip.end():]
    p = p.replace('<a href="../../index.html"><span class="dir">' + ARROW + ' Module</span> Accueil du module</a>',
                  '<a href="../../index.html"><span class="dir">' + ARROW + ' Programme</span> Accueil</a>')
    open(fp, "w", encoding="utf-8").write(p)
    os.remove(idx)
    changed += 1
print("modules transformes:", changed)

# index racine : courses/<slug>/ -> courses/<slug>/<first>.html
t = open("index.html", encoding="utf-8").read()


def fix(m):
    slug = m.group(1)
    dd = "courses/" + slug
    if not os.path.isdir(dd):
        return m.group(0)
    return "courses/%s/%s" % (slug, first_section(dd))


t = re.sub(r"courses/([a-z0-9-]+)/", fix, t)
open("index.html", "w", encoding="utf-8").write(t)

# liens croises ../<slug>/ -> ../<slug>/<first>.html dans toutes les pages
n = 0
for f in glob.glob("courses/*/*.html"):
    p = open(f, encoding="utf-8").read()

    def fix2(m):
        global n
        slug = m.group(1)
        dd = "courses/" + slug
        if not os.path.isdir(dd):
            return m.group(0)
        n += 1
        return "../%s/%s" % (slug, first_section(dd))

    p2 = re.sub(r"(?<![/\w])\.\./([a-z0-9-]+)/", fix2, p)
    if p2 != p:
        open(f, "w", encoding="utf-8").write(p2)
print("liens croises reecrits:", n)

# verification finale des liens relatifs
bad = []
for f in ["index.html"] + glob.glob("courses/*/*.html") + glob.glob("courses/*.html"):
    t = open(f, encoding="utf-8").read()
    for h in re.findall(r'href="([^"#][^"]*)"', t):
        if h.startswith(("http", "mailto")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), h))):
            bad.append((f, h))
print("liens casses:", len(bad))
for b in bad[:8]:
    print("  ", b)
