# Coherence of the science courses with objectives O1 to O8

This report scores the chapter body of every science course. A session plan line that names a section the chapter does not contain does not raise the score. The folder `specs/coherence-2026-10/` is the 22 October 2026 before-state. `python3 tools/check_coherence_map.py` reads the score table below.

Depth is the scale from that archive. 0 means absent. 1 means a mention, a pointer, or a single bullet, with nothing a student can use. 2 means a section that teaches the objective and still leaves a sub-topic, a derivation, or an exercise out. 3 means several chapters with derivations and exercises, a lab, or a project on the page.

## Objective definitions

The wording follows section 1 of `specs/coherence-2026-10/objectives.md`.

| Id | Objective |
|---|---|
| O1 | ML and DL foundations. Statistical learning, optimisation, neural architectures, and training. |
| O2 | Generative modelling theory. Probabilistic models, VAEs, GANs, flows, diffusion, and autoregressive models. |
| O3 | Large language models. Transformers, pre-training, fine-tuning and alignment, inference, retrieval and agents, and evaluation. |
| O4 | Graph-structured data. GNNs and graph learning for networks, molecules, and logistics. |
| O5 | Graph x LLM. Knowledge graphs with LLMs, GraphRAG, and neuro-symbolic reasoning. This is the distinctive emphasis. |
| O6 | Multimodal generative AI. Vision, language, speech, and 3D or geometric data. |
| O7 | Hands-on and industry practice. Projects, case studies, industry domains, deployment, and research readiness. |
| O8 | Trustworthy and responsible AI. Robustness, privacy, explainability, uncertainty, and ethics. |

Nine course directories are framing pages. They have no science row. They are `m1-humanites`, `m1-langues`, `m1-sports`, `m1p1-strategy-marketing`, `m1p2-startup-entrepreneurship`, `m2-ethical-issues-ai`, `m1p3-research-internship`, `m2-internship`, and `m2-projet-transverse`.

## Score matrix

One integer per cell, from 0 to 3. Every number is copied from section 2 of the archive except two cells. `m1p2-nlp-text-mining` O2 is 2. Model 1.6 proves an interpolated Kneser-Ney bigram. There is still no VAE, GAN, flow, or diffusion on that page, so the cell is not 3. `m1p1-refresher-neural-nets` O7 is 2. Section 2.3 is an in-page NumPy training loop. The projects section says those projects exercise O1 only.

Reasons below changed because the chapter body changed. Every other score is unchanged.

LLM O3 stays 3. Chapter 4 now teaches prompting, in-context learning, LoRA, and logit distillation. Distributed training is still absent.

Relation extraction is still only named in NLP chapter 6. The chapter does not teach it.

Machine Learning has no group-fairness section and no TreeSHAP. O8 on that page stays 1.

LLM section 7.4 is still one GraphRAG bullet. O5 on that page stays 1. Sections 8.2b and 9.7 are not in the chapters.

Deep Learning (P2) still does not define self-attention and has no ancestral sampler.

Graph ML chapter 10 is still prose. O5 on that page stays 2. No course reaches O5 at 3.

The mean-curvature normal already matches on Shapes and on Geometric Data. Both write it as the outward-normal form in the notation page.

