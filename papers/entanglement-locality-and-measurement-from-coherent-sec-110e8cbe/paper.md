---
abstract: |
  Algebraic quantum field theory (AQFT) enforces relativistic locality at the level of observable algebras while allowing globally entangled states. However, AQFT alone does not explain why physically realized states are typically entangled, how entanglement propagates, or why measurement reduces entanglement without enabling superluminal signaling. We present a local, state-restricting framework in which physically admissible states are those induced by coherent-sector dynamics (bounded geometry, spectral gap, bounded coherent projector, and contractive stability). Entanglement is shown to arise as a global coherence constraint in configuration space, while microcausality and the time-slice property remain intact on spacetime. Measurement is modeled as localized disturbance followed by stabilization into admissible basins, yielding partial disentanglement. Standard Bell/CHSH and temporal Bell (Leggett–Garg) violations are recovered without nonlocal influence. Entanglement spreading via common ancestors (mediated entanglement and entanglement swapping) is interpreted as causal propagation of coherence constraints through local interactions. The framework integrates the MTT QFT-projection layer, the measurement-as-stabilization model, and the Bell/temporal-Bell analyses in a single AQFT-compatible description.
author:
- Peter Nero
current_version: v1.0
date: Janury 2026
generated_from_main_tex_sha256: 1bd31d3d007786e398113b1635d8a137e3f9a450c7bf9eda63b84b0efa0a0674
paper_id: entanglement-locality-and-measurement-from-coherent-sec-110e8cbe
release_state: zenodo_released
released_version: v1.0
title: Entanglement, Locality, and Measurement from Coherent Sector Dynamics
zenodo_doi: 10.5281/zenodo.18261393
zenodo_record_id: 18261393
zenodo_url: "https://zenodo.org/records/18261393"
---

# Introduction

Quantum entanglement is often presented as a tension between locality and correlation. Relativistic quantum field theory resolves this tension formally in the algebraic framework (AQFT), which enforces strict locality at the level of observable algebras while allowing highly entangled global states . AQFT thereby explains why entanglement does not permit superluminal signaling, but it does not explain why physically realized states are typically entangled, how entanglement spreads, or how measurement reduces entanglement.

In Modal Triplet Theory (MTT), physical states are not arbitrary states on the AQFT net: they are restricted by coherence admissibility (bounded geometry, spectral gap, bounded coherent projector, and stability margins encoded by the Fundamental Contractivity Condition, FCC) . Measurement is modeled as localized disturbance followed by stabilization into an admissible basin , and Bell/temporal-Bell violations are treated as projection artifacts of globally consistent coherent histories .

This paper provides a unified, AQFT-compatible formulation:

- We do *not* modify AQFT axioms (locality, isotony, time-slice).

- We restrict the physically relevant state space to an admissible class $`\mathcal{S}_{\mathrm{coh}}\subset\mathcal{S}(\mathcal{A})`$ induced by coherent-sector dynamics.

- Entanglement is explained as a coherence constraint in configuration space, while microcausality and causal propagation remain intact on spacetime.

- Measurement reduces entanglement by disturbance + stabilization, without nonlocal influence.

- Entanglement propagation through common ancestors is treated as standard local interaction and causal spreading (Lieb–Robinson-type bounds).

# AQFT preliminaries: locality and states

Let $`(Y^4,g)`$ be a globally hyperbolic spacetime. AQFT assigns to each suitable region $`\mathcal{O}\subset Y^4`$ a C$`^\ast`$-algebra $`\mathcal{A}(\mathcal{O})`$ such that:

#### Isotony.

If $`\mathcal{O}_1\subset\mathcal{O}_2`$, then $`\mathcal{A}(\mathcal{O}_1)\subset\mathcal{A}(\mathcal{O}_2)`$.

#### Microcausality (local commutativity).

If $`\mathcal{O}_1`$ and $`\mathcal{O}_2`$ are spacelike separated, then
``` math
\begin{equation}
\label{eq:microcausality}
[\mathcal{A}(\mathcal{O}_1),\mathcal{A}(\mathcal{O}_2)]=0.
\end{equation}
```

