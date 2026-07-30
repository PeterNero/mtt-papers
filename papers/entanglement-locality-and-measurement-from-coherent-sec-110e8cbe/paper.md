---
abstract: |
  Algebraic quantum field theory (AQFT) separates locality of observable algebras from factorization of states: spacelike algebras may commute while a state on their joint algebra remains entangled. We formulate the precise MTT-compatible version of this distinction. Given an upper local net indexed over a globally hyperbolic four-dimensional base, a decomposable coherent projector, and the coherent-preserving local subalgebra, the fixed-point locality-descent theorem transports isotony and microcausality to the compressed net. Nonfactorizing states may restrict to that net, but admissibility and locality alone neither force entanglement nor select a Bell-violating state. Bell/CHSH violation is therefore compatible with upper-local dynamics when a suitable nonseparable state and local instruments are independently supplied. Measurement is treated as an ordinary localized completely positive instrument. Such instruments obey operational no-signaling under the standard locality assumptions; they cannot increase an entanglement monotone on average, although an individually postselected branch need not lose entanglement. Common-ancestor protocols and finite-speed correlation spreading remain standard local mechanisms. The result is a conditional AQFT-compatible MTT encoding, not a derivation of all physical states or measurement probabilities from admissibility alone.
author:
- Peter Nero
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: 43857ab4b9efbd06603cde2a8a84496589f01d112fa949428482926eb9538980
paper_id: entanglement-locality-and-measurement-from-coherent-sec-110e8cbe
release_state: zenodo_released
released_version: v2
title: Entanglement, Locality, and Measurement from Coherent Sector Dynamics
zenodo_doi: 10.5281/zenodo.21665963
zenodo_record_id: 21665963
zenodo_url: "https://zenodo.org/records/21665963"
---

# Version 2 Revision Note

Supersedes
*Entanglement, Locality, and Measurement from Coherent Sector Dynamics*, version 1.

Reason
The earlier paper restricted the state space without defining the coherent-preserving local algebra, treated that restriction as if it typically produced entanglement, and claimed branchwise entanglement reduction from local measurement and upper contraction without a valid entanglement monotonicity theorem.

Resolution
This version imports the fixed-point locality-descent theorem from its Foundation owner, defines the compressed local net, separates commutation from state factorization, makes Bell and temporal-Bell statements conditional on supplied states and instruments, and replaces branchwise disentanglement by the correct average LOCC monotonicity statement.

Retained result
Upper-local dynamics, nonseparable states, local instruments, Bell correlations, and operational no-signaling are mutually compatible under the declared AQFT and descent hypotheses.

Remaining boundary
MTT does not yet select every physically realized entangled state, derive a general Bell state and detector pair from one upper source, or derive arbitrary measurement probabilities and entanglement dynamics from admissibility alone.

# Introduction

Quantum entanglement is often presented as a tension between locality and correlation. Relativistic quantum field theory resolves this tension formally in the algebraic framework (AQFT), which enforces strict locality at the level of observable algebras while allowing highly entangled global states . AQFT thereby explains why entanglement does not permit superluminal signaling, but it does not select one physical state merely from the locality axioms. State preparation, interactions, and measurement instruments are additional physical data.

In Modal Triplet Theory (MTT), one candidate physical sector is a restricted class of states on the AQFT net induced by coherent configurations satisfying bounded geometry, a spectral gap, a bounded coherent projector, and declared stability margins . Measurement can then be represented by an ordinary localized quantum instrument, with disturbance and subsequent stabilization providing an MTT interpretation of that instrument . The companion Bell paper explains how upper-local dynamics can coexist with nonfactorizing states, but retains state and instrument selection as explicit obligations .

This paper provides a unified, AQFT-compatible formulation:

- We do *not* modify AQFT axioms (locality, isotony, time-slice).

- We define a candidate admissible class $`\mathcal{S}_{\mathrm{coh}}\subset\mathcal{S}(\mathcal{A})`$ induced by coherent-sector dynamics.

- We derive locality of the compressed observable net from the coherent-preserving upper algebra; restricting states alone is not the locality proof.

- We allow, but do not force, nonfactorizing states on commuting local algebras.

- We treat measurement by standard local completely positive instruments and separate their exact operational consequences from the MTT stabilization interpretation.

