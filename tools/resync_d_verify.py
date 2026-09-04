#!/usr/bin/env python3
"""Verification + commit resync EN batch D (9 intros M2)."""
import re, html.parser, os, subprocess

mods = ['m2-privacy-uncertainty', 'm2-boosting-foundation-tabular', 'm2-control-generative-ai',
        'm2-mlops-llm-engineering', 'm2-security-robustness', 'm2-graph-generative-models',
        'm2-explainability-security-privacy-llms', 'm2-speech-technology', 'm2-advanced-topics-llms']

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
    f = 'en/courses/%s/intro.html' % m
    t = open(f, encoding='utf-8').read()
    p = P(); p.feed(t)
    if p.errs or [x for x in p.stack if x not in ('html', 'body')]:
        issues.append((m, 'TAGS'))
    if cjk.findall(t) or 'lang="fr"' in t:
        issues.append((m, 'CJK/LANG'))
    if 'Official objectives and syllabus' not in t:
        issues.append((m, 'NO_OFFICIAL_SECTION'))
print('ISSUES: ' + str(issues[:5]) if issues else 'TOUT OK (9 intros EN)')

if not issues:
    paths = ['en/courses/%s/intro.html' % m for m in mods]
    subprocess.run(['git', 'add'] + paths, check=True)
    msg = 'EN resync: 9 intros M2 (Official objectives and syllabus, fiches a jour)'
    subprocess.run(['git', 'commit', '-q', '-m', msg], check=True)
    subprocess.run(['git', 'push', '-q', 'origin', 'main'], check=True)
    print('PUSHED')
