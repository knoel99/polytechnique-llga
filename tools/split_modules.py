#!/usr/bin/env python3
"""Decoupe chaque module (fichier plat courses/<slug>.html) en dossier
courses/<slug>/ avec une page par section (tutoriel classique, sommaire lateral).

Usage : python3 tools/split_modules.py [slug ...]   (sans argument : tous les modules valides)
"""
import os, re, sys, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES = os.path.join(ROOT, "courses")

HEAD_TMPL = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — LLGA</title>
<link rel="stylesheet" href="{css}style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}]}});"></script>
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <div class="brand">
      <div class="rx">X</div>
      <div>
        <div class="t1">MSc&amp;T LLGA · Supports de cours</div>
        <div class="t2">{t2}</div>
      </div>
    </div>
    <nav><a href="../../index.html">Accueil</a></nav>
  </div>
</header>
"""

SECTION_NUM = {"ex": "Exercices", "refs": "Références"}


def balanced_block(t, start_idx):
    """Renvoie (html, end_idx) du bloc <section ...> ... </section> equilibre."""
    depth = 0
    i = start_idx
    token = re.compile(r"<section\b|</section>")
    for m in token.finditer(t, start_idx):
        depth += 1 if m.group(0).startswith("<section") else -1
        if depth == 0:
            end = m.end()
            return t[start_idx:end], end
    raise ValueError("section non fermee a l'index %d" % start_idx)


def extract(pattern, t, flags=0):
    m = re.search(pattern, t, flags)
    return m.group(1).strip() if m else None


def parse_module(path):
    t = open(path, encoding="utf-8").read()
    if re.search(r"<!--\s*(A_COMPLETER|SUITE)\s*-->", t):
        raise ValueError("marqueur d'inacheve present")
    slug = os.path.basename(path)[:-5]
    title = extract(r"<h1>(.*?)</h1>", t) or slug
    code = extract(r'<div class="code-line">(.*?)</div>', t)
    facts = extract(r'<div class="facts">(.*?)</div>', t, re.S)
    tags = extract(r'<div class="tags">(.*?)</div>', t, re.S)
    t2 = extract(r'<div class="t2">(.*?)</div>', t) or ""
    # entrees de la TOC
    toc_m = re.search(r'<nav class="toc">.*?<ol>(.*?)</ol>', t, re.S)
    toc = re.findall(r'<a href="#([^"]+)">([^<]+)</a>', toc_m.group(1)) if toc_m else []
    # sections (ch*, ex, refs, ou tout autre id present dans la TOC)
    sections = {}
    order = []
    for m in re.finditer(r'<section class="[^"]*" id="([^"]+)"[^>]*>', t):
        sid = m.group(1)
        if sid in sections:
            continue
        html_block, _ = balanced_block(t, m.start())
        sections[sid] = html_block
        order.append(sid)
    missing = [sid for sid, _ in toc if sid not in sections]
    if missing:
        raise ValueError("sections manquantes vs TOC : %s" % missing)
    if "ex" not in sections or "refs" not in sections:
        raise ValueError("exercices ou references absents")
    return dict(slug=slug, title=title, code=code, facts=facts, tags=tags,
                t2=t2, toc=toc, sections=sections)


def rewrite_anchors(html, sids):
    if not sids:
        return html
    pat = re.compile(r'href="#(%s)"' % "|".join(re.escape(s) for s in sids))
    return pat.sub(r'href="\1.html"', html)


def sidebar(mod, active, first_sid=None):
    links = []
    for sid, stitle in mod["toc"]:
        cls = ' class="active"' if sid == active else ""
        links.append(f'<a href="{sid}.html"{cls}>{stitle}</a>')
    code = (mod["code"] or "")[:26]
    home = f"{first_sid}.html" if first_sid else "../../index.html"
    return ('<aside class="sidebar">\n'
            f'<a class="sidebar-home" href="{home}"><span class="code-mini">{code}</span>{mod["title"]}</a>\n'
            '<nav class="sidebar-toc">\n' + "\n".join(links) + '\n</nav>\n'
            '<a class="sidebar-program" href="../../index.html">← Programme du master</a>\n'
            '</aside>')


def pager(mod, sid):
    ids = [s for s, _ in mod["toc"]]
    i = ids.index(sid)
    prev_lnk = next_lnk = ""
    if i > 0:
        pid, ptitle = mod["toc"][i - 1]
        prev_lnk = (f'<a href="{pid}.html"><span class="dir">← Précédent</span> {ptitle}</a>')
    else:
        prev_lnk = '<a href="index.html"><span class="dir">← Module</span> Accueil du module</a>'
    if i < len(ids) - 1:
        nid, ntitle = mod["toc"][i + 1]
        next_lnk = (f'<a class="next" href="{nid}.html"><span class="dir">Suivant</span> {ntitle}</a>')
    else:
        next_lnk = '<a class="next" href="../../index.html"><span class="dir">Fin du module</span> Programme</a>'
    return f'<nav class="pager">{prev_lnk}{next_lnk}</nav>'


def section_label(sid, toc_titles=None):
    if sid.startswith("ch") and sid[2:].isdigit():
        return "Chapitre " + sid[2:]
    if sid == "ex":
        return "Exercices"
    if sid == "refs":
        return "Références"
    if toc_titles and sid in toc_titles:
        return toc_titles[sid]
    return sid


def build(mod):
    d = os.path.join(COURSES, mod["slug"])
    os.makedirs(d, exist_ok=True)
    first_sid = mod["toc"][0][0] if mod["toc"] else None
    hero = f"""<div class="course-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../../index.html">Programme</a> › {mod["title"]}</div>
    <div class="code-line">{mod["code"] or mod["slug"]}</div>
    <h1>{mod["title"]}</h1>
    <div class="tags">{mod["tags"] or ""}</div>
    <div class="facts">{mod["facts"] or ""}</div>
  </div>
