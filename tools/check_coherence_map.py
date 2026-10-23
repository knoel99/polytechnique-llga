#!/usr/bin/env python3
"""Fail unless the coherence report scores every science course on O1 to O8."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "specs" / "coherence-objectives-report.md"

FRAMING = {
    "m1-humanites",
    "m1-langues",
    "m1-sports",
    "m1p1-strategy-marketing",
    "m1p2-startup-entrepreneurship",
    "m2-ethical-issues-ai",
    "m1p3-research-internship",
    "m2-internship",
    "m2-projet-transverse",
}

SLUG_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`")
OBJECTIVES = [f"O{i}" for i in range(1, 9)]


def split_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def score_table(text: str) -> dict[str, list[int]]:
    lines = text.splitlines()
    header_at = None
    columns = None
    for index, line in enumerate(lines):
        cells = split_row(line)
        if not cells:
            continue
        positions = []
        for name in OBJECTIVES:
            if name not in cells:
                positions = []
                break
            positions.append(cells.index(name))
        if positions and positions == list(range(positions[0], positions[0] + 8)):
            header_at = index
            columns = positions
            break
    if header_at is None or columns is None:
        raise SystemExit("coherence map: no score table with columns O1 to O8")

    scores: dict[str, list[int]] = {}
    for line in lines[header_at + 1 :]:
        cells = split_row(line)
        if not cells:
            break
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        found = SLUG_RE.search(cells[0])
        if not found:
            break
        slug = found.group(1)
        raw = []
        for column in columns:
            if column >= len(cells):
                raise SystemExit(f"coherence map: {slug} is missing a score")
            raw.append(cells[column])
        try:
            values = [int(item) for item in raw]
        except ValueError:
            raise SystemExit(f"coherence map: {slug} has a non-integer score {raw}")
        if slug in scores:
            raise SystemExit(f"coherence map: duplicate row {slug}")
        scores[slug] = values
    return scores


def main() -> int:
    if not REPORT.is_file():
        print(f"coherence map: missing {REPORT.relative_to(ROOT)}", file=sys.stderr)
        return 1
    scores = score_table(REPORT.read_text(encoding="utf-8"))
    science = sorted(
        path.name
        for path in (ROOT / "courses").iterdir()
        if path.is_dir() and path.name not in FRAMING
    )
    failed = False
    missing = [slug for slug in science if slug not in scores]
    extra = [slug for slug in scores if slug not in science]
    if missing:
        failed = True
        print("coherence map: missing " + ", ".join(missing), file=sys.stderr)
    if extra:
        failed = True
        print("coherence map: unexpected " + ", ".join(extra), file=sys.stderr)
    for slug, values in scores.items():
        if any(value < 0 or value > 3 for value in values):
            failed = True
            print(f"coherence map: {slug} score outside 0-3 {values}", file=sys.stderr)
    expected = {
        "m1p2-nlp-text-mining": (1, 2),
        "m1p1-refresher-neural-nets": (6, 2),
    }
    for slug, (index, want) in expected.items():
        got = scores.get(slug)
        if got is None or got[index] != want:
            failed = True
            print(
                f"coherence map: {slug} O{index + 1} is "
                f"{None if got is None else got[index]}, expected {want}",
                file=sys.stderr,
            )
    if failed:
        return 1
    print(
        f"coherence map: {len(scores)} science courses, "
        "scores in 0-3, nlp O2=2, refresher neural nets O7=2"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
