# LLGA objectives coverage: objective x course matrix

Lens: objectives coverage. Read-only analysis of `/home/user/polytechnique-llga` (home curriculum tree and route tags `data-p` in `index.html`; per-course records in `the per-course reader records`; course pages `courses/<slug>/index.qmd` opened to check Graph ML ch10, LLM 7.4/8.2/ch9 and session plans, NLP ch6-ch7, DL P1 ch9, and the ethics, transverse-project and internship pages). Date of analysis: 2026-10-22.

## 1. Objectives and scoring rubric

| Id | Objective (from the official description quoted on the home page) |
|---|---|
| O1 | ML & DL foundations: statistical learning, optimisation, neural architectures and training |
| O2 | Generative modelling theory: probabilistic models, VAEs, GANs, flows, diffusion, autoregressive models |
| O3 | Large Language Models: Transformers, pre-training, fine-tuning and alignment, inference, retrieval and agents, evaluation |
| O4 | Graph-structured data: GNNs and graph learning for networks, molecules, logistics |
| O5 | Graph x LLM: knowledge graphs with LLMs, GraphRAG, neuro-symbolic reasoning (the distinctive emphasis) |
| O6 | Multimodal generative AI: vision, language, speech, 3D / geometric data |
| O7 | Hands-on and industry practice: projects, case studies, industry domains, deployment, research readiness |
| O8 | Trustworthy and responsible AI: robustness, privacy, explainability, uncertainty, ethics |

Strength scale, judged on what the page actually delivers (not on what it announces):

- **0**: absent, or a passing word.
- **1**: bridge or mention: a note, pointer, single bullet or analogy; no definitions or derivations a student could use.
- **2**: taught: a section or chapter with definitions, derivations or a lab, but partial for the objective (sub-topics missing, labs unwritten, no exercise).
- **3**: core supplier: several chapters with derivations plus exercises, labs or a project on the page.

"Depth >= 2" in the path analysis means at least one course on that path scores 2 or 3 on the objective.

## 2. Coverage matrix (scores)

| Course (slug) | Status | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|---|
| **Pre-programme refreshers** | *level-1 support; not credit-bearing science options* | | | | | | | | |
| Refresher Statistics (`m1p1-refresher-statistics`) | pre-programme | 2 | 1 | 1 | 1 | 0 | 0 | 1 | 1 |
| Refresher CS (`m1p1-refresher-cs`) | pre-programme | 1 | 0 | 1 | 2 | 0 | 0 | 2 | 0 |
| Refresher Neural Nets (`m1p1-refresher-neural-nets`) | off-curriculum | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| **Mandatory science core (Y1 P1-P2, Y2 P1)** | *DL is 'required once': P1 (CSC_51054_EP) or P2 variant (APM_52183_EP)* | | | | | | | | |
| Machine Learning (`m1p1-machine-learning`) | mandatory Y1 P1 | 3 | 1 | 1 | 1 | 0 | 0 | 2 | 1 |
| Deep Learning (P1) (`m1p1-deep-learning`) | DL once (P1; gllm) | 3 | 2 | 2 | 1 | 1 | 1 | 2 | 0 |
| Deep Learning (P2 variant) (`m1p2-deep-learning-p2`) | DL once (P2; sys) | 3 | 2 | 2 | 1 | 0 | 0 | 2 | 2 |
| Reinforcement Learning (`m1p2-reinforcement-learning`) | mandatory Y1 P2 | 3 | 1 | 2 | 1 | 1 | 0 | 2 | 1 |
| Graph ML (`m1p2-graph-ml`) | mandatory Y1 P2 | 2 | 2 | 1 | 3 | 2 | 1 | 2 | 1 |
| Text Mining & NLP (`m1p2-nlp-text-mining`) | mandatory Y1 P2 | 2 | 1 | 2 | 1 | 1 | 0 | 3 | 1 |
| Large Language Models (`m2-large-language-models`) | mandatory Y2 P1 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 |
| Geometric Data (`m2-geometric-deep-learning`) | mandatory Y2 P1 | 1 | 1 | 0 | 2 | 0 | 2 | 2 | 1 |
| **Y1 P1 options (choose 3)** | *home route tags: gllm = DL, Emerging ML, TDA; sys = Signal, CV, Shapes* | | | | | | | | |
| Signal Processing (`m1p1-signal-processing`) | P1 option (sys) | 2 | 1 | 1 | 1 | 0 | 2 | 2 | 0 |
| Emerging ML / Collaborative (`m1p1-emerging-ml`) | P1 option (gllm) | 2 | 0 | 1 | 1 | 0 | 0 | 2 | 3 |
| Computer Animation (`m1p1-computer-animation`) | P1 option (no route) | 1 | 1 | 0 | 1 | 0 | 1 | 2 | 0 |
| Image Analysis & CV (`m1p1-computer-vision`) | P1 option (sys) | 2 | 0 | 0 | 1 | 0 | 2 | 2 | 0 |
| Topological Data Analysis (`m1p1-tda`) | P1 option (gllm) | 1 | 1 | 1 | 2 | 0 | 1 | 2 | 1 |
| Shapes (`m1p1-shapes`) | P1 option (sys) | 1 | 0 | 0 | 2 | 0 | 2 | 1 | 0 |
| **Y1 P2 options (choose 1)** | *DL P2 variant is listed in the core block; gllm preselects Multimodal GenAI, sys preselects DL P2* | | | | | | | | |
| Multimodal GenAI (`m1p2-multimodal-genai`) | P2 option (gllm) | 2 | 3 | 1 | 1 | 1 | 3 | 2 | 1 |
| Optimal Transport & Fairness (`m1p2-optimal-transport`) | P2 option (no route) | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 2 |
| Optimization for AI (`m1p2-optimization-ai`) | P2 option (no route) | 3 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
| Advanced Deep Learning (`m1p2-advanced-deep-learning`) | P2 option (no route) | 3 | 1 | 1 | 1 | 0 | 1 | 3 | 2 |
| Image Synthesis (`m1p2-image-synthesis`) | P2 option (no route) | 1 | 1 | 0 | 0 | 0 | 2 | 2 | 0 |
| **Y1 P2 slot TBC, sys-tagged (not in the 2026-27 lists; kept for reference)** | *no SynapseS code; the sys route's Choose-1 slot is used by DL P2* | | | | | | | | |
| CV: Fundamentals to Applications (`m1p2-computer-vision-applications`) | slot TBC (sys) | 2 | 0 | 0 | 1 | 0 | 1 | 3 | 2 |
| Real-time AI in Video Games (`m1p2-realtime-ai-videogames`) | slot TBC (sys) | 1 | 0 | 1 | 1 | 0 | 0 | 2 | 1 |
| **Y2 P1 slot TBC (announced)** | *gllm preselects Advanced GNN and Control in GenAI; no sys tag in Y2 P1* | | | | | | | | |
| Advanced GNN (`m2-advanced-gnn`) | Y2 P1 TBC (gllm) | 2 | 1 | 1 | 3 | 1 | 1 | 2 | 2 |
| Privacy & UQ (`m2-privacy-uncertainty`) | Y2 P1 TBC (no route) | 2 | 1 | 1 | 0 | 0 | 0 | 2 | 3 |
| Boosting to Foundation (tabular) (`m2-boosting-foundation-tabular`) | Y2 P1 TBC (no route) | 3 | 1 | 1 | 0 | 0 | 0 | 3 | 1 |
| Control in GenAI (`m2-control-generative-ai`) | Y2 P1 TBC (gllm) | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 |
| **Y2 P2 announced themes (official list unpublished)** | *gllm: MLOps, Security, Graph Gen, ESP-LLMs, Adv. Topics; sys: MLOps, Security, ESP-LLMs, Speech* | | | | | | | | |
| MLOps & LLM Engineering (`m2-mlops-llm-engineering`) | Y2 P2 (gllm sys) | 1 | 0 | 2 | 0 | 1 | 0 | 3 | 2 |
| Security & Robustness (`m2-security-robustness`) | Y2 P2 (gllm sys) | 2 | 0 | 1 | 1 | 0 | 0 | 2 | 3 |
| Graph Generative Models (`m2-graph-generative-models`) | Y2 P2 (gllm) | 1 | 3 | 1 | 2 | 2 | 2 | 2 | 1 |
| Explainability, Security, Privacy of LLMs (`m2-explainability-security-privacy-llms`) | Y2 P2 (gllm sys) | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 3 |
| Speech Technology (`m2-speech-technology`) | Y2 P2 (sys) | 2 | 2 | 1 | 0 | 0 | 3 | 2 | 2 |
| Advanced Topics in LLMs (`m2-advanced-topics-llms`) | Y2 P2 (gllm) | 1 | 1 | 3 | 1 | 2 | 0 | 2 | 1 |
| **Notes kept for reference (not in the 2026-27 LLGA lists)** | *not selectable in 2026-27; scored for completeness* | | | | | | | | |
| Probability & Monte Carlo (`m1p1-probability-monte-carlo`) | reference | 2 | 2 | 0 | 0 | 0 | 0 | 1 | 1 |
| DBMS (`m1p1-dbms`) | reference | 1 | 0 | 1 | 1 | 1 | 0 | 2 | 1 |
| Statistical Learning Theory (`m1p1-statistical-learning-theory`) | reference | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| Optimisation & Responsible AI (`m1p2-responsible-ai-sustainability`) | reference | 2 | 0 | 1 | 0 | 0 | 0 | 2 | 2 |
| Statistics in Action (`m1p2-statistics-in-action`) | reference | 2 | 0 | 0 | 1 | 0 | 0 | 2 | 1 |
| Social Media: Probabilistic Models (`m1p2-social-media-probabilistic`) | reference | 1 | 2 | 0 | 2 | 0 | 0 | 1 | 1 |

