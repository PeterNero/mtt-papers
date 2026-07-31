---
abstract: |
  This paper determines exactly what coherence-capacity data can and cannot establish about horizons and entropy in Modal Triplet Theory (MTT). A zero of a declared capacity certificate is a failure boundary for that certificate. It is not, by itself, an event horizon, a trapped surface, an entropy, or an arrow of time. Those notions require additional Lorentzian, state, algebraic, and dynamical data.

  The positive result is a typed conditional theorem. Let $`\Sigma`$ be a cross-section of a separately specified causal horizon. Suppose a selected model supplies an entropy-transfer density $`s_\Sigma`$, an integrated capacity-transfer density $`q_\Sigma`$, and constants $`\kappa,\sigma_{\max}\geq 0`$ such that
  ``` math
  0\leq s_\Sigma(x)\leq\kappa q_\Sigma(x),
    \qquad
    q_\Sigma(x)\leq\sigma_{\max}
  ```
  almost everywhere. Then
  ``` math
  \Delta S(\Sigma)\leq
    \kappa\sigma_{\max}\operatorname{Area}(\Sigma).
  ```
  Equality holds precisely when both inequalities saturate almost everywhere, up to null sets. Thus bounded capacity transport can support an area *upper bound*, but an area equality requires a saturation theorem. Reproducing black-hole entropy further requires an independent source for $`\kappa\sigma_{\max}=1/(4G\hbar)`$ in units $`c=k_{\mathrm B}=1`$. Capacity terminology alone does not derive that coefficient.

  Recovery is also formulated correctly. For an exterior channel $`\mathcal E_{\mathrm{ext}}`$, recovery means that a channel $`\mathcal R`$ reconstructs a declared code or observable algebra: $`\mathcal R\circ\mathcal E_{\mathrm{ext}}=\mathrm{Id}`$ on that domain. It is not a “partial right inverse” of a noninjective projection, and noninjectivity alone neither proves nor forbids code-relative recovery. Hawking radiation, generalized entropy, island formulas, and Page curves remain imported results of their established regimes. MTT contributes a common typed language and a finite source contract for connecting those results to an upper admissibility model.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, July 2026
generated_from_main_tex_sha256: f0b99c12301eb8b0514d1233de49f98ff0c051f1b6c8a1397ae75cbfb815fda3
paper_id: horizons-area-laws-and-entropy-from-coherence-capacity-b849ea71
release_state: zenodo_released
released_version: v3
title: |
  **Horizons, Capacity Bounds, and Entropy
  in Modal Triplet Theory:**
  A Conditional Interface with Black-Hole Thermodynamics
zenodo_doi: 10.5281/zenodo.21716284
zenodo_record_id: 21716284
zenodo_url: "https://zenodo.org/records/21716284"
---

# Version 3 revision note

#### Supersedes.