#### Time-slice axiom.

If $`\mathcal{O}`$ contains a Cauchy surface for its domain of dependence, then $`\mathcal{A}(\mathcal{O})`$ generates the algebra in the domain of dependence.

A *state* is a positive normalized linear functional
``` math
\omega:\mathcal{A}\to\mathbb{C},\qquad \omega(\mathbf{1})=1,\quad \omega(A^\ast A)\ge 0.
```
States need not factorize over commuting subalgebras, and AQFT explicitly permits entangled states .

# Entanglement in AQFT and the factorization gap

Let $`\mathcal{A}_1:=\mathcal{A}(\mathcal{O}_1)`$ and $`\mathcal{A}_2:=\mathcal{A}(\mathcal{O}_2)`$ for spacelike-separated regions. Microcausality implies $`[A,B]=0`$ for $`A\in\mathcal{A}_1`$ and $`B\in\mathcal{A}_2`$, but it does *not* imply state factorization.

A state is *separable* on $`\mathcal{A}_1\vee\mathcal{A}_2`$ if it admits a convex decomposition
``` math
\begin{equation}
\label{eq:separable}
\omega(AB)=\sum_i p_i\,\omega^{(1)}_i(A)\,\omega^{(2)}_i(B),
\quad A\in\mathcal{A}_1,\;B\in\mathcal{A}_2,\; p_i\ge 0,\;\sum_i p_i=1.
\end{equation}
```
Otherwise it is entangled. Thus entanglement is compatible with AQFT locality: non-factorization is a property of the state, not of commutators.

AQFT therefore answers the *compatibility* question (“how can entanglement exist without signaling?”), but it does not by itself supply a selection principle for why physically realized states are typically non-factorizing.

# Coherent-sector admissibility as a state-selection principle

## Two-layer picture: configuration versus observables

MTT distinguishes:

1.  a higher-dimensional coherent configuration layer (10D / bundle manifold) in which admissibility and stability are formulated (spectral gaps, projector boundedness, contractive evolution);

2.  an effective 4D observable layer described by AQFT on $`(Y^4,g)`$.

The QFT-projection paper formalizes the effective AQFT output of coherent-sector reduction and renormalization on curved spacetimes (Hadamard states, local covariance, and standard renormalization freedoms) .

## Admissible state class

<div id="def:Scoh" class="definition">

**Definition 1** (Admissible (coherent) state class). Let $`\mathcal{S}(\mathcal{A})`$ denote the space of AQFT states. Define $`\mathcal{S}_{\mathrm{coh}}\subset\mathcal{S}(\mathcal{A})`$ to be the subclass of states induced by admissible coherent configurations, i.e. those satisfying:

1.  bounded geometry on time slabs;

2.  persistence of a uniform spectral gap separating coherent from noncoherent modes;

3.  boundedness of the coherent projector on Sobolev scales;

4.  local disturbance–damping stability margins (FCC) on the relevant invariant sets.

</div>

This is a state-selection principle: AQFT axioms remain unchanged, but the set of physically realized states is restricted.

<div id="prop:locality-preserved" class="proposition">

**Proposition 2** (Locality preserved). *For any $`\omega\in\mathcal{S}_{\mathrm{coh}}`$, microcausality <a href="#eq:microcausality" data-reference-type="eqref" data-reference="eq:microcausality">[eq:microcausality]</a> holds exactly as in AQFT.*

</div>

<div class="proof">

*Proof.* Microcausality is an algebraic property of the net $`\mathcal{O}\mapsto\mathcal{A}(\mathcal{O})`$, independent of state choice. Restricting to $`\mathcal{S}_{\mathrm{coh}}`$ does not alter commutators. ◻

</div>

## Entanglement as coherence constraint

<div id="prop:entanglement-coherence" class="proposition">

**Proposition 3** (Entanglement from global coherence constraints). *States in $`\mathcal{S}_{\mathrm{coh}}`$ may be non-factorizing over spacelike-separated regions. Such non-factorization is interpreted as a coherence constraint in configuration space, not as superluminal influence in spacetime.*