Highest score per objective across all science pages:

| Objective | Max | Courses at 3 | Courses at 2 |
|---|---|---|---|
| O1 ML & DL foundations | 3 | Machine Learning, Deep Learning (P1), Deep Learning (P2 variant), Reinforcement Learning, Optimization for AI, Advanced Deep Learning, Boosting to Foundation (tabular), Statistical Learning Theory | Refresher Statistics, Refresher Neural Nets, Graph ML, Text Mining & NLP, Large Language Models, Signal Processing, Emerging ML / Collaborative, Image Analysis & CV, Multimodal GenAI, Optimal Transport & Fairness, CV: Fundamentals to Applications, Advanced GNN, Privacy & UQ, Security & Robustness, Speech Technology, Probability & Monte Carlo, Optimisation & Responsible AI, Statistics in Action |
| O2 Generative modelling theory | 3 | Multimodal GenAI, Graph Generative Models | Deep Learning (P1), Deep Learning (P2 variant), Graph ML, Large Language Models, Control in GenAI, Speech Technology, Probability & Monte Carlo, Social Media: Probabilistic Models |
| O3 Large Language Models | 3 | Large Language Models, Advanced Topics in LLMs | Deep Learning (P1), Deep Learning (P2 variant), Reinforcement Learning, Text Mining & NLP, Control in GenAI, MLOps & LLM Engineering, Explainability, Security, Privacy of LLMs |
| O4 Graph-structured data | 3 | Graph ML, Advanced GNN | Refresher CS, Geometric Data, Topological Data Analysis, Shapes, Optimal Transport & Fairness, Graph Generative Models, Social Media: Probabilistic Models |
| O5 Graph x LLM | 2 | none | Graph ML, Graph Generative Models, Advanced Topics in LLMs |
| O6 Multimodal generative AI | 3 | Multimodal GenAI, Speech Technology | Geometric Data, Signal Processing, Image Analysis & CV, Shapes, Image Synthesis, Control in GenAI, Graph Generative Models |
| O7 Hands-on, industry, research readiness | 3 | Text Mining & NLP, Advanced Deep Learning, CV: Fundamentals to Applications, Boosting to Foundation (tabular), MLOps & LLM Engineering | Refresher CS, Machine Learning, Deep Learning (P1), Deep Learning (P2 variant), Reinforcement Learning, Graph ML, Large Language Models, Geometric Data, Signal Processing, Emerging ML / Collaborative, Computer Animation, Image Analysis & CV, Topological Data Analysis, Multimodal GenAI, Optimal Transport & Fairness, Image Synthesis, Real-time AI in Video Games, Advanced GNN, Privacy & UQ, Security & Robustness, Graph Generative Models, Explainability, Security, Privacy of LLMs, Speech Technology, Advanced Topics in LLMs, DBMS, Optimisation & Responsible AI, Statistics in Action |
| O8 Trustworthy & responsible AI | 3 | Emerging ML / Collaborative, Privacy & UQ, Security & Robustness, Explainability, Security, Privacy of LLMs | Deep Learning (P2 variant), Large Language Models, Optimal Transport & Fairness, Advanced Deep Learning, CV: Fundamentals to Applications, Advanced GNN, Control in GenAI, MLOps & LLM Engineering, Speech Technology, Optimisation & Responsible AI |

O5 is the only objective that no page reaches at depth 3. It is also the distinctive emphasis of the master.

## 3. Justification of every cell

Each cell is `score: reason`. Reasons come from the records' `topics_taught`, `thin_areas` and `objective_contribution`, checked against the pages where noted.

### Pre-programme refreshers

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| Refresher Statistics | 2: likelihood to loss, ERM, bias-variance, OLS/Gauss-Markov (level 1) | 1: inverse-CDF sampling, change of variables, ELBO bridge | 1: chain rule as autoregression, next-token likelihood | 1: node dependence; unobserved edge is not a negative edge | 0: none | 0: none | 1: coverage simulations, A/B comparisons; no project | 1: Simpson's paradox, multiple testing, missing-data bias |
| Refresher CS | 1: NumPy linear algebra, SVD-PCA, cost models | 0: none | 1: vocab hashing, tries for prefix-constrained decoding, top-k heaps | 2: CSR/COO edge_index, BFS/Dijkstra/MST, GNN-style aggregation exit example (mostly self-study) | 0: none | 0: none | 2: pytest, profiling, typing, git, Docker toolkit | 0: reproducibility notes only |
| Refresher Neural Nets | 2: hand backprop, MSE vs CE, init, SGD/momentum/Adam in NumPy | 0: none | 1: single-head attention as a TxT matrix | 0: computation graph vs data graph remark only | 0: none | 0: none | 1: reruns an external MNIST notebook | 0: none |

### Mandatory science core (Y1 P1-P2, Y2 P1)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| Machine Learning | 3: ERM, bias-variance, linear/kernel/SVM, trees/boosting, EM/PCA, VC/Rademacher with proofs | 1: GMM/EM via ELBO-KL, PPCA, naive Bayes as generative classifier (groundwork only) | 1: softmax cross-entropy; TF-IDF text baseline (20 Newsgroups) | 1: graph kernels, spectral clustering, SBM via EM as forward pointers | 0: none | 0: none | 2: leak-free sklearn pipelines, nested CV, calibration; running project Ex. 12 | 1: calibration, leakage, permutation importance; no fairness/privacy/robustness |
| Deep Learning (P1) | 3: backprop theorem, Xavier/He, SGD/momentum/Adam proofs, norms, CNN/RNN | 2: VAE ELBO + reparameterization, GAN optimal discriminator/JSD derived; diffusion only in a table, no implementation | 2: scaled dot-product/multi-head attention, pre-norm, RoPE, BPE, CLM/MLM, perplexity, LoRA sketch | 1: transformer read as message passing; GNN notions only in ch10 notes | 1: Graph-of-Words (ch10, self-study) | 1: CNN image encoder, generative-families table, cross-modal research pointers | 2: ch8 training protocol, MNIST MLP/CNN/ViT project Ex. 12; 3 session labs unwritten | 0: reproducibility/determinism only |
| Deep Learning (P2 variant) | 3: autodiff, He init, LR stability, CNN equivariance proof, BPTT, mixed precision, ZeRO; attention/normalisation only recapped | 2: VAE ELBO gap, GAN/JS value, DDPM forward + eps-loss; no reverse process or sampler | 2: 6ND, Chinchilla sizing, KV cache, prefill/decode, decoding, speculative decoding, 7B budget; self-attention never defined | 1: DeepSets permutation-equivariant layers, gossip spectral gap | 0: none | 0: pointer to Multimodal GenAI only | 2: ResNet-18 pipeline, parallelism decisions, roofline, Ex. 7 budget capstone, Ex. 8 measurement; labs lack code | 2: Lipschitz certified radius (proved), FGSM/PGD training, distribution shift, energy/emissions |
| Reinforcement Learning | 3: MDPs, Bellman contraction, DP, TD/Q-learning convergence, policy gradients, deep RL with proofs | 1: max-entropy RL / control as inference; decision transformer as conditional generation | 2: PPO-clip/GAE prepare RLHF/GRPO; ch7 LLM agents (ReAct, tools, memory), deep-research agent lab | 1: random walks; multi-agent systems as graphs | 1: GraphRAG cross-reference; agent DAG as a graph | 0: none | 2: Gymnasium labs, agent lab + Ex. 16, LinUCB news recommendation; two labs and the 50% project unspecified | 1: constrained MDPs, offline-RL shift, agent-safety bullets |
| Graph ML | 2: spectral clustering, GCN from Chebyshev filters, skip-gram gradients, over-smoothing theorem | 2: graphons, ER/SBM likelihood, GraphVAE, GraphRNN, DiGress (no loss), MMD/FCD | 1: LLM extraction and pseudo-code prompting (ch10) | 3: kernels, node2vec, spectral, MPNN/GCN/SAGE/GAT/R-GCN, scale, heterophily, temporal, EGNN, link prediction | 2: ch10 GraphRAG pipeline, pseudo-code prompting, GNN+LLM hybrids, KGC; prose only, no code/formulas, final lab underspecified | 1: molecules/3D geometric graphs; text-to-graph conditioning mentioned | 2: fraud, PinSage, KGC, OGB, leakage-free protocol, PyG code; team project undefined | 1: evaluation hygiene; GraphRAG hallucination/re-identification note |
| Text Mining & NLP | 2: NB as Dirichlet posterior, sparse logistic, LDA Gibbs, SVD, HMM/CRF, SGNS gradients | 1: LDA generative story, Unigram LM, perplexity, GPT/T5 objectives | 2: BPE/WordPiece/Unigram, embeddings, BERT/GPT/T5 objectives, fine-tuning protocol, BM25 as RAG baseline; architecture deferred to DL P1 ch6 | 1: TextRank, word2vec vs DeepWalk, graph-of-words (ch9) | 1: NER to KG export for mini-GraphRAG; relation extraction named but never taught | 0: text only | 3: ticket-routing case, recommenders (MF), ads CTR, social monitoring, capstone pipeline Ex. 14; deployment only bullets | 1: WEAT bias test and debiasing, calibration |
| Large Language Models | 2: pre-LN, RoPE proof, GQA, MoE, FlashAttention, scaling-law derivations | 2: LM objectives, Chinchilla optimum, DPO closed form, speculative-decoding exactness | 3: tokenizer to pre-training to SFT/RLHF/DPO/GRPO to inference/serving to RAG to agents to evaluation; gaps: LoRA/PEFT, distributed training | 1: attention as message passing; graph linearization pointer | 1: 7.4 GraphRAG is one bullet deferring to Graph ML ch10; final lab vector RAG vs GraphRAG | 1: 8.2 ViT + projector, audio, video, documents: four descriptive bullets | 2: nanoGPT, SFT, toy GRPO, RAG/agent labs, serving cost arithmetic; no rubric | 2: ch9 contamination, judge bias, hallucination, jailbreak/injection, watermark z-test; no privacy/fairness |
| Geometric Data | 1: PointNet universality sketch, invariance/equivariance theory; no training material | 1: pointers to diffusion over shapes/conformers | 0: speculative 'shape-GPT' note only | 2: meshes as geometric graphs: cotangent Laplacian, spectra, DGCNN, EGNN equivariance proof | 0: none | 2: 3D shapes/point clouds as a modality: descriptors, functional maps, DiffusionNet; analysis only | 2: libigl/PyTorch labs, FAUST/SHREC/ModelNet, Ex. 11-12 (no setup) | 1: descriptor robustness to remeshing (HKS stability) |

