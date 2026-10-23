# Contract — projects and assessment on every science page; end-of-year projects

| Field | Value |
|---|---|
| ID | `projects-and-assessment` |
| Request | Owner, 22 October 2026: “propose project subjects to carry out solo or in groups, or classical assessments; then propose end-of-year projects that bring together what has been studied” |
| Scope | Section `## Projects and assessment {#projects}` of every science page (`courses/*/index.qmd` minus `specs/non-science-pages.md`); page `projects/index.qmd` |
| Gate | `tools/check_gates.py` checks that `projects/` exists and that the home page links to it. The per-course section counts below are the format for the owner of that page work. They are not enforced yet, because the subjects and exam proposals are not written. |
| Shared with | `knoel99/master-mva` (same section format) |
| Depends on | `specs/coherence-objectives.md` (objectives O1–O8 that the projects exercise) |

## Why

The official LLGA sheets announce quizzes, team projects, lab reports, paper implementations and written exams, but most LLGA sections of the 2026–2027 sheets display no modality. A student needs ready-to-use project subjects at the right scale, a picture of what an exam on the course looks like, and — at the end of each year — projects that make the courses work together, the way the master's objectives (`specs/coherence-objectives.md`) ask.

## Section format (between *Exercises* and *References*)

```
## Projects and assessment {#projects}

One paragraph: the official assessment of the course (from the fiche, or “not displayed”) and how the proposals below fit it; which master objectives (O1–O8) the projects exercise.

### Solo projects {#projects-solo}

1.  **[Solo · ≈ 20 h] Title.** Question studied; what to implement or prove; data or paper used; deliverables (code, 4–6 page report, 10-min talk); chapters used (ch. 2, 4); success criterion.

### Group projects {#projects-group}

1.  **[Group of 3 · ≈ 30 h each] Title.** Same fields, plus how the work splits between members.

### Written exam (proposal) {#projects-exam}

Format line (duration, documents allowed, number of exercises).

1.  **Question (n points).** Statement. *Expected*: the outline of a full-mark answer.

### Grading rubric (proposal) {#projects-rubric}

| Criterion | Weight | What earns the marks |
|---|---|---|
```

## Rules

- **P1** At least **2 solo** and **2 group** subjects; each names its scale (hours), its deliverables, the chapters it uses, and a success criterion. At least one subject is a **paper study** (reproduce or extend a named, real research paper with authors and year), and at least one connects the course to another LLGA module (a graph, an LLM, a generative model, an agent).
- **P2** Subjects are feasible: public or synthetic data, a laptop or a free GPU tier, a clear success criterion.
- **P3** The **written exam** proposal has at least **3 questions** with points summing to 20 and an expected-answer outline for each; it mixes a course question, a computation and a short proof.
- **P4** A **rubric** table gives criteria and weights summing to 100 %.
- **P5** Airy prose (`specs/front-redesign.md`): each list item ≤ 100 words; sub-bullets allowed.
- **P6** No invented official rule: the opening paragraph quotes the fiche; the proposals are labelled as proposals.

## End-of-year projects (`projects/index.qmd`)

- **Year 1** — integrative projects at the end of Period 2, combining the Period 1 foundations (Machine Learning, a Deep Learning course, the chosen options) with the Period 2 core (Reinforcement Learning, Graph ML, Text Mining & NLP) and the Choose-1 elective; sized for 4–6 weeks of a group of 3–4, a dress rehearsal for the research internship.
- **Year 2** — integrative projects suited to the official **Transverse project (8 ECTS)**, combining the Year 2 core (Large Language Models, Geometric Data) with the Period 2 advanced topics and Year 1 foundations.
- For each project: the courses it draws on (links), the research or engineering question, the master objectives it exercises (O1–O8), milestones, deliverables, evaluation, and solo / group variants. At least one project per route of the home page (Graph × LLM, AI systems).

## Proof

- `python3 tools/check_gates.py`: for each science page, the section exists in the right place with ≥ 2 `**[Solo` items, ≥ 2 `**[Group` items and ≥ 3 numbered exam questions; the projects page exists, is linked from the home page, and links only existing course pages.