| Course | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|---|---|---|---|---|---|---|---|---|
| `m1p1-refresher-statistics` | 2 | 1 | 1 | 1 | 0 | 0 | 1 | 1 |
| `m1p1-refresher-cs` | 1 | 0 | 1 | 2 | 0 | 0 | 2 | 0 |
| `m1p1-refresher-neural-nets` | 2 | 0 | 1 | 0 | 0 | 0 | 2 | 0 |
| `m1p1-machine-learning` | 3 | 1 | 1 | 1 | 0 | 0 | 2 | 1 |
| `m1p1-deep-learning` | 3 | 2 | 2 | 1 | 1 | 1 | 2 | 0 |
| `m1p2-deep-learning-p2` | 3 | 2 | 2 | 1 | 0 | 0 | 2 | 2 |
| `m1p2-reinforcement-learning` | 3 | 1 | 2 | 1 | 1 | 0 | 2 | 1 |
| `m1p2-graph-ml` | 2 | 2 | 1 | 3 | 2 | 1 | 2 | 1 |
| `m1p2-nlp-text-mining` | 2 | 2 | 2 | 1 | 1 | 0 | 3 | 1 |
| `m2-large-language-models` | 2 | 2 | 3 | 1 | 1 | 1 | 2 | 2 |
| `m2-geometric-deep-learning` | 1 | 1 | 0 | 2 | 0 | 2 | 2 | 1 |
| `m1p1-signal-processing` | 2 | 1 | 1 | 1 | 0 | 2 | 2 | 0 |
| `m1p1-emerging-ml` | 2 | 0 | 1 | 1 | 0 | 0 | 2 | 3 |
| `m1p1-computer-animation` | 1 | 1 | 0 | 1 | 0 | 1 | 2 | 0 |
| `m1p1-computer-vision` | 2 | 0 | 0 | 1 | 0 | 2 | 2 | 0 |
| `m1p1-tda` | 1 | 1 | 1 | 2 | 0 | 1 | 2 | 1 |
| `m1p1-shapes` | 1 | 0 | 0 | 2 | 0 | 2 | 1 | 0 |
| `m1p2-multimodal-genai` | 2 | 3 | 1 | 1 | 1 | 3 | 2 | 1 |
| `m1p2-optimal-transport` | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 2 |
| `m1p2-optimization-ai` | 3 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
| `m1p2-advanced-deep-learning` | 3 | 1 | 1 | 1 | 0 | 1 | 3 | 2 |
| `m1p2-image-synthesis` | 1 | 1 | 0 | 0 | 0 | 2 | 2 | 0 |
| `m1p2-computer-vision-applications` | 2 | 0 | 0 | 1 | 0 | 1 | 3 | 2 |
| `m1p2-realtime-ai-videogames` | 1 | 0 | 1 | 1 | 0 | 0 | 2 | 1 |
| `m2-advanced-gnn` | 2 | 1 | 1 | 3 | 1 | 1 | 2 | 2 |
| `m2-privacy-uncertainty` | 2 | 1 | 1 | 0 | 0 | 0 | 2 | 3 |
| `m2-boosting-foundation-tabular` | 3 | 1 | 1 | 0 | 0 | 0 | 3 | 1 |
| `m2-control-generative-ai` | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 |
| `m2-mlops-llm-engineering` | 1 | 0 | 2 | 0 | 1 | 0 | 3 | 2 |
| `m2-security-robustness` | 2 | 0 | 1 | 1 | 0 | 0 | 2 | 3 |
| `m2-graph-generative-models` | 1 | 3 | 1 | 2 | 2 | 2 | 2 | 1 |
| `m2-explainability-security-privacy-llms` | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 3 |
| `m2-speech-technology` | 2 | 2 | 1 | 0 | 0 | 3 | 2 | 2 |
| `m2-advanced-topics-llms` | 1 | 1 | 3 | 1 | 2 | 0 | 2 | 1 |
| `m1p1-probability-monte-carlo` | 2 | 2 | 0 | 0 | 0 | 0 | 1 | 1 |
| `m1p1-dbms` | 1 | 0 | 1 | 1 | 1 | 0 | 2 | 1 |
| `m1p1-statistical-learning-theory` | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| `m1p2-responsible-ai-sustainability` | 2 | 0 | 1 | 0 | 0 | 0 | 2 | 2 |
| `m1p2-statistics-in-action` | 2 | 0 | 0 | 1 | 0 | 0 | 2 | 1 |
| `m1p2-social-media-probabilistic` | 1 | 2 | 0 | 2 | 0 | 0 | 1 | 1 |

## Path maxima

The maximum on a path is the highest cell among courses on that path. Framing pages do not raise it.

The mandatory path is Machine Learning, one of the two Deep Learning courses, Reinforcement Learning, Graph ML, NLP, Large Language Models, and Geometric Data.

The Graph x LLM route adds Deep Learning (P1), Emerging ML, Topological Data Analysis, Multimodal Generative AI, Advanced GNN, Control in Generative AI, MLOps, Security and Robustness, Graph Generative Models, Explainability Security and Privacy of LLMs, and Advanced Topics in LLMs.

The AI systems route uses Deep Learning (P2) for the single Deep Learning requirement and adds Signal Processing, Computer Vision, Shapes, MLOps, Security and Robustness, Explainability Security and Privacy of LLMs, and Speech. Computer Vision Applications and Real-time AI in Video Games are tagged on the home page and are not in the 2026-27 choice lists.

