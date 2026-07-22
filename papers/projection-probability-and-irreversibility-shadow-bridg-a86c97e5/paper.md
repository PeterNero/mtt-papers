---
abstract: |
  This corrected successor separates three mathematical questions that the earlier shadow-bridge paper conflated: whether upstairs dynamics descends to a deterministic shadow map, whether an upstairs state can be recovered from shadow data, and whether probability laws in measurement, black-hole radiation and cosmology have one selected common source. We prove the exact fiber-preservation criterion for descent and the injectivity-on-a-code criterion for exact recovery. These results correct the earlier right-inverse argument: a noninjective surjection may have a measurable section, while still failing to recover the lost state. We also prove that noninjective projection alone does not imply an arrow of time; a quotient is reversible when its fiber equivalence relation is invariant in both time directions. At the probabilistic level, one upper measure and three explicit outcome maps do yield three pushforwards, but arbitrary target weights can always be represented by basin sizes, so basin representation alone derives neither the Born rule, Hawking weights nor a cosmological measure. Measurement instruments and island constructions are consequently described as updates or recovery on restricted codes/algebras, not as global inverses. The three physical domains remain useful structural shadow bridges. Their theorem-level unification requires an MTT-selected upper measure, explicit pushforward maps and independent derivations of all three target laws.
author:
- Peter Nero
current_version: v3
date: |
  July 2026  
  Version 3
generated_from_main_tex_sha256: 619c935fea0a867af0a668eea6427a517e2d09b6fe02dbd885d143fb51b0ecfd
paper_id: projection-probability-and-irreversibility-shadow-bridg-a86c97e5
release_state: zenodo_released
released_version: v1.0
title: |
  Projection, Probability, and Irreversibility:  
  A Descent, Recovery, and Measure-Separation Framework for MTT Shadow Bridges
zenodo_doi: 10.5281/zenodo.18262041
zenodo_record_id: 18262041
zenodo_url: "https://zenodo.org/records/18262041"
---

# Correction and claim tiers

The paper studies an invertible upstairs flow and a many-to-one shadow description. It does not claim that the current MTT corpus has derived quantum measurement, black-hole evaporation or cosmological probabilities from one measure. The corrected claim tiers are:

1.  **Exact mathematics:** descent, reversibility, restricted recovery, pushforward and nonuniqueness theorems.

2.  **Established domain mathematics:** quantum instruments and code recovery, semiclassical Hawking radiation, and measures on declared cosmological model spaces.

3.  **MTT shadow bridges:** possible common structural interpretations, conditional on source maps that have not yet been selected.

The MTT geometry is denoted $`Y_4\times X_6`$. The local Circle–Lens–Nil filtration is not used as a literal product topology. No result below depends on identifying compact phase with physical time.

# Descent of upstairs dynamics

Let $`\mathcal X`$ and $`\mathcal Y`$ be standard Borel spaces, let $`P:\mathcal X\to\mathcal Y`$ be a measurable surjection, and let $`\Phi_t:\mathcal X\to\mathcal X`$ be a measurable bijection. Define the fiber equivalence relation
``` math
x\sim_P x'\quad\Longleftrightarrow\quad P(x)=P(x').
```

<div id="thm:descent" class="theorem">

**Theorem 1** (Descent theorem). *There exists a map $`T_t:\mathcal Y\to\mathcal Y`$ satisfying
``` math
\begin{equation}
 T_t\circ P=P\circ\Phi_t
\label{eq:descent}
\end{equation}
```
if and only if
``` math
\begin{equation}
 P(x)=P(x')\quad\Longrightarrow\quad
 P(\Phi_t x)=P(\Phi_t x')
\label{eq:fiber}
\end{equation}
```
for all $`x,x'\in\mathcal X`$. If it exists, $`T_t`$ is unique. It is measurable whenever the quotient map has the corresponding measurable factorization property.*

</div>

<div class="proof">

*Proof.* If $`T_t`$ exists, applying it to $`P(x)=P(x')`$ gives condition <a href="#eq:fiber" data-reference-type="eqref" data-reference="eq:fiber">[eq:fiber]</a>. Conversely, define $`T_t(y)=P(\Phi_t x)`$ for any $`x`$ with $`P(x)=y`$. Condition <a href="#eq:fiber" data-reference-type="eqref" data-reference="eq:fiber">[eq:fiber]</a> makes the definition independent of the representative. Surjectivity gives uniqueness. ◻

</div>

Thus a many-to-one shadow does not automatically possess autonomous shadow dynamics. When the fiber-preservation condition fails, two upstairs representatives of one shadow state have different shadow futures. The correct output is then a relation, stochastic kernel, memory-dependent evolution, or an enlarged state, not a single-valued $`T_t`$.

