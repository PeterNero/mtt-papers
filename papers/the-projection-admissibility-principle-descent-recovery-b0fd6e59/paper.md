---
abstract: |
  We replace the former noninvertibility obstruction by a typed theory of projection, descent, recovery, and admissibility. For an upper evolution $`\Phi_t`$, an initial reduction $`P_0`$, and a final reduction $`P_t`$, four different questions arise. A right section selects one compatible upper representative; a left decoder recovers the actual upper input; an autonomous reduced map exists exactly when upper evolution respects the initial equivalence classes; and an effective merger is noninjectivity of that reduced map. Noninjectivity of a cross-level projection does not forbid a right section. We prove the correct factor-through theorem, a valid no-right-section criterion for a genuinely contractive reduced self-map, a section-conditioning diagnostic, and locality descent for fiberwise coherent compression of a local operator net. Probability requires an upper measure and disintegration; entropy, irreversibility, and an arrow of time require additional structures. Applications to open systems, Wilsonian reduction, exterior gravity, and MTT are consequently reconstructions or conditional realizations rather than corollaries of noninjectivity alone.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: e90f981327db60b358897c2024000cc46ab24c6d073d984ae0070d5e57ee393c
paper_id: the-projection-admissibility-principle-descent-recovery-b0fd6e59
release_state: zenodo_released
released_version: v2
title: |
  The Projection–Admissibility Principle
  Descent, Recovery, and Structural Constraints on Effective Description
zenodo_doi: 10.5281/zenodo.21652659
zenodo_record_id: 21652659
zenodo_url: "https://zenodo.org/records/21652659"
---

# Revision note for this edition

Supersedes.
The original *Projection–Admissibility Principle: Structural Constraints on Effective Physical Description*.

Reason.
Noninjectivity of a cross-level projection was incorrectly used to rule out a right section and to infer several unrelated physical effects.

Resolution.
Version 2 separates right sections, left decoders, autonomous descent, and effective mergers, and replaces the obstruction claim by the correct factor-through and conditioning theorems.

Retained result.
Projection and admissibility remain useful structural organizers once every map is typed.

Remaining boundary.
Probability, entropy, irreversibility, and physical recovery require measures, dynamics, and observable-specific hypotheses.

# How to Read the Principle

A projection deliberately forgets distinctions. The central issue is not whether information was forgotten, but which later questions can still be answered from what remains. Four questions recur throughout the paper:

<div class="description">

Required equation: $`T_tS_t=\operatorname{id}`$. Failure means that some final reduced states have no admissible upper representative, or none with the requested regularity.

Required equation: $`D_tT_t=\operatorname{id}`$. Failure means that distinct upper inputs have become indistinguishable at the final reduced level.

Required equation: $`F_tP_0=P_t\Phi_t`$. Failure means that the initial reduced state omits distinctions that influence the later reduced state.

Required relation: $`F_t(y)=F_t(y')`$ for $`y\ne y'`$. Its occurrence means that distinct initial reduced states have the same final reduced image.

</div>

The equations point in different directions and therefore cannot be replaced by one slogan about invertibility.

## Object picture: what the reduced state remembers

For the projection $`P_0(x,h)=x`$, the coordinate $`h`$ is hidden. If upper evolution changes the visible coordinate by an amount depending on $`h`$, two upper states represented by the same $`x`$ can have different visible futures. Autonomous descent then fails because the reduced state has forgotten something needed for prediction. A representative section can still choose, for example, $`h=0`$; that choice does not recover the hidden value that was actually present.

This memory picture is useful across the applications. Initial system–environment correlations, eliminated ultraviolet couplings, interior boundary data, and complementary coherent modes can all act as an $`h`$-type variable. Whether they matter is decided by the factor-through condition, not by the mere fact that a projection was used.

## Argument map

Sections 2–4 type the maps and prove the descent/recovery classification. Section 5 gives the genuine diameter obstruction. Sections 6 and 7 treat stable continuation and chart boundaries. Sections 8 and 9 explain which measure and temporal data must be added for stochastic or irreversible interpretations. Section 10 proves the separate locality-descent statement. The final applications then show how the same distinctions change the interpretation of open systems, Wilsonian reduction, exterior gravity, and MTT.