### Y1 P1 options (choose 3)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| Signal Processing | 2: Fourier/convolution view of CNNs, sparse coding, LISTA | 1: FID/FAD as Gaussian W2 | 1: sinusoidal PE as Fourier basis (pointer) | 1: graph Fourier / spectral GCN pointer (two lines) | 0: none | 2: audio front-end: STFT, Mel, MFCC, masks (analysis, no generation) | 2: NumPy/SciPy labs, industrial cases, denoising project Ex. 12 | 0: none |
| Emerging ML / Collaborative | 2: SGD convergence proof, lower bounds, SVRG/SAGA, distributed and federated SGD | 0: none | 1: Chinchilla allocation, MoE, federated LoRA (self-study notes) | 1: gossip on communication graphs (lambda_2) | 0: none | 0: none | 2: graded group research project, paper-reading sessions; labs without code | 3: Byzantine-robust aggregation, poisoning/backdoors, DP and DP-SGD, MIA, secure aggregation |
| Computer Animation | 1: integrator stability, skinning fits as regression | 1: PFNN / autoregressive motion only named | 0: none | 1: mass-spring networks, kinematic trees (implicit graphs) | 0: none | 1: motion and 3D deformation as modalities; no generative motion model | 2: mini-garment project Ex. 10, production pipeline; no C++/OpenGL lab material | 0: none |
| Image Analysis & CV | 2: filtering to CNNs, detection/segmentation families, SVD/PCA | 0: none | 0: none | 1: graph cuts, normalized cuts, kNN point-cloud graphs | 0: none | 2: image formation, stereo, ICP, NeRF/3DGS pointers; no generation | 2: OpenCV labs, IGN LiDAR case; project kick-off without subject | 0: none |
| Topological Data Analysis | 1: single linkage/MST as 0-dim persistence, kernels on diagrams | 1: topological-regularizer note | 1: embeddings-as-point-clouds asserted, never shown | 2: graph homology, clique complexes, PersLay/extended persistence for graph classification | 0: none | 1: image/3D practice not implemented | 2: GUDHI/ripser labs (synthetic only), paper presentation | 1: stability theorems as provable feature robustness; Mapper |
| Shapes | 1: PCA normals, least squares, eigen-decomposition | 0: none | 0: none | 2: mesh as graph: cotangent Laplacian, spectrum, Fiedler cut | 0: none | 2: 3D modality: point clouds, meshes, SDFs, reconstruction | 1: labs are one-liners; no project | 0: none |

### Y1 P2 options (choose 1)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| Multimodal GenAI | 2: Gaussians, KL, reparameterization, cross-attention | 3: ELBO, GAN/WGAN, DDPM ELBO, noise = score, CFG, DDIM derived | 1: VQ/codec tokens, MLLM connectors (sketch) | 1: DiGress / graph-text analogy notes | 1: graph x generation analogy only | 3: CLIP, text-to-image pipeline, video, audio, VLA, multimodal LLMs | 2: LoRA fine-tuning project Ex. 14, MiniVAE and DDPM/DDIM labs | 1: deepfakes, C2PA, copyright, AI Act (bullet list) |
| Optimal Transport & Fairness | 2: LP/convex duality, W vs KL, sample complexity | 1: WGAN critic via KR duality, FID as Bures; no flow matching | 1: WMD, GW word-embedding alignment | 2: GW/FGW/COOT graph comparison and alignment | 1: KG alignment for GraphRAG (mention) | 1: COOT/GW align heterogeneous spaces; FID/FAD | 2: POT labs, OTDA, Adult fairness lab, synthesis lab, group project | 2: barycentric fairness repair with DP proof, EO post-processing (lab code broken) |
| Optimization for AI | 3: GD/Nesterov/prox/SGD/SVRG/Newton/Adam with proofs | 1: GDA divergence explains GAN instability | 1: AdamW, warmup/cosine, LARS/LAMB; no LLM case | 0: none | 0: none | 0: none | 1: NumPy labs, HPO practice; no project | 1: constrained learning for fairness (formulation) |
| Advanced Deep Learning | 3: ViT/Swin/ConvNeXt/MoE, SimCLR/MAE, training at scale | 1: amortized inference, gradient estimators; CFG/DDIM stated without DDPM | 1: MoE balancing, scaling laws, muP, distillation (vision side) | 1: permutation equivariance of attention | 0: none | 1: neural fields/NeRF, CLIP pointer | 3: replication project with deliverables, reading seminar, efficiency grid | 2: PGD/adversarial training, Lipschitz certificate, reproducibility |
| Image Synthesis | 1: Monte Carlo estimation, learned denoisers | 1: physical image formation, not probabilistic models | 0: none | 0: none | 0: none | 2: NeRF, 3D Gaussians, differentiable rendering (thin ch10) | 2: NumPy path tracer, GLSL shaders, paper-implementation project | 0: none |

### Y1 P2 slot TBC, sys-tagged (not in the 2026-27 lists; kept for reference)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| CV: Fundamentals to Applications | 2: detection losses, focal loss, segmentation, set prediction | 0: none | 0: no VLM content | 1: bipartite matching, PointNet set function | 0: none | 1: camera/LiDAR/BEV perception front-end; no VLM or generation | 3: industrial cases, ONNX/INT8/edge deployment, YOLO datasheet project | 2: ch9 adversarial examples, dataset bias, AI Act/biometrics (thin) |
| Real-time AI in Video Games | 1: classical decision AI; RL only recapped | 0: none | 1: LLM-driven NPC survey, no implementation | 1: graph search (A*, navmesh, HPA*), no GNN | 0: none | 0: none | 2: budgets, profiling, studio cases, Ex. 12 project; ch7-9 without exercises | 1: anti-cheat, moderation, children's data |

