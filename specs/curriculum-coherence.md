# Curriculum coherence, projects and assessment

| Field | Value |
|---|---|
| ID | `curriculum-coherence` |
| Request (owner, 22 October 2026) | "Analyse the overall coherence of the courses so that their content meets the objectives set by the master. Propose project topics, solo or in groups, or classical evaluations. Then propose end-of-year projects that bring together what has been studied." |
| Scope | 40 science pages, 9 framing pages, the home page, one new framing page `m1-integrative-projects` |
| Gates | `tools/check_gates.py` (new checks below), `tools/check_progression.py`, `tools/check_airiness.py` |

## 1. Objectives of the master

The objectives are taken from three official sources, read on 22 October 2026:
- the programme page;
- the course-content page;
- the curriculum wiki, last modified 9 September 2026.

| ID | Objective | Official wording |
|---|---|---|
| O1 | Theoretical foundation in machine and deep learning | "solid theoretical foundation in machine and deep learning" |
| O2 | Hands-on generative techniques, including graph generation | "hands-on experience with state-of-the-art generative techniques in the context of LLMs and graph generation" |
| O3 | Large Language Models | "special emphasis on Large Language Models (LLMs)" |
| O4 | Graph-structured data: GNNs, networks, molecules, logistics | "graph-structured data"; "Graph Neural Networks … networks, molecules, or logistics" |
| O5 | LLMs combined with graph methods, and multimodal generative AI | "Together, LLMs and graph methods enable multimodal generative AI" |
| O6 | Applications: healthcare, biology, pharma, finance, social networks, recommendation, logistics, communication | "apply them across diverse fields—from healthcare and biology to finance, social networks"; career prospects |
| O7 | Industry practice: projects, case studies, deployment | "hands-on industry expertise"; "Through projects, case studies, and industrial applications" |
| O8 | Responsible AI: ethics, law, fairness, privacy, security, explainability, sustainability | mandatory seminar "ethical issues, law and novel applications of AI" (IME_50430_EP, 6 ECTS) |
| O9 | Research readiness: papers, open problems, PhD track | "pursuing a PhD after this program is perfectly possible"; research-oriented internship |

## 2. Findings of the audit (23 October 2026)

**Method.**
- Ten readers each covered one group of pages.
- Three syntheses followed: objectives by path, prerequisite chains, and assessment and projects.
- A final adversarial pass checked about 115 claims with `grep` and by reading the cited passages:
  - 3 claims were refuted;
  - 2 severities were lowered;
  - 17 claims were corrected.
- No internal link was broken (985 checked).

**Paths judged.** Four paths through the official 2026–27 offering:
- (a) the mandatory core plus one Deep Learning course;
- (b) the site's Graph × LLM route;
- (c) the site's AI systems route;
- (d) the weakest legal choice of electives.

Reference-only notes do not count as offered.

| Objective | (a) core | (b) Graph × LLM | (c) AI systems | (d) weakest |
|---|---|---|---|---|
| O1 | met | met | met | met |
| O2 | thin | met | thin | thin |
| O3 | met | met | met, thin foundations | met |
| O4 | met, logistics missing | met, logistics missing | met, logistics missing | met, logistics missing |
| O5 | thin | met | mixed | thin |
| O6 | thin | mostly met | thin | thin |
| O7 | met, thin deployment | met | met | met, thin deployment |
| O8 | thin | met, fairness thin | met, with gaps | missing beyond the seminar |
| O9 | met | met | met | met |

Route (b) relies on seven M2 slots that are not yet confirmed (TBC).

### Structural causes

1. The Deep Learning P2 page was written as a sequel to Deep Learning P1, yet the wiki makes it the *only* Deep Learning course of its students. It never defined the transformer block, normalisation, dropout or LoRA, which NLP, the LLM course and several M2 pages assume. This was blocking.
2. The P2 electives of the single "choose 1" group pointed to one another as prerequisites or companions.
3. Four P1 pages leaned on Graph ML, which comes in P2.
4. Some gaps had no home in any offered course:
   - relation extraction for knowledge-graph construction;
   - group-fairness metrics;
   - privacy, law and energy;
   - hands-on graph generation;
   - logistics;
   - finance data;
   - a vector-index treatment, which existed only in the reference-only DBMS notes.
5. The transverse project page listed no subjects, and the ethics-seminar page was empty framing.

## 3. Decisions

### D1 — Fix the gaps inside existing modules, mandatory modules first

