#!/usr/bin/env python3
"""Mechanical gates from AGENTS.md (Spec Kit-compatible / BMAD light).

Run from the repository root:  python3 tools/check_gates.py
Exit code 0 = all gates pass; 1 = at least one gate failed.

Checks (code-level proxies for the manual gates):
- Pages: courses/<id>/index.qmd + rendered index.html, lang="en", theme.js loaded.
- Index: every course linked from root index.html or catalogue.html (homepage-source-decision).
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
root_pages = ["index.html", "catalogue.html"]
for page in root_pages:
    p = ROOT / page
    check(p.is_file(), f"root: {page} present")
    if p.is_file():
        check(not FR_SWITCHER.search(read(p)), f"root: {page} no FR switcher")

linked_from = read(ROOT / "index.html") + read(ROOT / "catalogue.html")
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
structure_pages = [
    "index.html", "catalogue.html", "curriculum.html",
    "coherence-2years/index.html", "exit-capabilities/index.html",
]
for page in structure_pages:
    p = ROOT / page
    check(p.is_file(), f"structure: {page} present")
    if p.is_file():
        check("brochure" not in read(p).lower(), f"structure: {page} brochure-free")

cur = ROOT / "curriculum.html"
check(cur.is_file(), "curriculum tree page present")
if cur.is_file():
    check("msct.dix.polytechnique.fr/llga/wiki" in read(cur),
          "curriculum tree links the official wiki")
check("curriculum.html" in read(ROOT / "index.html"),
      "home links the curriculum tree")

cat = read(ROOT / "catalogue.html")
check('class="badge mandatory"' in cat, "catalogue: official Mandatory badges")
check('class="badge choice"' in cat, "catalogue: official Choose-N badges")
check("not yet published" in cat, "catalogue: M2 P2 honesty line")

# --- Report ------------------------------------------------------------------
total = passed + len(failures)
print(f"check_gates: {passed}/{total} checks passed")
for f in failures:
    print(f"FAIL  {f}")
sys.exit(1 if failures else 0)