### Y2 P1 slot TBC (announced)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| Advanced GNN | 2: injectivity arguments, deep-GNN residuals, CI/paired-test hygiene | 1: NGG/EDM pointers | 1: transformer-GNN thread; GNN x LLM in prose | 3: WL expressivity (GIN proof), over-squashing, PEs, graph transformers, temporal, scale | 1: 8.3 soft tokens / graph-RAG / LLM-annotated TAGs: prose, no formulation, no exercise | 1: text-attributed graphs, 3D molecular geometry | 2: OGB labs, real-time fraud pipeline (TGN), reproduction project Ex. 11 | 2: Nettack/Metattack, smoothing sketch, edge/node DP, degree-bias fairness |
| Privacy & UQ | 2: calibration, Bayesian DL, conformal and quantile regression | 1: generative conformal / semantic entropy sketched | 1: LLM UQ (verbalized confidence, semantic entropy) descriptive | 0: graph DP/UQ only promised | 0: none | 0: none | 2: Opacus DP-SGD, industry deployments, Ex. 11 project with rubric | 3: DP mechanisms, composition, RDP, DP-SGD, calibration, conformal coverage proofs |
| Boosting to Foundation (tabular) | 3: functional GD, XGBoost leaf weights/gain, GOSS proofs, deep tabular, benchmarking | 1: PFN prior; CTGAN/TabDDPM named without maths | 1: table serialization, TabLLM, text-to-SQL (one definition) | 0: no relational/graph bridge | 0: none | 0: none | 3: symmetric OpenML benchmark, leakage lab, decision guide (CRM/fraud) | 1: target leakage, honest benchmarking, synthetic is not anonymous |
| Control in GenAI | 1: exponential-tilting entropy derivative, Gibbs inequality | 2: KL-regularized closed form, CFG as tilting proof, support-constraint entropy bound | 2: DFA-constrained decoding, steering vectors, RLHF/DPO as control, watermark z-test | 1: control of graph generators (synthesis of another module) | 1: automaton constraints as symbolic control of LLM output | 2: CFG, ControlNet, DDIM/null-text inversion | 1: toy labs (HF LogitsProcessor, GPT-2 steering); no project | 2: provenance watermarking, AI Act art. 50, reward hacking, attacks on control |

### Y2 P2 announced themes (official list unpublished)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| MLOps & LLM Engineering | 1: Hoeffding CI gates, PSI/Jeffreys, Little's law | 0: none | 2: continuous batching, PagedAttention, cost per M tokens, RAG Ops, LoRA ops, agent tracing | 0: no graph-specific ops | 1: GraphRAG operational cost vs vector RAG | 0: none | 3: 12 instrumentation labs (DVC, MLflow, vLLM, RAGAS, OTel, CodeCarbon), enterprise-assistant thread, post-mortem | 2: secrets/sandbox/supply chain, guardrails, drift monitoring, green ops |
| Security & Robustness | 2: robust min-max, dual-norm proofs, robust sample complexity | 0: none | 1: GCG / prompt injection overview (one paragraph) | 1: Nettack case study, no lab | 0: none | 0: none | 2: nine PyTorch labs, RobustBench reports, threat-analysis mini-project | 3: threat models, PGD-AT/TRADES, randomized smoothing, backdoors, poisoning, extraction, MIA |
| Graph Generative Models | 1: change of variables and ELBO as tools | 3: exchangeability/graphons, autoregressive, VAE, flows, D3PM posterior derived | 1: SMILES/SELFIES LMs, LLM-written generators | 2: GNN encoders/denoisers throughout; generative graph theory | 2: text-to-graph routes (MolT5, LLM-written NetworkX, LLM+GNN loops), Ex. 8 mini-project | 2: text-to-molecule, property-conditioned and crystal generation | 2: drug-discovery pipeline, MOSES/GuacaMol, MMD lab; GraphRNN/VAE labs missing | 1: synthetic networks for privacy, metric gaming |
| Explainability, Security, Privacy of LLMs | 1: Shapley uniqueness, IG completeness, DP post-processing | 1: generation watermarking | 2: probes, logit/tuned lens, SAEs, LLM attack matrix | 0: no graph content | 0: no GraphRAG injection, no GNN explainability | 0: image/OCR injection only listed | 2: RAG injection and hardening lab, red-team protocol to CI tests, Opacus DP fine-tuning | 3: interpretability, jailbreak/injection, memorization/MIA/DP, red teaming, AI Act |
| Speech Technology | 2: HMM/Viterbi to CTC derived, Conformer, RNN-T | 2: WaveNet, HiFi-GAN, VITS (VAE+flow+GAN); diffusion/flow TTS objectives not written | 1: speech LLMs, audio tokens, three audio-LLM connections (descriptive) | 0: none | 0: none | 3: full audio modality: ASR, TTS, vocoders, codecs, full-duplex dialogue | 2: Whisper/TTS labs, RTF and latency budgets; no graded project | 2: voice-cloning consent, AI Act art. 50, audio watermark ROC |
| Advanced Topics in LLMs | 1: MoE/SSM architectures (assumes foundations) | 1: self-consistency marginalization, speculative decoding exactness | 3: reasoning/RLVR, long context, memory, MoE, SSMs, efficiency, agents, evaluation | 1: G-Retriever GNN encoder; no GNN depth | 2: ch8 NLGraph, Talk like a Graph, G-Retriever; ch4 GraphRAG; Ex. 12 reproduction | 0: multimodal LLMs absent | 2: reproduction labs, paper seminar, position paper Ex. 13 | 1: contamination, judge bias, agent injection, model collapse |

### Notes kept for reference (not in the 2026-27 LLGA lists)

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| Probability & Monte Carlo | 2: measure-theoretic expectation, LLN/CLT, conditional expectation as L2 projection | 2: MCMC, Langevin, score = grad log pi, annealed Langevin | 0: none | 0: none | 0: none | 0: none | 1: NumPy sampler labs, no project | 1: MC error bars, ESS, R-hat |
| DBMS | 1: data layer of ML pipelines | 0: none | 1: vector stores and ANN (IVF, HNSW, PQ); RAG not taught | 1: property graphs, RDF, Cypher/SPARQL (no learning) | 1: KG + vector-store infrastructure for GraphRAG (promised, not taught) | 0: none | 2: SQL, transactions, EXPLAIN, SQLite labs | 1: provenance, entity resolution, fact-checking |
| Statistical Learning Theory | 3: ERM, concentration, VC, Rademacher, margins, minimax, Lasso oracle inequalities | 1: KL/TV/Pinsker, PAC-Bayes note | 0: none | 0: none | 0: none | 0: none | 1: short snippets; scheduled labs unsupplied | 1: concentration tools for audits only |
| Optimisation & Responsible AI | 2: LP/ILP, duality, multi-objective, compression with proofs | 0: none | 1: memory-bound decoding economics, int8/int4 | 0: none | 0: none | 0: none | 2: data-center/EV cases, CodeCarbon, public-claim audit | 2: carbon accounting, rebound, greenwashing (environmental side only) |
| Statistics in Action | 2: power, multiple testing, bootstrap, regression diagnostics | 0: none | 0: none | 1: graphex bootstrap research notes | 0: none | 0: none | 2: A/B testing (CUPED, sequential), case studies, three-star project | 1: selection bias, Simpson, causal inference, honest reporting |
| Social Media: Probabilistic Models | 1: MLE, spectral methods, EM on graphs | 2: ER/configuration/BA/SBM as generative graph models with thresholds | 0: none | 2: random graphs, epidemics, SBM, community detection (no learning) | 0: none | 0: none | 1: networkx labs on synthetic graphs | 1: de-anonymization, disinformation spread |

## 4. Mandatory non-science elements (supplement)

These pages are framing notes (about 74 lines each, tagged "Extrapolating"). Two scores are given: what the **page** delivers, and what the **programme element** is designed to deliver. The path analysis counts the programme element only as "by design", never as delivered content.

| Element (slug) | ECTS | Page delivers | Programme element by design | What is missing on the page |
|---|---|---|---|---|
| Transverse project (`m2-projet-transverse`) | 8 | O7 1 (project-mode framing); O3/O4/O5 0 (conditional on topic) | O7 3; O3-O5 only if the topic is Graph x LLM | no subject bank, no domain from the official list (healthcare, finance, recommendation, logistics), no milestones or rubric; the "skill checkpoints" link points to `index.html#checkpoints`, which now lists post-master roles |
| Research internship (`m1p3-research-internship`) | 20 | O7 1 | O7 3 (first full research cycle) | no 16-week milestone plan, proposal/report/poster template, reproducibility checklist or example topics |
| Final internship (`m2-internship`) | 24 | O7 1, O8 1 (asks for a risks/ethics/data section) | O7 3 | no module map for "link the topic to 2-3 modules", no report structure or rubric |
| Ethics seminar (`m2-ethical-issues-ai`) | 6 | O8 1 (facts / values / options grid, one bullet) | O8 2-3 | no case list, readings, AI Act / GDPR / model cards, fairness definitions, deliverable |
| Strategy/Marketing, Startup, Humanities, Languages, Sports | - | O7 at most 1 (framing); Humanities O8 1 | - | not objective-bearing; listed for completeness |