Version 2.0, DOI [10.5281/zenodo.18322069](https://doi.org/10.5281/zenodo.18322069).

#### Reason.

Version 2 identified a zero-capacity hypersurface with a horizon without supplying causal geometry, inferred a codimension-one barrier from an informal flux imbalance, defined entropy as lost capacity, and inferred monotonicity without a selected irreversible evolution. It also used an ill-typed “partial inverse” for recovery and promoted a bounded flux into black-hole entropy equality without deriving either saturation or the Bekenstein–Hawking coefficient.

#### Resolution.

Version 3 separates five objects that were previously conflated: capacity certificate, causal horizon, entropy functional, transport law, and recovery channel. It proves the surviving area upper bound with an exact equality criterion, makes all black-hole statements conditional on a separately supplied gravitational and quantum-field-theoretic model, and uses code-relative channel recovery.

#### Retained result.

The useful structural idea survives. A selected capacity record may control how well an exterior encoding transports or reconstructs information. If a same-source model also proves an entropy–capacity comparison, its finite transport density yields an area upper bound.

#### Remaining boundary.

MTT has not yet selected from one upper source a black-hole spacetime, Hadamard state, horizon algebra, renormalized generalized entropy, capacity current, entropy–capacity coefficient, saturation law, and decoder. In particular, the coefficient $`1/(4G\hbar)`$ remains downstream of the gravitational normalization and quantum theory.

# Introduction: the question being answered

The phrase “a horizon stores one bit per area” joins several different statements. General relativity supplies causal horizons. Quantum field theory on curved spacetime supplies Hawking radiation in a specified state and regime. Black-hole thermodynamics supplies an entropy with a particular coefficient. Quantum information theory supplies restricted channels, codes, and recovery criteria. MTT adds an upper/lower description and its admissibility certificates.

These structures can interact, but none should silently stand in for another. The purpose of this paper is therefore not to rederive black-hole thermodynamics from a scalar word called “capacity.” It is to answer a narrower and testable question:

> Under which explicit hypotheses can an MTT capacity record imply an area bound, and what additional data are needed to identify that bound with black-hole entropy?

The answer has three parts.

1.  A regular capacity zero set is only a certificate boundary.

2.  A bounded entropy-linked capacity flux gives an area upper bound.

3.  Black-hole equality and recovery require independent physical and channel-theoretic source data.

## In plain language

It helps to picture four instruments rather than one. A capacity certificate is a gauge showing how much reserve remains in a declared effective description. A causal horizon is a boundary drawn by the light-cone structure of spacetime. An entropy is an accounting rule defined from a physical state. A recovery channel is a procedure that tries to reconstruct selected information from an exterior record.

The old argument treated one gauge reading as though it supplied all four instruments. The corrected argument connects them only through explicit inequalities. If each unit of area can carry at most a fixed amount of capacity transfer, and each unit of that transfer controls at most a fixed amount of entropy transfer, then total entropy transfer is bounded by area. This explains why the upper bound is robust. It also explains why equality, the numerical coefficient, and information recovery are separate questions.

# Five distinct mathematical objects

## Capacity certificate

In the corrected capacity papers, coherence capacity is a normalized record of reserve in declared control rows, not a new conserved substance . Let
``` math
C:U\longrightarrow [0,\infty)
```
be one fixed normalized representative on a domain $`U`$. The statement $`C(x)>0`$ means only that the encoded estimates represented by this certificate retain positive reserve. The statement $`C(x)=0`$ means that at least one active row has reached its declared boundary.

A current $`J_C`$, diffusion equation, balance law, source, sink, or reset kernel is extra constitutive data. It does not follow from the existence of $`C`$.

## Causal horizon

Let $`(M,g)`$ be a time-oriented Lorentzian spacetime. An event horizon is a global causal boundary, for example
``` math
\mathcal H^+=\partial J^-(\mathcal I^+)
```
in an asymptotically predictable setting. Trapping horizons, Killing horizons, and causal horizons have related but distinct definitions. A regular event horizon need not be a local failure of field equations or of freely falling physics.

## Entropy

Entropy is defined from states, algebras, measures, or a thermodynamic limit. In a finite type-I setting one may use
``` math
S(\rho)=-\operatorname{Tr}(\rho\log\rho).
```
In local quantum field theory, local algebras are generally not finite matrix algebras, and relative entropy or a renormalized generalized entropy is often the appropriate object. The generalized entropy has the schematic form
``` math
S_{\mathrm{gen}}
  =
  \frac{\operatorname{Area}(\Sigma)}{4G\hbar}
  +S_{\mathrm{out}}
  +S_{\mathrm{ct}},
```
where the definition and counterterms belong to the chosen semiclassical theory. None of these functionals is defined by $`C=0`$.

## Transport

Suppose a selected or postulated model gives a capacity current $`J_C`$. For a horizon segment whose null generators meet a cross-section $`\Sigma`$, integrate the normal flux along each generator over the declared segment. This produces a nonnegative transfer density
``` math
q_\Sigma:\Sigma\longrightarrow[0,\infty).
```
Its units are capacity per area. Separately, let
``` math
s_\Sigma:\Sigma\longrightarrow[0,\infty)
```
be an entropy-transfer density derived from the chosen state and dynamics. Its integral is
``` math
\Delta S(\Sigma)=\int_\Sigma s_\Sigma\,\mathrm{d}A.
```
The two densities have different origins. Relating them requires a comparison theorem or constitutive hypothesis.

## Recovery

Let
``` math
\mathcal E_{\mathrm{ext}}:\mathcal S_{\mathrm{up}}\longrightarrow
  \mathcal S_{\mathrm{ext}}
```
be a completely positive trace-preserving channel, or use its unital Heisenberg dual on observable algebras. A recovery map is another channel with a declared domain of validity. It asks whether selected states or observables can be reconstructed after exterior restriction. This is not the same question as whether a set-theoretic section of a surjection exists.

# What a capacity zero set proves

<div id="prop:regular" class="proposition">

**Proposition 1** (Regular certificate boundary). *Let $`C\in C^1(U,\mathbb R)`$. If $`0`$ is a regular value of $`C`$, then
``` math
B_C=C^{-1}(0)
```
is a codimension-one embedded submanifold of $`U`$.*

</div>

<div class="proof">

*Proof.* This is the regular-value theorem. ◻

</div>

<div class="remark">

*Remark 2*. The conclusion is geometric but limited. It says nothing about whether $`B_C`$ is null, achronal, trapped, globally defined, or invariant under a physical evolution. Each of those properties needs further data.

</div>

<div id="prop:nohorizon" class="proposition">

**Proposition 3** (No horizon from imbalance alone). *An inward/outward capacity imbalance, without a specified evolution equation and causal geometry, does not imply the formation of a causal horizon.*

</div>

<div class="proof">

*Proof.* On $`M=\mathbb R\times\mathbb R^3`$, let $`C(t,x)=e^{-t}`$. The certificate decreases everywhere and remains positive for every finite $`t`$; no zero set forms. Alternatively, $`C(t,x)=1-t`$ reaches zero on the spacelike slice $`t=1`$, which is not an event horizon in Minkowski spacetime. Thus loss or exhaustion of a scalar record does not determine the causal type or global meaning of its zero set. ◻

</div>

To identify $`B_C`$ with a physical horizon, a model must at least supply a Lorentzian spacetime, a horizon definition, and an intertwining statement showing that the selected certificate boundary coincides with that causal object on the stated domain. Equality of sets is already a nontrivial theorem; matching generators, measures, connections, and dynamics is stronger.

# The conditional area-bound theorem

<div id="ass:interface" class="assumption">

**Assumption 4** (Typed horizon-capacity interface). The following data are fixed:

1.  a causal horizon cross-section $`\Sigma`$ with finite induced area;

2.  a measurable entropy-transfer density $`s_\Sigma\geq0`$;

3.  a measurable integrated capacity-transfer density $`q_\Sigma\geq0`$;

4.  constants $`\kappa,\sigma_{\max}\geq0`$ such that, almost everywhere,
    ``` math
    s_\Sigma\leq\kappa q_\Sigma,
        \qquad
        q_\Sigma\leq\sigma_{\max}.
    ```

</div>

<div id="thm:area" class="theorem">

**Theorem 5** (Capacity-controlled area upper bound). *Under <a href="#ass:interface" data-reference-type="ref+label" data-reference="ass:interface">4</a>,
``` math
\Delta S(\Sigma)
  \leq
  \kappa\sigma_{\max}\operatorname{Area}(\Sigma).
```*

</div>

<div class="proof">

*Proof.* Integrating the pointwise inequalities gives
``` math
\Delta S(\Sigma)
  =
  \int_\Sigma s_\Sigma\,\mathrm{d}A
  \leq
  \kappa\int_\Sigma q_\Sigma\,\mathrm{d}A
  \leq
  \kappa\sigma_{\max}\int_\Sigma\mathrm{d}A.
```
 ◻

</div>

<div id="thm:equality" class="theorem">

**Theorem 6** (Exact equality criterion). *Assume $`\kappa>0`$, $`\sigma_{\max}>0`$, and $`\operatorname{Area}(\Sigma)<\infty`$. Equality in <a href="#thm:area" data-reference-type="ref+label" data-reference="thm:area">5</a> holds if and only if
``` math
s_\Sigma=\kappa q_\Sigma
  \quad\text{and}\quad
  q_\Sigma=\sigma_{\max}
```
almost everywhere on $`\Sigma`$.*

</div>

<div class="proof">

*Proof.* Define the nonnegative deficits
``` math
d_1=\kappa q_\Sigma-s_\Sigma,
  \qquad
  d_2=\kappa(\sigma_{\max}-q_\Sigma).
```
The gap in <a href="#thm:area" data-reference-type="ref+label" data-reference="thm:area">5</a> is
``` math
\kappa\sigma_{\max}\operatorname{Area}(\Sigma)
  -\Delta S(\Sigma)
  =
  \int_\Sigma(d_1+d_2)\,\mathrm{d}A.
```
It vanishes exactly when both nonnegative deficits vanish almost everywhere. ◻

</div>

<div class="corollary">

**Corollary 7** (Strictness on an unsaturated set). *If either comparison is strict on a measurable subset of positive area, then the area bound is strict.*

</div>

<div class="proof">

*Proof.* At least one nonnegative deficit has strictly positive integral. ◻

</div>

## What the coefficient means

The product $`\kappa\sigma_{\max}`$ contains two independent pieces: $`\kappa`$ converts the declared capacity transfer into an entropy bound, while $`\sigma_{\max}`$ bounds capacity transfer per area. Rescaling an unnormalized capacity representative would rescale these factors. A physical coefficient therefore requires a normalized source convention and a derivation that is invariant under all allowed changes of representative.

In units $`c=k_{\mathrm B}=1`$, black-hole entropy is
``` math
S_{\mathrm{BH}}
  =
  \frac{\operatorname{Area}(\Sigma)}{4G\hbar}
  \cite{Bekenstein1973,Hawking1975,GibbonsHawking1977}.
```
The capacity theorem reproduces this equality only if a same-source model proves both saturation conditions and
``` math
\kappa\sigma_{\max}=\frac{1}{4G\hbar}.
```
Using the observed or imported value on the right is a matching condition, not an MTT derivation.

# Entropy is not lost capacity

The former definition “entropy equals irreversibly shed capacity” hid three assumptions: that capacity is additive, that its loss is irreversible, and that it agrees with a state entropy. None follows from the certificate definition.

<div id="prop:noentropy" class="proposition">

**Proposition 8** (Capacity exhaustion does not imply entropy growth). *There is no universal implication
``` math
C(t_2)<C(t_1)
  \quad\Longrightarrow\quad
  S(\rho_{t_2})\geq S(\rho_{t_1})
```
without a law linking $`C`$ to the state dynamics.*

</div>

<div class="proof">

*Proof.* Let $`\rho_t=\lvert0\rangle\langle0\rvert`$ be a fixed pure state, so $`S(\rho_t)=0`$ for all $`t`$, and choose any decreasing positive certificate $`C(t)`$. Capacity decreases while entropy is constant. Conversely, one may keep $`C`$ constant while a selected noisy channel increases the entropy of a finite-dimensional state. Therefore neither quantity determines the other. ◻

</div>

There is nevertheless a rigorous information-theoretic monotonicity available once a channel is supplied. Quantum relative entropy obeys the data-processing inequality
``` math
D(\mathcal E(\rho)\Vert\mathcal E(\sigma))
  \leq
  D(\rho\Vert\sigma)
```
for a completely positive trace-preserving map $`\mathcal E`$ . This is loss of distinguishability under a declared channel. It is not a theorem that every von Neumann entropy increases, and it is not sourced by $`C=0`$.

# Recovery on an exterior code

<div class="definition">

**Definition 9** (Exact code-relative recovery). Let $`\mathfrak C\subseteq\mathcal S_{\mathrm{up}}`$ be a declared code of states. The exterior channel $`\mathcal E_{\mathrm{ext}}`$ is exactly recoverable on $`\mathfrak C`$ if there exists a channel $`\mathcal R:\mathcal S_{\mathrm{ext}}\to\mathcal S_{\mathrm{up}}`$ such that
``` math
\mathcal R\circ\mathcal E_{\mathrm{ext}}(\rho)=\rho
  \qquad
  \text{for every }\rho\in\mathfrak C.
```

</div>

<div class="definition">

**Definition 10** (Observable-algebra recovery). For a declared upper observable algebra $`\mathcal A_{\mathrm{code}}`$, recovery means that the Heisenberg maps reproduce expectation values of every $`A\in\mathcal A_{\mathrm{code}}`$ on the declared state family, exactly or within a stated error.

</div>

<div class="proposition">

**Proposition 11** (Noninjectivity is not the criterion). *Noninjectivity of $`\mathcal E_{\mathrm{ext}}`$ on the full upper state space does not preclude exact recovery on a smaller code. Conversely, the existence of a set-theoretic right inverse on the image does not establish a physical recovery channel.*

</div>

<div class="proof">

*Proof.* If the restriction of $`\mathcal E_{\mathrm{ext}}`$ to $`\mathfrak C`$ is reversibly encoded, a recovery channel can exist even when states outside $`\mathfrak C`$ are identified. In the other direction, a set-theoretic section need not be linear, completely positive, trace-preserving, local, stable, or compatible with the dynamics. It therefore need not be a physical decoder. ◻

</div>

This is the correct mathematical setting for the analogy with entanglement-wedge reconstruction. In holographic models, reconstruction is code- and algebra-relative . It is not recovery of an arbitrary microscopic history from an exterior record.

# Black holes, Hawking radiation, and islands

## What is imported

Hawking radiation is a result of quantum field theory on a black-hole background with a specified quantum state and asymptotic mode interpretation . The area term is fixed by the gravitational normalization and quantum theory . These are physical inputs to the present interface, not consequences of capacity language.

Island and quantum-extremal-surface calculations reproduce Page-curve behavior in controlled semiclassical and holographic models . Their content depends on the generalized-entropy functional, the path-integral or holographic regime, the chosen state, and the radiation algebra. They do not automatically select an MTT upper projection.

## The legitimate MTT interpretation

MTT may interpret an exterior restriction as a lower encoding of a larger state. A capacity record can then measure one declared reserve for that encoding, such as spectral separation, decoder stability, or control of a projection chart. The interpretation becomes a theorem only when one constructs the commuting diagram
``` math
\begin{CD}
  \mathcal S_{\mathrm{up}} @>{\Phi_t}>> \mathcal S_{\mathrm{up}}\\
  @V{\mathcal E_{\mathrm{ext}}}VV @VV{\mathcal E_{\mathrm{ext}}}V\\
  \mathcal S_{\mathrm{ext}} @>>{\phi_t}> \mathcal S_{\mathrm{ext}}
\end{CD}
```
on a stated domain, together with the state, horizon geometry, entropy functional, capacity normalization, and recovery criterion.

The diagram distinguishes three outcomes:

1.  *descent*: exterior dynamics $`\phi_t`$ is autonomous;

2.  *recovery*: a decoder reconstructs a declared code or algebra;

3.  *information comparison*: a chosen entropy or relative entropy obeys a proved inequality.

None is implied by the other two.

# The corrected theorem

<div id="thm:mtt" class="theorem">

**Theorem 12** (Conditional MTT horizon-capacity theorem). *Assume:*

1.  *a selected Lorentzian model supplies a causal horizon and cross-section $`\Sigma`$;*

2.  *a selected quantum model supplies the state, exterior algebra or channel, and entropy-transfer density $`s_\Sigma`$;*

3.  *a normalized MTT capacity record and constitutive dynamics supply $`q_\Sigma`$;*

4.  *the two source chains are connected by the comparison and flux bounds of <a href="#ass:interface" data-reference-type="ref+label" data-reference="ass:interface">4</a>.*

*Then the entropy transfer obeys the area upper bound of <a href="#thm:area" data-reference-type="ref+label" data-reference="thm:area">5</a>. If, in addition, the two saturation conditions of <a href="#thm:equality" data-reference-type="ref+label" data-reference="thm:equality">6</a> and $`\kappa\sigma_{\max}=1/(4G\hbar)`$ are derived from the same selected source, the bound agrees with the Bekenstein–Hawking area equality on that domain.*

</div>

<div class="proof">

*Proof.* The upper bound is <a href="#thm:area" data-reference-type="ref+label" data-reference="thm:area">5</a>; equality is <a href="#thm:equality" data-reference-type="ref+label" data-reference="thm:equality">6</a>; the coefficient identification is the final stated hypothesis. ◻

</div>

<div class="remark">

*Remark 13*. The theorem is intentionally conditional. Its value is that every missing bridge has a type and a source obligation. It cannot be promoted by renaming capacity as entropy or by fitting the final coefficient.

</div>

# Current MTT status

<div class="center">

| Object | Status | Meaning for this paper |
|:---|:---|:---|
| Normalized capacity record | Established conditionally | A declared reserve can be computed from supplied control rows; it is not automatically conserved or physical. |
| Regular zero-set theorem | Exact | $`C^{-1}(0)`$ is a hypersurface only under the regular-value hypothesis. |
| Capacity transport | Constitutive | A current, balance law, and coefficients must be selected or postulated. |
| Capacity-to-entropy comparison | Open | No same-source theorem currently emits $`s_\Sigma\leq\kappa q_\Sigma`$ for a physical black-hole sector. |
| Area upper bound | Exact conditional | Follows by integration once the typed densities and bounds are supplied. |
| Black-hole equality | Imported | Requires saturation and the independent coefficient $`1/(4G\hbar)`$. |
| Exterior recovery | Model-dependent | Must be stated on a code or observable algebra with a physical decoder. |
| Nonperturbative MTT QFT | Open | The selected full interacting state, renormalized transport, and horizon completion remain unresolved. |

</div>

# Research program

The corrected paper turns a vague area-law claim into a finite program.

1.  **Select the gravitational background.** Derive or declare the Lorentzian metric, causal horizon, cross-sections, and measure from the same upper branch.

2.  **Select the quantum state.** Construct the field algebra, Hadamard state or other admissible state, exterior/radiation restriction, and renormalized entropy functional.

3.  **Derive capacity dynamics.** Supply a normalized capacity record, current, source terms, units, and horizon transfer density from a selected action or controlled reduction.

4.  **Prove the comparison.** Establish $`s_\Sigma\leq\kappa q_\Sigma`$ with a sourced $`\kappa`$, rather than declaring capacity to be entropy.

5.  **Decide saturation.** Determine whether either deficit in <a href="#thm:equality" data-reference-type="ref+label" data-reference="thm:equality">6</a> vanishes. Generic bounded transport gives only a strict inequality.

6.  **Source the coefficient.** Derive $`G`$, $`\hbar`$, field normalization, and counterterms on the same branch. Numerical agreement after importing $`G`$ is a consistency check, not a prediction.

7.  **Construct recovery.** Publish the code or algebra, decoder channel, error norm, state domain, and compatibility with dynamics.

8.  **Compare observables.** Recover Hawking flux, generalized entropy, and Page-curve observables with a declared uncertainty and regime.

# Discussion

## Why the correction strengthens the idea

The old argument was attractive because it appeared to obtain several features at once: horizon, entropy, area scaling, and irreversibility. That compression was also its weakness. A scalar failure certificate cannot carry all those meanings without additional maps.

The corrected result is smaller but reusable. It applies to any model in which an independently defined entropy transfer is controlled by a bounded resource transfer. It also shows exactly where black-hole physics enters: causal geometry identifies the horizon; QFT and gravity define the entropy; MTT supplies a possible upper source and capacity control; the comparison theorem connects them.

## What would count as a major advance

A major MTT advance would not be another area-shaped plot or a fitted coefficient. It would be one same-source construction that emits:
``` math
\begin{gathered}
  (M,g,\mathcal H^+),\qquad
  (\mathcal A_{\mathrm{ext}},\omega,\mathcal E_{\mathrm{ext}}),\\
  (C,J_C,q_\Sigma),\qquad
  (S_{\mathrm{gen}},s_\Sigma),\qquad
  (\kappa,\sigma_{\max},\mathcal R),
\end{gathered}
```
and proves the commuting, comparison, saturation, and recovery statements. That would turn the present conditional interface into a derived black-hole sector.

## Relation to companion MTT papers

The normalized definition and invariance warnings belong to the capacity paper . Constitutive transport, first exit, and the absence of automatic horizon or entropy deductions belong to the dynamics paper . Descent, recovery, and measure separation belong to the shadow-bridge paper . The black-hole/measurement comparison is handled as a channel analogy in . The projection-first quantum-gravity paper supplies the broader programmatic context . This paper owns only the corrected horizon-capacity interface and the area-bound/equality analysis.

# Conclusion

Coherence capacity does not, by itself, create a horizon or define an entropy. A capacity zero set is a boundary of a declared certificate. A physical horizon requires Lorentzian causal data; entropy requires a state and functional; irreversibility requires a dynamical or thermodynamic theorem; recovery requires a channel and a code.

Once those types are respected, a clean theorem survives. If entropy transfer is bounded by capacity transfer and capacity transfer is bounded per unit area, entropy obeys an area upper bound. Equality is equivalent to almost-everywhere saturation of both bounds. Agreement with Bekenstein–Hawking entropy additionally requires the independently derived coefficient $`1/(4G\hbar)`$.

The achievement is therefore not a derivation of black-hole entropy from a metaphor. It is a rigorous interface showing precisely how such a derivation would have to work, which steps are elementary, and which physical source theorems remain open.

# Computational evidence and reproducibility

This paper proves analytic inequalities and type-correction statements. It uses no numerical MTT packet as evidence for a horizon, entropy functional, saturation law, or black-hole coefficient. The current research-status ledger and reproducibility repository are available at <https://github.com/PeterNero/mtt-results-repro>; they are cited here only to make the open source boundary auditable, not as proof of the local theorems.
