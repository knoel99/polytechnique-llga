# LLGA notes: prerequisite chain and progression

Lens: prerequisite chain and progression. Inputs: `the per-course reader records` (49 course records, 858 `assumed_knowledge` entries, `topics_taught`, `links_to_other_modules`, chapters with in-class / self-study flags), the curriculum tree and route tags (`data-p`) of `index.html`, and spot checks of the `.qmd` sources. This analysis is read-only. Finding ids (PR-xx) match the structured findings returned with this file.

Timeline order: L3 < pre-programme refreshers < Y1 P1 < Y1 P2 < Y1 P3 (research internship) < Y2 P1 < Y2 all-year (transverse project, ethics seminar) < Y2 P2 < Y2 P3.

## Findings index

| Id | Severity | Finding |
|---|---|---|
| PR-01 | high | "Deep Learning once, in P1 or P2" breaks for DL2 takers: DL2 assumes DL1, and also Optimization for AI from its own Choose-1 group |
| PR-02 | high | The mandatory Y1 P2 trio and the sys-route P1 options assume DL1 content that sys-route students get late (VAE) or never (attention) |
| PR-03 | high | Basic RAG is used in Y1 P2 (Graph ML final lab, NLP, RL) but first taught in Y2 P1 |
| PR-04 | high | Prompting and in-context learning are taught nowhere, and the pointers to "LLM ch. 3" are broken |
| PR-05 | high | Control in GenAI (Y2 P1) depends on Graph Generative Models (Y2 P2) and on LLM sessions later in the same period |
| PR-06 | high | Mandatory Geometric DL names optional courses (Shapes, Signal Processing, OT, Multimodal, Advanced GNN) as prerequisites |
| PR-07 | high | Y2 route modules name prerequisites their own route excludes (Graph-gen → OT, Adv-topics → Advanced DL, Speech → gllm-only modules) |
| PR-08 | medium | Diffusion (DDPM/CFG/FID) is assumed by mandatory Graph ML ch9 and GDL ch7–8, but DL1 has no diffusion |
| PR-09 | medium | Normalizing flows (Y2 P2 only) and flow matching (nowhere), although objective O2 names flows |
| PR-10 | medium | LoRA/PEFT and distillation have no mandatory home; the LLM page's self-pointer "ch. 6" is broken |
| PR-11 | medium | Group fairness metrics have no mandatory home; the ethics seminar points to an off-list course with no fairness content |
| PR-12 | medium | Differential privacy is first taught in a gllm-only P1 option, yet both-route Y2 P2 trust modules assume it |
| PR-13 | medium | Y2 P2 siblings declare each other as prerequisites (Security ↔ ESP-LLM ↔ MLOps; Adv-topics on all three) |
| PR-14 | medium | The information-theory and duality toolkit (entropy, CE, KL, Gibbs, KKT) has no in-class home on the mandatory path |
| PR-15 | medium | Markov chains and MCMC: stated sources are off-list or do not contain them |
| PR-16 | medium | Statistical model comparison and experimental protocol are assumed from Y1 P3 on, but sit only in self-study or route-excluded courses |
| PR-17 | medium | ViT and CLIP for vision-language models are taught only in options that both routes exclude |
| PR-18 | medium | Mutually exclusive Choose-1 siblings are cited as prerequisites or companions |
| PR-19 | medium | P1 options cite P2 modules as prerequisites (forward dependencies) |
| PR-20 | low | Orphan concepts used by several pages and taught nowhere in class (GPU memory hierarchy, ANN indexes, Hungarian algorithm, Kalman filter, n-gram LMs, MAML, activation patching) |
| PR-21 | low | Off-list courses still named as prerequisites (Image Synthesis, Responsible AI, DBMS, Graph-gen → SLT) |
| PR-22 | low | Broken chapter-level pointers (wrong module or chapter) |
| PR-23 | low | Refreshers (level 1) assume downstream content and measure theory |
| PR-24 | low | All-year M2 mandatory items and the M1 internship anchor on later or optional modules |
| PR-25 | low | Mandatory P2 pages defer core statements to optional or later M2 modules (1-WL/GIN, Bradley–Terry) |

## 0. How to read the tables

**Status of a teaching page**

| Code | Meaning |
|---|---|
| MAND | mandatory for everyone: Machine Learning (Y1 P1); RL, Graph ML, NLP (Y1 P2); LLM, Geometric DL (Y2 P1); internships, ethics seminar, transverse project |
| REF | pre-programme refresher listed in LLGA 1 – S1 (Statistics, Computer Science). Only part of each is taught in class (see section 1). |
| SUP | off-curriculum support (Refresher Neural Nets) |
| DL1 / DL2 | the "Deep Learning once, in P1 or P2" requirement: `m1p1-deep-learning` (DL1) or `m1p2-deep-learning-p2` (DL2, which is also a Y1 P2 Choose-1 option) |
| OPT-P1 | Y1 P1 Choose-3 option |
| OPT-P2 | Y1 P2 Choose-1 option. These options are mutually exclusive. |
| TBC | announced slot (Y1 P2 extras, Y2 P1 electives, Y2 P2 themes) |
| OFF | notes kept for reference, not in the 2026–27 lists |

**Verdicts**

| Verdict | Meaning |
|---|---|
| OK | the concept is taught earlier, in a page every student takes |
| SAME | taught in the same period; check the session order |
| LATER | taught after the page that uses it |
| OPT-ONLY | a mandatory page relies on an optional course |
| EXCL | the route preselects a course that excludes the source (Choose-1), or the route does not include the source |
| OFF | the source is an off-list course |
| NOWHERE | no page teaches it in class |
| WRONG | the cited page or chapter does not contain the concept |

## 1. What a student is guaranteed to have seen, by period and route

| Period | Everyone (mandatory) | Graph × LLM route (`gllm`) adds | AI systems route (`sys`) adds | Never guaranteed |
|---|---|---|---|---|
| Pre-programme | Refresher Statistics (in class: ch1, ch2, ch4, ch5; **self-study: ch3, ch6 tests/CIs, ch7 regression, ch8 Bayes, ch9 stats→ML incl. KL, ch10**); Refresher CS (in class: ch1, ch2, ch4, ch5; **self-study: ch3 git/Docker, ch6 sorting/DP, ch7 graph algorithms, ch8**) | Refresher NN (support) | Refresher NN (support) | Refresher in Computer Graphics (CSC_51438_EP, not covered by the notes) |
| Y1 P1 | Machine Learning | **Deep Learning (P1)**, Emerging ML, TDA | Signal Processing, Computer Vision, Shapes (**no DL in P1**) | Computer Animation; OFF: Prob./Monte Carlo, DBMS, SLT, Responsible AI |
| Y1 P2 | RL, Graph ML, NLP | Multimodal GenAI | **Deep Learning P2** (+ TBC: CV Applications, Real-time games) | OT, Optimization for AI, Advanced DL, Image Synthesis (no route preselects them); OFF: Statistics in Action, Social media |
| Y1 P3 | Research internship | | | |
| Y2 P1 | LLM, Geometric DL | Advanced GNN, Control in GenAI | — | Privacy & UQ, Boosting→Tabular |
| Y2 P2 | — (official list unpublished) | MLOps, Security, ESP-LLM, Graph Generative, Advanced Topics LLMs | MLOps, Security, ESP-LLM, Speech | |
| Y2 all-year / P3 | Transverse project, ethics seminar, humanities, languages and sports; final internship | | | |

Consequences:
1. Only the refreshers (their in-class part), ML, RL, Graph ML, NLP, LLM and GDL are safe prerequisites for everyone.
2. "Deep Learning" exists in two versions with different content. DL2 assumes DL1 (PR-01).
3. Advanced DL, OT, Optimization for AI and Image Synthesis are preselected by **no** route. Each one is excluded for a student who follows either route, because the route uses the Choose-1 slot for Multimodal (gllm) or DL2 (sys).

## 2. Concept dependency table: the problem rows (curated)

Every row was checked against `topics_taught` of all 49 records and, where marked, against the `.qmd` source. Rows with an OK verdict are kept only when they are a useful contrast.

### 2.1 Deep-learning foundations (O1)

| # | Concept | Used by (page · ch · period) | Page says it comes from | Actually taught (page · ch · period · status) | Verdict | Finding |
|---|---|---|---|---|---|---|
| C01 | Scaled dot-product / multi-head attention, transformer block | Graph ML ch5 GAT (s6), ch9–10 · NLP ch7 (s8–9) · LLM ch0/ch2 · Multimodal ch0/4/5 · CV ch9 DETR (P1) · CV-apps ch2/3/6 · Speech ch3–4 · Adv-GNN ch4–5 · Boosting ch5–6 · ESP ch1–3 · Refresher CS ch2 | DL1 ch6 | DL1 ch6 (Y1 P1, DL1) · Refresher NN ch6 single head (SUP) · **DL2 only recaps it** (ch0 recap box, `.qmd` l.183–192) | DL1-only. Missing for DL2 takers, i.e. the whole sys route | PR-01, PR-02 |
| C02 | CNN layer, receptive field, ResNet | CV ch9 (Y1 P1, sys) · Signal Proc. ch3/5/8 (Y1 P1, sys) · CV-apps ch0–3 · Multimodal ch0–1 · Adv DL ch3/5 · Security ch0–4 | DL1 ch4 | DL1 ch4 (P1) · DL2 ch1 (P2, s4) | EXCL on sys route in P1 (CV and SP come before any DL) | PR-02 |
| C03 | VAE / ELBO / reparameterization | Graph ML ch6 VGAE (s8), ch9.3 (s10) · TDA ch8 · Graph-gen ch3 | DL1 ch9 | DL1 ch9 · DL2 ch7.3 (**s11**) · Multimodal ch0–1 (s1–2) · ML ch7.2 EM via ELBO/KL (MAND) | DL2 takers see it 3 sessions after VGAE | PR-02 |
| C04 | Contrastive learning, choice of negatives | Graph ML ch6 ("Deep Learning module, contrastive", l.1118) | DL1 | not in DL1. Taught in Adv DL ch7 (OPT-P2), Multimodal ch5 (OPT-P2), NLP ch7 SBERT triplet (MAND, s9), Graph ML ch3 SGNS negatives (own) | WRONG | PR-02, PR-22 |
| C05 | LoRA / PEFT; distillation | LLM ch3 (l.386 "ch. 6: distillation, LoRA"), ch8.3, Ex. 3 · NLP ch7 (l.859 → MLOps ch7) · Multimodal ch6–7/Ex.14 · ESP ch7–8 · Speech ch11 · Adv-topics ch10 · Emerging ML ch1/3 | LLM ch6 (self-link); MLOps ch7 (Y2 P2); DL1 §7.3 | DL1 ch7 (P1, DL1; **not in DL2**) · MLOps ch7 param count (Y2 P2, TBC). Distillation: Adv DL ch3, CV-apps ch8, Responsible AI ch3 (OFF) | NO MANDATORY HOME. LLM self-link WRONG | PR-10 |
| C06 | Adam/AdamW, non-convex SGD rate, Nesterov, minimax | DL2 ch0, ch2, ch7, ch8 | Optimization for AI Thm 5.5, ch2–3, 5, 8, 10–11 | DL1 ch3; Refresher NN ch5; ML ch0 (SGD); OptAI (same Choose-1 group as DL2) | EXCL (sibling) | PR-01, PR-18 |
| C07 | GPU memory hierarchy (HBM vs SRAM, bandwidth) | DL1 ch0.3/2.2/6.3/8.3 · DL2 ch1–6 · LLM ch2 FlashAttention · Adv-topics ch3 | LLM: "cf. Signal Processing module" (l.309); others: not stated | nowhere as a concept (DL2 ch6 roofline gives arithmetic intensity only); Signal Processing has none | NOWHERE + WRONG | PR-20 |
| C08 | ViT patch embedding | LLM ch8 (VLM) · Multimodal ch4 DiT, ch5 CLIP encoder, ch8.4 · CV-apps ch3 SAM | Adv DL ch4 | Adv DL ch4 only (OPT-P2, no route) | EXCL on both routes | PR-17 |
| C09 | CLIP / InfoNCE | LLM ch8 · Adv DL ch7.2/10.6 · CV ch9 note · DBMS ch9 | Multimodal ch5 | Multimodal ch5 (OPT-P2, gllm) | gllm only. Adv DL is its Choose-1 sibling (EXCL) | PR-17, PR-18 |
| C10 | FlashAttention / online softmax | DL2 ch5–6/Ex.8 · Adv-topics ch3/Ex.7 | LLM ch2 (Y2 P1) / not stated | DL1 ch6.3 · LLM ch2 | LATER for DL2 | PR-01 |

### 2.2 Generative modelling (O2)

| # | Concept | Used by | Page says | Actually taught | Verdict | Finding |
|---|---|---|---|---|---|---|
| C11 | DDPM, ε-prediction, classifier-free guidance | **Graph ML ch9.5–9.7 (MAND, s11)** · **GDL ch7–8 (MAND)** · Adv DL ch10.4 · Control ch7 · Graph-gen ch5/8 · Speech ch7 · Boosting ch8 · Adv-GNN ch9 | Multimodal ch3–4. Boosting cites Image Synthesis, which is WRONG | Multimodal ch3–4 (gllm, s5–8) · DL2 ch7.3 (sys, s11) · **not in DL1** (ch9 = AE/VAE/GAN) | OPT-ONLY for two mandatory pages; missing for DL1 + OT/OptAI/AdvDL/ImageSynth students | PR-08 |
| C12 | FID / Fréchet distance of Gaussians | Graph ML ch9.6 FCD (MAND) · Graph-gen ch0/6 · Control ch8–9 | Multimodal ch7 | Multimodal ch2/7 (gllm) · Signal Proc. ch8 (P1 sys) · OT ch2 (no route) | OPT-ONLY | PR-08 |
| C13 | Normalizing flows (change of variables, coupling) | Control ch0/ch8 ("assumed acquired": GraphAF) · Speech ch7 VITS (l.495 → Graph-gen ch4) · Multimodal ch4 probability-flow ODE | Graph-gen ch4 | Graph-gen ch4 only (Y2 P2, gllm, TBC) | LATER (Control) / EXCL (Speech, sys) | PR-05, PR-07, PR-09 |
| C14 | Flow matching | Multimodal ch8.3 (π0 action expert) · Speech ch7 Voicebox (objective never written) | not stated | **nowhere** | NOWHERE | PR-09 |
| C15 | SDE, Brownian motion, reverse-time dynamics | Multimodal ch4 | not stated | Prob./MC ch9 (OFF) | OFF | PR-09 |
| C16 | GAN, optimal discriminator | OT ch4, RL ch6 GAIL, Speech ch6, Boosting ch8 | DL1 ch9 / Multimodal ch2 | DL1 ch9 · DL2 ch7.3 · Multimodal ch2 | OK (either DL) | — |
| C17 | Wasserstein, KR duality, W2–Bures | Multimodal ch2/7/Ex.9 · DL1 ch7.2/9.3 · TDA ch5/7/8 · Signal Proc. ch8–9 · RL ch6 (distributional) · Prob./MC ch9 | OT ch1–2 | OT ch1–2 (OPT-P2, no route) · Signal Proc. ch8 (1D W2, Gaussian W2; P1 sys) · Multimodal ch2 (WGAN, FID-Bures) | LATER (P1 pages) / EXCL (Multimodal: same Choose-1) | PR-18, PR-19 |
| C18 | Gromov–Wasserstein | Graph ML ch9.6 · **GDL ch4/ch8/Ex.12 (MAND)** · Graph-gen ch6/ch10 (stated prerequisite) | OT ch5 | OT ch5 only (OPT-P2, no route) | OPT-ONLY / EXCL on gllm (Graph-gen) | PR-06, PR-07 |
| C19 | Classical graph generators (GraphRNN, NeVAE, DiGress), MMD/FCD | Control ch0/ch8 | Graph-gen ch3–6 (Y2 P2) | **Graph ML ch9 (MAND, Y1 P2)** except GraphAF | WRONG target (LATER) | PR-05 |

### 2.3 Mathematical and statistical toolkit (O1)

| # | Concept | Used by | Page says | Actually taught | Verdict | Finding |
|---|---|---|---|---|---|---|
| C20 | Entropy, cross-entropy, KL, Gibbs inequality, forward/reverse KL | ML ch7.2 (KL ≥ 0 asserted, l.1185) · DL1 ch9 · RL ch4–6 · LLM ch5 (closed-form RLHF optimum) · Control ch5/9 · Security ch4 TRADES · Adv DL ch3/7/9 · DL2 ch7 · Privacy ch8 | not stated (all) | Refresher Stats ch9 (**self-study**, l.1795) · OT ch0, Multimodal ch0 (options) | no in-class home on the mandatory path | PR-14 |
| C21 | Lagrangian duality, KKT, LP duality | ML ch3.2 and Ex. 2 (points to ch0, which lacks it) · RL ch1 occupancy LP, ch6 CMDP · LLM ch3 Chinchilla · Control ch5 · OT ch3 | ML ch0 (WRONG) / not stated | ML ch3 SVM dual (inline) · OptAI ch0, OT ch0 (options) · Responsible AI ch0 (OFF) | weak home | PR-14 |
| C22 | Finite Markov chains, stationarity, ergodicity | RL ch0–3 · NLP ch5/6/8.1 · Graph ML ch0 Prop 0.6 · Multimodal ch0/3 · OptAI ch11 | RL → Prob./MC (OFF); NLP → Refresher CS (WRONG); Graph ML, Multimodal → Refresher Stats (WRONG: only "Markov's inequality", l.232/492) | RL ch0 recap (s1) · Graph ML ch0 random walks (s1) · Prob./MC ch7 (OFF) | OFF / WRONG | PR-15 |
| C23 | MCMC, Gibbs sampling | NLP ch5 collapsed Gibbs (s6) · Graph ML ch9.2 | Refresher Stats | Prob./MC ch8 only (OFF) | OFF | PR-15 |
| C24 | Hypothesis tests, CIs, power, paired comparisons, multiple testing | LLM ch9 · Control ch6 · ESP ch8–10 · Security ch5/8 · MLOps ch2 · Adv-GNN ch1 · Boosting ch9/Ex.7 · Adv DL ch1 · Privacy ch0/8/9 · Graph-gen ch6 · Real-time games ch9 | Refresher Stats ch6; Statistics in Action (Privacy); not stated (LLM, MLOps, Boosting) | Refresher Stats ch6 (**self-study ≈ 5 h**) · Adv DL ch1 (no route) · Statistics in Action (OFF) | self-study only | PR-16 |
| C25 | Experimental protocol (baseline, seeds, ablations) | **M1 research internship (MAND)** · Adv-GNN ch1 · Boosting ch9 · LLM ch9 | not stated | Adv DL ch1 Def 1.1 (no route) · Refresher NN ch5 hygiene (SUP) · DL1 ch8, DL2 ch0 debugging · ML ch4 nested CV/leakage | partial | PR-16 |
| C26 | Hoeffding inequality | Real-time games ch0/6 · Adv-topics ch1 · Privacy ch0 · MLOps ch2 | Refresher Stats (games, adv-topics): WRONG; ML ch0 (others) | ML ch0 Thm 0.3 (MAND) · SLT ch2 (OFF) | WRONG in 2 pages | PR-22 |
| C27 | Bootstrap | ML ch6.2 · TDA ch7 · Graph-gen ch6 | Refresher Stats ch4 | Refresher Stats ch4 (in class, s3) | OK | — |
| C28 | Martingales, de Finetti | Graph-gen ch1 Prop 1.3 | Refresher Stats | RL ch0 (Robbins–Siegmund), SLT ch0 (OFF). Not in Refresher Stats | WRONG | PR-22 |

### 2.4 LLMs and Graph × LLM (O3, O5)

| # | Concept | Used by | Page says | Actually taught | Verdict | Finding |
|---|---|---|---|---|---|---|
| C29 | Basic RAG pipeline (chunk → embed → retrieve → prompt) | **Graph ML ch10 + final lab "vector RAG vs GraphRAG" (MAND, s12)** · **NLP ch3/8/9 (MAND, s12)** · **RL ch7 (MAND, s12)** · Real-time games ch9 · DBMS intro | LLM ch7 (Y2 P1) | LLM ch7 (Y2 P1, s7) | LATER by one year | PR-03 |
| C30 | Prompting, in-context learning, few-shot, CoT | NLP ch3 (l.547), ch8 · Graph ML ch10.2 pseudo-code prompting · RL ch7 · Boosting ch6 Def 6.1 · ESP ch2 Ex 2.2 · Privacy ch11 · LLM ch5 self-consistency | LLM (ch3) | **nowhere**: the LLM page has no section on prompting, few-shot or ICL. Adv-topics ch2 has CoT (Y2 P2, TBC) | NOWHERE + WRONG | PR-04 |
| C31 | ANN indexes (IVF, HNSW, PQ), vector DB | NLP ch8.5 · LLM ch7 (FAISS/HNSW table, l.646) · CV ch4 | DBMS ch9 (CV); not stated | DBMS ch9 (OFF) · CV ch4 kd-tree/LSH (P1 sys) | OFF / NOWHERE on the mandatory path | PR-20 |
| C32 | n-gram language models with smoothing | Speech ch1 · LLM ch0 ("from n-grams") | NLP ch2 (WRONG) | NLP ch1.3 has n-grams as features only | NOWHERE | PR-20 |
| C33 | Relation extraction / KG construction | LLM ch7 | NLP ch6, ch9 (ch9 = self-study research) | NLP ch6 NER + extractor lab · Graph ML ch10.1 extraction pipeline | weak target | PR-22 |
| C34 | Bradley–Terry reward model | RL ch6 (l.1280) | LLM (Y2 P1) | LLM ch5 | LATER (forward reference) | PR-25 |
| C35 | Decoding (temperature, top-k, top-p) | Control ch0 (s1) | LLM ch6 | LLM ch6 (**s6**) · DL2 ch1 (sys) | SAME period, 5 sessions later | PR-05 |
| C36 | Function calling / JSON output | Control ch3 (s3) | LLM ch8 | LLM ch8.1 (**s7**) · RL ch7 (descriptive) | SAME period, later session | PR-05 |
| C37 | RLHF, DPO | Control ch5 (s4) | LLM ch4–5 | LLM ch5 (s4–5) | SAME week | PR-05 |
| C38 | Prompt injection, jailbreaks | Control ch10 (Y2 P1) · Security ch9 · MLOps ch5/8/9 · Adv-topics ch9 | ESP-LLM (Y2 P2) | **LLM ch9 (MAND, Y2 P1, s8)** · ESP ch5 (Y2 P2) | WRONG target (later sibling, though a mandatory source exists) | PR-05, PR-13 |
| C39 | MoE, Switch load-balancing loss | Adv-topics ch5 | Adv DL ch6 | Adv DL ch6 (EXCL on gllm) · **LLM ch2 (MAND)** | WRONG prerequisite | PR-07 |
| C40 | GraphRAG (extraction, Leiden, map-reduce) | LLM ch7/8 · Adv-GNN ch7–9 · MLOps ch6 · Adv-topics ch4/8 · RL ch7 | Graph ML ch10 | Graph ML ch10 (MAND, s12) | OK (RL ch7 is the same week) | — |
| C41 | PPO / policy gradient / GAE | LLM ch5 · Adv-topics ch2 · Control ch5 | RL ch5 | RL ch3/ch5 (MAND) | OK | — |
| C42 | BPE / WordPiece / Unigram | LLM ch1 · Control ch3 · Multimodal ch6 | NLP ch1 | NLP ch1 (MAND) · DL1 ch6.5 | OK | — |

### 2.5 Graph-structured data and geometry (O4, O6)