- We treat common-ancestor generation and Lieb–Robinson propagation as standard local mechanisms whenever their Hamiltonian hypotheses are supplied.

#### Concrete two-laboratory picture.

Let Alice’s observables lie in $`\mathcal A_4(O_A)`$ and Bob’s in $`\mathcal A_4(O_B)`$, with $`O_A`$ spacelike to $`O_B`$. Locality says $`[A,B]=0`$; it does not say $`\omega(AB)=\omega(A)\omega(B)`$. A singlet state is the familiar example: the operators commute across the laboratories, the joint state does not factorize, and local choices cannot signal. The MTT question is therefore not whether such algebraic data are consistent. It is whether one selected upper state and one selected descent produce the required lower state and detector instruments. This paper establishes the conditional framework for that question.

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

AQFT therefore answers the compatibility question, “How can entanglement exist without signaling?” It does not by itself select a particular nonfactorizing preparation.

# Coherent-sector admissibility as a state-selection principle

## Locality descent before state selection

Let $`\pi:M_{10}\to Y^4`$ be a bundle over the globally hyperbolic base and let
``` math
O\longmapsto\mathcal A_{10}(\pi^{-1}O)
```
be an upper net indexed by base regions. Let the coherent projector be decomposable over the base,
``` math
P=\int_{Y^4}^{\oplus}P_x\,d\mu(x).
```
The algebra that can be compressed without leaving the coherent sector is not the whole upper algebra. It is
``` math
\mathcal A_{10}^{P}(O)
 =\{A\in\mathcal A_{10}(\pi^{-1}O):[A,P]=0\}.
```
Define the compressed net on $`\operatorname{Ran}P`$ by
``` math
\mathcal A_4(O)
 =\{PAP|_{\operatorname{Ran}P}:A\in\mathcal A_{10}^{P}(O)\}.
```
The Fixed-Point Locality-Descent Theorem, proved in the Foundation paper, states that isotony descends and that upper commutation for spacelike separated base regions implies commutation of the compressed observables . The elementary identity is
``` math
[PAP,PBP]|_{\operatorname{Ran}P}
 =P[A,B]P|_{\operatorname{Ran}P},
```
which is valid because both observables commute with $`P`$. This is the locality proof used below. It transports an existing upper local relation; it does not create locality from an arbitrary nonlocal projector.

## Admissible state class

<div id="def:Scoh" class="definition">

**Definition 1** (Admissible (coherent) state class). Let $`\mathcal{S}(\mathcal{A}_4)`$ denote the space of states on the compressed net. Define $`\mathcal{S}_{\mathrm{coh}}\subset\mathcal{S}(\mathcal{A}_4)`$ to be the candidate subclass induced by coherent configurations for which:

1.  bounded geometry on time slabs;

2.  persistence of a uniform spectral gap separating coherent from noncoherent modes;

3.  boundedness of the coherent projector on Sobolev scales;

4.  local disturbance–damping stability margins (FCC) on the relevant invariant sets.

</div>

This definition is a domain restriction, not an existence or uniqueness theorem. For a physical application one must construct at least one upper state whose restriction gives a member of this class and show that the preparation dynamics selects it.

<div id="prop:locality-preserved" class="corollary">

**Corollary 2** (State restriction does not alter locality). *For every $`\omega\in\mathcal{S}_{\mathrm{coh}}`$, the commutation relations of the descended net remain those established by locality descent.*

</div>

<div class="proof">

*Proof.* Microcausality is a property of the algebra, independent of which positive normalized functional is evaluated on it. Restricting the state class cannot change an operator commutator. ◻

</div>

## Nonfactorization as an allowed coherence constraint

<div id="prop:entanglement-coherence" class="proposition">

**Proposition 3** (Conditional nonfactorization). *Suppose an admissible upper state restricts to $`\omega\in\mathcal S_{\mathrm{coh}}`$ and the restriction of $`\omega`$ to $`\mathcal A_4(O_1)\vee\mathcal A_4(O_2)`$ is not separable in the sense of <a href="#eq:separable" data-reference-type="eqref" data-reference="eq:separable">[eq:separable]</a>. Then the descended state is entangled across $`O_1,O_2`$, while the local algebras still commute when the regions are spacelike separated.*

</div>

<div class="proof">