| Objective | Mandatory path | Graph x LLM route | AI systems route |
|---|---|---|---|
| O1 | 3 | 3 | 3 |
| O2 | 2 | 3 | 2 |
| O3 | 3 | 3 | 3 |
| O4 | 3 | 3 | 3 |
| O5 | 2 | 2 | 2 |
| O6 | 2 | 3 | 3 |
| O7 | 3 | 3 | 3 |
| O8 | 2 | 3 | 3 |

O3 is 3 on every path because the Large Language Models page is mandatory. Prompting and LoRA are on that page, in section 4.0 and Definition 4.3. Attention is still undefined for students who take only Deep Learning (P2). Distributed training is still absent from the LLM chapters.

O2 stays 2 on the mandatory path and on the AI systems route. NLP now supplies an interpolated Kneser-Ney bigram, which is an autoregressive model at depth 2. No mandatory page derives a normalizing flow. Deep Learning (P2) states a diffusion objective and does not give an ancestral sampler. The Graph x LLM route reaches 3 in Multimodal Generative AI and in Graph Generative Models.

O5 stays 2 on every path. Graph ML chapter 10 is the only mandatory source at 2, and it is prose. No page reaches 3.

O6 on the mandatory path is 2 from Geometric Data, which teaches 3D analysis. The generative multimodal part of the LLM page is still the four bullets of section 8.2. The routes reach 3 in Multimodal Generative AI and in Speech.

O8 on the mandatory path is 2 from LLM chapter 9. Machine Learning does not teach group fairness or TreeSHAP.

## Fix register

This table is the gap list. Each row names the page and one fix. Size is small or large. Status is applied or backlog. Applied rows are local edits on the page that already existed. Backlog rows are chapter rewrites that this report does not pretend have landed.