# Scope and correction of the former obstruction

The previous version argued that a noninjective map cannot have a right inverse. That statement is false. A surjection may be highly noninjective and still admit a section. For example,
``` math
r:\mathbb R^2\to\mathbb R,\qquad r(x,z)=x,
 \qquad s(x)=(x,0)
```
satisfies $`r\circ s=\operatorname{id}_{\mathbb R}`$.

The mistake was a type error. A right inverse chooses one preimage; it does not recover the preimage that was actually supplied. Actual microscopic recovery is a left-inverse condition. Autonomous effective evolution is a third condition, namely factorization through the initial reduction. This paper keeps those objects separate.

The results are structural set-theoretic, topological, metric, measure-theoretic, or operator-algebraic theorems according to the hypotheses stated in each section. No probability, entropy, Hilbert structure, geometry, or physical time is inferred from a bare map of sets.

# Typed projection and evolution data

Let $`A`$ be an admissible upper state domain and let
``` math
\Phi_t:A\to X_t
```
be an upper evolution map. Invertibility of $`\Phi_t`$ is not needed for the basic typing results. Let
``` math
P_0:A\to Y_0,
 \qquad
 P_t:\Phi_t(A)\to Y_t
```
be surjective reduction maps onto their declared effective images, and define the cross-level output map
``` math
T_t=P_t\circ\Phi_t:A\to Y_t.
```

The fibers of $`P_0`$ define the initial effective equivalence relation
``` math
x\sim_0x'\quad\Longleftrightarrow\quad P_0(x)=P_0(x').
```

<div class="definition">

**Definition 1** (Representative section). A representative section for $`T_t`$ is a map $`S_t:Y_t\to A`$ satisfying
``` math
T_t\circ S_t=\operatorname{id}_{Y_t}.
```
It chooses one upper state compatible with each final effective state.

</div>

<div class="definition">

**Definition 2** (Exact upper decoder). An exact decoder is a map $`D_t:T_t(A)\to A`$ satisfying
``` math
D_t\circ T_t=\operatorname{id}_A.
```
It recovers the actual upper input from the final effective output.

</div>

<div class="definition">

**Definition 3** (Autonomous reduced evolution). An autonomous reduced evolution is a map $`F_t:Y_0\to Y_t`$ satisfying
``` math
F_t\circ P_0=P_t\circ\Phi_t.
```

</div>

<div class="definition">

**Definition 4** (Effective merger). If $`F_t`$ exists, an effective merger occurs when distinct initial effective states $`y\ne y'`$ satisfy $`F_t(y)=F_t(y')`$.

</div>

These four definitions have different domains and equations. They are not interchangeable notions of inversion.

# Projection–descent and recovery theorem

<div id="thm:main" class="theorem">

**Theorem 5** (Projection–descent and recovery). *For the typed data above:*

1.  *A set-theoretic representative section $`S_t`$ exists if $`T_t`$ is surjective and the relevant choice principle is available. A continuous, measurable, local, or Lipschitz section requires a theorem in that category.*

2.  *An exact decoder $`D_t:T_t(A)\to A`$ exists only if $`T_t`$ is injective. Conversely, if $`T_t`$ is injective, its inverse on $`T_t(A)`$ is an exact decoder.*

3.  *An autonomous reduced evolution $`F_t`$ exists if and only if
    ``` math
    \begin{equation}
     P_0(x)=P_0(x')
     \quad\Longrightarrow\quad
     P_t(\Phi_t x)=P_t(\Phi_t x')
     \label{eq:factor}
    \end{equation}
    ```
    for all $`x,x'\in A`$. When it exists, $`F_t`$ is unique.*

4.  *If <a href="#eq:factor" data-reference-type="eqref" data-reference="eq:factor">[eq:factor]</a> holds and there are $`x,x'\in A`$ with $`P_0(x)\ne P_0(x')`$ but $`P_t(\Phi_t x)=P_t(\Phi_t x')`$, then $`F_t`$ is noninjective. The prior effective state cannot be decoded uniquely from the final effective state.*

