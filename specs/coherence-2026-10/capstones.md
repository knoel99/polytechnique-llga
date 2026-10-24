# End-of-year projects (capstones) for the LLGA master

Lens: end-of-year projects. Sources: the per-course records (integration hooks, project ideas, existing project material, thin areas), the course pages `courses/<slug>/index.qmd` (session plans and chapters checked for every chapter cited below), the transverse-project and internship pages, and the home page (curriculum tree, the two routes, "After the master"). Date: 2026-10-22.

These are independent proposals, written so that they can become the projects page of the notes. They are not official subjects: the programme publishes no Year 1 project, and the transverse-project page says "brief and grading = official project setup". Each brief therefore says which official vehicle it can serve and which course chapters it relies on.

## 1. What these projects are for

**Year 1 (end of Period 2), 5 projects.** Every Year 1 project combines the three mandatory Period 2 courses (Reinforcement Learning, Graph ML, Text Mining & NLP) with the Period 1 foundations (Machine Learning, one Deep Learning, the refreshers) and at least one elective. The programme already has three empty or half-specified project slots in Period 2:

- Graph ML, session 9: "lab: Example 8.1 (start the team project)". No subject is given, and the course description says "quizzes and team projects".
- Reinforcement Learning: the course description announces "course project (50%)". The page does not specify the subject; Ex. 16 ("Agent project") is the closest material.
- NLP: Ex. 14 is a capstone pipeline that exports triples "to the Graph ML mini-GraphRAG".

The proposal is **one team repository, three graded components**: the graph work package is graded as the Graph ML team project, the RL work package as the RL course project, and the NLP work package as the NLP capstone. Timeline: six weeks, from Graph ML session 9 (W1) to about two weeks after the end of Period 2 (which runs 4 January to 19 March 2027 according to the RL and NLP sheets), before the 16-week research internship. The exact weeks depend on the official timetable. Assumed workload: 60-80 h per student in a group of 3-5, 45-60 h for a solo variant.

**Year 2 (Transverse project, 8 ECTS), 5 projects.** Every Year 2 project combines the two Year 2 core courses (Large Language Models, Analysis and Deep Learning on Geometric Data) with at least two Period 2 advanced themes and Year 1 foundations. 8 ECTS is about 200-240 h of student work at the usual 25-30 h per ECTS (the programme publishes no split). Proposed shape: a charter week (W0) at the end of Year 2 Period 1, a six-week build phase (W1-W6) in Period 2, then the defence. Every Year 2 project feeds the ethics seminar (one case memo) and the final internship (one open question).

**Objective ids** (from the official description quoted on the home page):

| Id | Objective |
|---|---|
| O1 | ML & DL foundations: statistical learning, optimisation, neural architectures and training |
| O2 | Generative modelling theory: probabilistic models, VAEs, GANs, flows, diffusion, autoregressive models |
| O3 | Large Language Models: Transformers, pre-training, fine-tuning and alignment, inference, retrieval and agents, evaluation |
| O4 | Graph-structured data: GNNs for networks, molecules, logistics |
| O5 | Graph x LLM: knowledge graphs with LLMs, GraphRAG, neuro-symbolic reasoning (the distinctive emphasis) |
| O6 | Multimodal generative AI: vision, language, speech, 3D / geometric data |
| O7 | Hands-on and industry practice: projects, case studies, industry domains (healthcare, finance, recommendation, logistics), deployment, research readiness |
| O8 | Trustworthy and responsible AI: robustness, privacy, explainability, uncertainty, ethics |

The design deliberately pushes the objectives that the objectives lens found weakest on the mandatory path: O5 (no course reaches depth 3), O6 (depth 1 on the mandatory path for the generative part), O8 (narrow on the mandatory path) and O7 (the project vehicles are empty pages, and logistics appears in no course).

## 2. Overview

| Id | Title | Route | Industry case | Core objectives | Mandatory courses used | Electives / advanced topics used |
|---|---|---|---|---|---|---|
| Y1.1 | From paragraphs to a knowledge graph to answers: GraphRAG with a learned retrieval router | Graph x LLM | enterprise knowledge (open-domain proxy) | O5, O3, O4 | ML, DL, RL, Graph ML, NLP | TDA or OT or Multimodal GenAI |
| Y1.2 | Demand-aware fleet dispatch with natural-language bookings | AI systems | logistics (urban fleet) | O7, O4, O1 | ML, RL, Graph ML, NLP | Signal Processing, DL (P2 variant) |
| Y1.3 | Text, knowledge graph and bandits for cold-start news recommendation | both | recommendation | O7, O4, O5 | ML, RL, Graph ML, NLP | Emerging ML (gllm) or DL P2 (sys) or OT / Optimization for AI |
| Y1.4 | Molecules from words: text-graph alignment as retriever, guide and reward | Graph x LLM | molecules / healthcare | O2, O5, O6 | ML, DL, RL, Graph ML, NLP | Multimodal GenAI (optional OT) |
| Y1.5 | Seeing, then reasoning: scene-graph question answering under perception noise | AI systems | visual inspection / robotics | O6, O5, O7 | ML, RL, Graph ML, NLP | Image Analysis & CV, DL (P2 variant) |
| Y2.1 | Semi-structured biomedical QA: GraphRAG, GNN retriever or graph tokens, with calibrated abstention | Graph x LLM | healthcare | O5, O3, O8 | LLMs, Geometric Data | Advanced Topics in LLMs, Advanced GNN, Privacy & UQ, ESP of LLMs, MLOps |
| Y2.2 | A text-to-3D-molecule copilot with controlled generation and calibrated property intervals | Graph x LLM | molecules / pharma | O2, O6, O8 | LLMs, Geometric Data | Graph Generative Models, Control in GenAI, Privacy & UQ, Advanced GNN, ESP of LLMs |
| Y2.3 | Speak, see, shop: a voice-first assistant that retrieves and recommends 3D products | AI systems | recommendation / e-commerce | O6, O7, O3 | LLMs, Geometric Data | Speech Technology, MLOps, Security & Robustness, ESP of LLMs |
| Y2.4 | The natural-language dispatcher: an LLM agent over exact and learned routing with built-in symmetry | AI systems (Graph x LLM option) | logistics (last mile) | O7, O4, O3 | LLMs, Geometric Data | MLOps, Control in GenAI, Advanced GNN, Advanced Topics in LLMs, Security, Boosting/tabular |
| Y2.5 | Fraud alerts you can defend: temporal GNN, spectral descriptors and grounded LLM narratives under attack | both | finance | O8, O4, O7 | LLMs, Geometric Data (light) | Advanced GNN, Security & Robustness, Privacy & UQ, Boosting/tabular, MLOps, ESP of LLMs |

Route rule respected: Year 1 has two Graph x LLM projects (Y1.1, Y1.4), two AI systems projects (Y1.2, Y1.5) and one for both (Y1.3); Year 2 has two Graph x LLM (Y2.1, Y2.2), two AI systems (Y2.3, Y2.4) and one for both (Y2.5). Industry cases cover the five domains named in the brief: healthcare (Y1.4, Y2.1), molecules (Y1.4, Y2.2), recommendation (Y1.3, Y2.3), logistics (Y1.2, Y2.4) and finance (Y2.5).

**Continuation paths** (Year 1 project, then research internship, then Year 2 project), following the "From M1 question to M2 capstone" idea of the research-internship record:

| Year 1 | Internship topic family it prepares | Year 2 |
|---|---|---|
| Y1.1 KG-QA router | relation extraction, KG quality, retrieval evaluation | Y2.1 |
| Y1.2 fleet dispatch | spatio-temporal forecasting, RL for operations | Y2.4 |
| Y1.3 news recommendation | recommender systems, bandits, privacy or fairness | Y2.3, Y2.5 |
| Y1.4 molecules from words | molecular ML, generative chemistry | Y2.2 |
| Y1.5 scene-graph QA | perception, neuro-symbolic reasoning, efficient inference | Y2.3 |

## 3. Common rules (all projects)

### 3.1 Charter (Year 1: end of W1; Year 2: W0)

A two-page charter, reviewed by a tutor, then re-read against the final report:

