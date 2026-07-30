---
abstract: |
  This paper replaces the former claim that a single projection obstruction makes the observed form of physics inevitable. Projection, recovery, autonomous descent, effective merger, stochastic reduction, locality, and physical realization are different mathematical questions and require different hypotheses. We give a typed closure map for these questions. An autonomous reduced evolution exists exactly when upper evolution preserves the fibers of the initial reduction. An effective merger prevents recovery of the prior effective state, while noninjectivity of a cross-level map prevents exact upper decoding but does not prevent representative selection. A stochastic reduced kernel requires an upper probability measure and disintegration; stationary mixing supplies a conditional correlation law but does not select Born weights. Microcausality descends only for a local upper net under fiberwise compatible compression. Fixed-point robustness, complex Hilbert structure, Born probabilities, Einstein dynamics, and entropy normalization consequently remain separate theorem targets. The result is a conditional dependency theorem for the Modal Triplet Theory corpus, not an inevitability theorem.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 22d40e2308d937ec0e4de749ec4e49ddd6c287908cf5e929b6fe0901f2f82776
paper_id: closure-and-inevitability-in-modal-triplet-theory
release_state: zenodo_released
released_version: v2
title: Conditional Closure Relations in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21652662
zenodo_record_id: 21652662
zenodo_url: "https://zenodo.org/records/21652662"
---

# Revision note for this edition

Supersedes.
Version 1, *Closure and Inevitability in Modal Triplet Theory*.

Reason.
Version 1 conflated a right section, a left decoder, autonomous descent, and reversal of effective time evolution. It then inferred probability, Hilbert structure, gravity, horizons, and entropy from that conflation.

Resolution.
Version 2 withdraws the single obstruction and replaces it with separately typed projection, measure, locality, stability, and physical realization statements.

Retained result.
Projection and admissibility remain useful organizers of the corpus, and effective descriptions can lose distinctions present in an upper description.

Remaining boundary.
Born weights, complex Hilbert structure, complete QFT reconstruction, gravitational normalization, horizon entropy, and a physical arrow of time require independent source and realization theorems.

# How to read the closure map

This paper is organized around four questions, not one obstruction. Read the symbols in the next section as a bookkeeping device for an upper process, the information retained by a reduced description, and the evolution visible after that reduction. Sections <a href="#sec:admissibility" data-reference-type="ref" data-reference="sec:admissibility">5</a>–<a href="#sec:closure-map" data-reference-type="ref" data-reference="sec:closure-map">9</a> then add the independent measure, locality, stability, and physical realization gates.

In plain language, imagine that a detailed state is compressed to a dashboard display. Choosing one detailed state compatible with a displayed value is a *representative selection*. Recovering the particular detailed state that actually produced the display is *decoding*. Predicting the next display from the current display alone is *autonomous descent*. Two different current displays later becoming the same display is an *effective merger*. A dashboard can permit one of these operations and forbid another; noninjectivity by itself does not decide all four.

The central picture is therefore a directed dependency graph. Each arrow must be justified in its own category. A set-theoretic arrow does not silently become continuous, local, probabilistic, or physical. The value of the corrected closure map is that it shows exactly where an additional source or realization theorem must enter.

# Scope: closure as a dependency map

The earlier edition proposed one “projection–admissibility obstruction” and presented several physical structures as unavoidable consequences. That central theorem is withdrawn. Its failure is a type error: choosing one preimage, recovering the actual preimage, evolving an equivalence class, and reversing an effective dynamics are not the same operation.

The corrected purpose of this paper is narrower and more useful. It records which conclusions follow from which hypotheses, and it identifies where an additional theorem is required. In this sense, *closure* means a closed logical dependency graph. It does not mean that every node in the graph has already been derived from a common axiom set.

No probability, entropy, geometry, complex scalar field, or physical time is inferred below from a bare map of sets. Whenever a result is topological, metric, measure-theoretic, or operator-algebraic, its hypotheses are stated in that category.