| Gap | Fix | Module |
|---|---|---|
| Transformer block, normalisation, dropout and LoRA on Deep-Learning-in-P2 paths | definition with PyTorch code; normalisation, residuals and dropout box; LoRA definition; recap boxes in NLP ch. 7 and LLMs | DL P2, NLP, LLMs ch. 4 (the site's LoRA reference) |
| Knowledge-graph construction | relation-extraction subsection, plus an exercise; the session-8 lab exports triples to the Graph ML GraphRAG lab | NLP ch. 6 |
| Diffusion on every path | "Diffusion in one page" with VAE and DDPM labs | DL P1 ch. 9 |
| Hands-on graph generation | runnable starters for the ER/SBM exercise and the ZINC generation exercise | Graph ML ch. 9 |
| Group fairness | fairness and subgroup evaluation section, Folktables exercise | ML 4.8 |
| Privacy, law, cost | privacy, memorisation, law and cost section | LLMs 9.6 |
| Retrieval layer, LLM + graph hybrids, multimodality, evaluation statistics | vector-index box, worked GraphRAG example, graph as soft tokens, concrete multimodality, statistics of LLM evaluation | LLMs ch. 7–9 |
| Logistics | attention policy for vehicle routing with REINFORCE and a rollout baseline; TSP exercise | RL ch. 5 |
| Finance, explainability | exercise on the Elliptic transaction graph; GNN explanation note; Shapley note | Graph ML ch. 8, ML ch. 6 |
| Healthcare, proteins | PubMedQA RAG exercise; protein binding-site worked example | LLMs ch. 7, Geometric Data ch. 8 |
| M2 direct entrants | language and graph modelling primer (self-study) | Refresher CS |

Every in-class addition keeps the page within 100–320 words per class hour (`specs/hours-and-progression.md`, R2). Larger additions go to self-study chapters or exercises.

### D2 — Prerequisites: self-contained recap boxes, never a dependency on an exclusive or later course

- A concept that a legal path may not have taught yet gets a `::: recap` box of 80–250 words where it is used. The box links the page that teaches it in full; when two mutually exclusive courses teach it, it links both.
- Reference-only notes are never prerequisites.
- Pages in the P2 choose-1 group are self-contained with respect to each other.
- P1 pages do not assume Graph ML.

### D3 — One reference module per repeated concept

For each concept retold in full on several pages, one page holds the full treatment; the others keep a short recap and link to it (audit §5).

| Concept | Reference page |
|---|---|
| attention | DL P1 ch. 6, and DL P2 for its path |
| LoRA | LLMs ch. 4 |
| vector indexes | LLMs ch. 7 |
| Markov chains | RL ch. 0 |
| skip-gram | Graph ML ch. 3 |
| RoPE, KV cache, speculative decoding | LLMs |
| differential privacy | Emerging ML ch. 5 (M1) and Privacy & UQ ch. 1–4 (M2) |
| membership inference | Security ch. 8 |

### D4 — Consistency fixes

The verified fixes of audit §6 are applied:
- "walks" instead of "paths" for $(A^k)_{ij}$;
- one convention for the DiGress transition matrix;
- the false claim that masking is exact conditioning, restated with a counterexample;
- scaling-law attributions;
- the speculative-decoding count;
- the MoE balancing condition;
- RLHF notation;
- mislabelled prerequisites;
- route badges on the M2 slot pages;
- "skill checkpoints" links that now lead to the career section.

Each Year-2 course labels its derivation sessions level 3, so that Year 2 reads as harder than Period 2.

### D5 — Every science page ends with `## Projects and assessment {#projects}`

The section sits after Exercises and before References, and is listed in the page contents. Its structure is fixed:

1. A `::: note` status box. It quotes the official assessment of the fiche verbatim, with its source section, and states that what follows are independent proposals. The consequence depends on the official mode:
   - **exam-only** unit: the projects are formative;
   - **project-based** unit: the projects are candidate topics for the official project;
   - **mode not displayed**: a balanced default is proposed.
2. `### A classical assessment {#projects-exam}`:
   - a components table (weights and formats consistent with the official mode);
   - the resit;
   - 4–6 sample questions with marking points.
3. `### Projects {#projects-list}`:
   - one grading grid for the whole page;
   - 3–5 project cards `#### P<k> · ★… · solo|group · <Title> {#proj-<k>}`, sorted by difficulty. Each card is a table giving the goal (measurable, against a baseline the module teaches), the data (public, licence named, URL checked), the chapters used, the deliverables, the effort and compute, the objectives served, an optional specific criterion and a "going further" line.
4. `### End-of-year projects {#projects-capstone}`: which Year-1 integrative projects or Year-2 capstones use the module.

House rules:
- **Data:** no credentialed or controlled-access data.
- **Compute:** a laptop CPU or one free Colab GPU, with no paid API.
- **Effort per student:**
  - 36 h / 4.5 ECTS course: ★ 8–15 h, ★★ 15–25 h, ★★★ 25–35 h;
  - 24 h / 2 ECTS course: at most 20 h;
  - 12 h refresher: at most 12 h.
- **Responsible AI:** every card on people's data has a line on consent, licence, subgroup errors or misuse.

A page that stated a grading scheme contradicting its sheet now points to `#projects`.

### D6 — End-of-year projects

- **Year 1:** a new framing page `courses/m1-integrative-projects/` with the badge "Off-curriculum support". No course code is invented (AGENTS.md principle 3). It holds eight team projects, `#y1-1` to `#y1-8`. Each combines the mandatory Year-1 courses, one Deep Learning course and route electives, and covers one domain:
  - pharma;
  - finance;
  - social media;
  - recommendation;
  - logistics;
  - chemistry;
  - medical imaging;
  - public institutions.

  Each comes with a six-week milestone plan, a rubric, route variants and an internship seed. The page is listed in the home tree (Period 3).
- **Year 2:** the transverse project page (MDC_54430_EP, 8 ECTS, half a day a week) gets a capstone catalogue of eight briefs, `#c1` to `#c8`. Each brief is written for a generic role and combines Year-1 foundations with Year-2 modules. It comes with milestones over M2 P1–P2, a rubric, operations milestones (CI, serving, monitoring) and a responsible-AI checklist.
- **Ethics seminar:** the page (IME_50430_EP) gets three things:
  - a map of where each trust topic is taught;
  - one page on the law (AI Act, GDPR);
  - three cases and assessment proposals.

### D7 — Home page

A section "How the courses serve the master's objectives" (`#objectives`) gives:
- the nine objectives;
- the modules that carry each one, with mandatory modules first;
- what was added to close the gaps;
- links to the end-of-year projects.

## 4. Proof

- `python3 tools/check_gates.py` passes. New checks:
  - every science page has `id="projects"`, a classical-assessment block and at least three project cards, one of them a group project;
  - the Year-1 page has projects `y1-1` to `y1-8`;
  - the transverse project page has capstones `c1` to `c8`;
  - the home page has `id="objectives"`.
- `python3 tools/check_progression.py` and `python3 tools/check_airiness.py` pass on every page.
- KaTeX renders every span; no literal `$$` remains in rendered pages.
- Every dataset URL of the new sections answered HTTP 200 when written (checked with `curl`).

## 5. Result (24 October 2026)

- **Projects and assessment** on all 40 science pages:
  - 156 project cards: 87 solo, 69 group;
  - 201 sample questions, each with marking points that add up to the paper's total.
- **End-of-year projects**: eight Year-1 integrative projects and eight Year-2 capstones.
- **Every gap of §3 is fixed** in the module named there. The verified audit's prerequisite, redundancy and consistency fixes are applied as well.
- **Writer checks.** Each page was written by one agent, who checked every URL with `curl`.
  - github.com answers 403 through the build proxy, so repositories were checked through `raw.githubusercontent.com`.
- **Independent review.** A second agent then re-checked each page adversarially. About 90 defects were found and fixed, among them:
  - marking keys that did not add up;
  - wrong dataset sizes and licences;
  - chapters cited for content they do not teach;
  - a false claim about VITS likelihoods;
  - a dropout-dependent causal check.
- **Law.** The Digital Omnibus on AI was read in the Official Journal: Regulation (EU) 2026/1744 of 8 July 2026 (OJ of 24 July 2026). The AI Act timelines of the LLM, explainability and ethics pages follow it.
- **Checks passed:**
  - `check_gates.py`: 1055/1055;
  - `check_progression.py`: 40/40;
  - `check_airiness.py`: 50/50 pages;
  - KaTeX: every span renders;
  - no literal `$$` in any page;
  - internal links and anchors resolve;
  - Playwright: 51 pages × (1440 px, 390 px) × (light, dark), with no overflow, no script error and text contrast ≥ 7:1.
