#!/usr/bin/env python3
"""Verification + commit resync EN batch C."""
import re, html.parser, os, subprocess

mods = ['m1p2-realtime-ai-videogames', 'm1p2-advanced-deep-learning', 'm1p2-optimization-ai',
        'm1p2-responsible-ai-sustainability', 'm1p2-deep-learning-p2',
        'm1p2-social-media-probabilistic', 'm1p2-image-synthesis',
        'm2-large-language-models', 'm2-advanced-gnn', 'm2-geometric-deep-learning']

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
# fichiers chapitres touches
extra = ['en/courses/m1p2-responsible-ai-sustainability/ch8.html',
         'en/courses/m1p2-deep-learning-p2/ch8.html',
         'en/courses/m1p2-image-synthesis/ch11.html']
for f in extra:
    if os.path.exists(f):
        t = open(f, encoding='utf-8').read()
        p = P(); p.feed(t)
        if p.errs or [x for x in p.stack if x not in ('html', 'body')]:
            issues.append((f, 'TAGS'))
        paths.append(f)
print('ISSUES: ' + str(issues[:5]) if issues else 'TOUT OK (10 modules, %d fichiers)' % len(paths))

if not issues:
    subprocess.run(['git', 'add'] + paths, check=True)
    msg = 'EN resync: batch C (10 modules - Official objectives and syllabus, fiches SynapseS a jour)'
    subprocess.run(['git', 'commit', '-q', '-m', msg], check=True)
    subprocess.run(['git', 'push', '-q', 'origin', 'main'], check=True)
    print('PUSHED')