*Proof.* Entanglement is the failure of the separable representation <a href="#eq:separable" data-reference-type="eqref" data-reference="eq:separable">[eq:separable]</a>. Commutation follows independently from the locality-descent theorem. Neither statement supplies a signal from one region to the other. ◻

</div>

<div class="remark">

*Remark 4*. The proposition does not say that every admissible state is entangled. Calling nonfactorization a “global coherence constraint” is an MTT interpretation of a state already shown to be nonseparable; it is not a substitute for constructing that state.

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

**Proposition 5** (Conditional Bell compatibility). *Let $`\omega\in\mathcal{S}_{\mathrm{coh}}`$ and suppose selected observables $`A_i,B_j`$ give $`|S|>2`$. Then that violation is compatible with the microcausality of the descended net. It excludes the corresponding factorizable hidden-variable representation; it does not by itself exclude upper algebraic locality.*

</div>

<div class="proof">

*Proof.* Microcausality ensures $`[A_i,B_j]=0`$ but does not imply <a href="#eq:separable" data-reference-type="eqref" data-reference="eq:separable">[eq:separable]</a>. The CHSH bound $`2`$ follows from the additional factorization assumptions. Hence its violation conflicts with those assumptions, not with the operator commutators. Operational no-signaling requires the local-instrument hypotheses stated below. ◻

</div>

This is the status of the companion MTT Bell analysis: upper-local dynamics can coexist with lower nonfactorization, but a physical MTT realization must still emit the singlet state and detector instruments from one selected upper source .

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

**Proposition 6** (Conditional temporal witness). *For a specified sequential instrument, an observed value $`K>1`$ excludes the conjunction of macrorealism and noninvasive measurability used to derive <a href="#eq:LG" data-reference-type="eqref" data-reference="eq:LG">[eq:LG]</a>. If the instrument changes the later joint statistics, it supplies an explicit failure of the noninvasiveness premise. Coherent-sector admissibility alone does not determine the value of $`K`$.*

</div>

<div class="remark">

*Remark 7*. The MTT disturbance-and-stabilization language can model the invasive instrument, but a numerical violation still requires a prepared state, Hamiltonian or channel, measurement times, and outcome operators .

</div>

# Local measurement instruments and entanglement

Measurement is an ordinary localized physical interaction represented by a completely positive instrument $`\{\mathcal M_m\}`$, where each map is trace-nonincreasing and $`\sum_m\mathcal M_m`$ is trace preserving. In density-operator language,
``` math
\begin{equation}
\label{eq:instrument}
\rho \mapsto \rho_m'=\frac{\mathcal{M}_m(\rho)}{p_m},
\qquad p_m=\operatorname{Tr}(\mathcal M_m(\rho)),
\qquad
\mathcal{M}_m(\rho)=\sum_\alpha K_{m,\alpha}\rho K_{m,\alpha}^\ast.
\end{equation}
```
In an MTT realization, the Kraus operators and outcome maps must be derived from the localized interaction and stabilization dynamics; naming those stages does not determine the instrument .

<div id="prop:nosignal" class="proposition">

**Proposition 8** (Nonselective local no-signaling). *Let $`\Lambda_A=\sum_m\mathcal M_m`$ be trace preserving. For every bipartite state $`\rho_{AB}`$,
``` math
\operatorname{Tr}_A\!\left[(\Lambda_A\otimes I_B)(\rho_{AB})\right]
=\operatorname{Tr}_A\rho_{AB}.
```
Thus Bob’s unconditioned state is unchanged by Alice’s local instrument.*

</div>

<div class="proof">

*Proof.* The dual map $`\Lambda_A^\ast`$ is unital. For every Bob observable $`B`$,
``` math
\operatorname{Tr}\!\left[(\Lambda_A\otimes I)(\rho_{AB})(I\otimes B)\right]
 =\operatorname{Tr}\!\left[\rho_{AB}(\Lambda_A^\ast(I)\otimes B)\right]
 =\operatorname{Tr}\!\left[\rho_{AB}(I\otimes B)\right].
```
 ◻

</div>

<div id="prop:partial" class="proposition">

