# LLGA study notes: coherence report

Sources: the per-course reader records (49 pages); objectives.md, prerequisites.md, redundancy-notation.md, errors.md and capstones.md in this folder; index.html; course pages, which were opened to check locations. Hours headroom comes from tools/check_progression.py. This was read-only work.

## 1. Objectives
O1 ML & DL foundations. O2 Generative modelling theory. O3 Large Language Models. O4 Graph-structured data. O5 Graph × LLM (the distinctive emphasis). O6 Multimodal generative AI. O7 Hands-on and industry practice. O8 Trustworthy and responsible AI.

## 2. Coverage summary
Maximum depth (0–3) by path, judged on what pages deliver:
- O1: 3 on the mandatory path, Graph × LLM route and AI-systems route.
- O2: 2 (partial) mandatory, 3 Graph × LLM, 2 AI systems. DL P1 has no diffusion or flows, yet mandatory Graph ML 9.5 and Geometric Data ch7–8 assume diffusion.
- O3: 3 everywhere, with holes: no LoRA, no prompting/ICL, and attention is undefined for DL P2 students.
- O4: 3 everywhere.
- O5: 2 everywhere. No page reaches 3. On the mandatory path it is one prose chapter (Graph ML ch10), relation extraction is never taught, and LLM 7.4 is one bullet.
- O6: 2 nominal / 1 for the generative part on the mandatory path (LLM 8.2 is four bullets); 3 on the routes (Multimodal, Speech).
- O7: 3 through courses. The 58 ECTS of project vehicles are framing pages, and logistics appears nowhere.
- O8: 2 narrow on the mandatory path (LLM ch9 only); 3 on the routes. The ethics seminar page is empty.

## 3. Main gaps and how the plan fixes them
- O5 chain: NLP 6.4 Relation extraction; Graph ML 10.4 GraphRAG worked (2WikiMultiHopQA final lab, BM25 and dense baselines); LLM 7.4 KG retrieval with STaRK. Route depth: Advanced GNN 8.3 worked, Advanced Topics ch8 graph instruction tuning, one shared taxonomy (Graph ML 10.2).
- O6: LLM 8.2b VLM worked (self-study); DL P1 6.6 ViT; Geometric Data ch8 worked bridges (text–shape retrieval, HKS on graphs, functional-map alignment).
- O8: ML 4.8 group fairness and 6.4 TreeSHAP; LLM 9.7 privacy and bias (self-study); ethics seminar cases, regulation primer and memo deliverable.
- O2: DL P1 9.4 diffusion + flow box (self-study); DL P2 7.3 sampler; Graph ML 9.5 D3PM loss; Multimodal 4.x flows to flow matching; Speech ch7 CFM/Grad-TTS.
- O3: LLM 4.0 prompting/ICL and 4.3 PEFT + distillation; NLP ch7 transformer and few-shot boxes and 7.4 minimal RAG; DL P2 ch0 'From MLP to transformer block'; LLM 9.6 and ML 4.9 model comparison.
- O7: transverse subject bank, calendar, rubric, trust work package and licence checklist; research-internship template; final-internship module map; Team-project boxes in Graph ML, RL and NLP; logistics notes in RL, Graph ML, Advanced GNN and Geometric Data.

## 4. Prerequisite problems (top)
1. 'DL once' is broken: DL P2 assumes DL P1 and a Choose-1 sibling. Fix: new prerequisites (ML + Refresher NN), a taught DL P2 ch0, review boxes in Graph ML/NLP/RL, and corrected status wording.
2. Basic RAG is used in Y1 P2 but taught in Y2 P1. Fix: NLP 7.4.
3. Prompting/ICL is taught nowhere. Fix: LLM 4.0.
4. Control (Y2 P1) depends on Graph Gen (Y2 P2). Fix: joint edit; Control rereads Graph ML ch9.
5. Mandatory Geometric Data names optional prerequisites. Fix: ch0 boxes.
6. Y2 pages name prerequisites excluded on their own route. Fix: each page gets its own boxes.
7. LoRA, fairness, DP, KL/KKT, Markov chains and model comparison have no mandatory home. Fix: LLM 4.3, ML 4.8/0.3/0.4/4.9, Refresher Stats 2.x, Privacy & UQ tagged for both routes.
8. Y2 P2 siblings cite each other circularly. Fix: relabel as co-requisites; LLM 9.4 is the guaranteed source.
9. Orphan concepts (Hungarian, Kalman, n-gram LM, ANN, GPU memory, MAML) get one canonical home each, and about 40 wrong pointers are retargeted.