</div>

<div class="proof">

*Proof.* The first item is the definition of a section of a surjection. If $`D_tT_t=\operatorname{id}_A`$ and $`T_t(x)=T_t(x')`$, applying $`D_t`$ gives $`x=x'`$, proving the second item. For the third, necessity follows by applying $`F_t`$ to equal initial effective states. Under <a href="#eq:factor" data-reference-type="eqref" data-reference="eq:factor">[eq:factor]</a>, define
``` math
F_t(P_0x):=P_t(\Phi_tx).
```
The implication makes the value independent of the representative; surjectivity of $`P_0`$ gives existence and uniqueness. The last item follows directly from the definition of $`F_t`$. ◻

</div>

<div class="corollary">

**Corollary 6** (Noninjectivity does not obstruct representative selection). *Noninjectivity of $`T_t`$ rules out an exact decoder, not a representative section. Surjectivity is the set-theoretic gate for a right section.*

</div>

The load-bearing part of Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">5</a> is item 3. It asks whether the upper evolution maps every initial projection fiber into one final projection fiber. If so, all upper representatives of one reduced state give the same reduced future and $`F_t`$ is well defined. If not, choosing a section can manufacture one representative-dependent trajectory, but it cannot turn that trajectory into an autonomous law on $`Y_0`$.

# A valid no-right-section obstruction

There is a correct obstruction when the map in question is a self-map of the same reduced space and its image is provably too small.

<div id="thm:diameter" class="theorem">

**Theorem 7** (Finite-diameter contraction obstruction). *Let $`(Y_A,d)`$ have finite positive diameter $`D`$, and let $`G:Y_A\to Y_A`$ satisfy
``` math
d(Gy,Gy')\le\kappa d(y,y')+c\varepsilon,
 \qquad0\le\kappa<1,\quad c\varepsilon\ge0.
```
Then
``` math
\operatorname{diam}G(Y_A)\le\kappa D+c\varepsilon.
```
If $`(1-\kappa)D>c\varepsilon`$, then $`G`$ is not surjective and therefore has no right section $`S:Y_A\to Y_A`$ with $`G\circ S=\operatorname{id}_{Y_A}`$.*

</div>

<div class="proof">

*Proof.* Take the supremum of the displayed inequality over all pairs. Under the strict condition the image diameter is smaller than $`D`$, whereas a surjective image would equal $`Y_A`$ and have diameter $`D`$. ◻

</div>

This theorem concerns a reduced self-map $`G:Y_A\to Y_A`$. It does not apply to a cross-level map $`T_t:A\to Y_t`$ merely because that map is noninjective. Moreover, the additive-error inequality is not a Banach contraction. Banach requires a genuine Lipschitz constant below one on a complete invariant domain.

# Stable representative continuation

Suppose $`A,Y_t`$ are metric spaces. For all Lipschitz right sections define the best section condition number
``` math
\kappa_{\rm sec}(t)
 :=\inf\{\operatorname{Lip}(S_t):T_tS_t=\operatorname{id}_{Y_t}\},
```
with $`\kappa_{\rm sec}(t)=+\infty`$ if no Lipschitz section exists.

<div class="proposition">

**Proposition 8** (Section-conditioning diagnostic). *If $`\kappa_{\rm sec}(t)`$ remains bounded on an interval and a chosen family of sections attains a uniform bound, representative selection is uniformly Lipschitz on that interval. Blow-up of $`\kappa_{\rm sec}`$ or loss of surjectivity is an obstruction to such stable continuation. It is not, by itself, a physical singularity, entropy law, or stochastic transition.*

</div>

For spectral projections, a parallel diagnostic is failure of bounded norm-resolvent continuation of the selected Riesz projector. These two diagnostics are related only when a realization proves the relation.

# Admissibility without automatic selection

Let $`m_j(t,x)`$ be declared continuous margins and define
``` math
A_t^\delta=\{x:m_j(t,x)\ge\delta\text{ for every }j\}.
```
The margins may record operator domains, spectral separation, complementary damping, leakage, contraction, truncation error, section conditioning, or physical hyperbolicity. A first exit from $`A_t^0`$ means that at least one declared description condition fails.