| # | Concept | Used by | Page says | Actually taught | Verdict | Finding |
|---|---|---|---|---|---|---|
| C43 | Graph Laplacian, λ2 (spectral gap), spectral radius | Emerging ML ch2 Thm 2.6/Ex 7 (P1, l.430) · TDA ch0 (P1) · CV ch8 normalized cuts (P1) · ML ch5/7.3 (P1) · Signal Proc. ch8 (P1) | Graph ML ch4 (Y1 P2) | Graph ML ch0/ch4 (P2) · Refresher CS ch2 normalization D^-1/2AD^-1/2 (in class) · Shapes ch8 Fiedler (P1 sys) | LATER | PR-19 |
| C44 | Cliques, components, cyclomatic number, MST/union-find | TDA ch1–3, Ex 6 | Graph ML ch0 (Y1 P2, and absent there) / not stated | Refresher CS ch7 (self-study: BFS/DFS, MST, union-find); TDA ch3 proves β1 itself | LATER + WRONG | PR-19 |
| C45 | MPNN ≤ 1-WL, GIN | Graph ML ch2/5/8 (l.542, 840, 956) · TDA ch8 · Graph-gen ch0 | Adv-GNN ch2 (Y2 P1, gllm TBC) | Adv-GNN ch2 only; Graph ML ch2 has the WL kernel | LATER, optional | PR-25 |
| C46 | Laplacian eigenmaps / spectral PE | GDL ch3 (s4) | Adv-GNN ch4 (s5) | Graph ML ch4 spectral clustering/Fiedler (MAND) · Adv-GNN ch4 | SAME period + optional | PR-06 |
| C47 | Graph transformers / GPS | GDL ch6 (MAND) · Graph-gen ch4/5 | Adv-GNN ch5 | Adv-GNN ch5 only (gllm TBC) | OPT-ONLY for GDL | PR-06 |
| C48 | Triangle-mesh data structures (half-edge, manifoldness) | GDL ch1/ch5 (MAND) · Image Synthesis ch3/5/6 · Animation ch4/7 | Shapes (GDL l.105) | Shapes ch1 (P1, sys) | OPT-ONLY. EXCL on gllm | PR-06 |
| C49 | Fourier transform, convolution theorem, heat = low-pass | GDL ch0/2/5 (MAND, l.165) · Graph ML ch4 Def 4.1 (MAND) · Adv-topics ch3/6 · CV ch0–2 | Signal Processing | Signal Proc. ch2–5 (P1 sys) · CV ch2 (P1 sys) | OPT-ONLY. EXCL on gllm | PR-06, PR-07 |
| C50 | GCN on citation graphs | Security ch9 | Adv-GNN ch7 | Graph ML ch5 (MAND) | WRONG (optional target; sys students lack Adv-GNN) | PR-22 |
| C51 | E(n) equivariance, EGNN | Adv-GNN ch4/8 · Graph-gen ch5/8 | GDL ch7 | GDL ch7 (MAND Y2 P1) · Graph ML ch8.2 | OK (Adv-GNN concurrent) | — |
| C52 | ER/SBM/graphons | Graph-gen ch0–1 · Social media | Graph ML ch9 | Graph ML ch9 (MAND) | OK | — |
| C53 | Hungarian algorithm / min-cost assignment | Graph ML ch9.3 · Graph-gen ch3/9 · CV-apps ch2/ch5 · Real-time games ch4/8 · CV ch9 DETR | OT ch1–2 / L3 / CV-apps / not stated | **nowhere** (Refresher CS ch7 has bipartite matching by max-flow, self-study) | NOWHERE | PR-20 |
| C54 | Kalman filter | CV-apps ch5 · CV ch10 · Refresher Stats ch3/8 | Signal Processing | **nowhere** (Signal Proc. ch7 defers it "to downstream modules") | NOWHERE + WRONG | PR-20 |

### 2.6 Trustworthy AI (O8)

| # | Concept | Used by | Page says | Actually taught | Verdict | Finding |
|---|---|---|---|---|---|---|
| C55 | Group fairness metrics (DP, EO, calibration by group) | **Ethics seminar (MAND)** · MLOps ch2/5 · CV-apps ch9.2/Ex.11 · Adv-GNN ch7 · OptAI ch8/11 | Responsible AI (ethics: OFF, and no fairness content); Emerging ML ch6; ML (absent); OT | Emerging ML ch6 (P1 gllm) · OT ch6 (no route) · OptAI ch8 (no route) | OPT-ONLY / WRONG | PR-11 |
| C56 | Differential privacy: definition, mechanisms, composition, DP-SGD | Privacy ch0 · **ESP ch8 (both routes)** · **Security ch5/7/8 (both routes)** · Graph-gen ch8 · Boosting ch8 · Adv-GNN ch7 | Emerging ML ch5 | Emerging ML ch5 (P1, **gllm only**) · Privacy & UQ ch1–4 (Y2 P1, **no route**) · Adv-GNN ch7 (edge/node DP) | EXCL for sys students | PR-12 |
| C57 | Rényi DP / moments accountant | ESP ch8, Ex 9 | not stated | Privacy & UQ ch3 (no route) · Emerging ML ch5 (statement) | option | PR-12 |
| C58 | Membership inference | Boosting ch8 (Y2 P1) · Graph-gen ch8/10 | Security ch8 (Y2 P2) | Emerging ML ch5 shadow models (P1 gllm) · Privacy ch5 (Y2 P1) · ESP ch8 / Security ch8 (Y2 P2) | LATER (Boosting) | PR-12 |
| C59 | LIME / KernelSHAP | ESP ch4 ("M1 recap — feature attributions", l.343) | M1 | no M1 page: grep finds no SHAP/LIME in `m1*` pages. Nearest: ML ch4 permutation importance, Emerging ML ch6 Shapley data valuation | WRONG (phantom recap) | PR-22 |
| C60 | Adversarial examples / adversarial training | CV-apps ch9.1 · OptAI ch8 | ML (absent) | Adv DL §4.5 (no route) · DL2 ch7.1 (sys) · Security ch2–4 (Y2 P2) | WRONG | PR-22 |
| C61 | Attack taxonomy, threat model | ESP ch5–6 (l.113 "assumed") | Security (Y2 P2 sibling) | Security ch1 (Y2 P2) · ESP ch0 | sibling cycle | PR-13 |
| C62 | CI/CD, monitoring, guardrails | ESP ch6/ch10 · Security ch7/ch10 | MLOps (Y2 P2 sibling) | MLOps ch2/5/8/9 | sibling cycle | PR-13 |

### 2.7 Systems and practice (O7)

| # | Concept | Used by | Page says | Actually taught | Verdict | Finding |
|---|---|---|---|---|---|---|
| C63 | Tensor parallelism | MLOps ch3 | Emerging ML ch2 | DL2 ch2 Megatron (sys). Emerging ML ch2 covers DP-SGD, all-reduce and gossip only | WRONG | PR-22 |
| C64 | KS two-sample test; MMD | MLOps ch5 | Refresher Stats (KS); ML (MMD) | KS: nowhere. MMD: Graph ML ch9.6 structural MMD (MAND), Graph-gen ch6 (Y2 P2); DL1 and OT only use it | WRONG | PR-22 |
| C65 | LLM serving: continuous batching, KV cache, PagedAttention | MLOps ch3 · Adv-topics ch5/7/10 · **Transverse project (all year)** | LLM ch6 / MLOps (transverse: not stated) | LLM ch6 (MAND Y2 P1) · DL2 ch5 | OK, but the transverse page links nothing | PR-24 |
| C66 | Containers, git | MLOps ch1–3 | Refresher CS ch3 | Refresher CS ch3 (self-study) | OK (self-study) | — |
| C67 | SQL / relational model | Boosting ch7 text-to-SQL | not stated | DBMS ch2 (OFF) | OFF | PR-21 |

## 3. Module-level prerequisite statements that break the timeline or the routes

| Consumer (period, status) | Stated prerequisite | Problem | Change to | Finding |
|---|---|---|---|---|
| DL2 (Y1 P2, DL-once option) | DL1 "whose foundation it assumes" (`.qmd` l.122); OptAI Thm 5.5 etc. | DL2 replaces DL1; OptAI is a Choose-1 sibling. The official sheet asks only for "basics in ML, Python" | ML + Refresher NN; self-contained ch0 | PR-01 |
| Graph ML, NLP, RL (Y1 P2, MAND) | DL1 (Graph ML l.120: "the attention mechanism is presented there") | sys/DL2 students take DL in parallel, and DL2 never defines attention | "DL1, or DL2 in parallel (read ch0 first)" + review boxes | PR-02 |
| CV (Y1 P1, sys) | DL1 ch4/6/7 for ch9 | the sys route has no DL in P1 | CNN box in ch9; route note | PR-02 |
| RL (Y1 P2, MAND) | Prob./Monte Carlo for Markov chains (l.116) | OFF-list | Refresher Stats (new §) + RL ch0 | PR-15 |
| GDL (Y2 P1, MAND) | Shapes + Graph ML (l.105); Signal Proc. (l.165); OT ch5; Multimodal ch3; Adv-GNN ch4–5 | 4 of the 6 are optional; Shapes and Signal Proc. are sys-only, so gllm students have neither | Graph ML + DL; ch0 boxes | PR-06 |
| Control (Y2 P1, gllm) | LLM (same period); Graph-gen (Y2 P2) "assumed acquired" | LATER + circular (Graph-gen l.182 says the reverse) | Graph ML ch9; self-contained ch0 | PR-05 |
| Graph-gen (Y2 P2, gllm) | Graph ML ch9, Adv-GNN, **OT** (l.105) + Multimodal (in text) | OT and Multimodal are mutually exclusive; the gllm route picks Multimodal | OT → optional + GW box | PR-07 |
| Adv-topics LLMs (Y2 P2, gllm) | LLM + **Advanced DL** (l.107) | Adv DL is EXCL on gllm (and on sys) | LLM ch2 (MoE) | PR-07 |
| Speech (Y2 P2, sys) | Signal Proc. + LLM (OK), but ch0/ch7/ch9 lean on Multimodal, Graph-gen, Control | all three are gllm-only | DL2 ch7.3 + own boxes | PR-07 |
| Privacy & UQ (Y2 P1) | Emerging ML ch5 + **Statistics in Action** "assumed acquired" (l.107) | OFF-list; Emerging ML is gllm-only | Refresher Stats ch4/6 + ML §4.x | PR-16 |
| Security (Y2 P2, both routes) | ESP-LLM listed in ch0 "Prerequisites" (l.172) but called downstream (l.107); Adv-GNN ch7 | circular; Adv-GNN is not on sys | co-requisite; Graph ML ch5 | PR-13, PR-22 |
| ESP-LLM (Y2 P2, both routes) | Security taxonomy "assumed" (l.113), MLOps ch2/5/8/9, Emerging ML ch5 DP | circular; DP source gllm-only | co-requisite; DP box | PR-12, PR-13 |
| Image Synthesis (Y1 P2) | Prob./Monte Carlo "main P1 feeder" | OFF-list | Refresher Stats ch4 + own ch0/ch7 | PR-21 |
| Responsible AI (OFF, now Y1 P1) | OptAI as "upstream toolbox", DL2 ch1–2 | both are Y1 P2, so the dependency runs backwards in time | ML ch0/ch3, Emerging ML ch7 | PR-21 |
| Ethics seminar (Y2, MAND) | "possible responsible modules in P2" (l.63) | none exists in 2026–27; Responsible AI has no fairness content | ML §4.x (new) + OT ch6 / Emerging ML ch6 | PR-11 |
| Multimodal ↔ OT; Adv DL → Multimodal/Image Synth.; OptAI → OT/DL2 | "take alongside", proofs deferred to sibling | same Choose-1 group | self-contained boxes | PR-18 |

## 4. Same-period sequencing checks (session numbers from each page's session plan)

| Consumer (session) | Needs | Provider (session) | Status |
|---|---|---|---|
| Graph ML s6 (GAT, ch5) | attention | DL1 ch6 (P1) / DL2 never defines it (s5 has only a transformer recap) | ✗ for DL2 takers |
| Graph ML s8 (VGAE, ch6) | VAE/ELBO | DL2 ch7.3 (**s11**); Multimodal ch1 (s2); ML ch7.2 (P1) | ✗ for DL2 takers (fixable via ML ch7.2) |
| Graph ML s10–11 (GraphVAE, DiGress) | ELBO, DDPM, FID | Multimodal s5–6 ✓ (gllm); DL2 s11 (same week); none for others | ✗ for DL1 + non-Multimodal |
| Graph ML s4 (skip-gram, ch3) | word2vec | NLP s5 | ✓ Graph ML derives SGNS itself |
| Graph ML s12 (final lab: vector RAG vs GraphRAG) | basic RAG | NLP s12 (same week, deferred to M2); LLM ch7 (Y2) | ✗ |
| RL s12 (agents, memory/RAG) | RAG, GraphRAG | Graph ML s12, NLP s12 | ✗ same week |
| NLP s1 (Unigram tokenizer: Viterbi segmentation) | DP | RL ch2 (s3); Refresher CS ch6 (self-study) | ~ (relink to Refresher CS ch6) |
| NLP s6 (LDA collapsed Gibbs) | Markov chains/MCMC | RL ch0 (s1) ✓ chains; MCMC: none on-list | ✗ MCMC |
| RL s7–9 (neural policies, DQN) | NN training | DL2 s1–2 ✓; DL2 covers DQN/REINFORCE again at s10 (overlap) | ~ |
| Control s1 (ch0 decoding) | temperature/top-k/top-p | LLM s6 | ✗ |
| Control s3 (ch3 JSON / function calling) | function calling | LLM s7 | ✗ |
| Control s4 (ch5 DPO as exponential guidance) | RLHF/DPO | LLM s4–5 | ~ same week |
| Control s7 (ch8 graph generators) | GraphRNN/NeVAE/GraphAF/DiGress | Graph-gen (Y2 P2) | ✗ (Graph ML ch9 would be ✓) |
| GDL s4 (ch3 LapEig) | spectral PE | Adv-GNN s5 | ✗ (Graph ML ch4 would be ✓) |
| GDL s7 (ch6 GPS) | graph transformers | Adv-GNN s6 | ✓ only if Adv-GNN is taken |
| Security s8 (ch9 LLM attacks) | jailbreak/injection | ESP s5 ✓ if taken; LLM ch9 (Y2 P1) ✓ | relink to LLM ch9 |
| ESP s5–6 (attacks, defenses) | attack taxonomy | Security s1 ✓ if taken | co-requisite |
| MLOps s5 (monitoring, injection) | injection, MIA | ESP s5–7 | ~ |

## 5. Route audit: dependencies on courses the route excludes

**Graph × LLM route** (DL1, Emerging ML, TDA → Multimodal → LLM, GDL, Adv-GNN, Control → MLOps, Security, ESP, Graph-gen, Adv-topics)
- Multimodal ← OT (KR/W2 proofs), Adv DL (ViT), Image Synthesis (NeRF), Signal Proc. (STFT, ch8.2): all four are excluded.
- Emerging ML (P1) ← Graph ML λ2 (P2), OT fairness/barycenters (P2, excluded), RL agents (P2).
- TDA (P1) ← Graph ML ch0/2/4/5 (P2), OT (P2, excluded).
- GDL (MAND) ← Shapes, Signal Proc. (excluded on this route), OT (excluded).
- LLM (MAND) ch8 ← Adv DL ViT (excluded).
- Graph-gen ← OT (excluded). Adv-topics ← Adv DL, Signal Proc. (excluded).
- Control ← Graph-gen (LATER).

**AI systems route** (SP, CV, Shapes → DL2 (+CV-apps, Real-time games) → LLM, GDL → MLOps, Security, ESP, Speech)
- SP and CV (P1) ← DL1 (no DL in P1 on this route); CV ← Graph ML ch4 (P2), Multimodal, OT (excluded), DBMS (OFF).
- DL2 ← DL1 (excluded by construction), OptAI, Multimodal (Choose-1 siblings), Emerging ML (not on route), Responsible AI (OFF), LLM FlashAttention (LATER).
- Graph ML, NLP, RL (MAND) ← DL1 attention/VAE/LoRA (DL2 in parallel, attention never defined); Graph ML ← Multimodal DDPM/FID (excluded; DL2 ch7.3 substitutes for DDPM only).
- LLM (MAND) ← Adv DL ViT, Multimodal CLIP (excluded), DL1 ch6 attention.
- GDL ← OT, Multimodal (excluded; DL2 ch7.3 substitutes), Adv-GNN (not on route).
- MLOps ← Emerging ML ch2/ch6 (not on route; DL2 ch2 substitutes for tensor parallelism).
- Security, ESP ← Emerging ML ch4/ch5 DP and Byzantine (not on route), Privacy & UQ (no route), Adv-GNN ch7 (not on route).
- Speech ← Multimodal, Graph-gen, Control (all gllm-only), DL1 attention.

## 6. Difficulty jumps

| Where | Jump | Finding |
|---|---|---|
| DL2 as the only DL course (sys route) | the official sheet asks for "basics in ML, Python"; the page addresses "a deep learning engineer who already trains models", recaps the foundations in one box, then goes to ZeRO, roofline and MSDA lower bounds | PR-01 |
| Refresher Stats (12 h, level 1) | in-class ch1/2/4 use Borel sets, pushforward, Tonelli–Fubini, Vitali set, Lévy continuity, Borel–Cantelli; self-study ch9 assumes SLT (OFF), VAE/diffusion, Kalman, GPs | PR-23 |
| Refresher CS (level 1) | examples use GNN message passing / PyG, attention, LLM decoding/BPE, HMM/Viterbi, Bellman, PyTorch nn.Module, all taught later | PR-23 |
| GDL for gllm students | 24 h of discrete differential geometry, FEM, functional maps and DiffusionNet, with neither Shapes nor Signal Processing behind them; ch0 is the only bridge | PR-06 |
| Control ch0 (level 1) | its "reminders" presuppose LLM sessions 4–7 of the same period and a Y2 P2 module | PR-05 |
| Speech ch7 (sys) | flows, flow matching, diffusion, VAE+flow+GAN (VITS) in one chapter, with sources only on the other route | PR-07, PR-09 |
| Graph ML ch9 (s10–11, level 3) | graphons, GraphVAE ELBO with matching and discrete diffusion, built on a continuous-diffusion background that a DL1 + OT/OptAI/AdvDL/ImageSynth student never received | PR-08 |

## 7. Counts over all 858 assumed-knowledge entries (mechanical, from the stated source)

The mechanical classification in Appendix B uses only the source the page itself names, and keeps the most favourable verdict when several sources are named:
343 "not stated" (checked by hand above where they matter), 30 "L3", 7 unnamed; 179 OK, 28 OK on the consumer's route, 7 partly on route; 116 same period; **55 later**; 26 DL1-only (seen by a mandatory or both-route page); 15 same Choose-1 group (mutually exclusive); 13 option-only for a mandatory page; 11 option not guaranteed; 8 off-route option; 13 excluded on the consumer's own route; 7 off-list.


## Appendix A. Module-level prerequisite links in the records (mechanical)

Each row is a link whose record note mentions "prerequisite" (explicit, implicit or de facto; a few are "related" links that discuss a missing prerequisite) and that is not tagged as downstream. The timing verdict compares the period of the linked module with the consumer's period, its status and the consumer's route.