**Proposition 9** (Average entanglement monotonicity). *Let $`E`$ be an entanglement monotone satisfying strong monotonicity under local operations. For
``` math
p_m=\operatorname{Tr}[(\mathcal M_m\otimes I)(\rho_{AB})],
 \qquad
 \rho_{AB,m}=\frac{(\mathcal M_m\otimes I)(\rho_{AB})}{p_m},
```
one has
``` math
\sum_m p_m E(\rho_{AB,m})\le E(\rho_{AB}).
```
An individual postselected branch may have larger entanglement than the input; branchwise reduction is not a theorem.*

</div>

<div class="proof">

*Proof.* The displayed inequality is the strong LOCC monotonicity condition for an entanglement monotone . Postselection explains why no pointwise inequality in $`m`$ follows. ◻

</div>

The current q79 binary one-anchor recorder supplies one selected operational output law and exact second-moment capture descent on its declared commuting output algebra. That result does not yet construct arbitrary bipartite instruments or a general entanglement-decay law.

# Entanglement propagation: common ancestors and causal spreading

Entanglement can be created between subsystems that never directly interacted by local interactions with a third system.

## Mediated entanglement and entanglement swapping

Let $`A,B,C`$ be three subsystems. Suppose $`A`$ interacts locally with $`C`$ and later $`B`$ interacts locally with $`C`$. After tracing out $`C`$, $`\rho_{AB}`$ can become entangled even if $`A`$ and $`B`$ had no shared creation history.

In MTT language, $`C`$ may be called a *common coherence ancestor*. The mathematical mechanism is still the supplied sequence of local interaction channels; the label adds no nonlocal dynamics.

## Finite-speed spreading

In many-body and lattice models, locality of interactions implies Lieb–Robinson bounds : for observables $`A`$ and $`B`$ supported at distance $`d`$,
``` math
\begin{equation}
\label{eq:LR}
\|[A(t),B]\|\le C\,e^{-\mu(d-vt)}.
\end{equation}
```
This expresses a finite propagation cone for the stated lattice Hamiltonian. An MTT model inherits such a bound only after its local generator satisfies the corresponding Lieb–Robinson hypotheses. In a relativistic AQFT model, the relevant exact input is instead microcausality and, where supplied, hyperbolic propagation.

<div class="remark">

*Remark 10*. Equation <a href="#eq:LR" data-reference-type="eqref" data-reference="eq:LR">[eq:LR]</a> is a standard theorem under model-specific hypotheses, not a consequence of bounded geometry alone. It illustrates how correlations can spread through local interactions without superluminal signaling.

</div>

# What is explained and what is not

Under its declared hypotheses this framework:

- derives locality of the compressed coherent-preserving net;

- permits nonfactorizing states without confusing them with noncommuting spacelike observables;

- proves nonselective local no-signaling and average entanglement monotonicity for standard local instruments;

- makes Bell and temporal-Bell compatibility conditional on the supplied states, channels, and observables; and

- keeps common-ancestor and finite-speed propagation within standard local dynamics.

It does not prove that admissibility selects entanglement, determine a Bell-violating preparation, derive every measurement instrument, or produce a unique global history. Where asymptotic flatness fails, local algebras and states remain the appropriate framework.

# Conclusion

AQFT reconciles entanglement with locality by separating algebraic commutation from state factorization. MTT adds a candidate coherent-sector restriction and, through the already-proved locality-descent theorem, a precise route from an upper local net to a compressed local net. The result supports the intended upper-world reading of Bell correlations: local dynamics and global nonseparability can coexist. It does not remove the need to construct the selected state and instruments. Measurement remains an ordinary local physical process, governed by completely positive maps and their standard no-signaling and entanglement-monotonicity properties.

# Upper-Bundle Formulation and Interface Obligations

## The upper net is indexed by the causal base

The notation $`M_{10}`$ does not require six additional time directions. Let $`\pi:M_{10}\to Y^4`$ be the upper bundle over the causal base. Locality is assigned to base regions:
``` math
O\longmapsto\mathcal A_{10}(\pi^{-1}O).
```
If $`O_1,O_2\subset Y^4`$ are spacelike separated, the upper locality hypothesis is
``` math
[\mathcal A_{10}(\pi^{-1}O_1),
   \mathcal A_{10}(\pi^{-1}O_2)]=0.
```
Together with the decomposable projector and the algebra $`\mathcal A_{10}^P`$ defined in the main text, the Foundation locality theorem then gives the compressed local net. This paper uses that theorem; it does not reproduce or rename it.