</div>

<div class="remark">

*Remark 4*. The phrase “global” here refers to configuration-space admissibility and stability constraints, not to a physical signal propagating in spacetime. This is the same logical distinction used throughout FP V–VI to separate global attractors in configuration space from unique spacetime histories .

</div>

# Bell/CHSH violations without nonlocal influence

Let $`A_0,A_1\in\mathcal{A}(\mathcal{O}_A)`$ and $`B_0,B_1\in\mathcal{A}(\mathcal{O}_B)`$ be observables with spectra in $`[-1,1]`$, with $`\mathcal{O}_A`$ spacelike to $`\mathcal{O}_B`$. Define the CHSH expression
``` math
\begin{equation}
\label{eq:CHSH}
S:=\omega(A_0B_0)+\omega(A_0B_1)+\omega(A_1B_0)-\omega(A_1B_1).
\end{equation}
```

Classical local hidden-variable models yield $`|S|\le 2`$ . Quantum theory permits $`|S|\le 2\sqrt{2}`$ (Tsirelson bound) .

<div id="prop:bell" class="proposition">

**Proposition 5** (Bell violation within AQFT locality). *For $`\omega\in\mathcal{S}_{\mathrm{coh}}`$, CHSH inequalities can be violated while microcausality holds.*

</div>

<div class="proof">

*Explanation.* Microcausality ensures $`[A_i,B_j]=0`$ but does not imply separability <a href="#eq:separable" data-reference-type="eqref" data-reference="eq:separable">[eq:separable]</a>. CHSH derivations of $`|S|\le 2`$ require a factorizable hidden-variable representation, which fails for generic entangled states. Since $`\mathcal{S}_{\mathrm{coh}}`$ includes non-factorizing admissible states, violations are possible. No signaling follows because commutators vanish and local marginals cannot be controlled by spacelike choices. ◻

</div>

This connects directly to the MTT Bell analysis: Bell nonlocality is a failure of classical factorization, interpreted as a projection artifact of a local higher-dimensional ontology .

# Temporal Bell (Leggett–Garg) violations from disturbance + stabilization

Let $`Q(t)`$ be a dichotomic observable ($`\pm 1`$) associated with a system measured at times $`t_1<t_2<t_3`$. Define correlators $`C_{ij}:=\omega(Q(t_i)Q(t_j))`$. A standard Leggett–Garg inequality is
``` math
\begin{equation}
\label{eq:LG}
K := C_{12}+C_{23}-C_{13}\le 1
\end{equation}
```
under macrorealism and noninvasive measurability.

<div id="prop:temporal" class="proposition">

**Proposition 6** (Temporal Bell violations). *Temporal Bell/Leggett–Garg violations in $`\mathcal{S}_{\mathrm{coh}}`$ arise because measurement is necessarily invasive: it acts as a disturbance that perturbs coherence, followed by stabilization into an admissible basin.*

</div>

<div class="remark">

*Remark 7*. This is precisely the mechanism formalized in the temporal Bell and measurement papers: violations reflect global consistency constraints on admissible histories together with unavoidable disturbance .

</div>

# Measurement as disturbance and stabilization: partial disentanglement

We model measurement as a localized interaction channel described by a completely positive (CP) instrument. In density-operator language, an outcome channel $`m`$ is
``` math
\begin{equation}
\label{eq:instrument}
\rho \mapsto \rho_m'=\frac{\mathcal{M}_m(\rho)}{\Tr(\mathcal{M}_m(\rho))},
\qquad
\mathcal{M}_m(\rho)=\sum_\alpha K_{m,\alpha}\rho K_{m,\alpha}^\ast.
\end{equation}
```
In MTT interpretation, the Kraus operators represent: (i) a localized disturbance (kicking modal amplitudes), and (ii) stabilization/damping returning the configuration to an admissible basin .

<div id="prop:partial" class="proposition">