<div id="thm:reversible" class="theorem">

**Theorem 2** (Reversible quotient criterion). *Suppose $`\{\Phi_t\}_{t\in\mathbb R}`$ is a measurable group and the fiber relation is preserved by every $`\Phi_t`$, positive and negative. Then the descended maps form a group,
``` math
T_{t+s}=T_tT_s,\qquad T_t^{-1}=T_{-t}.
```
Consequently, noninjectivity of $`P`$ alone does not imply irreversible shadow dynamics or an arrow of time.*

</div>

<div class="proof">

*Proof.* Using surjectivity of $`P`$ and <a href="#eq:descent" data-reference-type="eqref" data-reference="eq:descent">[eq:descent]</a>,
``` math
T_{t+s}P=P\Phi_{t+s}=P\Phi_t\Phi_s=T_tP\Phi_s=T_tT_sP.
```
Therefore $`T_{t+s}=T_tT_s`$. Taking $`s=-t`$ gives the inverse. ◻

</div>

Irreversibility can arise if only a forward semigroup descends, if the retained description is repeatedly coarse-grained, if an environment is traced out, or if a boundary/initial condition selects one branch. Each requires its own theorem.

# Recovery is not a right inverse of a surjection

The earlier paper argued that noninjectivity forbids a right inverse. This is false. For example, $`P:\mathbb R\to[0,\infty)`$, $`P(x)=x^2`$, is noninjective but has the measurable section $`S(y)=\sqrt y`$ with $`P S=\mathrm{Id}`$. The section chooses a representative; it does not recover the sign of the original input.

Let $`\mathcal C\subseteq\mathcal X`$ be a declared code or admissible subset. At time $`t`$, exact state recovery means a map
``` math
R_t:P(\Phi_t\mathcal C)\to\Phi_t\mathcal C
```
such that
``` math
R_t(P(\Phi_t x))=\Phi_t x\qquad(x\in\mathcal C).
```

<div id="thm:recovery" class="theorem">

**Theorem 3** (Exact restricted-recovery theorem). *An exact recovery map $`R_t`$ exists if and only if $`P|_{\Phi_t\mathcal C}`$ is injective. If $`\Phi_t\mathcal C`$ is Borel, the spaces are standard Borel and $`P|_{\Phi_t\mathcal C}`$ is a Borel injection, then its inverse on the image is Borel measurable.*

</div>

<div class="proof">

*Proof.* If $`R_t`$ exists and $`P(z)=P(z')`$ for $`z,z'\in\Phi_t\mathcal C`$, then $`z=R_tP(z)=R_tP(z')=z'`$. Conversely, injectivity defines the inverse of the restriction. The measurable statement is the standard Borel injection theorem. ◻

</div>

<div class="corollary">

**Corollary 4** (No global recovery after a collision). *If two distinct states in the declared code have the same shadow image, no recovery map can restore both. A section may still return one representative, but cannot be an inverse on the original code.*

</div>

This is the correct mathematical form of an admissibility barrier: either descent fails because a fiber splits into different shadow futures, or recovery fails because the shadow channel identifies distinct code states. Gap closure or projector discontinuity may cause such a failure, but the failure must be checked rather than inferred from terminology.

# Quantum channels and restricted codes

Let $`\mathcal N`$ be a completely positive trace-preserving channel and let $`\mathcal C`$ now denote a set of density operators on a code subspace.

<div id="prop:channel" class="proposition">

**Proposition 5** (Channel recovery obstruction). *If there are distinct $`\rho,\sigma\in\mathcal C`$ with $`\mathcal N(\rho)=\mathcal N(\sigma)`$, no channel $`\mathcal R`$ can satisfy $`\mathcal R\mathcal N(\omega)=\omega`$ for every $`\omega\in\mathcal C`$. Exact recovery is therefore a code-relative property, not a global consequence of projection.*

</div>

<div class="proof">

*Proof.* Applying a purported recovery channel to the equality would give $`\rho=\sigma`$. ◻

</div>

For a finite-dimensional quantum code and noise operators $`E_a`$, the Knill–Laflamme conditions 
``` math
P_{\mathcal C}E_a^\dagger E_bP_{\mathcal C}=\alpha_{ab}P_{\mathcal C}
```
are the standard necessary and sufficient conditions for exact correction of the declared error set. Island and entanglement-wedge reconstruction should be compared with this restricted algebra/code language. They are not global inverses from all radiation states to a unique microscopic bulk state.

## Measurement instruments are updates