## Upper states and lower nonfactorization

Let $`\omega_{10}`$ be a positive normalized functional on the upper algebra with support in the coherent sector. Its restriction to compressed observables defines
``` math
\omega_4(PAP|_{\operatorname{Ran}P})
 :=\omega_{10}(PAP),
 \qquad A\in\mathcal A_{10}^{P}(O),
```
provided this assignment is representation independent. Alternatively, a declared conditional expectation onto the compressed algebra may be used. These are the required state-descent data; an unspecified “natural lift” is not enough.

Neither a nonproduct invariant set nor a spectral gap proves that $`\omega_4`$ is entangled. Entanglement is established only after the restricted functional is shown to violate a separability criterion or an entanglement witness. Once that is done, the commutation calculation and the state nonfactorization remain logically independent.

## Why fixed-point contraction is not an entanglement theorem

An upper disturbance-and-relaxation model may have the schematic form
``` math
\begin{equation}
\label{eq:FP-measure}
 \Psi\longmapsto T_\tau(\Psi+\delta\Psi),
 \qquad T_\tau=P\Phi_\tau.
\end{equation}
```
A contraction estimate for $`T_\tau`$ controls distance in its declared configuration norm. It does not by itself control an entanglement monotone of a reduced density operator. To obtain such a statement one must supply:

1.  the map from upper configurations or states to the bipartite lower state;

2.  the localized outcome maps generated by the disturbance and relaxation;

3.  complete positivity, normalization, and domain control for those maps;

4.  the relation between the upper contraction metric and a chosen lower entanglement measure; and

5.  either an exact monotonicity theorem or a controlled error bound.

The q79 one-anchor recorder completes an operational probability interface on one restricted output algebra, but it does not yet provide this general bipartite interface.

## Common ancestors are local channels

For three systems $`A,B,C`$, sequential local interactions $`U_{AC}`$ and $`U_{BC}`$ can leave the reduced state
``` math
\rho_{AB}
 =\operatorname{Tr}_C\!\left[
 U_{BC}U_{AC}\rho_{ABC}U_{AC}^\ast U_{BC}^\ast
 \right]
```
nonseparable even when $`A`$ and $`B`$ never interact directly. Calling $`C`$ a common coherence ancestor is compatible with MTT, but the displayed local channels are the mechanism. Their causal ordering and support must be derived from the selected dynamics.

## Dependency and status table

<div class="center">

| Object | Status in this paper |
|:---|:---|
| Upper locality | Supplied hypothesis on the upper net |
| Locality descent | Imported exact theorem from the Foundation owner |
| Nonfactorizing state | Conditional on an explicitly restricted upper state |
| Bell violation | Conditional on selected state and observables |
| Local no-signaling | Exact for a nonselective local CPTP instrument |
| Entanglement change | Average monotonicity for a declared entanglement monotone |
| MTT measurement source | Exact only for the current restricted q79 recorder; general bipartite interface open |

</div>

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The locality discussion depends on algebraic commutation, state nonfactorization, and the supplied measurement model. The mapped open ledger proves none of these statements; it is recorded only to delimit later claims of complete MTT-to-physics descent.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

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

G. Vidal, Entanglement monotones, , 47:355–376, 2000.

P. Nero, The Projection–Admissibility Principle: Descent, Recovery, and Structural Constraints, Modal Triplet Theory preprint, 2026.

P. Nero, Fixed Points III: Disturbance–Damping Balance and Stability, Preprint, 2025.

P. Nero, Fixed Points V: Curvature Coupling and Admissibility Barriers, Preprint, 2025.

P. Nero, Fixed Points VI: Formal Synthesis and Physical Interpretations, Preprint, 2025.

P. Nero, Modal Triplet Theory: From MTT to Quantum Field Theory on Curved Spacetime, Preprint, 2025.

P. Nero, Measurement as Disturbance and Stabilization in Modal Triplet Theory, Preprint, 2025.

P. Nero, Temporal Bell Inequalities and Global Consistency, Preprint, 2025.

P. Nero, Modal Fixed Points, Bell’s Beables, and the Limits of Factorization, Preprint, 2025.

</div>