## 5. Path analysis

### (a) Mandatory path alone

ML + one DL (P1 `m1p1-deep-learning` or P2 `m1p2-deep-learning-p2`) + RL + Graph ML + NLP + LLMs + Geometric Data, plus transverse project, internships and the ethics seminar.

| Obj | Max with DL P1 | Max with DL P2 | Courses at >= 2 | Reached at >= 2? |
|---|---|---|---|---|
| O1 | 3 | 3 | ML 3, DL (either) 3, RL 3; Graph ML, NLP, LLM 2 | **Yes** |
| O2 | 2 | 2 | DL P1 ch9 (VAE/GAN) or DL P2 7.3 (VAE/GAN/DDPM objective) 2; Graph ML ch9 2; LLM 2 | **Yes, but partial**: no course at 3; with DL P1, diffusion/score and flows are never derived, yet Graph ML 9.5 (DiGress) assumes diffusion. With DL P2, the DDPM loss is given without reverse process or sampler. Normalizing flows: absent on both variants. -> finding OBJ-O2 |
| O3 | 3 | 3 | LLM 3; DL (either) 2, NLP 2, RL 2 | **Yes**, with chain holes: LoRA/PEFT is never taught in LLM (the page points to a "ch. 6: distillation, LoRA" that does not exist); DL P2 never defines self-attention while NLP ch7 says its architecture is "carried over from the Deep Learning module ch. 6" (P1). -> finding OBJ-O3 |
| O4 | 3 | 3 | Graph ML 3; Geometric Data 2 | **Yes** |
| O5 | 2 | 2 | Graph ML ch10 only (2); NLP, LLM, RL, DL P1 at 1 | **Barely**: the only depth-2 source is one 3-hour chapter of prose (Thm 10.1 pipeline, 10.2 bullets, a final lab with no corpus, model or baseline). Relation extraction, which the chain NLP ch6 -> Graph ML ch10 -> LLM 7.4 needs, is never taught. LLM 7.4 is one bullet. -> finding OBJ-O5 (high) |
| O6 | 2 | 2 | Geometric Data 2 (3D analysis only) | **Only nominally**: the generative and cross-modal part is at 1 (LLM 8.2, four descriptive bullets). No CLIP/contrastive alignment, no VLM training objective, no text-to-image/audio on the mandatory path. -> finding OBJ-O6 (high) |
| O7 | 3 | 3 | NLP 3; ML, DL, RL, Graph ML, LLM, Geometric 2 | **Yes through courses**; the programme's dedicated vehicles (transverse project, internships: 52 ECTS) have framing pages only; deployment is limited to LLM 6.5 serving; logistics never appears. -> finding OBJ-O7 |
| O8 | 2 | 2 | LLM ch9 2; DL P2 7.1 2 (P2 variant only) | **Narrowly**: only LLM security/evaluation reaches 2. Privacy (DP, MIA, memorization), fairness metrics and explainability are at most 1 on the mandatory path; the mandatory 6-ECTS ethics seminar page has no content. -> finding OBJ-O8 (high) |

### (b) Graph x LLM route (`data-p="gllm"`)

Mandatory + DL P1, Emerging ML, TDA (P1) + Multimodal GenAI (P2) + Advanced GNN, Control in GenAI (Y2 P1) + MLOps, Security & Robustness, Graph Generative Models, ESP-LLMs, Advanced Topics in LLMs (Y2 P2).

| Obj | Max | Reached by | Verdict |
|---|---|---|---|
| O1 | 3 | ML, DL P1, RL | reached |
| O2 | 3 | Multimodal GenAI, Graph Generative Models | reached |
| O3 | 3 | LLM, Advanced Topics in LLMs (Control 2, ESP 2, MLOps 2) | reached |
| O4 | 3 | Graph ML, Advanced GNN (Graph Gen 2, TDA 2) | reached |
| O5 | **2** | Graph ML ch10, Advanced Topics ch8, Graph Generative Models ch7 | **never 3** on the route that exists for it; Advanced GNN 8.3 (GNN x LLM injection) is prose with no formulation or exercise -> ROUTE-GLLM-O5 |
| O6 | 3 | Multimodal GenAI (Control 2, Graph Gen 2) | reached; speech absent from this route |
| O7 | 3 | NLP, MLOps | reached |
| O8 | 3 | Emerging ML, Security & Robustness, ESP-LLMs | reached (if the student takes one of these in the unpublished Y2 P2 list) |

### (c) AI systems route (`data-p="sys"`)

Mandatory with DL P2 + Signal Processing, Image Analysis & CV, Shapes (P1) + DL P2 in the P2 Choose-1 + MLOps, Security & Robustness, ESP-LLMs, Speech (Y2 P2). CV Applications and Real-time AI are tagged `sys` but have no SynapseS code and are not in the 2026-27 lists, and the route's only P2 Choose-1 slot is taken by DL P2; no Y2 P1 course carries a `sys` tag.

| Obj | Max | Reached by | Verdict |
|---|---|---|---|
| O1 | 3 | ML, DL P2, RL | reached |
| O2 | **2** | DL P2 7.3, Speech, Graph ML ch9, LLM | **never 3**: no diffusion sampler, no flows; Speech ch7 uses diffusion/flow-matching TTS whose objectives live in Multimodal GenAI (not on the route) -> ROUTE-SYS |
| O3 | 3 | LLM (MLOps 2, ESP 2) | reached; LoRA first taught in MLOps ch7 (Y2 P2), after LLM Ex. 3 asks to fine-tune a 1-3B model |
| O4 | 3 | Graph ML (Shapes 2, Geometric 2) | reached |
| O5 | **2** | Graph ML ch10 only | the route adds nothing above 1 (MLOps 1) |
| O6 | 3 | Speech (Signal 2, CV 2, Shapes 2, Geometric 2) | reached for audio; vision/3D only as analysis |
| O7 | 3 | NLP, MLOps (CV Applications 3 is not selectable) | reached |
| O8 | 3 | Security & Robustness, ESP-LLMs (DL P2 2) | reached |

### Summary: objective x path

| Obj | Mandatory | Graph x LLM | AI systems |
|---|---|---|---|
| O1 | 3 ML/DL/RL | 3 | 3 |
| O2 | 2 (partial) DL ch9 / DL P2 7.3 | 3 Multimodal GenAI, Graph Gen | 2 DL P2, Speech |
| O3 | 3 LLM | 3 LLM, Adv. Topics | 3 LLM |
| O4 | 3 Graph ML | 3 Graph ML, Adv. GNN | 3 Graph ML |
| O5 | 2 (weak) Graph ML ch10 | 2 Graph ML ch10, Adv. Topics ch8, Graph Gen ch7 | 2 (weak) Graph ML ch10 |
| O6 | 2 nominal / 1 generative (Geometric Data; LLM 8.2) | 3 Multimodal GenAI | 3 Speech |
| O7 | 3 NLP (project/internship pages 1) | 3 NLP, MLOps | 3 NLP, MLOps |
| O8 | 2 narrow (LLM ch9) | 3 Emerging ML, Security, ESP | 3 Security, ESP |

## 6. Findings: objectives weakly served on the mandatory path

Fixes are bounded: each adds a section, a worked case or a signposted self-study chapter to an existing chapter of a mandatory course, or fills a framing page; no new course is proposed. Where a session is already full (LLM session 8, DL P1 session 12), the addition is marked self-study with a time estimate.