# Typed projection and evolution data

Let $`A`$ be an admissible upper state domain and let
``` math
\Phi_t:A\longrightarrow X_t
```
be an upper evolution. Invertibility of $`\Phi_t`$ is not required for the typing results in this section. Let
``` math
P_0:A\longrightarrow Y_0,
  \qquad
  P_t:\Phi_t(A)\longrightarrow Y_t
```
be surjective reductions onto their declared effective images, and set
``` math
T_t=P_t\circ\Phi_t:A\longrightarrow Y_t.
```
The initial effective equivalence relation is
``` math
x\sim_0x'
  \quad\Longleftrightarrow\quad
  P_0(x)=P_0(x').
```

<div class="definition">

**Definition 1** (Representative section). A representative section is a map $`S_t:Y_t\to A`$ satisfying
``` math
T_t\circ S_t=\operatorname{id}_{Y_t}.
```
It selects one compatible upper representative for each attained final effective state.

</div>

<div class="definition">

**Definition 2** (Exact upper decoder). An exact upper decoder is a map $`D_t:T_t(A)\to A`$ satisfying
``` math
D_t\circ T_t=\operatorname{id}_{A}.
```
It recovers the actual upper input, not merely a compatible representative.

</div>

<div class="definition">

**Definition 3** (Autonomous reduced evolution). An autonomous reduced evolution is a map $`F_t:Y_0\to Y_t`$ satisfying
``` math
F_t\circ P_0=P_t\circ\Phi_t.
```

</div>

<div class="definition">

**Definition 4** (Effective merger). If $`F_t`$ exists, an effective merger is a pair $`y\ne y'`$ in $`Y_0`$ for which $`F_t(y)=F_t(y')`$.

</div>

The four equations have different domains and different logical gates. They must not be used interchangeably.

# Projection, descent, and recovery

<div id="thm:typed" class="theorem">

**Theorem 5** (Typed descent and recovery). *For the data above:*

1.  *A set-theoretic representative section exists when $`T_t`$ is surjective and the relevant choice principle is available. A continuous, measurable, local, smooth, or Lipschitz section requires a theorem in that category.*

2.  *An exact upper decoder exists if and only if $`T_t`$ is injective, with the decoder defined on $`T_t(A)`$.*

3.  *An autonomous reduced evolution exists if and only if
    ``` math
    \begin{equation}
      P_0(x)=P_0(x')
      \quad\Longrightarrow\quad
      P_t(\Phi_t x)=P_t(\Phi_t x')
      \label{eq:factor}
    \end{equation}
    ```
    for every $`x,x'\in A`$. When it exists, $`F_t`$ is unique.*

4.  *If <a href="#eq:factor" data-reference-type="eqref" data-reference="eq:factor">[eq:factor]</a> holds and two distinct initial effective states merge, then no map $`E_t:Y_t\to Y_0`$ can satisfy $`E_t\circ F_t=\operatorname{id}_{Y_0}`$.*

</div>

<div class="proof">

*Proof.* The first statement is the section condition for a surjection. If $`D_tT_t=\operatorname{id}_A`$ and $`T_t(x)=T_t(x')`$, applying $`D_t`$ gives $`x=x'`$. Conversely, an injective $`T_t`$ has an inverse on its image. For the third statement, necessity follows by applying $`F_t`$ to equal initial effective states. If <a href="#eq:factor" data-reference-type="eqref" data-reference="eq:factor">[eq:factor]</a> holds, define
``` math
F_t(P_0x):=P_t(\Phi_tx).
```
The implication makes this independent of the representative, while surjectivity of $`P_0`$ gives existence and uniqueness. Finally, if $`F_t(y)=F_t(y')`$ and $`E_tF_t`$ were the identity, then applying $`E_t`$ would give $`y=y'`$, contradicting the merger assumption. ◻

</div>

<div class="corollary">