## 5. Redundancies (canonical page ← recall boxes elsewhere)
R1 DL P1 ch9 ← Multimodal ch0–2 (3–4 h freed); R2 LLM Thm 9.3 ← Control ch6, ESP 9.2; R3 RL ch6 lemma ← LLM ch5, Control Thm 5.1; R4 Graph ML Prop 8.3 ← GDL ch7, Advanced GNN 8.1; R5 NLP Thm 4.1 ← Graph ML 3.1; R6 LLM systems results ← Advanced Topics, MLOps; R7 GDL ch1–3 ← Shapes; R8 CV ch9/ch6 ← CV Applications; R9 RL ← DL P2 7.2; R10 Security Def 8.3 / Privacy & UQ ← ESP ch8; R11 Multimodal Thm 4.1 ← Control, Graph Gen; R12 Graph ML ch9 taxonomy ← Graph Gen; R13 TDA ← Shapes ch9; R14 Graph ML 10.2 ← Advanced GNN/Advanced Topics. The freed time funds the O5/O6/O8 additions.

## 6. Notation
Contradictions to fix first: C1 mean-curvature sign (GDL); C2 PageRank α; C3 CFG weight (Advanced DL); C4 discrete-diffusion orientation (Graph Gen); C5 spectral gap; C6 randomized response p; C7 'normalized' Laplacian (Shapes); C8 SGNS letters; C9 distillation weights (CV Applications); C10 eigen-indexing (Shapes). Create notation.qmd with 16 rows (returned in notation_conventions). The 27 conflicting active pages open their notation block with a 'deviations' header.

## 7. Confirmed errors
All 11 high-severity errors are confirmed, three by re-run:
- ER-H01: Probability/MC Ex. 2, triangle walk is aperiodic.
- ER-H02: MALA acceptance ratio reversed (variance 0.40 → 0.998 once fixed).
- ER-H03: SLT Cor. 4.2(i) universal consistency claim.
- ER-H04: boids separation sign.
- ER-H05: eigsh column order (accuracy 0.534 → 1.0).
- ER-H06: Image Synthesis E_ca sign.
- ER-H07: OT repair_1d.
- ER-H08: Advanced GNN over-squashing via λ_max (should be λ2 / Cheeger).
- ER-H09: Control Thm 2.2 masking ≠ exact conditioning (joint edit with GGM Prop 3.3).
- ER-H10: DL P2 Ex. 1 should be 2.2e18 FLOPs.
- ER-H11: Opt-AI Prop 1.2 proof.

Cross-page contradictions: ER-X01 DL status; ER-X02 14 badges; ER-X03 status vocabulary (CV Applications has four statuses); ER-X04 attention equivariance; ER-X05 LoRA/ICL pointers; ER-X06 GraphAF/DiGress misdescriptions; ER-X07 about 45 phantom pointers; ER-X08 UAT 'full proof'; ER-X09 five values that differ between pages; ER-X10 home sentences.

## 8. Capstones
- Y1.1 GraphRAG with a LinUCB router (Graph × LLM; O5 O3 O4)
- Y1.2 fleet dispatch with NL bookings (AI systems, logistics; O7 O4 O1)
- Y1.3 MIND news recommendation (both routes; O7 O4 O5)
- Y1.4 molecules from words (Graph × LLM; O2 O5 O6)
- Y1.5 CLEVR scene-graph QA (AI systems; O6 O5 O7)
- Y2.1 STaRK-Prime GraphRAG with conformal abstention (Graph × LLM, healthcare; O5 O3 O8)
- Y2.2 text-to-3D-molecule copilot (Graph × LLM; O2 O6 O8)
- Y2.3 voice-first 3D product search on ABO (AI systems; O6 O7 O3)
- Y2.4 NL dispatcher with PyVRP + E(2) routing (AI systems; O7 O4 O3)
- Y2.5 Elliptic fraud under attack and drift (both routes, finance; O8 O4 O7)

Vehicles: in Year 1, one repository with three graded work packages (Graph ML team project, RL 50% project, NLP capstone); in Year 2, the transverse project (W0 charter, W1–W6 build, W4 red-team swap).

## 9. Plan size and order of work
49 pages, 194 actions (87 must, 107 should), at most 6 per page.

Mandatory-page headroom at 320 words/h:
- ML ≈5,500
- DL P1 ≈3,600
- DL P2 ≈3,300
- RL ≈4,100
- Graph ML ≈2,500 (tight)
- NLP ≈5,300
- LLM ≈3,000
- GDL ≈3,400
- Refresher Stats ≈200 (Markov chains are paid for by moving measure theory to self-study)
- Advanced Topics ≈1,250 (paid for by recalls)

The larger additions go to self-study: DL P1 9.4, LLM 8.2b and 9.7, GDL ch8 bridges, ML 0.4 and 4.9.

Order of work:
1. Errors and joint contradiction edits.
2. Prerequisite repairs on the mandatory path.
3. O5/O6/O8/O2 gaps.
4. Project vehicles and the projects page.
5. notation.qmd, then the redundancy recalls.
6. Re-run check_progression, check_gates and cross_refs.