### OBJ-O5 (high): Graph x LLM rests on one prose chapter
- **Evidence.** `m1p2-graph-ml` ch10 (session 12) is Thm 10.1 (pipeline in prose), 10.2 (serialization, pseudo-code prompting, hybrids as bullets), note 10.3 and a "Final lab" with no corpus, LLM, baseline or metric definitions; the record's thin_areas: "GraphRAG is prose only. There is no code, no retrieval or scoring formula, and no definition of the evaluation metrics". `m1p2-nlp-text-mining` Def. 6.1 calls NER "the gateway to building knowledge graphs (entity + relation extraction)" and the capstone exports "NER + relations", but relation extraction is never taught. `m2-large-language-models` 7.4 is one bullet ("detailed in the Graph ML module ch. 10"); its final lab compares vector RAG with a GraphRAG version that is not specified.
- **Fix.** (1) Graph ML ch10: add "10.4 GraphRAG, worked": triplet-extraction prompt with a JSON schema, an entity-resolution rule (string + embedding threshold), Leiden on a 30-entity toy graph, the local-search scoring rule (seed entities by embedding similarity, k-hop expansion, chunk ranking), the global map-reduce, and an evaluation protocol (multi-hop QA set, exact match and citation faithfulness, tokens and latency); about 60 lines of runnable Python (networkx, leidenalg, sentence-transformers, a small open LLM); the final lab names a corpus (e.g. 200 Wikipedia articles or a HotpotQA subset) and baselines (BM25, dense RAG). One exercise with solution on retrieval scoring. Fits session 12. (2) NLP ch6: add "6.4 Relation extraction" (pipeline vs joint, entity-marker classifier on an encoder, distant supervision, few-shot LLM triplet extraction, triplet micro-F1) with one exercise; fits session 8. (3) LLM 7.4: replace the bullet with half a page on KG retrieval (k-hop or PCST subgraph selection, linearization, cost comparison) and specify the final lab (corpus, metrics, deliverable).
- **Targets.** m1p2-graph-ml, m1p2-nlp-text-mining, m2-large-language-models.

### OBJ-O6 (high): multimodal generative AI is effectively depth 1 on the mandatory path
- **Evidence.** LLM 8.2 is four descriptive bullets (ViT patches + projector, audio, video, documents); its official_syllabus_gaps: "projector training and the VLM instruction-tuning objective are not taught". Geometric Data: "no generative model is taught", the 3D-token link to LLMs "is speculative". DL P2: "not served". Only Multimodal GenAI (a Choose-1 elective) and Speech (an unpublished Y2 P2 theme) reach 3, and a student who takes DL P2 in the P2 slot cannot take Multimodal GenAI.
- **Fix.** (1) LLM ch8: add a signposted self-study section "8.2b Vision-language models, worked" (about 2 h): CLIP symmetric InfoNCE (formula), the two LLaVA stages (projector alignment on caption pairs, then visual instruction tuning with loss masking), the token-budget arithmetic per image, and one exercise (projector parameter count plus a 30-line open_clip zero-shot classification). (2) Geometric Data ch8: replace the bullet list with one worked case "3D + language": contrastive text-shape retrieval with a point-cloud encoder and a frozen text encoder (loss, metric, dataset). (3) DL P1 ch9: one paragraph tying the VAE decoder to latent diffusion and CLIP conditioning, pointing to the self-study section of OBJ-O2.
- **Targets.** m2-large-language-models, m2-geometric-deep-learning, m1p1-deep-learning.

### OBJ-O8 (high): trustworthy AI is narrow on the mandatory path
- **Evidence.** LLM record: "fairness and privacy are absent" (ch9 covers contamination, judges, hallucination, jailbreaks, watermarking). ML: "no fairness, privacy or robustness"; only permutation importance (thin_areas: "no interpretability tools beyond the permutation-importance remark"). DL P1: "minimal, only reproducibility". NLP: WEAT only. Graph ML: "evaluation hygiene and a short note". Ethics seminar page: no cases, readings, regulation, fairness definitions or deliverable. DP and MIA appear only in electives (Emerging ML, Privacy & UQ, ESP-LLMs, Security).
- **Fix.** (1) ML ch4: add "4.8 Group fairness in the evaluation pipeline" (demographic parity, equalized odds, calibration within groups, the impossibility statement, per-group metrics in the leak-free pipeline) with an Adult exercise; fits session 7. (2) ML ch6: add "Explaining tree ensembles" (Shapley axioms, TreeSHAP usage, bias of impurity importance), which also delivers the outcome's "interpretability constraint". (3) LLM ch9: add self-study "9.6 Privacy of LLMs" (about 1.5 h): canary exposure, the training-data extraction recipe, membership inference as a likelihood-ratio test, deduplication and DP fine-tuning as mitigations, plus a paragraph on bias evaluation (BBQ-style). (4) Ethics seminar page: add 6-8 cases, each mapped to its technical chapter (recommender exposure fairness, GraphRAG re-identification, LLM hallucination in a clinical setting, voice cloning, agent autonomy, dual-use molecule generation), a regulation primer (AI Act risk tiers and GPAI duties, GDPR art. 22, model cards and datasheets), readings, and a case-memo deliverable using the facts / values / options grid.
- **Targets.** m1p1-machine-learning, m2-large-language-models, m2-ethical-issues-ai.

### OBJ-O2 (medium): generative theory stops at VAE/GAN/autoregressive
- **Evidence.** DL P1 ch9 is "AE, VAE, GAN"; diffusion appears only as a table row pointing to Multimodal GenAI. Graph ML thin_areas: "9.5 DiGress: no training loss ... relies on diffusion from Multimodal GenAI, which is an elective". DL P2 7.3: "no reverse-process derivation or sampler". No normalizing flows on either variant. Advanced DL 10.4 also uses eps_theta without DDPM.
- **Fix.** (1) DL P1: self-study "9.4 Diffusion in one section" (about 2 h): closed-form q(x_t|x_0), ELBO to eps-prediction MSE, ancestral sampler, noise = score identity, a 40-line 2-D PyTorch toy; plus a half-page box on normalizing flows (change of variables, affine coupling, exact log-likelihood). (2) DL P2 7.3: add the Gaussian posterior q(x_{t-1}|x_t,x_0), the sampler and the link between the eps-loss and the ELBO. (3) Graph ML 9.5: add the D3PM posterior and the cross-entropy loss (6-8 lines) so DiGress is self-contained.
- **Targets.** m1p1-deep-learning, m1p2-deep-learning-p2, m1p2-graph-ml.

### OBJ-O7 (medium): the programme's project vehicles are empty pages
- **Evidence.** Transverse project thin_areas: no example subjects, no domain from the master objectives, no deliverable template, milestone calendar or rubric; the checkpoint link is stale. Research and final internship pages: no milestones, templates or module map. Graph ML session 9: "start the team project" with no subject. NLP: "from data to production deployment" is bullets in 8.4. Logistics appears in no course.
- **Fix.** (1) Transverse project: add a subject bank of 6 briefs (healthcare: clinical-notes KG + RAG; finance: transaction-graph fraud GNN with LLM explanations; recommendation: text + graph recommender with cold start; logistics: graph routing with an LLM planner agent; molecules: text-conditioned graph generation; enterprise documents: GraphRAG assistant), each with required modules, dataset, baseline and success metric; a milestone calendar (proposal, mid-term review, demo, report) and a rubric; fix the checkpoint link. (2) Research internship: a 16-week milestone template, a reproducibility checklist and a report skeleton. (3) Final internship: a module map (which course chapters back which topic families). (4) Graph ML: specify the team project (subject from the final lab, deliverables, rubric). (5) NLP 8.4: a half-page serving and monitoring box on the ticket case (packaging, latency budget, drift check), pointing to MLOps.
- **Targets.** m2-projet-transverse, m1p3-research-internship, m2-internship, m1p2-graph-ml, m1p2-nlp-text-mining.

### OBJ-O3 (medium): holes in the LLM chain that depend on the DL variant
- **Evidence.** LLM (line 386) refers to "ch. 6: distillation, LoRA", but ch6 has no LoRA and Ex. 3 asks to fine-tune a 1-3B model. DL P2 thin_areas: "no definition of self-attention, positional encoding or tokenization". NLP ch7: "Architecture: carried over from the Deep Learning module ch. 6". LLM ch9 lacks "statistics for benchmark comparison".
- **Fix.** (1) LLM ch4: add "4.x Parameter-efficient fine-tuning" (LoRA: W + BA, rank, alpha/r scaling, initialization, parameter count, merging; QLoRA) and correct the dangling reference. (2) NLP ch7: a one-page self-contained "transformer block" box (attention, multi-head, sinusoidal and learned positions, residual + LayerNorm, causal mask) so DL P2 students are covered. (3) LLM ch9: add "comparing two models honestly" (bootstrap CI, paired McNemar or permutation test, variance over prompts and seeds).
- **Targets.** m2-large-language-models, m1p2-nlp-text-mining, m1p2-deep-learning-p2.

## 7. Route-level findings

### ROUTE-GLLM-O5 (medium): no course reaches O5 at depth 3
The route built for Graph x LLM tops out at 2 (Graph ML ch10, Advanced Topics ch8, Graph Gen ch7). Advanced GNN 8.3 thin_areas: "GNN x LLM injection has no formulation (projection layer, contrastive objective), no benchmark numbers and no exercise". Advanced Topics ch8 thin_areas: "no graph foundation models, no graph-token / graph-instruction-tuning methods (GraphGPT, LLaGA) and no KG completion with LLMs". **Fix**: Advanced GNN 8.3, a worked section (GNN embeddings -> MLP projector -> LLM soft tokens; graph-text contrastive alignment loss; one exercise on a text-attributed graph such as ogbn-arxiv); Advanced Topics ch8, a section on graph instruction tuning and LLM-based KG completion with one reading exercise. Together with OBJ-O5 this gives the route a depth-3 path.

