from __future__ import annotations

import ast
import enum
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


def _default_repo() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent.parent, here.parent, Path("/workspace")):
        gate = candidate / "tools" / "check_gates.py"
        if gate.is_file() and (candidate / "courses").is_dir():
            return candidate
    return Path("/workspace")


REPO = _default_repo()

H2 = "## Projects and assessment {#projects}"
SOLO_PREFIX = "### Solo projects"
GROUP_PREFIX = "### Group projects"
EXAM_PREFIX = "### Written exam"
RUBRIC_PREFIX = "### Grading rubric"
SOLO_H = "### Solo projects {#projects-solo}"
GROUP_H = "### Group projects {#projects-group}"
EXAM_H = "### Written exam (proposal) {#projects-exam}"
RUBRIC_H = "### Grading rubric (proposal) {#projects-rubric}"

PROPOSAL_SENTENCE = "The questions and project subjects below are **proposals**."

PAPER_RE = re.compile(
    r"paper study of\s+[A-Z][^()\n]{1,120}\(\d{4}\)",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"\]\(\.\./([a-z0-9-]+)/index\.html")
POINTS_RE = re.compile(r"^\d+\.\s+\*\*Question \((\d+) points?\)", re.MULTILINE)
NUMBERED_RE = re.compile(r"^\d+\.\s", re.MULTILINE)
WEIGHT_RE = re.compile(r"^\|[^|\n]+\|\s*(\d+)\s*%\s*\|", re.MULTILINE)
HEADING_RE = re.compile(rf"^{re.escape(H2)}\s*$", re.MULTILINE)
UE_RE = re.compile(r"\b[A-Z]{2,}_[0-9]{4,}(?:_[A-Z0-9]+)?\b")
ANCHOR_ID_RE = re.compile(r"\{#([\w-]+)")
ANCHOR_ID_ATTR_RE = re.compile(r'id="([\w-]+)"')
ANCHOR_REF_RE = re.compile(r"\]\(#([\w-]+)\)")


class ProjectError(Exception):
    pass


class Objective(enum.Enum):
    O1 = "O1"
    O2 = "O2"
    O3 = "O3"
    O4 = "O4"
    O5 = "O5"
    O6 = "O6"
    O7 = "O7"
    O8 = "O8"


class DataKind(enum.Enum):
    PUBLIC = "public"
    SYNTHETIC = "synthetic"


class Compute(enum.Enum):
    LAPTOP = "laptop"
    FREE_GPU = "free GPU"


class ExamKind(enum.Enum):
    COURSE = "course question"
    COMPUTATION = "computation"
    PROOF = "short proof"


class _Brand(int):
    label = "value"

    def __new__(cls, value: int) -> _Brand:
        if type(value) is not int:
            raise ProjectError(f"{cls.label} must be a plain int")
        if value <= 0:
            raise ProjectError(f"{cls.label} must be positive")
        return int.__new__(cls, value)


class Hours(_Brand):
    label = "hours"


class Points(_Brand):
    label = "points"


class Percent(_Brand):
    label = "weight"


