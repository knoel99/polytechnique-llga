#!/usr/bin/env python3
"""Mechanical gates from AGENTS.md (Spec Kit-compatible / BMAD light).

Run from the repository root:  python3 tools/check_gates.py
Exit code 0 = all gates pass; 1 = at least one gate failed.

Checks (code-level proxies for the manual gates):
- Pages: courses/<id>/index.qmd + rendered index.html, lang="en", theme.js loaded.
- Index: every course linked from the root index.html curriculum tree.
- No FR switcher on any published page.
- Pedagogy: >= 6 exercises on science modules (specs/non-science-pages.md exempt);
  NumPy primary in the NN/ML refresher.
- Theme: paper.css defines .def/.thm/.note and a dark block; theme.js uses localStorage.
- Specs: every contract file has a row in specs/README.md (index stays honest).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pages outside the ">= 6 exercises" gate — specs/non-science-pages.md (lot A).
NON_SCIENCE = {
    "m1p1-strategy-marketing", "m1-sports", "m1-humanites", "m1-langues",
    "m1p2-startup-entrepreneurship", "m1p3-research-internship",
    "m2-ethical-issues-ai", "m2-projet-transverse", "m2-internship",
}

FR_SWITCHER = re.compile(r"français|lang-toggle|href=\"[^\"]*/fr/", re.IGNORECASE)
EX_SECTION = re.compile(r'<h2 id="ex(?:ercises)?"[^>]*>', re.IGNORECASE)
NEXT_H2 = re.compile(r"<h2[ >]")
LI = re.compile(r"<li[ >]")


def exercise_count(html: str) -> int:
    """<li> items between the Exercises <h2> and the next <h2>."""
    m = EX_SECTION.search(html)
    if not m:
        return 0
    end = NEXT_H2.search(html, m.end())
    body = html[m.end(): end.start() if end else len(html)]
    return len(LI.findall(body))


failures: list[str] = []
passed = 0


def check(ok: bool, label: str, detail: str = "") -> None:
    global passed
    if ok:
        passed += 1
    else:
        failures.append(f"{label}{': ' + detail if detail else ''}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


# --- Pages -------------------------------------------------------------------
course_dirs = sorted(p for p in (ROOT / "courses").iterdir() if p.is_dir())
check(bool(course_dirs), "courses/ has course directories")

nn_numpy_seen = False
for cdir in course_dirs:
    cid = cdir.name
    html_path = cdir / "index.html"
    check((cdir / "index.qmd").is_file(), f"{cid}: index.qmd source present")
    if not html_path.is_file():
        check(False, f"{cid}: rendered index.html present")
        continue
    html = read(html_path)
    check('lang="en"' in html[:400], f"{cid}: lang=en")
    check("theme.js" in html, f"{cid}: theme.js loaded")
    check(not FR_SWITCHER.search(html), f"{cid}: no FR switcher / French link")
    n_ex = exercise_count(html)
    if cid in NON_SCIENCE:
        check(True, f"{cid}: exercises (non-science exempt, {n_ex})")
    else:
        check(n_ex >= 6, f"{cid}: >= 6 exercises", f"found {n_ex}")
    if cid == "m1p1-refresher-neural-nets":
        qmd = read(cdir / "index.qmd") if (cdir / "index.qmd").is_file() else html
        nn_numpy_seen = bool(re.search(r"numpy|import np\b|np\.", qmd, re.IGNORECASE))

check(nn_numpy_seen, "NN refresher: NumPy primary")

# --- Root surface ------------------------------------------------------------
root_pages = ["index.html"]
for page in root_pages:
    p = ROOT / page
    check(p.is_file(), f"root: {page} present")
    if p.is_file():
        check(not FR_SWITCHER.search(read(p)), f"root: {page} no FR switcher")

linked_from = read(ROOT / "index.html")
for cdir in course_dirs:
    check(f"courses/{cdir.name}/" in linked_from, f"index: {cdir.name} reachable")

check((ROOT / "assets/paper.css").is_file(), "assets: paper.css present")
check((ROOT / "assets/theme.js").is_file(), "assets: theme.js present")

css = read(ROOT / "assets/paper.css")
check(".def" in css and ".thm" in css and ".note" in css,
      "paper.css: .def/.thm/.note styles")
check("prefers-color-scheme: dark" in css and 'data-theme="dark"' in css,
      "paper.css: dark blocks present")
check("localStorage" in read(ROOT / "assets/theme.js"), "theme.js: localStorage toggle")

# --- Specs index honesty -----------------------------------------------------
readme = read(ROOT / "specs/README.md")
for spec in sorted((ROOT / "specs").glob("*.md")):
    if spec.name in {"README.md", "_template-module.md"}:
        continue
    check(f"`{spec.stem}`" in readme, f"specs index: {spec.stem} listed")

# --- Single structural source (specs/competency-tree.md) ----------------------
# Structure pages never cite the brochure; the wiki is the only structural source.
structure_pages = ["index.html"]
for page in structure_pages:
    p = ROOT / page
    check(p.is_file(), f"structure: {page} present")
    if p.is_file():
        check("brochure" not in read(p).lower(), f"structure: {page} brochure-free")

check(not (ROOT / "curriculum.html").exists(),
      "curriculum.html deleted (tree lives on the home page)")
check(not (ROOT / "catalogue.html").exists(),
      "catalogue.html deleted (home tree is the full module index)")

# Satellite pages deleted (rev 4): coherence + exit-capabilities (+ FR redirects)
for gone in ["coherence-2years", "coherence-2ans", "exit-capabilities", "capacites-sortie"]:
    check(not (ROOT / gone).exists(), f"{gone}/ deleted")
FORBIDDEN = ["catalogue.html", "coherence-2years/", "exit-capabilities/",
             "coherence-2ans/", "capacites-sortie/"]
all_pages = list(ROOT.glob("*.html")) + list(ROOT.glob("courses/*/index.html")) + [ROOT / "en/index.html"]
for page in all_pages:
    if page.is_file():
        content = read(page)
        for f_ in FORBIDDEN:
            check(f_ not in content, f"no {f_} link in {page.relative_to(ROOT)}")

# Path descriptions (rev 4): justification paragraph wired to the buttons
home = read(ROOT / "index.html")
check('id="path-desc"' in home, "home: path description paragraph present")
check("generative spine" in home and "deployment spine" in home,
      "home: both route justifications written")
check('aria-live="polite"' in home, "home: path description announced politely")

# Skill checkpoints section (ex exit-capabilities), after Official documentation
check('id="checkpoints"' in home, "home: skill checkpoints section present")
check(home.find('id="official"') < home.find('id="checkpoints"'),
      "home: checkpoints section after official documentation")

home = read(ROOT / "index.html")
check('class="badge mandatory"' in home, "home: official Mandatory badges")
check('class="badge choice"' in home, "home: official Choose-N badges")
check("not yet published" in home, "home: M2 P2 honesty line")
check("TBC = " in home, "home: TBC abbreviation glossed")

# --- Home tree + path preselection (specs/path-preselection.md) ---------------
home = read(ROOT / "index.html")
check('id="curriculum-tree"' in home, "home: full curriculum tree present")
check("tree-cols" not in home, "home: tree is single-column")
buttons = home.count('data-path=')
check(buttons == 3, "home: exactly 3 path buttons", f"found {buttons}")
check('data-path="gllm"' in home and 'data-path="sys"' in home,
      "home: both recommended routes wired")
check("curriculum.html" not in home, "home: no link to the deleted curriculum.html")

# Refreshers listed inside the tree section
tree_html = home.split('id="curriculum-tree"')[1].split("</section>")[0]
for ref in ["m1p1-refresher-statistics", "m1p1-refresher-cs",
            "m1p1-refresher-neural-nets"]:
    check(f"courses/{ref}/index.html" in tree_html, f"home tree: {ref} listed")


# Route quotas: each route preselects EXACTLY N per official choice group, and
# every elective in a choice group carries a data-p marker (an unmarked li would
# stay bright on every route and inflate the visible count).
def _choice_group(marker: str) -> str:
    return home.split(marker)[1].split("</ul>")[0]


LI_ATTRS = re.compile(r"<li([^>]*)>")


def route_counts(seg: str):
    counts, unmarked = {"gllm": 0, "sys": 0}, 0
    for attrs in LI_ATTRS.findall(seg):
        m = re.search(r'data-p="([^"]*)"', attrs)
        if m is None:
            unmarked += 1
            continue
        for r in counts:
            if r in m.group(1).split():
                counts[r] += 1
    return counts, unmarked


for marker, quota, label in [
    ('class="badge choice">Choose 3</span> of:', 3, "P1 choose-3"),
    ('class="badge choice">Choose 1</span> of:', 1, "P2 choose-1"),
]:
    seg = _choice_group(marker)
    counts, unmarked = route_counts(seg)
    check(unmarked == 0, f"home {label}: every elective carries a path marker",
          f"{unmarked} unmarked")
    for r, c in counts.items():
        check(c == quota, f"home {label}: {r} preselects exactly {quota}",
              f"found {c}")

# Official documentation section (verified URLs)
off = home.split('id="official"')[1].split("</section>")[0] if 'id="official"' in home else ""
check(bool(off), "home: official documentation section present")
for domain in ["programmes.polytechnique.edu", "msct.dix.polytechnique.fr",
               "synapses.polytechnique.fr"]:
    check(domain in off, f"home: official docs link {domain}")

# --- De-branding: "Extrapolons" never appears on published pages --------------
published = [p for p in list(ROOT.glob("*.html")) + list((ROOT / "courses").glob("*/index.html"))
             + list((ROOT / "courses").glob("*/index.qmd"))
             + [ROOT / "assets/ATTRIBUTION.md", ROOT / "en/index.html",
                ROOT / "coherence-2ans/index.html", ROOT / "capacites-sortie/index.html"]
             if p.is_file()]
branded = [str(p.relative_to(ROOT)) for p in published
           if "extrapolons" in read(p).lower()]
check(not branded, "published pages Extrapolons-free", f"in {branded[:5]}")

# --- Report ------------------------------------------------------------------
total = passed + len(failures)
print(f"check_gates: {passed}/{total} checks passed")
for f in failures:
    print(f"FAIL  {f}")
sys.exit(1 if failures else 0)