### ROUTE-SYS (medium): the AI systems route has a hollow Y1 P2 and no depth-3 generative theory
The two `sys` P2 additions (CV Applications, Real-time AI) are not selectable in 2026-27, and the Choose-1 slot is DL P2; no Y2 P1 course is tagged `sys`; O2 maxes at 2, and Speech ch7 cites diffusion/flow-matching objectives it never writes. **Fix**: DL P2 7.3 diffusion completion (as OBJ-O2); Speech ch7: write the conditional flow-matching loss and the Grad-TTS score objective (half a page each); on the home tree, tag `m2-privacy-uncertainty` and `m2-boosting-foundation-tabular` with `sys` (calibration/DP and production tabular ML), and label the two P2 `sys` pages "reference, not selectable in 2026-27".

### PREREQ-CHOOSE1 (medium): prerequisites inside one choice group change which objectives are reached
Multimodal GenAI relies on KR duality, Bures and ViT that live in Optimal Transport and Advanced DL (same Choose-1). Advanced DL 10.4 uses DDPM from Multimodal GenAI (same group). DL P2 sends non-convex guarantees to Optimization for AI (same group). Geometric Data ch1-3 assume mesh background from Shapes, which gllm students do not take. **Fix**: half-page self-contained recaps: Multimodal ch0 (KR duality statement, Bures formula, ViT patching); Advanced DL 10.4 (10-line DDPM recap); DL P2 ch0 (Adam/AdamW box, non-convex SGD statement); Geometric Data, a signposted self-study "Meshes in 2 hours" (half-edge, Euler, cotangent Laplacian) so ch1-3 can be shortened.

### REDUNDANCY (low): repeated derivations crowd out weak objectives
Kirchenbauer watermark z-test in LLM 9.5, Control ch6 and ESP 9.2; speculative decoding in DL P2 ch5, LLM 6.3 and Advanced Topics ch7; RoPE in DL P1 6.2, LLM ch2, Advanced Topics ch3; DP basics in Emerging ML ch5, Privacy & UQ ch1-4, ESP ch8, Advanced GNN ch7; Chinchilla in DL P2, LLM ch3, Advanced DL ch9, Emerging ML ch7. **Fix**: name one owner per derivation and reduce the others to "recap + extension" (ESP 9.2 -> distortion-free and robust schemes; Advanced Topics ch7 -> optimal-gamma walltime derivation); freed time goes to OBJ-O5/O6/O8 content.

## 8. Stated outcomes ("What you will be able to do") that the page does not deliver

Source: the records' `thin_areas`, checked against the pages where marked. "Fix" is bounded to the chapter named.

### 8.1 Mandatory courses

| Course | Outcome as stated | Why it is not delivered | Bounded fix | Obj |
|---|---|---|---|---|
| ML | State and exploit generalization bounds | ch8.3-8.4: VC and Rademacher bounds sketched; no McDiarmid, contraction lemma not stated | state McDiarmid and the contraction lemma; one exercise applying the margin bound | O1 |
| ML | Conduct a complete unsupervised analysis | ch7: no choice of K (BIC, silhouette), no hierarchical/density clustering, no nonlinear reduction; no PCA exercise | ch7 box: K selection + t-SNE/UMAP caveats; one PCA exercise | O1 |
| ML | Choose trees/forests/boosting under an interpretability constraint | ch6: no XGBoost second-order step, no interpretability tool | TreeSHAP section (OBJ-O8) | O1 O8 |
| ML | Evaluation pipeline ... scaling up; read an ML paper | ch4.6 "big data" is one paragraph; no guided reading exercise | worked out-of-core example (partial_fit + hashing); one guided reading exercise in ch9 | O7 |
| DL P1 | Build a neural network from scratch | every sample uses autograd; no NumPy forward/backward MLP | ch2: 40-line NumPy MLP with finite-difference gradient check | O1 |
| DL P1 | Explain attention and the transformer | positional encodings named but not defined; dangling `max_n, d = 512, 128`; no cross-attention | ch6: define sinusoidal/learned PE, finish the snippet, add encoder-decoder cross-attention | O3 |
| DL P1 | Adapt a pretrained model (freezing/tuning reflexes); launch a realistic run | ch7 no worked fine-tuning; ch8 mixed precision and tracking are bullets | ch7 worked linear probe vs partial vs full fine-tuning; ch8 autocast/GradScaler + TensorBoard snippet | O1 O7 |
| DL P1 | Distinguish generative families; RNN/LSTM | no AE/VAE/GAN or RNN code; diffusion only in a table; 3 session labs unwritten | OBJ-O2 self-study 9.4; write the 3 lab sheets | O2 |
| DL P2 | Choose an architecture for text generation (causal transformer) | self-attention, PE, tokenization not defined; GQA used in Ex. 3 undefined | self-study box on attention and tokenization (OBJ-O3) | O3 |
| DL P2 | Policy gradient and deep Q-learning; derive VAE/GAN/diffusion objectives | DQN prose only; no DDPM reverse process or sampler; no exercise covers official items 4-9 | DQN pseudocode; DDPM sampler (OBJ-O2); 3 exercises (CNN equivariance, DDPM sampler, REINFORCE baseline) | O1 O2 |
| DL P2 | Write, debug and monitor a training pipeline | monitoring is a checklist, no logging code; Adam never written | ch0 Adam/AdamW box and a logging snippet | O1 O7 |
| RL | Analyze multi-agent systems | no Markov games, equilibria or MARL algorithm | ch7: half-page Markov games (definition, independent learners, self-play) + one exercise | O1 O3 |
| RL | Carry out deep RL (DDPG/SAC, offline RL); compare distributional/model-based/imitation | no DDPG/SAC code; offline RL a CQL sketch; no exercises on 6.2-6.6; labs of sessions 10-11 named only | write the "C51 vs DQN" and "BC vs DAgger" lab sheets with 30-line skeletons; specify the 50% project subjects | O1 O7 |
| RL | (intro) RLHF as a motivation | RLHF named, never defined | 3-line definition pointing to LLM ch5 | O3 |
| Graph ML | Combine graphs and LLMs (GraphRAG, hybrids) | ch10 prose only; final lab underspecified | OBJ-O5 worked case | O5 |
| Graph ML | Build E(3)-invariant and equivariant models | one definition + EGNN proposition; no code; Ex. 14 without solution | 30-line EGNN layer in PyTorch with an equivariance test; Ex. 14 solution | O4 |
| Graph ML | Generate realistic graphs | no code for any generator; DiGress without loss | D3PM loss (OBJ-O2); Ex. 15 solution sketch | O2 O4 |
| Graph ML | Handle temporal graphs without leaking the future | TGAT/TGN without loss or negative-sampling protocol | half-page temporal link-prediction protocol | O4 |
| Graph ML | Explore a graph; compare graphs with kernels | session-2 (Karate Club) and session-3 (WL + SVM on MUTAG) labs have no code; team project undefined | two short lab sheets; team-project brief (OBJ-O7) | O4 O7 |
| NLP | Fine-tune a transformer for a given task | Protocol 7.1 + `pipeline()` only; no training loop; session 8-9 lab sheets absent; Ex. 11 scheduled before fine-tuning | 40-line fine-tuning loop for a small encoder as the session-9 lab sheet; move Ex. 11 after session 9 | O3 |
| NLP | Label sequences with HMMs and CRFs | Baum-Welch deferred to ML, which defers HMMs back to NLP; CRF inference only stated | half-page Baum-Welch E/M updates; CRF forward algorithm for Z | O1 |
| NLP | Text mining project from data to production deployment | 8.4 bullets (drift, retraining); RAG one bullet though session 12 lists it | serving/monitoring box (OBJ-O7) | O7 |
| NLP | (implied by capstone) NER + relations to a KG | relation extraction never taught | 6.4 Relation extraction (OBJ-O5) | O5 |
| LLM | Implement alignment methods (SFT, RLHF, DPO, GRPO) | no DPO/GRPO code; GRPO formula omits the importance ratio and clipping; SFT two definitions | correct the GRPO objective; 30-line DPO loss; SFT data-quality paragraph | O3 |
| LLM | Explain the complete pipeline | LoRA/PEFT and distributed training absent; mini-GPT lab without code | PEFT section (OBJ-O3); one paragraph on data/tensor/pipeline parallelism pointing to DL P2 ch2-4 | O3 |
| LLM | Explore agents, multimodality | narrative only | agent evaluation protocol (task success, p^k, cost per task) + one exercise; 8.2b VLM self-study (OBJ-O6) | O3 O6 |
| LLM | Evaluate performance and safety with rigorous protocols | no statistics for comparisons, no red-teaming protocol, no fairness/privacy | OBJ-O3 statistics + OBJ-O8 privacy section | O3 O8 |
| Geometric Data | Train networks that operate directly on surfaces | DiffusionNet gradient block inaccurate, no training recipe, lab skeleton with shape bugs | fix the skeleton; add loss, augmentation and spectral precomputation recipe | O4 O6 |
| Geometric Data | Correspondence (by deep learning) | learned functional maps are two bullets | half-page differentiable FMap layer + unsupervised loss; turn one level-2 session into level 3 | O4 |
| Geometric Data | Parameterize and process surfaces | LSCM without formulas; spectral-smoothing code buggy | LSCM energy; fix the code | O4 |
| Transverse project / internships / ethics | all framing outcomes ("define done in usage terms", "state a question, read the literature", "cases, readings, argumentation") | no template, subject, milestone, reading or rubric | OBJ-O7 and OBJ-O8 page fixes | O7 O8 |