| Id | Path | Size | Status | Fix |
|---|---|---|---|---|
| ER-H01 | `courses/m1p1-probability-monte-carlo/index.qmd` | large | backlog | Rewrite exercise 2 so the triangle walk is irreducible and aperiodic, with returns in 2 steps and in 3 steps. |
| ER-H02 | `courses/m1p1-probability-monte-carlo/index.qmd` | small | applied | Write the MALA log-ratio as `q(y, x) - q(x, y)`. |
| ER-H03 | `courses/m1p1-statistical-learning-theory/index.qmd` | small | applied | State corollary (i) as consistency relative to H, and keep universal consistency for a growing sieve. |
| ER-H04 | `courses/m1p2-realtime-ai-videogames/index.qmd` | small | applied | Drop the leading minus on separation and divide by the squared distance. |
| ER-H05 | `courses/m1p2-social-media-probabilistic/index.qmd` | small | applied | Take the second-largest eigenpair from `eigsh`, not column 1 of `which="LA"`. |
| ER-H06 | `courses/m1p2-image-synthesis/index.qmd` | small | applied | Set `E_ca(p) = 3(p_x - 1)`, mark pixel (2, 2) inside with edge values 4, 5, and 3, and subtract `(b_y - a_y)` when x increases by 1. |
| ER-H07 | `courses/m1p2-optimal-transport/index.qmd` | small | applied | Return each person their own repaired value, weighted by group mass. |
| ER-H08 | `courses/m2-advanced-gnn/index.qmd` | large | backlog | Tie over-squashing to the spectral gap and to Cheeger, and stop using lambda max as the bottleneck. |
| ER-H09 | `courses/m2-control-generative-ai/index.qmd` | large | backlog | Separate masking, which gives validity, from exact conditioning, and align the Graph Generative Models citation. |
| ER-H10 | `courses/m1p2-deep-learning-p2/index.qmd` | small | applied | Change the expected GPT-2 small count from `2.2e21` to `2.2e18` FLOPs. |
| ER-H11 | `courses/m1p2-optimization-ai/index.qmd` | small | applied | Conclude that 0 is in the subdifferential, and allow a nonzero subgradient to remain. |
| C1 | `courses/m1p1-shapes/index.qmd` | small | applied | No edit. Shapes and Geometric Data already write the mean-curvature normal as the outward form on the notation page. |
| C2 | `courses/m1p2-graph-ml/index.qmd` | small | applied | Make PageRank alpha the teleport probability in both displays, and say that TextRank `d` equals `1 - alpha`. |
| C3 | `courses/m1p2-advanced-deep-learning/index.qmd` | small | applied | Write classifier-free guidance as unconditional plus `w` times (conditional minus unconditional). |
| C4 | `courses/m2-graph-generative-models/index.qmd` | small | applied | Use row vectors `X_{t-1} Q_t` next to the row-stochastic claim in Definition 5.1. |
| C5 | `courses/m1p1-emerging-ml/index.qmd` | small | applied | Call `lambda_2(L)` algebraic connectivity, and call `1 - abs(lambda_2(W))` the spectral gap of the mixing matrix. |
| C6 | `courses/m2-advanced-gnn/index.qmd` | small | applied | Let `p` be the probability of a truthful answer, with `epsilon = ln(p/(1-p))`, in the edge-DP note and in exercise 10. |
| C7 | `courses/m1p1-shapes/index.qmd` | small | applied | Call `I - D^{-1}A` the random-walk Laplacian. |
| C8 | `courses/m1p2-graph-ml/index.qmd` | small | applied | Use center `v_w` and context `u_c` in derivation 3.1 and in NLP exercise 9. |
| C9 | `courses/m1p2-computer-vision-applications/index.qmd` | small | applied | Put the distillation weight on the teacher KL term at temperature `T`, and use the same roles in Responsible AI. |
| C10 | `courses/m1p1-shapes/index.qmd` | small | applied | Start Definition 8.1 at `0 = lambda_1`, reindex the cycle so the zero mode is `lambda_1`, and say the Dirichlet chain has no zero eigenvalue. |
| PTR-LORA | `courses/m2-mlops-llm-engineering/index.qmd` | small | applied | Delete the claim that the LLM module skips LoRA, and point at section 4.0 and Definition 4.3. |
| PTR-ICL | `courses/m2-explainability-security-privacy-llms/index.qmd` | small | applied | Point the in-context learning example at LLM section 4.0. |
| PTR-DISTILL | `courses/m1p2-nlp-text-mining/index.qmd` | small | applied | Point the distillation sentence at LLM section 4.4, because chapter 6 is inference. |
| PTR-ATTN | `courses/m1p2-graph-ml/index.qmd` | small | applied | Say that attention is defined in Deep Learning (P1) chapter 6, is not defined on the P2 page, and is reading for students on the P2 route. The same sentence is on Reinforcement Learning and on NLP. |
| PTR-OPT | `courses/m1p2-deep-learning-p2/index.qmd` | small | applied | Mark Optimization for AI citations as optional reading from the same Choose-1 slot, and keep the rate already written on the page. |
| PTR-RAG | `courses/m1p2-graph-ml/index.qmd` | small | applied | Add a short retrieve-then-generate recall in chapter 10, name BM25 as the NLP baseline, and point the full treatment at LLM chapter 7. |
| PTR-DDPM | `courses/m1p2-graph-ml/index.qmd` | small | applied | State the DDPM forward step and the FID definition where chapter 9 treats them as known, and say the derivation is in the optional Multimodal course. The same two sentences are on Geometric Data chapter 8. |
| PTR-GDL | `courses/m2-geometric-deep-learning/index.qmd` | small | applied | Say that chapter 0 is what the page guarantees, and that Optimal Transport, Multimodal, and Advanced GNN are optional. |
| PTR-CTRL | `courses/m2-control-generative-ai/index.qmd` | small | applied | Say that Graph Generative Models is a Year 2 Period 2 course and that chapter 8 currently assumes its chapters 3 to 5. |
| PTR-SESS | `courses/m1p1-machine-learning/index.qmd` | small | applied | Point session-plan hours at blocks that exist, on Machine Learning, NLP, the LLM page, Deep Learning (P2), and Geometric Data. |
| OBJ-O5 | `courses/m1p2-graph-ml/index.qmd` | large | backlog | Teach relation extraction on the NLP page, a worked GraphRAG in Graph ML chapter 10, and more than one bullet in LLM section 7.4. |
| OBJ-O6 | `courses/m2-large-language-models/index.qmd` | large | backlog | Add a worked vision-language section. Sections 8.2b and the Geometric Data bridges named in the October plan are not in the chapters. |
| OBJ-O8 | `courses/m1p1-machine-learning/index.qmd` | large | backlog | Add group fairness and TreeSHAP on Machine Learning, and a privacy section on the LLM page. Section 9.7 is not in the chapters. |
| OBJ-O2 | `courses/m1p2-deep-learning-p2/index.qmd` | large | backlog | Derive the ancestral sampler on Deep Learning (P2) and a diffusion section on Deep Learning (P1). Do not add that chapter in this pass. |
| OBJ-O3 | `courses/m1p2-deep-learning-p2/index.qmd` | large | backlog | Define self-attention on the P2 page, or in a box the P2 student actually meets. Prompting and LoRA are no longer this gap. |
| OBJ-O7 | `courses/m2-projet-transverse/index.qmd` | large | backlog | The project, internship, and ethics pages are still framing. Subjects, exams, and assessment rules are out of scope here. |
| ROUTE-O5 | `courses/m2-advanced-gnn/index.qmd` | large | backlog | Give Advanced GNN section 8.3 and Advanced Topics chapter 8 a formulation and an exercise so some page can reach O5 at 3. |
| R1 | `courses/m1p2-multimodal-genai/index.qmd` | large | backlog | Keep the VAE and GAN derivations on Deep Learning (P1) chapter 9, and leave the Multimodal copies in place. |
| R2 | `courses/m2-control-generative-ai/index.qmd` | large | backlog | Keep the watermark z-test on LLM chapter 9.5, and leave the Control and Explainability copies in place. |
| R3 | `courses/m2-large-language-models/index.qmd` | large | backlog | Keep the KL-regularised closed form on Reinforcement Learning chapter 6, and leave the LLM and Control copies in place. |
| R4 | `courses/m2-geometric-deep-learning/index.qmd` | large | backlog | Keep the EGNN proof on Graph ML proposition 8.3, and leave the Geometric Data and Advanced GNN copies in place. |
| R5 | `courses/m1p2-graph-ml/index.qmd` | large | backlog | Keep the skip-gram derivation on NLP theorem 4.1, and leave the Graph ML derivation in place aside from the letter change in C8. |
| R6 | `courses/m2-advanced-topics-llms/index.qmd` | large | backlog | Keep RoPE, mixture-of-experts, the KV cache, speculative decoding, Chinchilla, and judge bias on the LLM page, and leave the later copies in place. |
| R7 | `courses/m1p1-shapes/index.qmd` | large | backlog | Keep the discrete differential geometry derivations on Geometric Data, and leave the Shapes derivations in place aside from C1, C7, and C10. |
| R8 | `courses/m1p2-computer-vision-applications/index.qmd` | large | backlog | Keep detection metrics and stereo on Computer Vision, and leave the applications-page copies in place aside from C9. |
| R9 | `courses/m1p2-deep-learning-p2/index.qmd` | large | backlog | Keep the MDP and policy-gradient proofs on Reinforcement Learning, and leave the P2 recall in place. |
| R10 | `courses/m2-explainability-security-privacy-llms/index.qmd` | large | backlog | Keep membership inference on Security definition 8.3 and the DP proofs on Privacy and Uncertainty, and leave the other copies in place. |
| R11 | `courses/m2-control-generative-ai/index.qmd` | large | backlog | Keep the classifier-free guidance identity on Multimodal theorem 4.1, and leave the Control and Graph Generative Models copies in place aside from C3. |
| R12 | `courses/m2-graph-generative-models/index.qmd` | large | backlog | Keep the conditioning taxonomy on Graph ML chapter 9, and leave the later copies in place. The masking theorem is ER-H09 and stays backlog. |
| R13 | `courses/m1p1-shapes/index.qmd` | large | backlog | Keep simplicial homology on Topological Data Analysis, and leave the Shapes chapter 9 copy in place. |
| R14 | `courses/m2-advanced-gnn/index.qmd` | small | backlog | Map the hybrid category names onto Graph ML section 10.2 in one sentence on Advanced GNN and on Advanced Topics. Do not rewrite the chapters. |

