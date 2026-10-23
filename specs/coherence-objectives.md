# Contract — coherence of the courses with the master's objectives

| Field | Value |
|---|---|
| ID | `coherence-objectives` |
| Request | Owner, 22 October 2026: “analyse the overall coherence of the courses, so that their content fulfils the objectives set by the master” |
| Scope | All 49 pages under `courses/` (40 science pages, 9 framing pages), the home page, the new pages `projects/` and `notation/` |
| Full analysis | `specs/coherence-objectives-report.md` (current scores, applied local fixes, backlog). `specs/coherence-2026-10/` is the 22 October 2026 before-state: `report.md`, `objectives.md`, `prerequisites.md`, `redundancy-notation.md`, `errors.md`, `capstones.md` |
| Related | `specs/projects-and-assessment.md` (projects on every page, end-of-year projects) |

## Method

1. **Read every page in full.** One reader per page wrote a structured record. It covers the outcomes the page states, the concepts it actually teaches, the concepts it uses without teaching (with chapter ids), its links to other modules, notation, exercises, official assessment, existing project material, errors found, contribution to each objective, and project ideas. That makes 49 records and 473 reported issues (11 high, 122 medium, 340 low severity).
2. **Analyse across pages through five lenses.**
   - objectives coverage;
   - prerequisite chain and timeline;
   - redundancy and notation;
   - cross-page consistency and confirmation of the high-severity errors;
   - end-of-year projects.
3. **Plan bounded edits.** At most six coherence actions per page (87 "must", 107 "should"), plus the page's own issue list. The in-class prose of each page stays within 100 to 320 words per hour. Larger additions would go to signposted self-study sections. That plan was not carried out as chapter rewrites.
4. **Score the chapter body, then apply only local corrections.** The readable matrix, the applied fixes, and the backlog are in `specs/coherence-objectives-report.md`. No second agent reviewed a chapter rewrite, because those rewrites did not land. `python3 tools/check_coherence_map.py` checks the matrix.

## Objectives (from the official description quoted on the home page)

| Id | Objective |
|---|---|
| O1 | ML & DL foundations: statistical learning, optimisation, neural architectures and training |
| O2 | Generative modelling theory: probabilistic models, VAEs, GANs, flows, diffusion, autoregressive models |
| O3 | Large Language Models: Transformers, pre-training, fine-tuning and alignment, inference, retrieval and agents, evaluation |
| O4 | Graph-structured data: GNNs for networks, molecules, logistics |
| O5 | Graph × LLM: knowledge graphs with LLMs, GraphRAG, neuro-symbolic reasoning — the distinctive emphasis |
| O6 | Multimodal generative AI: vision, language, speech, 3D / geometric data |
| O7 | Hands-on and industry practice: projects, case studies, industry domains, deployment, research readiness |
| O8 | Trustworthy and responsible AI: robustness, privacy, explainability, uncertainty, ethics |

## Findings before the edits

The table below is the 22 October 2026 reading. The current matrix is in `specs/coherence-objectives-report.md`. Two cells moved. NLP O2 is 2 because Model 1.6 proves an interpolated Kneser-Ney bigram. Refresher Neural Nets O7 is 2 because section 2.3 is an in-page NumPy loop. LLM chapter 4 now teaches prompting, in-context learning, LoRA, and logit distillation. Distributed training is still absent. Attention is still undefined for students who take only Deep Learning (P2).

Each cell gives the maximum depth on that path: 0 absent, 1 mention, 2 taught but partial, 3 core supplier. Depth is judged on what the pages deliver, not on what they announce.

| Objective | Mandatory path | Graph × LLM route | AI systems route |
|---|---|---|---|
| O1 | 3 (ML, DL, RL) | 3 | 3 |
| O2 | 2, partial: diffusion and flows never derived for DL P1 students, yet assumed by Graph ML 9.5 and Geometric Data | 3 | 2 |
| O3 | 3, with holes: no LoRA/PEFT, no prompting / in-context learning, self-attention undefined for DL P2 students | 3 | 3 |
| O4 | 3 (Graph ML) | 3 | 3 |
| O5 | **2, weak**: one prose chapter (Graph ML ch. 10); relation extraction never taught; LLM 7.4 is one bullet | 2 | 2 |
| O6 | **1 for the generative part** (LLM 8.2 is four bullets); 2 only through 3D shape analysis | 3 | 3 |
| O7 | 3 through courses, but the 58 ECTS of project vehicles (internships, transverse project, ethics seminar) were framing pages without subjects | 3 | 3 |
| O8 | **2, narrow** (LLM ch. 9 only); fairness, privacy and explainability at most 1; the 6-ECTS ethics seminar page was empty | 3 | 3 |

Main structural problems:

