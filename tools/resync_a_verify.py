#!/usr/bin/env python3
"""Verification + commit resync EN batch A."""
import re, html.parser, os, subprocess

mods = ['m1p1-refresher-statistics', 'm1p1-refresher-cs', 'm1p1-machine-learning',
        'm1p1-deep-learning', 'm1p1-signal-processing', 'm1p1-emerging-ml',
        'm1p1-probability-monte-carlo', 'm1p1-statistical-learning-theory',
        'm1p1-dbms', 'm1p1-computer-vision']

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
extra = ['en/courses/m1p1-signal-processing/ch7.html', 'en/courses/m1p1-signal-processing/ch8.html',
         'en/courses/m1p1-emerging-ml/ch8.html', 'en/courses/m1p1-statistical-learning-theory/ch5.html',
         'en/courses/m1p1-statistical-learning-theory/ch6.html']
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
    msg = 'EN resync: batch A (10 modules P1 - Official objectives and syllabus, fiches SynapseS a jour, corrections equipes)'
    subprocess.run(['git', 'commit', '-q', '-m', msg], check=True)
    subprocess.run(['git', 'push', '-q', 'origin', 'main'], check=True)
    print('PUSHED')