## Redundancies

R1 to R14 are the repeated derivations from section 1 of `specs/coherence-2026-10/redundancy-notation.md`. The canonical page is the one a later edit would keep. The other pages still contain the full derivation. Every recall is backlog. This pass does not delete a duplicate derivation.

| Id | Canonical page | Other pages |
|---|---|---|
| R1 | `m1p1-deep-learning` chapter 9 | `m1p2-multimodal-genai` chapters 0 to 2 |
| R2 | `m2-large-language-models` chapter 9.5 | `m2-control-generative-ai` chapter 6, `m2-explainability-security-privacy-llms` section 9.2 |
| R3 | `m1p2-reinforcement-learning` chapter 6 | `m2-large-language-models` chapter 5, `m2-control-generative-ai` theorem 5.1 |
| R4 | `m1p2-graph-ml` proposition 8.3 | `m2-geometric-deep-learning` chapter 7, `m2-advanced-gnn` section 8.1 |
| R5 | `m1p2-nlp-text-mining` theorem 4.1 | `m1p2-graph-ml` derivation 3.1, `m1p1-deep-learning` section 6.5 |
| R6 | `m2-large-language-models` | `m2-advanced-topics-llms`, `m2-mlops-llm-engineering`, `m1p1-deep-learning`, `m1p2-deep-learning-p2`, `m1p2-advanced-deep-learning`, `m1p1-emerging-ml` |
| R7 | `m2-geometric-deep-learning` chapters 1 to 3 and 5 | `m1p1-shapes` chapters 5, 7, and 8 |
| R8 | `m1p1-computer-vision` chapters 6 and 9 | `m1p2-computer-vision-applications` |
| R9 | `m1p2-reinforcement-learning` chapters 1, 5, and 6 | `m1p2-deep-learning-p2` section 7.2 |
| R10 | `m2-security-robustness` definition 8.3, and `m2-privacy-uncertainty` chapters 1 to 4 | `m2-explainability-security-privacy-llms` chapter 8, `m1p1-emerging-ml` chapter 5 |
| R11 | `m1p2-multimodal-genai` theorem 4.1 | `m2-control-generative-ai` chapter 7, `m2-graph-generative-models` chapter 7 |
| R12 | `m1p2-graph-ml` chapter 9, and `m2-control-generative-ai` theorem 2.2 | `m2-graph-generative-models` chapters 3 and 7 |
| R13 | `m1p1-tda` chapters 3 and 4 | `m1p1-shapes` chapter 9 |
| R14 | `m1p2-graph-ml` section 10.2 | `m2-advanced-gnn` section 8.3, `m2-advanced-topics-llms` chapter 8 |