1. **One question, one metric, one baseline per work package**, before any stacking of models (rule of the research-internship page, `m1p3-research-internship` #travailler).
2. **"Done" in usage terms** (`m2-projet-transverse` #travailler): an acceptance test stated as what a user can do, not only as a model metric. Mandatory in Year 2, encouraged in Year 1.
3. **Module map**: for each work package, the 2-3 course chapters it applies (`m2-internship` #travailler). This is the "path evidence" the internship report will reuse.
4. **Compute and cost budget**: FLOPs, GPU-hours and euros, with the calculators of `m1p2-deep-learning-p2` ch1 and ch6 (Ex. 7) or `m1p1-emerging-ml` ch7, and in Year 2 the euros-per-million-tokens model of `m2-mlops-llm-engineering` ch4.
5. **Data licence and consent check**: licence of each dataset (several used below are non-commercial), and consent forms whenever people are recorded or rated outputs.
6. **Which courses the team actually took.** Several Year 2 courses are "slot TBC" and the Year 2 Period 2 list is unpublished. Each brief below names a fallback chapter for every slot-TBC course it uses.

### 3.2 Shared evaluation kit

Every team builds (or reuses) the same evaluation kit. The pieces already exist in the notes but are scattered:

- leak-free pipelines and the "golden rule" of `m1p1-machine-learning` ch4 (4.2 nested CV, 4.3 leaks, 4.5 calibration, 4.6 reference pipeline);
- leakage-free graph splits and temporal splits: `m1p2-graph-ml` ch8 Example 8.1 and the causality rule of ch5 (5.6-5.8);
- paired comparisons with confidence intervals: the "Graph x LLM transfer check" of `m1p1-refresher-statistics` (exit checkpoint: paired gains, cluster bootstrap by source group, shuffled-edge control) and ch6 (tests, 6.6 multiple testing);
- the winner's curse when picking the best of many runs (`m1p1-refresher-statistics` Example 3.6): final numbers come from a test set touched once;
- seeds and budgets: at least 3 seeds per trained model in Year 1, at least 5 in Year 2 (`m1p2-advanced-deep-learning` Def. 1.1, `m2-advanced-gnn` ch1 protocol, `m2-boosting-foundation-tabular` ch9);
- in Year 2, significance-aware CI gates (`m2-mlops-llm-engineering` ch2, Def. 2.1, Ex. 6).

### 3.3 Reproducibility and logs

- Repository template of `m1p1-refresher-cs` ch3 (pytest, lockfile, Dockerfile, logging) and the training checks of `m1p1-deep-learning` ch8 (seeding, overfit one batch, LR range test).
- A weekly log "hypothesis, trial, result, next question" (`m1p3-research-internship` #travailler) and a decision and technical-debt log (`m2-projet-transverse` #travailler).
- Year 2 adds artefact lineage for data, prompts, indexes, graph snapshots and adapters (`m2-mlops-llm-engineering` ch1, DVC + MLflow).

### 3.4 Trust work package

- **Year 1**: one "failure modes and limits" section per report (leakage, bias, misuse, privacy of the data used), with at least one measured failure mode.
- **Year 2**: a mandatory trust work package: a threat model in the format of `m2-security-robustness` Def. 1.1; an attack suite scored by attack success rate (ASR) per family, following the protocol of `m2-explainability-security-privacy-llms` Ex. 11 (30 attacks, 10 of them adaptive; 20 and 5 for a solo variant); one uncertainty or privacy guarantee with a "guarantee sheet" (`m2-privacy-uncertainty` Ex. 11 format); successful attacks turned into CI regression tests.
- **Year 2 red-team swap (W4)**: each team attacks another team's system for one week with a fixed budget, as in the "game day" of `m2-mlops-llm-engineering` Ex. 12. The defending team reports detection time and fixes.

### 3.5 Deliverables

| | Year 1 | Year 2 |
|---|---|---|
| Code | repository runnable with one command; tagged release | the same, plus a deployed service or demo and lineage (DVC/MLflow) |
| Report | 8-10 pages: question, method per work package, evaluation with CIs, ablations, failure analysis | 6-8-page workshop-style paper in English plus appendices, and a one-page French executive summary (the `m1-langues` hook) |
| Defence | 15 min + 10 min questions | 20 min including a live demo + 10 min questions |
| Documentation | datasheet for any dataset the team built | model card, datasheet, guarantee sheet, decision log |
| Ethics | failure-modes section | facts / values / options memo (`m2-ethical-issues-ai` #travailler), reusable in the seminar |
| Next step | one-page open question for the research internship | one-page open question for the final internship (or a PhD/CIFRE proposal) |

Optional for both years: a "metrics beyond accuracy" paragraph (cost of error in euros, latency, adoption) using the `m1p1-strategy-marketing` hook, and a corpus or KG bias audit in the spirit of the `m1-humanites` hook.

### 3.6 Common rubrics

Each project section below gives its own weighted rubric, adapted from these templates.

**Year 1 template (100 points).** Framing and baselines 15 · RL work package 10-15 · Graph work package 10-15 · NLP work package 10-15 · Elective component 5-10 · Evaluation rigour (splits, seeds, CIs, ablations) 20 · Analysis and honesty (failure analysis, negative results) 10 · Reproducibility 5-10 · Communication 5. When the project serves three courses, each course grades its work package on its own row and shares the other rows.

**Year 2 template (100 points).** Usage-based acceptance tests 15 · Technical depth and correctness of the core (LLMs, Geometric Data) 20 · Advanced work packages 10-15 · Evaluation and statistics 15 · Trust work package and red-team swap 15 · Engineering and operations (serving, SLOs, cost, CI) 10 · Reproducibility and decision log 5 · Communication and ethics memo 5-10.

---

## 4. Year 1 projects (end of Period 2)

Common timing note. Several chapters the projects need are taught at the very end of Period 2: Graph ML ch9 (sessions 10-11) and ch10 (session 12), RL ch6 (sessions 9-11) and ch7 (session 12), NLP ch8 (sessions 10-12). The milestones below put work that needs these chapters in W3-W5, and each brief lists what to read ahead. The Graph ML page itself tells students to read ch10 alongside the NLP course.

### Y1.1 From paragraphs to a knowledge graph to answers: GraphRAG with a learned retrieval router

**Route** Graph x LLM. **Domain** enterprise knowledge, with open-domain multi-hop QA as a measurable proxy (variant: a regulatory or corporate corpus).

**Pitch.** Build the mini-GraphRAG of the Graph ML final lab properly. Extract a knowledge graph from the paragraphs of a multi-hop QA benchmark with NER and relation extraction, scored against gold triples. Complete it with knowledge-graph completion. Answer questions in four ways (lexical, dense, graph traversal, pseudo-code prompting over a subgraph). Then let a contextual bandit learn, per question, which retrieval mode is worth its token cost.

**Research question.** On multi-hop questions, when does an LLM-built knowledge graph beat lexical and dense retrieval, at what token cost, and can a cost-aware contextual bandit learn a routing policy that dominates every fixed retrieval mode on the accuracy-cost plane?

**Courses and chapters**

- `m1p2-nlp-text-mining`: ch1 (normalisation, subword tokenisation); ch2 and 2.1 (BM25, inverted index, MAP/nDCG/MRR of Def. 2.7); ch6 (NER, BIO decoding, entity-level F1); ch7 (Protocol 7.1 fine-tuning, Sentence-BERT); Ex. 14 as the ingestion skeleton.
- `m1p2-graph-ml`: ch0 (modularity, Louvain/Leiden); ch3 (node2vec, Example 3.4) for structural features of seed entities; ch6 (TransE, R-GCN + DistMult, link-prediction protocol); ch8 Example 8.1 (leakage-free split for KG completion); ch10 (10.1 pipeline, 10.2 serialisation and pseudo-code prompting, 10.3 hygiene, final lab).
- `m1p2-reinforcement-learning`: ch4 (UCB1, Alg. 4.4 Thompson sampling, Alg. 4.5 LinUCB, regret); ch7 (Def. 7.1 POMDP framing, ReAct tool loop, guiding lab and Ex. 16 with cost metrics).
- `m1p1-machine-learning` ch4 (metrics, calibration 4.5, reference pipeline 4.6); `m1p1-refresher-statistics` exit checkpoint (paired gains, cluster bootstrap, shuffled-edge control) and ch6.
- `m1p1-deep-learning` ch6 (6.4 transformer block) and ch7 (7.3 LoRALinear) for the supervised relation classifier. AI-systems students use `m1p2-deep-learning-p2` ch5 for the serving budget instead.
- Elective (one): `m1p1-tda` ch2 (Def. 2.9 ToMATo), ch6 (Mapper) and ch7 (bootstrap stability), to compare density-persistence clusters of entity embeddings with Leiden communities for the community summaries; or `m1p2-optimal-transport` ch5 (FGW, Example 5.5) to align the entity sets of two extraction runs; or `m1p2-multimodal-genai` ch5 (symmetric InfoNCE) to fine-tune the dense retriever on question-paragraph pairs.

**Objectives** O5 (core), O3, O4, O1, O7, O8 (citation faithfulness; the re-identification note of Graph ML 10.3).

**Data and resources**

- 2WikiMultiHopQA (Ho et al., COLING 2020): multi-hop questions with gold supporting facts and evidence triples. The gold triples score the relation extractor; the four question types (comparison, inference, compositional, bridge comparison) give natural strata.
- HotpotQA, distractor setting (Yang et al., EMNLP 2018) as a transfer check; MuSiQue (Trivedi et al., TACL 2022) as an optional harder set.
- Tools: spaCy, sentence-transformers, rank_bm25, NetworkX, python-igraph + leidenalg, PyTorch Geometric (`RGCNConv`, `torch_geometric.nn.kge` TransE/DistMult), the open-source `microsoft/graphrag` implementation (Edge et al., 2024) as a reference, a 7-8B open-weight instruct model (for example Qwen2.5-7B-Instruct or Llama-3.1-8B-Instruct, or a newer model of the same size) served with vLLM or llama.cpp; GUDHI (TDA option), POT (OT option).

**Milestones (6 weeks; W1 = Graph ML session 9)**

| Week | Milestone | Exit evidence |
|---|---|---|
| W1 | Charter. Fix the corpus: about 1,000 2Wiki dev questions and their paragraphs, split 600 router-training / 400 test, stratified by question type. BM25 and dense baselines. | EM/F1, supporting-paragraph recall@k, tokens and latency per question logged |
| W2 | Extraction: NER (spaCy vs fine-tuned encoder) and relation extraction (few-shot LLM with a JSON schema vs a fine-tuned entity-marker classifier trained on 2Wiki training triples). Entity-resolution rule (string + embedding threshold). KG v1. | triple micro-F1 against gold; entity-resolution precision on 100 checked pairs |
| W3 | Graph retrieval: k-hop local search from seed entities, community summaries (Leiden, or ToMATo for the TDA option), pseudo-code prompting for path questions. KG completion with a leakage-free split, giving KG v2. | precision of added edges against gold triples; answer EM per mode |
| W4 | ReAct agent over the four tools. LinUCB and Thompson routers: context = question-type prediction, number of linked entities, seed-entity degree, BM25 score margin; reward = correct - lambda * tokens/1000. Mid-point review. | regret curves on the training questions; router frozen before test |
| W5 | Evaluation on the 400 test questions: accuracy-cost plane for the four fixed modes, the router and an oracle router; paired bootstrap by question type; shuffled-edge control; ablations (no KG completion, no communities, LLM vs supervised relation extraction); 30 failures analysed. | figure and tables with CIs |
| W6 | Report, defence, repository freeze, open question for the internship. | tagged release |

Read ahead: Graph ML 10.1-10.2 by W2 (taught in session 12); RL ch7 by W4 (session 12).

**Deliverables** Repository (ingestion, KG, retrieval, router; one command); KG export with source passage per triple; evaluation notebook; report; defence; datasheet of the extracted KG.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Framing and baselines | 10 | BM25 and dense baselines tuned; question types defined before results |
| NLP: NER, relation extraction, entity resolution | 15 | triple F1 against gold; LLM vs supervised extractor compared at equal data |
| Graph: KG, completion, graph retrieval | 15 | leakage-free completion split; added-edge precision reported; graph gains per question type |
| RL: agent and router | 15 | router beats the best fixed mode or the report explains why not; comparison to the oracle router |
| Elective component | 5 | one measured comparison (ToMATo vs Leiden, FGW alignment, or InfoNCE fine-tuning) |
| Evaluation rigour | 20 | paired CIs by question type; shuffled-edge control; closed-book control for memorisation |
| Analysis, reproducibility, communication | 20 | failure taxonomy; one-command rerun; clear accuracy-cost figure |

**Solo variant.** 300 questions and two question types (bridge, comparison); LLM-only triple extraction (still scored against gold); three modes (BM25, dense, 2-hop graph); Thompson sampling over three arms; the elective as one ablation.

**Group variant (4-5).** WP-NLP (NER, relation extraction, entity resolution); WP-Graph (KG, completion, communities, graph retrieval); WP-RL (agent, router, cost model); WP-Eval (harness, statistics, error analysis); optional WP-Elective.

**Risks and mitigations**

- Relation extraction is never taught: NLP ch6 names it ("entity + relation extraction", the capstone exports "NER + relations") but covers only NER. Mitigation: the 2Wiki gold triples give a supervised signal and a scorer; the team documents its method in one page.
- The Graph ML final lab names no corpus, LLM or baseline, and ch10 is prose only. This brief supplies them.
- LLM extraction cost and non-determinism: cache all calls, temperature 0, log prompts; cap the corpus.
- Memorisation: Wikipedia facts may already be in the LLM. Add a closed-book baseline as a control.
- Small test set: use paired tests; do not over-read differences inside the CI.

### Y1.2 Demand-aware fleet dispatch with natural-language bookings

**Route** AI systems. **Domain** logistics (urban fleet operations).

**Pitch.** A city fleet must decide where idle vehicles wait. Forecast zone-level demand from public trip records with signal-processing models and a spatio-temporal GNN, learn a repositioning policy with RL in a simulator built from the same records, and accept advance bookings written in natural language. Then measure how forecast errors and parsing errors propagate to the service rate, within a per-decision latency budget.

**Research question.** How much of the gain of a learned repositioning policy over greedy dispatch survives when the policy is fed real forecasts (seasonal and AR models, gradient boosting, spatio-temporal GNN) instead of oracle demand, and how much service does a natural-language booking parser lose relative to perfectly structured bookings?

**Courses and chapters**

- `m1p1-signal-processing`: ch5 (digital filtering), ch6 (time-frequency analysis), ch7 (periodogram, Welch, AR models and Yule-Walker: identify daily and weekly periodicities, AR baselines), ch8 (graph signal processing bridge: graph Fourier transform, polynomial filters).
- `m1p2-graph-ml`: ch4 (spectral filters, ChebNet on the zone graph), ch5 (5.6-5.8 temporal graphs and the causality rule), ch8 Example 8.1 (time-respecting split).
- `m1p2-reinforcement-learning`: ch1 (MDP formulation of repositioning), ch3 (Q-learning as a tabular sanity check), ch5 (REINFORCE, actor-critic, PPO of Theorem 5.5), ch6 (6.1 DQN; Def. 6.5 constrained MDP for a cap on empty kilometres; 6.4 MPC as a model-based baseline).
- `m1p2-nlp-text-mining`: ch1 (normalising place names), ch6 (sequence labelling, CRF, BIO, entity-level F1), ch7 (Protocol 7.1 fine-tuning of a small encoder).
- `m1p1-machine-learning` ch4 (temporal validation, leakage) and ch6 (gradient boosting baseline); `m1p1-refresher-cs` ch7 (Dijkstra and A* on the road or zone graph) and ch3 (repository template).
- Elective: `m1p2-deep-learning-p2` ch1 (counting FLOPs and memory), ch5 (efficient inference: int8, batching), Example 5.4 (the four-column protocol: quality, p50/p99 latency, throughput, energy).

**Objectives** O7 (core: logistics, real-time constraints), O4, O1, O3 (light: slot filling with an encoder or an LLM), O8 (light: robustness to parse errors; service disparity across boroughs).

**Data and resources**

- NYC TLC Trip Record Data (New York City Taxi & Limousine Commission; monthly Parquet files for yellow taxis and high-volume for-hire vehicles) and the TLC Taxi Zones shapefile (263 zones), from which the zone adjacency graph is built.
- MultiWOZ 2.2 (Zang et al., 2020), taxi domain (slots departure, destination, leave-at, arrive-by), for slot filling.
- Optional: METR-LA and PEMS-BAY (Li et al., ICLR 2018, DCRNN) as standard benchmarks for the spatio-temporal forecaster; OSMnx (Boeing, 2017) for road-network travel times.
- Tools: DuckDB or pandas, `scipy.signal`, statsmodels, LightGBM, PyTorch Geometric Temporal (Rozemberczki et al., CIKM 2021), Gymnasium, sklearn-crfsuite, Hugging Face transformers, OR-Tools (assignment baseline), ONNX Runtime.

**Milestones (6 weeks)**

| Week | Milestone | Exit evidence |
|---|---|---|
| W1 | Charter. Data slice (for example Manhattan zones, three months: two for training, one for test). Zone graph. Simulator v0: 15-minute steps, requests replayed from the records, zone-to-zone travel times from historical medians by hour. Baselines: no repositioning, greedy towards forecast demand. | simulator reproduces historical served-trip counts within a stated tolerance |
| W2 | Forecasting: seasonal naive, AR(p) after Welch-identified periodicities, LightGBM with calendar features, spatio-temporal GNN (ChebNet or GCN + GRU). Temporal split. | MAE per zone and hour with CIs over test days |
| W3 | RL: tabular Q-learning on an aggregated state, then DQN or PPO with parameters shared across vehicles; Lagrangian constraint on empty kilometres (Def. 6.5); 3 seeds. | learning curves over seeds; constraint satisfaction |
| W4 | Booking parser: CRF vs fine-tuned small encoder vs few-shot LLM on MultiWOZ taxi; 150 New York bookings written by the team, mapped to zones with a gazetteer, as a transfer test; parsed bookings injected into the simulator. Mid-point review. | entity-level F1 on both sets |
| W5 | Decision-level evaluation: oracle vs each forecaster x each policy; parsing-error propagation; p50/p99 latency per dispatch decision on CPU; service rate by borough. | "forecast MAE vs service rate" figure; block bootstrap by day |
| W6 | Report and defence. | tagged release |

**Deliverables** Simulator package with tests; forecasting benchmark; policy checkpoints; parser with its team-built test set and datasheet; report; defence.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Framing, simulator validity | 15 | assumptions stated; validation against historical statistics; sensitivity to one key assumption |
| Signal and graph forecasting | 15 | periodicities identified, AR order justified, GNN compared under a temporal split |
| RL policy | 15 | sanity check (tabular) before deep RL; seeds; constraint handled explicitly |
| NLP parser | 10 | entity-level F1; transfer gap from Cambridge (MultiWOZ) to New York reported |
| Systems elective (DL P2) | 10 | latency measured per decision, compared with the counted FLOPs |
| Evaluation rigour | 20 | decision-level metrics with CIs; oracle forecasts as the upper bound; no future leakage |
| Analysis, reproducibility, communication | 15 | error propagation explained; one-command rerun |

**Solo variant.** Manhattan only; AR vs GNN forecasts; tabular Q-learning or DQN; CRF vs few-shot LLM on MultiWOZ only; DL P2 reduced to a timing table.

**Group variant (4).** WP-Forecast (Signal Processing + Graph ML); WP-Simulator+RL; WP-NLP; WP-Systems and evaluation (DL P2 budgets, latency, fairness across boroughs).

**Risks and mitigations**

- Simulator realism (no traffic dynamics, no driver behaviour): state the assumptions and test the sensitivity of the conclusions to them.
- RL instability: start tabular, then deep; fixed seeds; shared parameters across vehicles.
- RL ch7 has no multi-agent theory: treat vehicles as independent learners with shared parameters and say so.
- MultiWOZ is set in Cambridge (UK): report the transfer gap to the team's New York bookings instead of hiding it.
- AI-systems students take DL (P2 variant) in parallel: the latency work sits in W5.

### Y1.3 Text, knowledge graph and bandits for cold-start news recommendation

**Route** both (the elective changes with the route). **Domain** recommendation.

**Pitch.** News articles are cold by nature: they live for hours. Combine text encoders, the knowledge-graph entities attached to each article and a user-news click graph to score fresh items, then let a contextual bandit decide what to show. One elective adds privacy, serving efficiency or exposure fairness.

**Research question.** For items with no click history, do knowledge-graph entity signals and graph-propagated user representations improve click ranking over text-only encoders, and does a LinUCB or Thompson policy that uses these representations as context earn more clicks than epsilon-greedy and popularity in a simulator calibrated on held-out logs?

**Courses and chapters**

- `m1p2-nlp-text-mining`: ch2 (TF-IDF content baseline); ch4 (embeddings, SIF); ch7 (Sentence-BERT, Protocol 7.1); ch8.5 (content-based Def. 8.2, matrix factorisation and the hybrid q_i = W x_i of Model 8.3); ch8.3 (MinHash-LSH to merge near-duplicate stories); Ex. 13.
- `m1p2-graph-ml`: ch3 (node2vec on the entity co-occurrence graph); ch5 (GraphSAGE or GAT on the user-news bipartite graph); ch6 (link prediction, PinSage, TransE entity embeddings); ch7 (neighbour sampling); ch8 Example 8.1 (time-respecting split).
- `m1p2-reinforcement-learning`: ch4 (UCB1, Alg. 4.4 Thompson sampling, Alg. 4.5 LinUCB, regret); ch6.2 (offline RL caveats, used to frame off-policy evaluation).
- `m1p1-machine-learning` ch4 (AUC, calibration, leakage); `m1p1-refresher-statistics` ch8 (Beta-Bernoulli), Example 3.6 (winner's curse), ch6.6 (multiple testing).
- Elective, by route:
  - Graph x LLM: `m1p1-emerging-ml` ch3 (FedAvg over simulated user devices) and ch5 (DP-SGD on the user encoder, privacy accountant).
  - AI systems: `m1p2-deep-learning-p2` ch5 (two-tower serving, int8, batching) and ch1 (cost counting) under a latency SLO.
  - Neither route: `m1p2-optimal-transport` ch6 (exposure fairness across categories by OT post-processing) or `m1p2-optimization-ai` ch8 (exposure constraint by stochastic primal-dual).

**Objectives** O7 (core: recommendation), O4, O3, O5 (knowledge-graph entities x text), O1, O8 (privacy or fairness variant).

**Data and resources**

- MIND, Microsoft News Dataset (Wu et al., ACL 2020), MIND-small: impression logs with clicked and non-clicked candidates; news title, abstract and category; entities linked to Wikidata, with pre-trained TransE entity embeddings. Microsoft Research licence (non-commercial research use).
- Optional: Open Bandit Dataset and Open Bandit Pipeline (Saito et al., NeurIPS 2021 Datasets & Benchmarks; ZOZOTOWN, with a uniformly random logging policy) for an unbiased off-policy evaluation check. MovieLens-25M as a fallback.
- Tools: `recommenders-team/recommenders` (NRMS and NAML baselines for MIND), PyTorch Geometric (LightGCN, SAGEConv), sentence-transformers, obp; Flower and Opacus (Graph x LLM variant; FedNewsRec, Qi et al., Findings of EMNLP 2020, as the reference design); ONNX Runtime (AI systems variant); POT (OT variant).

**Milestones (6 weeks)**

| Week | Milestone | Exit evidence |
|---|---|---|
| W1 | Charter. MIND-small split by time (last day as test). Popularity, TF-IDF content and MF baselines. Cold-item subset defined (items unseen in training). | AUC, MRR, nDCG@5/10, overall and on cold items |
| W2 | Text towers: Sentence-BERT frozen vs fine-tuned; entity tower from the TransE embeddings; hybrid q_i = W x_i. | same metrics; cold-item gain per tower |
| W3 | Graph: user-news bipartite graph, LightGCN or GraphSAGE; inductive scoring of cold items through their text and entity features; node2vec on entity co-occurrence. | ablation table |
| W4 | Simulator: click model fitted on held-out days, with position bias. Bandits: epsilon-greedy, UCB1, Thompson, LinUCB with each tower's embedding as context. Mid-point review. | regret curves over 5 seeds |
| W5 | Elective experiment; paired bootstrap over impressions grouped by user; replay on logged impressions as a biased sanity check, with a discussion of its bias; optional OPE on the Open Bandit Dataset. | elective figure (epsilon-utility curve, latency SLO table or exposure-utility Pareto front) |
| W6 | Report and defence. | tagged release |

Read ahead: NLP 8.5 (session 11) by W1.

**Deliverables** Repository; ranking table (overall vs cold); bandit regret plots with CIs; elective result; report; defence.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Framing and baselines | 10 | popularity and MF baselines; cold items defined before modelling |
| NLP towers | 15 | fine-tuning protocol followed; cold-start gain isolated |
| Graph component | 15 | inductive treatment of cold items; time-respecting split |
| Bandits | 15 | context ablation; regret with CIs; simulator assumptions tested |
| Elective | 10 | one curve with a stated guarantee or SLO |
| Evaluation rigour | 20 | user-grouped bootstrap; replay bias discussed; test touched once |
| Analysis, reproducibility, communication | 15 | what the simulator can and cannot show is stated |

**Solo variant.** Text tower + entity tower + LinUCB; graph tower reduced to node2vec features; one elective experiment.

**Group variant (4).** WP-Text, WP-Graph, WP-Bandit and simulator, WP-Elective and evaluation.

**Risks and mitigations**

- Simulator bias (the policy is evaluated in a model of users the team built): also report results on the logged impressions, and state what each evaluation can show.
- MIND licence: keep the data out of the repository and cite the licence.
- Non-stationarity of news breaks the bandit assumptions of RL ch4: test a sliding-window variant.
- DP variant: utility may collapse at small epsilon; report the whole curve.

### Y1.4 Molecules from words: text-graph alignment as retriever, guide and reward

**Route** Graph x LLM. **Domain** molecules and healthcare (drug discovery).

**Pitch.** Learn a CLIP-style space shared by molecular graphs and their textual descriptions. Use it to retrieve molecules from text, then steer a molecule generator towards a description, either by guidance or by RL fine-tuning, and catch the generator when it learns to fool the critic.

**Research question.** Can one contrastive text-graph model serve both as retriever and as reward, and at equal sampling budget does RL fine-tuning (REINFORCE or PPO with a KL anchor to the prior) beat guidance and best-of-N reranking on fidelity, validity and diversity, or does it reward-hack the critic?

**Courses and chapters**

- `m1p2-graph-ml`: ch5 (GCN/GIN encoders); ch8 (8.2-8.4 EGNN, optional with RDKit conformers); ch9 (9.4 GraphRNN, 9.6 validity/uniqueness/novelty, MMD and FCD, 9.7 conditional generation); Ex. 15.
- `m1p2-nlp-text-mining`: ch1 (BPE vs atom-level tokenisation of SMILES/SELFIES); ch4 (evaluating embeddings); ch7 (fine-tuning a scientific encoder, Protocol 7.1).
- `m1p2-reinforcement-learning`: ch5 (5.1-5.2 REINFORCE with baseline; 5.3 PPO-clip, Theorem 5.5); ch6.5 (imitation pre-training as the prior); ch4.2 (MCTS over graph edits, optional).
- `m1p2-multimodal-genai` (elective): ch5 (symmetric InfoNCE); ch4 (classifier-free guidance); ch3 (diffusion, for an optional DiGress-lite); ch7 (evaluation, costs, ethics).
- `m1p1-deep-learning` ch5-ch6 (sequence models for the SELFIES language model), ch8 (training protocol), ch9 (VAE baseline); `m1p1-machine-learning` ch4 (scaffold split as a leakage control).
- Optional: `m1p2-optimal-transport` ch5 (FGW distance between generated and reference molecule sets).

**Objectives** O2 (core), O5 (graph x language), O6 (cross-modal alignment), O4, O1, O7 (molecules), O8 (reward hacking, dual use).

**Data and resources**

- ChEBI-20 (Edwards, Zhai & Ji, EMNLP 2021, Text2Mol): molecule-description pairs with standard splits.
- ZINC250k for pre-training the generator; MOSES (Polykovskiy et al., 2020) and GuacaMol (Brown et al., 2019) metrics; Therapeutics Data Commons oracles (QED, SA, logP).
- MolT5 checkpoints (Edwards et al., EMNLP 2022) as the text-to-molecule baseline; SciBERT (Beltagy et al., 2019) as the text encoder.
- Tools: RDKit, SELFIES (Krenn et al., 2020), PyTorch Geometric, Hugging Face transformers.

**Milestones (6 weeks)**

| Week | Milestone | Exit evidence |
|---|---|---|
| W1 | Charter. ChEBI-20 splits; RDKit featurisation; retrieval baseline (TF-IDF over training descriptions, then nearest training molecule); MolT5 numbers reproduced on a test subset. | validity, exact match, Morgan fingerprint similarity, FCD |
| W2 | Contrastive model: GIN graph encoder + SciBERT text encoder, symmetric InfoNCE; temperature and batch-size ablation. | MRR and Hits@1/10 for text-to-molecule retrieval |
| W3 | Generator: SELFIES language model pre-trained on ZINC250k (valid by construction); GraphRNN as a stretch goal. | unconditional MOSES metrics |
| W4 | Steering at equal budget: (a) best-of-N reranking by the critic; (b) guidance; (c) RL fine-tuning with reward = critic similarity + validity and property terms - beta * KL to the prior. Mid-point review. | KL, entropy and reward curves during RL |
| W5 | Evaluation by an independent critic (other seed, architecture and text encoder) and by RDKit checks for descriptions that state computable properties; diversity; scaffold-split generalisation; reward-hacking analysis (high training-critic score, low independent score). | fidelity-diversity curves per method; case gallery |
| W6 | Report and defence, with a one-page dual-use note. | tagged release |

Read ahead: Graph ML 9.4-9.7 (sessions 10-11) by W3.

**Deliverables** Repository; retrieval table; fidelity-diversity curves at equal sampling budget; reward-hacking gallery; report; defence; dual-use note.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Framing and baselines | 10 | MolT5 and retrieval baselines reproduced |
| Graph encoders and generation metrics | 15 | validity, uniqueness, novelty, FCD computed correctly |
| NLP: tokenisation and text encoder | 10 | tokenisation choice measured; fine-tuning protocol |
| RL steering | 15 | KL anchor and entropy tracked; equal-budget comparison with guidance |
| Multimodal elective | 10 | InfoNCE trained and ablated; guidance strength swept |
| Evaluation rigour | 25 | independent critic; scaffold split; seeds |
| Analysis, ethics, communication | 15 | reward hacking diagnosed; dual-use note |

**Solo variant.** Retrieval model + best-of-N + REINFORCE on the SELFIES language model (no diffusion), on a 2,000-description test subset.

**Group variant (4).** WP-Encoders, WP-Generator, WP-RL and guidance, WP-Evaluation and ethics.

**Risks and mitigations**

- Multimodal GenAI is a Choose-1 elective: an AI-systems student who took DL (P2 variant) has not seen InfoNCE or guidance. Mitigation: Multimodal ch5 (contrastive loss, about 2 h of self-study) is enough for the solo variant.
- RL collapse or reward hacking: KL anchor, entropy bonus, early stopping on the independent critic.
- ChEBI-20 descriptions are ontology-styled, so exact-match fidelity will be low: report fingerprint similarity and property checks as well.
- Dual use: no toxicity objective; restrict properties to benign targets; discuss in the report.

### Y1.5 Seeing, then reasoning: scene-graph question answering under perception noise

**Route** AI systems. **Domain** visual inspection and robotics (questions about objects and their spatial relations).

**Pitch.** Detect objects in rendered scenes, build a scene graph, parse the question, and answer it with three reasoners over the graph: a symbolic program executor, a question-conditioned GNN, and an RL agent that walks the graph. Then degrade perception step by step and measure which reasoner fails gracefully, and at what latency.

**Research question.** When the scene graph comes from an imperfect detector rather than ground truth, which reasoning layer (symbolic execution, GNN, or a REINFORCE-trained graph walker) loses least accuracy per unit of perception error, and which meets a per-question CPU latency budget?

**Courses and chapters**

- `m1p1-computer-vision`: ch9 (fine-tuning a detector, IoU/AP); ch5 (projective geometry: from image coordinates to left/right and front/behind relations); ch1 (camera model).
- `m1p2-graph-ml`: ch2 (permutation invariance, graph tasks); ch5 (GAT, R-GCN with relation types); ch10.2 (serialisation or pseudo-code prompting as an optional fourth reasoner).
- `m1p2-nlp-text-mining`: ch6 (sequence labelling for attribute and relation mentions); ch7 (fine-tuned small encoder or sequence-to-sequence model: question to program); ch1.
- `m1p2-reinforcement-learning`: ch5 (5.1-5.2 REINFORCE with a learned baseline); ch7 (Def. 7.1: the walker observes only its neighbourhood, a POMDP); ch3 (n-step returns).
- `m1p2-deep-learning-p2` (elective): ch1 (FLOPs), ch5 (efficient inference, int8), Example 5.4 (four-column protocol), 7.1 (robustness).
- `m1p1-machine-learning` ch4; `m1p1-refresher-cs` ch7 (BFS-based program executor) and ch3.

**Objectives** O6 (core: vision + language), O5 (neuro-symbolic reasoning over a graph), O4, O1, O7 (latency budget; inspection use case), O3 (light).

**Data and resources**

- CLEVR (Johnson et al., CVPR 2017): rendered scenes with full scene annotations (object attributes, 3D and pixel coordinates, pairwise spatial relations) and a functional program for each question.
- CLEVR-Humans (Johnson et al., ICCV 2017): human-written questions on CLEVR images, for language transfer.
- GQA (Hudson & Manning, CVPR 2019): real images with Visual Genome scene graphs, as a stretch goal.
- Tools: Ultralytics YOLO (detector with attribute heads), PyTorch Geometric, Hugging Face transformers, ONNX Runtime; NS-VQA (Yi et al., NeurIPS 2018) as the reference for program execution and MINERVA (Das et al., ICLR 2018) as the reference for RL path walking.

**Milestones (6 weeks)**

| Week | Milestone | Exit evidence |
|---|---|---|
| W1 | Charter. CLEVR subset (for example 10k training images, 2k test images). Scene graphs from the annotations; symbolic executor on gold graphs (upper bound); question-to-program parser baseline. | accuracy per question family on gold graphs |
| W2 | Perception: detector + attribute classifier, with boxes derived from the projected coordinates; predicted scene graphs. | AP, attribute accuracy, relation accuracy |
| W3 | Reasoners: (i) parser + executor; (ii) question-conditioned GAT answer classifier; (iii) RL walker (start at an object named in the question; actions = follow a relation edge or answer an attribute; REINFORCE with baseline; 3 seeds). | accuracy on gold graphs per reasoner |
| W4 | Noise study: controlled corruption of gold graphs (drop objects with probability p, flip attributes with probability q, swap relations with probability r), plus real predicted graphs. Mid-point review. | accuracy-noise curves per reasoner and per question family |
| W5 | Systems: ONNX export, int8, p50/p99 per question on CPU, energy if measurable; CLEVR-Humans transfer; GQA stretch. | four-column table |
| W6 | Report and defence. | tagged release |

**Deliverables** Repository; accuracy-noise curves; latency table; report; defence.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Framing and gold-graph upper bound | 10 | upper bound reported per question family |
| Vision (perception to scene graph) | 15 | AP and attribute accuracy; relation errors analysed |
| NLP (question to program) | 10 | CLEVR-Humans transfer measured |
| Graph reasoner | 10 | relation types used; compared at equal training data |
| RL walker | 15 | curriculum or baseline justified; seeds |
| Systems elective | 10 | latency measured, not estimated; int8 effect on accuracy |
| Evaluation rigour | 15 | explicit noise model; per-family breakdown; CIs |
| Analysis, reproducibility, communication | 15 | which reasoner degrades gracefully, and why |

**Solo variant.** Gold and synthetically corrupted graphs only (a pretrained detector or no perception step); two reasoners (executor and RL walker); CLEVR only.

**Group variant (4).** WP-Perception (CV), WP-Language (NLP), WP-Reasoners (Graph ML + RL), WP-Systems and evaluation (DL P2).

**Risks and mitigations**

- CLEVR is synthetic and nearly solved with gold programs: the object of study is degradation under noise, not the headline accuracy.
- Sparse rewards for the walker: curriculum from one-hop questions; reward shaping is reported as such.
- Boxes derived from projected coordinates are approximate: document the procedure.
- DL (P2 variant) never defines self-attention: use a BiLSTM-CRF or few-shot LLM parser, or read NLP ch7.

---

## 5. Year 2 projects (Transverse project, 8 ECTS)

Common shape. **W0** (last weeks of Year 2 Period 1, part time): charter, acceptance tests, data access and licences, a first baseline, compute and euro budget, draft risk register. **W1-W6** (Year 2 Period 2): build phase, with a "walking skeleton" (thinnest end-to-end version) at the end of W1, the red-team swap in W4 and the defence after W6. The advanced themes of Year 2 Period 2 are taught during the build phase, so each brief says which chapter to read before which week. Each brief also names fallbacks for slot-TBC courses.

### Y2.1 Semi-structured biomedical QA: GraphRAG, GNN retriever or graph tokens, with calibrated abstention

**Route** Graph x LLM (flagship for O5). **Domain** healthcare (biomedical knowledge, not clinical advice).

**Pitch.** Biomedical questions mix text ("drugs described as kinase inhibitors") and relations ("... that target a gene associated with disease X"). Over the PrimeKG knowledge base, build three structure-aware retrievers (community GraphRAG, a GNN subgraph retriever that feeds soft tokens to an LLM in the G-Retriever style, and an agentic router) and compare them with a strong hybrid text retriever. Wrap the answers in a conformal abstention layer. Attack the system through poisoned node descriptions. And test whether two tools of spectral shape analysis transfer to knowledge graphs: heat-kernel signatures as structural encodings, and functional maps for aligning two biomedical graphs.

**Research question.** On a knowledge base that mixes text and relations, for which query types does structure-aware retrieval beat a hybrid text retriever, and can conformal abstention bound the error rate of the answers that are given without collapsing coverage on relational queries? Secondary geometric question: do multi-scale heat-kernel signatures (computed on the graph Laplacian) help a GNN retriever more than random-walk or Laplacian positional encodings, and does a functional-map alignment of Hetionet to PrimeKG recover the gold correspondences better than name matching?

**Usage-based "done" (examples, fixed at W0).** (i) Hit@5 at least equal to the hybrid baseline overall and significantly higher on relational queries; (ii) error rate on answered questions at or below the target (for example 10%) at a reported coverage; (iii) every answer cites node ids or passages that an automatic checker validates; (iv) attack success rate below the agreed threshold after defences; (v) P95 latency and cost per 1,000 queries within budget. Optional: a 40-question session with two pharmacy or medicine students, timed against PubMed search alone.

**Courses and chapters**

- `m2-large-language-models`: ch7 (7.1 chunking of node documents, 7.2 hybrid BM25 + dense + RRF + reranking, 7.3 RAG evaluation, 7.4 GraphRAG); ch8 (Def. 8.1 ReAct router; the 8.3 final lab and Ex. 12 as starting code); ch9 (9.2 LLM judge, 9.3 hallucinations, 9.4 prompt injection); ch4 (SFT of the projector and adapter of the soft-token model).
- `m2-geometric-deep-learning`: ch2 (Laplacian and its spectrum, here on the KG); ch3 (Def. 3.1 HKS, WKS, scale normalisation, the HKS stability bound); ch4 (functional maps; correspondence from descriptors); ch8 (Connection 1, "operators shared with graphs"; Connection 2, alignment as transport).
- `m2-advanced-topics-llms`: ch1 (1.1 contamination, 1.2 judge calibration); 3.4 (RAG or long context, Self-Route); ch4 (memory, GraphRAG); ch8 (8.1 serialised graphs, Def. 8.2 G-Retriever); Ex. 12.
- `m2-advanced-gnn`: ch4 (Laplacian eigenvector PE with SignNet, RWSE of Example 4.2); ch5 (graph transformers); 8.3 (GNN x LLM: soft tokens, alignment of spaces).
- `m2-privacy-uncertainty`: ch7 (calibration, ECE); ch9 (split conformal, Example 9.3); ch11 (Def. 11.1-11.2: verbalised confidence, self-consistency, semantic entropy); ch12 (Def. 12.2 abstention, risk-coverage).
- `m2-explainability-security-privacy-llms`: ch4 (integrated gradients for attributing an answer to passages or nodes); 5.3 (indirect injection, Example 5.2); ch6 (Def. 6.1 defence in depth); ch10 (red teaming; AI Act); Ex. 8 and Ex. 11.
- `m2-mlops-llm-engineering`: ch2 (CI gates); ch4 (cost); ch6 (6.1 freshness, Def. 6.1 RAGAS, 6.3 the graph in RAG); ch8 (tracing).
- Year 1: `m1p2-graph-ml` ch6 (KG completion) and ch10; `m1p2-nlp-text-mining` ch2 and ch6; `m1p2-reinforcement-learning` ch4 (bandit router) and ch7; `m1p2-optimal-transport` ch5 (FGW alignment baseline, if taken); `m1p1-deep-learning` 7.3 (LoRA); `m1p1-refresher-statistics` exit checkpoint.
- `m2-ethical-issues-ai` (#travailler grid): where an exploration tool ends and medical advice begins; abstention policy.

**Objectives** O5 (core), O3, O4, O8, O7 (healthcare), O1.

**Data and resources**

- STaRK (Wu et al., NeurIPS 2024 Datasets & Benchmarks; `snap-stanford/stark`), split STaRK-Prime: semi-structured queries over PrimeKG with a text document per node; official metrics Hit@1, Hit@5, Recall@20, MRR. Use its human-written queries where provided, in addition to the synthesised ones.
- PrimeKG (Chandak, Huang & Zitnik, Scientific Data 2023; Harvard Dataverse).
- Hetionet v1.0 (Himmelstein et al., eLife 2017) for the alignment experiment: shared identifiers on the overlapping node types (genes, compounds, diseases) give gold correspondences.
- Encoders: MedCPT (Jin et al., Bioinformatics 2023) and a general-purpose embedding model. G-Retriever code (He et al., NeurIPS 2024). `microsoft/graphrag`. GRASP (Hermanns et al., 2021) as the reference for graph alignment with spectral signatures and functional maps.
- Tools: a 7-8B open-weight instruct LLM served with vLLM; PyTorch Geometric; `scipy.sparse.linalg.eigsh`; RAGAS; MAPIE or a hand-written split-conformal wrapper; DVC + MLflow; OpenTelemetry or Langfuse.
- Domain variant (finance): FinanceBench (Islam et al., 2023) with SEC EDGAR 10-K filings and an LLM-built company graph.

**Milestones**

| Week | Milestone | Exit evidence |
|---|---|---|
| W0 | Charter; acceptance tests; STaRK-Prime and PrimeKG loaded; query taxonomy (textual / relational / mixed); hybrid baseline on a 500-query development subset. | baseline Hit@5 and MRR per query type; budget sheet |
| W1 | Walking skeleton: hybrid retrieval, LLM answer with node-id citations, citation checker; evaluation harness (STaRK metrics + answer accuracy + citation validity); contamination check on regenerated query variants. | end-to-end run on 100 queries |
| W2 | GraphRAG (communities, summaries, local k-hop search) and GNN subgraph retriever (prize-collecting Steiner tree subgraph + graph-transformer encoder). Geometric WP 1: HKS/WKS node encodings vs RWSE vs LapPE in the retriever. | ablation with 5 seeds |
| W3 | Soft-token LLM (projector + LoRA, G-Retriever style) vs textual serialisation; agentic router (LLM ch8 or bandit); geometric WP 2 (stretch): functional-map alignment of Hetionet and PrimeKG subgraphs vs FGW vs name + embedding matching. | Hits@k of alignment against gold |
| W4 | Conformal abstention (scores from the retriever, semantic entropy, self-consistency). Red-team swap: another team attacks with poisoned node descriptions and direct injections; layered defences. | ASR per family before and after |
| W5 | Full evaluation: paired bootstrap per query type; risk-coverage curves; latency and cost; ablations; CI tests from successful attacks; model card, datasheet, ethics memo. | evaluation report |
| W6 | Paper, defence with live demo, decision log, open question. | tagged release |

Read before: Advanced Topics ch8 and Advanced GNN 8.3 by W2; ESP ch5-ch6 by W4; Privacy & UQ ch9 and ch11 by W4.

**Deliverables** Service (OpenAI-compatible endpoint + small UI) with lineage; evaluation report with per-type CIs; risk-coverage plot; attack report and CI tests; model card and datasheet; guarantee sheet (coverage, error rate, limits); ethics memo; 6-8-page paper.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Usage-based acceptance tests | 15 | tests fixed at W0 and passed or honestly failed |
| LLM core: retrieval, generation, router | 15 | hybrid baseline strong; router compared to the best fixed retriever and an oracle |
| Geometric Data core: spectral encodings, alignment | 10 | HKS ablation with CIs; eigen-cost reported; a clear yes or no |
| Graph x LLM retrievers (Advanced Topics, Advanced GNN) | 15 | GraphRAG, GNN retriever and soft tokens compared per query type |
| Evaluation and statistics | 15 | per-type paired CIs; contamination check; calibrated judge with a human-checked subset |
| Trust: conformal abstention and attack suite | 15 | coverage checked on held-out queries, exchangeability discussed; adaptive attacks |
| Operations, reproducibility, communication | 15 | latency and cost per query; CI gates; paper and memo |

**Solo variant (research pilot).** 1,000 STaRK-Prime queries; hybrid baseline vs one structure-aware retriever (k-hop or G-Retriever-lite); the HKS ablation; split-conformal abstention; a 20-attack suite on the solo system; no alignment experiment.

**Group variant (4-5).** WP-Retrieval (LLM ch7, NLP); WP-Graph (GNN retriever, Advanced GNN, Geometric Data encodings and alignment); WP-LLM (soft tokens, router, Advanced Topics); WP-Trust (Privacy & UQ, ESP, red team); WP-Ops (MLOps, cost, CI).

**Risks and mitigations**

- Synthesised queries may favour text retrieval or carry artefacts: add the human-written queries and 50 team-written questions checked by a domain student.
- LoRA is not taught in the LLM course (the page refers to a "ch. 6: distillation, LoRA" that does not exist): use `m1p1-deep-learning` 7.3 or `m2-mlops-llm-engineering` ch7.
- Spectral cost on a large graph: only the low end of the spectrum is needed (sparse `eigsh`, k of about 100-300) or local HKS on k-hop neighbourhoods; measure the cost in W2.
- Slot-TBC courses: if Advanced GNN is not offered, use Graph ML ch5 encoders; if Privacy & UQ is not offered, its ch9 (conformal) is self-contained enough to self-study.
- Medical risk: the system is for literature and KG exploration; abstain, cite, and carry a disclaimer; the AI Act and the facts / values / options grid go in the memo.

### Y2.2 A text-to-3D-molecule copilot with controlled generation and calibrated property intervals

**Route** Graph x LLM. **Domain** molecules and pharma (inverse design).

**Pitch.** A chemist types a property profile in natural language. An LLM agent parses it into a validated specification (grammar-constrained decoding), calls an E(3)-equivariant diffusion generator and an EGNN property predictor, and returns 3D candidates with conformal property intervals. It refuses or flags requests that cross a written dual-use policy.

**Research questions.** (1) At equal sampling budget, does conditioning an E(3)-equivariant generator on parsed numeric targets give a better fidelity-diversity curve than conditioning on text embeddings? (2) Do conformal intervals from an EGNN property predictor keep their nominal coverage on generated molecules, which are a covariate shift from the training set, and does a weighted or adaptive conformal variant restore it?

**Usage-based "done" (examples).** For 100 natural-language requests: at least 95% parsed into a valid specification (checked by hand on a sample); median fraction of returned candidates that are valid, unique, novel and inside the requested ranges above an agreed level; empirical coverage of the property intervals within 5 points of nominal on generated molecules; a known false-refusal rate and miss rate for the dual-use filter.

**Courses and chapters**

- `m2-geometric-deep-learning`: ch7 (Def. 7.1, the EGNN theorem and its proof; numerical equivariance tests); ch8 (3D molecules, molecular descriptors, generation by equivariant diffusion).
- `m2-large-language-models`: ch4 (SFT of a small model for request parsing, if few-shot is not enough); ch7 (retrieving known similar molecules and their literature as grounding); 8.1 (tool-using agent); ch9 (evaluation, hallucination).
- `m2-graph-generative-models`: ch5 (Def. 5.1 discrete diffusion, DiGress); ch6 (Def. 6.1 MMD, validity, uniqueness, novelty, FCD; lab 1); ch7 (Def. 7.1 conditioning mechanisms, 7.2 text-to-graph, Example 7.3 classifier-free guidance); ch8 (Def. 8.1 inverse design and Pareto fronts).
- `m2-control-generative-ai`: ch3 (Def. 3.1 DFA, 3.2 masking: JSON specification and SELFIES grammar); ch8 (controlling graph generators); ch9 (Def. 9.1 fidelity and diversity, strength sweeps); ch10 (Def. 10.3 robustness budget; Theorem 10.1, syntactically valid attacks); Ex. 1.
- `m2-advanced-gnn` 8.1 (EGNN for 3D molecules) and ch2 (expressivity of the property predictor).
- `m2-privacy-uncertainty`: ch9 (split conformal), ch10 (CQR), ch12 (decision and abstention).
- `m2-advanced-topics-llms` ch9 (agent reliability, the p^k law); 2.3 (RLVR with chemistry-verifiable rewards, optional).
- `m2-explainability-security-privacy-llms` 5.2 (jailbreaks) and ch10 (red teaming of dual-use requests; AI Act).
- `m2-mlops-llm-engineering` ch1 (lineage of generator checkpoints, datasets and policy versions) and ch8 (tracing the agent's tool calls, per-request budgets).
- Year 1: `m1p2-graph-ml` ch8 (EGNN) and ch9; `m1p2-multimodal-genai` ch3-ch5 (DDPM, guidance, InfoNCE); `m1p2-reinforcement-learning` ch5 (RL fine-tuning as an alternative steering); `m1p2-nlp-text-mining` ch1 (tokenisation).
- `m2-ethical-issues-ai`: the dual-use molecule-generation case.

**Objectives** O2 (core), O6 (text + 3D), O4, O5, O7 (pharma), O8 (dual use, uncertainty), O3.

**Data and resources**

- QM9 (Ramakrishnan et al., Scientific Data 2014): small molecules with DFT 3D geometries and quantum properties.
- GEOM-Drugs (Axelrod & Gómez-Bombarelli, Scientific Data 2022) as a stretch goal.
- ChEBI-20 (Text2Mol) for text conditioning; MoleculeNet Tox21 for a toxicity flag; Therapeutics Data Commons oracles; GuacaMol multi-property objectives.
- Models: EDM, E(3)-equivariant diffusion (Hoogeboom et al., ICML 2022; code `e3_diffusion_for_molecules`); DiGress (Vignac et al., ICLR 2023).
- Tools: RDKit (ETKDG conformers, exact descriptors such as Crippen logP, TPSA, molecular weight, QED), GFN2-xTB (Bannwarth, Ehlert & Grimme, JCTC 2019) for cheap geometry and energy checks on a subsample, Outlines or XGrammar for constrained decoding, MAPIE, PyTorch Geometric, vLLM.

**Milestones**

| Week | Milestone | Exit evidence |
|---|---|---|
| W0 | Charter; QM9 splits; generator choice (released checkpoint or reduced model); specification grammar (property, comparator, value, tolerance); dual-use policy drafted with the ethics seminar. | baseline unconditional samples with metrics |
| W1 | Walking skeleton: request, constrained specification, property-conditioned generator, RDKit validity and stability checks, answer. | 20 requests end to end |
| W2 | EGNN predictor with numerical equivariance test; split-conformal intervals; text-conditioning path (ChEBI-20 text embeddings projected to the conditioning vector, or a 2D DiGress with text guidance followed by conformer generation). | coverage on the QM9 test set |
| W3 | Fidelity-diversity curves against guidance strength for numeric vs text conditioning; two-objective Pareto inverse design. | curves with CIs at equal budget |
| W4 | Coverage under shift: on generated molecules with exact (RDKit) or computed (xTB subsample) ground truth, measure coverage; weighted conformal variant. Red-team swap: jailbreaks against the dual-use policy; syntactically valid but adversarial specifications. | coverage table; ASR and false-refusal rate |
| W5 | Evaluation: MMD, validity, uniqueness, novelty, stability, FCD; agent reliability on 100 multi-step requests; latency; model card; ethics memo. | evaluation report |
| W6 | Paper, demo, defence. | tagged release |

Read before: Control ch3 and Graph Generative Models ch7 by W1; Privacy & UQ ch9 by W2.

**Deliverables** Agent service with constrained tool calls; fidelity-diversity and coverage-under-shift figures; policy evaluation (refusals and misses), without generating hazardous content; model card; ethics memo; paper.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Usage-based acceptance tests | 15 | measured on 100 requests |
| Geometric core: EGNN, equivariant generator | 15 | equivariance verified numerically; generator stability reported |
| LLM core: parsing, grounding, agent | 10 | constrained decoding; parse errors classified |
| Generative modelling and control | 15 | equal-budget comparison; strength sweep; Pareto front, not means |
| Evaluation and statistics | 15 | standard generation metrics; seeds; CIs |
| Trust: conformal under shift, dual-use policy | 15 | coverage measured on generated molecules; refusal rates both ways |
| Operations, reproducibility, communication | 15 | budget respected; paper and memo |

**Solo variant (research pilot on question 2).** QM9 only; numeric conditioning only; a released checkpoint; EGNN predictor; conformal coverage under shift with exact RDKit ground truth.

**Group variant (4).** WP-Generator (Graph Generative Models, Geometric Data); WP-Predictor and UQ (Geometric Data ch7, Privacy & UQ); WP-Agent and control (LLMs, Control); WP-Evaluation and ethics (ESP, ethics seminar).

**Risks and mitigations**

- Training an equivariant diffusion model to paper quality takes several GPU-days: use released checkpoints where available, or a reduced model with fewer diffusion steps, and say so.
- ChEBI-20 molecules are larger and more diverse than QM9: keep the text path in 2D (DiGress) with RDKit conformers and document the mismatch.
- Several courses are slot TBC (Control, Graph Generative Models, Privacy & UQ): fallbacks are Graph ML ch9, Multimodal GenAI ch4 and self-study of Control ch3 and Privacy & UQ ch9.
- Dual use: the policy restricts targets to benign properties; red-team prompts are scored on refusal behaviour, never on the chemistry produced.

### Y2.3 Speak, see, shop: a voice-first assistant that retrieves and recommends 3D products

**Route** AI systems. **Domain** recommendation and e-commerce.

**Pitch.** A customer describes an object out loud ("a low oak side table with a round top"). The assistant transcribes in streaming mode, parses the request, retrieves products by fusing text, rendered-image and 3D-shape embeddings, suggests similar items over a product graph, and answers by voice within a latency budget. Seller-written descriptions are treated as untrusted input.

**Research question.** How much retrieval quality is lost from typed to spoken queries (ASR errors, accents, noise); how much of it does a 3D shape tower trained by text-shape contrastive learning recover compared with text-only retrieval and CLIP on rendered views; and can the whole loop meet a P95 time-to-first-audio of 1.5 s on one GPU?

**Usage-based "done" (examples).** On 60 hand-written queries spoken by consenting team members in quiet and noisy conditions, nDCG@10 within an agreed margin of the typed version; P95 time-to-first-audio at or under 1.5 s at the target load; no successful instruction injection from product descriptions in the CI suite.

**Courses and chapters**

- `m2-speech-technology`: ch4 (Whisper; Example 4.3 on French WER); ch5 (Def. 5.1 streaming latencies, chunking, VAD); ch7 (TTS; Example 7.4 latency budget); ch10 (conversational loop: endpointing, barge-in); ch9 (voice-cloning ethics: no cloning in this project); Ex. 1, 2 and 5.
- `m2-geometric-deep-learning`: ch6 (Architecture 6.1 PointNet, DGCNN, DiffusionNet); ch3 (HKS, WKS and ShapeDNA as a non-learned retrieval baseline); ch8 (industrial CAD and mesh retrieval; Connection 3, 3D tokens for LLMs); Ex. 11 and Ex. 12 (shape retrieval with mAP).
- `m2-large-language-models`: ch7 (hybrid retrieval, reranking); ch8 (8.1 agent and tools, 8.2 multimodality); ch6 (6.4 quantisation, 6.5 serving).
- `m2-mlops-llm-engineering`: ch3 (Def. 3.3 serving SLOs: TTFT, TPOT, P99; batching); ch4 (euros per million tokens); ch5 (drift monitors on queries); ch8 (tracing, guardrails); Ex. 3 and Ex. 7.
- `m2-explainability-security-privacy-llms` 5.3 (indirect injection through product text) and ch6 (layered defences); `m2-security-robustness` ch1 (Def. 1.1), ch9 and ch10.
- Year 1: `m1p1-signal-processing` ch5-ch8 (Mel features, noise, resampling); `m1p1-computer-vision` ch10 (point clouds, kNN graphs); `m1p1-shapes` ch4 (point processing, normals) and ch8 (spectral descriptors); `m1p2-graph-ml` ch6 (link prediction on an item graph, PinSage); `m1p2-nlp-text-mining` ch6 (attribute slot filling: colour, material, size); `m1p2-deep-learning-p2` ch5; `m1p2-multimodal-genai` ch5 (InfoNCE) if taken, otherwise self-study.

**Objectives** O6 (core: speech, language, images, 3D), O7 (e-commerce, deployment), O3, O8, O4, O1, O2 (light: generative TTS).

**Data and resources**

- Amazon Berkeley Objects, ABO (Collins et al., CVPR 2022): product listings with multilingual metadata, catalogue images and artist-made 3D models (glTF); CC BY-NC 4.0.
- Objaverse (Deitke et al., CVPR 2023) with Cap3D captions (Luo et al., NeurIPS 2023), for text-shape pre-training (stretch).
- Mozilla Common Voice (accented English and French read speech) for robustness; MUSAN (Snyder, Chen & Povey, 2015) for noise.
- Tools: Whisper (`openai/whisper`, or faster-whisper), Silero VAD, OpenCLIP, Piper or MMS-TTS, vLLM, trimesh or Open3D, pyrender or Blender for multi-view renders, PyTorch Geometric, FAISS, OpenTelemetry or Langfuse.
- Query set built by the team: 300 queries generated from held-out ABO metadata (gold items known), 60 hand-written queries with graded relevance, and spoken versions (consented recordings by team members, plus TTS renders with MUSAN noise).

**Milestones**

| Week | Milestone | Exit evidence |
|---|---|---|
| W0 | Charter; ABO subset (furniture and home categories that have 3D models); licence check; query-set protocol; consent form. | typed-query baseline |
| W1 | Walking skeleton: typed query, BM25 + dense retrieval over titles and attributes, answer; per-stage tracing. | nDCG@10, Recall@10; latency trace |
| W2 | Shape tower: point clouds sampled from the glTF meshes; PointNet++ or DGCNN (and DiffusionNet on meshes) trained with a contrastive text-shape loss; CLIP-on-renders tower; fusion (RRF or learned). | retrieval ablation per tower |
| W3 | Speech front end: streaming Whisper, VAD, endpointing; WER per condition; spoken-query retrieval; TTS reply; similar-item suggestions over a product graph (attribute edges + shape kNN edges; link prediction). | WER and nDCG typed vs spoken |
| W4 | SLOs: vLLM serving, quantisation, batching; P50/P95/P99 time-to-first-audio. Red-team swap: instructions injected in product descriptions, poisoning of the index. | SLO dashboard; ASR before and after |
| W5 | Evaluation: typed vs spoken (clean, noise, accent) with paired bootstrap; shape-tower robustness to remeshing and subsampling (the collapse discussed in the Geometric Data introduction); cost per 1,000 sessions; model card; ethics memo (voice data, persuasion and dark patterns). | evaluation report |
| W6 | Paper, live demo, defence. | tagged release |

Read before: Speech ch5 and ch10 by W3; MLOps ch3 by W4.

**Deliverables** Deployed demo; retrieval and ASR tables; per-stage latency budget; attack report and fixes; datasheet of the query set; model card; ethics memo; paper.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Usage-based acceptance tests | 15 | spoken-query test passed or the gap explained |
| Geometric core: shape tower | 15 | contrastive training; fair comparison with CLIP renders; robustness to remeshing |
| LLM core: retrieval, agent, serving | 10 | hybrid retrieval and reranking; quantisation measured |
| Speech | 15 | WER per condition; streaming latency decomposed |
| Evaluation and statistics | 15 | paired tests on the same items and queries |
| Trust: injection, poisoning, voice data | 15 | adaptive attacks; consent and retention policy applied |
| Operations, reproducibility, communication | 15 | P95 per stage, not only means; cost per session |

**Solo variant.** Typed and synthetic spoken queries; pretrained Whisper; one shape tower (PointNet) vs CLIP renders; text replies (no TTS); latency budget table.

**Group variant (5).** WP-Speech, WP-3D (Geometric Data), WP-Retrieval and LLM, WP-Ops, WP-Trust.

**Risks and mitigations**

- Many ABO listings have no 3D model: restrict the catalogue to modelled items.
- ABO is non-commercial: research use only.
- Rendering and point sampling take time: do them offline in W0-W1.
- Voice recordings are personal data: consent, deletion after the study, no voice cloning.
- Speech Technology is an announced, unpublished theme: if it is not offered, use Whisper and VAD as tools and budget latency with LLM 6.5 and MLOps ch3.
- GPU contention between ASR, LLM and TTS: measure it and quantise.

### Y2.4 The natural-language dispatcher: an LLM agent over exact and learned routing with built-in symmetry

**Route** AI systems, with a Graph x LLM option. **Domain** logistics (last-mile delivery).

**Pitch.** A dispatcher types "add a 15:00-16:00 pickup at stop 42, van 3 is off after 14:00, re-plan". The agent turns the request into a validated formulation (grammar-constrained), runs an exact solver and a learned neural routing policy, compares them, explains the change, and serves the result under latency SLOs. The learned policy is made invariant to rotations and reflections of the map by construction, and compared with policies that only learn the symmetry from augmentation.

**Research questions.** (1) At equal training budget, does building E(2) symmetry into the neural routing policy (an EGNN-style invariant encoder) generalise to unseen city layouts better than symmetry augmentation (POMO and Sym-NCO style)? (2) Can an LLM agent that delegates to a solver portfolio answer what-if requests on real last-mile routes with route quality close to solver-only and P95 latency within budget, and how often does it mis-formalise a request?

**Usage-based "done" (examples).** On 100 dispatcher requests with gold specifications: formalisation accuracy at or above an agreed level, with zero silent errors (every change is shown and confirmed); route cost within x% of PyVRP; P95 response under y s; no successful injection through customer notes in the CI suite.

**Courses and chapters**

- `m2-geometric-deep-learning`: ch7 (Def. 7.1, the EGNN theorem and proof, adapted to E(2); numerical invariance tests); ch8 (applications); ch0 (reminders).
- `m2-large-language-models`: 8.1 (ReAct, tools); ch4 (SFT of the request-to-specification parser); ch6 (serving); ch9 (evaluation).
- `m2-control-generative-ai`: ch3 (DFA masking for JSON specifications); ch10 (Theorem 10.1, syntactically valid injections; Def. 10.3 robustness budget); Ex. 1.
- `m2-advanced-gnn`: 8.2 (neural algorithmic reasoning); ch5 (attention-based graph encoders); ch1 (protocol).
- `m2-advanced-topics-llms`: ch9 (9.1 ReAct, 9.2 Toolformer, reliability per step); ch7 (efficiency).
- `m2-mlops-llm-engineering`: ch3 (SLOs); ch8 (8.1 tracing, Example 8.1 "the budget as the first guardrail", 8.3 agent evaluation); ch2 (CI gates); ch9 (sandbox).
- `m2-security-robustness` ch1 (Def. 1.1) and ch10; `m2-explainability-security-privacy-llms` 5.3 (injection through customer notes and stop names) and ch6.
- `m2-boosting-foundation-tabular` ch1-ch3 (gradient boosting for service-time and travel-time prediction) and ch9 (honest benchmarking); `m2-privacy-uncertainty` ch10 (CQR intervals on travel times, turned into a time-window risk), optional.
- Year 1: `m1p2-reinforcement-learning` ch5 (REINFORCE with rollout or shared baselines) and 4.2 (MCTS as search at decoding time); `m1p2-graph-ml` ch5 and ch8; `m1p1-refresher-cs` ch7 (Dijkstra, A*); `m1p2-nlp-text-mining` ch6 (entity tagging of formulation elements on NL4Opt); `m1p2-optimization-ai` ch8 (constraints), if taken. Continues Y1.2.

**Objectives** O7 (core: logistics, deployment), O4, O3, O5 (LLM coupled with combinatorial graph optimisation), O8, O1.

**Data and resources**

- Amazon Last Mile Routing Research Challenge data set (Merchán et al., Transportation Science 2024; AWS Open Data Registry): real delivery routes in several US metropolitan areas with stops, time windows, package information, travel-time matrices and the sequences drivers actually followed.
- CVRPLIB (Uchoa et al., EJOR 2017, "X" instances) and the Solomon VRPTW instances.
- NL4Opt (Ramamonjison et al., NeurIPS 2022 competition) for natural-language-to-formulation entity tagging.
- Solvers and learned policies: PyVRP (Wouda, Lan & Kool, INFORMS Journal on Computing 2024), OR-Tools; RL4CO (Berto et al.) implementations of the Attention Model (Kool, van Hoof & Welling, ICLR 2019), POMO (Kwon et al., NeurIPS 2020) and Sym-NCO (Kim, Park & Park, NeurIPS 2022).
- Tools: Outlines or XGrammar, vLLM, OpenTelemetry, OSMnx (optional geometry).

**Milestones**

| Week | Milestone | Exit evidence |
|---|---|---|
| W0 | Charter; instance generator and Amazon subset; PyVRP baselines with gaps; specification schema; request taxonomy (add or remove a stop, time window, vehicle availability, priority). | baseline costs |
| W1 | Walking skeleton: request, constrained specification, PyVRP, explained difference; 100 hand-written requests with gold specifications. | formalisation accuracy |
| W2 | Neural policy: Attention Model / POMO baseline via RL4CO; EGNN-style invariant encoder; invariance tests; training at equal budget on uniform CVRP-50/100; augmentation variant. | training curves; invariance error at machine precision |
| W3 | Generalisation: clustered instances, X instances, Amazon routes (projected coordinates), rotated and reflected copies; portfolio policy (neural first, solver when the estimated gap or the time allows). | gap tables with CIs over instances |
| W4 | Serving and SLOs. Red-team swap: injections in customer notes and stop names, malicious what-ifs ("assign every stop to van 1"), budget exhaustion; guardrails. | ASR before and after |
| W5 | Evaluation: agent reliability on multi-step requests; cost; drift monitor on a new city; model card; ethics memo (driver workload, labour impact). | evaluation report |
| W6 | Paper, demo, defence. | tagged release |

Read before: Control ch3 by W1; MLOps ch8 and ESP ch5 by W4.

**Deliverables** Dispatcher service; symmetry-study figures; taxonomy of formalisation errors; SLO dashboard; attack report; model card; ethics memo; paper.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Usage-based acceptance tests | 15 | measured on the 100-request set |
| Geometric core: built-in symmetry | 15 | invariance proved and tested; equal-budget comparison with augmentation |
| LLM core: formalisation and agent | 15 | the LLM never writes routes directly; every change goes through validated tools |
| Advanced work packages (Control, Advanced GNN, tabular models) | 10 | constrained decoding; algorithmic-reasoning view discussed |
| Evaluation and statistics | 15 | optimality gaps against PyVRP; drivers' actual sequences as a realism check |
| Trust and SLOs | 15 | adaptive injections; budgets enforced |
| Operations, reproducibility, communication | 15 | P95 measured; decision log |

**Solo variant (research pilot on question 1).** Symmetry built in vs augmentation on CVRP, rotated and clustered tests and an Amazon subset; the LLM part reduced to constrained parsing of 50 requests.

**Group variant (4).** WP-Neural routing (Geometric Data, Year 1 RL, Advanced GNN); WP-Agent (LLMs, Control, Advanced Topics); WP-Ops (MLOps); WP-Trust and evaluation.

**Risks and mitigations**

- Neural routing will not beat PyVRP on quality: the value studied is speed for what-if requests and generalisation, not a new optimum.
- Real-data quirks (coordinates, time windows): budget preprocessing time in W0.
- POMO-style training takes hours per run: use small sizes and few seeds per configuration, stated in the charter.
- Mis-formalisation: validation plus a confirmation step before any re-plan.
- No course teaches logistics: the brief supplies the references (see the maintainers' notes in section 7).

### Y2.5 Fraud alerts you can defend: temporal GNN, spectral descriptors and grounded LLM narratives under attack

**Route** both. **Domain** finance (anti-money laundering on a cryptocurrency transaction graph).

**Pitch.** Detect illicit transactions on a real transaction graph with a strictly temporal protocol. Compare a tuned gradient-boosting model, temporal GNNs and spectral structural descriptors. Attach to each alert a narrative written by an LLM, every claim of which is checked against the evidence subgraph. Then audit the whole pipeline for regime shift, evasion attacks and privacy leakage.

**Research question.** Under a strictly temporal protocol, which signals (account features, temporal GNN embeddings, multi-scale heat-kernel descriptors) add detection value over a tuned GBDT, and which of them survive a budgeted edge-injection attack and the regime shift reported late in the Elliptic timeline? Can an LLM write alert narratives in which every factual claim is verifiable against the subgraph? The geometric hypothesis comes from the HKS stability bound of Geometric Data ch3: descriptors that are Lipschitz in the metric should be harder to move with a few injected edges than learned message-passing features.

**Usage-based "done" (examples).** Recall at a fixed alert budget (for example 100 alerts per time step) above the GBDT baseline with a CI that excludes zero; 100% of narrative claims machine-checkable and at most an agreed share flagged false; a drift alarm that fires within an agreed number of time steps after the known shift; a model card that a compliance reviewer accepts.

**Courses and chapters**

- `m2-advanced-gnn`: ch6 (TGN, TGAT, strict temporal splits); ch7 (robustness and privacy on graphs); ch4 (positional encodings); ch1 (protocol: at least 5 seeds, CIs); Ex. 8 and Ex. 9.
- `m2-geometric-deep-learning`: ch2 (Laplacian spectrum); ch3 (Def. 3.1 HKS, WKS and the HKS stability bound). This is the lightest geometric share of the five Year 2 projects; a team that wants more geometry should choose Y2.2, Y2.3 or Y2.4.
- `m2-large-language-models`: ch7 (grounded generation over retrieved evidence); 9.3 (hallucination); ch6 (serving a small model).
- `m2-control-generative-ai` ch3 (constrained narrative template).
- `m2-boosting-foundation-tabular`: ch1-ch4 (GBDT, encodings); ch9 (honest benchmarking); Ex. 2 (leakage) and Ex. 7.
- `m2-security-robustness`: ch1 (Def. 1.1); ch9 (graph attacks, Nettack-style); ch8 (Def. 8.1 model extraction against the scoring API, Def. 8.3 membership inference); Ex. 9 (threat analysis of a bank scoring system).
- `m2-privacy-uncertainty`: ch7 (calibration); ch9 (conformal alert sets); ch12 (Def. 12.2 cost-sensitive decision, abstention to an analyst).
- `m2-explainability-security-privacy-llms` ch4 (attributions and their faithfulness) and 10.2 (AI Act).
- `m2-mlops-llm-engineering`: ch5 (Def. 5.1 drift, monitoring loops); ch2 (gates); ch1 (lineage).
- Year 1: `m1p2-graph-ml` 5.6-5.8 (temporal graphs) and ch8 Example 8.1; `m1p1-machine-learning` ch4 (imbalance, calibration, cost-based thresholds) and ch6; `m1p2-reinforcement-learning` ch4 (alert-budget bandit, optional); `m1p1-refresher-statistics`; `m1p1-strategy-marketing` (cost of error in euros).
- `m2-ethical-issues-ai`.

**Objectives** O8 (core), O4, O7 (finance), O3, O5 (LLM narratives grounded in subgraphs), O1.

**Data and resources**

- Elliptic Data Set (Weber et al., KDD 2019 Workshop on Anomaly Detection in Finance; Kaggle): Bitcoin transaction graph over 49 time steps with anonymised features and about 2% of transactions labelled illicit. The authors report that models stop detecting illicit activity after a dark-market shutdown late in the timeline: the drift case for MLOps ch5.
- Elliptic++ (Elmougy & Liu, KDD 2023): adds the wallet-address graph and features.
- IBM synthetic AML transactions (Altman et al., NeurIPS 2023 Datasets & Benchmarks; Kaggle "IBM Transactions for Anti Money Laundering"): a second, fully labelled setting with amounts, currencies and laundering patterns, which gives the narratives something concrete to say.
- Tools: PyTorch Geometric (TGN), XGBoost or LightGBM, DeepRobust (graph attacks), SHAP, Captum, MAPIE, vLLM, Outlines, MLflow; PSI and KS monitors written by the team or from a monitoring library.

**Milestones**

| Week | Milestone | Exit evidence |
|---|---|---|
| W0 | Charter: alert budget, cost of error in euros, temporal split (early steps for training, then validation, then a test window that includes the shift); GBDT baseline on transaction features. | baseline per time step |
| W1 | Walking skeleton: GBDT, calibrated scores, alert queue, template narrative; evaluation harness (PR-AUC, recall at budget, illicit-class F1 per time step). | per-step curves |
| W2 | Graph signals: static GCN/GAT, TGN; HKS/WKS descriptors (per time-step component, sparse eigensolver) fed to the GBDT; ablations with 5 seeds. | ablation table with CIs |
| W3 | LLM narratives: evidence subgraph (k-hop plus top-attributed edges), constrained template, claim checker (each claim becomes a graph query); faithfulness and usefulness rated by 3 reviewers on 50 alerts. | claim-level precision |
| W4 | Attacks and red-team swap: budgeted edge injection from attacker-controlled wallets, feature evasion; robustness of each signal; model extraction and membership inference against the scoring API; conformal alert sets and abstention. | robustness curves against budget |
| W5 | Drift monitoring across time steps (PSI, KS; detection delay); retraining policy; cost-in-euros report; model card; AI Act classification note; ethics memo. | drift report |
| W6 | Paper, analyst-console demo, defence. | tagged release |

Read before: Advanced GNN ch6 and ch7 by W2; Security ch9 by W4.

**Deliverables** Analyst-console demo; per-time-step performance with CIs; robustness curves per signal; narrative faithfulness study; drift report; model card; ethics memo; paper.

**Rubric (100)**

| Criterion | Pts | Full marks |
|---|---|---|
| Usage-based acceptance tests | 15 | recall at budget with CI; narrative and drift tests |
| Graph and geometric core: temporal GNN, spectral descriptors | 15 | strictly temporal; the stability hypothesis tested, confirmed or refuted |
| LLM core: grounded narratives | 10 | every claim checked automatically; reviewer study |
| Advanced work packages (tabular, Advanced GNN) | 10 | GBDT tuned with an equal budget |
| Evaluation and statistics | 15 | per-step curves; seeds; paired tests |
| Trust: attacks, privacy, calibration, drift | 20 | budgeted and adaptive attacks; extraction and MIA; detection delay measured |
| Operations, reproducibility, communication | 15 | cost in euros; decision log; AI Act note |

**Solo variant.** Elliptic only; GBDT vs GBDT + HKS vs TGN; one attack; template narratives with the claim checker (no fine-tuning).

**Group variant (5).** WP-Detection, WP-Spectral and robustness, WP-Narratives, WP-Ops and drift, WP-Trust.

**Risks and mitigations**

- Elliptic features are anonymised: narratives can only cite structure and timing; use Elliptic++ and the IBM data for amounts and patterns.
- Most Elliptic transactions are unlabelled: state how unknowns are treated (excluded or positive-unlabelled) and test the choice.
- Evasion on public financial data: report attacks at the level needed for the evaluation, without operational guidance for real-world laundering.
- AI Act classification must be checked by the team: the creditworthiness item of Annex III excludes fraud detection, but other obligations (GDPR, AML law) remain.
- Slot-TBC courses: if Advanced GNN is not offered, Graph ML 5.6-5.8 covers TGAT and TGN at the level needed; if Security is not offered, use ESP ch5 and Advanced GNN ch7.

---

## 6. Cross-cutting views

### 6.1 Objectives x projects

Legend: ● core objective of the project (graded as such); ○ exercised in at least one work package.

| Objective | Y1.1 | Y1.2 | Y1.3 | Y1.4 | Y1.5 | Y2.1 | Y2.2 | Y2.3 | Y2.4 | Y2.5 |
|---|---|---|---|---|---|---|---|---|---|---|
| O1 ML & DL foundations | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| O2 Generative modelling | | | | ● | | | ● | ○ | | |
| O3 LLMs | ● | ○ | ○ | | ○ | ● | ○ | ● | ● | ○ |
| O4 Graph-structured data | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ● | ● |
| O5 Graph x LLM | ● | | ● | ● | ● | ● | ○ | | ○ | ○ |
| O6 Multimodal generative AI | | | | ● | ● | | ● | ● | | |
| O7 Industry practice | ○ | ● | ● | ○ | ● | ○ | ○ | ● | ● | ● |
| O8 Trustworthy AI | ○ | ○ | ○ | ○ | | ● | ● | ○ | ○ | ● |

Every objective except O1 (exercised in all ten projects, core in Y1.2) is core in at least two projects. O5, the distinctive emphasis, is core in five projects and O6 in four; on the mandatory path alone these are the two weakest objectives.

### 6.2 Courses x projects

Projects that use each course in a graded work package (chapter ids are in the briefs).

| Course | Projects |
|---|---|
| `m1p1-machine-learning` | all Year 1; Y2.5 |
| `m1p1-deep-learning` / `m1p2-deep-learning-p2` | Y1.1, Y1.4 (P1 variant); Y1.2, Y1.3 sys, Y1.5 (P2 variant) |
| `m1p1-refresher-statistics`, `m1p1-refresher-cs` | evaluation kit and repository template of all projects; Y1.2 and Y1.5 (graph algorithms) |
| `m1p1-signal-processing` | Y1.2; Y2.3 |
| `m1p1-computer-vision` | Y1.5; Y2.3 |
| `m1p1-shapes` | Y2.3 |
| `m1p1-tda` | Y1.1 (option) |
| `m1p1-emerging-ml` | Y1.3 (Graph x LLM variant) |
| `m1p1-strategy-marketing` | Y2.5 (cost of error); optional section in all |
| `m1p2-reinforcement-learning` | all Year 1; Y2.1, Y2.2, Y2.4; Y2.5 (optional) |
| `m1p2-graph-ml` | all Year 1; all Year 2 |
| `m1p2-nlp-text-mining` | all Year 1; Y2.1, Y2.2 (tokenisation), Y2.3, Y2.4 |
| `m1p2-multimodal-genai` | Y1.4, Y1.1 (option); Y2.2, Y2.3 |
| `m1p2-optimal-transport` | Y1.1 and Y1.3 (options), Y1.4 (optional); Y2.1 (alignment baseline) |
| `m1p2-optimization-ai` | Y1.3 (option); Y2.4 (optional) |
| `m2-large-language-models` | all Year 2 |
| `m2-geometric-deep-learning` | all Year 2 (Y2.5 light) |
| `m2-advanced-gnn` | Y2.1, Y2.2, Y2.4, Y2.5 |
| `m2-privacy-uncertainty` | Y2.1, Y2.2, Y2.5; Y2.4 (optional) |
| `m2-boosting-foundation-tabular` | Y2.4, Y2.5 |
| `m2-control-generative-ai` | Y2.2, Y2.4, Y2.5 |
| `m2-mlops-llm-engineering` | all Year 2 |
| `m2-security-robustness` | Y2.3, Y2.4, Y2.5 |
| `m2-graph-generative-models` | Y2.2 |
| `m2-explainability-security-privacy-llms` | all Year 2 |
| `m2-speech-technology` | Y2.3 |
| `m2-advanced-topics-llms` | Y2.1, Y2.2, Y2.4 |
| `m2-ethical-issues-ai` | all Year 2 (memo) |
| `m2-projet-transverse` | the container of all Year 2 projects |
| `m1p3-research-internship`, `m2-internship` | the "open question" deliverable of every project |

Not used in a graded work package: Computer Animation and Advanced DL among the 2026-27 electives (each brief can absorb them as an extra ablation: a crowd simulator as an RL environment for Y1.2, a self-supervised image tower for Y2.3), Image Synthesis (rendering of the ABO views in Y2.3 is a natural fit), and the pages kept for reference.

### 6.3 Existing course material reused

The projects are built so that students extend labs that already exist instead of starting from nothing:

| Existing material | Reused in |
|---|---|
| Graph ML final lab (mini-GraphRAG), Example 8.1, Example 3.4, Ex. 15 | Y1.1, Y1.3, Y1.4; Y2.1 |
| NLP Ex. 14 capstone pipeline, Ex. 13 (MF vs content on MovieLens) | Y1.1, Y1.3 |
| RL ch7 guiding lab and Ex. 16 (agent project), Ex. 8 (LinUCB) | Y1.1, Y1.3 |
| Multimodal GenAI ch5 InfoNCE code, Ex. 5 | Y1.4; Y2.3 |
| DL (P2 variant) Example 5.4 protocol, Ex. 7 budget | Y1.2, Y1.5; all charters |
| LLM final lab (8.3) and Ex. 12 (vector vs graph router), 7.3 RAG lab protocol | Y2.1 |
| Advanced Topics Ex. 12 (Talk like a Graph + light G-Retriever) | Y2.1 |
| Geometric Data Ex. 11 (DiffusionNet vs GCN), Ex. 12 (shape retrieval, mAP) | Y2.3 |
| Graph Generative Models lab 1 (MMD harness), Ex. 8 | Y2.2 |
| Control Ex. 1 (DFA mask as a LogitsProcessor) | Y2.2, Y2.4, Y2.5 |
| Advanced GNN Ex. 8 (TGN memory ablation), Ex. 9 (edge attack + defence) | Y2.5 |
| Security Ex. 9 (threat analysis of a bank scoring system) | Y2.5 |
| Privacy & UQ Ex. 10 (LLM UQ), Ex. 11 (privacy + UQ pipeline, guarantee sheet) | Y2.1, Y2.2, Y2.5 |
| ESP Ex. 8 (RAG injection, central lab), Ex. 11 (red-team protocol) | all Year 2 |
| MLOps Ex. 12 (enterprise assistant, game day), Ex. 6 (gate significance) | all Year 2 |
| Speech Ex. 1, 2, 5 | Y2.3 |
| Boosting Ex. 2 (leakage), Ex. 7 (symmetric benchmark) | Y2.4, Y2.5 |

## 7. Notes for maintainers: what the course pages need for these projects to run

1. **Year 1 project slots have no subject.** Graph ML session 9 says "start the team project" with no subject, the RL project (50%) is unspecified, and NLP Ex. 14 is a separate capstone. Proposed fix: a short "Team project" box in Graph ML ch8 (after Example 8.1), in the RL introduction (assessment paragraph) and in NLP 8.6 pointing to the projects page, with the rule "one repository, three graded work packages".
2. **The transverse-project page has no brief, calendar or rubric.** Add a subject bank (the five Year 2 briefs, one paragraph each), the W0 + W1-W6 calendar, the Year 2 rubric, the mandatory trust work package and the W4 red-team swap.
3. **The O5 chain lacks the pieces Y1.1 and Y2.1 need.** Relation extraction is never taught (NLP ch6); Graph ML ch10 is prose with an unspecified final lab; LLM 7.4 is one bullet. Add NLP 6.4 "Relation extraction" (one exercise scored on 2WikiMultiHopQA triples), Graph ML 10.4 "GraphRAG, worked" with a named corpus and baselines, and a half page in LLM 7.4 on KG retrieval that points to STaRK.
4. **Late teaching.** Graph ML ch9-ch10, RL ch6-ch7 and NLP 8.5 come in the last sessions. Add a "read ahead for the team project" line to each session plan.
5. **Geometric Data has no worked bridge to graphs and language.** Ch8 is a bullet list. Add a self-study worked case (about 2 h): HKS computed on a graph Laplacian and a functional-map graph alignment with gold correspondences (GRASP-style), plus a "3D + language" contrastive retrieval example. Without it, Y2.1 and Y2.5 rely on students transposing ch3-ch4 alone.
6. **Logistics is in the official description but in no course.** Add bounded notes: RL 5.4 or 4.2, neural combinatorial optimisation (Attention Model, POMO, rollout baseline) with one exercise; Graph ML ch8, a spatio-temporal demand-forecasting use case on a zone graph; Advanced GNN 8.2, routing as an algorithmic-reasoning application; Geometric Data ch7, one remark on E(2)-symmetric routing (Sym-NCO).
7. **LoRA/PEFT** is needed by Y2.1, Y2.2 and Y2.4 but is not taught in the LLM course (the page refers to a missing "ch. 6: distillation, LoRA"). Add a PEFT section to LLM ch4.
8. **AI-systems prerequisites.** DL (P2 variant) never defines self-attention and AI-systems students cannot take Multimodal GenAI. Add a self-contained transformer box to NLP ch7 and a half-page InfoNCE recap where Y2.3 first needs it (Geometric Data ch6 or LLM 8.2).
9. **One evaluation kit.** The pieces (ML 4.6, the statistics refresher's exit checkpoint, Advanced DL Def. 1.1, Advanced GNN ch1, Boosting ch9, MLOps ch2) should be gathered in one section, best in the statistics refresher's exit checkpoint, with cross-references from ML 4.6 and MLOps ch2.
10. **Ethics seminar deliverable.** The seminar page has no deliverable. Add a facts / values / options memo on the student's own transverse project, with the AI Act classification step.
11. **Internship bridges.** Add to the research-internship page a "from Year 1 project to internship proposal" paragraph, and to the final-internship page a module map that lists which course chapters back which topic family.
12. **Data licences and consent.** Several datasets above are non-commercial (MIND, ABO), and Y2.3 records voices. Add a licence and consent checklist to the transverse page's "How to approach it".