def _plain(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProjectError(f"{label} must be a non-empty string")
    if "\n" in value or "\r" in value:
        raise ProjectError(f"{label} must be one line")
    if "{#" in value or value.lstrip().startswith("#"):
        raise ProjectError(f"{label} cannot carry a heading or an anchor id")
    return value.strip()


def _maybe_math(value: str | None, label: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ProjectError(f"{label} must be a non-empty display block")
    if "{#" in value or "$$" in value:
        raise ProjectError(f"{label} must not contain an anchor id or dollar fences")
    for line in value.splitlines():
        if line.lstrip().startswith("#"):
            raise ProjectError(f"{label} cannot contain a heading")
    return value.strip("\n")


def _tuple(label: str, value: object, minimum: int) -> tuple:
    if type(value) is not tuple:
        raise ProjectError(f"{label} must be a tuple")
    if len(value) < minimum:
        raise ProjectError(f"{label} needs at least {minimum}")
    return value


@dataclass(frozen=True)
class Paper:
    authors: str
    year: int
    title: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "authors", _plain(self.authors, "paper authors"))
        object.__setattr__(self, "title", _plain(self.title, "paper title"))
        if type(self.year) is not int or not 1000 <= self.year <= 9999:
            raise ProjectError("paper year must be a four-digit int so the gate can read it")
        if "(" in self.authors or ")" in self.authors:
            raise ProjectError("put the year in Paper.year, not in the authors")


@dataclass(frozen=True)
class CrossLink:
    slug: str
    label: str

    def __post_init__(self) -> None:
        slug = _plain(self.slug, "cross-link slug")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ProjectError("cross-link slug must be a course directory name")
        object.__setattr__(self, "slug", slug)
        object.__setattr__(self, "label", _plain(self.label, "cross-link label"))


@dataclass(frozen=True)
class ChapterRef:
    number: int

    def __post_init__(self) -> None:
        if type(self.number) is not int or self.number < 0:
            raise ProjectError("chapter number must be an int >= 0")


@dataclass(frozen=True)
class Subject:
    title: str
    hours: Hours
    question: str
    implement: str
    data: str
    data_kind: DataKind
    compute: Compute
    deliverables: str
    chapters: tuple[ChapterRef, ...]
    success: str
    paper: Paper | None = None
    cross_link: CrossLink | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "title", _plain(self.title, "title"))
        object.__setattr__(self, "question", _plain(self.question, "question"))
        object.__setattr__(self, "implement", _plain(self.implement, "implement"))
        object.__setattr__(self, "data", _plain(self.data, "data"))
        object.__setattr__(self, "deliverables", _plain(self.deliverables, "deliverables"))
        object.__setattr__(self, "success", _plain(self.success, "success"))
        if type(self.hours) is not Hours:
            raise ProjectError("hours must be Hours")
        if not isinstance(self.data_kind, DataKind) or not isinstance(self.compute, Compute):
            raise ProjectError("data_kind and compute must be the enums")
        chapters = _tuple("chapters", self.chapters, 1)
        if not all(type(c) is ChapterRef for c in chapters):
            raise ProjectError("chapters must contain ChapterRef values")
        if len({c.number for c in chapters}) != len(chapters):
            raise ProjectError("chapters must not repeat a number")
        if self.paper is not None and type(self.paper) is not Paper:
            raise ProjectError("paper must be Paper or None")
        if self.cross_link is not None and type(self.cross_link) is not CrossLink:
            raise ProjectError("cross_link must be CrossLink or None")


@dataclass(frozen=True)
class Group:
    subject: Subject
    size: int
    split: str

    def __post_init__(self) -> None:
        if type(self.subject) is not Subject:
            raise ProjectError("group subject must be a Subject")
        if type(self.size) is not int or self.size < 2:
            raise ProjectError("group size must be an int >= 2")
        object.__setattr__(self, "split", _plain(self.split, "split"))


@dataclass(frozen=True)
class NotDisplayed:
    reason: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "reason", _plain(self.reason, "reason"))


@dataclass(frozen=True)
class FicheQuote:
    """verbatim must already occur in the qmd outside this section. apply() checks."""

    verbatim: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "verbatim", _plain(self.verbatim, "fiche quotation"))


@dataclass(frozen=True)
class ExamQuestion:
    points: Points
    kind: ExamKind
    lead: str
    parts: tuple[str, ...]
    expected: tuple[str, ...]
    display: str | None = None
    expected_display: str | None = None

    def __post_init__(self) -> None:
        if type(self.points) is not Points:
            raise ProjectError("question points must be Points")
        if not isinstance(self.kind, ExamKind):
            raise ProjectError("question kind must be ExamKind")
        object.__setattr__(self, "lead", _plain(self.lead, "question lead"))
        parts = _tuple("question parts", self.parts, 0)
        expected = _tuple("expected outline", self.expected, 1)
        object.__setattr__(self, "parts", tuple(_plain(p, "question part") for p in parts))
        object.__setattr__(
            self, "expected", tuple(_plain(p, "expected line") for p in expected)
        )
        object.__setattr__(self, "display", _maybe_math(self.display, "display"))
        object.__setattr__(
            self, "expected_display", _maybe_math(self.expected_display, "expected display")
        )


@dataclass(frozen=True)
class Exam:
    duration_hours: int
    materials: str
    questions: tuple[ExamQuestion, ...]

    def __post_init__(self) -> None:
        if type(self.duration_hours) is not int or self.duration_hours <= 0:
            raise ProjectError("exam duration must be a positive int")
        object.__setattr__(self, "materials", _plain(self.materials, "exam materials"))
        questions = _tuple("exam questions", self.questions, 3)
        if not all(type(q) is ExamQuestion for q in questions):
            raise ProjectError("exam questions must be ExamQuestion values")
        if sum(q.points for q in questions) != 20:
            raise ProjectError("exam points must sum to 20")
        kinds = {q.kind for q in questions}
        if kinds != set(ExamKind):
            raise ProjectError("exam must include a course question, a computation, and a short proof")