Exit does not imply that $`T_t`$ has no set-theoretic section; the failed margin must be identified. Nor does exit select a new state. One must stop the reduced description, derive continuation from upper dynamics, or add a hybrid reset law. A reset is new continuation data and must prove conservation, measurability, and any assigned probabilities.

# Measure-dependent stochastic reduction

Projection does not create a probability measure. A stochastic reduced law can be induced only after preparation or invariant measure data are supplied.

<div id="thm:kernel" class="theorem">

**Theorem 9** (Measure-dependent reduced kernel). *Let $`A,Y_0,Y_t`$ be standard Borel spaces, let $`P_0`$ be measurable, and let $`\mu`$ be a probability measure on $`A`$. Let $`\{\mu_y\}`$ be a regular conditional distribution of $`x`$ given $`P_0(x)=y`$. Then
``` math
K_t(y,B)
 :=\mu_y\bigl(\{x:P_t(\Phi_tx)\in B\}\bigr)
```
defines a Markov kernel from $`Y_0`$ to $`Y_t`$, up to the usual $`(P_0)_\#\mu`$-null sets. If autonomous descent holds, then
``` math
K_t(y,\cdot)=\delta_{F_t(y)}
```
for almost every $`y`$.*

</div>

<div class="proof">

*Proof.* Regular conditional distributions exist on standard Borel spaces. Measurability and countable additivity pass through the measurable preimage defining $`K_t`$. Under descent, $`P_t\Phi_tx=F_t(P_0x)`$ is constant on each conditional fiber. ◻

</div>

Different upper measures, even with the same projection fibers, may induce different kernels. Fiber cardinality alone does not determine weights and does not imply the Born rule.

# Information, entropy, and temporal direction

Noninjectivity states only that some distinctions are absent from the reduced state. Quantitative information requires a sigma-algebra, coding, metric, or probability measure. Entropy requires a specified entropy functional and state. Monotone entropy production requires a dynamical theorem such as data processing for a declared stochastic channel, a coarse-graining inequality, or a thermodynamic balance law.

Likewise, failure of an exact decoder does not by itself establish an arrow of time. A temporal arrow requires an oriented evolution family and an asymmetric property such as a semigroup without inverse in the chosen category, a monotone Lyapunov/entropy functional, or a boundary condition. A representative section is not a reverse-time evolution.

Universality also needs more than equivalence classes. It requires stability of reduced laws under a declared class of microscopic perturbations, for example the basin-local contraction estimate of the corrected Foundation and Fixed Points spine.

# Locality descent under coherent compression

Let $`\pi:M_{10}\to Y_4`$ be the canonical physical bundle and let
``` math
P=\int_{Y_4}^{\oplus}P_x\,d\mu(x)
```
be a decomposable fiberwise coherent projector. Suppose $`O\mapsto\mathcal A_{10}(\pi^{-1}O)`$ is an upper local net. Define
``` math
\mathcal A_{10}^P(O)
 =\{A\in\mathcal A_{10}(\pi^{-1}O):[A,P]=0\}
```
and
``` math
\mathcal A_4(O)
 =\{PAP|_{\operatorname{Ran}P}:A\in\mathcal A_{10}^P(O)\}.
```

<div id="thm:locality" class="theorem">

**Theorem 10** (Fixed-point locality descent). *If the upper net is isotonic, then $`\mathcal A_4`$ is isotonic. If upper observables assigned to spacelike separated base regions commute, then their compressed coherent observables commute. Thus microcausality descends on the $`P`$-compatible subalgebra.*

</div>

<div class="proof">

*Proof.* Upper inclusion immediately gives compressed inclusion. For compatible $`A,B`$, commutation with $`P`$ gives
``` math
[PAP,PBP]|_{\operatorname{Ran}P}=P[A,B]P|_{\operatorname{Ran}P},
```
which vanishes for spacelike separated upper observables. ◻

</div>