**Corollary 6** (Fiber splitting). *If there are $`x,x'\in A`$ with $`P_0(x)=P_0(x')`$ but $`P_t(\Phi_tx)\ne P_t(\Phi_tx')`$, then no autonomous reduced map $`F_t`$ exists on the declared state space $`Y_0`$.*

</div>

<div class="corollary">

**Corollary 7** (Merger and effective recovery). *An effective merger obstructs unique recovery of the prior effective state. It does not, by itself, obstruct selection of a compatible upper representative for a final state.*

</div>

<div class="example">

**Example 8** (Why noninjectivity is insufficient). The projection
``` math
r:\mathbb R^2\to\mathbb R,
  \qquad r(x,z)=x,
```
is noninjective, but $`s(x)=(x,0)`$ satisfies $`r\circ s=\operatorname{id}_{\mathbb R}`$. Thus noninjectivity rules out recovery of the actual pair $`(x,z)`$ from $`x`$; it does not rule out choosing one pair above each $`x`$.

</div>

There is a valid no-section result when the map is a reduced self-map and its image is provably too small. For example, let $`(Y,d)`$ have finite diameter $`D>0`$ and let $`G:Y\to Y`$ obey
``` math
d(Gy,Gy')\leq \kappa d(y,y')+c\varepsilon,
  \qquad 0\leq\kappa<1.
```
Then $`\operatorname{diam}G(Y)\leq\kappa D+c\varepsilon`$. If $`(1-\kappa)D>c\varepsilon`$, the map is not surjective and therefore has no section $`S:Y\to Y`$ with $`GS=\operatorname{id}_Y`$. This metric theorem does not apply to $`T_t:A\to Y_t`$ merely because $`T_t`$ is noninjective.

# Admissibility is a vector of declared gates

Let $`m_1,\ldots,m_N`$ be continuous margins and define
``` math
A_t^\delta
  =\{x:m_j(t,x)\geq\delta\text{ for every }j\}.
```
The margins may encode domain control, spectral separation, complementary damping, leakage, contraction, truncation error, section conditioning, or hyperbolicity. First exit from $`A_t^0`$ says only that at least one declared condition has failed. The failed component must be identified before a conclusion is drawn.

A scalar such as
``` math
C(t,x)=\min_j \frac{m_j(t,x)}{s_j},
  \qquad s_j>0,
```
can summarize a chosen normalized list of margins. Its value depends on the list, scales, and aggregation rule. It is therefore a useful diagnostic, not a universal invariant “coherence capacity” unless a realization proves independence from those choices.

Loss of an admissibility margin does not automatically select a successor state, create a probability law, or establish a physical singularity. One must stop the reduced description, derive continuation from the upper dynamics, or supply a typed reset or boundary law with its own consistency proof.

# Measure-dependent stochastic reduction

Projection does not create a probability measure. Let $`A,Y_0,Y_t`$ be standard Borel spaces, let $`P_0`$ be measurable, and let $`\mu`$ be a probability measure on $`A`$. Write $`\{\mu_y\}`$ for a regular conditional distribution of $`x`$ given $`P_0(x)=y`$.

<div id="thm:kernel" class="theorem">

**Theorem 9** (Conditional reduced kernel). *For every measurable $`B\subseteq Y_t`$, define
``` math
K_t(y,B)
  :=\mu_y\bigl(\{x:P_t(\Phi_tx)\in B\}\bigr).
```
Then $`K_t`$ is a Markov kernel from $`Y_0`$ to $`Y_t`$, up to $`(P_0)_\#\mu`$-null sets. If autonomous descent holds, then
``` math
K_t(y,\cdot)=\delta_{F_t(y)}
```
for almost every $`y`$.*

</div>

<div class="proof">

*Proof.* Regular conditional distributions exist on standard Borel spaces. Measurability and countable additivity pass through the measurable preimage in the definition of $`K_t`$. Under descent, $`P_t\Phi_tx=F_t(P_0x)`$ is constant on each conditional fiber, so the conditional law is a point mass. ◻

</div>