@dataclass(frozen=True)
class RubricRow:
    criterion: str
    weight: Percent
    earns: str

    def __post_init__(self) -> None:
        criterion = _plain(self.criterion, "criterion")
        earns = _plain(self.earns, "what earns the marks")
        if "|" in criterion or "|" in earns:
            raise ProjectError("rubric cells cannot contain a pipe")
        if criterion.lower() == "total":
            raise ProjectError("the rubric has no total row; the weight sum is derived")
        if type(self.weight) is not Percent:
            raise ProjectError("weight must be Percent")
        object.__setattr__(self, "criterion", criterion)
        object.__setattr__(self, "earns", earns)


@dataclass(frozen=True)
class Assessment:
    opening: NotDisplayed | FicheQuote
    objectives: tuple[Objective, ...]
    solos: tuple[Subject, ...]
    groups: tuple[Group, ...]
    exam: Exam
    rubric: tuple[RubricRow, ...]

    def __post_init__(self) -> None:
        if type(self.opening) not in (NotDisplayed, FicheQuote):
            raise ProjectError("opening must be NotDisplayed or FicheQuote")
        objectives = _tuple("objectives", self.objectives, 1)
        if not all(isinstance(o, Objective) for o in objectives):
            raise ProjectError("objectives must be Objective values")
        if len(set(objectives)) != len(objectives):
            raise ProjectError("objectives must not repeat")
        solos = _tuple("solos", self.solos, 2)
        groups = _tuple("groups", self.groups, 2)
        if not all(type(s) is Subject for s in solos):
            raise ProjectError("solos must be Subject values")
        if not all(type(g) is Group for g in groups):
            raise ProjectError("groups must be Group values")
        if type(self.exam) is not Exam:
            raise ProjectError("exam must be an Exam")
        rubric = _tuple("rubric", self.rubric, 1)
        if not all(type(r) is RubricRow for r in rubric):
            raise ProjectError("rubric must be RubricRow values")
        if sum(r.weight for r in rubric) != 100:
            raise ProjectError("rubric weights must sum to 100")
        subjects = list(solos) + [g.subject for g in groups]
        if not any(s.paper is not None for s in subjects):
            raise ProjectError("at least one subject must name a paper")
        if not any(s.cross_link is not None for s in subjects):
            raise ProjectError("at least one subject must link to another course")


@dataclass(frozen=True)
class ApplyResult:
    slug: str
    status: str
    path: str
    preexisting_broken_anchors: tuple[str, ...]


def _objective_sentence(objectives: tuple[Objective, ...]) -> str:
    labels = [f"**{item.value}**" for item in objectives]
    if len(labels) == 1:
        return f"The projects exercise objective {labels[0]}."
    if len(labels) == 2:
        return f"The projects exercise objectives {labels[0]} and {labels[1]}."
    return (
        "The projects exercise objectives "
        + ", ".join(labels[:-1])
        + f", and {labels[-1]}."
    )


def _opening_paragraph(opening: NotDisplayed | FicheQuote, objectives: tuple[Objective, ...]) -> str:
    objectives_sentence = _objective_sentence(objectives)
    if type(opening) is NotDisplayed:
        return (
            f"Official assessment: not displayed. {opening.reason} "
            f"{PROPOSAL_SENTENCE} {objectives_sentence}"
        )
    quoted = opening.verbatim.replace('"', "'")
    return (
        f'Official assessment, quoted from this page: "{quoted}" '
        f"{PROPOSAL_SENTENCE} {objectives_sentence}"
    )


def _chapter_list(chapters: tuple[ChapterRef, ...]) -> str:
    return ", ".join(f"ch. {c.number}" for c in chapters)


def _paper_clause(paper: Paper | None) -> str:
    if paper is None:
        return ""
    return f' Paper study of {paper.authors} ({paper.year}), "{paper.title}".'


def _success_line(subject: Subject) -> str:
    if subject.cross_link is None:
        return f"    -   *Success*: {subject.success}"
    link = subject.cross_link
    return (
        f"    -   *Success*: {subject.success} "
        f"See [{link.label}](../{link.slug}/index.html)."
    )


