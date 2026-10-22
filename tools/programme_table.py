#!/usr/bin/env python3
"""Regenerate the home-page programme table (index.html, #programme).

Usage (repository root):  python3 tools/programme_table.py

Per module it reads, from courses/<slug>/index.qmd: title, code and period
(subtitle), and the session plan (total hours, number of sessions, self-study
hours) written under specs/hours-and-progression.md. The 2026–2027 catalogue
status of each course unit is kept by hand in LISTING below: SynapseS could
only be read through its public listing excerpts (October 2026), so every
"not seen" entry says so instead of claiming the unit is gone.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- programme:start -->", "<!-- programme:end -->"

# (group heading, [slugs or ("uncovered", code, title, hours, status)])
GROUPS = [
    ("Year 1 · Period 1 — refreshers", [
        "m1p1-refresher-statistics", "m1p1-refresher-cs",
        ("uncovered", "CSC_51438_EP", "Refresher in Computer Graphics", "—",
         "new in the 2026–27 track listing (M.-P. Cani, P. Guehl); not covered by these notes"),
        "m1p1-refresher-neural-nets",
    ]),
    ("Year 1 · Period 1 — courses", [
        "m1p1-machine-learning", "m1p1-deep-learning", "m1p1-signal-processing",
        "m1p1-emerging-ml", "m1p1-computer-animation", "m1p1-computer-vision",
        "m1p1-tda", "m1p1-shapes", "m1p1-probability-monte-carlo", "m1p1-dbms",
        "m1p1-statistical-learning-theory", "m1p2-responsible-ai-sustainability",
    ]),
    ("Year 1 · Period 2 — courses", [
        "m1p2-reinforcement-learning", "m1p2-graph-ml", "m1p2-nlp-text-mining",
        "m1p2-multimodal-genai", "m1p2-deep-learning-p2", "m1p2-optimal-transport",
        "m1p2-optimization-ai", "m1p2-advanced-deep-learning", "m1p2-image-synthesis",
        "m1p2-statistics-in-action",
        "m1p2-social-media-probabilistic", "m1p2-computer-vision-applications",
        "m1p2-realtime-ai-videogames",
    ]),
    ("Year 1 — management and culture course units of the 2026–27 listing", [
        ("covered", "IME_51456_EP", "Introduction au marketing et à la stratégie", "—",
         "listed (S1) — framed by our page <a href=\"courses/m1p1-strategy-marketing/index.html\">Strategy / Marketing</a>"),
        ("uncovered", "HSS_51G16_EP", "Sociology of AI", "—",
         "listed (N. Wanlin, A. Wirth); humanities option — not covered"),
        ("uncovered", "LEN_51G07_EP · LEN_52G18_EP · HSS_52G27_EP",
         "Culture options (Supermodels…; Music, Literature and Femmes Fatales 2; Dark sides of the City of Lights)", "—",
         "listed; language/humanities options — see <a href=\"courses/m1-langues/index.html\">Languages</a>, <a href=\"courses/m1-humanites/index.html\">Humanities</a>"),
    ]),
    ("Year 2 — Periods 1 and 2", [
        "m2-large-language-models", "m2-geometric-deep-learning", "m2-advanced-gnn",
        "m2-privacy-uncertainty", "m2-boosting-foundation-tabular", "m2-control-generative-ai",
        "m2-mlops-llm-engineering", "m2-security-robustness", "m2-graph-generative-models",
        "m2-explainability-security-privacy-llms", "m2-speech-technology",
        "m2-advanced-topics-llms",
    ]),
]

S1 = "listed in LLGA 1 – S1"
S2 = "listed in LLGA 1 – S2"
NOT_SEEN = "in the 2026–27 catalogue (other tracks); not seen in the LLGA listing excerpts — to verify"
M2 = "LLGA 2 – S3/S4 contents not published yet"
LISTING = {
    "m1p1-refresher-statistics": S1, "m1p1-refresher-cs": S1,
    "m1p1-refresher-neural-nets": "off-curriculum support (no course unit)",
    "m1p1-machine-learning": S1 + " (mandatory)", "m1p1-signal-processing": S1,
    "m1p1-emerging-ml": S1, "m1p1-computer-animation": S1, "m1p1-computer-vision": S1,
    "m1p1-tda": S1, "m1p1-shapes": S1,
    "m1p1-deep-learning": "wiki: Deep Learning once, P1 or P2; not seen in the LLGA S1 listing excerpts — to verify",
    "m1p1-probability-monte-carlo": NOT_SEEN, "m1p1-dbms": NOT_SEEN,
    "m1p1-statistical-learning-theory": NOT_SEEN,
    "m1p2-reinforcement-learning": S2 + " (mandatory)", "m1p2-graph-ml": S2 + " (mandatory)",
    "m1p2-nlp-text-mining": S2 + " (mandatory)", "m1p2-multimodal-genai": S2,
    "m1p2-deep-learning-p2": S2, "m1p2-optimal-transport": S2, "m1p2-optimization-ai": S2,
    "m1p2-advanced-deep-learning": S2, "m1p2-image-synthesis": S2,
    "m1p2-statistics-in-action": "36 h unit of the 2026–27 catalogue, not in the LLGA 1 – S2 list",
    "m1p2-responsible-ai-sustainability": "changed: now CSC_51076_EP in Period 1 (was CSC_52073_EP, P2); not seen in the LLGA S1 listing excerpts — to verify",
    "m1p2-social-media-probabilistic": "absent from the 2026–27 catalogue (last sheet 2025–26)",
    "m1p2-computer-vision-applications": "announced slot, no SynapseS code",
    "m1p2-realtime-ai-videogames": "announced slot, no SynapseS code",
    "m2-large-language-models": "mandatory (wiki); " + M2,
    "m2-geometric-deep-learning": "mandatory (wiki); " + M2,
}

CODE_RE = re.compile(r"^([A-Z]{2,4}_\d{5}_EP)")


def module_row(slug: str) -> str:
    src = (ROOT / "courses" / slug / "index.qmd").read_text(encoding="utf-8")
    title = re.search(r'^title: "(.*)"', src, re.M).group(1)
    subtitle = re.search(r'^subtitle: "(.*)"', src, re.M).group(1)
    code_m = CODE_RE.match(subtitle)
    code = code_m.group(1) if code_m else "—"
    period = re.search(r"Year (\d)\s*·\s*Period (\d)", subtitle)
    period = f"Y{period.group(1)} P{period.group(2)}" if period else "—"
    plan = src.split("### Session plan {#sessions}", 1)
    volume, ours, self_h = "—", "—", "—"
    if len(plan) == 2:
        p = plan[1].split("\n### ", 1)[0]
        tot = re.search(r"\*\*(\d+(?:\.\d+)?) h (in class|of guided self-study)(?: \((assumed|announced)\))?", p)
        rows = len(re.findall(r"^\|\s*\d+\s*\|", p, re.M))
        if tot:
            hours = tot.group(1)
            if tot.group(2) == "in class":
                volume = f"{hours} h" + (f" ({tot.group(3)})" if tot.group(3) else "")
                ours = f"{rows} sessions"
            else:
                volume = "— (self-study)"
                ours = f"{rows} steps · {hours} h"
        sm = re.search(r"\*\*Self-study, outside the [^*]*\*\* \(about (\d+(?:\.\d+)?) h", p)
        self_h = f"≈ {sm.group(1)} h" if sm else "none"
    status = LISTING.get(slug, M2 if slug.startswith("m2-") else "")
    return (f'<tr><td><a href="courses/{slug}/index.html">{title}</a></td>'
            f'<td><span class="code-mini">{code}</span></td><td>{period}</td>'
            f"<td>{volume}</td><td>{ours}</td><td>{self_h}</td><td>{status}</td></tr>")


def extra_row(kind: str, code: str, title: str, hours: str, status: str) -> str:
    cls = ' class="nc"' if kind == "uncovered" else ""
    return (f"<tr{cls}><td>{html.escape(title)}</td><td><span class=\"code-mini\">{code}</span></td>"
            f"<td>Y1</td><td>{hours}</td><td>—</td><td>—</td><td>{status}</td></tr>")


def build() -> str:
    out = [START, '<div class="tbl-wrap"><table class="tbl programme">',
           "<thead><tr><th>Course</th><th>Code</th><th>Period</th><th>Official volume</th>"
           "<th>These notes</th><th>Self-study</th><th>2026–27 SynapseS listing</th></tr></thead><tbody>"]
    for heading, items in GROUPS:
        out.append(f'<tr><th colspan="7">{heading}</th></tr>')
        for it in items:
            out.append(module_row(it) if isinstance(it, str) else extra_row(*it))
    out += ["</tbody></table></div>", END]
    return "\n".join(out)


if __name__ == "__main__":
    path = ROOT / "index.html"
    page = path.read_text(encoding="utf-8")
    if START not in page:
        raise SystemExit("index.html has no programme markers")
    head, rest = page.split(START, 1)
    _, tail = rest.split(END, 1)
    path.write_text(head + build() + tail, encoding="utf-8")
    print("index.html: programme table regenerated")