Mixing and invariance sharpen this construction without selecting its measure. Suppose now that $`P_0=P_t=P`$, that $`\Phi_t`$ preserves $`\mu`$, and put $`\nu=P_\#\mu`$. Then
``` math
\begin{equation}
 \int_C K_t(y,D)\,\nu(\mathrm dy)
 =\mu\bigl(P^{-1}(C)\cap\Phi_t^{-1}(P^{-1}(D))\bigr)
 \label{eq:mixing}
\end{equation}
```
for measurable $`C,D\subseteq Y`$. If $`\Phi_t`$ is mixing, the right-hand side tends to $`\nu(C)\nu(D)`$. The projected two-time law is therefore stationary and inherits the mixing limit. It is genuinely stochastic at time $`t`$ only where $`K_t(y,\cdot)`$ is non-Dirac. Moreover, these pairwise kernels need not satisfy the Chapman–Kolmogorov equations unless an additional lumpability or Markov theorem is proved.

Different upper measures on the same projection fibers can give different kernels. Neither fiber cardinality, invariance, nor mixing selects the Born rule. A Born-weight result must identify the physical state/measure and prove the quadratic weight functional independently.

# Locality under compatible compression

Let $`\pi:M\to Y`$ be a physical bundle and let
``` math
P=\int_Y^{\oplus}P_y\,\mathrm d\nu(y)
```
be a decomposable fiberwise projector. Suppose $`O\mapsto\mathcal A_M(\pi^{-1}O)`$ is an isotonic upper local net. Define
``` math
\mathcal A_M^P(O)
  =\{A\in\mathcal A_M(\pi^{-1}O):[A,P]=0\}
```
and
``` math
\mathcal A_Y(O)
  =\{PAP|_{\operatorname{Ran}P}:A\in\mathcal A_M^P(O)\}.
```

<div id="thm:locality" class="theorem">

**Theorem 10** (Locality descent). *The compressed net $`\mathcal A_Y`$ is isotonic. If upper observables assigned to spacelike separated base regions commute, then their compatible compressions commute. Hence microcausality descends on the $`P`$-compatible subalgebra.*

</div>

<div class="proof">

*Proof.* Upper inclusion gives compressed inclusion. For $`[A,P]=[B,P]=0`$,
``` math
[PAP,PBP]|_{\operatorname{Ran}P}
 =P[A,B]P|_{\operatorname{Ran}P},
```
which vanishes whenever the upper commutator vanishes. ◻

</div>

This theorem does not construct the upper local net, prove Lorentz covariance, or imply factorization of states. A projector nonlocal over the base, or an observable that does not preserve $`\operatorname{Ran}P`$, lies outside its scope.

# Fixed points and conditional universality

Projection equivalence classes alone do not establish universality. A useful local result comes from uniform stability. For instance, let $`G_\lambda`$ be contractions on a common complete invariant domain with constant $`\kappa<1`$, and suppose
``` math
\sup_x d(G_\lambda x,G_{\lambda'}x)\leq\eta.
```
If $`x_\lambda`$ and $`x_{\lambda'}`$ are their fixed points, then
``` math
d(x_\lambda,x_{\lambda'})
 \leq \frac{\eta}{1-\kappa}.
```
This follows by inserting and subtracting $`G_\lambda(x_{\lambda'})`$ and applying the contraction bound. Such estimates support basin-local robustness under a declared perturbation class. They do not prove that every microscopic model flows to the same physical theory.

The corrected MTT Foundation and Fixed Points sequence provide conditional instances of existence, damping, curved-projector continuation, and stability under their stated gap, domain, covariance, and contraction hypotheses. Each instance must still be connected to a selected physical realization before it becomes a physical universality statement.

# The corrected MTT closure map

The present corpus supports the following dependency statements.

Projection and autonomous descent.
Theorem <a href="#thm:typed" data-reference-type="ref" data-reference="thm:typed">5</a> supplies the exact factor-through gate. A selected MTT operator must separately prove that its evolution preserves the chosen projection fibers.