def _subject_lines(index: int, label: str, subject: Subject, extra: tuple[str, ...] = ()) -> list[str]:
    lines = [
        f"{index}.  **{label} {subject.title}.** {subject.question}{_paper_clause(subject.paper)}",
        f"    -   *Implement*: {subject.implement}",
        (
            f"    -   *Data*: {subject.data_kind.value} data on a {subject.compute.value}. "
            f"{subject.data}"
        ),
    ]
    lines.extend(extra)
    lines.extend(
        [
            f"    -   *Deliverables*: {subject.deliverables}",
            f"    -   *Chapters*: {_chapter_list(subject.chapters)}.",
            _success_line(subject),
        ]
    )
    return lines


def _math_block(text: str | None) -> list[str]:
    if text is None:
        return []
    return ["", "$$", text, "$$"]


def render(assessment: Assessment) -> str:
    if type(assessment) is not Assessment:
        raise ProjectError("render takes an Assessment")
    lines = [H2, "", _opening_paragraph(assessment.opening, assessment.objectives), "", SOLO_H, ""]
    for i, subject in enumerate(assessment.solos, start=1):
        label = f"[Solo · ≈ {int(subject.hours)} h]"
        lines.extend(_subject_lines(i, label, subject))
    lines.extend(["", GROUP_H, ""])
    for i, group in enumerate(assessment.groups, start=1):
        label = f"[Group of {group.size} · ≈ {int(group.subject.hours)} h each]"
        extra = (f"    -   *Split*: {group.split}",)
        lines.extend(_subject_lines(i, label, group.subject, extra))
    exam = assessment.exam
    lines.extend(
        [
            "",
            EXAM_H,
            "",
            (
                f"*Format*: {exam.duration_hours} h written exam, {exam.materials}; "
                f"{len(exam.questions)} questions, 20 points."
            ),
            "",
        ]
    )
    for i, question in enumerate(exam.questions, start=1):
        lines.append(f"{i}.  **Question ({int(question.points)} points).** {question.lead}")
        lines.extend(_math_block(question.display))
        for part in question.parts:
            lines.append(f"    -   {part}")
        lines.append("")
        lines.append("    *Expected*:")
        lines.extend(_math_block(question.expected_display))
        lines.append("")
        for outline in question.expected:
            lines.append(f"    -   {outline}")
    lines.extend(
        [
            "",
            RUBRIC_H,
            "",
            "| Criterion | Weight | What earns the marks |",
            "|---|---|---|",
        ]
    )
    for row in assessment.rubric:
        lines.append(f"| {row.criterion} | {int(row.weight)} % | {row.earns} |")
    return "\n".join(lines) + "\n"


def _subject_region(section_body: str) -> str:
    if SOLO_PREFIX not in section_body:
        return section_body
    rest = section_body.split(SOLO_PREFIX, 1)[1]
    return rest.split(EXAM_PREFIX, 1)[0]


def _exam_slice(section_body: str) -> str | None:
    if EXAM_PREFIX not in section_body:
        return None
    rest = section_body.split(EXAM_PREFIX, 1)[1]
    return re.split(r"^### ", rest, maxsplit=1, flags=re.MULTILINE)[0]


def _rubric_slice(section_body: str) -> str | None:
    if RUBRIC_PREFIX not in section_body:
        return None
    rest = section_body.split(RUBRIC_PREFIX, 1)[1]
    return re.split(r"^### ", rest, maxsplit=1, flags=re.MULTILINE)[0]


def _course_on_disk(root: Path, item: str, slug: str | None) -> bool:
    if slug is not None and item == slug:
        return False
    return (root / "courses" / item / "index.qmd").is_file()


def gate_invariants(
    section_body: str, slug: str | None = None, root: Path | None = None
) -> tuple[str, ...]:
    repo = REPO if root is None else root
    findings: list[str] = []
    region = _subject_region(section_body)
    if not PAPER_RE.search(region):
        findings.append("P1 paper study with authors and a year")
    links = LINK_RE.findall(region)
    if not any(_course_on_disk(repo, item, slug) for item in links):
        findings.append("P1 cross-link to another course")
    exam = _exam_slice(section_body)
    if exam is None:
        findings.append("P3 written exam heading")
    else:
        parsed = [int(n) for n in POINTS_RE.findall(exam)]
        numbered = NUMBERED_RE.findall(exam)
        if not parsed or len(parsed) != len(numbered) or sum(parsed) != 20:
            findings.append(f"P3 points sum to 20 (parsed {parsed})")
    rubric = _rubric_slice(section_body)
    if rubric is None:
        findings.append("P4 rubric heading")
    else:
        weights = [int(n) for n in WEIGHT_RE.findall(rubric)]
        if sum(weights) != 100:
            findings.append(f"P4 weights sum to 100 (parsed {weights})")
    return tuple(findings)