**Proposition 8** (Partial disentanglement). *Let $`\rho_{AB}`$ be a bipartite state. A local measurement on $`A`$ produces
``` math
\rho_{AB}\mapsto \rho'_{AB,m}=\frac{(\mathcal{M}_m\otimes I)\rho_{AB}}{\Tr((\mathcal{M}_m\otimes I)\rho_{AB})},
```
which generically reduces entanglement between $`A`$ and $`B`$ by damping off-diagonal coherence in the measured sector.*

</div>

<div class="remark">

*Remark 9*. This explains “collapse-like” behavior without superluminal influence: the operation is local, but the global admissible state is updated after disturbance and stabilization.

</div>

# Entanglement propagation: common ancestors and causal spreading

Entanglement can be created between subsystems that never directly interacted by local interactions with a third system.

## Mediated entanglement and entanglement swapping

Let $`A,B,C`$ be three subsystems. Suppose $`A`$ interacts locally with $`C`$ and later $`B`$ interacts locally with $`C`$. After tracing out $`C`$, $`\rho_{AB}`$ can become entangled even if $`A`$ and $`B`$ had no shared creation history.

In MTT terms, $`C`$ acts as a *common coherence ancestor* in configuration space: local interactions impose a joint admissibility constraint that propagates through admissible dynamics.

## Finite-speed spreading

In many-body and lattice models, locality of interactions implies Lieb–Robinson bounds : for observables $`A`$ and $`B`$ supported at distance $`d`$,
``` math
\begin{equation}
\label{eq:LR}
\|[A(t),B]\|\le C\,e^{-\mu(d-vt)}.
\end{equation}
```
This expresses finite-speed propagation of influence/correlation. In the MTT coherent regime, effective causal cones and bounded-geometry dynamics provide analogous control: correlations spread through local interaction, but signaling remains bounded by the effective light cone.

<div class="remark">

*Remark 10*. Equation <a href="#eq:LR" data-reference-type="eqref" data-reference="eq:LR">[eq:LR]</a> is a standard template; the precise constants depend on the effective dynamics. The conceptual point is that “entanglement spreading” is causal: it proceeds through a chain of local interactions and does not constitute superluminal influence.

</div>

# What is explained and what is not

This framework:

- preserves AQFT locality and causal propagation;

- explains entanglement as non-factorization induced by coherent admissibility constraints;

- explains measurement-induced partial disentanglement as disturbance + stabilization;

- accounts for Bell and temporal Bell violations without nonlocal influence.

It does not claim a unique global spacetime history or a global S-matrix on generic curved backgrounds. Where asymptotic flatness fails, the correct description is via local algebras and states.

# Conclusion

AQFT already reconciles entanglement with locality by separating algebraic locality (commutators) from state factorization. MTT adds a physically motivated state-selection principle: admissible coherent-sector states. Within this restriction, entanglement is interpreted as a coherence constraint in configuration space, while microcausality remains exact. Measurement reduces entanglement via localized disturbance and stabilization into admissible basins. Entanglement spreads through local interactions via common ancestors and finite-speed propagation. This supplies a coherent mathematical and physical account unifying AQFT locality with the MTT measurement and Bell analyses.

# A Ten–Dimensional Formulation in Fixed–Point Language

## 10D local algebras and locality

Let $`M^{10}`$ denote the full Modal Triplet manifold equipped with the bundle/folding structure introduced in the Fixed Points series. For any causally admissible region $`\mathcal{U}\subset M^{10}`$, define a local observable algebra $`\mathcal{A}_{10}(\mathcal{U})`$ generated by fields supported in $`\mathcal{U}`$.

Locality in ten dimensions is imposed in the standard algebraic sense: for spacelike–separated regions $`\mathcal{U}_1,\mathcal{U}_2\subset M^{10}`$,
``` math
\begin{equation}
\label{eq:10D-locality}
[\mathcal{A}_{10}(\mathcal{U}_1),\mathcal{A}_{10}(\mathcal{U}_2)]=0.
\end{equation}
```
This axiom is purely kinematic and independent of any coherence or stability assumptions.