- **“Deep Learning once, in P1 or P2” leaves holes.** The DL P2 page still does not define self-attention. Graph ML, NLP and RL now point P2-route students at Deep Learning (P1) chapter 6 as reading. A transformer block on the P2 page is backlog.
- **Retrieval is used before it is taught.** Basic RAG is used in Year 1 P2. The full treatment is LLM chapter 7. Graph ML chapter 10 has a short recall. A worked Year 1 chapter is backlog.
- **Prompting and in-context learning** are LLM section 4.0. LoRA is Definition 4.3 on that page.
- **Concepts without a mandatory home.** Group fairness, TreeSHAP, differential privacy and model comparison are still not taught on the mandatory path. LoRA now has a section on the LLM page.
- **Course order.** Control in Generative AI (Year 2 P1) depends on Graph Generative Models (Year 2 P2).
- **Year 2 prerequisites.** Year 2 pages name prerequisites that their own route excludes.
- **Pointers.** About 45 pointers lead to the wrong chapter or to content that does not exist.
- **Repeated derivations.** About fourteen derivations are taught in full in three or more pages at the same depth, for example the VAE/GAN chapters and the Bradley–Terry / DPO derivation.
- **Notation.** Ten notation contradictions, including the sign of the mean curvature, the PageRank α, the classifier-free guidance weight and the orientation of discrete diffusion.
- **Errors.** All eleven high-severity errors were confirmed, for example a reversed MALA acceptance ratio, an over-squashing bound stated with the wrong eigenvalue, and a FLOP count off by orders of magnitude.

## Decisions (October plan, not applied as chapter rewrites)

The table is the plan from 22 October 2026. Large rows are backlog. Local fixes that did land are marked applied in `specs/coherence-objectives-report.md`.

| Gap | Fix |
|---|---|
| O5 Graph × LLM | Teach the chain explicitly: NLP gets a relation-extraction section; Graph ML ch. 10 gets a worked GraphRAG (extraction schema, entity resolution, community detection, local and global search, evaluation protocol, a named final-lab corpus and baselines); LLM 7.4 gets knowledge-graph retrieval and a specified final lab; Advanced GNN and Advanced Topics deepen the route. |
| O6 multimodal | LLM gets a worked vision-language section (CLIP objective, projector alignment, visual instruction tuning; self-study); DL P1 gets the ViT; Geometric Data gets worked 3D + language bridges. |
| O8 trustworthy AI | ML gets group-fairness metrics in the evaluation pipeline and TreeSHAP; LLM gets privacy and bias (self-study); the ethics seminar page gets cases, a regulation primer and a memo deliverable. |
| O2 generative theory | DL P1 gets a diffusion and flow box (self-study); DL P2 gets the sampler; Graph ML gets the D3PM loss; Multimodal and Speech connect flows to flow matching. |
| O3 LLM chain | LLM gets prompting / in-context learning and PEFT + distillation; NLP gets a transformer box and a minimal RAG; DL P2 gets “From MLP to transformer block”. |
| O7 project vehicles | Transverse project: subject bank, calendar, rubric, trust work package. Research internship: report template. Final internship: module map. Team-project boxes in Graph ML, RL and NLP. End-of-year projects page (`projects/`). |
| Prerequisites | Review boxes where a concept is assumed but taught elsewhere on an optional path; wrong prerequisite links fixed; Year 2 P2 siblings relabelled as co-requisites. |
| Redundancy | One canonical page per repeated derivation; the others keep a short recall with a link. The time freed pays for the O5/O6/O8 additions. |
| Notation | A site-wide convention page (`notation/`). Pages that conflict align, or say at the start of their notation block that they deviate. |

## End-of-year projects

Ten integrative projects, in `projects/` (`specs/projects-and-assessment.md`):

| Id | Project | Route | Objectives |
|---|---|---|---|
| Y1.1 | GraphRAG with a learned retrieval router | Graph × LLM | O5 O3 O4 |
| Y1.2 | Demand-aware fleet dispatch with natural-language bookings (logistics) | AI systems | O7 O4 O1 |
| Y1.3 | Text, knowledge graph and bandits for cold-start news recommendation | both | O7 O4 O5 |
| Y1.4 | Molecules from words: text–graph alignment | Graph × LLM | O2 O5 O6 |
| Y1.5 | Scene-graph question answering under perception noise | AI systems | O6 O5 O7 |
| Y2.1 | Semi-structured biomedical QA with calibrated abstention (healthcare) | Graph × LLM | O5 O3 O8 |
| Y2.2 | Text-to-3D-molecule copilot with controlled generation | Graph × LLM | O2 O6 O8 |
| Y2.3 | Voice-first retrieval and recommendation of 3D products | AI systems | O6 O7 O3 |
| Y2.4 | Natural-language dispatcher over exact and learned routing | AI systems | O7 O4 O3 |
| Y2.5 | Fraud alerts under attack and drift (finance) | both | O8 O4 O7 |

Year 1 projects map onto three official Period 2 vehicles in one team repository: the Graph ML team project, the RL course project (50 %) and the NLP capstone. Year 2 projects are sized for the official Transverse project (8 ECTS).

## Proof

- Current scores, applied local fixes, and backlog: `specs/coherence-objectives-report.md`.
- `python3 tools/check_coherence_map.py` reads that report. It fails if a science course is missing or a score is outside 0 to 3. It checks that NLP O2 is 2 and that Refresher Neural Nets O7 is 2.
- `python3 tools/check_gates.py`, `python3 tools/check_progression.py`, and `python3 tools/check_airiness.py` still gate the pages. They do not score objectives.
- The 194 planned chapter edits were not applied and were not independently reviewed.
