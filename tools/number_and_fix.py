#!/usr/bin/env python3
"""Numerote les sous-sections (h3 -> N.k., h4 -> N.k.j.) de chaque page de
section dont le h2 porte un numero ; corrige des fautes de francais connues.
Exclut par defaut les fichiers passes en argument --skip."""
import re, os, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKIP = set(sys.argv[1:])

FIXES = [
    # accents combinants (entities) -> precompose
    (re.compile(r"e&#769;"), "é"),
    (re.compile(r"E&#769;"), "É"),
    (re.compile(r"a&#768;"), "à"),
    (re.compile(r"&#769;"), ""),
    # fautes grammaticales systematiques
    (re.compile(r"\bla équipe\b"), "l'équipe"),
    (re.compile(r"\bde équipe\b"), "de l'équipe"),
    (re.compile(r"\bà le\b"), "au"),
    (re.compile(r"\bsous-sections\b"), "sous-sections"),
]

H3_RE = re.compile(r"<h3(\s[^>]*)?>(.*?)</h3>", re.S)
H4_RE = re.compile(r"<h4(\s[^>]*)?>(.*?)</h4>", re.S)
LEAD_NUM = re.compile(r"^\s*(\d+(?:\.\d+)*)\.?\s+")


def strip_num(s):
    return LEAD_NUM.sub("", s)


pages = badge = 0
counted = fixed = 0
for f in sorted(glob.glob("courses/*/*.html")):
    if f in SKIP:
        continue
    t = open(f, encoding="utf-8").read()
    t0 = t
    # corrections
    for pat, rep in FIXES:
        t = pat.sub(rep, t)
    # numerotation : uniquement si le premier h2 du contenu porte un numero
    m2 = re.search(r'<h2(\s[^>]*)?>(.*?)</h2>', t, re.S)
    if m2:
        num = re.match(r"\s*(\d+)\.", m2.group(2))
        if num:
            chap = num.group(1)
            k = 0

            def repl3(mm):
                global k
                k += 1
                inner = strip_num(mm.group(2))
                return "<h3%s>%s.%d. %s</h3>" % (mm.group(1) or "", chap, k, inner)

            t = H3_RE.sub(repl3, t)
            if k:
                counted += 1
            # h4 : renumerote apres h3 ; approx : numerotation continue par bloc
            # on gere le cas simple : h4 consecutifs sous le dernier h3
            j = 0
            out = []
            pos = 0
            for mm in H3_RE.finditer(t):
                out.append(t[pos:mm.start()])
                out.append(mm.group(0))
                pos = mm.end()
                j = 0
                # h4 suivants jusqu'au prochain h3
                rest = t[pos:]
                nxt = H3_RE.search(rest)
                seg_end = nxt.start() if nxt else len(rest)
                seg = rest[:seg_end]

                def repl4(m4, _j=[0]):
                    _j[0] += 1
                    inner = strip_num(m4.group(2))
                    return "<h4%s>%s.%d.%d. %s</h4>" % (m4.group(1) or "", chap, k, _j[0], inner)

                seg = H4_RE.sub(repl4, seg)
                out.append(seg)
                pos += seg_end
            out.append(t[pos:])
            t = "".join(out)
    if t != t0:
        open(f, "w", encoding="utf-8").write(t)
        badge += 1
    pages += 1
    if "e&#769;" in t0 or "la équipe" in t0:
        fixed += 1

print("pages:", pages, "| modifiees:", badge, "| pages avec numerotation:", counted,
      "| pages avec fautes corrigees:", fixed)