### 8.2 Electives, slot-TBC and refresher pages (most consequential gaps)

| Course | Outcome not delivered | Reason (record thin_areas) | Bounded fix | Obj |
|---|---|---|---|---|
| Multimodal GenAI | Score matching; assemble the text-to-image pipeline | no denoising-score-matching theorem, no Langevin; no Diffusers code; flow matching never taught (used by pi0) | DSM theorem; 40-line Diffusers pipeline; half-page flow-matching box | O2 O6 |
| Graph Generative Models | Explain DeepGMG/GraphRNN in detail; derive graph-VAE ELBO | no GraphRNN/VAE code, promised labs absent; Example 3.4 "to be written"; DiGress mechanics inaccurate | toy GraphRNN lab; finish Example 3.4; correct ch5 | O2 O4 |
| Control in GenAI | From the reward model to policy optimization; grammar-constrained decoding | no reward-model objective or PPO/GRPO step; only regular languages; Thm 2.2 wrongly claims exactness | Bradley-Terry objective + one PPO step; pushdown/JSON-schema note; correct Thm 2.2 (local renormalization distorts) | O3 |
| Image Synthesis | Write a Monte Carlo path tracer; interactive rendering system | GGX/Smith and MIS weights not written; no MVP matrices or host code; NeRF/3DGS without loss | write D, G and MIS weights; MVP section; NeRF photometric loss | O6 O7 |
| Speech | Size a streaming system; explain diffusion and flow TTS | one exercise; flow-matching and Grad-TTS objectives not written | WER(lambda) lab; write both objectives (ROUTE-SYS) | O6 O2 |
| Advanced DL | Replicate DINOv2 / muP projects | DINOv2 objective and muP table absent; diffusion assumed | DINO loss formula; muP table; DDPM recap (PREREQ-CHOOSE1) | O1 |
| Security & Robustness | Transpose the approach to LLMs and graphs | ch9 one paragraph; no graph or text lab | Nettack-on-GCN mini-lab or a GCG-on-small-LM lab | O8 O4 O3 |
| ESP-LLMs | Explain by SHAP, LIME or gradients; anonymize | only IG; no LIME/KernelSHAP; anonymization three prose traps; no graph content | LIME and KernelSHAP procedures + exercise; k-anonymity box; GraphRAG-injection variant of Ex. 8 | O8 O5 |
| Privacy & UQ | Audit the uncertainty of an LLM; DP-SGD guarantee | ch11 descriptive; amplification by subsampling not derived | semantic-entropy formula; subsampling amplification statement | O8 O3 |
| MLOps | CI that tests models; arbitrate API vs fine-tune vs distillation | Hoeffding only; no distillation economics; no graph ops | paired bootstrap/McNemar gate; crossover formula; graph-index freshness box | O7 O4 |
| Advanced GNN | Diagnose over-squashing; situate GNN x LLM bridges | incorrect lambda_max bound; 8.3 prose | correct Cheeger-type bound; ROUTE-GLLM-O5 section | O4 O5 |
| Advanced Topics LLMs | Analyze long context; LLMs x graphs | ring-attention and YaRN formulas missing for Ex. 6-7; ch8 only three papers; multimodal LLMs absent | write the formulas; ROUTE-GLLM-O5 section | O3 O5 |
| Boosting to Foundation | Write and debug text-to-SQL; use TabPFN | text-to-SQL one definition; PFN objective unwritten | execution-accuracy metric + error taxonomy; PFN NLL objective | O3 O1 |
| Emerging ML | Fairness across participants, incentives | DP/EO not defined; no federated fairness algorithm | q-FFL / agnostic FL half page | O8 |
| Optimal Transport | Implement Sinkhorn; fairness trade-off lab | only `ot.sinkhorn`; ch6 lab code broken | 15-line log-domain Sinkhorn; fix ch6 code | O1 O8 |
| Optimization for AI | Prove acceleration optimality and FISTA rates; connect to NN training | lower bound and FISTA admitted; no diverging-run lab code | prove the FISTA rate; lab code | O1 |
| Image Analysis & CV | Implement CNNs for detection and segmentation; graph cuts | ch9 no code, losses or exercise; no max-flow algorithm | detection/segmentation losses + fine-tuning lab sheet; augmenting-path box | O1 O6 |
| TDA | Vectorize persistence into an ML pipeline; Mapper | one landscape + SVM example on synthetic circles; no Mapper code | a graph-classification lab with PersLay or sliced-Wasserstein kernel | O4 |
| Shapes | Non-rigid correspondence; reconstruct with guarantees; curves | functional maps one paragraph; no reconstruction or Bezier exercise | C-matrix least squares + one exercise each | O4 O6 |
| Signal Processing | Spectral representation for learning | STFT inversion and spectral losses absent | overlap-add/COLA + multi-resolution STFT loss | O6 |
| Computer Animation | Industry methods in C++/OpenGL | no C++/OpenGL lab support; rigid-body contact with spin missing | contact impulse with rotation; lab stub | O7 |
| CV Applications (slot TBC) | Use SAM; implement MOT; measure dataset bias | no code, no MOTA/IDF1 exercise, no bias metric | SAM prompt example; MOT exercise; per-subgroup metric | O7 O8 |
| Real-time AI (slot TBC) | Conversational LLM NPC within a latency budget; self-play | no async-call architecture or latency method; no RL/self-play material | async-call pattern + budget method; self-play lab sheet | O3 O7 |
| Refresher Statistics | Confidence intervals/tests; regression | in-class hours cover ch1, 2, 4, 5 only; no concentration inequalities | add Hoeffding to ch4; mark ch6-7 as required self-study | O1 |
| Refresher CS | Linked structures; spanning trees | no linked-list section; no Kruskal/Prim code | short sections + one MST exercise | O4 |
| Refresher Neural Nets | Measured loss-curve comparisons | relies on an external notebook; no full training loop | inline training loop and reference numbers | O1 |

## 9. Finding index

| Id | Severity | Objectives | Targets |
|---|---|---|---|
| OBJ-O5 | high | O5 | m1p2-graph-ml, m1p2-nlp-text-mining, m2-large-language-models |
| OBJ-O6 | high | O6 | m2-large-language-models, m2-geometric-deep-learning, m1p1-deep-learning |
| OBJ-O8 | high | O8 | m1p1-machine-learning, m2-large-language-models, m2-ethical-issues-ai |
| OBJ-O2 | medium | O2 | m1p1-deep-learning, m1p2-deep-learning-p2, m1p2-graph-ml |
| OBJ-O7 | medium | O7 | m2-projet-transverse, m1p3-research-internship, m2-internship, m1p2-graph-ml, m1p2-nlp-text-mining |
| OBJ-O3 | medium | O3 | m2-large-language-models, m1p2-nlp-text-mining, m1p2-deep-learning-p2 |
| ROUTE-GLLM-O5 | medium | O5 | m2-advanced-gnn, m2-advanced-topics-llms |
| ROUTE-SYS | medium | O2 O6 | m1p2-deep-learning-p2, m2-speech-technology, m2-privacy-uncertainty, m2-boosting-foundation-tabular |
| PREREQ-CHOOSE1 | medium | O1 O2 O4 O6 | m1p2-multimodal-genai, m1p2-advanced-deep-learning, m1p2-deep-learning-p2, m2-geometric-deep-learning |
| OUT-* (section 8.1) | medium | per row | the 8 mandatory science pages |
| OUT-ELECTIVES (section 8.2) | medium/low | per row | elective and slot-TBC pages |
| REDUNDANCY | low | O3 O8 | m2-explainability-security-privacy-llms, m2-advanced-topics-llms, m2-control-generative-ai |