## Prerequisite breaks that are still true

The October prerequisite table is `specs/coherence-2026-10/prerequisites.md`. The rows below are the breaks that the chapter body still has. A sentence-level fix is marked applied. A missing chapter is backlog.

Attention is defined in Deep Learning (P1) chapter 6. It is not defined on the Deep Learning (P2) page. Graph ML, NLP, and Reinforcement Learning now say that students on the P2 route need the P1 chapter as reading. That sentence is applied. A transformer block on the P2 page is backlog.

Classic RAG is used in Graph ML chapter 10 in Year 1 Period 2. The full treatment is LLM chapter 7 in Year 2 Period 1. A short recall on the Graph ML page is applied. It defines retrieve-then-generate and names BM25. A worked RAG chapter in Year 1 is backlog.

Deep Learning (P2) cites Optimization for AI for rates the page also writes locally. Those citations are now optional reading from the same Choose-1 slot. The written rate stays. A self-contained non-convex chapter is backlog.

Graph ML section 9.5 and Geometric Data chapter 8 use a diffusion step and a FID-style distance whose derivation lives in Multimodal Generative AI. Two or three sentences now state the forward step and the definition of FID, and they say that course is optional. A diffusion chapter on the mandatory pages is backlog.

Geometric Data points at Optimal Transport chapter 5, at Multimodal, and at Advanced GNN. One clause now says chapter 0 is what the page guarantees and those courses are optional. Mesh, Fourier, and graph-transformer boxes beyond chapter 0 are backlog.

Control chapter 8 assumes Graph Generative Models chapters 3 to 5. One sentence now says that course is Year 2 Period 2. Rewriting chapter 8 so it stands on Graph ML chapter 9 is backlog. Theorem 2.2 is ER-H09 and is backlog.

Prompting and in-context learning are LLM section 4.0. The October claim that they are taught nowhere is closed. LoRA is Definition 4.3. The MLOps sentence that said the LLM module skips LoRA is removed.

Relation extraction is still only a name in NLP chapter 6. A section that teaches it is backlog.