This theorem does not imply state factorization. Entangled or otherwise nonfactorizing states may restrict to the descended net. A projection nonlocal over the base, or an observable not preserving $`\operatorname{Ran}P`$, lies outside this theorem.

Thus coherent compression preserves locality only for the algebra on which the displayed commutation calculation is legal. The theorem transports an existing upper microcausal relation; it does not create spacetime locality from an arbitrary projector and does not force the compressed state to be unentangled.

# Corrected realizations

## Open quantum systems

For a system and environment, partial trace
``` math
P(\rho_{SE})=\operatorname{Tr}_E\rho_{SE}
```
is noninjective but surjective onto system density matrices when an environment state is available. The assignment $`S(\rho_S)=\rho_S\otimes\sigma_E`$ is a representative section. It is not an exact decoder of the actual correlated state $`\rho_{SE}`$.

A state-independent reduced channel exists only under assignment and compatibility conditions. Initial system–environment correlations can make the future reduced state depend on more than $`\rho_S`$, violating the descent criterion. Probabilities are already supplied by the quantum state and Born rule; they are not derived from noninjectivity of partial trace.

## Wilsonian reduction

Integrating out high-frequency modes maps UV actions or measures to lower-scale effective data. Distinct UV inputs may have the same IR image, so exact UV decoding generally fails. A representative UV completion, when it exists, is a section and is nonunique. Autonomous RG evolution requires a selected theory space and closure or controlled truncation; it does not follow from coarse graining alone. Universality requires a fixed-point/basin stability theorem.

## Exterior gravity

Restriction of a global solution to an exterior domain can be noninjective. An exterior-to-global extension, where constraint-compatible extensions exist, is a representative section rather than recovery of the actual interior. Autonomous exterior evolution requires boundary conditions, flux data, and a well-posed domain. Horizon area or entropy is not obtained from noninjectivity alone.

## Modal Triplet Theory

In the corrected MTT Foundation, $`P`$ is the joint coherent spectral projector and $`R_\tau`$ is the stabilization flow. An autonomous coherent map exists exactly when $`P R_\tau`$ is constant on the relevant initial $`P`$-fibers. Exact invariance is a sufficient special case. FP I–VI provide conditional fixed-point, damping, curved-projector, covariance, and admissibility results.

The internal gap and Riesz-projector continuation can support stable coherent reduction. They do not by themselves derive a measure, Born weights, entropy, a reset outcome, quantum field theory, gravity, or cosmology. MTT is therefore a conditional realization of the typed framework only to the extent that each gate is verified.

# Scoped projection–admissibility theorem

<div id="thm:scope" class="theorem">

**Theorem 11** (Scoped principle). *For typed upper evolution and reductions:*

1.  *representative selection, exact recovery, autonomous descent, and effective merger obey the separate conditions in Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">5</a>;*

2.  *a reduced self-map has no right section when its image diameter is strictly smaller than its state-space diameter;*

3.  *stable representative continuation can be tested by section conditioning or, in spectral realizations, bounded projector continuation;*

4.  *an upper measure and regular conditional distributions induce a reduced Markov kernel; and*

5.  *upper locality descends to the coherent $`P`$-compatible compressed net.*

*No probability rule, entropy production, arrow of time, universality class, geometry, or Hilbert structure follows from noninjectivity alone.*

</div>

# Conclusion

Projection and admissibility remain useful organizing ideas once their maps are typed correctly. The corrected principle says precisely when effective dynamics descends, what a section can and cannot recover, when a reduced map truly loses a right section, and which additional measure, stability, and locality data support stronger conclusions. This narrower theorem is more useful than the former universal obstruction because each downstream claim now has a checkable mathematical gate.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, revised v7, 2026.

P. Nero, *Fixed Points I–VI*, corrected theorem spine, 2026.

A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995.

H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press, 2002.

</div>

# Computational Evidence and Reproducibility

The numerical and machine-verifiable claims used by this paper are archived in the curated repository, `https://github.com/PeterNero/mtt-results-repro`. The mapped authority/result identifiers are `no result rows mapped`. Claim tiers in that capsule distinguish exact derivation, certified numerics, profile replay, conditional results, and open obligations.
