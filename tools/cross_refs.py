#!/usr/bin/env python3
"""List mentions of *other* modules' chapters, with the chapter they now hit.

Usage (repository root):
    python3 tools/cross_refs.py                 # every module
    python3 tools/cross_refs.py m1p1-tda        # mentions inside one module

For each mention such as "Machine Learning module, ch. 6", "chapter 2 of the
Machine Learning module" or "[Deep Learning](../m1p1-deep-learning/index.html)
(ch. 9)", prints the target module, the number, the current title of that
chapter in the target page, and the surrounding text, so that a reader can
see at once whether the number still points at the topic the sentence names.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ALIASES = {
    "m1p1-machine-learning": ["Machine Learning"],
    "m1p1-deep-learning": ["Deep Learning", "DL"],
    "m1p1-refresher-statistics": ["Refresher in Statistics", "Refresher Statistics", "Statistics refresher"],
    "m1p1-refresher-cs": ["Refresher in Computer Science", "Refresher CS", "CS refresher", "Refresher in CS"],
    "m1p1-refresher-neural-nets": ["Refresher Neural Nets"],
    "m1p1-signal-processing": ["Signal Processing"],
    "m1p1-emerging-ml": ["Emerging Subjects", "Emerging ML", "Collaborative Learning"],
    "m1p1-statistical-learning-theory": ["Statistical Learning Theory", "SLT"],
    "m1p1-probability-monte-carlo": ["Probability", "Monte Carlo"],
    "m1p1-computer-vision": ["Computer Vision", "Image Analysis"],
    "m1p1-computer-animation": ["Computer Animation"],
    "m1p1-shapes": ["Shapes"],
    "m1p1-tda": ["TDA", "Topological Data Analysis"],
    "m1p1-dbms": ["DBMS", "Database"],
    "m1p2-graph-ml": ["Graph ML", "Graph Machine"],
    "m1p2-nlp-text-mining": ["NLP", "Text Mining"],
    "m1p2-reinforcement-learning": ["Reinforcement Learning", "RL"],
    "m1p2-multimodal-genai": ["Multimodal"],
    "m1p2-optimal-transport": ["Optimal Transport", "OT"],
    "m1p2-optimization-ai": ["Optimization for AI"],
    "m1p2-deep-learning-p2": ["Deep Learning (P2", "DL P2"],
    "m1p2-advanced-deep-learning": ["Advanced Deep Learning"],
    "m1p2-image-synthesis": ["Image Synthesis"],
    "m1p2-responsible-ai-sustainability": ["Responsible AI"],
    "m1p2-statistics-in-action": ["Statistics in Action"],
    "m1p2-social-media-probabilistic": ["Social Media"],
    "m1p2-computer-vision-applications": ["Computer Vision (P2", "Computer Vision: From", "CV applications"],
    "m1p2-realtime-ai-videogames": ["Video Games"],
    "m2-large-language-models": ["Large Language Models", "LLMs module", "LLM module"],
    "m2-geometric-deep-learning": ["Geometric Data", "Geometric DL", "Geometric Deep Learning"],
    "m2-advanced-gnn": ["Advanced GNN"],
    "m2-graph-generative-models": ["Graph Generative"],
    "m2-advanced-topics-llms": ["Advanced Topics"],
    "m2-control-generative-ai": ["Control in Generative"],
    "m2-privacy-uncertainty": ["Privacy and Uncertainty"],
    "m2-explainability-security-privacy-llms": ["Explainability"],
    "m2-security-robustness": ["Security and Robustness", "Security & Robustness"],
    "m2-mlops-llm-engineering": ["ML Ops", "MLOps"],
    "m2-speech-technology": ["Speech"],
    "m2-boosting-foundation-tabular": ["Boosting"],
}
CH = r"(?:ch\.|chapters?|§)\s*(\d+)"


def titles(slug: str) -> dict[int, str]:
    src = (ROOT / "courses" / slug / "index.qmd").read_text(encoding="utf-8")
    return {int(n): t.strip() for n, t in re.findall(r"^## (\d+)\. (.*?)\{#ch", src, re.M)}


def main(only: list[str]) -> None:
    table = {s: titles(s) for s in ALIASES}
    alias_re = "|".join(sorted((re.escape(a) for v in ALIASES.values() for a in v), key=len, reverse=True))
    link_re = r"\]\(\.\./([a-z0-9-]+)/index\.html[^)]*\)"
    patterns = [
        re.compile(rf"(?P<alias>{alias_re})(?:\s*\([^)]*\))?[^.;\n]{{0,25}}?\b{CH}"),
        re.compile(rf"\b{CH}(?:\s*\d*)?\s+of\s+the\s+(?:\[)?(?P<alias>{alias_re})"),
        re.compile(rf"{link_re}[^.;\n]{{0,25}}?\b{CH}"),
    ]
    lookup = {a: s for s, v in ALIASES.items() for a in v}
    for page in sorted((ROOT / "courses").glob("*/index.qmd")):
        own = page.parent.name
        if only and own not in only:
            continue
        text = page.read_text(encoding="utf-8")
        body = text.split("\n## References", 1)[0]
        seen = set()
        for pat in patterns:
            for m in pat.finditer(body):
                target = m.groupdict().get("alias")
                slug = lookup.get(target) if target else m.group(1)
                if not slug or slug == own or slug not in table:
                    continue
                num = int([g for g in m.groups() if g and g.isdigit()][-1])
                if (m.start(), num) in seen:
                    continue
                seen.add((m.start(), num))
                line = body.count("\n", 0, m.start()) + 1
                ctx = body[max(0, m.start() - 70): m.end() + 50].replace("\n", " ")
                hit = table[slug].get(num, "?? no such chapter")
                print(f"{own}:{line}\t→ {slug} ch.{num} = «{hit[:55]}»\n\t…{ctx}…")


if __name__ == "__main__":
    main(sys.argv[1:])