Group fairness, TreeSHAP, and a mandatory differential-privacy chapter are still absent from the mandatory path. Those sections are backlog.

Reinforcement Learning still points Markov chains at the off-list probability course. A mandatory home for that recap, beyond the existing chapter 0 box, is backlog.

## High-severity errors

Eleven high-severity errors were confirmed in `specs/coherence-2026-10/errors.md`. Eight are applied. Three stay backlog. ER-H01, ER-H08, and ER-H09 are the backlog rows. The corrected statements for those three stay in the archive. This pass does not rewrite them.

| Id | Page | Status |
|---|---|---|
| ER-H01 | `m1p1-probability-monte-carlo` | backlog |
| ER-H02 | `m1p1-probability-monte-carlo` | applied |
| ER-H03 | `m1p1-statistical-learning-theory` | applied |
| ER-H04 | `m1p2-realtime-ai-videogames` | applied |
| ER-H05 | `m1p2-social-media-probabilistic` | applied |
| ER-H06 | `m1p2-image-synthesis` | applied |
| ER-H07 | `m1p2-optimal-transport` | applied |
| ER-H08 | `m2-advanced-gnn` | backlog |
| ER-H09 | `m2-control-generative-ai` | backlog |
| ER-H10 | `m1p2-deep-learning-p2` | applied |
| ER-H11 | `m1p2-optimization-ai` | applied |

## Notation

The site-wide convention is `notation/index.qmd`. C1 already matches on Shapes and on Geometric Data, so those pages were not edited for the sign. C2 to C10 are applied on the side that disagreed with that page. The agreeing side is left as it was. Multimodal and Control are not edited for the guidance weight. Definition 8.5 on Shapes is not reindexed.

| Id | Disagreeing page | What the edit does |
|---|---|---|
| C1 | none in this pass | Mean curvature already matches. |
| C2 | `m1p2-graph-ml`, `m1p2-nlp-text-mining`, `m2-advanced-gnn` | Alpha is the teleport probability. TextRank may keep `d` with `d = 1 - alpha`. Advanced GNN says teleport where it used to say damping. |
| C3 | `m1p2-advanced-deep-learning` | Guidance uses unconditional plus `w` times the difference of conditional and unconditional. |
| C4 | `m2-graph-generative-models` | Definition 5.1 multiplies row vectors on the right by a row-stochastic `Q_t`. |
| C5 | `m1p1-emerging-ml` | `lambda_2(L)` is algebraic connectivity. The spectral gap of `W` is `1 - abs(lambda_2(W))`. |
| C6 | `m2-advanced-gnn` | `p` is the probability of a truthful answer. |
| C7 | `m1p1-shapes` | `I - D^{-1}A` is the random-walk Laplacian. |
| C8 | `m1p2-graph-ml`, `m1p2-nlp-text-mining` | Center is `v_w` and context is `u_c`. |
| C9 | `m1p2-computer-vision-applications`, `m1p2-responsible-ai-sustainability` | The weight sits on the teacher KL term and the temperature is `T`. |
| C10 | `m1p1-shapes` | The spectrum in Definition 8.1 starts at `0 = lambda_1`. The cycle example uses that index. The Dirichlet chain has no zero eigenvalue. |

## What this means for a student on the mandatory path

This section is a reading of the scores. It is not a new policy.

A student on the mandatory science courses meets O1 and O4 at depth 3. O3 reaches 3 on the Large Language Models page, which teaches prompting, in-context learning, LoRA, and logit distillation. A student who takes only Deep Learning (P2) still has no definition of self-attention on that page, and needs Deep Learning (P1) chapter 6 as reading. O2 stays at 2. The NLP page now proves an interpolated Kneser-Ney bigram, and no mandatory page derives a flow or an ancestral sampler. O5 stays at 2, from the prose of Graph ML chapter 10, and relation extraction is only named. O6 stays at 2 from 3D analysis on Geometric Data. The generative multimodal part of the LLM page is still four bullets. O7 reaches 3 on the NLP page. O8 stays at 2 from LLM chapter 9. Machine Learning does not teach group fairness or TreeSHAP.

## Out of scope

`projects/` is out of scope. Capstone subjects are out of scope. Exams are out of scope. Official assessment rules are out of scope. New SynapseS codes and new UE codes are out of scope. This report does not invent a course code. It does not add a project subject. It does not change how a page says it is graded.
