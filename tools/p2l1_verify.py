#!/usr/bin/env python3
"""Verification + commit des intros P2 lot 1."""
import re, html.parser, os, subprocess

mods = ['m1p2-reinforcement-learning', 'm1p2-graph-ml', 'm1p2-nlp-text-mining',
        'm1p2-optimal-transport', 'm1p2-multimodal-genai']

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
for m in mods:
    f = 'courses/%s/intro.html' % m
    t = open(f, encoding='utf-8').read()
    p = P(); p.feed(t)
    if p.errs or [x for x in p.stack if x not in ('html', 'body')]:
        issues.append((m, 'TAGS', p.errs[:2]))
    if cjk.findall(t) or 'CONTENU_INTRO' in t:
        issues.append((m, 'CJK/MARKER'))
    if 'programme officiel' not in t.lower():
        issues.append((m, 'NO_OFFICIAL_SECTION'))
    if m == 'm1p2-optimal-transport' and 'APM_52188_EP' not in t:
        issues.append((m, 'CODE NOT UPDATED'))
    for h in re.findall(r'href="(\.\./[^"]+)"', t):
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), h))):
            issues.append((m, 'LINK', h))
print('ISSUES: ' + str(issues[:5]) if issues else 'TOUT OK (5 intros)')

if not issues:
    paths = ['courses/%s/intro.html' % m for m in mods]
    subprocess.run(['git', 'add'] + paths, check=True)
    msg = ('Rework SynapseS P2 lot 1: RL/GraphML/NLP/OT/Multimodal '
           '(OT -> APM_52188 Flamary+Gaucher, programmes 9 semaines, evaluations detaillees)')
    subprocess.run(['git', 'commit', '-q', '-m', msg], check=True)
    subprocess.run(['git', 'push', '-q', 'origin', 'main'], check=True)
    print('PUSHED')
