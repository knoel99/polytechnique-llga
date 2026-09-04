#!/usr/bin/env python3
"""Verification + commit resync EN batch B + controle global final FR+EN."""
import re, html.parser, os, glob, subprocess

mods = ['m1p1-computer-animation', 'm1p1-shapes', 'm1p1-tda', 'm1p2-reinforcement-learning',
        'm1p2-graph-ml', 'm1p2-nlp-text-mining', 'm1p2-optimal-transport', 'm1p2-multimodal-genai',
        'm1p2-computer-vision-applications', 'm1p2-statistics-in-action']

class P(html.parser.HTMLParser):
    VOID = {'br', 'img', 'meta', 'link', 'hr', 'input', 'col', 'area', 'base',
            'embed', 'source', 'track', 'wbr'}
    def __init__(s):
        super().__init__(); s.stack = []; s.errs = []
    def handle_starttag(s, tag, a):
        if tag not in s.VOID: s.stack.append(tag)
    def handle_endtag(s, tag):
        if tag in s.VOID: return
        if s.stack and s.stack[-1] == tag: s.stack.pop()
        else: s.errs.append((tag, s.getpos()[0]))

cjk = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff]')
issues = []
paths = []
for m in mods:
    f = 'en/courses/%s/intro.html' % m
    t = open(f, encoding='utf-8').read()
    p = P(); p.feed(t)
    if p.errs or [x for x in p.stack if x not in ('html', 'body')]:
        issues.append((m, 'TAGS'))
    if cjk.findall(t) or 'lang="fr"' in t:
        issues.append((m, 'CJK/LANG'))
    if 'Official objectives and syllabus' not in t:
        issues.append((m, 'NO_OFFICIAL_SECTION'))
    paths.append(f)
# chapitres touches (OT code/titre nouveaux partout dans le module)
for f in glob.glob('en/courses/m1p2-optimal-transport/*.html'):
    if f.endswith('intro.html'):
        continue
    paths.append(f)
for f in paths:
    t = open(f, encoding='utf-8').read()
    p = P(); p.feed(t)
    if p.errs or [x for x in p.stack if x not in ('html', 'body')]:
        issues.append((f, 'TAGS'))
print('ISSUES: ' + str(issues[:5]) if issues else 'TOUT OK (10 modules, %d fichiers)' % len(paths))

if not issues:
    subprocess.run(['git', 'add'] + ['en/courses/%s' % m for m in mods], check=True)
    msg = ('EN resync: batch B (10 modules - Official objectives and syllabus, '
           'OT -> APM_52188 partout, defs ajoutees Animation/Shapes/TDA)')
    subprocess.run(['git', 'commit', '-q', '-m', msg], check=True)
    subprocess.run(['git', 'push', '-q', 'origin', 'main'], check=True)
    print('PUSHED')

# ---------- controle global final FR + EN ----------
cjk2 = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff]')
grand = []
for f in ['index.html', 'en/index.html'] + sorted(glob.glob('courses/*/*.html')) + sorted(glob.glob('en/courses/*/*.html')):
    t = open(f, encoding='utf-8').read()
    p = P(); p.feed(t)
    if p.errs or [x for x in p.stack if x not in ('html', 'body')]:
        grand.append(('TAGS', f))
    if cjk2.findall(t):
        grand.append(('CJK', f))
    for h in re.findall(r'href="([^"#][^"]*)"', t):
        if h.startswith(('http', 'mailto')):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), h))):
            grand.append(('LINK', f, h))
nfr = len(glob.glob('courses/*/*.html'))
nen = len(glob.glob('en/courses/*/*.html'))
print('GLOBAL: pages FR=%d, EN=%d, total=%d' % (nfr, nen, nfr + nen))
print('problemes globaux:', len(grand))
for g in grand[:8]:
    print('  ', g)
