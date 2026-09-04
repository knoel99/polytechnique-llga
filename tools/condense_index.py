#!/usr/bin/env python3
"""Condense les pages d'index : lead/track/pied raccourcis, descriptifs
retires, listes de cours converties en tableaux compacts (.tbl)."""
import re

TRACK_FR = '''<p>Quatre tracks sont possibles ; le cœur du master est le croisement <strong>LLM&nbsp;+&nbsp;graphes</strong>. Sélection rédigée ici&nbsp;:</p>
<ul>
<li><strong>P1</strong>&nbsp;: Machine Learning (tronc commun)&nbsp;; au choix&nbsp;: Deep Learning, Signal Processing, EA Collaborative Learning.</li>
<li><strong>P2</strong>&nbsp;: RL &amp; Autonomous Agents, Graph ML &amp; DL for Generative AI (cours central), Text Mining &amp; NLP&nbsp;; au choix&nbsp;: Computational Optimal Transport, Multimodal Generative AI.</li>
<li><strong>Année 2</strong>&nbsp;: Large Language Models, Advanced Graph Neural Networks, Analysis &amp; Deep Learning on Geometric Data.</li>
</ul>'''

TRACK_EN = '''<p>Four tracks are possible; the heart of the program is the <strong>LLM&nbsp;+&nbsp;graphs</strong> intersection. Selection written up here:</p>
<ul>
<li><strong>P1</strong>: Machine Learning (core); electives: Deep Learning, Signal Processing, EA Collaborative Learning.</li>
<li><strong>P2</strong>: RL &amp; Autonomous Agents, Graph ML &amp; DL for Generative AI (central course), Text Mining &amp; NLP; electives: Computational Optimal Transport, Multimodal Generative AI.</li>
<li><strong>Year 2</strong>: Large Language Models, Advanced Graph Neural Networks, Analysis &amp; Deep Learning on Geometric Data.</li>
</ul>'''

LEAD_FR = ('Supports de cours du master MSc&amp;T «&nbsp;Large Language Models, Graphs and Applications&nbsp;», '
           'rédigés module par module pour le track recommandé «&nbsp;profil équilibré&nbsp;» (cœur Graph&nbsp;+&nbsp;LLM). '
           'La page suit la brochure&nbsp;: tronc commun et moments de choix&nbsp;; les cours avec lien mènent au support '
           'rédigé, les autres (management, langues, sport, stages) sont listés sans lien.')

LEAD_EN = ('Course notes for the MSc&amp;T master "Large Language Models, Graphs and Applications", written module by '
           'module for the recommended "balanced profile" track (Graph&nbsp;+&nbsp;LLM core). The page follows the '
           'brochure: core curriculum and choice points; courses with a link lead to the written material, the others '
           '(management, languages, sports, internships) are listed without links.')

WIKI = 'https://msct.dix.polytechnique.fr/llga/wiki/doku.php?id=curriculum'
FOOT_FR = (f'Structure reproduite de la brochure MSc&amp;T&nbsp;; effectifs de choix actualisés par le '
           f'<a href="{WIKI}">curriculum détaillé officiel LLGA</a>. Ces supports ne remplacent pas les cours '
           f'officiels de l\'École Polytechnique.')
FOOT_EN = (f'Structure reproduced from the MSc&amp;T brochure; required numbers of choices updated by the '
           f'<a href="{WIKI}">official detailed LLGA curriculum</a>. These materials do not replace the official '
           f'courses of École Polytechnique.')

HEADS = ['Code', 'Cours', 'Équipe', 'Statut']

def li_to_row(body, nc, heads):
    body = body.split('<span class="d">')[0]  # descriptif ignoré (peut contenir des liens)
    link = re.search(r'<a href="([^"]+)">([^<]*)</a>', body)
    mini = re.search(r'<span class="code-mini">(.*?)</span>', body, re.S)
    em = re.search(r'<em>(.*?)</em>', body, re.S)
    if link:
        href, title = link.group(1), link.group(2)
        code, team = (mini.group(1).split(' · ', 1) + [''])[:2] if mini else ('', '')
    else:
        t = re.sub(r'<span[^>]*>.*?</span>', '', body, flags=re.S)
        title = re.sub(r'<em>.*?</em>', '', t, flags=re.S)
        title = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', title)).strip(' —\t')
        href, code = None, ''
        team = mini.group(1) if mini else ''
    marks = re.sub(r'\s+', ' ', em.group(1)).strip() if em else ''
    tcell = f'<a href="{href}">{title}</a>' if href else title
    cls = ' class="nc"' if nc else ''
    cells = [code.strip(), tcell, re.sub(r'\s+', ' ', team).strip(), marks]
    return '<tr%s><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (cls, *cells)

def ul_to_table(m):
    inner = m.group(1)
    rows = []
    for nc, body in re.findall(r'<li( class="nc")?>(.*?)</li>', inner, re.S):
        rows.append(li_to_row(body, bool(nc), HEADS))
    head = '<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>' % tuple(HEADS)
    return '<table class="tbl">\n' + head + '\n' + '\n'.join(rows) + '\n</table>'

def condense(path, lead, track, foot, heads):
    global HEADS
    HEADS = heads
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'<p class="lead">.*?</p>', lambda m: '<p class="lead">' + lead + '</p>', t, count=1, flags=re.S)
    # bloc track : paragraphe + liste qui suivent le h2#track
    t = re.sub(r'(<h2 id="track">.*?</h2>)\s*<p>.*?</p>\s*<ul>.*?</ul>', r'\1\n' + track, t, count=1, flags=re.S)
    n = 0
    def repl(m):
        nonlocal n; n += 1
        return ul_to_table(m)
    t = re.sub(r'<ul class="courses">(.*?)</ul>', lambda m: repl(m), t, flags=re.S)
    t = re.sub(r'<footer class="foot">\s*<p>.*?</p>\s*</footer>',
               '<footer class="foot">\n<p>' + foot + '</p>\n</footer>', t, count=1, flags=re.S)
    open(path, 'w', encoding='utf-8').write(t)
    return n

if __name__ == '__main__':
    print('index.html :', condense('index.html', LEAD_FR, TRACK_FR, FOOT_FR, ['Code', 'Cours', 'Équipe', 'Statut']), 'tableaux')
    print('en/index.html :', condense('en/index.html', LEAD_EN, TRACK_EN, FOOT_EN, ['Code', 'Course', 'Team', 'Status']), 'tableaux')