Probability and Born weights.
Theorem <a href="#thm:kernel" data-reference-type="ref" data-reference="thm:kernel">9</a> constructs a conditional reduced kernel after an upper measure is supplied. The physical measure and the Born quadratic functional are independent source targets; they are not consequences of projection multiplicity.

Complex Hilbert structure.
If a realization already acts on a complex Hilbert bundle, coherent compression can inherit that structure. Projection alone does not derive the complex field, inner product, completeness, or the physical observable algebra.

QFT locality.
Theorem <a href="#thm:locality" data-reference-type="ref" data-reference="thm:locality">10</a> preserves isotony and microcausality for a compatible compressed net. It does not by itself supply the net, state, spectrum condition, scattering theory, or renormalized dynamics.

Gravity.
The current q79 proof corpus contains a conditional composition in which one discrete physical-realization declaration $`A_{\mathrm{QG}}`$, one binary causal boundary mark $`A_{\mathrm{causal}}`$, a selected global comparison field, and a same-source metric-factorization rule give a global Lorentzian coframe and the TEGR/Einstein two-derivative bulk class. This is not a consequence of projection alone. The gravitational normalization and cosmological term remain independent open coordinates.

Irreversibility and temporal direction.
Effective merger prevents recovery of a prior effective state. A physical arrow additionally requires an oriented evolution and an asymmetric condition such as a semigroup law, a monotone functional, or boundary data. The binary causal representative does not by itself derive a thermodynamic arrow.

Horizons and entropy.
Exterior restriction can discard distinctions, but horizon entropy requires a specified state, entropy functional, dynamics, and normalization theorem. Area scaling is not a map-theoretic corollary.

Thus the corrected closure statement is conditional: several mechanisms can be composed when their interfaces and source data are proved. Their mere presence in one interpretive architecture does not collapse them into one theorem.

# Changes from Version 1

Version 2 makes the following substantive changes.

1.  It retitles the work to remove the unsupported claim of physical inevitability.

2.  It withdraws the former Projection–Admissibility Obstruction and all corollaries that depended on it alone.

3.  It replaces the old obstruction by the typed descent-and-recovery Theorem <a href="#thm:typed" data-reference-type="ref" data-reference="thm:typed">5</a>.

4.  It replaces the proposed universal scalar coherence capacity by a declared vector of admissibility margins; scalar aggregation is explicitly normalization dependent.

5.  It derives a reduced stochastic kernel only after measure and disintegration data are supplied, and distinguishes this from Born-weight selection.

6.  It states the exact compatibility hypotheses under which locality descends through compression.

7.  It records fixed-point robustness, Hilbert structure, QFT completion, gravity, temporal direction, and entropy as separate conditional branches.

8.  It updates the gravity branch to the present q79 conditional $`A_{\mathrm{QG}}+A_{\mathrm{causal}}`$ tier while retaining the open normalization boundary.

# Conclusion

Projection is a powerful structural operation, but it is not a generator of all physical law. It defines fibers, can obstruct exact recovery, and—when fiber preservation holds—supports autonomous descent. Measures and disintegration produce conditional stochastic laws. Compatible compression can preserve locality. Stability estimates can establish controlled universality. None of these conclusions licenses the others without their additional hypotheses.

The resulting MTT program is more sharply testable than the inevitability claim it replaces. For each proposed physical reconstruction, the remaining task is explicit: identify the upper object, prove descent through the selected projection, provide any required measure or boundary data, and verify the physical normalization. Conditional closure is achieved when that chain is complete and auditable.

<div class="thebibliography">

9

P. Nero, *The Projection–Admissibility Principle: Descent, Recovery, and Structural Constraints on Effective Description*, version 2, 2026.

P. Nero, *Modal Triplet Theory: Foundation*, version 7, 2026.

P. Nero, *Fixed Points I–VI*, corrected editions, 2026.

P. Nero, *q79 Selected Lorentzian Coframe and Causal Representative Closure*, technical theorem packet, 2026.

</div>