</div>"""
    # ---- une page par section : la premiere porte le hero, pas de page intermediaire ----
    for sid, stitle in mod["toc"]:
        content = rewrite_anchors(mod["sections"][sid], list(mod["sections"].keys()))
        page = HEAD_TMPL.format(title=f'{mod["title"]} — {stitle}', css="../../assets/", t2=mod["t2"])
        if sid == first_sid:
            top = hero
        else:
            top = (f'<div class="section-strip"><a href="../../index.html">Programme</a> › '
                   f'<a href="{first_sid}.html">{mod["title"]}</a> › {stitle}</div>')
        # pager : la premiere section ramene au programme du master
        ids = [s for s, _ in mod["toc"]]
        i = ids.index(sid)
        if i > 0:
            pid, ptitle = mod["toc"][i - 1]
            prev_lnk = f'<a href="{pid}.html"><span class="dir">← Précédent</span> {ptitle}</a>'
        else:
            prev_lnk = '<a href="../../index.html"><span class="dir">← Programme</span> Accueil</a>'
        if i < len(ids) - 1:
            nid, ntitle = mod["toc"][i + 1]
            next_lnk = f'<a class="next" href="{nid}.html"><span class="dir">Suivant</span> {ntitle}</a>'
        else:
            next_lnk = '<a class="next" href="../../index.html"><span class="dir">Fin du module</span> Programme</a>'
        page += top + f"""
<div class="tutorial-layout">
{sidebar(mod, sid, first_sid)}
<main class="content">
{content}
<nav class="pager">{prev_lnk}{next_lnk}</nav>
</main>
</div>

</body>
</html>
"""
        open(os.path.join(d, sid + ".html"), "w", encoding="utf-8").write(page)


def main():
    args = sys.argv[1:]
    done, skipped = [], []
    for f in sorted(os.listdir(COURSES)):
        if not f.endswith(".html"):
            continue
        slug = f[:-5]
        if args and slug not in args:
            continue
        try:
            mod = parse_module(os.path.join(COURSES, f))
            build(mod)
            os.remove(os.path.join(COURSES, f))
            done.append(slug)
        except ValueError as e:
            skipped.append((slug, str(e)))
    print("migrés :", len(done))
    for s in done:
        print("  ok", s)
    if skipped:
        print("ignorés :")
        for s, r in skipped:
            print("  --", s, ":", r)


if __name__ == "__main__":
    main()