A quantum instrument is a family of completely positive trace-nonincreasing maps $`\{\mathcal I_i\}`$ whose sum is trace preserving. Its probabilities and conditional states are
``` math
p_i=\mathop{\mathrm{Tr}}\mathcal I_i(\rho),\qquad
 \rho_i=\frac{\mathcal I_i(\rho)}{p_i}\quad(p_i>0).
```
This is a selected operational law. It is not a right inverse of premeasurement dynamics. Projection language may encode the outcome partition, but it does not derive the instrument, the Born functional, or objective single-outcome collapse.

# Coarse graining and entropy

Information loss, entropy growth and dynamical noninvertibility are related but not identical.

<div id="prop:entropy" class="proposition">

**Proposition 6** (No entropy arrow from noninjectivity alone). *A noninjective channel or shadow map does not by itself imply monotonic increase of von Neumann entropy. Unital quantum channels do not decrease entropy in finite dimension, but general nonunital channels may decrease it. Likewise, Theorem <a href="#thm:reversible" data-reference-type="ref" data-reference="thm:reversible">2</a> provides noninjective projections with reversible quotient dynamics.*

</div>

<div class="proof">

*Proof.* The unital statement follows from majorization. As a counterexample for general channels, amplitude damping sends every state asymptotically to a pure ground state, so some mixed-state entropies decrease. The reversible quotient statement follows from Theorem <a href="#thm:reversible" data-reference-type="ref" data-reference="thm:reversible">2</a>. ◻

</div>

A physical arrow therefore needs additional input: an initial-condition asymmetry, a dissipative semigroup, repeated coarse graining, a bath state, or a branch selection rule. The current MTT branch axiom may serve as such input only after its physical source and compatibility conditions are proved.

# One upper measure and three pushforwards

Let $`(\mathcal X,\Sigma,\mu)`$ be a probability space and let $`O_j:\mathcal X\to\mathcal Y_j`$ be measurable maps for $`j\in\{\mathrm{meas},\mathrm{BH},\mathrm{cos}\}`$.

<div id="thm:push" class="theorem">

**Theorem 7** (Common-source pushforward theorem). *Each domain receives the probability measure
``` math
\nu_j=(O_j)_*\mu,\qquad
 \nu_j(A)=\mu(O_j^{-1}(A)).
```
For a finite outcome partition $`B_{j,a}=O_j^{-1}(\{a\})`$, its weights are $`\nu_j(a)=\mu(B_{j,a})`$.*

</div>

<div class="proof">

*Proof.* This is the definition of pushforward measure. Measurability makes inverse images events, and countable additivity and normalization are inherited from $`\mu`$. ◻

</div>

This theorem says exactly what a common basin measure would mean. To use it physically, one must provide the same explicit $`\mu`$ and all three selected maps. Merely writing three unrelated measures with the same symbol does not establish a common source.

<div id="thm:nonunique" class="theorem">

**Theorem 8** (Basin representation is not a derivation). *Let $`(p_1,\ldots,p_n)`$ be any probability vector. On the atomless probability space $`([0,1],\mathcal B,dx)`$ there exists a measurable partition $`[0,1]=B_1\sqcup\cdots\sqcup B_n`$ with $`dx(B_i)=p_i`$. There are generally infinitely many such partitions. Hence reproducing target probabilities as basin volumes has no predictive content unless the measure and basins are selected independently of those target probabilities.*

</div>

<div class="proof">

*Proof.* Let $`a_0=0`$ and $`a_i=\sum_{k\leq i}p_k`$, and take $`B_i=[a_{i-1},a_i)`$, with the final endpoint included. Measure-preserving rearrangements generate further partitions with the same weights. ◻

</div>

# The three probability laws remain distinct

## Born probabilities

For a density operator $`\rho`$ and projective outcomes $`\Pi_i`$, the Born weights are
``` math
p_i=\mathop{\mathrm{Tr}}(\rho\Pi_i).
```
Gleason’s theorem  shows, under its dimension and additivity hypotheses, that probability measures on the projection lattice have this density-operator form. It does not select $`\rho`$, an MTT outcome map, or a physical collapse mechanism. A basin model derives Born weights only if its independently selected pushforward is proved equal to this functional for all allowed states and measurement contexts.

## Hawking weights

Semiclassical Hawking occupation factors  arise from quantum-field mode propagation and Bogoliubov coefficients on a black-hole background. They are not a probability measure on the same sample space as a laboratory quantum instrument merely because both contain normalized weights. A common-source MTT theorem must construct $`O_{\mathrm{BH}}`$ and recover the temperature, greybody factors and state dependence, not insert them as basin labels.

Island formulae and entanglement-wedge reconstruction   provide entropy and recovery statements in declared gravitational/holographic settings. Their natural comparison here is restricted recovery on a code algebra. They do not establish the global MTT projection or a common Born–Hawking measure.