| Consumer (period · status · route) | Linked prerequisite (period · status) | Verdict | Record note (truncated) |
|---|---|---|---|
| `m1p1-refresher-statistics` (pre · REF · —) | `m1p1-refresher-cs` (pre · REF) | SAME | prerequisite (cited for arrays/NumPy) |
| `m1p1-refresher-neural-nets` (pre · SUP · —) | `m1p1-refresher-cs` (pre · REF) | SAME | prerequisite / remediation for implementation foundations (positioning task 1, refs) |
| `m1p1-refresher-neural-nets` (pre · SUP · —) | `m1p1-refresher-statistics` (pre · REF) | SAME | prerequisite / remediation for evaluation concepts (positioning task 3, ch7) |
| `m1p1-machine-learning` (Y1P1 · MAND · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (concentration, estimation, distributions; cited for Student CIs) |
| `m1p1-machine-learning` (Y1P1 · MAND · —) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (Python, NumPy, complexity; streaming engineering) |
| `m1p1-deep-learning` (Y1P1 · DL1 · gllm) | `m1p1-machine-learning` (Y1P1 · MAND) | SAME | prerequisite / twin: official blocks 1-5 (paradigms, pipelines, naive Bayes, trees, clustering, kernels/SVM, ensembles, feature and model selection) are handed to it with |
| `m1p1-deep-learning` (Y1P1 · DL1 · gllm) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (CLT in ch0) |
| `m1p1-deep-learning` (Y1P1 · DL1 · gllm) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (NumPy for the labs) |
| `m1p1-signal-processing` (Y1P1 · OPT-P1 · sys) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (probability for random signals) |
| `m1p1-signal-processing` (Y1P1 · OPT-P1 · sys) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (NumPy for labs) |
| `m1p1-signal-processing` (Y1P1 · OPT-P1 · sys) | `m1p1-computer-vision` (Y1P1 · OPT-P1) | SAME | related/downstream (filtering, convolution and sampling; the CV page treats this module as an internal prerequisite) |
| `m1p1-emerging-ml` (Y1P1 · OPT-P1 · gllm) | `m1p1-machine-learning` (Y1P1 · MAND) | SAME | prerequisite (optimization foundation, SGD analysis ch0 0.2, generalization; cited 'Where this course fits' and 'How to study') |
| `m1p1-emerging-ml` (Y1P1 · OPT-P1 · gllm) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (CLT for batch variance, ch0 recap) |
| `m1p1-emerging-ml` (Y1P1 · OPT-P1 · gllm) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (named upstream refresher) |
| `m1p1-computer-animation` (Y1P1 · OPT-P1 · —) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (programming/algorithms). Cited for its graphs chapter (A*/Dijkstra, ch9) and for a 'spatial data structures chapter' that does not exist. |
| `m1p1-computer-animation` (Y1P1 · OPT-P1 · —) | `m1p1-deep-learning` (Y1P1 · DL1) | SAME | implicit prerequisite for learned skinning and learned motion ('neural networks seen in P1'). Backpropagation is its ch2 and RNN/LSTM its ch5. |
| `m1p1-computer-vision` (Y1P1 · OPT-P1 · sys) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | SAME | prerequisite (the page calls it an internal prerequisite; cites ch. 1, 3, 4 for convolution, the Fourier transform and Shannon) |
| `m1p1-computer-vision` (Y1P1 · OPT-P1 · sys) | `m1p1-deep-learning` (Y1P1 · DL1) | SAME | prerequisite for ch9 (cites ch. 4 CNN/ResNet, ch. 6 attention/DETR, ch. 7 transfer learning) |
| `m1p1-computer-vision` (Y1P1 · OPT-P1 · sys) | `m1p1-machine-learning` (Y1P1 · MAND) | SAME | prerequisite (cites ch. 2 least squares, ch. 7 k-means) |
| `m1p1-computer-vision` (Y1P1 · OPT-P1 · sys) | `m1p2-deep-learning-p2` (Y1P2 · DL2) | LATER | related: on the AI systems route DL is taken via this P2 variant, which is a scaling/systems course, so it does not supply the P1 CNN prerequisite of ch9 |
| `m1p1-tda` (Y1P1 · OPT-P1 · gllm) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (probabilistic background; ch. 5 estimation and ch. 6 tests cited for the bootstrap in ch7) |
| `m1p1-tda` (Y1P1 · OPT-P1 · gllm) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (cites ch. 2 linear algebra and ch. 4 complexity; MST of its ch. 7.5 used but not cited) |
| `m1p1-tda` (Y1P1 · OPT-P1 · gllm) | `m1p1-machine-learning` (Y1P1 · MAND) | SAME | prerequisite / cites specific sections (ch. 3 and 5 kernel SVMs, ch. 7 k-means/PCA; ch. 7 also cited for metric spaces, single linkage, DBSCAN, mean-shift, which it does  |
| `m1p1-shapes` (Y1P1 · OPT-P1 · sys) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (programming fluency, data structures) |
| `m1p1-probability-monte-carlo` (Y1P1 · OFF · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: cites ch. 1 (probability spaces), ch. 3 (distributions), ch. 4 (LLN/CLT), ch. 7 (regression), ch. 8 (Bayesian); the refresher's comparison table links back  |
| `m1p1-statistical-learning-theory` (Y1P1 · OFF · —) | `m1p1-machine-learning` (Y1P1 · MAND) | SAME | prerequisite / related: deepens its ch. 8 'Generalization theory' and cites ch. 1, 2, 3, 4, 5, 6 (that module links back) |
| `m1p1-statistical-learning-theory` (Y1P1 · OFF · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: cites ch. 4, 5, 6, 7 (that module's exit table points here) |
| `m1p2-responsible-ai-sustainability` (Y1P1 · OFF · —) | `m1p1-machine-learning` (Y1P1 · MAND) | SAME | Prerequisite (ch. 0 review, the L3 reminders) and cites its ch. 5–6 for forecasting s_t, w_t, c_t. |
| `m1p2-responsible-ai-sustainability` (Y1P1 · OFF · —) | `m1p1-refresher-cs` (pre · REF) | OK | Prerequisite: the page cites its ch. 7 for NP-hardness. |
| `m1p2-responsible-ai-sustainability` (Y1P1 · OFF · —) | `m1p1-deep-learning` (Y1P1 · DL1) | SAME | Implicit prerequisite, not linked on the page: CNN/MLP training and PyTorch for the distillation lab. |
| `m1p2-reinforcement-learning` (Y1P2 · MAND · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite |
| `m1p2-reinforcement-learning` (Y1P2 · MAND · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite (Deep Learning is taken once, in P1 or P2) |
| `m1p2-reinforcement-learning` (Y1P2 · MAND · —) | `m1p2-deep-learning-p2` (Y1P2 · DL2) | SAME | related: the P2 alternative to the DL prerequisite. A student on that route takes DL at the same time as this course; that page links here |
| `m1p2-reinforcement-learning` (Y1P2 · MAND · —) | `m1p1-probability-monte-carlo` (Y1P1 · OFF) | OFF | cited as the prerequisite for Markov chains, but the home page marks it 'not in the 2026-27 LLGA 1 - S1 list' |
| `m1p2-reinforcement-learning` (Y1P2 · MAND · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (conditional expectation) |
| `m1p2-reinforcement-learning` (Y1P2 · MAND · —) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (memoization, topological sort) |
| `m1p2-graph-ml` (Y1P2 · MAND · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (kernel methods, PCA, k-means) |
| `m1p2-graph-ml` (Y1P2 · MAND · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite (attention, ELBO/VAE, contrastive learning). If DL is taken in P2, it runs in parallel |
| `m1p2-graph-ml` (Y1P2 · MAND · —) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (BFS, DFS, Dijkstra) |
| `m1p2-graph-ml` (Y1P2 · MAND · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (Markov chain convergence, ER as a null model) |
| `m1p2-nlp-text-mining` (Y1P2 · MAND · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (Naive Bayes in ML 3.3, EM and PCA in ML ch7, logistic regression); ML ch7 says EM 'will reappear in HMMs (NLP module)' |
| `m1p2-nlp-text-mining` (Y1P2 · MAND · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite: cites ch. 6 (attention/transformers). Overlaps DL 6.5 (BPE, MLM/CLM, perplexity) and DL ch7 (fine-tuning, LoRA) |
| `m1p2-nlp-text-mining` (Y1P2 · MAND · —) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite (sparse matrices, dynamic programming) |
| `m1p2-multimodal-genai` (Y1P2 · OPT-P2 · gllm) | `m1p1-deep-learning` (Y1P1 · DL1) | OK-ROUTE | prerequisite; cites ch. 6 (attention) and ch. 9 (VAE/GAN). ch0–ch2 here re-derive the ELBO and the GAN equilibrium already proved in DL ch. 9.2–9.3, so the two overlap |
| `m1p2-multimodal-genai` (Y1P2 · OPT-P2 · gllm) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | OFF-ROUTE | prerequisite (spectrograms for section 8.2) |
| `m1p2-multimodal-genai` (Y1P2 · OPT-P2 · gllm) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (Gaussians, Markov chains) |
| `m1p2-multimodal-genai` (Y1P2 · OPT-P2 · gllm) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (EM/PCA recap in ch0) |
| `m1p2-deep-learning-p2` (Y1P2 · DL2 · sys) | `m1p1-deep-learning` (Y1P1 · DL1) | EXCL(sys: DL in P2) | prerequisite: the page assumes its foundation, recaps its ch. 1–9 and sends the UAT proof to its ch. 1.2. In the curriculum it is also the alternative ('DL once, in P1 or |
| `m1p2-deep-learning-p2` (Y1P2 · DL2 · sys) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite implied by the sheet ('basics in ML'); not cited on the page |
| `m1p2-optimal-transport` (Y1P2 · OPT-P2 · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (learning framework) |
| `m1p2-optimal-transport` (Y1P2 · OPT-P2 · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (handling distributions, quantiles) |
| `m1p2-optimal-transport` (Y1P2 · OPT-P2 · —) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | OPT | useful prerequisite with the same instructor; cites ch. 8 (FID/Bures, spectral loss) and ch. 9 (bridge lab, spectrograms); SP ch. 8 says it prepares OT ch. 2-3 |
| `m1p2-optimization-ai` (Y1P2 · OPT-P2 · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (cites ch. 0 convex analysis, ch. 2 LASSO, ch. 3 SVM, ch. 4 massive data) |
| `m1p2-optimization-ai` (Y1P2 · OPT-P2 · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite de facto (cites ch. 1 init, ch. 2 backprop, ch. 3 momentum/Adam); students choosing this option must take DL in P1 |
| `m1p2-advanced-deep-learning` (Y1P2 · OPT-P2 · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite (ch0 recaps DL ch. 2, 3, 6, 7) |
| `m1p2-advanced-deep-learning` (Y1P2 · OPT-P2 · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (tests for ch1) |
| `m1p2-advanced-deep-learning` (Y1P2 · OPT-P2 · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (model selection, ch1) |
| `m1p2-image-synthesis` (Y1P2 · OPT-P2 · —) | `m1p1-probability-monte-carlo` (Y1P1 · OFF) | OFF | prerequisite (MC estimators, importance sampling; called "the heart of path tracing") |
| `m1p2-image-synthesis` (Y1P2 · OPT-P2 · —) | `m1p1-shapes` (Y1P1 · OPT-P1) | OPT | prerequisite (3D surface/mesh representation; mesh data structures are left to it) |
| `m1p2-image-synthesis` (Y1P2 · OPT-P2 · —) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | OPT | prerequisite (filtering, frequency analysis) |
| `m1p2-image-synthesis` (Y1P2 · OPT-P2 · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite in practice for ch8 and ch10 (backprop, CNNs). The page cites it wrongly as the "Machine Learning module". |
| `m1p2-statistics-in-action` (Y1P2 · OFF · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (cites ch. 4, 5, 6, 7, 10 for limit theorems, estimation, tests, regression, missing data, bootstrap) |
| `m1p2-statistics-in-action` (Y1P2 · OFF · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite / related (cites ch. 1 and 8 for the stats-ML bridge, ch. 2 ridge/lasso, ch. 7 PCA; claims causal forests are covered there, which they are not) |
| `m1p2-social-media-probabilistic` (Y1P2 · OFF · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite; cites ch. 3 (distributions, coupon collector), ch. 4 (convergence, bootstrap), ch. 5 (MLE, Hawkes) and ch. 6 (tests, LR test) |
| `m1p2-social-media-probabilistic` (Y1P2 · OFF · —) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite; cites ch. 7 (BFS/DFS, connected components) |
| `m1p2-social-media-probabilistic` (Y1P2 · OFF · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite; cites ch. 7 (k-means, EM, spectral clustering) for ch. 6 |
| `m1p2-computer-vision-applications` (Y1P2 · TBC · sys) | `m1p1-computer-vision` (Y1P1 · OPT-P1) | OK-ROUTE | prerequisite (a P1 Choose-3 elective, so not guaranteed). Heavy overlap: P1 ch9 already teaches two-stage/one-stage detection, NMS, DETR with Hungarian matching, U-Net, I |
| `m1p2-computer-vision-applications` (Y1P2 · TBC · sys) | `m1p1-deep-learning` (Y1P1 · DL1) | EXCL(sys: DL in P2) | prerequisite; cites ch1, ch3, ch4, ch6, ch7, ch9 |
| `m1p2-computer-vision-applications` (Y1P2 · TBC · sys) | `m1p2-deep-learning-p2` (Y1P2 · DL2) | SAME | related (same period). On the AI-systems route DL is taken here in parallel, so the CNN prerequisites arrive too late. Its ch7.1 also covers FGSM |
| `m1p2-computer-vision-applications` (Y1P2 · TBC · sys) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | OK-ROUTE | prerequisite; cites ch3 (2D convolution) and ch4 (sampling). Its Kalman cross-reference is broken |
| `m1p2-computer-vision-applications` (Y1P2 · TBC · sys) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite (ROC, CV); also cited for adversarial defenses and subgroup evaluation that it does not contain |
| `m1p2-realtime-ai-videogames` (Y1P2 · TBC · sys) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite: cites ch4 (amortized analysis), ch5 (heaps) and ch7 (Dijkstra/A*) |
| `m1p2-realtime-ai-videogames` (Y1P2 · TBC · sys) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: cited for Hoeffding and rank tests, but neither is present there (broken) |
| `m1p2-startup-entrepreneurship` (Y1P2 · OFF · —) | `m1p1-strategy-marketing` (Y1P1 · MAND) | OK | prerequisite (explicit 'Upstream' hyperlink in #place) |
| `m1p3-research-internship` (Y1P3 · MAND · —) | `m1p2-graph-ml` (Y1P2 · MAND) | OK | prerequisite / suggested topic anchor ('Graph ML' in #travailler) |
| `m1p3-research-internship` (Y1P3 · MAND · —) | `m1p2-optimal-transport` (Y1P2 · OPT-P2) | OPT-ONLY | prerequisite / suggested topic anchor ('OT' in #travailler) |
| `m1p3-research-internship` (Y1P3 · MAND · —) | `m1p2-nlp-text-mining` (Y1P2 · MAND) | OK | prerequisite / implied anchor for an 'LLM' topic in M1 (not named on the page) |
| `m2-large-language-models` (Y2P1 · MAND · —) | `m1p2-nlp-text-mining` (Y1P2 · MAND) | OK | prerequisite; cites ch. 0, 1, 1.2, 2, 4, 6, 7, 8.3, 9 (the page calls itself its direct continuation) |
| `m2-large-language-models` (Y2P1 · MAND · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite; cites ch. 6 (attention and transformers) |
| `m2-large-language-models` (Y2P1 · MAND · —) | `m1p2-reinforcement-learning` (Y1P2 · MAND) | OK | prerequisite; cites ch. 4 (bandits), ch. 5 (PPO, the stated prerequisite reading for RLHF), ch. 7 (agents) |
| `m2-large-language-models` (Y2P1 · MAND · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite; cites ch. 3 for cross-entropy |
| `m2-geometric-deep-learning` (Y2P1 · MAND · —) | `m1p1-shapes` (Y1P1 · OPT-P1) | OPT-ONLY | Stated prerequisite, but it is an M1 P1 Choose-3 elective on the 'sys' route, so a mandatory M2 course depends on an optional M1 course. There is also heavy overlap: Shap |
| `m2-geometric-deep-learning` (Y2P1 · MAND · —) | `m1p2-graph-ml` (Y1P2 · MAND) | OK | Prerequisite (mandatory). Cites ch. 0 (graph Laplacian), ch. 2 (permutation invariance) and ChebNet (ch. 4). |
| `m2-geometric-deep-learning` (Y2P1 · MAND · —) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | OPT-ONLY | Prerequisite cited for Fourier/convolution in the ch0 recap box, without a link; elective. |
| `m2-advanced-gnn` (Y2P1 · TBC · gllm) | `m1p2-graph-ml` (Y1P2 · MAND) | OK | prerequisite; ch0 restates its chapters 2–7, and the page cites its ch. 0, 3, 4, 5, 6, 7, 9.5, 9.6, 10, 10.2 and 11 section by section |
| `m2-advanced-gnn` (Y2P1 · TBC · gllm) | `m1p1-emerging-ml` (Y1P1 · OPT-P1) | OK-ROUTE | prerequisite: distributed training (ch1); temporal-split hygiene claimed in ch6 but not found there |
| `m2-privacy-uncertainty` (Y2P1 · TBC · —) | `m1p1-emerging-ml` (Y1P1 · OPT-P1) | OPT | prerequisite: ch. 5 (first DP encounter) and ch. 3 (federated learning) cited in ch0, ch4, ch11 |
| `m2-privacy-uncertainty` (Y2P1 · TBC · —) | `m1p2-statistics-in-action` (Y1P2 · OFF) | OFF | prerequisite: ch. 7-9 (multiple testing, bootstrap, intervals) and ch. 11 (exchangeability, de Finetti) cited in ch0, ch8, ch9 |
| `m2-privacy-uncertainty` (Y2P1 · TBC · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite: ch. 0 concentration, ch. 4 evaluation, ch. 8 generalization, ch. 9 drift |
| `m2-privacy-uncertainty` (Y2P1 · TBC · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite: ch. 3 and 8 (SGD, dropout) for DP-SGD and MC dropout |
| `m2-privacy-uncertainty` (Y2P1 · TBC · —) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: ch. 4, 6 (limit theorems, intervals, tests) and ch. 8 (Bayesian statistics) |
| `m2-boosting-foundation-tabular` (Y2P1 · TBC · —) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite; cites ch. 6 (trees, forests, boosting) and ch. 4 (evaluation). Overlap: ML ch. 6.3 Thm 6.4 already derives boosting as functional gradient descent. |
| `m2-boosting-foundation-tabular` (Y2P1 · TBC · —) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite; cited for multi-head attention (its ch. 6) |
| `m2-boosting-foundation-tabular` (Y2P1 · TBC · —) | `m1p2-multimodal-genai` (Y1P2 · OPT-P2) | OPT | related, not linked; ch. 3 DDPM is the real diffusion prerequisite for TabDDPM |
| `m2-boosting-foundation-tabular` (Y2P1 · TBC · —) | `m1p1-dbms` (Y1P1 · OFF) | OFF | related, not linked; SQL and relational model are the prerequisite for text-to-SQL (ch7) |
| `m2-control-generative-ai` (Y2P1 · TBC · gllm) | `m1p2-multimodal-genai` (Y1P2 · OPT-P2) | OK-ROUTE | prerequisite: ch. 3-4 (DDPM, CFG, DDIM inversion) are recalled in ch. 7 with proof; ch. 1 (VAE/ELBO); ch. 7 (FID) cited in ch. 9 |
| `m2-control-generative-ai` (Y2P1 · TBC · gllm) | `m2-large-language-models` (Y2P1 · MAND) | SAME | prerequisite, but taught in the same period (Y2 P1): ch. 1-2 and ch. 6 (decoding/sampling) cited in ch. 0; ch. 4-5 (RLHF/DPO/GRPO) cited in ch. 5; ch. 8 (agents/function  |
| `m2-control-generative-ai` (Y2P1 · TBC · gllm) | `m1p2-graph-ml` (Y1P2 · MAND) | OK | prerequisite: ch. 9 graph generation cited in ch. 0 |
| `m2-control-generative-ai` (Y2P1 · TBC · gllm) | `m2-graph-generative-models` (Y2P2 · TBC) | LATER | cites specific sections: ch. 8 rereads its ch. 3 (NeVAE valence), ch. 4 (GraphAF), ch. 5 (DiGress), ch. 6 (evaluation), ch. 7 (text-to-graph) and example 7.3 (molecular C |
| `m2-control-generative-ai` (Y2P1 · TBC · gllm) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: hypothesis testing and CLT for the watermark z-test (ch. 6) |
| `m2-projet-transverse` (Y2 all-year · MAND · —) | `m1p3-research-internship` (Y1P3 · MAND) | OK | prerequisite: the project "capitalizes on" the research internship (prose mention, no hyperlink) |
| `m2-ethical-issues-ai` (Y2 all-year · MAND · —) | `m1-humanites` (Y2 all-year · MAND) | SAME | prerequisite (upstream: 'M1/M2 humanities'); also named as a partner in #intro |
| `m2-ethical-issues-ai` (Y2 all-year · MAND · —) | `m1p2-responsible-ai-sustainability` (Y1P1 · OFF) | OFF | prerequisite (implied by 'possible responsible modules in P2', not linked) |
| `m2-ethical-issues-ai` (Y2 all-year · MAND · —) | `m1p3-research-internship` (Y1P3 · MAND) | OK | prerequisite (upstream: 'research internship', not linked) |
| `m2-mlops-llm-engineering` (Y2P2 · TBC · gllm/sys) | `m2-large-language-models` (Y2P1 · MAND) | OK | prerequisite (hyperlinked). The page cites ch. 1 tokenization, ch. 4-5 SFT/DPO, ch. 6 inference/vLLM, ch. 7 RAG, ch. 8 agents and ch. 9 evaluation. The serving content (K |
| `m2-mlops-llm-engineering` (Y2P2 · TBC · gllm/sys) | `m1p2-deep-learning-p2` (Y1P2 · DL2) | EXCL(gllm) | prerequisite (hyperlinked): training cost and serving questions |
| `m2-mlops-llm-engineering` (Y2P2 · TBC · gllm/sys) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite (PyTorch, GPU, checkpoints). It teaches LoRA in §7.3, but ch7 does not cite it. |
| `m2-mlops-llm-engineering` (Y2P2 · TBC · gllm/sys) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite: Hoeffding, used in ch2. MMD is cited from it, but it does not cover MMD. |
| `m2-mlops-llm-engineering` (Y2P2 · TBC · gllm/sys) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: KS test cited in ch5, but not covered there |
| `m2-mlops-llm-engineering` (Y2P2 · TBC · gllm/sys) | `m1p1-refresher-cs` (pre · REF) | OK | prerequisite: containers, queues, complexity (ch3) |
| `m2-security-robustness` (Y2P2 · TBC · gllm/sys) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite (gradient training, convolutions; the optimization attacks are grafted onto it) |
| `m2-security-robustness` (Y2P2 · TBC · gllm/sys) | `m2-advanced-gnn` (Y2P1 · TBC) | PART-ROUTE | prerequisite; cites ch. 7 (Nettack, graph robustness and certification defenses) for ch9. Reciprocal: Advanced GNN names this course as downstream for Nettack. |
| `m2-security-robustness` (Y2P2 · TBC · gllm/sys) | `m1p1-emerging-ml` (Y1P1 · OPT-P1) | PART-ROUTE | prerequisite; cites ch. 4 (Byzantine robustness / FL) for ch6-7 and ch. 5 (DP, Gaussian mechanism, DP-SGD) for ch5, ch7, ch8 |
| `m2-security-robustness` (Y2P2 · TBC · gllm/sys) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite; cites ch. 8 (generalization) in ch0 |
| `m2-security-robustness` (Y2P2 · TBC · gllm/sys) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite (hypothesis testing, Neyman-Pearson lemma, ch. 6 there) for ch5 and ch8 |
| `m2-graph-generative-models` (Y2P2 · TBC · gllm) | `m1p2-graph-ml` (Y1P2 · MAND) | OK | prerequisite: ch. 9 (graph generation, revisited in ch0); ch. 11 (DaSciM research) |
| `m2-graph-generative-models` (Y2P2 · TBC · gllm) | `m2-advanced-gnn` (Y2P1 · TBC) | OK-ROUTE | prerequisite: ch. 2 (WL), ch. 5 (graph transformers), ch. 1 (Dwivedi benchmarking), ch. 9 (DaSciM) |
| `m2-graph-generative-models` (Y2P2 · TBC · gllm) | `m1p2-optimal-transport` (Y1P2 · OPT-P2) | EXCL(gllm) | prerequisite: Gromov-Wasserstein for graph comparison and evaluation |
| `m2-graph-generative-models` (Y2P2 · TBC · gllm) | `m1p2-multimodal-genai` (Y1P2 · OPT-P2) | OK-ROUTE | prerequisite: ch. 1 (VAE/ELBO), ch. 3-4 (diffusion, CFG, latent diffusion), ch. 7 (FID) |
| `m2-explainability-security-privacy-llms` (Y2P2 · TBC · gllm/sys) | `m2-large-language-models` (Y2P1 · MAND) | OK | prerequisite (cites ch. 1, 2, 3, 4-5). Its ch. 9 already covers jailbreaks, indirect injections and the Kirchenbauer watermark; this page does not acknowledge that overla |
| `m2-explainability-security-privacy-llms` (Y2P2 · TBC · gllm/sys) | `m1p1-emerging-ml` (Y1P1 · OPT-P1) | PART-ROUTE | prerequisite: DP from ch. 5 (definition, Gaussian/Laplace mechanisms, post-processing, DP-SGD), recapped in ch8 |
| `m2-explainability-security-privacy-llms` (Y2P2 · TBC · gllm/sys) | `m1p1-deep-learning` (Y1P1 · DL1) | DL1-ONLY | prerequisite: transformer (ch. 6) |
| `m2-explainability-security-privacy-llms` (Y2P2 · TBC · gllm/sys) | `m1p1-refresher-statistics` (pre · REF) | OK | prerequisite: tests and Gaussian vectors for ch8-9 |
| `m2-speech-technology` (Y2P2 · TBC · sys) | `m1p1-signal-processing` (Y1P1 · OPT-P1) | OK-ROUTE | prerequisite; cites ch. 4 (sampling), ch. 6 (STFT), ch. 7 (random signals/PSD), ch. 8 (Mel/MFCC) |
| `m2-speech-technology` (Y2P2 · TBC · sys) | `m2-large-language-models` (Y2P1 · MAND) | OK | prerequisite; cites ch. 8 (multimodal/audio-in) and ch. 6 (speculative decoding) |
| `m2-speech-technology` (Y2P2 · TBC · sys) | `m1p1-deep-learning` (Y1P1 · DL1) | EXCL(sys: DL in P2) | prerequisite (cited as 'Deep Learning M1', no link): LSTM, attention |
| `m2-speech-technology` (Y2P2 · TBC · sys) | `m1p2-multimodal-genai` (Y1P2 · OPT-P2) | EXCL(sys) | prerequisite; cites ch. 1 (VAE), ch. 2 (GAN), ch. 3 (DDPM). Its ch. 8.2 (codec tokens, sound generation) overlaps ch11 but is not cited |
| `m2-speech-technology` (Y2P2 · TBC · sys) | `m1p1-machine-learning` (Y1P1 · MAND) | OK | prerequisite; cites ch. 7 (EM) |
| `m2-advanced-topics-llms` (Y2P2 · TBC · gllm) | `m2-large-language-models` (Y2P1 · MAND) | OK | Prerequisite (ch. 2-9 cited throughout). It also overlaps heavily without saying so: the RoPE relative proof (LLMs thm 2.3, Ex. 5), speculative decoding (LLMs thm 6.3), G |
| `m2-advanced-topics-llms` (Y2P2 · TBC · gllm) | `m1p2-advanced-deep-learning` (Y1P2 · OPT-P2) | EXCL(gllm) | Prerequisite. Its ch. 6 already derives the Switch load-balancing loss with a balancing exercise, so ch. 5 here repeats it without citing it. |
| `m2-advanced-topics-llms` (Y2P2 · TBC · gllm) | `m1p2-reinforcement-learning` (Y1P2 · MAND) | OK | Prerequisite: ch. 5 (PPO), ch. 6 (deep RL) and ch. 7 (LLM agents) are cited for ch. 2 and ch. 9. |
| `m2-advanced-topics-llms` (Y2P2 · TBC · gllm) | `m1p2-graph-ml` (Y1P2 · MAND) | OK | Prerequisite: ch. 5 (message passing) and ch. 10 (GraphRAG) are cited for ch. 4 and ch. 8. |
| `m2-internship` (Y2P3 · MAND · —) | `m1p3-research-internship` (Y1P3 · MAND) | OK | prerequisite (linked, used as the comparison baseline in #place) |

## Appendix B. Every assumed-knowledge entry (858) with the timing of the source the page names (mechanical)

Columns: concept assumed; the chapters that use it; the source the page names; and the verdict for each named slug. Verdict codes: OK = earlier and guaranteed; OK-ROUTE = earlier and on the consumer's route; SAME = same period; SAME-CHOOSE1 = mutually exclusive option; LATER; OFF = off-list; DL1-ONLY = only for students who took DL in P1; EXCL(route) = the route excludes it; OPT-ONLY = a mandatory page relying on an option; OPT / OFF-ROUTE = an option that is not guaranteed. "not stated" and "L3" rows carry no slug; the significant ones were resolved by hand in section 2.


### `m1p1-refresher-statistics` — Refresher in Statistics (APM_51438_EP) (pre · REF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Linear algebra: inverse, determinant, rank, positive (semi)definite matrices, orthogonal projection | ch2, ch3, ch7 | L3 | L3 |
| Multivariable calculus: Jacobian, gradient/Hessian, Taylor expansion, differentiation under the integral sign | ch2, ch4, ch5 | L3 | L3 |
| Python/NumPy arrays and vectorized simulation | ch2, ch3, ch4, ch6, ch7, ch9, ex | m1p1-refresher-cs | refresher-cs: SAME |
| Measure/Lebesgue integration: Borel sets, pushforward measure, Tonelli-Fubini, measure extension theorem, Vitali set | ch1, ch2 | not stated (connections table sends measure-theoretic depth to m1p1-probability-monte-carlo) | probability-monte-carlo: LATER |
| Characteristic functions and Lévy's continuity theorem | ch4 | not stated | not stated |
| Borel-Cantelli lemma; strong LLN; Glivenko-Cantelli (stated, not proved) | ch4 | not stated | not stated |
| Conditional independence (named, never formally defined) | ch1, ch10, ex 1 | not stated | not stated |
| Entropy, conditional entropy and KL divergence | ch9 | not stated | not stated |
| Logits, softmax classifier, affine MNIST classifier | ch9 | not stated (implicitly m1p1-refresher-neural-nets / m1p1-deep-learning) | refresher-neural-nets: SAME; deep-learning: LATER |
| Uniform convergence, complexity control, stability as generalization guarantees | ch9 | m1p1-statistical-learning-theory | statistical-learning-theory: LATER |
| Ridge/lasso regularization, validation and model selection | ch7, ch8, ch9 | m1p1-machine-learning | machine-learning: LATER |
| Importance sampling, antithetic variables, rejection sampling | ch2, ch4 | not stated (fits m1p1-probability-monte-carlo) | probability-monte-carlo: LATER |
| EM algorithm, MICE, multiple imputation combining rules | ch5, ch10 | not stated (Little & Rubin in references) | not stated |
| Benjamini-Hochberg FDR procedure; Welch-Satterthwaite degrees of freedom | ch6 | not stated | not stated |
| Studentized residuals, Cook's distance, robust/sandwich standard errors | ch7 | not stated | not stated |
| Block/cluster bootstrap and group-level uncertainty | ch4, exit | not stated | not stated |
| Causal adjustment, randomization | ch1, ex 2 | not stated | not stated |
| VAE/ELBO, diffusion forward/reverse processes, Kalman filter, Gaussian processes | ch3, ch8, ch9 | not stated | not stated |
| Thompson sampling / Bayesian bandits | ch8, ex 7 | not stated | not stated |
| Neumann series and spectral radius | ch10 | L3 | L3 |
| Probabilistic calibration | ch6, ch8 | not stated | not stated |

### `m1p1-refresher-cs` — Refresher in Computer Science (CSC_51440_EP) (pre · REF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Basic Python syntax (variables, functions, loops) | ch1 | L3 | L3 |
| Linear algebra: eigendecomposition, SVD, condition number, spectral radius / Neumann series | ch2 | m1p1-refresher-statistics | refresher-statistics: SAME |
| Probability: independence, expectation, uniform hashing model (expected costs, Bloom filter analysis) | ch4, ch5, ch6 | m1p1-refresher-statistics | refresher-statistics: SAME |
| PCA as a statistical method (variance, components) | ch2 | not stated | not stated |
| Softmax / logits | ch1, ch2 | not stated | not stated |
| Least squares fitted by gradient descent (docstring example) | ch2, ch3 | not stated | not stated |
| Train/validation/test splits, leakage, model selection | ch2, ch3, ch5 | m1p1-machine-learning | machine-learning: LATER |
| PyTorch nn.Module, Linear layers, ReLU, MLP | ch3 | m1p1-deep-learning | deep-learning: LATER |
| Transformer attention (Q K^T, heads, sequence length) | ch2, ch4 | not stated | not stated |
| Graph Laplacian, spectral methods, PageRank | ch2 | not stated | not stated |
| GNN message passing, PyG edge_index | ch2, ch7, exit | m1p2-graph-ml | graph-ml: LATER |
| LLM decoding: top-k sampling, beam search, subword/BPE tokenization | ch5, ch7 | not stated | not stated |
| HMM/Viterbi and RL Bellman value functions | ch6, ch7 | not stated | not stated |
| Union-find (disjoint-set) structure | ch7 | not stated | not stated |
| Eulerian walk / circuit | ch7 | not stated | not stated |
| Big-Omega notation | ch4 | not stated | not stated |
| Hard-margin SVM geometry | ch8 | not stated | not stated |
| Kendall rank comparison | ch6 | not stated | not stated |
| Optimal transport / Hungarian assignment | ch7 | not stated | not stated |
| Shell/CLI usage and basic git (commit, branch) | ch3 | not stated | not stated |
| Calculus/series: differentiating a geometric series, harmonic numbers, logarithmic asymptotics | ch4, ch5, ch6 | L3 | L3 |

### `m1p1-refresher-neural-nets` — Refresher Neural Nets (pre · SUP · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Python/NumPy programming, array broadcasting, matrix multiplication | before-start, ch1, ch3, ch5, ch6, ex | m1p1-refresher-cs | refresher-cs: SAME |
| multivariable chain rule, partial derivatives, Jacobians | ch3, ex (Ex. 3, Ex. 6) | not stated | not stated |
| train/validation/test splits, held-out evaluation, generalization | before-start, ch1 (§1.3), ch7, ex (Ex. 8) | m1p1-refresher-statistics (and Machine Learning on the course map) | refresher-statistics: SAME |
| Gaussian distribution and the variance of a sum of independent random variables | ch4 (§4.1), ex (Ex. 7) | not stated | not stated |
| logarithm/exponential and probability distributions (outputs summing to one) | ch2, ch6 | not stated | not stated |
| gradient descent as an optimization method (convergence, step size) | ch1, ch3, ch5 | not stated (Machine Learning is the evaluation-first exit) | not stated |
| automatic differentiation / reverse-mode autodiff in a framework | ch3 (computation-graph note), ch7 | m1p1-deep-learning | deep-learning: LATER |
| LayerNorm, residual connections, multi-head attention, learned Q/K/V projections, pre-norm transformer block | ch6 | m1p1-deep-learning | deep-learning: LATER |
| tokenization, shifted targets, causal masking, sequence evaluation | ch6, ex (Ex. 4) | m1p2-nlp-text-mining (NLP entry on the course map) | nlp-text-mining: LATER |
| message passing, relational splits, data graphs | ch3 (note), ch6, ch7 | m1p2-graph-ml (Graph ML entry on the course map) | graph-ml: LATER |
| regularization, model comparison, leakage controls | ch7 | m1p1-machine-learning (ML entry on the course map) | machine-learning: LATER |
| FLOP accounting conventions (multiply-add vs 2 FLOPs) | ex (Ex. 1) | not stated | not stated |
| GPU acceleration with CuPy (optional appendix of the external notebook) | ch1 (§1.3), intro (#sessions) | not stated | not stated |

### `m1p1-machine-learning` — Machine Learning (MDC_51006_EP, SynapseS "Foundations of Machine Learning") (Y1P1 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| multivariable calculus, gradients, convexity, Taylor expansion | ch0, ch2, ch3, ch6.3 | L3 (ch0 recap title), but the intro attributes optimization to m1p1-refresher-statistics, which explicitly does not cover it | refresher-statistics: OK |
| spectral theorem, eigendecomposition, SVD, Rayleigh quotient | ch0, ch2.2 (Prop 2.5), ch7.3 | L3 (ch0 recap); SVD practice in m1p1-refresher-cs | refresher-cs: OK |
| Lagrange multipliers, Lagrangian duality, Slater condition, KKT | ch3.2, ex (Ex. 2, Ex. 6) | not stated (Ex. 2 wrongly points to chapter 0) | not stated |
| Gaussian, Student and chi-square distributions; unbiased variance estimation | ch2.1 | m1p1-refresher-statistics | refresher-statistics: OK |
| maximum likelihood, Bayes' formula, MAP | ch2.2, ch3.1, ch3.3, ch7.2 | m1p1-refresher-statistics | refresher-statistics: OK |
| Kullback-Leibler divergence and entropy | ch7.2 (EM theorem) | not stated | not stated |
| Hilbert spaces, completion, Cauchy-Schwarz | ch5.1 | not stated | not stated |
| Ledoux-Talagrand contraction lemma, McDiarmid/bounded differences, symmetrization | ch3.2 (Thm 3.6), ch8.4 | used as a black box; deepened in m1p1-statistical-learning-theory | statistical-learning-theory: SAME |
| Radon's theorem | ch8.2 | not stated | not stated |
| bootstrap resampling | ch6.2 | not stated (taught in m1p1-refresher-statistics 4.1) | refresher-statistics: OK |
| ANOVA F statistic, chi-square test, mutual information (as filter scores) | ch4.7 | not stated (tests in m1p1-refresher-statistics ch6) | refresher-statistics: OK |
| Python, NumPy, scikit-learn API | all chapters (code blocks), ex | m1p1-refresher-cs | refresher-cs: OK |
| graph Laplacian | ch5 (graph kernels), ch7.3 note | m1p2-graph-ml (forward reference) | graph-ml: LATER |
| count vectorization / TF-IDF text features | ex (Ex. 12) | not stated (redone in m1p2-nlp-text-mining) | nlp-text-mining: LATER |
| data streams, concept drift, prequential evaluation | ch9.1 | m1p1-refresher-cs for the engineering | refresher-cs: OK |
| isotonic regression | ch4.5 | not stated (named only) | not stated |

### `m1p1-deep-learning` — Deep Learning (CSC_51054_EP) (Y1P1 · DL1 · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Chain rule, Jacobians, gradients of quadratic forms, softmax derivative | ch0, ch2 | L3 | L3 |
| Central limit theorem, covariance of iid sums | ch0 | m1p1-refresher-statistics | refresher-statistics: OK |
| NumPy matrix computation / Python for the labs | all labs | m1p1-refresher-cs | refresher-cs: OK |
| Cross-entropy loss, maximum likelihood, logistic/softmax classification | ch0, ch3.6, ch5.3, ch6.5 | not stated (m1p1-machine-learning 3.1 implicitly) | machine-learning: SAME |
| Spectral theorem, eigendecomposition, Lipschitz gradient, condition number, strong convexity | ch3.1, ch3.2 | not stated (L3 linear algebra; m1p1-machine-learning 0.2 GD/SGD) | machine-learning: SAME |
| Bias-variance decomposition, ridge regression | ch3.6, Ex. 12 | m1p1-machine-learning | machine-learning: SAME |
| Hahn-Banach separation, finite signed measures, Fourier transform injectivity, uniform continuity | ch1.2 | not stated (L3 analysis) | not stated |
| Gaussian CDF / erf | ch1.4 | not stated | not stated |
| KL divergence, Jensen's inequality, Jensen-Shannon divergence | ch9.2, ch9.3 | not stated (JSD only glossed inline) | not stated |
| EM algorithm / variational inference | ch9.2 | m1p1-machine-learning (7.2) | machine-learning: SAME |
| PCA and the Eckart-Young theorem | ch9.1 | m1p1-machine-learning (7.3); Eckart-Young not stated | machine-learning: SAME |
| Pointwise mutual information | ch6.5 | not stated | not stated |
| Floating-point formats (fp32/fp16/bf16), GPU memory hierarchy (SRAM/HBM) | ch0.3, ch2.2, ch6.3, ch8.3 | not stated | not stated |
| Wasserstein distance, MMD | ch7.2, ch9.3 | m1p2-optimal-transport (named 'Optimal Transport module', no link) | optimal-transport: LATER |
| Diffusion models (noising/denoising, guidance) | ch9.3 note, ch10.3 | m1p2-multimodal-genai (downstream) | multimodal-genai: LATER |
| Message-passing GNN / MPNN, Weisfeiler-Lehman test, graph Laplacian spectrum, k-core decomposition | ch6.3 note, ch10.1, ch10.2 | m1p2-graph-ml / m2-advanced-gnn (both downstream) | graph-ml: LATER; M2:advanced-gnn: LATER |
| TF-IDF, bag-of-words | ch10.1 | not stated (m1p2-nlp-text-mining is downstream) | nlp-text-mining: LATER |
| Convolution theorem / spectral filtering | ch4 note | m1p1-signal-processing | signal-processing: SAME |
| Bayesian reading of dropout (MC dropout) | ch3.6 | m1p1-emerging-ml | emerging-ml: SAME |

### `m1p1-signal-processing` — Signal Processing (APM_51055_EP, "Signal processing: from Fourier to Machine Learning") (Y1P1 · OPT-P1 · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Lebesgue integration, L¹/L² spaces, Hilbert spaces, Cauchy–Schwarz, Fubini (recalled in a recap box, not taught) | ch0, ch2, ch3 | L3 | L3 |
| Riemann–Lebesgue lemma | ch2 | not stated | not stated |
| Distribution theory (Dirac as a continuous linear form, transform of the comb taken as given) | ch1, ch3, ch4, ch7 | not stated | not stated |
| Complex analysis: power series and annulus of convergence, contour shift/holomorphy | ch5, ex 9 | not stated | not stated |
| Probability: random variables, expectation, Gaussian, chi-square distribution, random processes | ch7 | m1p1-refresher-statistics | refresher-statistics: OK |
| Bochner's theorem (proof of Wiener–Khinchin taken as given) | ch7 | not stated | not stated |
| Linear algebra: Toeplitz systems, matrix square roots, trace, Frobenius norm, PCA/Karhunen–Loève | ch6, ch7, ch8 | not stated (official prerequisite 'linear algebra') | not stated |
| NumPy/SciPy programming for the labs | ch4–ch9, exercises | m1p1-refresher-cs | refresher-cs: OK |
| Lasso, soft-thresholding/ISTA, alternating least squares | ch8 | not stated | not stated |
| Optimal transport: Wasserstein distance, Bures formula, Sinkhorn, transport plans, dual potentials | ch8, ch9, ex 12 | m1p2-optimal-transport | optimal-transport: LATER |
| CNNs, autoencoders, transformers and positional encodings, audio data augmentation | ch3, ch5, ch8 | m1p1-deep-learning | deep-learning: SAME |
| GCN layer, graph Laplacian, Laplacian positional encodings | ch8 | m1p2-graph-ml (cited as 'Graph ML module', no link) | graph-ml: LATER |
| GMM-HMM speech models, Kalman filter (named only) | ch7, ch8 | not stated (Kalman: 'downstream modules') | not stated |

### `m1p1-emerging-ml` — Emerging Subjects in ML and Collaborative Learning (APM_51178_EP, SynapseS 2026-27: "EA Collaborative Learning") (Y1P1 · OPT-P1 · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| convexity, L-smoothness, strong convexity, gradient-descent rates | ch0, ch2, ch3 | m1p1-machine-learning | machine-learning: SAME |
| CLT and variance of an average of i.i.d. gradients; Gaussian quantiles Φ^{-1} | ch0, ch1 (1.1 worked example), Ex 1 | m1p1-refresher-statistics | refresher-statistics: OK |
| graph Laplacian, its spectrum, second eigenvalue λ2 / algebraic connectivity (the course is in P1, but the Graph ML module that teaches this is P2) | ch2 (Theorem 2.6), Ex 7 | m1p2-graph-ml | graph-ml: LATER |
| Lagrange multipliers / constrained optimization | ch7 (Theorem 7.2), Ex 11 | not stated | not stated |
| neural-network training: backprop, per-example gradients, classifier confidence scores | ch5 (DP-SGD, membership inference), ch6 (mode connectivity) | not stated | not stated |
| Transformers, feed-forward layers, tokens, LoRA low-rank adapters | ch1, ch3 (Applications and LLMs note), ch7 (MoE, federated L | not stated (M2 Large Language Models module mentioned as continuation) | not stated |
| cryptographic primitives: pseudo-random generators, Shamir secret sharing | ch4 (Proposition 4.5) | not stated | not stated |
| Byzantine agreement in distributed systems (f < K/3 information-theoretic bound) | ch4 (Definition 4.1) | not stated | not stated |
| Rényi divergence / Rényi DP, privacy amplification by subsampling, advanced composition | ch5 (Theorem 5.3 usage, Algorithm 5.5), Ex 10 | not stated | not stated |
| Gaussian tail bounds (proof of the Gaussian mechanism) | ch5 (Theorem 5.4) | not stated | not stated |
| group fairness metrics (demographic parity, equalized odds) and OT barycenters | ch6 | m1p2-optimal-transport | optimal-transport: LATER |
| loss landscape, permutation symmetry of neural networks | ch6 | not stated | not stated |
| EM algorithm, Gaussian mixtures, HMMs | ch8 (Work 8.4) | not stated (taught in m1p1-machine-learning ch7) | machine-learning: SAME |
| least-squares regression, Polyak-Ruppert averaging | ch8 (Work 8.3) | not stated (m1p1-machine-learning) | machine-learning: SAME |
| Elias integer coding | ch2 (Theorem 2.3) | not stated | not stated |
| GPU throughput, bf16, FLOP/s utilization | ch7 (worked example) | not stated | not stated |
| LLM agents / multi-agent systems | ch1, ch6 | m1p2-reinforcement-learning | reinforcement-learning: LATER |

### `m1p1-computer-animation` — Computer Animation (CSC_51085_EP) (Y1P1 · OPT-P1 · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Cauchy-Lipschitz, Taylor expansions with remainder, eigen-decomposition of symmetric matrices, SO(3) (recapped only) | ch0, ch2, ch3, ch4 | L3 | L3 |
| Newton's method for nonlinear systems (solving the implicit Euler step) | ch2, ch4 | not stated | not stated |
| Conjugate gradient / multigrid for sparse SPD systems | ch4 (Def 4.4, Def 4.10), ex (Ex. 10) | not stated | not stated |
| Incompressible Navier-Stokes, divergence/gradient/Laplacian operators, Poisson equation | ch4 (Def 4.6, Def 4.10) | not stated | not stated |
| Continuum mechanics: strain, Hooke's law, Lamé parameters, speed of sound | ch4 (Def 4.5, Ex 4.7) | not stated | not stated |
| Newtonian mechanics: torque, moment of inertia, momentum | ch5, ch6 | not stated | not stated |
| Homogeneous 4x4 rigid transforms and frame changes (bone transforms M_i B_i^-1, FK composition) | ch7, ch8 | INF443 / 'C++ and basics of computer graphics' (official prerequisite); the Refresher in Computer Graphics CSC_51438_EP is not covered by the notes | unnamed |
| Dual quaternions and their normalized blending | ch7 (Def 7.3), ex (Ex. 7c) | not stated | not stated |
| Harmonic / Green coordinates for cage deformation | ch7 (Def 7.3) | not stated | not stated |
| Convexity, Minkowski difference, separating-axis theorem (GJK, SAT) | ch6 | not stated | not stated |
| Linear complementarity problems, projected Gauss-Seidel | ch6 | not stated | not stated |
| Least squares / orthogonal projection | ch7 (Ex 7.6) | not stated (taught in m1p1-machine-learning ch2) | machine-learning: SAME |
| Triangle meshes, dihedral angles, isosurfaces | ch4 (Def 4.8, SPH free surface), ch7 | m1p1-shapes | shapes: SAME |
| Spatial data structures: uniform grids, kd-trees, nearest-neighbour search | ch6, ch9, ch10 | m1p1-refresher-cs (the cited 'spatial data structures chapter' does not exist there) | refresher-cs: OK |
| Graph search: A*, Dijkstra | ch9 | m1p1-refresher-cs (graphs chapter) | refresher-cs: OK |
| Eikonal equation / fast marching / geodesic distances | ch9 | m1p1-shapes ('the geometry module') | shapes: SAME |
| Neural networks, backpropagation, RNNs/transformers, regression | ch7 (Def 7.3, Def 7.5), ch10 (Prop 10.3) | m1p1-machine-learning (cited, but these chapters live in m1p1-deep-learning) | machine-learning: SAME; deep-learning: SAME |
| Discrete exterior calculus, differential forms | ch11 | m2-geometric-deep-learning | M2:geometric-deep-learning: LATER |
| C++ and OpenGL programming for interactive labs | intro (official lab format); not used by the page's own code | INF443 / official prerequisite 'C++ and basics of computer graphics' | unnamed |

### `m1p1-computer-vision` — Image Analysis and Computer Vision (CSC_51073_EP) (Y1P1 · OPT-P1 · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| 1D convolution, Fourier transform, convolution theorem, Shannon sampling theorem | ch0, ch1 (Def. 1.4), ch2 (Def. 2.1), ex (Ex. 2c) | m1p1-signal-processing (ch. 1, 3, 4) | signal-processing: SAME |
| Least squares and normal equations | ch0, ch5 (DLT), ch7 (Lucas-Kanade) | m1p1-machine-learning (ch. 2) | machine-learning: SAME |
| Eigenvalues, orthogonal matrices, trace identities, basic SVD, Taylor expansions, chain rule | ch0, ch4, ch5, ch10 | L3 | L3 |
| Weyl's inequality for singular values; characteristic functions | ch0 | not stated (L3 implied) | not stated |
| Swapping derivative and convolution (Fubini) | ch2 (Def. 2.3) | m1p1-signal-processing (and ch0 review) | signal-processing: SAME |
| Cross-product matrix [t]_x and the projective plane P^2 beyond homogeneous coordinates | ch5, ch6 | not stated | not stated |
| Nonlinear least squares: Gauss-Newton / Levenberg-Marquardt, sparse systems | ch5 (Prop. 5.3), ch6 (Def. 6.5 bundle adjustment) | not stated | not stated |
| Dynamic programming | ch6 (Note modern dense stereo) | not stated | not stated |
| Calculus of variations / Euler-Lagrange equations | ch7 (Horn-Schunck note) | not stated | not stated |
| Max-flow/min-cut theorem, Ford-Fulkerson, submodularity, NP-hardness of multi-label cuts | ch8 (Def. 8.3) | not stated | not stated |
| Spectral clustering / graph Laplacian (normalized cuts) | ch8 (Prop. 8.4) | m1p2-graph-ml (ch. 4) | graph-ml: LATER |
| k-means++ initialisation, elbow/silhouette selection of k | ch8, ex (Ex. 8) | m1p1-machine-learning (ch. 7) | machine-learning: SAME |
| CNN layers, backpropagation, training of deep networks, ResNet | ch9, ch10 (Prop. 10.6), ch11 | m1p1-deep-learning (ch. 4) | deep-learning: SAME |
| Attention/transformers and Hungarian set matching (DETR) | ch9 (Def. 9.2) | m1p1-deep-learning (ch. 6) | deep-learning: SAME |
| Transfer learning / fine-tuning | ch9 (Prop. 9.1), session 10 lab | m1p1-deep-learning (ch. 7) | deep-learning: SAME |
| Contrastive image-text pretraining (CLIP), conditional diffusion | ch9 (Note beyond massive supervision) | m1p2-multimodal-genai (ch. 4-6, CLIP ch. 5) | multimodal-genai: LATER |
| Optimal transport and Wasserstein distance | ch10 (Note ICP and optimal transport) | m1p2-optimal-transport (cited only as 'the M1P2 module of the same master's program, ch. 1-2') | optimal-transport: LATER |
| Vector search / approximate nearest-neighbour indexing | ch4 (Prop. 4.5) | m1p1-dbms (ch. 9) | dbms: SAME |
| PCA (covariance eigenvectors) | ch10 (Prop. 10.2) | not stated (ch0 Eckart-Young cited; ML ch. 7 covers PCA) | not stated |
| Kalman filtering / GNSS-inertial fusion | ch10 (Def. 10.1) | not stated | not stated |
| Neural radiance fields, 3D Gaussian splatting | ch6 (Def. 6.9) | not stated (named only) | not stated |
| Image inpainting / diffusion PDEs | ch6 (Example 6.10), ch11 | not stated | not stated |

### `m1p1-tda` — Topological Data Analysis (CSC_51056_EP) (Y1P1 · OPT-P1 · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| metric spaces, norms, open/closed balls | ch0, ch2, ch7 | m1p1-machine-learning (ch. 7) — but that chapter only covers k-means/EM/PCA | machine-learning: SAME |
| general topology: open/closed/compact sets, continuity | ch0, ch1, ch2, ch7 | L3 | L3 |
| linear algebra: kernel, image, rank theorem, Gaussian elimination, quotient spaces | ch3, ch4 | m1p1-refresher-cs (ch. 2) | refresher-cs: OK |
| eigenvalues and spectral radius | ch0 (recap only) | m1p2-graph-ml (ch. 4) — a P2 module, i.e. after this course | graph-ml: LATER |
| asymptotic complexity (O-notation) | ch1, ch4, ch8, ch9 | m1p1-refresher-cs (ch. 4) | refresher-cs: OK |
| graphs, connected components, cliques, cyclomatic number | ch1, ch2, ch3, ex (Ex 6) | m1p2-graph-ml (ch. 0) — P2 module, and clique / cyclomatic number are not defined there | graph-ml: LATER |
| minimum spanning tree, Kruskal's algorithm, union-find | ch2 | not stated (actually taught in m1p1-refresher-cs ch. 7.5) | refresher-cs: OK |
| single-linkage hierarchical clustering, dendrograms, DBSCAN | ch2, ch6, ex (Ex 10) | m1p1-machine-learning (ch. 7) — not taught there | machine-learning: SAME |
| density estimation (kernel / k-NN density estimates) | ch2 (Def 2.9), ch6, ch10 | not stated | not stated |
| mode seeking / mean-shift | ch10 | m1p1-machine-learning (ch. 7) — not taught there | machine-learning: SAME |
| PCA and k-means | ch0, ch6 | m1p1-machine-learning (ch. 7) | machine-learning: SAME |
| kernel methods, positive-definite kernels, SVM | ch8, ch9 (Lab 3) | m1p1-machine-learning (ch. 3, ch. 5) | machine-learning: SAME |
| optimal transport, Wasserstein distances between measures | ch5, ch7, ch8 | m1p2-optimal-transport (P2 module, after this course) | optimal-transport: LATER |
| bootstrap, confidence intervals, permutation tests | ch7 | m1p1-refresher-statistics (ch. 5, ch. 6) | refresher-statistics: OK |
| MLPs, end-to-end training, auto-encoders and VAEs | ch8 | m1p1-deep-learning | deep-learning: SAME |
| permutation-invariant aggregation / Deep Sets, message passing | ch8 | m1p2-graph-ml (ch. 5) — Deep Sets not mentioned there | graph-ml: LATER |
| GNNs, graph classification, 1-WL expressivity | ch8, ch10, ex (Ex 12) | m1p2-graph-ml (ch. 2), m2-advanced-gnn (ch. 2) | graph-ml: LATER; M2:advanced-gnn: LATER |
| extended persistence and heat kernel signatures | ch8, ch10 | not stated | not stated |
| quiver representations / Gabriel's theorem | ch4, ch10 | not stated (declared out of scope, Oudot 2015) | not stated |
| partition of unity, nerve lemma proof tools | ch2 | not stated (declared out of scope) | not stated |
| medial axis, reach, tubular neighbourhoods, Riemannian manifolds | ch7, ch10 | not stated | not stated |
| Smith normal form; Δ-complexes | ch3, ex (Ex 2) | not stated | not stated |
| UMAP, scipy hierarchical clustering, networkx | ex (Ex 10) | not stated | not stated |
| Python / NumPy / scikit-learn programming | ch4, ch9 | m1p1-refresher-cs (ch. 1-2) | refresher-cs: OK |

### `m1p1-shapes` — Digital Representation and Analysis of Shapes (CSC_51074_EP) (Y1P1 · OPT-P1 · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| SVD-based optimal rigid alignment (Kabsch–Umeyama) used inside ICP | ch4 | m1p1-computer-vision | computer-vision: SAME |
| kd-trees, priority queues, hash tables, expected-cost / randomized-incremental complexity analysis | ch1, ch3, ch4, ch6 | m1p1-refresher-cs | refresher-cs: OK |
| spectral theorem, least squares / normal equations, constrained minimisation of quadratic forms | ch4, ch6, ch8 | L3 | L3 |
| discrete Fourier modes / Fourier series orthogonality | ch5 | L3 | L3 |
| differential geometry of surfaces: principal and normal curvatures, shape operator, geodesic distance, isometry | ch7, ch8 | not stated | not stated |
| spectral theory of the Laplace–Beltrami operator (self-adjoint, compact resolvent, L2 eigenbasis) and the heat equation | ch8 | not stated | not stated |
| finite elements with piecewise-linear hat functions (origin of cotangent weights) | ch5 | m2-geometric-deep-learning | M2:geometric-deep-learning: LATER |
| Poisson equation, divergence, surface Dirac measure | ch4 | not stated | not stated |
| principal component analysis | ch4 | not stated | not stated |
| chain complexes, boundary operators, Smith normal form | ch9 | not stated | not stated |
| stability theorem for persistence diagrams | ch9 | not stated | not stated |
| Gromov–Hausdorff distance and wave kernel signature (WKS), named without definition | ch8 | m2-geometric-deep-learning | M2:geometric-deep-learning: LATER |
| Hausdorff distance between surfaces | ch6, ex | not stated | not stated |
| Lagrange interpolation and the Runge phenomenon | ch1 | L3 | L3 |
| inscribed angle theorem / cyclic quadrilaterals | ch3 | L3 | L3 |
| linear programming and 3D convex hull algorithms | ch0, ch3 | L3 | L3 |
| medial axis and reach; signed distance functions | ch1, ch4 | not stated | not stated |
| rotation group SO(3) and rigid motions | ch4 | L3 | L3 |
| differential forms and Stokes theorem (discrete exterior calculus) | ch10 | not stated | not stated |

### `m1p1-probability-monte-carlo` — Probability Theory for ML: Applications to Monte Carlo Methods and Generative Models (APM_51056_EP) (Y1P1 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Standard distributions (binomial, Poisson, exponential, Gaussian, gamma) with their moments | ch0, ch3, ch4, ch5 | m1p1-refresher-statistics | refresher-statistics: OK |
| Dominated convergence theorem (named in the ch. 1 summary note, never stated) | ch1, ch2 | L3 | L3 |
| Multivariate change of variables / Jacobian | ch1, ch3 | L3 | L3 |
| Characteristic functions and Lévy's continuity theorem (admitted) | ch2 | not stated | not stated |
| Slutsky's lemma, tightness / O_P(1) | ch2 | not stated | not stated |
| Borel-Cantelli lemma and Kolmogorov's maximal inequality (strong LLN admitted) | ch2, ch7 | not stated | not stated |
| Gaussian quantiles and confidence intervals (1.96) | ch2, ch4 | m1p1-refresher-statistics | refresher-statistics: OK |
| Existence of conditional expectation (Radon-Nikodym or L^2 projection extended to L^1) | ch6 | not stated | not stated |
| Hilbert-space orthogonal projection onto a closed subspace of L^2 | ch6 | not stated | not stated |
| Linear regression (conditional expectation as regression) | ch6 | m1p1-refresher-statistics | refresher-statistics: OK |
| Kernels / kriging (affine Gaussian conditioning link) | ch6 | m1p1-machine-learning | machine-learning: SAME |
| Bayesian posterior inference (target known up to a constant) | ch5, ch8 | m1p1-refresher-statistics | refresher-statistics: OK |
| Gaussian mixtures and EM | ch1, ch8 | m1p1-machine-learning | machine-learning: SAME |
| Eigenvalues / spectral decomposition of a stochastic matrix | ch7 | not stated | not stated |
| Positive recurrence and Harris recurrence in general state spaces | ch7 | not stated | not stated |
| Brownian motion, SDEs, the infinitesimal generator of a diffusion (no LLGA module teaches stochastic calculus) | ch9 | not stated | not stated |
| Euler-Maruyama discretization | ch9 | not stated | not stated |
| L-smoothness and strong convexity of a potential | ch9, ch10 | not stated | not stated |
| Wasserstein distance W2 (cited from a P2 module, so used before it is taught) | ch9, ch10 | m1p2-optimal-transport | optimal-transport: LATER |
| Kullback-Leibler divergence | ch10 | not stated | not stated |
| Diffusion models (DDPM), score matching, noised marginals p_t (downstream P2 module) | ch9, ch10 | m1p2-multimodal-genai | multimodal-genai: LATER |
| VAE/GAN and training a neural network as the score model s_theta | ch9 | m1p1-deep-learning | deep-learning: SAME |
| Python/NumPy programming (the official sheet promises a mini-training at the start of the course) | ch3, ch4, ch5, ch8, ch9 | not stated | not stated |

### `m1p1-dbms` — DataBase Management System (CSC_51053_EP) (Y1P1 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| sets, Cartesian products, binary relations, first-order logic quantifiers (recalled in a recap box, not taught) | ch0, ch1, ch2, ch3 | m1p1-refresher-cs | refresher-cs: OK |
| big-O complexity, logarithms, average cost of hash tables, sorting and merging | ch4, ch5, ch8 | m1p1-refresher-cs | refresher-cs: OK |
| basic probability: the 'n balls into m bins' paradigm, expectation | ch0 (announced for ch5 but never actually used there) | L3 | L3 |
| graph algorithms: transitive closure, cycle detection, topological order | ch1, ch2, ch6 | not stated | not stated |
| k-means clustering | ch9 | m1p1-machine-learning | machine-learning: SAME |
| text/image embeddings produced by encoders | ch9 | m1p2-nlp-text-mining (ch. 4), m1p2-multimodal-genai (ch. 5) | nlp-text-mining: LATER; multimodal-genai: LATER |
| cosine / L2 distance, NumPy vectorised linear algebra | ch9 | not stated | not stated |
| named-entity recognition and information extraction by models | ch10 | m1p2-nlp-text-mining | nlp-text-mining: LATER |
| RAG pipeline (retrieval-augmented generation) | intro, ch9 | m2-large-language-models | M2:large-language-models: LATER |
| node embeddings, GNNs, message passing | ch9 | m1p2-graph-ml | graph-ml: LATER |
| Python programming, DB-API usage | ch2 | not stated | not stated |
| distributed-systems basics: replication, network partitions, consistent hashing, Bloom filters | ch9 | not stated | not stated |
| ontologies RDFS/OWL and logical inference | ch9, ch10 | not stated | not stated |
| tuple relational calculus (used in Th. 1.7, never defined) | ch1 | not stated | not stated |
| outer joins (LEFT JOIN … IS NULL anti-join) | ex | not stated | not stated |

### `m1p1-statistical-learning-theory` — Statistical Learning Theory (APM_51059_EP) (Y1P1 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| LLN, CLT, Markov and Chebyshev inequalities, modes of convergence | ch0, ch2, ex (Ex. 5 uses the CLT) | m1p1-refresher-statistics (ch. 4); proved version in m1p1-probability-monte-carlo (ch. 2) | refresher-statistics: OK; probability-monte-carlo: SAME |
| Bias/variance, MLE, confidence intervals, tests | ch0, ch8 | m1p1-refresher-statistics (ch. 5-6) | refresher-statistics: OK |
| Least squares, normal equations, Gauss-Markov, ridge | ch0, ch9 | m1p1-refresher-statistics (ch. 7); m1p1-machine-learning (ch. 2) | refresher-statistics: OK; machine-learning: SAME |
| Convexity, Jensen's inequality, subgradients and the optimality condition 0 in the subdifferential | ch2, ch5, ch7, ch9 | L3 (ch. 0 recap lists it without teaching it) | L3 |
| Conditional expectation and Doob martingale (McDiarmid proof admitted) | ch2, ch5 | L3 (listed in the ch. 0 recap); martingales: not stated | L3 |
| Gaussian concentration of Lipschitz functions; Gaussian tail bounds (Mills ratio) | ch2, ch9 | m1p1-probability-monte-carlo (ch. 2) | probability-monte-carlo: SAME |
| Binomial-sum bound (eN/d)^d | ch3 | not stated (admitted) | not stated |
| Kullback-Leibler divergence, total variation distance, Pinsker's inequality | ch8, ex (Ex. 6) | not stated | not stated |
| Covering numbers / metric entropy | ch5 (Dudley note) | not stated | not stated |
| Hard-margin SVM formulation | ch6 | m1p1-machine-learning (ch. 3) | machine-learning: SAME |
| Kernels and RKHS | ch5 | m1p1-machine-learning (ch. 5) | machine-learning: SAME |
| Logistic regression and boosting as algorithms | ch6 (Tsybakov note), ch7 | m1p1-machine-learning (ch. 3, ch. 6) | machine-learning: SAME |
| K-fold cross-validation, one-standard-error rule | ch4, ch7, ch9 | m1p1-machine-learning (ch. 4) | machine-learning: SAME |
| Lasso as an ML algorithm | ch9 | m1p1-machine-learning (ch. 2) | machine-learning: SAME |
| Neural networks and weight norms | ch6 (margins and deep learning note) | Deep Learning module ch. 3 (m1p1-deep-learning; that chapter is 'Optimization in practice') | deep-learning: SAME |
| Bayesian prior/posterior | ch7 (PAC-Bayes note), ch10 | not stated | not stated |
| Mirror descent | ch10 (paper 3) | not stated | not stated |
| Python/NumPy/scikit-learn | ch3, ch5, ch7, ch9 code | not stated | not stated |

### `m1p2-responsible-ai-sustainability` — Optimization and Responsible AI for Sustainability (official title: Optimisation and Responsible AI) (Y1P1 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Linear programming basics: polyhedra, vertices, simplex and interior-point methods | ch0, ch2, ch4, ch5 | L3 | L3 |
| Lagrangian duality, Slater condition, KKT conditions | ch0, ch2 | m1p2-optimization-ai | optimization-ai: LATER |
| Convexity (a local minimum is global) | ch0, ch1, ch2 | m1p2-optimization-ai | optimization-ai: LATER |
| NP-hardness and complexity classes | ch0, ch4 | m1p1-refresher-cs | refresher-cs: OK |
| Softmax, logits, KL divergence, cross-entropy loss | ch3, ex | not stated | not stated |
| Lipschitz constant of a network layer | ch3, ex | not stated | not stated |
| Training CNN/MLP classifiers on MNIST in PyTorch | ex | not stated | not stated |
| Logistic regression | ex | not stated | not stated |
| Scaling laws (accuracy vs compute) | ch1 | m1p2-deep-learning-p2 | deep-learning-p2: LATER |
| Pipeline parallelism / job dependencies in training | ch2 | m1p2-deep-learning-p2 | deep-learning-p2: LATER |
| Autoregressive LLM decoding, memory bandwidth, roofline reasoning | ch3 | not stated | not stated |
| Fake quantization and the straight-through estimator (QAT) | ch3 | not stated | not stated |
| Sparse storage (CSR) | ch3 | not stated | not stated |
| Distributed / federated learning and job placement | ch2 | m1p1-emerging-ml | emerging-ml: SAME |
| Forecasting solar/wind/carbon intensity with regression models | ch5 | m1p1-machine-learning | machine-learning: SAME |
| Stochastic programming with recourse; robust optimization | ch5, ch8 | not stated | not stated |
| Multi-objective evolutionary algorithms (NSGA-II) | ch1 | not stated | not stated |
| Variance of sums of independent variables, log-normal distribution, Monte Carlo percentiles | ch6 | not stated | not stated |
| Price elasticity of demand (economics) | ch7, ex | not stated | not stated |
| GHG Protocol reporting (Scope 2 location-based vs market-based) | ch6, ch7 | not stated | not stated |
| Hyperparameter optimization / algorithm configuration | ch8 | m1p2-optimization-ai | optimization-ai: LATER |

### `m1p1-strategy-marketing` — Strategy, Innovation & Marketing (official unit: IME_51456_EP Introduction au marketing et à la stratégie) (Y1P1 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| 4P marketing mix | intro | not stated | not stated |
| Porter's five forces | intro | not stated | not stated |
| graph RAG (retrieval-augmented generation over a knowledge graph) | intro, travailler | not stated | not stated |
| fraud detection with GNNs | intro, travailler | not stated | not stated |
| recommender systems | travailler | not stated | not stated |
| multimodal models and LLM agents | intro | not stated | not stated |
| accuracy and other model-evaluation metrics | intro | not stated | not stated |
| optimal transport (OT) as a research area | industrie | not stated | not stated |
| data moat, cost of error, latency as product constraints | travailler | not stated | not stated |
| CIFRE thesis (French industrial PhD scheme) | industrie | not stated | not stated |

### `m1p2-reinforcement-learning` — Reinforcement Learning and Autonomous Agents (CSC_52081_EP) (Y1P2 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Banach fixed-point theorem | ch1, ch2 | L3 | L3 |
| Markov chains: transition matrices, stationary distribution, Perron-Frobenius, total-variation convergence | ch0, ch1, ch3 | m1p1-probability-monte-carlo (cited as prerequisite but not in the 2026-27 LLGA list); recap box labelled 'L3 prerequisites' | probability-monte-carlo: OFF |
| conditional expectation, filtrations | ch0, ch3 | m1p1-refresher-statistics | refresher-statistics: OK |
| memoization, Bellman-Ford shortest paths, topological sort / DAG execution | ch0, ch7 | m1p1-refresher-cs | refresher-cs: OK |
| random walks on graphs P = D^{-1}A, PageRank | ch0 | m1p2-graph-ml (taught in the same period) | graph-ml: SAME |
| Hoeffding concentration inequality | ch4 | not stated | not stated |
| KL divergence (and its asymmetry) | ch4, ch5, ch6 | not stated | not stated |
| Jensen's inequality | ch3 | not stated | not stated |
| Fisher information matrix, conjugate gradient, line search | ch5 | not stated | not stated |
| linear programming duality, Lagrangian / primal-dual optimization | ch1, ch6 | not stated | not stated |
| neural networks, backpropagation, SGD, PyTorch, Huber loss, gradient clipping | ch5, ch6 | m1p1-machine-learning / m1p1-deep-learning | machine-learning: OK; deep-learning: DL1-ONLY |
| ridge regression | ch4 | not stated | not stated |
| reparameterization trick | ch6 | not stated | not stated |
| Wasserstein distance, quantile-regression loss | ch6 | not stated | not stated |
| GAN discriminator / adversarial training | ch6 | not stated | not stated |
| causal transformer, token embeddings, cross-entropy training | ch6 | not stated | not stated |
| Bradley-Terry preference model / RLHF reward model | ch6 | m2-large-language-models (downstream, so only forward-referenced) | M2:large-language-models: LATER |
| RAG, vector stores, embeddings, GraphRAG | ch7 | m1p2-graph-ml ch10 and m1p2-nlp-text-mining | graph-ml: SAME; nlp-text-mining: SAME |
| LLM prompting, function calling, JSON schema | ch7 | not stated | not stated |
| computational complexity (PSPACE-hardness) | ch7 | not stated | not stated |
| distributed SGD and Byzantine-robust aggregation | ch6, ch7 | m1p1-emerging-ml ch2 and ch4 | emerging-ml: OPT-ONLY |
| multi-label classification basics (binary relevance), WEKA/MEKA | ch8 | not stated | not stated |

### `m1p2-graph-ml` — Graph Machine and Deep Learning for Generative AI (CSC_52072_EP) (Y1P2 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Attention mechanism / softmax attention, MLP, LeakyReLU (used for GAT, DiGress denoiser, graph transformers). DL can be taken in P2 (Deep Learning P2 variant),  | ch5, ch9, ch10 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| VAE, ELBO, KL divergence, reparameterisation trick | ch6 (VGAE), ch9 (GraphVAE, NeVAE) | m1p1-deep-learning | deep-learning: DL1-ONLY |
| RNN / LSTM / GRU and teacher forcing | ch5 (GraphSAGE-LSTM, TGN GRU memory), ch9 (GraphRNN), ch11 ( | not stated | not stated |
| Denoising diffusion models (DDPM forward/backward process), classifier guidance | ch9 (9.5 DiGress, 9.7), ch11 (NGG latent diffusion) | m1p2-multimodal-genai (an elective in the same P2 Choose-1 group) | multimodal-genai: SAME |
| FID (used to define FCD by analogy) | ch9 (9.6) | m1p2-multimodal-genai | multimodal-genai: SAME |
| Kernel methods: RKHS feature maps, PSD Gram matrices, SVM, kernel ridge, kernel PCA | ch2 (graph kernels), session 3 lab (WL+SVM on MUTAG) | m1p1-machine-learning | machine-learning: OK |
| PCA and k-means | ch0, ch3, ch4 | m1p1-machine-learning | machine-learning: OK |
| word2vec skip-gram, unigram^{3/4} noise distribution, hierarchical softmax (the SGNS loss itself is derived) | ch3 | m1p2-nlp-text-mining (taught in parallel, same period) | nlp-text-mining: SAME |
| LLM prompting/few-shot, NER, relation extraction, vector index / classic RAG | ch10, final lab | m1p2-nlp-text-mining; m2-large-language-models (downstream) | nlp-text-mining: SAME; M2:large-language-models: LATER |
| Convergence theorem for finite Markov chains | ch0 (Prop 0.6) | m1p1-refresher-statistics | refresher-statistics: OK |
| DFS, Dijkstra, priority queues | ch0, ch7 | m1p1-refresher-cs | refresher-cs: OK |
| Fourier transform / convolution in classical signal processing | ch4 (Def 4.1) | m1p1-signal-processing (a P1 elective, not on the Graph × LLM route) | signal-processing: OPT-ONLY |
| Gromov-Wasserstein optimal transport | ch9 (9.6) | m1p2-optimal-transport (an elective) | optimal-transport: SAME |
| Federated learning (partitions = clients) | ch7 | m1p1-emerging-ml | emerging-ml: OPT-ONLY |
| Contrastive learning and choice of negatives | ch6 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| Symmetric-matrix diagonalisation, Kronecker product mixed-product rule, Ky Fan theorem | ch0, ch2, ch4 | L3 | L3 |
| Bochner's theorem / random Fourier features | ch5 (TGAT time encoding) | not stated | not stated |
| Maximum likelihood, EM, MCMC, binomial distribution | ch9 (9.2) | m1p1-refresher-statistics (only for the ER null model) | refresher-statistics: OK |
| PyTorch training loop (Adam, cross-entropy, weight decay, dropout) | ch5 code, ex 4, ex 6 | not stated | not stated |
| Hungarian matching / graph matching | ch9 (9.3) | not stated | not stated |
| METIS graph partitioning | ch7 (7.2) | not stated | not stated |
| t-SNE | ex 2 | not stated | not stated |
| GIN and the 1-WL expressivity bound for GNNs (forward reference) | ch5, ch8 | m2-advanced-gnn | M2:advanced-gnn: LATER |
| Bayesian optimisation / QSAR pipeline | ch9 (9.7) | not stated | not stated |

### `m1p2-nlp-text-mining` — Introduction to Text Mining and NLP (CSC_52082_EP) (Y1P2 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Dirichlet distribution, Dirichlet-multinomial conjugacy, multivariate beta function | ch3 (Laplace = Dirichlet posterior mean), ch5 (LDA, collapse | L3 | L3 |
| Markov chains (stationary distribution, Perron-Frobenius, MCMC convergence) | ch5 (Gibbs sampler), ch6, ch8.1 (TextRank) | m1p1-refresher-cs ("Refresher CS"), but that page has no Markov material; it is actually in m1p1-refresher-statistics and m1p2-reinforcement-learning  | refresher-cs: OK; refresher-statistics: OK; reinforcement-learning: SAME |
| Dynamic programming / Bellman principle | ch6 (Viterbi), ch1 (Unigram Viterbi segmentation) | m1p1-refresher-cs; m1p2-reinforcement-learning ch. 2 | refresher-cs: OK; reinforcement-learning: SAME |
| EM algorithm and variational inference | ch1 (Unigram tokenizer), ch5 (LDA), ch6 (HMM training, only  | m1p1-machine-learning | machine-learning: OK |
| MLE with Lagrange multipliers | ch3 | L3 | L3 |
| SVD and PCA | ch0, ch4 (SIF), ch5 (LSA), ch8.5 | L3 and m1p1-machine-learning (PCA) | machine-learning: OK |
| Logistic regression, SVM, L1/L2 regularization | ch3, ch8.6 | m1p1-machine-learning | machine-learning: OK |
| Classification metrics (precision/recall/F1, PR vs ROC, confusion matrix, reliability curve) | ch3, ch6, ch8.4 | not stated (taught in m1p1-machine-learning ch4) | machine-learning: OK |
| Transformer architecture (multi-head attention, residuals, LayerNorm, encoder/decoder) | ch7 | m1p1-deep-learning ch. 6 | deep-learning: DL1-ONLY |
| Sentence CNNs and BiLSTMs | ch3 | not stated (m1p1-deep-learning ch4-5) | deep-learning: DL1-ONLY |
| AdamW, warmup/decay schedules, SGD | ch4, ch7, ch8.5 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| LoRA/adapters, int8 quantization, distillation | ch7 | m2-mlops-llm-engineering ch. 7 and m2-large-language-models ch. 6 (downstream modules; LoRA is also in m1p1-deep-learning ch7) | M2:mlops-llm-engineering: LATER; M2:large-language-models: LATER; deep-learning: DL1-ONLY |
| k-means and clustering | ch2 note, ch5 (BERTopic, WSI), ch9 | not stated (m1p1-machine-learning ch7) | machine-learning: OK |
| Optimal transport (Word Mover's Distance) | ch2 (comparison table) | m1p2-optimal-transport (an elective in Choose-1) | optimal-transport: SAME |
| Noise contrastive estimation | ch4 | not stated | not stated |
| Permutation test, effect size | ch4 (WEAT) | not stated | not stated |
| Approximate nearest-neighbour search | ch8.5 (two-tower retrieval) | not stated | not stated |
| Sparse matrix formats | ch2 | m1p1-refresher-cs | refresher-cs: OK |
| RAG, in-context learning, zero/few-shot prompting | ch3, ch8, ch9 | m2-large-language-models (downstream) | M2:large-language-models: LATER |
| Knowledge graphs, GraphRAG, k-core decomposition, communities, PageRank | ch6 note, ch8.6, ch9 | m1p2-graph-ml | graph-ml: SAME |

### `m1p2-multimodal-genai` — Multimodal Generative AI (CSC_52002_EP) (Y1P2 · OPT-P2 · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| scaled dot-product attention and transformer blocks | ch0, ch4 (DiT), ch5, ch8 | m1p1-deep-learning (ch. 6) | deep-learning: OK-ROUTE |
| CNNs, transposed convolutions, U-Net training in PyTorch | ch0, ch1 (MiniVAE code), ch3 (unet) | m1p1-deep-learning | deep-learning: OK-ROUTE |
| VAE/ELBO and GAN minimax as first seen (re-derived here) | ch0, ch1, ch2 | m1p1-deep-learning (ch. 9) | deep-learning: OK-ROUTE |
| Vision Transformer patch tokenization (ViT) | ch4 (DiT), ch5 (CLIP image encoder), ch8.4 | not stated (taught in m1p2-advanced-deep-learning ch. 4, which is in the same Choose-1 group) | advanced-deep-learning: SAME-CHOOSE1 |
| Kantorovich-Rubinstein duality, Wasserstein W1, W2 between Gaussians (Bures) | ch2 (WGAN, FID), ch7, Ex. 9 | m1p2-optimal-transport ("OT module"); this course is in the same Choose-1 group, so a student who takes it cannot also take OT | optimal-transport: SAME-CHOOSE1 |
| Jensen's inequality, characteristic functions and Lévy uniqueness, Bayes' rule, Markov chains | ch0, ch3 | m1p1-refresher-statistics ("Refresher Statistics, chains") | refresher-statistics: OK |
| EM algorithm and PCA (VAE as a probabilistic PCA) | ch0 recap | m1p1-machine-learning | machine-learning: OK |
| stochastic differential equations, Brownian motion, reverse-time dynamics | ch4 (SDE note, probability-flow ODE) | not stated | not stated |
| mutual information | ch5 (InfoNCE bound) | not stated | not stated |
| LoRA low-rank adaptation | ch6, ch7 project, Ex. 14 | not stated (derived in m1p1-deep-learning ch. 7.3) | deep-learning: OK-ROUTE |
| LayerNorm, GELU/SiLU, residual identity initialization | ch4 DiT block | not stated (m1p1-deep-learning ch. 3.5) | deep-learning: OK-ROUTE |
| subword tokenization (BPE, SentencePiece), T5 encoders | ch6 | m1p2-nlp-text-mining ("NLP module") | nlp-text-mining: SAME |
| STFT, sampling rate, spectrograms | ch8.2 | m1p1-signal-processing | signal-processing: OFF-ROUTE |
| imitation learning / behaviour cloning, receding-horizon control | ch8.3 | m1p2-reinforcement-learning (section 6.5) | reinforcement-learning: SAME |
| model-based RL and LLM agents | ch8.4 | m1p2-reinforcement-learning (sections 6.4, ch. 7) | reinforcement-learning: SAME |
| flow matching | ch8.3 (pi0) | not stated (not taught anywhere in M1) | not stated |
| Inception-v3 and I3D feature extractors | ch2, ch7, ch8.1 | not stated | not stated |
| neural scaling laws | ch4 (DiT note) | not stated (m1p2-advanced-deep-learning ch. 9) | advanced-deep-learning: SAME-CHOOSE1 |
| graph generation and discrete diffusion (DiGress), GNN-LLM embedding alignment | ch1, ch3, ch5 notes, ch8.4 | m1p2-graph-ml (ch. 9, ch. 10) | graph-ml: SAME |
| NeRF and volume rendering background | ch8.4 | not stated (taught in m1p2-image-synthesis ch. 10, which is in the same Choose-1 group; the page points to m2-geometric-deep-learning instead) | image-synthesis: SAME-CHOOSE1; M2:geometric-deep-learning: LATER |
| PyTorch and the Hugging Face transformers API | ch1, ch3, ch4, ch5 code, Ex. 3 | not stated | not stated |

### `m1p2-deep-learning-p2` — Deep Learning (P2 variant) — APM_52183_EP, "Apprentissage profond de la théorie à la pratique" (Y1P2 · DL2 · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Transformer block: multi-head attention softmax(QKᵀ/√d)V, positional encoding, residual connections, layer norm (recap only, never defined here) | ch1, ch2, ch5, ch6 | m1p1-deep-learning | deep-learning: EXCL(sys: DL in P2) |
| Adam/AdamW update rule (only paraphrased; m and v used in memory counts) | ch0, ch1 (def 1.4), ch4 | m1p2-optimization-ai | optimization-ai: SAME-CHOOSE1 |
| Non-convex SGD convergence O(1/√K) (theorem 5.5) and why networks train well | ch0 | m1p2-optimization-ai | optimization-ai: SAME-CHOOSE1 |
| Strong convexity, L-smoothness, condition number κ, Nesterov acceleration and the Ω(√κ) lower bound | ch8 | m1p2-optimization-ai | optimization-ai: SAME-CHOOSE1 |
| Dual problem / accelerated dual ascent (MSDA) | ch8 | m1p2-optimization-ai | optimization-ai: SAME-CHOOSE1 |
| Chebyshev polynomial acceleration of gossip | ch8 | not stated | not stated |
| Minimax / saddle-point optimization (adversarial training) | ch7 | m1p2-optimization-ai | optimization-ai: SAME-CHOOSE1 |
| LARS large-batch training; mini-batch variance reduction; optimal statistical rates (Dieuleveut) | ch2, ch8 | m1p2-optimization-ai | optimization-ai: SAME-CHOOSE1 |
| Empirical risk, cross-entropy, train/validation/test split, overfitting | ch0 | not stated | not stated |
| Normalization layers (BatchNorm/LayerNorm), data augmentation, transfer learning | ch0, ch7 | m1p1-deep-learning | deep-learning: EXCL(sys: DL in P2) |
| Full proof of the universal approximation theorem | ch0 | m1p1-deep-learning | deep-learning: EXCL(sys: DL in P2) |
| KL and Jensen–Shannon divergences, Bayes rule, Gaussian latent-variable models | ch7 | not stated | not stated |
| Spectral norm, eigenvalues of symmetric, circulant and doubly stochastic matrices | ch7, ch8 | not stated | not stated |
| Grouped-query attention (GQA) | ex (Ex. 3) | not stated | not stated |
| Straight-through estimator for QAT; quantization error propagation bound | ch4, ch5 | m1p2-responsible-ai-sustainability | responsible-ai-sustainability: OFF |
| Energy, PUE and carbon-intensity accounting | ch5 (ex 5.4), ch6 (ex 6.4), ex (Ex. 7) | m1p2-responsible-ai-sustainability | responsible-ai-sustainability: OFF |
| Error-feedback gradient compression, local steps, federated learning | ch3, ch8 | m1p1-emerging-ml | emerging-ml: OFF-ROUTE |
| GPU memory hierarchy (SRAM, HBM, NVLink, InfiniBand, tensor cores); only a short note in ch6 | ch1, ch2, ch3, ch5, ch6 | not stated | not stated |
| FlashAttention IO-aware algorithm | ch5, ch6, ex (Ex. 8) | m2-large-language-models | M2:large-language-models: LATER |
| Actor-critic, PPO, RLHF | ch7 | m1p2-reinforcement-learning | reinforcement-learning: SAME |
| Message passing / graph neural networks (cited as skeleton of permutation-equivariant layers) | ch1 | not stated | not stated |
| Python / PyTorch coding | ch0, ch1, ex | not stated | not stated |

### `m1p2-optimal-transport` — Machine learning with Optimal Transport and Algorithmic Fairness (home tree label: Computational Optimal Transport for ML and Fairness) (Y1P2 · OPT-P2 · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Lagrangian/KKT stationarity conditions and envelope theorem | ch3 (Th. 3.2, Th. 3.4) | not stated | not stated |
| Bregman divergence / Bregman projection | ch3 (Th. 3.2 proof), ch4 (IBP barycenters) | not stated | not stated |
| Hilbert projective metric, contraction of positive matrices | ch3 (Th. 3.3) | not stated | not stated |
| Measure theory: narrow convergence, tightness, monotone convergence, absolute continuity | ch0, ch1 (Th. 1.3), ch2 (Brenier, narrow topology note) | L3 | L3 |
| Polyhedra, vertices / basic feasible solutions of an LP | ch1 (Th. 1.3), ex (Ex. 8) | L3 | L3 |
| Matrix square roots of SPD matrices, trace cyclicity, Gaussian covariances | ch2 (Th. 2.7), ch4 (spectral loss note) | not stated | not stated |
| Quantile functions, empirical CDF | ch2 (Prop. 2.6, Cor. 2.8), ch6 (Th. 6.2) | m1p1-refresher-statistics | refresher-statistics: OK |
| Minkowski inequality, conditional distributions | ch2 (Th. 2.5) | not stated | not stated |
| MMD / kernel distances | ch3 (Sinkhorn divergence note) | not stated (audience line assumes it) | not stated |
| Monte-Carlo estimation | ch3 (Def. 3.5) | not stated | not stated |
| GANs (generator, discriminator), gradient penalty, spectral normalisation | ch4 (Prop. 4.2 / WGAN) | m1p1-deep-learning | deep-learning: DL1-ONLY |
| Transfer learning and deep features | ch4 (OTDA) | m1p1-deep-learning | deep-learning: DL1-ONLY |
| Backpropagation / autodiff frameworks (PyTorch, JAX) | ch3 (Th. 3.4), ch4, ch7 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| Supervised learning framework, classifier training, covariate shift, logistic regression | ch4 (Def. 4.1, OTDA), ch6 (lab) | m1p1-machine-learning | machine-learning: OK |
| Group-lasso regularisation | ch4 (OTDA step 2), ch7 | not stated | not stated |
| k-means | ch5 (COOT initialisation) | not stated | not stated |
| Word embeddings (word2vec/GloVe), TF-IDF | ch4 (Ex. 4.4), ch5 (Ex. 5.5), ex (Ex. 5) | m1p2-nlp-text-mining | nlp-text-mining: SAME |
| Graphs, adjacency matrices, GNN message passing, knowledge graphs, GraphRAG | ch5 (Def. 5.3, Ex. 5.5) | m1p2-graph-ml | graph-ml: SAME |
| Stochastic block models | ex (Ex. 12) | not stated | not stated |
| Frank-Wolfe / conditional gradient with line search | ch5 (PGW) | not stated | not stated |
| FID / Fréchet distance, spectrograms | ch2 (bridge note), ch3 (Def. 3.5), ch4 (spectral loss note) | m1p1-signal-processing | signal-processing: OPT |
| ROC space (TPR/FPR), calibration | ch6 (Prop. 6.3, limits note), ex (Ex. 11) | not stated | not stated |
| Causal graphs (S -> X), confounding | ch6 (Prop. 6.3, limits note) | not stated | not stated |
| EEG / biosignal normalisation | ch5 (COOT), ch7 | m1p1-signal-processing | signal-processing: OPT |

### `m1p2-optimization-ai` — Optimization for AI (APM_52067_EP) (Y1P2 · OPT-P2 · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| basic convex analysis and LP/KKT duality (recap only) | ch0, ch8 | L3; m1p1-machine-learning ch. 0; m1p2-optimal-transport ch. 0 (OT is in the same Choose-1 group, so not available to these students) | machine-learning: OK; optimal-transport: SAME-CHOOSE1 |
| multivariate calculus: gradients, Hessians, integral Taylor remainder, operator norms, eigenvalues of symmetric matrices, Cholesky | ch2, ch7, ex | not stated | not stated |
| LASSO, ridge, logistic regression, hard/soft-margin SVM | ch1, ch4, ch8 | m1p1-machine-learning ch. 2-3 | machine-learning: OK |
| conditional expectation, variance, independence of noises | ch5, ch6 | not stated | not stated |
| backpropagation, cross-entropy training of neural networks, initialization/normalization, loss-landscape pictures | ch1, ch2, ch3, ch10 | m1p1-deep-learning ch. 1-3 | deep-learning: DL1-ONLY |
| Gaussian-process regression posterior (mu_k, sigma_k), Gaussian CDF/PDF | ch9 | not stated | not stated |
| online convex optimization and regret | ch10 | not stated | not stated |
| GANs and adversarial examples / adversarial training | ch8 | not stated | not stated |
| fairness criteria (demographic parity) | ch8, ch11 | m1p1-emerging-ml ch. 6 | emerging-ml: OPT |
| PAC learning / generalization framework | ch8, ch11 | not stated | not stated |
| Markov chains and stationary laws | ch11 | not stated | not stated |
| constrained MDPs / RL | ch11 | m1p2-reinforcement-learning | reinforcement-learning: SAME |
| distributed / large-batch training, transformer (BERT/LLM) pretraining | ch10 | m1p2-deep-learning-p2 ch. 8 (same Choose-1 group) | deep-learning-p2: SAME-CHOOSE1 |
| Python/NumPy, scipy.optimize, scikit-optimize | ch2, ch4, ch5, ch9, ex | not stated | not stated |

### `m1p2-advanced-deep-learning` — Advanced Deep Learning (CSC_52087_EP, official title "Apprentissage profond avancé") (Y1P2 · OPT-P2 · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| backpropagation / autograd (recap only) | ch0, ch3, ch10 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| SGD with momentum, Adam/AdamW, learning-rate schedules | ch0, ch4.2, ch9 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| scaled dot-product and multi-head attention, transformer encoder, positional encoding | ch0, ch4, ch6, ch8 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| BatchNorm vs LayerNorm, residual connections | ch0, ch5 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| CNNs, ResNet blocks, receptive field | ch3, ch5, ch7 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| transfer learning, fine-tuning, linear probing | ch0, ch7, ch8 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| cross-entropy, softmax, KL divergence | ch3.2, ch7, ch9.1 | not stated | not stated |
| Student t confidence intervals, paired tests, multiple-testing correction, statistical power | ch1, ex 5 | m1p1-refresher-statistics | refresher-statistics: OK |
| model selection, train/val/test discipline | ch1 | m1p1-machine-learning | machine-learning: OK |
| latent-variable models, VAE, ELBO | ch10.3 | not stated | not stated |
| DDPM forward process, noise schedule alpha-bar_t, epsilon-prediction network | ch10.4, ch8 (ex 8.2), ch10.5 | m1p2-multimodal-genai | multimodal-genai: SAME-CHOOSE1 |
| VQ-VAE / discrete visual tokenizer | ch8.1, ch8.2 | not stated | not stated |
| BERT masked language modelling | ch8 | m1p2-nlp-text-mining | nlp-text-mining: SAME |
| GNN message passing and its permutation equivariance | ch4.4, ch11.2 | m1p2-graph-ml | graph-ml: SAME |
| distributed SGD (data parallel, sharding) | ch9.1 | m1p1-emerging-ml | emerging-ml: OPT |
| quantization and pruning for deployment | ch3.2, ch3.3 | m1p2-computer-vision-applications | computer-vision-applications: SAME |
| volume rendering / light transport | ch10.1 | m1p2-image-synthesis | image-synthesis: SAME-CHOOSE1 |
| Lipschitz constants, l_p norms, projection onto a norm ball | ch4.5 | not stated | not stated |
| group actions | ch4.4 | not stated | not stated |
| Gumbel-softmax relaxation | ch10.2 | not stated | not stated |
| ordinary/partial differential equations, initial and boundary conditions | ch10.5 | not stated | not stated |
| CLIP image-text contrastive training | ch7.2, ch10.6 | m1p2-multimodal-genai | multimodal-genai: SAME-CHOOSE1 |

### `m1p2-image-synthesis` — Image Synthesis: Theory and Practice (CSC_52084_EP) (Y1P2 · OPT-P2 · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Expectation, variance, LLN, CLT for MC error | ch0, ch7, ch8, ch9 | m1p1-probability-monte-carlo (also recapped as L3 in ch0) | probability-monte-carlo: OFF |
| Sampling from a given density (inverse CDF / change of variables) to draw cosine, GGX or area-light samples | ch7, ex (Ex 5c, 6c), code (reading exercise 1) | L3 (ch0 recap gives only the change-of-variables formula); m1p1-probability-monte-carlo ch3 would be the natural source | probability-monte-carlo: OFF |
| Multiple importance sampling weights (balance/power heuristic) | ch7 | not stated (only named, Veach) | not stated |
| Sampling theory, aliasing, prefiltering, frequency analysis, SNR in dB | ch5 (textures), ch8 | m1p1-signal-processing | signal-processing: OPT |
| Triangle meshes, mesh data structures, UV parameterization/unwrapping | ch3, ch5, ch6 | m1p1-shapes | shapes: OPT |
| Homogeneous coordinates, 4x4 model/view/projection matrices, clip space and perspective divide, inverse-transpose normal transform | ch9 (shader code) | not stated | not stated |
| Contraction mapping / Banach fixed point, Fredholm integral operators | ch4 | not stated | not stated |
| Cauchy's formula (mean projected area = surface/4) from integral geometry | ch6 | not stated (used as a black box) | not stated |
| Spherical harmonics | ch9 (light probes), ch10 (3DGS colour) | not stated | not stated |
| MLPs, CNNs, recurrent autoencoders, gradient-based training, backpropagation | ch8, ch9, ch10 | "Machine Learning module, backpropagation chapter" (it is actually in m1p1-deep-learning) | deep-learning: DL1-ONLY |
| Fourier features / spectral bias of MLPs | ch10 | not stated (Tancik et al. cited) | not stated |
| Camera calibration and structure-from-motion poses | ch10 | not stated (m1p1-computer-vision would be the source) | computer-vision: OPT |
| Projection of a 3D Gaussian to a 2D ellipse (EWA / Jacobian of projection) | ch10 | not stated | not stated |
| Kernel / k-NN density estimation | ch9 (photon mapping) | not stated | not stated |
| Snell refraction and dielectric Fresnel equations (index of refraction) | ex (Ex 10a project) | not stated | not stated |
| GPU/SIMD/SIMT architecture, C/C++ and OpenGL API programming | ch6 note, ch9 | official prerequisites (C/C++); OpenGL engineering is left to the course's lab sessions | unnamed |
| Wasserstein distances / OT sampling estimators (analogy only) | ch7 note | m1p2-optimal-transport | optimal-transport: SAME-CHOOSE1 |

### `m1p2-statistics-in-action` — Statistics in Action (APM_52066_EP) (Y1P2 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| LLN, CLT, delta method | ch0, ch2, ch8 | m1p1-refresher-statistics | refresher-statistics: OK |
| Parametric estimation, MLE and its asymptotics | ch0, ch6 (Box-Cox profile likelihood) | m1p1-refresher-statistics | refresher-statistics: OK |
| Confidence intervals, tests, p-values, type I/II errors, two-sample Student and chi-square tests, Normal quantiles z and Phi | ch0, ch2, ch9, ch10 | m1p1-refresher-statistics | refresher-statistics: OK |
| Fisher F distribution and the ANOVA F test; Student quantile used for the LSD | ch3 | not stated (one-way ANOVA is in m1p1-refresher-statistics 6.5) | refresher-statistics: OK |
| OLS, hat matrix, Gauss-Markov, coefficient tests, R^2 | ch6 | m1p1-refresher-statistics | refresher-statistics: OK |
| Orthogonal projector, trace = rank, leave-one-out update formula | ch6 | not stated (L3 linear algebra) | not stated |
| Missing-data framing | ch5 | m1p1-refresher-statistics | refresher-statistics: OK |
| Beta-Binomial conjugate posterior, credible intervals | ch10 | not stated (Bayesian statistics is ch. 8 of m1p1-refresher-statistics) | refresher-statistics: OK |
| Sequential probability ratio test / likelihood ratio, stopping times | ch10, Ex. 8 | not stated | not stated |
| Conditional Slutsky lemma, functional delta method, empirical Donsker theorem | ch8 | not stated (van der Vaart ch. 23) | not stated |
| Monte Carlo simulation and NumPy random generation | ch0, ch8, ch10, Ex. 6-8 | L3 | L3 |
| Ridge / lasso regularization | ch6 | m1p1-machine-learning | machine-learning: OK |
| PCA (for AMMI/GGE models) | ch3 note | m1p1-machine-learning | machine-learning: OK |
| Causal forests / heterogeneous-effect estimation | ch5 note | m1p1-machine-learning (cited, but not actually covered there) | machine-learning: OK |
| Multi-armed bandits | ch10 | m1p2-reinforcement-learning | reinforcement-learning: SAME |
| Holm step-down procedure | Ex. 7 | not stated | not stated |
| Tukey simultaneous intervals | Ex. 10 | not stated | not stated |
| AR(1) processes / serial correlation | ch5, Ex. 6 | not stated | not stated |
| Intraclass correlation (design effect) | ch10 | not stated | not stated |
| Exchangeability, de Finetti, graphex processes, Bayesian nonparametrics, HMMs | ch11 | not stated (graphons/exchangeability appear in m1p2-graph-ml ch. 9) | graph-ml: SAME |

### `m1p2-social-media-probabilistic` — Social Media and Communication: Probabilistic Models and Algorithms (APM_51058_EP) (Y1P2 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Discrete-time and continuous-time Markov chains (ergodicity, generators, exponential clocks, strong Markov property). Continuous-time dynamics are used in the S | ch3, ch5 | not stated | not stated |
| Perron–Frobenius theorem, spectral radius, eigen-decomposition of A | ch0, ch3, ch6 | m1p2-graph-ml | graph-ml: SAME |
| Random walk mixing time and spectral gap | ch0, ch4, ch5 | m1p2-graph-ml | graph-ml: SAME |
| Probability generating functions | ch0, ch1 | not stated | not stated |
| Supermartingales and martingale deviation control | ch3, ch4 | not stated | not stated |
| Markov/Chebyshev inequalities, LLN, CLT | ch0, ch1 | m1p1-refresher-statistics | refresher-statistics: OK |
| Maximum likelihood estimation | ch2, ch3, ch6 | m1p1-refresher-statistics | refresher-statistics: OK |
| Hypothesis testing, likelihood-ratio and KS tests, bootstrap | ch2, ch3, ch8 | m1p1-refresher-statistics | refresher-statistics: OK |
| Hawkes processes for cascade timestamps. Never defined; the page cites Refresher Statistics ch. 5, which does not contain it. | ch3, ch7 | m1p1-refresher-statistics | refresher-statistics: OK |
| Coupon collector problem. The page cites Refresher Statistics ch. 3, which does not contain it. | ch4 | m1p1-refresher-statistics | refresher-statistics: OK |
| BFS/DFS, connected components | ch0, ch1, ch8 | m1p1-refresher-cs | refresher-cs: OK |
| k-means, EM algorithm, spectral clustering | ch6, ch8 | m1p1-machine-learning | machine-learning: OK |
| Variational EM (E/M steps, responsibilities) on latent block models | ch6 | m1p1-machine-learning | machine-learning: OK |
| Semidefinite relaxation | ch6 | not stated | not stated |
| NP-hardness and reductions (Set Cover), approximation ratios, competitive analysis | ch4, ch5 | not stated | not stated |
| Convex optimization and Lagrangian duality (behind alpha-fairness and TCP as decentralized optimization) | ch5 | not stated | not stated |
| Mean-field / fluid-limit ODE approximation of Markov processes (Kurtz) | ch5 | not stated | not stated |
| Poisson processes | ch5 | m1p1-refresher-statistics | refresher-statistics: OK |
| SGD and federated learning | ch5, ch9 | not stated | not stated |
| Sparse eigensolvers (scipy eigsh), NumPy | ch8 | not stated | not stated |
| Positional encodings for GNNs (forward pointer only) | ch0, ch9 | m2-advanced-gnn | M2:advanced-gnn: LATER |

### `m1p2-computer-vision-applications` — Computer Vision: From Fundamentals to Applications (Y1P2 · TBC · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Hungarian algorithm / min-cost bipartite assignment (used but never taught) | ch2 (DETR), ch5 (SORT, ByteTrack), Ex. 5 | L3 (ch5 note); m1p2-optimal-transport ch1-2 (ch2 note), but that page never mentions the Hungarian algorithm | optimal-transport: SAME |
| Kalman filter derivation and its Bayesian interpretation | ch5 | m1p1-signal-processing, which does not cover it: its ch7 defers Kalman to downstream modules | signal-processing: OK-ROUTE |
| CNNs, receptive fields, pooling, ResNet | ch0, ch1, ch3 | m1p1-deep-learning ch4. On the AI-systems route DL is taken as m1p2-deep-learning-p2, in the same period, so it is not available beforehand | deep-learning: EXCL(sys: DL in P2); deep-learning-p2: SAME |
| attention, transformer encoder-decoder | ch2 (DETR), ch3 (SAM), ch6 (BEVFormer) | m1p1-deep-learning ch6 | deep-learning: EXCL(sys: DL in P2) |
| Vision Transformer (ViT) | ch3 (SAM image encoder) | m1p2-advanced-deep-learning ch4, an elective in the same P2 Choose-1 group | advanced-deep-learning: SAME |
| sigmoid, logits, cross-entropy, gradient descent/Adam, transfer learning and fine-tuning | ch0, ch1 (focal loss), Ex. 12 | m1p1-deep-learning ch1, ch3, ch7 | deep-learning: EXCL(sys: DL in P2) |
| autoencoders for learning normality | ch7.1 | m1p1-deep-learning ch9 | deep-learning: EXCL(sys: DL in P2) |
| 2D convolution, image sampling/resolution | ch0, ch3 | m1p1-signal-processing ch3, ch4 | signal-processing: OK-ROUTE |
| ROC/AUROC, cross-validation; pixel AUROC and the PRO metric (named, never defined) | ch0, ch7.1 | m1p1-machine-learning (ROC, CV); PRO: not stated | machine-learning: OK |
| KL divergence, softmax with temperature | ch8.3 | m1p2-advanced-deep-learning ch3 | advanced-deep-learning: SAME |
| epipolar geometry, rectification, camera calibration and distortion | ch6.1-6.2 | m1p1-computer-vision (P1, Hartley & Zisserman) | computer-vision: OK-ROUTE |
| bilinear interpolation, transposed convolution / upsampling | ch3.2, ch3.3 | not stated | not stated |
| metric learning for ReID embeddings (triplet/contrastive training) | ch5.2 | not stated | not stated |
| deformable attention | ch2.3 | not stated | not stated |
| adversarial training and certified robustness | ch9.1 | m1p1-machine-learning, which has no such content. It is actually covered in m1p2-advanced-deep-learning §4.5 and m2-security-robustness | machine-learning: OK; advanced-deep-learning: SAME; M2:security-robustness: LATER |
| subgroup / fairness evaluation | ch9.2, Ex. 11 | m1p1-machine-learning (not present there) | machine-learning: OK |
| scene graphs | ch9.3 | m1p2-graph-ml (not present there) | graph-ml: SAME |
| MDP formalization for planning | ch7.2 | m1p2-reinforcement-learning | reinforcement-learning: SAME |
| 3D rendering for synthetic data | ch4.2 | m1p2-image-synthesis | image-synthesis: SAME |

### `m1p2-realtime-ai-videogames` — Real-time AI in Video Games: decisive & collaborative actions (Y1P2 · TBC · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Graphs, BFS/DFS, Dijkstra, priority queues/binary heaps, amortized complexity | ch0, ch2 | m1p1-refresher-cs (chapters 4, 5, 7) | refresher-cs: OK |
| Hoeffding's inequality / concentration | ch0, ch6 | m1p1-refresher-statistics ("chapter on concentration"). This is wrong: it is taught in m1p1-machine-learning ch0, Thm 0.3. | refresher-statistics: OK; machine-learning: OK |
| UCB1 and its logarithmic regret | ch6 | m1p2-reinforcement-learning ch4 | reinforcement-learning: SAME |
| MDPs, Bellman equations, Q-learning, DQN, policy gradient / PPO, actor-critic | ch7, ch8 | m1p2-reinforcement-learning ch1-6 | reinforcement-learning: SAME |
| AlphaGo/AlphaZero policy-value guided MCTS (PUCT) | ch6, ch7 | m1p2-reinforcement-learning ch5-6. This is wrong: it is actually in ch4 §4.2. | reinforcement-learning: SAME |
| Hungarian algorithm / minimum-cost assignment | ch4 (Def. 4.3), ch8 (Ex. 8.2), Ex. 7 (Hungarian by hand) | m1p2-optimal-transport ch1-2 and m1p2-computer-vision-applications ch5 | optimal-transport: SAME; computer-vision-applications: SAME |
| kd-trees / quadtrees for neighbourhood queries | ch4, ch5 | m1p1-computer-vision ch10 | computer-vision: OK-ROUTE |
| Explicit (Euler) integration and numerical stability | ch1, ch4, Ex. 6 | not stated (m1p1-computer-animation covers it but is never linked) | computer-animation: OFF-ROUTE |
| Velocity obstacles RVO/ORCA, funnel algorithm, navmesh voxelization | ch2 | not stated (named only) | not stated |
| Value-decomposition MARL (QMIX, VDN), theory of mind, emergent communication | ch8 | m1p2-reinforcement-learning ch7. That chapter does not cover them. | reinforcement-learning: SAME |
| Behavioral cloning, inverse RL | ch7 | not stated (m1p2-reinforcement-learning ch6 covers imitation) | reinforcement-learning: SAME |
| Knowledge distillation, small/quantized networks | ch7, ch9 | m1p2-advanced-deep-learning ch3 | advanced-deep-learning: SAME |
| LLM inference (quantization, streaming, caching) and RAG | ch9 | m2-large-language-models (ch7 for RAG); m1p2-reinforcement-learning ch7 for LLM agents | M2:large-language-models: LATER; reinforcement-learning: SAME |
| Log-normal law, rank tests, multiple testing / false positives | ch9 (Ex. 9.1) | m1p1-refresher-statistics and m1p1-machine-learning. Neither module teaches rank tests or multiple testing. | refresher-statistics: OK; machine-learning: OK |
| Graph analysis of player interaction graphs (collusion communities) | ch9 | m1p2-graph-ml | graph-ml: SAME |

### `m1p2-startup-entrepreneurship` — Startup, Large Companies & Entrepreneurship (Y1P2 · OFF · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Strategy / marketing basics (alliances, positioning) that P2 is said to push 'to cases' | intro, place | m1p1-strategy-marketing | strategy-marketing: OK |
| Technology Readiness Level (TRL) as a measure of how mature a result is | industrie | not stated | not stated |
| Intellectual property, open-source vs proprietary licensing | industrie | not stated | not stated |
| Intrapreneurship, corporate venture, tech transfer, CIFRE industrial PhD scheme | industrie | not stated | not stated |
| Industrialising an AI model / AI product ops (deployment, operation, MLOps) | intro, industrie | not stated | not stated |
| A P2 technical deliverable such as a graph+text demo | place, travailler | not stated (implicitly m1p2-graph-ml and m1p2-nlp-text-mining, the 'RL / Graph ML / NLP core') | graph-ml: SAME; nlp-text-mining: SAME |
| Responsible-AI / sustainability optimisation content for the sustainability option | travailler | not stated ('responsible / optimization modules', no link) | not stated |

### `m1p3-research-internship` — Research-Oriented Internship (Y1P3 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Experimental methodology: designing baselines and ablations, choosing a metric | industrie, travailler | not stated (the page names it as the research evidence bar but never teaches it) | not stated |
| Literature review and scientific writing (report or poster) | intro, industrie | not stated | not stated |
| Reproducible code practices (versioning, seeds, environments) | intro | not stated | not stated |
| Graph ML content (GNNs etc.) as a possible topic anchor | travailler, place | m1p2-graph-ml (named only as 'Graph ML'; 'Upstream: P1–P2') | graph-ml: OK |
| Optimal transport as a possible topic anchor | travailler | m1p2-optimal-transport (named only as 'OT') | optimal-transport: OPT-ONLY |
| LLM content as a possible topic anchor | travailler | not stated: 'LLM' is named, but the dedicated LLM course (m2-large-language-models) comes after this internship, so in M1 this can only be m1p2-nlp-te | M2:large-language-models: LATER; nlp-text-mining: OK; multimodal-genai: OPT-ONLY |
| Graph×LLM synthesis questions for framing a topic | place | home page #checkpoints | unnamed |

### `m2-large-language-models` — Large Language Models (CSC_53432_EP) (Y2P1 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| scaled dot-product and multi-head attention, residual connections, LayerNorm | ch0, ch2 | m1p1-deep-learning (ch. 6) | deep-learning: DL1-ONLY |
| basic BPE learning loop; WordPiece and Unigram (EM + Viterbi) | ch1 | m1p2-nlp-text-mining (ch. 1, 1.2) | nlp-text-mining: OK |
| static word embeddings (word2vec/GloVe, skip-gram, negative sampling) | ch0 | m1p2-nlp-text-mining (ch. 4) | nlp-text-mining: OK |
| TF-IDF and BM25 lexical retrieval | ch7 | m1p2-nlp-text-mining (ch. 2) | nlp-text-mining: OK |
| SBERT bi-encoder sentence embeddings; BERT/GPT as applications | ch3, ch7 | m1p2-nlp-text-mining (ch. 7) | nlp-text-mining: OK |
| MinHash signatures and LSH banding | ch3 | m1p2-nlp-text-mining (ch. 8.3) | nlp-text-mining: OK |
| NER / relation extraction and knowledge-graph construction | ch7 | m1p2-nlp-text-mining (ch. 6, ch. 9) | nlp-text-mining: OK |
| cross-entropy / maximum likelihood, perplexity, logistic regression | ch0, ch3, ch5 | m1p1-machine-learning (ch. 3) and m1p2-nlp-text-mining (ch. 0) | machine-learning: OK; nlp-text-mining: OK |
| policy gradients / REINFORCE, PPO clipping, critic/value function, advantage A = Q - V | ch5 | m1p2-reinforcement-learning (ch. 5) | reinforcement-learning: OK |
| bandits and exploration | ch4, ch5 | m1p2-reinforcement-learning (ch. 4) | reinforcement-learning: OK |
| perception-action loop for autonomous agents | ch8 | m1p2-reinforcement-learning (ch. 7) | reinforcement-learning: OK |
| GNN message passing (attention read as message passing on a token graph) | ch2 | m1p2-graph-ml (ch. 5) | graph-ml: OK |
| GraphRAG with community summaries over knowledge graphs | ch7, ch8 | m1p2-graph-ml (ch. 10) | graph-ml: OK |
| Vision Transformer patch embeddings | ch8 | m1p2-advanced-deep-learning (ch. 4) | advanced-deep-learning: OPT-ONLY |
| CLIP contrastive image-text alignment | ch8 | m1p2-multimodal-genai (ch. 5) | multimodal-genai: OPT-ONLY |
| GPU memory hierarchy (HBM vs SRAM) | ch2 | m1p1-signal-processing (cited, but that page never covers memory hierarchy) | signal-processing: OPT-ONLY |
| KL divergence and the variational (Gibbs) characterization used for the closed-form optimal policy | ch5, ex | not stated | not stated |
| Lagrange multipliers for constrained optimization | ch3, ex | not stated | not stated |
| Adam, mixed precision, learning-rate warmup | ch2, ch5 | not stated | not stated |
| linear state-space systems and matrix-exponential discretization | ch2 | not stated | not stated |
| approximate nearest-neighbour indexes (FAISS, HNSW) and vector databases | ch7 | not stated | not stated |
| ranking metrics (NDCG@10) and reciprocal rank fusion | ch7 | not stated | not stated |
| binomial distribution, CLT, z-test, p-values, statistical power | ch9, ex | not stated | not stated |
| rejection sampling (probability) | ch6 | not stated | not stated |
| Hessian-based second-order error compensation (OBS-style) behind GPTQ | ch6 | not stated | not stated |
| mel spectrograms and Whisper-style audio encoders | ch8 | not stated | not stated |
| LoRA / parameter-efficient fine-tuning and knowledge distillation | ch3, ch8, ex (Ex. 3) | page points to its own ch. 6, which does not cover them | unnamed |

### `m2-geometric-deep-learning` — Analysis and Deep Learning on Geometric Data (CSC_53431_EP) (Y2P1 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Graph Laplacian and its eigendecomposition | ch0, ch2, ch3 | m1p2-graph-ml | graph-ml: OK |
| Permutation invariance and message-passing GNNs | ch6, ch7 | m1p2-graph-ml | graph-ml: OK |
| Spectral graph filters / ChebNet | ch6 | m1p2-graph-ml | graph-ml: OK |
| Fourier transform, convolution and heat diffusion as low-pass filtering | ch0, ch2, ch5 | m1p1-signal-processing (cited as 'Signal Processing module', not linked; an M1 P1 Choose-3 elective) | signal-processing: OPT-ONLY |
| Triangle-mesh representation (vertices/edges/faces, mesh data structures, non-manifold meshes) | ch1, ch5 | m1p1-shapes (an M1 P1 Choose-3 elective on the 'sys' route, not the gllm route) | shapes: OPT-ONLY |
| Lagrange multipliers and compactness arguments | ch0 | L3 | L3 |
| MLPs, ReLU, backprop/SGD training and PyTorch | ch6, ch7, ex (Ex. 10-11) | not stated | not stated |
| SVD and orthogonal Procrustes | ch4, ch5 | not stated | not stated |
| Eigenvalue/eigenvector perturbation theory (Weyl, spectral-gap bounds) | ch3 | not stated | not stated |
| Eikonal equation, Dijkstra, Fast Marching | ch3 | not stated | not stated |
| Optimal transport, W1 and Gromov-Wasserstein | ch4, ch8, ex (Ex. 12) | m1p2-optimal-transport (ch. 5; a Choose-1 elective) | optimal-transport: OPT-ONLY |
| Laplacian eigenmaps / spectral positional encodings | ch3 | m2-advanced-gnn (ch. 4) | M2:advanced-gnn: SAME |
| Graph transformers / GPS recipe | ch6 | m2-advanced-gnn | M2:advanced-gnn: SAME |
| DDPM / diffusion generative models | ch7, ch8 | m1p2-multimodal-genai (ch. 3; elective) | multimodal-genai: OPT-ONLY |
| Self-supervised / contrastive pre-training and LLM pre-training | ch6, ch8 | not stated | not stated |
| Group representations / irreducible representations (SE(3)-transformers) | ch7 | not stated | not stated |
| Sparse linear systems / Poisson solvers | ch5 | not stated | not stated |
| Cauchy-Riemann equations / conjugate harmonic functions | ch5 | not stated | not stated |
| Retrieval and segmentation metrics (mAP, mIoU) | ch6, ex (Ex. 12) | not stated | not stated |

### `m2-advanced-gnn` — Advanced Graph Neural Networks (Y2P1 · TBC · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Message passing GNN layer, GCN / GraphSAGE / GAT | ch0, ch2, ch3, ch5 | m1p2-graph-ml | graph-ml: OK |
| Graph Laplacian L = D − A, spectrum, λ2, Chebyshev spectral filters, graph Fourier | ch0, ch3, ch4 | m1p2-graph-ml | graph-ml: OK |
| NeighborSampler, Cluster-GCN, GraphSAINT, bias/variance/memory trade-off | ch1 | m1p2-graph-ml | graph-ml: OK |
| Over-smoothing (geometric convergence to the mean) | ch0, ch3 | m1p2-graph-ml | graph-ml: OK |
| Permutation invariance/equivariance of layers and readouts | ch2, ch4 | m1p2-graph-ml | graph-ml: OK |
| DeepWalk / node2vec / NetMF node embeddings | ch7, ch9 | m1p2-graph-ml | graph-ml: OK |
| Link prediction with negative sampling, graph auto-encoders, PinSage | ch1, ch6 | m1p2-graph-ml | graph-ml: OK |
| PageRank / personalized PageRank damping | ch3 | m1p2-graph-ml | graph-ml: OK |
| GraphRAG pipeline, Leiden communities, NLGraph, pseudo-code prompting | ch7, ch8, ch9 | m1p2-graph-ml | graph-ml: OK |
| Graph diffusion generation (DiGress), MMD evaluation of generated graphs | ch2, ch9 | m1p2-graph-ml | graph-ml: OK |
| Distributed training: parameter server vs all-reduce | ch1 | m1p1-emerging-ml | emerging-ml: OK-ROUTE |
| Temporal train/test split hygiene | ch6 | m1p1-emerging-ml (not actually found on that page) | emerging-ml: OK-ROUTE |
| Wasserstein-1 distance / optimal transport plans | ch3 | m1p2-optimal-transport | optimal-transport: EXCL(gllm) |
| Individual vs group fairness tensions | ch7 | m1p2-optimal-transport | optimal-transport: EXCL(gllm) |
| Cheeger inequality, conductance, Tanner bound | ch3 | not stated | not stated |
| Transformer self-attention, multi-head attention, positional encodings for tokens | ch4, ch5 | not stated | not stated |
| Efficient / long-context attention (sparse, kernel, hashing) | ch5 | m2-large-language-models | M2:large-language-models: SAME |
| GRU / RNN sequence encoders, Time2Vec | ch6, ch9 | not stated | not stated |
| Meta-gradients / MAML (bilevel unrolled optimization) | ch7 | "RL/Deep Learning module" (MAML appears on no other page of the repo) | unnamed |
| Differential privacy definition, sensitivity, Laplace mechanism | ch7, ex | not stated (taught in m1p1-emerging-ml ch5 and m2-privacy-uncertainty) | emerging-ml: OK-ROUTE; M2:privacy-uncertainty: SAME |
| Randomized smoothing for certified robustness | ch7 | not stated (m2-security-robustness) | M2:security-robustness: LATER |
| Group equivariance, E(3)/SE(3), the geometric deep learning blueprint | ch4, ch8 | m2-geometric-deep-learning | M2:geometric-deep-learning: SAME |
| Latent / continuous diffusion models | ch9 | m1p2-multimodal-genai (via M1 Graph ML ch. 9.5) | multimodal-genai: OK-ROUTE |
| LLM embedding space, soft prompts, contrastive alignment | ch8 | not stated | not stated |
| Bayesian hyperparameter search, paired significance tests | ch1 | not stated | not stated |
| Classical algorithms (CLRS), BFS shortest paths | ch5, ch8 | m1p1-refresher-cs | refresher-cs: OK |

### `m2-privacy-uncertainty` — Privacy and Uncertainty Quantification (Y2P1 · TBC · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Concentration inequalities (Markov, Chernoff/Hoeffding) | ch0, ch3 | m1p1-machine-learning (ch. 0) | machine-learning: OK |
| Azuma / martingale concentration (advanced composition proof sketch) | ch3 | not stated | not stated |
| First encounter with epsilon-DP, Laplace noise, DP-SGD | ch0, ch1, ch4 | m1p1-emerging-ml (ch. 5) | emerging-ml: OPT |
| Federated learning | ch4, ch11 | m1p1-emerging-ml (ch. 3) | emerging-ml: OPT |
| Measure-theoretic tools: Radon-Nikodym derivative dP/dQ, regular conditional probability | ch1, ch3 | not stated | not stated |
| SGD, mini-batches, dropout | ch4, ch8 | m1p1-deep-learning (ch. 3 and 8) | deep-learning: DL1-ONLY |
| Softmax, logits, cross-entropy / NLL | ch7, ch9 | not stated (implicitly m1p1-deep-learning) | deep-learning: DL1-ONLY |
| Generalization theory, bias-variance | ch0, ch6 | m1p1-machine-learning (ch. 8) | machine-learning: OK |
| Evaluation curves, ROC/AUC | ch5, ch7 | m1p1-machine-learning (ch. 4) | machine-learning: OK |
| Bayesian inference (prior, posterior) | ch8 | m1p1-refresher-statistics (ch. 8) | refresher-statistics: OK |
| KL divergence and variational inference; deep Gaussian processes | ch8 | not stated | not stated |
| Confidence intervals, tests, p-values, bootstrap / plug-in principle | ch0, ch8, ch9 | m1p1-refresher-statistics (ch. 4, 6); m1p2-statistics-in-action (ch. 8, 9) | refresher-statistics: OK; statistics-in-action: OFF |
| Data drift in production | ch6 | m1p1-machine-learning (ch. 9) | machine-learning: OK |
| RLHF / alignment, token sampling temperature, chain-of-thought | ch11 | m2-large-language-models (ch. 9 cited; RLHF itself not cited) | M2:large-language-models: SAME |
| Perplexity of a language model | ch5 | not stated | not stated |
| Natural language inference (NLI) models for semantic clustering | ch11 | not stated | not stated |
| RAG | ch11 | not stated | not stated |
| Bloom filters, count-mean sketch, Hadamard transform | ch4, ch5 | not stated | not stated |
| Linear programming (quantile regression for linear models) | ch10 | not stated | not stated |
| CNNs / ResNet on CIFAR-10, MNIST training | ex (Ex. 3c, Ex. 5) | not stated | not stated |

### `m2-boosting-foundation-tabular` — From Boosting to Foundation Models: learning with Tabular Data (Y2P1 · TBC · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| CART trees, impurity criteria, bias-variance decomposition, bagging and random forests | ch0, ch1, ch2, ch3 | m1p1-machine-learning | machine-learning: OK |
| AdaBoost (reweighting, weighted vote); the page credits ML ch. 6 for it, but that chapter does not present AdaBoost | ch0, ch2 | m1p1-machine-learning | machine-learning: OK |
| Cross-validation, data leakage, benchmark protocols | ch0, ch4, ch9 | m1p1-machine-learning | machine-learning: OK |
| Second-order Taylor expansion, convex losses (log-loss derivatives) | ch2, ch3 | not stated | not stated |
| Multi-head attention and the transformer block | ch5, ch6 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| In-context / few-shot learning of LLMs (the cited M2 LLM module never covers it) | ch6, ch7 | m2-large-language-models | M2:large-language-models: SAME |
| Bayesian posterior predictive, priors over functions | ch6 | not stated | not stated |
| Structural causal models / random DAGs | ch6, ex (Ex 8) | not stated | not stated |
| AUC / ROC metrics | ch4, ch9, ex | not stated | not stated |
| Sparsemax / entmax | ch5 | not stated | not stated |
| Greedy graph colouring | ch3, ex (Ex 4) | not stated | not stated |
| GAN / VAE training | ch8, ex (Ex 6) | not stated | not stated |
| Gaussian and multinomial diffusion (DDPM); the page cites the Image Synthesis module, but diffusion is taught in m1p2-multimodal-genai ch. 3 | ch8, ex (Ex 6) | m1p2-image-synthesis | image-synthesis: OPT |
| Differential privacy, (epsilon, delta), Gaussian mechanism on gradients (DP-SGD) | ch8, ex (Ex 6) | m1p1-emerging-ml | emerging-ml: OPT |
| Membership inference attacks | ch8, ex (Ex 6) | m2-security-robustness | M2:security-robustness: LATER |
| Memorization in language models | ch8 | m2-large-language-models | M2:large-language-models: SAME |
| LLM tokenization of numbers, context window | ch7 | not stated | not stated |
| SQL, relational schemas, joins (taught in m1p1-dbms ch. 2, which the page does not cite) | ch7, ex (Ex 5) | not stated | not stated |
| Paired statistical tests (permutation test, corrected resampled t-test) | ch9, ex (Ex 7) | not stated | not stated |
| Hyperparameter optimisation (Optuna / TPE search) | ch9, ex (Ex 7) | not stated | not stated |
| KS / total-variation distances, real-vs-synthetic detectability classifier | ch8, ex (Ex 6) | not stated | not stated |
| Impurity-based feature importance and why it misleads | intro (How to study), ex (Ex 3) | not stated | not stated |
| Predictive uncertainty / abstention | ch6 | not stated | not stated |

### `m2-control-generative-ai` — Control in Generative AI (Y2P1 · TBC · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Autoregressive factorization, softmax over vocabulary, temperature/top-k/top-p sampling | ch0, ch3, ch4, ch6 | m2-large-language-models | M2:large-language-models: SAME |
| BPE subword tokenization | ch3, ex (Ex. 1) | m2-large-language-models | M2:large-language-models: SAME |
| Transformer residual stream, layer-wise activations, unembedding matrix W_U | ch4, ex (Ex. 3) | not stated | not stated |
| SFT, reward-model training, PPO-based RLHF, GRPO; Bradley-Terry preference model behind DPO | ch5 | m2-large-language-models | M2:large-language-models: SAME |
| KL divergence, entropy, Lagrange multipliers over distributions | ch5, ch9, ex (Ex. 4) | not stated | not stated |
| DDPM, noise prediction, score parametrization, noise schedule alpha-bar_t | ch7 | m1p2-multimodal-genai | multimodal-genai: OK-ROUTE |
| DDIM deterministic sampler and inversion; classifier guidance | ch7 | m1p2-multimodal-genai | multimodal-genai: OK-ROUTE |
| UNet blocks, cross-attention, latent text-to-image diffusion (Stable Diffusion) | ch7, ex (Ex. 5) | m1p2-multimodal-genai | multimodal-genai: OK-ROUTE |
| Graph generators GraphRNN, DeepGMG, NeVAE, GraphAF (normalizing flows), DiGress (discrete diffusion) | ch0, ch2, ch8 | m2-graph-generative-models (Y2 P2, i.e. taught after this course) and m1p2-graph-ml ch. 9 | M2:graph-generative-models: LATER; graph-ml: OK |
| Hypothesis testing (type I/II error, p-value, power), binomial CLT (De Moivre-Laplace), sample-size formula for a proportion | ch6, ex (Ex. 2) | m1p1-refresher-statistics | refresher-statistics: OK |
| Pseudo-random functions / keyed hashing | ch6 | not stated | not stated |
| FID, LPIPS, self-BLEU, FCD, MMD, validity/uniqueness/novelty | ch8, ch9 | m1p2-multimodal-genai ch. 7; m2-graph-generative-models ch. 6 | multimodal-genai: OK-ROUTE; M2:graph-generative-models: LATER |
| Context-free grammars, EBNF, incremental parsing (pushdown automata) | ch3, ch10 | not stated | not stated |
| Prompt injection and jailbreaks | ch10 | m2-explainability-security-privacy-llms (Y2 P2, downstream) | M2:explainability-security-privacy-llms: LATER |
| Hugging Face generation API (LogitsProcessor), GPT-2 model loading | ex (Ex. 1, Ex. 3) | not stated | not stated |
| Exponential family, log-partition function and its derivatives | ex (Ex. 4) | not stated | not stated |

### `m2-projet-transverse` — Transverse project (experience-based learning) (Y2 all-year · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Project management practice (backlog, milestones, review cycles) | industrie | not stated (would fit m1p2-startup-entrepreneurship / m1p1-strategy-marketing) | startup-entrepreneurship: OFF; strategy-marketing: OK |
| Integrating ML/LLM models into a product (serving, deployment, evaluation in production) | industrie | not stated (would fit m2-mlops-llm-engineering, m2-large-language-models) | M2:mlops-llm-engineering: LATER; M2:large-language-models: OK |
| Graph×LLM methods (GNNs, LLMs, their coupling) | travailler | not stated; refers only to home index.html#checkpoints (would fit m1p2-graph-ml, m1p2-nlp-text-mining, m2-large-language-models, m2-advanced-gnn) | graph-ml: OK; nlp-text-mining: OK; M2:large-language-models: OK; M2:advanced-gnn: OPT-ONLY |
| Reproducible research practice (experiment tracking, ablations, open-source release) | industrie | not stated (closest is m1p3-research-internship) | research-internship: OK |
| All M1 P1–P2 and M2 course content, research internship experience | place | not stated by slug ("capitalizes on M1 P1–P2 + research internship + M2 courses") | not stated |

### `m2-ethical-issues-ai` — Ethical Issues and Novel Applications of AI (Y2 all-year · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| LLM agents, multimodal generative systems and Graph x LLM pipelines (the 'novel applications' whose impact surface is discussed) | intro, industrie | not stated (#place names 'M2 LLMs, GNN, geometric DL' as parallel without links; corresponding slugs: m2-large-language-models, m2-advanced-gnn, m2-ge | M2:large-language-models: OK; M2:advanced-gnn: OPT-ONLY; M2:geometric-deep-learning: OK |
| privacy attacks (membership inference, data leakage) and sensitive relational data | intro, industrie, travailler | m2-privacy-uncertainty, m2-explainability-security-privacy-llms | M2:privacy-uncertainty: OPT-ONLY; M2:explainability-security-privacy-llms: LATER |
| product red-teaming, robustness, usage policies | industrie, travailler | m2-security-robustness, m2-explainability-security-privacy-llms | M2:security-robustness: LATER; M2:explainability-security-privacy-llms: LATER |
| fairness (notions and metrics) and algorithmic bias | intro, industrie | not stated ('possible responsible modules in P2'; closest module: m1p2-responsible-ai-sustainability) | responsible-ai-sustainability: OFF |
| explainability of models | intro, travailler | m2-explainability-security-privacy-llms | M2:explainability-security-privacy-llms: LATER |

### `m1-humanites` — Humanities (Y2 all-year · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Corpus and narrative bias (named as something to be sensitive to, never defined) | industrie | not stated | not stated |
| Leaderboard/benchmark culture in ML papers | intro | not stated | not stated |
| ML/DL foundation (AI seen as loss minimization) | place | not stated (M1 ML/DL foundation courses in general) | not stated |
| AI ethics discussion that the humanities 'feed' | place | m2-ethical-issues-ai | M2:ethical-issues-ai: SAME |
| Master's artefacts (model, dataset, agent demo) to tie themes to | travailler | not stated | not stated |

### `m1-langues` — Languages (Y2 all-year · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| attention (the vocabulary to reuse in talks) | travailler | not stated | not stated |
| message-passing (GNN vocabulary) | travailler | not stated | not stated |
| calibration | travailler | not stated | not stated |
| LLM/GNN research literature (the readings scientific English is meant for) | place | not stated | not stated |
| what the campus language programme offers (units, levels, schedule) | travailler | not stated | not stated |

### `m2-mlops-llm-engineering` — ML Ops and LLM Engineering Principles (Y2P2 · TBC · route gllm/sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Hoeffding's inequality (proof) | ch2 | m1p1-machine-learning | machine-learning: OK |
| autoregressive decoding, KV cache, GQA, quantization (GPTQ/AWQ), inference serving | ch3, ch4, ch10 | m2-large-language-models | M2:large-language-models: OK |
| tokenization (BPE) and token counts per language | ch4 | m2-large-language-models | M2:large-language-models: OK |
| RAG pipeline: chunking, embeddings, vector index, hybrid BM25 + dense retrieval, cross-encoder reranking | ch6, ch10 | m2-large-language-models (ch. 7) and m1p2-nlp-text-mining (ch. 2, 7) | M2:large-language-models: OK; nlp-text-mining: OK |
| SFT, RLHF/DPO post-training | ch7 | m2-large-language-models | M2:large-language-models: OK |
| LoRA mechanics beyond the two-line recap. The page says the LLMs module does not cover it but does not point to m1p1-deep-learning §7.3, which does. | ch7 | not stated | not stated |
| LLM agents (observation, reasoning, tool-action loop, planning) | ch8 | m2-large-language-models | M2:large-language-models: OK |
| multi-armed bandits for A/B testing and cost/quality model routing | ch0, ch4 | m1p2-reinforcement-learning | reinforcement-learning: OK |
| Kolmogorov-Smirnov two-sample test | ch5 | m1p1-refresher-statistics (which does not cover it) | refresher-statistics: OK |
| MMD (maximum mean discrepancy) | ch5 | m1p1-machine-learning (which does not cover it; MMD appears in m1p1-deep-learning, m1p2-optimal-transport, m1p2-graph-ml) | machine-learning: OK; deep-learning: DL1-ONLY; optimal-transport: EXCL(gllm/sys); graph-ml: OK |
| ADWIN stream drift detector | ch5 | not stated | not stated |
| tensor parallelism / multi-GPU replicas | ch3 | m1p1-emerging-ml (ch. 2) | emerging-ml: PART-ROUTE |
| subgroup fairness metrics (slices) | ch2, ch5 | m1p1-emerging-ml (ch. 6) | emerging-ml: PART-ROUTE |
| GraphRAG: LLM entity extraction, Leiden communities, map-reduce over summaries | ch6, ch10 | m1p2-graph-ml (ch. 10) | graph-ml: OK |
| direct and indirect prompt injection, backdoors, memorization/extraction, membership inference, AI Act | ch5, ch7, ch8, ch9 | m2-explainability-security-privacy-llms (ch. 5-10) | M2:explainability-security-privacy-llms: SAME |
| containers (Docker), queues, git, unit testing | ch1, ch2, ch3, ch9 | m1p1-refresher-cs | refresher-cs: OK |
| Kubernetes HPA, Prometheus, CI YAML (GitHub Actions) | ch2, ch3, ch10 | not stated | not stated |
| binomial confidence intervals and paired significance tests | ch2 | not stated | not stated |
| PyTorch training loops, GPU memory, checkpoints | ch0, ch7 | m1p1-deep-learning / m1p2-deep-learning-p2 | deep-learning: DL1-ONLY; deep-learning-p2: EXCL(gllm) |
| carbon accounting (PUE, electricity mix) | ch10 | not stated (m1p2-responsible-ai-sustainability covers it but is not linked) | responsible-ai-sustainability: OFF |

### `m2-security-robustness` — Fundamentals of Security and Robustness for AI (Y2P2 · TBC · route gllm/sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| SGD, backpropagation, softmax / cross-entropy, CNNs | ch0, ch2, ch3, ch4 | m1p1-deep-learning | deep-learning: DL1-ONLY |
| empirical vs true risk, overfitting, generalization theory | ch0, ch4 | m1p1-machine-learning (ch. 8) | machine-learning: OK |
| hypothesis testing, type I/II errors, Neyman-Pearson lemma | ch5, ch8 | m1p1-refresher-statistics | refresher-statistics: OK |
| Gaussian CDF and its inverse, Clopper-Pearson binomial confidence interval | ch5, ex (Ex. 5) | not stated | not stated |
| Hölder inequality and dual norms (L1 / Linf), Cauchy-Schwarz | ch2, ch3, ch4 | not stated | not stated |
| SVM / hinge loss and logistic regression | ch4, ch7, ch8 | not stated (taught in m1p1-machine-learning ch. 3) | machine-learning: OK |
| differential privacy (eps, delta), Gaussian mechanism, composition, group privacy, DP-SGD | ch5, ch7, ch8, ex (Ex. 8) | m1p1-emerging-ml (ch. 5); m2-privacy-uncertainty | emerging-ml: PART-ROUTE; M2:privacy-uncertainty: OFF-ROUTE |
| federated learning, Byzantine clients, robust aggregation (trimmed mean, coordinate-wise median) | ch6, ch7, ex (Ex. 7) | m1p1-emerging-ml (ch. 4) | emerging-ml: PART-ROUTE |
| KL divergence (TRADES regularizer) | ch4 | not stated | not stated |
| implicit function theorem, Hessian-vector products, LiSSA | ch7 | not stated | not stated |
| PCA / SVD of an activation matrix | ch6 | not stated (m1p1-machine-learning ch. 7) | machine-learning: OK |
| transfer learning / fine-tuning on pretrained features | ch6 | not stated (m1p1-deep-learning ch. 7) | deep-learning: DL1-ONLY |
| linear programming | ch8, ex (Ex. 3) | not stated | not stated |
| ROC curve, TPR/FPR, knowledge distillation | ch8, ex (Ex. 3, Ex. 8) | not stated | not stated |
| GNN message passing / GCN on citation graphs | ch9 | m2-advanced-gnn (ch. 7) | M2:advanced-gnn: PART-ROUTE |
| LLM tokens, jailbreaks, prompt injection, RLHF, agents / RAG | ch9, ex (Ex. 9) | m2-explainability-security-privacy-llms (listed as a prerequisite in ch0, although the intro calls it downstream) | M2:explainability-security-privacy-llms: SAME |
| decision trees / GBDTs as piecewise-constant functions | ch2, ch5, ch9, ch10 | not stated (m2-boosting-foundation-tabular, m1p1-machine-learning ch. 6) | M2:boosting-foundation-tabular: OFF-ROUTE; machine-learning: OK |
| drift / OOD detection, data lineage, monitoring | ch7, ch10 | m2-mlops-llm-engineering | M2:mlops-llm-engineering: SAME |
| AI Act risk classification | ch10 | m2-explainability-security-privacy-llms (ch. 10) | M2:explainability-security-privacy-llms: SAME |

### `m2-graph-generative-models` — Graph Generative Models and Applications (Y2P2 · TBC · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Message passing, MPNN, GIN, 1-WL expressivity bound | ch0, ch2, ch3, ch4, ch5, ch9 | m2-advanced-gnn (ch. 2); m1p2-graph-ml | M2:advanced-gnn: OK-ROUTE; graph-ml: OK |
| Graph transformers / global attention layers | ch4, ch5 | m2-advanced-gnn (ch. 5) | M2:advanced-gnn: OK-ROUTE |
| VAE and ELBO derivation, KL to N(0,I) prior | ch3, ch10 | m1p2-multimodal-genai (ch. 1) | multimodal-genai: OK-ROUTE |
| Continuous diffusion (DDPM / score matching), DDIM, latent diffusion | ch5, ch8, ch9 | m1p2-multimodal-genai (ch. 3-4) | multimodal-genai: OK-ROUTE |
| Classifier-free guidance | ch5, ch7, ex | m1p2-multimodal-genai (ch. 4) | multimodal-genai: OK-ROUTE |
| FID (image analogue of FCD) | ch0, ch6 | m1p2-multimodal-genai (ch. 7) | multimodal-genai: OK-ROUTE |
| Kernel methods / RKHS norm (needed to read MMD) | ch6 | not stated | not stated |
| Wasserstein-2 distance between Gaussians, matrix square root | ch6, ex | not stated | not stated |
| Gromov-Wasserstein distance | ch6, ch10 | m1p2-optimal-transport | optimal-transport: EXCL(gllm) |
| Martingale convergence theorem, De Finetti theorem | ch1 | m1p1-refresher-statistics (which does not actually cover martingales) | refresher-statistics: OK |
| Multivariate change of variables / Jacobian determinant | ch4 | m1p1-refresher-statistics (Jacobians chapter) | refresher-statistics: OK |
| RNNs and LSTMs | ch2, ch9 | not stated | not stated |
| BERT masked LM, T5 seq2seq pre-training | ch5, ch7 | m2-large-language-models (ch. 3) | M2:large-language-models: OK |
| LLM agents and tool calling | ch2, ch7, ch9 | m2-large-language-models (ch. 8) | M2:large-language-models: OK |
| Reinforcement learning policy optimization (REINVENT-style RL on SMILES) | ch8 | not stated | not stated |
| Bayesian optimization in a latent space | ch7, ch8 | not stated | not stated |
| Constrained decoding with masks/automata; fidelity/diversity entropy bound (Thm 9.2) | ch3, ch7, ch8, ch10, ex | m2-control-generative-ai (ch. 3, 8, 9) | M2:control-generative-ai: OK-ROUTE |
| Differential privacy, Gaussian mechanism | ch8 | m1p1-emerging-ml (ch. 5); m2-privacy-uncertainty | emerging-ml: OK-ROUTE; M2:privacy-uncertainty: OFF-ROUTE |
| Membership inference attacks | ch8, ch10 | m2-security-robustness | M2:security-robustness: SAME |
| Euclidean / translation equivariance (EDM, crystals) | ch5, ch8 | m2-geometric-deep-learning | M2:geometric-deep-learning: OK |
| Random graph models ER, SBM, Barabasi-Albert; graphons | ch0, ch1, ex | m1p2-graph-ml (ch. 9) | graph-ml: OK |
| Graph Laplacian spectrum as a graph feature | ch9, ex | not stated | not stated |
| Chemistry basics: valence, aromaticity, logP, QED, SA score, docking, ADMET | ch3, ch7, ch8 | not stated | not stated |
| Bootstrap confidence intervals, Hoeffding concentration | ch6, ex | not stated | not stated |
| Gumbel-softmax / straight-through estimator | ex (ex. 6) | not stated | not stated |
| Hungarian algorithm / graph matching | ch3, ch9 | not stated | not stated |
| Generalization theory and sample complexity | ch8, ch10 | m1p1-statistical-learning-theory; m1p1-machine-learning (ch. 8) | statistical-learning-theory: OFF; machine-learning: OK |

### `m2-explainability-security-privacy-llms` — Explainability, Security, Privacy of LLMs (Y2P2 · TBC · route gllm/sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Transformer internals: multi-head attention, residual stream, LayerNorm, unembedding W_U | ch1, ch2, ch3 | m2-large-language-models (ch. 2) and m1p1-deep-learning (ch. 6) | M2:large-language-models: OK; deep-learning: DL1-ONLY |
| Post-training SFT / RLHF / DPO (refusals as learned behaviour) | ch0, ch5, ch6, ch10 | m2-large-language-models (ch. 4-5) | M2:large-language-models: OK |
| (epsilon,delta)-DP definition, Gaussian mechanism, composition | ch8 | m1p1-emerging-ml (ch. 5); sibling m2-privacy-uncertainty | emerging-ml: PART-ROUTE; M2:privacy-uncertainty: OFF-ROUTE |
| Moments accountant / Renyi DP accounting | ch8, ex 9 | not stated (only named; taught in m2-privacy-uncertainty ch. 3) | M2:privacy-uncertainty: OFF-ROUTE |
| LIME and SHAP basics (KernelSHAP, TreeSHAP) | ch4 | 'M1 recap' (no M1 module on the site teaches LIME/SHAP feature attribution; m1p1-emerging-ml ch. 6 only uses Shapley values for data valuation) | emerging-ml: PART-ROUTE |
| Hypothesis testing, type I/II errors, CLT, Gaussian quantiles, ROC | ch8, ch9, ch10 | m1p1-refresher-statistics | refresher-statistics: OK |
| Logistic regression / linear classifiers, train/test split | ch1 | not stated (m1p1-machine-learning) | machine-learning: OK |
| Autoencoders | ch3 | not stated (m1p1-deep-learning ch. 9) | deep-learning: DL1-ONLY |
| RAG pipeline (retrieval, context injection) | ch0, ch4, ch5, ch6, ex 8 | not stated (m2-large-language-models ch. 7) | M2:large-language-models: OK |
| Tokenization and special tokens | ch5 | m2-large-language-models (ch. 1) | M2:large-language-models: OK |
| In-context learning | ch2 | m2-large-language-models ch. 3 (not actually treated there) | M2:large-language-models: OK |
| Perplexity, logits, sampling temperature | ch7, ch8, ch9 | not stated (m2-large-language-models) | M2:large-language-models: OK |
| Named-entity recognition | ch9 | m1p2-nlp-text-mining (ch. 6) | nlp-text-mining: OK |
| CI/CD for ML, monitoring, registries, sandboxing, supply chain | ch6, ch10 | m2-mlops-llm-engineering (ch. 2, 5, 8, 9) | M2:mlops-llm-engineering: SAME |
| Adversarial ML vocabulary (threat models, backdoors, model stealing, MIA) | ch5, ch6 | m2-security-robustness (assumed 'in broad outline') | M2:security-robustness: SAME |
| Activation patching / ablation methodology (TransformerLens) | ch1, ch2, ex 6 | not stated | not stated |
| LLM fine-tuning (full or LoRA) on a small corpus | ch7, ch8, ex 2, ex 9 | not stated (m2-large-language-models / m2-mlops-llm-engineering ch. 7) | M2:large-language-models: OK; M2:mlops-llm-engineering: SAME |
| GDPR concepts (personal data, pseudonymization) | ch9, ch10 | not stated | not stated |

### `m2-speech-technology` — Speech Technology for Conversational AI (Y2P2 · TBC · route sys)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Sampling theorem, STFT/Gabor windows, Mel filter bank and MFCC (recap only, no derivation) | ch0, ch1, ch6 | m1p1-signal-processing | signal-processing: OK-ROUTE |
| Power spectral density, periodogram (energy VAD, spread-spectrum watermark) | ch5, ch9 | m1p1-signal-processing | signal-processing: OK-ROUTE |
| LSTM/BLSTM, dot-product attention, transformer encoder-decoder | ch3, ch4, ch7 | m1p1-deep-learning | deep-learning: EXCL(sys: DL in P2) |
| EM / Baum-Welch training of latent-variable models and Gaussian mixtures | ch1 | m1p1-machine-learning | machine-learning: OK |
| n-gram language models (smoothing, LM rescoring/shallow fusion) | ch1, ch2 | m1p2-nlp-text-mining | nlp-text-mining: OK |
| HMM forward-backward (taught in NLP M1 ch. 6, which the page does not cite) | ch1, ch2 | not stated | not stated |
| GAN training, discriminators | ch6, ch7 | m1p2-multimodal-genai | multimodal-genai: EXCL(sys) |
| VAE / ELBO | ch7 | m1p2-multimodal-genai | multimodal-genai: EXCL(sys) |
| DDPM, noise prediction, number of sampling steps | ch7 | m1p2-multimodal-genai | multimodal-genai: EXCL(sys) |
| Normalizing flows / change of variables | ch7 | m2-graph-generative-models | M2:graph-generative-models: SAME |
| Conditional flow matching (Voicebox objective never written) | ch7 | not stated | not stated |
| Masked inpainting in discrete diffusion (DiGress analogy) | ch7 | m2-graph-generative-models | M2:graph-generative-models: SAME |
| Teacher forcing, cross-entropy, exposure bias, beam search | ch2, ch3, ch7 | not stated | not stated |
| Dilated / transposed / depthwise convolutions, GLU/SiLU, relative positional encoding | ch3, ch6 | not stated | not stated |
| Self-supervised speech representations (wav2vec 2.0 contrastive, HuBERT masked prediction) | ch3, ch10, ch11 | not stated | not stated |
| Vector quantization / VQ-VAE codebooks | ch11 | not stated | not stated |
| Multimodal LLM adapters (audio-in, projection into the LLM embedding space) | ch11 | m2-large-language-models | M2:large-language-models: OK |
| Speculative decoding | ex (Ex. 5b) | m2-large-language-models | M2:large-language-models: OK |
| LoRA adaptation | ch11 | m2-mlops-llm-engineering | M2:mlops-llm-engineering: SAME |
| Text watermarking (green/red lists, hypothesis test) | ch9 | m2-control-generative-ai | M2:control-generative-ai: OFF-ROUTE |
| Steering vectors and the hard/soft control taxonomy | ch5, ch8, ch11 | m2-control-generative-ai | M2:control-generative-ai: OFF-ROUTE |
| Fidelity/diversity trade-off curves and robustness budget under attack | ch5, ch7, ch9, ex | m2-control-generative-ai | M2:control-generative-ai: OFF-ROUTE |
| ROC curve / AUC | ch9, ex (Ex. 6) | not stated | not stated |
| Levenshtein edit distance (dynamic programming) | ch0, ex (Ex. 1) | not stated | not stated |
| Sequential change-point / hypothesis testing | ch10 | not stated | not stated |
| Psychoacoustic masking, mu-law companding | ch6, ch9 | not stated | not stated |
| Speaker verification (GE2E loss named, never defined) | ch9 | not stated | not stated |
| HuggingFace transformers ASR/TTS pipelines | ex (Ex. 1, 2) | not stated | not stated |

### `m2-advanced-topics-llms` — Advanced Topics in Large Language Models (Y2P2 · TBC · route gllm)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Transformer decoder architecture, attention, KV cache, perplexity | ch3, ch5, ch6, ch7 | m2-large-language-models | M2:large-language-models: OK |
| GRPO / PPO policy-gradient objectives (needed to implement the mini-GRPO of Ex. 5) | ch2, ex | m2-large-language-models (ch. 5); m1p2-reinforcement-learning (ch. 5) | M2:large-language-models: OK; reinforcement-learning: OK |
| Reward models, RLHF/DPO, reward hacking | ch2 | m2-large-language-models (ch. 4-5) | M2:large-language-models: OK |
| RAG pipeline, dense retrieval, vector stores, embeddings with cosine similarity | ch3, ch4 | m2-large-language-models (ch. 7); m2-mlops-llm-engineering (ch. 6) | M2:large-language-models: OK; M2:mlops-llm-engineering: SAME |
| GNN message passing (the encoder in G-Retriever) | ch8 | m1p2-graph-ml (ch. 5) | graph-ml: OK |
| Community detection (Leiden) and the GraphRAG foundations | ch4, ch8 | m1p2-graph-ml (ch. 10) | graph-ml: OK |
| Prize-collecting Steiner tree optimisation | ch8, ex | not stated | not stated |
| Parallel prefix scan (Blelloch algorithm) | ch6, ex | m1p1-refresher-cs (that page does not cover it) | refresher-cs: OK |
| FFT, convolution, spectral view and aliasing | ch3, ch6 | m1p1-signal-processing | signal-processing: OFF-ROUTE |
| RNN / LSTM recurrence | ch6 | m1p1-deep-learning (ch. 5) | deep-learning: OK-ROUTE |
| HiPPO structured state matrices; linear attention (Mamba-2/SSD) | ch6 | not stated | not stated |
| Optimal Brain Surgeon / Optimal Brain Damage, Hessian inverse, Cholesky decomposition | ch7 | m1p1-machine-learning, regularization chapter (OBS/OBD is not covered there) | machine-learning: OK |
| Online softmax / blockwise (Flash) attention, needed for ring attention and Ex. 7 | ch3, ex | not stated (FlashAttention is in m2-large-language-models ch. 2) | M2:large-language-models: OK |
| Concentration inequalities (Hoeffding) for leaderboard variance | ch1 | m2-mlops-llm-engineering (ch. 2); m1p1-refresher-statistics | M2:mlops-llm-engineering: SAME; refresher-statistics: OK |
| Monte Carlo marginalization | ch2 | m1p1-machine-learning ('ML module') | machine-learning: OK |
| Learning to rank / search-engine reranker signal fusion | ch4 | m1p2-nlp-text-mining (ch. 2, which covers only BoW/TF-IDF/BM25) | nlp-text-mining: OK |
| Distributed / expert-parallel training communication | ch5 | m1p1-emerging-ml (ch. 2) | emerging-ml: OK-ROUTE |
| LoRA, fine-tuning ops, catastrophic forgetting | ch10 | m2-mlops-llm-engineering (ch. 2, 7) | M2:mlops-llm-engineering: SAME |
| Prompt injection, least-privilege defences | ch9 | 'Security module' ch. 5-6 (= m2-explainability-security-privacy-llms); m2-mlops-llm-engineering ch. 8-9 | M2:explainability-security-privacy-llms: SAME; M2:mlops-llm-engineering: SAME |
| Linear probes, sparse autoencoders, AI Act GPAI obligations | ch10 | 'Security module' ch. 1-3 and 10 (= m2-explainability-security-privacy-llms) | M2:explainability-security-privacy-llms: SAME |
| Serving economics: continuous batching, prefix caching, euros per token | ch5, ch7, ch10 | m2-mlops-llm-engineering (ch. 3-4) | M2:mlops-llm-engineering: SAME |

### `m2-internship` — Internship — end-of-studies internship (Y2P3 · MAND · route —)

| Concept assumed | Used in | Named source | Verdict |
|---|---|---|---|
| Graph×LLM track exit skills / 'skill checkpoints' | intro | index (#checkpoints) | unnamed |
| Content of the M1 research internship (used as the comparison baseline) | place | m1p3-research-internship | research-internship: OK |
| M2 specialization modules (which ones is not stated) | place | not stated | not stated |
| Ethics framing of deployment decisions | place, industrie, travailler | not stated (named 'M2 ethics' / 'ethics seminar', i.e. m2-ethical-issues-ai, but not linked) | M2:ethical-issues-ai: OK |
| Management framing (P1/P2 management units) | industrie | not stated (P1/P2 management, i.e. m1p1-strategy-marketing and the P2 management units, not linked) | strategy-marketing: OK |
| Productionization, ops integration and impact measurement of ML systems | place, industrie | not stated (would come from m2-mlops-llm-engineering) | M2:mlops-llm-engineering: OPT-ONLY |
| CIFRE industrial PhD scheme | industrie | not stated | not stated |
| Transverse project experience | place | not stated (named 'transverse project', i.e. m2-projet-transverse, not linked) | M2:projet-transverse: OK |