def exempt_slugs(root: Path = REPO) -> frozenset[str]:
    source = (root / "tools" / "check_gates.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "NON_SCIENCE":
                return frozenset(ast.literal_eval(node.value))
    raise ProjectError("NON_SCIENCE is missing from check_gates.py")


def missing_slugs(root: Path = REPO) -> tuple[str, ...]:
    exempt = exempt_slugs(root)
    missing: list[str] = []
    for path in sorted((root / "courses").iterdir()):
        qmd = path / "index.qmd"
        if not path.is_dir() or not qmd.is_file() or path.name in exempt:
            continue
        text = qmd.read_text(encoding="utf-8")
        if not HEADING_RE.search(text):
            missing.append(path.name)
    return tuple(missing)


def _cut_section(text: str) -> str:
    found = list(HEADING_RE.finditer(text))
    if not found:
        return text
    if len(found) > 1:
        raise ProjectError("the qmd already has two projects headings")
    start = found[0].start()
    rest = text[found[0].end() :]
    ends: list[int] = []
    next_h2 = re.search(r"^## ", rest, re.MULTILINE)
    if next_h2:
        ends.append(next_h2.start())
    ref = rest.find("## References")
    if ref >= 0:
        ends.append(rest.rfind("\n", 0, ref) + 1)
    end = found[0].end() + min(ends) if ends else len(text)
    return text[:start] + text[end:]


def _insertion_index(text: str) -> int:
    if HEADING_RE.search(text):
        raise ProjectError("the projects heading is still present")
    exercises = text.find("## Exercises")
    references = text.find("## References")
    if exercises < 0 or references < 0 or exercises >= references:
        raise ProjectError("need ## Exercises before the references marker")
    line_start = text.rfind("\n", 0, references) + 1
    line_end = text.find("\n", references)
    line = text[line_start : len(text) if line_end < 0 else line_end]
    if line.startswith("## "):
        insert_at = line_start
    elif line.startswith("### "):
        previous = text.rfind("\n## ", 0, line_start)
        if previous < 0:
            raise ProjectError("the references marker has no enclosing h2")
        insert_at = previous + 1
    else:
        raise ProjectError("the references marker is not on a heading line")
    if insert_at <= exercises:
        raise ProjectError("the insertion point is not after Exercises")
    return insert_at


def _splice(text: str, rendered: str) -> str:
    if not rendered.startswith(H2 + "\n"):
        raise ProjectError("rendered section must start with the contract heading")
    if HEADING_RE.search(rendered[len(H2) :]) or "\n## " in rendered:
        raise ProjectError("rendered section must contain one h2, the contract heading")
    body = _cut_section(text)
    insert_at = _insertion_index(body)
    prefix = body[:insert_at].rstrip("\n") + "\n\n"
    suffix = body[insert_at:].lstrip("\n")
    return prefix + rendered.rstrip("\n") + "\n\n" + suffix


def _chapter_present(text: str, number: int) -> bool:
    return re.search(rf"\{{#ch{number}\b", text) is not None


def _broken_anchors(text: str) -> tuple[str, ...]:
    ids = set(ANCHOR_ID_RE.findall(text)) | set(ANCHOR_ID_ATTR_RE.findall(text))
    refs = set(ANCHOR_REF_RE.findall(text))
    return tuple(sorted(refs - ids))


def _airiness_violations(section: str, root: Path) -> list:
    import importlib.util

    path = root / "tools" / "check_airiness.py"
    spec = importlib.util.spec_from_file_location("_llga_airiness", path)
    if spec is None or spec.loader is None:
        raise ProjectError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.violations(section + "\n\n## References\n")


def _page_checks(page_without_section: str, assessment: Assessment, slug: str, root: Path) -> None:
    if type(assessment.opening) is FicheQuote:
        if assessment.opening.verbatim not in page_without_section:
            raise ProjectError("fiche quotation is not already on the page")
    for subject in list(assessment.solos) + [g.subject for g in assessment.groups]:
        for chapter in subject.chapters:
            if not _chapter_present(page_without_section, chapter.number):
                raise ProjectError(f"the page has no {{#ch{chapter.number}}}")
        link = subject.cross_link
        if link is None:
            continue
        if link.slug == slug:
            raise ProjectError("a cross-link must name another course")
        target = root / "courses" / link.slug / "index.qmd"
        if not target.is_file():
            raise ProjectError(f"cross-link target does not exist: {link.slug}")
    rendered = render(assessment)
    invented = set(UE_RE.findall(rendered)) - set(UE_RE.findall(page_without_section))
    if invented:
        raise ProjectError(f"UE code is not already on the page: {sorted(invented)}")
    violations = _airiness_violations(rendered, root if (root / "tools" / "check_airiness.py").is_file() else REPO)
    if violations:
        detail = "; ".join(f"line {ln}: {rule} {msg}" for ln, rule, msg in violations[:8])
        raise ProjectError(f"airiness failed: {detail}")


def apply(slug: str, assessment: Assessment, root: Path = REPO) -> ApplyResult:
    if type(assessment) is not Assessment:
        raise ProjectError("apply takes an Assessment")
    if slug in exempt_slugs(root):
        raise ProjectError(f"{slug} is outside the science set")
    path = root / "courses" / slug / "index.qmd"
    if not path.is_file():
        raise ProjectError(f"missing {path}")
    original = path.read_text(encoding="utf-8")
    if len(HEADING_RE.findall(original)) > 1:
        raise ProjectError("the qmd already has two projects headings")
    page = _cut_section(original)
    _page_checks(page, assessment, slug, root)
    rendered = render(assessment)
    updated = _splice(original, rendered)
    section_ids = set(ANCHOR_ID_RE.findall(rendered))
    page_ids = set(ANCHOR_ID_RE.findall(page)) | set(ANCHOR_ID_ATTR_RE.findall(page))
    missing = set(ANCHOR_REF_RE.findall(rendered)) - page_ids - section_ids
    if missing:
        raise ProjectError(f"the section links to a missing anchor: {sorted(missing)}")
    broken = _broken_anchors(updated)
    if updated == original:
        return ApplyResult(slug, "unchanged", str(path), broken)
    temporary = path.with_name(path.name + ".projects.tmp")
    temporary.write_text(updated, encoding="utf-8")
    try:
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return ApplyResult(slug, "written", str(path), broken)


def _sample(opening: NotDisplayed | FicheQuote, link_slug: str) -> Assessment:
    paper = Paper(
        "Glorot and Bengio",
        2010,
        "Understanding the difficulty of training deep feedforward neural networks",
    )
    link = CrossLink(link_slug, "the paired module")

    def subject(title: str, named: Paper | None = None, jump: CrossLink | None = None) -> Subject:
        return Subject(
            title=title,
            hours=Hours(8),
            question="How does the baseline move when one factor changes?",
            implement="A NumPy script with one factorial contrast and a finite-difference check.",
            data="A few hundred rows already named on this page.",
            data_kind=DataKind.PUBLIC,
            compute=Compute.LAPTOP,
            deliverables="A script and a 4-page report.",
            chapters=(ChapterRef(1),),
            success="The check stays under the stated tolerance, and the report names the factor.",
            paper=named,
            cross_link=jump,
        )

    return Assessment(
        opening=opening,
        objectives=(Objective.O1,),
        solos=(
            subject("Baseline contrast", named=paper),
            subject("Second contrast"),
        ),
        groups=(
            Group(subject("Shared contrast", jump=link), 3, "One member codes, one writes the report."),
            Group(subject("Replication contrast"), 2, "One member replicates, one member reviews."),
        ),
        exam=Exam(
            duration_hours=2,
            materials="one handwritten A4 sheet",
            questions=(
                ExamQuestion(
                    Points(6),
                    ExamKind.COURSE,
                    "Name the estimator and the assumption it needs.",
                    ("State the hypothesis in one sentence.",),
                    ("The sample mean, with the variance term named.",),
                ),
                ExamQuestion(
                    Points(8),
                    ExamKind.COMPUTATION,
                    "Compute the one-step update.",
                    ("Give the numerical result.",),
                    ("The updated value is 2.",),
                    display="z = Wx",
                ),
                ExamQuestion(
                    Points(6),
                    ExamKind.PROOF,
                    "Prove the stated bound.",
                    ("Write the inequality you apply.",),
                    ("Apply that inequality once and name the constant.",),
                ),
            ),
        ),
        rubric=(
            RubricRow("Correctness", Percent(40), "The derivation and the numbers match."),
            RubricRow("Protocol", Percent(30), "The split and the seeds are stated."),
            RubricRow("Report", Percent(30), "A classmate can rerun the result."),
        ),
    )


def _line_at(text: str, index: int) -> str:
    end = text.find("\n", index)
    return text[index : len(text) if end < 0 else end]


def self_check(repo: Path = REPO) -> int:
    failures: list[str] = []

    def expect(ok: bool, label: str) -> None:
        if not ok:
            failures.append(label)
            print(f"FAIL  {label}")
        else:
            print(f"ok    {label}")

    exempt = exempt_slugs(repo)
    expect("m1-sports" in exempt and "m1p1-refresher-neural-nets" not in exempt, "exemption read from check_gates.py")
    expect(H2 in (repo / "tools" / "check_gates.py").read_text(encoding="utf-8"), "heading string matches check_gates.py")

    missing = missing_slugs(repo)
    expect(len(missing) == 39, f"missing slugs count is 39 (found {len(missing)})")
    expect("m1p1-refresher-neural-nets" not in missing, "neural-nets is not in the work list")
    expect("m1p2-advanced-deep-learning" in missing, "advanced-deep-learning chapter heading is not the contract heading")
    expect("m1-sports" not in missing, "non-science pages are not in the work list")

    neural = (repo / "courses" / "m1p1-refresher-neural-nets" / "index.qmd").read_text(encoding="utf-8")
    body = neural.split(H2, 1)[1].split("\n## ", 1)[0]
    neural_findings = gate_invariants(body, "m1p1-refresher-neural-nets")
    expect(neural_findings == (), f"neural-nets invariants empty (found {neural_findings})")
    exam = _exam_slice(body) or ""
    rubric = _rubric_slice(body) or ""
    print(
        "      neural-nets points",
        POINTS_RE.findall(exam),
        "weights",
        WEIGHT_RE.findall(rubric),
    )

    sample = _sample(FicheQuote("Official assessment: a final exam."), "m1p1-machine-learning")
    rendered = render(sample)
    expect(gate_invariants(rendered, "m1p1-demo") == (), "rendered sample passes the four invariants")
    stripped = rendered.replace("Paper study of", "Reading note on", 1)
    expect(any(item.startswith("P1 paper") for item in gate_invariants(stripped)), "dropping the paper phrase fails P1")
    missing_course = rendered.replace(
        "../m1p1-machine-learning/index.html", "../not-a-course/index.html"
    )
    expect(
        any(item.startswith("P1 cross-link") for item in gate_invariants(missing_course, "m1p1-demo")),
        "a slug with no course directory fails the cross-link",
    )

    nested = (
        "## Exercises {#ex}\n\n1.  **★ One.**\n\n"
        "## Sources {#sources}\n\n"
        f"{H2}\n\nOld body.\n\n"
        "### References\n\n-   Goodfellow.\n"
    )
    nested_cut = _cut_section(nested)
    expect("Old body." not in nested_cut and "Goodfellow." in nested_cut, "a nested section keeps the bibliography")
    nested_placed = _splice(nested, H2 + "\n\nProbe body.\n")
    expect(
        "Goodfellow." in nested_placed
        and nested_placed.find(H2) < nested_placed.find("## Sources")
        < nested_placed.find("### References"),
        "the nested section moves above Sources and keeps Goodfellow",
    )

    bad_order: list[str] = []
    for slug in missing + ("m1p1-refresher-neural-nets",):
        text = (repo / "courses" / slug / "index.qmd").read_text(encoding="utf-8")
        try:
            placed = _splice(text, H2 + "\n\nProbe body.\n")
        except ProjectError as exc:
            bad_order.append(f"{slug}: {exc}")
            continue
        exercises = placed.find("## Exercises")
        projects = placed.find(H2)
        references = placed.find("## References")
        if not (0 <= exercises < projects < references):
            bad_order.append(f"{slug}: order {exercises, projects, references}")
        if placed.count(H2) != 1:
            bad_order.append(f"{slug}: heading count {placed.count(H2)}")
        again = _splice(placed, H2 + "\n\nProbe body.\n")
        if again != placed:
            bad_order.append(f"{slug}: second splice moved bytes")
    expect(not bad_order, "legal slot on every science page; " + "; ".join(bad_order[:6]))

    def slot_line(slug: str) -> str:
        text = (repo / "courses" / slug / "index.qmd").read_text(encoding="utf-8")
        return _line_at(_cut_section(text), _insertion_index(_cut_section(text)))

    expect(slot_line("m1p1-machine-learning").startswith("## References"), "machine-learning slot is References")
    expect(slot_line("m1p1-refresher-statistics").startswith("## References"), "statistics slot is References")
    expect(
        slot_line("m1p1-refresher-neural-nets").startswith("## Sources, scope and references"),
        "neural-nets slot is the sources h2 above ### References",
    )
    image = (repo / "courses" / "m1p2-image-synthesis" / "index.qmd").read_text(encoding="utf-8")
    image_placed = _splice(image, H2 + "\n\nProbe body.\n")
    expect(
        image_placed.find(H2) < image_placed.find("## References") < image_placed.find("## A complete path tracer"),
        "image-synthesis keeps the path tracer after References",
    )

    raised = False
    try:
        Assessment(
            opening=NotDisplayed("No sheet displays a modality for this page."),
            objectives=(Objective.O1,),
            solos=_sample(NotDisplayed("No sheet displays a modality for this page."), "m1p1-other").solos,
            groups=_sample(NotDisplayed("No sheet displays a modality for this page."), "m1p1-other").groups,
            exam=Exam(
                duration_hours=2,
                materials="one sheet",
                questions=tuple(
                    ExamQuestion(Points(5), kind, "Lead.", ("Part.",), ("Outline.",))
                    for kind in ExamKind
                ),
            ),
            rubric=_sample(NotDisplayed("No sheet displays a modality for this page."), "m1p1-other").rubric,
        )
    except ProjectError:
        raised = True
    expect(raised, "points that sum to 15 cannot be built")

    with tempfile.TemporaryDirectory(prefix="projects-section-") as tmp:
        mini = Path(tmp)
        (mini / "tools").mkdir()
        (mini / "courses" / "m1p1-demo").mkdir(parents=True)
        (mini / "courses" / "m1p1-other").mkdir()
        os.symlink(repo / "tools" / "check_gates.py", mini / "tools" / "check_gates.py")
        os.symlink(repo / "tools" / "check_airiness.py", mini / "tools" / "check_airiness.py")
        (mini / "courses" / "m1p1-other" / "index.qmd").write_text("# other\n", encoding="utf-8")
        fixture = """---
title: Demo
---

## 1. Demo chapter {#ch1}

A short chapter. Official assessment: a final exam.

## Exercises {#ex}

1.  **★ One.** Do the small thing.

## Sources and scope {#sources}

The fiche line above is the quotation.

## References {#refs}

-   A book.
"""
        target = mini / "courses" / "m1p1-demo" / "index.qmd"
        target.write_text(fixture, encoding="utf-8")
        assessment = _sample(FicheQuote("Official assessment: a final exam."), "m1p1-other")
        first = apply("m1p1-demo", assessment, mini)
        second = apply("m1p1-demo", assessment, mini)
        written = target.read_text(encoding="utf-8")
        expect(first.status == "written" and second.status == "unchanged", "second apply writes nothing")
        expect(written.count(H2) == 1, "one heading after two applies")
        expect(not target.with_name("index.qmd.projects.tmp").exists(), "temp file is gone after replace")
        expect(
            written.find("## Exercises") < written.find(H2) < written.find("## References"),
            "fixture order matches the gate",
        )
        before = written
        try:
            apply("m1-sports", assessment, mini)
            expect(False, "exempt slug raises")
        except ProjectError:
            expect(True, "exempt slug raises")
        expect(target.read_text(encoding="utf-8") == before, "a refused apply leaves the qmd")
        target.write_text(written.replace(H2, H2 + "\n\n" + H2, 1), encoding="utf-8")
        try:
            apply("m1p1-demo", assessment, mini)
            expect(False, "duplicate heading raises")
        except ProjectError:
            expect(True, "duplicate heading raises")
        expect(target.read_text(encoding="utf-8").count(H2) == 2, "duplicate heading is not rewritten")

    print(f"self-check: {len(failures)} failures")
    return 1 if failures else 0


if __name__ == "__main__" and sys.argv[1:] == ["self-check"]:
    raise SystemExit(self_check())