## The coherent sector as an admissible invariant set

Let $`\Pi_{\mathrm{coh}}`$ denote the coherent projector defined in FP I–II, acting on the 10D configuration space $`\mathcal{H}_{10}`$ and selecting the joint low–lying spectral sector compatible with the modal bundle structure.

Define the coherent configuration space
``` math
\mathcal{H}_{\mathrm{coh}}:=\operatorname{Ran}(\Pi_{\mathrm{coh}}).
```

As in FP III–V, we restrict attention to an admissible invariant set $`D\subset\mathcal{H}_{\mathrm{coh}}`$ satisfying:

1.  bounded geometry on time slabs;

2.  persistence of a uniform spectral gap separating coherent from noncoherent modes;

3.  boundedness of $`\Pi_{\mathrm{coh}}`$ on the relevant Sobolev scales;

4.  disturbance–damping balance (FCC), ensuring local contractivity of the projected evolution.

Physical configurations are elements of $`D`$. This restriction is dynamical and local; it does not modify the algebraic locality axiom <a href="#eq:10D-locality" data-reference-type="eqref" data-reference="eq:10D-locality">[eq:10D-locality]</a>.

## States and non-factorization in FP language

A ten–dimensional state is a positive normalized linear functional
``` math
\omega_{10}:\mathcal{A}_{10}\to\mathbb{C}.
```
We say $`\omega_{10}`$ is *admissible* if its support lies in $`D`$.

<div id="prop:10D-nonfact" class="proposition">

**Proposition 11** (Global constraints without nonlocality). *Let $`\mathcal{U}_1,\mathcal{U}_2\subset M^{10}`$ be spacelike separated. For $`\omega_{10}`$ admissible, expectation values need not factorize:
``` math
\omega_{10}(AB)\neq \omega_{10}(A)\,\omega_{10}(B),
\quad A\in\mathcal{A}_{10}(\mathcal{U}_1),\;B\in\mathcal{A}_{10}(\mathcal{U}_2),
```
even though <a href="#eq:10D-locality" data-reference-type="eqref" data-reference="eq:10D-locality">[eq:10D-locality]</a> holds.*

</div>

<div class="remark">

*Remark 12*. In FP terms, this non-factorization reflects the fact that the admissible invariant set $`D`$ is not a product set under decomposition into subregions. Admissibility imposes global constraints in configuration space while preserving local spacetime causality.

</div>

## Measurement as disturbance and contraction

Measurement in the FP framework is modeled as a localized disturbance followed by stabilization under the projected dynamics. Schematically,
``` math
\begin{equation}
\label{eq:FP-measure}
\Psi \;\mapsto\; T_\tau\bigl(\Psi+\delta\Psi\bigr),
\qquad
T_\tau:=\Pi_{\mathrm{coh}}\circ\Phi_\tau,
\end{equation}
```
where $`\delta\Psi`$ is a bounded local perturbation and $`\Phi_\tau`$ is the unprojected time–$`\tau`$ evolution.

By FCC, $`T_\tau`$ is contractive on $`D`$. Hence disturbances are damped and the configuration returns to an admissible basin.

<div id="prop:10D-partial" class="proposition">

**Proposition 13** (Partial disentanglement). *Let $`\Psi\in D`$ encode correlations between degrees of freedom supported in disjoint regions. A local disturbance acting in one region followed by <a href="#eq:FP-measure" data-reference-type="eqref" data-reference="eq:FP-measure">[eq:FP-measure]</a> typically reduces cross–region correlations by contracting the configuration into a smaller admissible basin.*

</div>

This is the FP–language counterpart of partial disentanglement in the 4D CP–map description.

## Entanglement propagation and common ancestors

Consider three regions $`\mathcal{U}_A,\mathcal{U}_B,\mathcal{U}_C\subset M^{10}`$. Suppose $`\Psi`$ evolves such that:

- $`\mathcal{U}_A`$ overlaps with $`\mathcal{U}_C`$ at some time,

- $`\mathcal{U}_B`$ overlaps with $`\mathcal{U}_C`$ at a later time,