## Cosmological measures

A cosmological probability law requires a declared solution/history space, symplectic or other measure, gauge quotient, cutoff and conditioning prescription  . Even a canonical measure on a finite model can become ambiguous after regularization of an infinite ensemble. Inflationary attraction can change distributions dynamically but does not by itself select the initial measure. Therefore a cosmological basin map is another independent source obligation.

<div class="corollary">

**Corollary 9** (Measure-separation verdict). *The Born, Hawking and cosmological laws may be three pushforwards of one upper MTT measure, but the current corpus has not proved that statement. Until one $`(\mathcal X,\mu)`$ and three explicit maps are supplied, the relationship is a structural shadow bridge rather than theorem-level probability equivalence.*

</div>

# Computational irreducibility

<div id="prop:undecidable" class="proposition">

**Proposition 10** (Conditional undecidability transfer). *Suppose an MTT basin-membership problem is computably defined and there is a computable reduction from the halting problem to it. Then no algorithm decides membership for all admissible inputs.*

</div>

<div class="proof">

*Proof.* Such a decision algorithm, composed with the reduction, would decide the halting problem. ◻

</div>

This conditional proposition is exact but does not establish undecidability for a specific MTT barrier. That requires an explicit encoding and reduction. Complexity or sensitive dependence alone is insufficient.

# MTT promotion contract

A theorem unifying the three domains must emit:

1.  a selected upstairs measurable or quantum state space $`\mathcal X`$;

2.  one normalized measure/state $`\mu`$ selected without using the three target laws;

3.  a flow or channel and a proof of the descent condition on each claimed domain;

4.  explicit outcome maps $`O_{\mathrm{meas}},O_{\mathrm{BH}},O_{\mathrm{cos}}`$;

5.  a proof that their pushforwards equal the Born, Hawking and cosmological laws, including domain-specific corrections;

6.  declared code algebras and recovery maps for every island or measurement claim;

7.  an independent source of any time arrow or entropy monotonicity; and

8.  a computable reduction before any MTT undecidability claim is promoted.

The current finite $`q=79`$ operators, shared-circle candidate and preprojection language program may help construct these objects. They do not yet provide the selected measurement capture measure identified as open in the quantization audit.

# Version delta

Relative to the previous version, this successor:

- replaces the false no-right-inverse argument by the descent and exact-recovery theorems;

- distinguishes a measurable section from recovery of the original state;

- proves that a noninjective shadow can still have reversible quotient dynamics;

- treats POVM instruments and islands as updates or restricted code recovery;

- separates structural analogies from a common probability measure;

- proves the nonuniqueness of basin representations of arbitrary weights;

- no longer identifies Born, Hawking and cosmological weights without one upper measure and three derived pushforwards;

- makes entropy growth and the time arrow independent source obligations; and

- reduces computational irreducibility to a conditional transfer theorem pending an explicit MTT reduction.

# Conclusion

Projection can hide information, obstruct autonomous descent, or prevent recovery, but these are different statements. The corrected mathematics identifies exactly which one holds. Likewise, basin measures can represent probabilities, but representation is not derivation. Measurement, black-hole reconstruction and cosmology remain genuinely suggestive MTT shadow bridges because all involve restricted observables, coarse descriptions and source-selection problems. Their strong unification is still open: it requires one selected upper measure and three independently computed pushforwards. This narrower formulation preserves the useful idea while making every future promotion testable.

<div class="thebibliography">

99 A. M. Gleason, *Measures on the closed subspaces of a Hilbert space*, Journal of Mathematics and Mechanics **6**, 885–893 (1957), doi:10.1512/iumj.1957.6.56050.

E. Knill and R. Laflamme, *A theory of quantum error-correcting codes*, Physical Review A **55**, 900–911 (1997), arXiv:quant-ph/9604034.

D. Petz, *Sufficient subalgebras and the relative entropy of states of a von Neumann algebra*, Communications in Mathematical Physics **105**, 123–131 (1986).

S. W. Hawking, *Particle creation by black holes*, Communications in Mathematical Physics **43**, 199–220 (1975), doi:10.1007/BF02345020.

G. W. Gibbons, S. W. Hawking and J. M. Stewart, *A natural measure on the set of all universes*, Nuclear Physics B **281**, 736–751 (1987), doi:10.1016/0550-3213(87)90425-1.

G. Penington, *Entanglement wedge reconstruction and the information paradox*, Journal of High Energy Physics **2020**, 2 (2020), arXiv:1905.08255.

A. Almheiri, N. Engelhardt, D. Marolf and H. Maxfield, *The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole*, Journal of High Energy Physics **2019**, 63 (2019).

</div>
