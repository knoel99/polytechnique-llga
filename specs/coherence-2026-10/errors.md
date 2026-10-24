# LLGA notes: cross-page consistency and high-severity errors

Lens: (1) contradictions between pages (facts about the same official course, different statements of the same result, a page describing another module's content wrongly); (2) verification of every error rated **high** in `the per-course reader records`. Inputs: the 49 records, `index.html` (curriculum tree, `data-p` route tags, programme table), the `.qmd` sources, `tools/cross_refs.py` (all 468 chapter-level cross-references were listed and the suspicious ones opened), and numerical re-runs of the disputed code. Read-only work. Finding ids (ER-xx) match the structured findings returned with this file.

Per-page low and medium errors already in the records are **not** re-listed. Where a cross-page item is already recorded on one page, it is cited only to say which *other* page must change with it. Overlaps with the sibling analyses are flagged: `prerequisites.md` (PR-xx) and `redundancy-notation.md` (C-xx). For example, the CFG weight convention (Advanced DL vs Multimodal/Control) is C3 and is not repeated here.

## Findings index

| Id | Severity | Finding |
|---|---|---|
| ER-H01 | high | Prob/Monte Carlo Ex. 2: the triangle walk is called periodic (period 2). It is aperiodic. **Confirmed** |
| ER-H02 | high | Prob/Monte Carlo ch. 9: the MALA acceptance ratio is reversed, giving a stationary variance of 0.40 instead of 1. **Confirmed (re-run)** |
| ER-H03 | high | SLT Cor. 4.2(i): "finite VC ⇒ universally consistent" is false. **Confirmed** |
| ER-H04 | high | Video games ch. 4.2: the boids separation term attracts instead of repelling, and is not proximity-weighted. **Confirmed** |
| ER-H05 | high | Social media Lab 3: `[:, 1]` picks the Perron vector, so accuracy is 0.534 instead of 1.0. **Confirmed (re-run)** |
| ER-H06 | high | Image Synthesis Ex. 3.4: wrong sign of E_ca, and the inside pixel (2,2) is declared outside. **Confirmed** |
| ER-H07 | high | Optimal Transport ch. 6 lab: `repair_1d` scrambles individuals and crashes on 2-D input. **Confirmed (re-run)** |
| ER-H08 | high | Advanced GNN ch. 3: over-squashing is tied to λ_max instead of the spectral gap/Cheeger constant, and the error spreads to Ex. 6 and §7.3. **Confirmed** |
| ER-H09 | high | Control in GenAI Thm 2.2: "masking = exact conditioning" is false. GGM Prop 3.3 says "≈", so the two pages contradict each other. **Confirmed** |
| ER-H10 | high | DL P2 Ex. 1: 6ND for GPT-2 small on 3B tokens is 2.2×10^18 FLOPs, not 10^21. **Confirmed** |
| ER-H11 | high | Optimization for AI Prop 1.2 (⇒) proof is wrong and "proves" ∂F(θ*) = {0}. **Confirmed** |
| ER-X01 | high | Deep Learning status: "mandatory gateway" (DL P1), "rereads the P1 course" (DL P2) and DL1-only prerequisites (Graph ML, NLP, RL) contradict the home rule "required once, P1 or P2" and the AI-systems route |
| ER-X02 | medium | 14 pages carry a position badge that contradicts their home route tag (`data-p`) |
| ER-X03 | medium | Status of off-list and slot-TBC courses differs between pages (CV-applications is "mandatory", "slot TBC", "notes kept for reference" and route-preselected at once) |
| ER-X04 | medium | Self-attention is "permutation-invariant" in Deep Learning P1 (three places) but "permutation-equivariant (proved)" in Advanced DL |
| ER-X05 | medium | LoRA / distillation / in-context learning: pages disagree on whether the M2 LLM course teaches them. It does not |
| ER-X06 | medium | Two M2 pages repeat the same misdescriptions of GraphAF and DiGress and cite each other, so both must be fixed together |
| ER-X07 | medium | "Phantom content": about 45 pointers credit a module with a topic it does not teach. 4 are new here, the rest are recorded. Grouped by target module |
| ER-X08 | low | Universal approximation: DL P2 states the Leshno theorem and says DL P1 "gives the full proof". DL P1 gives a sketch of Cybenko's narrower theorem |
| ER-X09 | low | Same quantity, different value on two pages (recorded on one side only): scaling-law attribution, modularity resolution limit, distillation ratio, Nettack, Chinchilla token count |
| ER-X10 | low | Home page: internal statements contradict the pages (level-1 refreshers, "P2 courses assume one DL course", route preselection outside choice groups) |

---

## Part A — Verification of the 11 high-severity errors

All 11 are **confirmed**. Each entry gives the exact text, the check performed and the corrected statement.

### ER-H01 — Probability Theory for ML, Exercises, Ex. 2 "Walk on the triangle" (`m1p1-probability-monte-carlo`, lines 1347–1349)

> "Show that the chain is irreducible but periodic (period 2) …"
> *Solution.* "Complete graph without loops: connected, hence irreducible; one returns to the starting point in an *even* number of steps (each step changes parity): period 2. … The lazy version is aperiodic (the introduced loops "break" the gcd)"

**Check.** From A, A→B→A takes 2 steps and A→B→C→A takes 3, so gcd(2, 3) = 1. The transition matrix P = (J − I)/2 has eigenvalues 1, −1/2, −1/2 and no eigenvalue −1. "Each step changes parity" is meaningless on an odd cycle. **Confirmed.**

**Corrected statement.** "The walk on the triangle (K₃ without loops) is irreducible **and aperiodic**: returns are possible in 2 and in 3 steps, and gcd(2,3) = 1. P = (J − I)/2 is doubly stochastic, with spectrum {1, −1/2, −1/2}. The law therefore converges to the uniform distribution in total variation at rate (1/2)ⁿ without any laziness. The lazy chain (I + P)/2 has spectrum {1, 1/4, 1/4} and converges faster. For a period-2 example, use the 4-cycle (or any bipartite graph): there returns occur only at even times, and only the lazy version converges." The statement and solution of Ex. 2 are both to be rewritten on this basis.

### ER-H02 — Probability Theory for ML, ch. 9, MALA code (`m1p1-probability-monte-carlo`, lines 1287–1299)

> `q = lambda a, b: -(b - a + gamma*dU(a))**2 / (4*gamma)` … `loga = U(x) - U(y) + q(x, y) - q(y, x)` … `print(f"MALA gamma=0.5 : var {mala(0.5).var():.4f} (exact 1)")`

**Check.** `q(a, b)` is the log-density of proposing b from a. The Metropolis–Hastings log-ratio is log π(y) + log q(y→x) − log π(x) − log q(x→y) = U(x) − U(y) + q(y, x) − q(x, y). The code reverses the proposal terms. Re-run with the page's code (rng seed 0, n = 200 000, γ = 0.5): stationary variance **0.398** as written, **0.998** with the corrected line. **Confirmed.** As written, the code silently contradicts the claim two lines above it that MALA "remov[es] the bias exactly".

**Corrected line.** `loga = U(x) - U(y) + q(y, x) - q(x, y)   # log[π(y) q(y→x)] − log[π(x) q(x→y)]`

### ER-H03 — Statistical Learning Theory, ch. 4, Corollary 4.2 (i) (`m1p1-statistical-learning-theory`, line 548)

> "(i) every class with finite VC dimension is **universally consistent** (Def. 1.3);"

with Def. 1.3 (line 265): "**universally consistent** if L(h_n) → inf_h L(h) = L* in probability for every distribution P (the minimum over all measurable functions …)".

**Check.** The bound just above the corollary gives L(ĥ) ≤ L(h*_H) + 4ε_n(δ), which controls the **estimation** error only. The approximation error inf_H L − L* does not vanish for a fixed class: take thresholds on ℝ with a Bayes rule that is an interval. The page itself states this trade-off after Prop. 1.2. **Confirmed.**

**Corrected statement.** "(i) ERM over a class of finite VC dimension d is **consistent relative to H**, uniformly over distributions: L(ĥ) − inf_H L ≤ 4ε_n(δ) = Õ(√(d/n)) → 0. It is universally consistent in the sense of Def. 1.3 only if inf_H L = L* for every P, which no fixed finite-VC class achieves. Universal consistency needs a growing sieve, H₁ ⊂ H₂ ⊂ … with ∪H_k dense, chosen by SRM with d_n → ∞ and d_n log n / n → 0 (ch. 7)."

### ER-H04 — Real-time AI in Video Games, ch. 4.2, boids separation (`m1p2-realtime-ai-videogames`, lines 482–486)

> "s_sep = −Σ_{j∈N(i)} (p_i − p_j)/‖p_i − p_j‖ — move away from neighbors that are too close (weighted by proximity)"

**Check.** p_i − p_j points from j to i, that is, away from the neighbour. The leading minus sign makes the force point **toward** the neighbours, which is attraction. Each term is a unit vector, so no proximity weighting is present. **Confirmed.**

**Corrected statement.** "s_sep = Σ_{j∈N(i)} (p_i − p_j)/‖p_i − p_j‖² — a repulsion away from each close neighbour, with magnitude 1/distance. Variants use 1/d² or restrict the sum to a smaller separation radius."

### ER-H05 — Social Media: Probabilistic Models, ch. 8, Lab 3 (`m1p2-social-media-probabilistic`, line 905)

> `v2 = eigsh(A, k=2, which="LA")[1][:, 1]              # 2nd eigenvector` … `# expected ~ 1.0`

**Check.** `scipy.sparse.linalg.eigsh` returns eigenpairs in ascending order. The page's exact SBM (seed 3) gives eigenvalues [41.32, 60.87], so column 1 is the Perron vector. Re-run: accuracy **0.534** with `[:, 1]` and **1.0** with `[:, 0]`. **Confirmed.**

**Corrected code.** `w, V = eigsh(A, k=2, which="LA"); v2 = V[:, np.argsort(w)[-2]]   # second-largest eigenpair`

### ER-H06 — Image Synthesis, ch. 3, Example 3.4 (`m1p2-image-synthesis`, lines 367–383)

> "E_{ca}(p) = 3(1 − p_x)." … "4. The pixel (2, 2): E_ab = 4, E_bc = 1, E_ca = −3 — mixed signs, outside."

**Check.** With the page's Theorem 3.2, E_ca(p) = (a_x − c_x)(p_y − c_y) − (a_y − c_y)(p_x − c_x). For a = (1,1), b = (5,1), c = (1,4) this is 0 − (−3)(p_x − 1) = **3(p_x − 1)**. At (2,2): E_ab = 4, E_bc = −4·1 − 3·(2 − 5) = **5** (not 1), and E_ca = **3**. All three are positive, so the pixel is **inside**: the hypotenuse crosses y = 2 at x ≈ 3.67. With the page's sign, E_ca(b) = −12 while E_ab(c) = E_bc(a) = 12, so the same-sign test would reject every interior pixel. Ex. 7(a) rasterizes this triangle and inherits the error. **Confirmed.**

**Corrected text.** "E_ca(p) = 3(p_x − 1)." "4. The pixel (2, 2): E_ab = 4, E_bc = 5, E_ca = 3 — same sign, inside; barycentrics (λ_a, λ_b, λ_c) = (5/12, 3/12, 4/12)." Step 3 for (1, 2) is unchanged (E_ca = 0, so λ_b = 0). The incremental rule of Theorem 3.2, recorded as a medium error, must be fixed in the same edit: E_ab(p + (1,0)) = E_ab(p) **−** (b_y − a_y), which is what the proof's gradient (−(b_y − a_y), b_x − a_x) already says.

### ER-H07 — Optimal Transport and Fairness, ch. 6, guided lab `repair_1d` (`m1p2-optimal-transport`)

> `xR[s == sv] = np.interp(np.argsort(np.argsort(x[s == sv])), ranks, rep)[np.argsort(idx)]` … docstring "Partial quantile repair, feature by feature (th. 6.2)" … called as `repair_1d(X_num, S, lam)`.

**Check (re-run).** On a 1-D test vector, λ = 0 should return x unchanged. It returns values shifted by up to **2.55**: the trailing `[np.argsort(idx)]` permutes values that are already in the original order, so each individual receives another individual's value. On a 2-D `X_num`, `np.interp` raises `ValueError: object too deep for desired array`. The barycenter is an unweighted `np.mean`, whereas Th. 6.2 weights the group quantiles by p_s. **Confirmed.**

**Corrected code** (tested: λ = 0 returns X exactly; λ = 1 equalizes the group marginals):

```python
def repair_1d(x, s, lam):
    """Partial quantile repair of one feature (th. 6.2): x -> (1-lam) x + lam Q_bar(F_s(x))."""
    xR, groups = x.astype(float).copy(), np.unique(s)
    p = {g: np.mean(s == g) for g in groups}                 # group weights p_s
    u = np.linspace(0, 1, 101)
    bary = sum(p[g] * np.quantile(x[s == g], u) for g in groups)  # weighted barycentric quantile
    for g in groups:
        xg = x[s == g]
        ug = (np.argsort(np.argsort(xg)) + 0.5) / len(xg)   # within-group ranks in (0, 1)
        xR[s == g] = (1 - lam) * xg + lam * np.interp(ug, u, bary)
    return xR

def repair(X, s, lam):                                       # feature by feature
    return np.column_stack([repair_1d(X[:, j], s, lam) for j in range(X.shape[1])])
```

### ER-H08 — Advanced GNN, ch. 3 over-squashing (`m2-advanced-gnn`, lines 285–343, 593, 720–722)

> Def. 3.1 "Over-squashing (Alon & Yahav, 2021) — formal definition via Jacobians … ‖∂h_v^{(L)}/∂h_u^{(0)}‖ ≤ c (f r(λ_max))^{−d(u,v)} … the *radius of convergence* r(λ_max) …"
> Prop. 3.2 "By Cheeger (inverted for the top of the spectrum, Tanner's bound for λ_max), a weak conductance forces a large λ_max … *topological bottleneck ⇔ poor spectral conditioning*."
> SDRF: "Effect: … λ_max drops, the bound of Definition 3.1 improves." DIGL note: "both target r(λ_max)". Ex. 6: "plot λ_max before/after rewiring … after DIGL, λ_max drops". §7.3: "certificates tied to λ_max of ch. 3".

**Check.** Cheeger's inequality for the normalized Laplacian is λ₂/2 ≤ h_G ≤ √(2λ₂). A bottleneck (small Cheeger constant) is therefore a **small spectral gap λ₂**. λ_max ≤ 2 measures closeness to bipartiteness, not bottlenecks. Topping et al. (ICLR 2022) give the sensitivity bound |∂h_v^{(r+1)}/∂x_u| ≤ (αβ)^{r+1}(Â^{r+1})_{vu} and link over-squashing to negative (Balanced Forman) curvature. The Jacobian formalization is theirs, not Alon & Yahav's (who coined the term). "r(λ_max)" and the "radius of convergence" bound appear nowhere in the literature. The Chebyshev argument also fails: ChebNet rescales the spectrum into [−1, 1], where the T_k are bounded by 1 and cannot "diverge". **Confirmed.**

**Corrected statements.**
- Def. 3.1: "(Topping et al., 2022) For an MPNN with ‖∇φ‖ ≤ α and ‖∇ψ‖ ≤ β, |∂h_v^{(r+1)}/∂x_u| ≤ (αβ)^{r+1}(Â^{r+1})_{vu}. Over-squashing is the regime where this sensitivity is exponentially small for d(u, v) = r + 1, because few paths carry the information from u to v. Alon & Yahav (2021) named the phenomenon."
- Prop. 3.2: "By Cheeger's inequality λ₂/2 ≤ h_G ≤ √(2λ₂), a topological bottleneck (small h_G) is equivalent to a small spectral gap λ₂. Rewiring aims to raise h_G and λ₂ (SDRF: curvature-based; FoSR and related methods: explicit spectral-gap maximization)."
- SDRF: rename it **Stochastic Discrete Ricci Flow** (recorded medium) and state its effect as "the most negative curvatures rise, and λ₂ / h_G typically increase".
- DIGL note: "both aim to widen the bottleneck (raise λ₂)".
- Ex. 6: "plot λ₂ (or an effective-resistance / Cheeger estimate) before and after rewiring; λ₂ should increase."
- §7.3: drop "tied to λ_max of ch. 3". Spectral certificates bound the propagation operator's norm or Lipschitz constant, which is a different quantity.

### ER-H09 — Control in Generative AI, Theorem 2.2 (`m2-control-generative-ai`, lines 242–264), with GGM Prop 3.3 (`m2-graph-generative-models`, lines 343–360)

> "Theorem 2.2 — The mask is an exact conditioning (renormalization) … If at each step one *masks* the tokens that make S unreachable, the effective law is exactly p̃_θ(y|x) = p_θ(y|x) 1[y∈S] / Σ_{y'∈S} p_θ(y'|x) = p_θ(y | x, y ∈ S)." Proof, step 3: "The normalization factor telescopes from step to step …" Line 264: "This is the analysis made in ch. 3 of the Graph Generative Models module for valences". Thm 3.3: "by induction over the steps (theorem 2.2)". Thm 8.1(1): "This is *word for word* theorem 2.2".

**Check.** Local renormalization gives p̃(y) = Π_t p_θ(y_t | y_<t) / Z_t(y_<t), and the per-step allowed mass Z_t depends on the prefix, so nothing telescopes. Counterexample (checked by hand): vocabulary {a, b}, length 2, p(a) = p(b) = ½, p(a|a) = 0.1, p(b|a) = 0.9, p(·|b) uniform, S = {aa, ba, bb}. Masking gives p̃(aa) = 0.5, while p(aa | S) = 0.05/0.55 ≈ 0.09. **Confirmed.**

**Cross-page contradiction.** GGM Prop 3.3, which Control cites as "the analysis", only claims the approximation "p̃_θ ≈ p_⋆(·|𝓛)" and states it for one decision. The two pages therefore make different claims about the same mechanism, and each cites the other ("The same analysis holds for all the decoding masks of the Control in Generative AI module (ch. 3)").

**Corrected statement (both pages).** "Proposition (masking guarantees validity, not exact conditioning). Masking at each step the tokens after which S is unreachable, then renormalizing, gives a law p̃ with supp p̃ ⊆ S (validity by construction), and p̃(y|x) = Π_t p_θ(y_t | y_<t, x) / Z_t(y_<t). The exact conditional reweights each allowed token by its future feasibility: p_θ(y_t | y_<t, x, S) ∝ p_θ(y_t | y_<t, x) · p_θ(S | y_≤t, x). Masking equals it only when p_θ(S | y_<t v, x) is the same for every allowed v. In general it distorts the conditional (counterexample above). Exact conditioning requires these lookahead weights (SMC, grammar-aligned decoding) or rejection (Prop. 2.3). Bound: if the masked mass is at most ε at every step, then (1 − ε)^T ≤ p̃(y)/p_θ(y | S) ≤ (1 − ε)^{−T}." Thm 3.3 and Thm 8.1(1) should cite only the validity part. In GGM Prop 3.3, keep "≈" and add the same per-sequence caveat.

### ER-H10 — Deep Learning (P2 variant), Exercises, Ex. 1 (`m1p2-deep-learning-p2`, line 1459)

> "verify theorem 1.3 on a GPT-2 small (N ≈ 124M …): compute C for D = 3B tokens … *Expected solution*: 6ND ≈ 2.2×10^21 FLOPs."

**Check.** 6 × 1.24×10⁸ × 3×10⁹ = 2.23×10¹⁸. The stated answer is 1000× too large. **Confirmed.** The page's other 6ND figures (7B case: 4.0×10²² FLOPs, ≈ 79 000 GPU·h; Example 1.6) are correct.

**Corrected text.** "*Expected solution*: 6ND ≈ 6 × 1.24×10⁸ × 3×10⁹ ≈ 2.2×10¹⁸ FLOPs (about 4.4 A100-hours at 45 % MFU)."

### ER-H11 — Optimization for AI, ch. 1, Proposition 1.2, proof of (⇒) (`m1p2-optimization-ai`)

> "the rate of increase … is ≥ 0, which is exactly ⟨v, θ − θ*⟩ ≥ 0 for every v ∈ ∂F(θ*) and every θ — taking θ = θ* + v, it follows that ‖v‖² ≤ 0."

**Check.** The one-sided directional derivative is F′(θ*; d) = max_{v∈∂F(θ*)} ⟨v, d⟩, not a statement about every v. With θ = θ* + v one gets ⟨v, v⟩ = ‖v‖² ≥ 0, not ≤ 0. The argument would "prove" ∂F(θ*) = {0}, which fails for |θ| at 0: the page's own Def. 1.3 example gives ∂|·|(0) = [−1, 1]. **Confirmed.**

**Corrected proof.** "(⇒) If θ* minimizes F, then for every θ, F(θ) ≥ F(θ*) = F(θ*) + ⟨0, θ − θ*⟩, which is exactly 0 ∈ ∂F(θ*) by Definition 1.3." Prop. 1.2 uses Def. 1.3 before stating it, so swap their order or add a forward reference.

---

## Part B — Cross-page contradictions

### ER-X01 (high) — The status of Deep Learning differs from page to page

Root cause shared with PR-01/PR-02. Here the issue is the **status wording**, which contradicts the official rule.

- Home tree: "Deep Learning — required once, here or in P2" and "Deep Learning (P2 variant) — the 'DL once in P1 or P2' option". AI-systems route tooltip: "DL via the P2 variant". Home text: "Period 2 courses assume Machine Learning and one Deep Learning course".
- `m1p1-deep-learning` line 64: badge "[Recommended — LLGA track]". Line 132: "Downstream, this module is the **mandatory gateway** to the whole 'large models' part of the program". The page never mentions the P2 variant or the once-rule.
- `m1p2-deep-learning-p2` line 71: "The module **rereads the core of the P1 Deep Learning course** through the lens of cost". Line 185: "Reminders — the P1 Deep Learning module, in eight points". Audience: "a deep learning engineer who already trains models".
- The mandatory P2 pages name only DL P1 as a prerequisite: Graph ML line 120, NLP line 107, RL line 116. Only 3 pages on the site (Optimization for AI, Responsible AI, MLOps) link `m1p2-deep-learning-p2` at all.

For an AI-systems-route student, who takes no DL in P1, every page says something different: DL is a mandatory gateway they skipped, the DL they take assumes the DL they skipped, and the three mandatory P2 courses list a course they never take.

**Fix.**
- DL P1: replace "mandatory gateway" with "one of the two ways to satisfy the 'Deep Learning once' rule (the other is the P2 variant)", and add a link to the P2 variant.
- DL P2: replace "rereads the P1 course" with "covers the P1 foundations in cost-oriented form". Its ch. 0 eight-point recap must then *teach*, not *recall*, attention and the VAE/GAN basics, at about 1 page each (or name them as self-study), as PR-01 proposes.
- Graph ML, NLP, RL prerequisites: "Deep Learning (P1, or the P2 variant taken in parallel: read its ch. 0 first)".
- Home: "Period 2 courses assume Machine Learning and Deep Learning (P1), or take DL P2 in parallel".

### ER-X02 (medium) — The position badge on 14 pages contradicts the home route tag

The site has no official "recommended track": the wiki only defines Mandatory / Choose-N, and the home page calls routes "guidance, not a rule". Yet pages carry "Recommended — LLGA track" or "Outside recommended track" badges that disagree with the home `data-p` tags.

| Page | Page badge | Home `data-p` |
|---|---|---|
| m1p1-tda | Outside recommended track | gllm |
| m1p1-computer-vision | Outside the recommended track | sys |
| m1p1-shapes | Outside recommended track | sys |
| m1p2-optimal-transport | **Recommended — LLGA track** | "" (no route) |
| m1p2-deep-learning-p2 | Outside recommended track | sys |
| m1p2-computer-vision-applications | Outside the recommended track | sys |
| m1p2-realtime-ai-videogames | Outside recommended track | sys |
| m2-control-generative-ai | Outside recommended track | gllm |
| m2-graph-generative-models | Outside the recommended track | gllm |
| m2-advanced-topics-llms | Outside the recommended track | gllm |
| m2-speech-technology | Outside the recommended track | sys |
| m2-mlops-llm-engineering | Outside recommended track | gllm sys |
| m2-security-robustness | Outside the recommended track | gllm sys |
| m2-explainability-security-privacy-llms | Outside the recommended track | gllm sys |

These pages agree with home: DL P1, Signal Processing, Emerging ML and Multimodal ("Recommended", each on one route); Computer Animation, Optimization for AI, Advanced DL, Image Synthesis, Privacy & UQ and Boosting ("Outside", no route). Advanced GNN has no position badge. Nine of the 14 mismatches are recorded one by one as low errors (TDA, CV, Shapes, Real-time AI, Control, GGM, Advanced topics, Explainability, Security). The other five are not: Optimal Transport, DL P2, CV-applications, MLOps and Speech. The records also flag the "Recommended" wording on Signal Processing and Emerging ML.

**Fix (one rule for all pages).** Generate the badge from `data-p`: "Graph × LLM route" / "AI-systems route" / "both routes" / "not preselected by a route". Drop the words "recommended track" everywhere, including the prose of each "Where this course fits" section.

### ER-X03 (medium) — Status of off-list and slot-TBC courses

- **CV: From Fundamentals to Applications.** The page (line 101) says: "Module of period 2 of M1 (36 h, 4.5 ECTS), **mandatory according to the MSc&T brochure**", repeated at lines 217 and 823. The home tree lists it under "Slot TBC announced, not yet in the wiki lists", the home table files it under "notes kept for reference: courses not in the 2026–27 LLGA lists", and the sys route preselects it, although the home says routes "preselect inside the official choice groups only — they never override Mandatory items". That is four statuses for one course. **New.** Fix: "Announced in the MSc&T brochure; not in the 2026–27 LLGA lists; covered here for reference". Drop "mandatory" and decide whether a slot-TBC item can carry a route tag.
- Pages whose status is already recorded as an error (fix with the same wording): Startup ("Year 1 · Period 2 · mandatory" vs "not in the 2026–27 list"), Statistics in Action ("[P2 option]"), Probability/Monte Carlo ("P1 elective", "4.5 ECTS (value of the LLGA track)"), Real-time AI ("an option of the period 2 elective group"), Machine Learning → SLT ("P1 option"), RL → Probability/MC (prerequisite), Strategy/Marketing → Startup, Responsible AI ("the other P2 courses"), Ethics → "responsible modules in P2", Languages/Sports (8 ECTS counted per page instead of shared).
- **Fix.** Use one status vocabulary on every page and on the home page, taken from the home tree: Mandatory · Choose-3 (P1) · Choose-1 (P2) · DL-once · Slot TBC (announced) · Notes kept for reference · Off-curriculum support.

### ER-X04 (medium) — Self-attention: "invariant" on one page, "equivariant (proved)" on another

- `m1p1-deep-learning` line 1105 (code comment, 6.4): "# Position: the transformer is permutation-invariant". Line 1485 (ch. 10, SHAKE-GNN note): "Chapter 6 showed that a transformer needs a positional encoding because attention is permutation-invariant". Ex. 4 asks for the same claim.
- `m1p2-advanced-deep-learning` Prop. 4.4: "Self-attention without positions is permutation-**equivariant** (proved)".

The record for DL P1 covers Ex. 4 and the 6.4 comment, but not line 1485. Graph ML and the LLM page build on the "transformer = GNN on a complete graph" reading, which needs equivariance. **Fix.** In all three DL P1 places, write: "without positions, self-attention is permutation-equivariant: permuting the tokens permutes the outputs. Invariance only comes after a symmetric pooling." DL P1 Ex. 4 should cite Advanced DL Prop. 4.4 as the proof.

### ER-X05 (medium) — Pages disagree on whether the M2 LLM course teaches LoRA, distillation and in-context learning

- `m1p1-deep-learning` line 1217: "The generalizations (QLoRA …) are covered in the LLMs module (M2)." **New.**
- `m2-large-language-models` line 386: "(ch. 6: distillation, LoRA)". Line 750: "Small Language Models & distillation … (ch. 6)". Recorded medium.
- `m1p2-advanced-deep-learning` line 1022: "MoE at inference, LLM quantization, LLM distillation — **M2 Large Language Models module, chapters 2, 6 and 8**". **New**: no LLM chapter teaches distillation.
- `m2-mlops-llm-engineering` line 685: "LoRA (Hu et al., ICLR 2022), **which the LLMs module does not cover**". This is correct and contradicts the three pointers above. MLOps ch. 4 also promises "distillation arbitrage" that it does not deliver (recorded).
- In-context learning: Boosting (line 531) and Explainability (Ex. 2.2) send readers to the LLM page, which never treats it (recorded low on each; PR-04).

The mandatory O3 course is the one that should hold these topics. **Fix.** Add about 1.5 pages to LLM ch. 4 (post-training): LoRA/QLoRA with the parameter count, logit distillation, and in-context learning / prompting basics (zero-/few-shot, ICL as a conditional law). That fits as self-study (≈ 2 h) if session 4 is full. Then make the four pointers consistent and keep MLOps ch. 7 as the operations view. This overlaps PR-04 and PR-10. The addition here is that the pages *contradict each other*, so all five pointers must change in one edit.

### ER-X06 (medium) — Two M2 pages repeat the same misdescriptions and cite each other

- **GraphAF property optimization.** Control Thm 8.1(2) says "one moves z_t along ∇_{z_t} Q(G_t) during generation … (the graph module ch. 4 derives it)", and GGM Thm 4.3 item 3 / Ex. 6 says the same. In Shi et al. (ICLR 2020) the optimization is RL fine-tuning (PPO). Both pages are recorded medium, but the Control text cites GGM as its source, so fixing only one side leaves a broken justification.
- **DiGress guidance.** Control Thm 8.1(3) ("classifier-free: thm 7.1 transposed") and GGM ch. 5 Thm 5.4 / ch. 7 Def 7.1 / ch. 10 (CFG with a masked descriptor) both describe classifier-free guidance. Vignac et al. (ICLR 2023) use regressor (classifier) guidance on noisy graphs.
- **Masking.** See ER-H09: Control Thm 2.2 and GGM Prop 3.3 cite each other with different claims.
- **Sequencing.** Control (Y2 P1) "rereads chapters 3, 4 and 5" of GGM (Y2 P2), and GGM ch. 0 presents Control ch. 8 as building on it (recorded; PR-05).

**Fix.** One joint edit of Control ch. 2 and ch. 8 and GGM ch. 3, 4, 5, 7 and 10. Make GGM the reference for model facts (GraphAF = RL fine-tuning; DiGress = regressor guidance, with CFG presented as the later alternative used in follow-up work). Control ch. 8 then summarizes GGM. Because GGM comes later in the year, Control's summary must be self-contained (about ½ page per model).

### ER-X07 (medium) — "Phantom content": pages credit a module with topics it does not teach

`tools/cross_refs.py` lists 468 chapter-level cross-references, and the records add the module-level ones. About 45 pointers attribute to a module content it does not contain. Grouped by **target**, with ★ marking pointers found here and not in the records:

| Target module (as cited) | Topics wrongly attributed to it (citing page) |
|---|---|
| Machine Learning (P1, mandatory) | neural nets / backprop / RNN (Computer Animation, Image Synthesis); metric spaces, single linkage, DBSCAN, mean-shift (TDA); adversarial defences and subgroup evaluation (CV-applications); causal forests (Statistics in Action); MMD (MLOps); OBS/OBD (Advanced topics); multiple testing (Real-time AI) |
| Refresher in Statistics | Hawkes processes, coupon collector (Social media); martingales (GGM); KS test (MLOps); concentration/Hoeffding chapter, rank tests (Real-time AI) |
| Refresher in CS | Markov chains (NLP); spatial data structures (Computer Animation); Blelloch scan (Advanced topics) |
| Signal Processing | Kalman filter (CV-applications); audio watermarking (Control ×2); memory hierarchy (LLM) |
| Deep Learning (P1) | ★ "the role of weight norms in controlling Lipschitzness", ch. 3 (SLT line 756: ch. 3 has weight decay but no Lipschitz/margin argument); ★ "full proof" of the Leshno theorem, ch. 1.2 (DL P2, see ER-X08); graph morphology, ch. 10 (DL P1 itself) |
| Multimodal GenAI | Langevin dynamics, ch. 9 (Probability/MC); stereo cost volume, captioner hallucination, ch. 8 (CV-applications); SDF/genus (Shapes); AtlasNet (Image Synthesis) |
| Large Language Models (M2) | ★ QLoRA (DL P1); ★ LLM distillation, ch. 2/6/8 (Advanced DL); LoRA/distillation, ch. 6 (LLM itself); in-context learning (Boosting, Explainability) — see ER-X05 |
| Graph ML | cyclomatic rank and clique complexes, ch. 0 (TDA); Deep Sets, ch. 5 (TDA); scene graphs (CV-applications) |
| RL | AlphaGo MCTS, ch. 5–6, and MARL taxonomy, ch. 7 (Real-time AI) |
| NLP | n-gram language model, ch. 2 (Speech); learning to rank, ch. 2 (Advanced topics) |
| Image Synthesis | diffusion (Boosting) |
| Optimal Transport | importance sampling (Image Synthesis) |
| Geometric DL / Advanced GNN | MC dropout and ensembles on graphs (Privacy & UQ); animation (Real-time AI → Geometric DL) |
| Emerging ML | extreme classification (Machine Learning); temporal split (Advanced GNN) |
| (any page) | MAML (Advanced GNN) |

**Fix rule.** If the target is mandatory and the topic is in its scope and short, add it to the target: LLM (ER-X05), or Machine Learning ch. 7 (one paragraph on hierarchical/density clustering, which TDA ch. 6 and Mapper rely on). Otherwise retarget the pointer to where the content really is: e.g. Real-time AI → Machine Learning ch. 0 for Hoeffding (stated there, line 215), Speech → NLP ch. 6 (HMM/Viterbi), CV-applications → Advanced DL §4.5 for attacks, Control → Speech ch. 9 for audio watermarking. If neither applies, delete the pointer. A cheap guard against new phantom pointers: run `tools/cross_refs.py` before each publish and check the topic word against the target chapter text.

### ER-X08 (low) — The universal approximation theorem is stated two ways, and the claimed proof does not exist

- DL P1 Thm 1.5 (Cybenko/Hornik): σ continuous and "discriminatory" ("the sigmoid and tanh qualify"). The proof is labelled "Guided sketch", and Cybenko's technical lemma is asserted, not proved.
- DL P2 Thm 0.1 (Leshno–Lin–Pinkus–Schocken): σ continuous and **not a polynomial**, which covers ReLU. Line 262 says: "The P1 Deep Learning module (ch. 1.2) gives **the full proof** of the theorem."

DL P1 neither proves Cybenko's lemma nor covers non-sigmoidal σ. **Fix.** DL P2: "DL P1 (ch. 1.2) sketches the proof for sigmoidal σ (Cybenko). The non-polynomial case (Leshno et al. 1993) is admitted here. Prop. 0.2 proves the 1-D ReLU case." Optionally, DL P1 can cite Leshno in one sentence so that ReLU networks are covered. The faulty "discriminatory" gloss in DL P1 is recorded separately.

### ER-X09 (low) — Same quantity, different value on two pages

These are recorded on **one** page only. They are listed so that the other page is checked in the same edit.

| Object | Page A | Page B | Correct / action |
|---|---|---|---|
| Parametric scaling law E + A/N^α + B/D^β | Advanced DL Def 9.1 attributes it to Kaplan 2020 | Emerging ML Thm 7.1 and LLM §3.2 attribute it to Hoffmann 2022 (Chinchilla) | Hoffmann. Fix Advanced DL |
| Modularity resolution limit | Graph ML: ~√(2m) edges | Social media ch. 7: ~√(m/2) (Fortunato–Barthélemy) | √(m/2)-type bound per F–B. Align Graph ML |
| Distillation compression | Responsible AI ch. 3: "10–50× fewer parameters" | DL P2 prop. 5.2 (citing it): "10–100×" | Pick one range with a source |
| Nettack | Advanced GNN §7.1: "gradient attack" on a one-layer surrogate | Security & Robustness Case 9.2: greedy search on a linearized two-layer surrogate | Security is right. Fix Advanced GNN |
| Chinchilla tokens | DL P2 ch. 1 note: "70B on 1.5T tokens" | DL P2 Ex. 1.6, Emerging ML, Advanced DL: 1.4T | 1.4T |

The CFG weight convention, PageRank α, discrete-diffusion transitions, spectral gap, randomized-response p, normalized Laplacian, SGNS letters, distillation weights and eigen-indexing are covered as C1–C10 in `redundancy-notation.md` and are not repeated here. Checked and **consistent** across pages: the Gaussian mechanism σ ≥ Δ₂√(2 ln(1.25/δ))/ε (Emerging ML, Privacy & UQ, Explainability), advanced composition, the DPO loss and RLHF closed form (LLM, Control), the green-list z-test (Control, Explainability), Hoeffding constants (ML, MLOps, SLT, Real-time AI), the KV-cache formula (LLM, DL P2, MLOps), the 12d² parameters per block (Advanced DL, DL P2, LLM), Bures/FID (OT, Signal Processing, Multimodal), the GCN propagator (Graph ML, Advanced GNN), GIN = 1-WL (Advanced GNN, Graph ML, GGM), GraphAF 68 %/100 % and NeVAE > 90 % (Control, GGM), and course codes, periods, hours and ECTS of every course unit mentioned on another page.

### ER-X10 (low) — Statements on the home page contradict the pages

- "the refreshers stay at level 1". Both refreshers have level-2 sessions: Refresher Statistics sessions 3–4 and Refresher CS sessions 3–4 are level 2. Fix the sentence to "levels 1–2", or relabel the sessions.
- "Period 2 courses assume Machine Learning and one Deep Learning course". See ER-X01.
- "The route buttons preselect inside the official choice groups only". Yet the sys route tags two slot-TBC items (CV-applications, Real-time AI), and both routes tag Y2 P2 announced themes, which are not choice groups. Reword to "preselect among the options and announced modules".
- CV-applications and Real-time AI sit under "Slot TBC announced" in the tree but under "notes kept for reference" in the programme table. Use one label in both places.