- $`\mathcal{U}_A`$ and $`\mathcal{U}_B`$ never overlap directly.

<div id="prop:ancestor" class="proposition">

**Proposition 14** (Common–ancestor correlations). *After tracing out degrees of freedom in $`\mathcal{U}_C`$, the reduced configuration on $`\mathcal{U}_A\cup\mathcal{U}_B`$ may exhibit non-factorizing correlations, even though no direct interaction occurred between $`\mathcal{U}_A`$ and $`\mathcal{U}_B`$.*

</div>

<div class="remark">

*Remark 15*. In FP terms, $`\mathcal{U}_C`$ acts as a *common ancestor* by imposing a joint admissibility constraint on the configuration in $`D`$. Correlations propagate through local overlap and projected evolution, not by superluminal influence.

</div>

## Projection to four dimensions

The effective four–dimensional AQFT description is obtained by projecting admissible 10D states to observables supported on the physical spacetime $`Y^4\subset M^{10}`$. Denote this pushforward by
``` math
\omega_{4}(A):=\omega_{10}(\tilde A),
```
where $`\tilde A`$ is the natural lift of $`A\in\mathcal{A}(Y^4)`$.

<div id="prop:projection" class="proposition">

**Proposition 16** (4D entanglement as a projection artifact). *Non-factorizing correlations in $`\omega_{4}`$ arise as the projection of admissible 10D coherence constraints. Local commutativity in 4D is preserved because it descends from <a href="#eq:10D-locality" data-reference-type="eqref" data-reference="eq:10D-locality">[eq:10D-locality]</a>.*

</div>

## Alignment with FP I–VI

This appendix shows that the entanglement framework used in the main text is the direct AQFT translation of FP I–VI principles:

- admissible states correspond to invariant sets $`D`$;

- Bell and temporal Bell violations reflect non-product structure of $`D`$;

- measurement corresponds to disturbance plus contraction under $`T_\tau`$;

- entanglement propagation is causal transport of constraints through local overlap.

Thus the 4D entanglement picture is fully aligned with the ten–dimensional fixed–point framework and introduces no additional assumptions beyond those already present in the FP series.

<div class="thebibliography">

99

R. Haag, , Springer, 2nd ed., 1996.

R. Brunetti, K. Fredenhagen, and R. Verch, The generally covariant locality principle: A new paradigm for local quantum field theory, , 237:31–68, 2003.

S. Hollands and R. M. Wald, Local Wick polynomials and time ordered products of quantum fields in curved spacetime, , 223:289–326, 2001.

J. S. Bell, On the Einstein Podolsky Rosen paradox, , 1:195–200, 1964.

J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, Proposed experiment to test local hidden-variable theories, , 23:880–884, 1969.

B. S. Tsirelson, Quantum generalizations of Bell’s inequality, , 4:93–100, 1980.

A. J. Leggett and A. Garg, Quantum mechanics versus macroscopic realism: Is the flux there when nobody looks?, , 54:857–860, 1985.

E. H. Lieb and D. W. Robinson, The finite group velocity of quantum spin systems, , 28:251–257, 1972.

P. Nero, Modal Triplet Theory: Foundation — A rigorous fixed-point framework for unified 4D physics, Preprint, 2025.

P. Nero, Fixed Points III: Disturbance–Damping Balance and Stability, Preprint, 2025.

P. Nero, Fixed Points V: Curvature Coupling and Admissibility Barriers, Preprint, 2025.

P. Nero, Fixed Points VI: Formal Synthesis and Physical Interpretations, Preprint, 2025.

P. Nero, Modal Triplet Theory: From MTT to Quantum Field Theory on Curved Spacetime, Preprint, 2025.

P. Nero, Measurement as Disturbance and Stabilization in Modal Triplet Theory, Preprint, 2025.

P. Nero, Temporal Bell Inequalities and Global Consistency, Preprint, 2025.

P. Nero, Modal Fixed Points, Bell’s Beables, and the Limits of Factorization, Preprint, 2025.

</div>
