---
abstract: |
  This paper asks what Modal Triplet Theory (MTT) presently establishes about nonrelativistic quantum mechanics. We separate four questions that are often conflated: whether MTT can encode a quantum model, whether a coherent sector reconstructs its Hilbert-space dynamics, whether one selected MTT source emits the required operators and instruments, and whether the probability law is derived for every apparatus. A complete quantum-mechanical record is defined, including the complex Hilbert space, state cone, operator algebra, self-adjoint Hamiltonian and domain, unitary evolution, clock convention, composition rule, effects, instruments, and source certificates. The main theorem is conditional: if one selected upper MTT state emits this record and the evaluation diagram commutes, then MTT reconstructs the corresponding quantum theory on the declared domain. Projection alone does not create a complex structure, noncommutative observable algebra, self-adjoint Hamiltonian, tensor product, or probability law. We give sufficient closed-form and reducing-subspace conditions for an exact coherent-sector Hamiltonian, and we show why reproducing an arbitrarily supplied Schrodinger potential is an expressiveness result rather than a prediction. Time is treated as an evolution or clock parameter; the valid Mandelstam–Tamm relation replaces the former unsupported universal self-adjoint time operator. Gleason- and Busch-type theorems characterize probability assignments after Hilbert/effect structure and additivity are assumed; they do not source those assignments. A stronger positive result is available on one selected domain: the canonical $`q=79`$ binary one-anchor recorder gives an exact stopped output measure and second-moment Born descent on its commuting Fock output algebra, with no fitted probability or additional classical noise. General apparatus contexts, finite-bandwidth and non-Markov control, pre-quantum probability semantics, and objective single-history selection remain open. The result is therefore a rigorous coherent-sector reconstruction with one exact selected measurement domain, not a complete first-principles derivation of all quantum mechanics.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v4
date: Version 4, July 2026
generated_from_main_tex_sha256: 582ba1b90adaf594fcf10271b41d0f0bfc2ab6f2c03490747e233b549d626cb2
paper_id: modal-triplet-theory-from-mtt-to-quantum-mechanics
release_state: zenodo_released
released_version: v4
title: |
  Modal Triplet Theory and Nonrelativistic Quantum Mechanics:
  A Coherent-Sector Reconstruction and the Born-Source Boundary
zenodo_doi: 10.5281/zenodo.21708961
zenodo_record_id: 21708961
zenodo_url: "https://zenodo.org/records/21708961"
---

# Revision note: Version 4

<div class="description">

Version 4 supersedes Version 3 and its claims of a complete first-principles derivation of quantum mechanics, a universal MTT derivation of the Born rule, and automatic realization of arbitrary Schrodinger dynamics from the former ten-dimensional tri-product geometry.

The former paper combined valid standard operator theory with unsupported source claims. It did not distinguish an assumed complex Hilbert space from one derived by projection, treated bounded pullback as sufficient for closedness of an unbounded quadratic form, and reproduced an arbitrary target potential by inserting that same potential upstairs. It also used a self-adjoint time operator without establishing one, treated Gleason-type probability characterization as a physical source theorem, and inferred general POVMs, entanglement, and Lindblad dynamics from projection alone. The literal three-factor internal product used there is no longer the canonical MTT geometry.

This revision defines the complete lower quantum record and a typed, conditional reconstruction theorem. It states explicit hypotheses for complex, symplectic, self-adjoint, unitary, clock, composition, and instrument structures; separates exact compression from approximate elimination; replaces the time-operator claim by operational clock and Mandelstam–Tamm statements; and separates Gleason–Busch characterization from probability sourcing. Standard mathematical theorems retain their literature ownership.

Closed semibounded forms remain an appropriate route to self-adjoint Hamiltonians once their domains and closedness are proved. Stone’s theorem then supplies unitary evolution. Target-form matching remains a useful exact representation test. Quantum instruments, dilations, tensor products, semiclassical kernels, and weak-coupling master equations remain valid lower-level tools under their standard hypotheses. The canonical $`q=79`$ binary recorder adds a selected exact output-measure result on its declared domain.

The universal Born-source blocker remains open. The current exact result covers one selected binary $`P/Q`$ counting context with standard normal-state operational semantics. It does not yet cover arbitrary preparations and apparatuses, finite-bandwidth or non-Markov detectors, pre-quantum probability semantics, or selection of one uniquely actual history.

</div>

# The question in its correct order

Nonrelativistic quantum mechanics is not one equation. It is a coordinated mathematical structure. A state belongs to a complex Hilbert space or a density-operator cone; observables are represented by a generally noncommutative operator algebra; dynamics is generated by a self-adjoint Hamiltonian; composition uses a tensor product; and experiments are described by effects or instruments. These pieces constrain one another, but no one of them is identical to the others .

MTT begins with an upper state, admissibility conditions, reduction maps, and coherent or fixed sectors . It is therefore natural to ask whether a coherent sector can carry quantum mechanics. Four logically distinct questions must be kept apart:

1.  *Encoding.* Can a chosen quantum model be represented inside an MTT carrier?

2.  *Reconstruction.* If the required lower data are present, does MTT evaluation reproduce the same states, dynamics, and experiments?

3.  *Selection.* Does one selected MTT source emit those lower data without inserting the target theory by hand?

4.  *Universality.* Does the same source construction cover every allowed preparation, apparatus context, and limiting regime?

An exact answer to the first question can coexist with an open answer to the third. This is what happens when an arbitrary potential $`V`$ is placed upstairs and then recovered downstairs: the construction proves expressive capacity, not why nature selected $`V`$. Conversely, a selected result on one detector context is genuine source progress even when the universal apparatus theorem remains open.

The paper’s positive claims occupy two levels. The general theory is a conditional reconstruction. In addition, one selected $`q=79`$ recorder supplies an exact finite-domain probability and capture result. Nothing below promotes that recorder into a universal derivation.

# The complete quantum record

It is useful to say explicitly what must be supplied before a lower quantum theory exists. This prevents a projector, a spectrum, or a formal Schrodinger equation from silently standing in for the entire theory.

<div id="def:record" class="definition">

**Definition 1** (Nonrelativistic quantum record). A nonrelativistic quantum record is a tuple
``` math
\mathcal R_{\mathrm{QM}}
=
\bigl(
\mathcal H,\mathcal S,\mathcal A,\mathcal D,H,\hbar,U,\mathcal T,\mathcal E,\mathcal I,\boxtimes,\mathcal L,\mathcal X
\bigr)
```
with the following typed rows.

1.  $`\mathcal H`$ is a complex separable Hilbert space.

2.  $`\mathcal S`$ is a declared state space, for example the positive trace-class operators $`\rho`$ with $`\operatorname{Tr}\rho=1`$.

3.  $`\mathcal A`$ is a unital $`C^*`$- or von Neumann observable algebra represented on $`\mathcal H`$; unbounded observables are supplied with domains and affiliation data.

4.  $`\mathcal D\subset\mathcal H`$ is the dense form or operator domain needed below, and $`H`$ is a self-adjoint Hamiltonian, normally bounded below.

5.  $`\hbar>0`$ is the action normalization and $`U(t)=\exp(-itH/\hbar)`$ is the strongly continuous unitary evolution.

6.  $`\mathcal T`$ declares how time is used: as an external evolution parameter, as readings of a physical clock, or through a specified covariant clock POVM.

7.  $`\mathcal E`$ contains the effects or POVMs used by the allowed experiments, while $`\mathcal I`$ contains their completely positive instruments and record spaces.

8.  $`\boxtimes`$ is the composition rule, ordinarily $`\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B`$, together with the corresponding local algebras.

9.  $`\mathcal L`$ records locality, symmetry, superselection, and boundary conditions appropriate to the model.

10. $`\mathcal X`$ contains source and error certificates: which rows are selected by MTT, which are imported lower data, the domain on which the comparison is exact, and any residual or approximation bound.

</div>

The record is deliberately larger than $`(\mathcal H,H)`$. A Hamiltonian does not specify which instruments exist. A POVM does not specify the post-record state change. A real inner-product space does not yet specify multiplication by $`i`$. A tensor-product notation does not prove that the MTT source map respects subsystem locality.

Let $`\mathcal U_{\mathrm{adm}}`$ be the declared upper MTT domain. A partial source map
``` math
\mathcal S_{\mathrm{QM}}\colon
\mathcal U_{\mathrm{adm}}\dashrightarrow
\{\text{quantum records}\}
```
is allowed to be undefined when one or more rows cannot be emitted. This is preferable to filling a missing row with the desired lower object and calling the result a derivation.

# Conditional coherent-sector reconstruction

Suppose an upper MTT state $`z`$ has a coherent sector $`\mathcal H_{\mathrm{coh}}(z)`$, and let
``` math
\mathcal P_z\colon\mathcal H_{\mathrm{up}}(z)\longrightarrow
\mathcal H_{\mathrm{coh}}(z)
```
be its orthogonal coherent projector. The notation alone says only that $`\mathcal P_z^2=\mathcal P_z=\mathcal P_z^*`$. It does not say that the coherent range is complex, invariant under an upper Hamiltonian, closed under a chosen observable algebra, or equipped with a probability interpretation.

Let $`\operatorname{Eval}_{\mathrm{MTT}}(z,C)`$ denote the MTT prediction for an allowed preparation-and-apparatus context $`C`$. Let $`\operatorname{Eval}_{\mathrm{QM}}(\mathcal R,C)`$ denote the standard quantum evaluation of the record in <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">1</a>.

<div id="thm:conditional" class="theorem">

**Theorem 2** (Conditional MTT–QM reconstruction). *Fix an upper state $`z\in\mathcal U_{\mathrm{adm}}`$ and a declared family $`\mathfrak C_z`$ of contexts. Assume:*

1.  *$`\mathcal S_{\mathrm{QM}}(z)=\mathcal R_{\mathrm{QM}}(z)`$ is defined and every row of <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">1</a> needed by $`\mathfrak C_z`$ is present;*

2.  *the Hilbert identification $`J_z\colon\mathcal H_{\mathrm{coh}}(z)\to\mathcal H`$ is unitary and intertwines the declared state and observable maps;*

3.  *coherent evolution is exact, or carries a stated error:
    ``` math
    J_z\mathcal P_zU_{\mathrm{up}}(t)\iota_z
          =
          U(t)J_z+\mathcal E_t,
          \qquad \|\mathcal E_t\|\leq\varepsilon_t;
    ```*

4.  *every allowed upper instrument descends to the corresponding lower instrument, again exactly or with a declared norm bound; and*

5.  *MTT evaluation factors through the lower record:
    ``` math
    \operatorname{Eval}_{\mathrm{MTT}}(z,C)
          =
          \operatorname{Eval}_{\mathrm{QM}}
          \bigl(\mathcal R_{\mathrm{QM}}(z),C\bigr)+r_C
    ```
    with $`|r_C|\leq\delta_C`$.*

*Then MTT reconstructs the quantum model $`\mathcal R_{\mathrm{QM}}(z)`$ on $`\mathfrak C_z`$, exactly when $`\varepsilon_t=\delta_C=0`$, and with the displayed control otherwise.*

</div>

<div class="proof">

*Proof.* The source map supplies a well-typed lower record by (R1). Conditions (R2) and (R3) transport states, observables, and dynamics to the lower Hilbert space. Condition (R4) transports the operational contexts, including their record probabilities and conditional states. Substitution into (R5) gives the asserted equality or error bound for every context in $`\mathfrak C_z`$. No claim outside that context family follows. ◻

</div>

The theorem is intentionally simple. Its value is diagnostic. It turns the phrase “MTT gives quantum mechanics” into a finite list of diagrams that can succeed or fail separately. It also distinguishes a theorem of reconstruction from a theorem that selects the record’s numerical or operator entries.

# Complex, symplectic, and noncommutative structure

A complex Hilbert space can be viewed as a real Hilbert space equipped with a compatible complex structure. If $`g`$ is a real inner product and $`J^2=-\operatorname{Id}`$ with $`J`$ orthogonal, then
``` math
\omega(x,y)=g(Jx,y)
```
is symplectic, and $`g`$, $`J`$, and $`\omega`$ determine the corresponding complex inner product after a sign convention is fixed. Conversely, on a complex Hilbert space, multiplication by $`i`$ supplies $`J`$, while the real and imaginary parts of the inner product supply $`g`$ and $`\omega`$.

This equivalence explains why Hilbert and symplectic descriptions can agree. It does not explain where $`J`$ comes from. A real orthogonal projector $`P`$ has eigenvalues $`0`$ and $`1`$; by itself it does not define an operator squaring to $`-\operatorname{Id}`$. A selected MTT source must therefore emit a complex line, root-plane complex structure, polarization, or equivalent datum and prove that it descends to the same coherent sector.

The same caution applies to noncommutativity. Compression of an already noncommutative algebra can preserve noncommutativity, but projection alone does not generate the canonical commutation relations. If $`\mathcal A_{\mathrm{up}}\subset\mathcal B(\mathcal H_{\mathrm{up}})`$, the compressed operators
``` math
A_{\mathrm{coh}}=\mathcal PA\mathcal P\big|_{\operatorname{Ran}\mathcal P}
```
need not even form an algebra, because
``` math
(\mathcal PA\mathcal P)(\mathcal PB\mathcal P)
\neq
\mathcal PAB\mathcal P
```
unless suitable invariance conditions hold. The observable-algebra row in <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">1</a> is therefore an independent obligation, not a consequence of the word “coherent.”

# Hamiltonians from forms and exact compression

## The valid quadratic-form route

Closed semibounded quadratic forms are a robust way to construct self-adjoint Hamiltonians. The first representation theorem associates a unique self-adjoint lower-bounded operator with every densely defined closed semibounded form; KLMN controls suitable form-bounded perturbations . These are imported standard theorems. MTT must still prove their hypotheses for the selected form.

The old paper used a bounded pullback as if it automatically preserved closedness. That is false without additional control. The following sufficient condition is the one needed for an exact coherent restriction.

<div id="prop:closed-pullback" class="proposition">

**Proposition 3** (Closed reducing pullback). *Let $`q_{\mathrm{up}}`$ be a densely defined closed semibounded form on $`\mathcal H_{\mathrm{up}}`$. Let $`I\colon\mathcal H_{\mathrm{coh}}\to\mathcal H_{\mathrm{up}}`$ be an isometry with closed range $`M`$, let $`P_M`$ be the orthogonal projector onto $`M`$, and assume
``` math
P_M\mathcal D(q_{\mathrm{up}})\subset\mathcal D(q_{\mathrm{up}}).
```
Assume also that
``` math
I\mathcal H_{\mathrm{coh}}\cap\mathcal D(q_{\mathrm{up}})
=I\mathcal D_{\mathrm{coh}},
```
and assume $`M`$ reduces the form:
``` math
q_{\mathrm{up}}(x,y)=0
\quad
\text{for }
x\in M\cap\mathcal D(q_{\mathrm{up}}),\
y\in M^\perp\cap\mathcal D(q_{\mathrm{up}}).
```
Then
``` math
q_{\mathrm{coh}}(\psi,\phi)
=q_{\mathrm{up}}(I\psi,I\phi),
\qquad
\psi,\phi\in\mathcal D_{\mathrm{coh}},
```
is densely defined, closed, and semibounded whenever $`\mathcal D_{\mathrm{coh}}`$ is dense. Its represented Hamiltonian is unitarily equivalent to the part of the upper Hamiltonian on $`M`$.*

</div>

<div class="proof">

*Proof.* The isometry preserves the Hilbert norm and transports the form norm on $`\mathcal D_{\mathrm{coh}}`$ to the form norm on $`M\cap\mathcal D(q_{\mathrm{up}})`$. A form-Cauchy sequence downstairs therefore maps to a form-Cauchy sequence upstairs. Closedness of $`q_{\mathrm{up}}`$, closedness of $`M`$, and the domain identity return a limit in $`I\mathcal D_{\mathrm{coh}}`$. This proves closedness downstairs. Semiboundedness is inherited through the isometry. Form reduction gives an orthogonal form sum on $`M\oplus M^\perp`$, so the representation theorem identifies the lower operator with the upper operator part on $`M`$. ◻

</div>

The proposition is a sufficient theorem, not a claim that every coherent projector satisfies its assumptions. A bounded nonisometric map can lose the lower norm needed for completeness, while a nonreducing range couples retained and discarded modes.

## When a compression is exact

Let $`H_{\mathrm{up}}`$ be self-adjoint and $`P`$ an orthogonal projector. If $`P`$ commutes with every spectral projection of $`H_{\mathrm{up}}`$, then $`M=\operatorname{Ran}P`$ reduces $`H_{\mathrm{up}}`$. The restriction
``` math
H_M=H_{\mathrm{up}}\big|_{\mathcal D(H_{\mathrm{up}})\cap M}
```
is self-adjoint on $`M`$, and
``` math
Pe^{-itH_{\mathrm{up}}/\hbar}\big|_M
=e^{-itH_M/\hbar}.
```
This is exact coherent-sector dynamics.

Without reduction, $`PHP`$ is not automatically self-adjoint on the naively compressed domain, and $`Pe^{-itH_{\mathrm{up}}/\hbar}P`$ need not be a unitary group on $`M`$. In block form,
``` math
H_{\mathrm{up}}
=
\begin{pmatrix}
H_{MM} & V\\
V^* & H_{\perp\perp}
\end{pmatrix},
```
the coupling $`V`$ feeds discarded modes back into the coherent sector. At a resolvent parameter $`z`$, an exact elimination, where defined, uses the Schur–Feshbach expression
``` math
H_{\mathrm{eff}}(z)
=H_{MM}
-V(H_{\perp\perp}-z)^{-1}V^*.
```
It is energy dependent and is not the same object as $`H_{MM}`$. A genuine approximation must bound the resolvent, the coupling, and the relevant time or spectral window. This is why “project and evolve” is not a universal derivation of unitary lower dynamics.

# Representation is not prediction

The old reconstruction theorem allowed an arbitrary target
``` math
H_{\mathrm{target}}
=-\frac{\hbar^2}{2m}\Delta+V
```
and chose MTT background or boundary data containing the same $`V`$. Under appropriate Kato or form assumptions, this can be made mathematically exact. Its logical status is nevertheless representational.

<div id="prop:embedding" class="proposition">

**Proposition 4** (Exact target embedding). *Let $`q_{\mathrm{target}}`$ be any densely defined closed semibounded form on $`\mathcal H`$. Let $`q_\perp`$ be such a form on an auxiliary Hilbert space $`\mathcal K`$. On $`\mathcal H_{\mathrm{up}}=\mathcal H\oplus\mathcal K`$, define
``` math
q_{\mathrm{up}}=q_{\mathrm{target}}\oplus q_\perp
```
and let $`P`$ project onto $`\mathcal H`$. Then the coherent restriction of $`q_{\mathrm{up}}`$ is exactly $`q_{\mathrm{target}}`$, and its represented Hamiltonian is $`H_{\mathrm{target}}`$.*

</div>

<div class="proof">

*Proof.* The direct sum is closed and semibounded on the direct-sum form domain. The first summand reduces it. Applying <a href="#prop:closed-pullback" data-reference-type="ref+label" data-reference="prop:closed-pullback">3</a> to the canonical inclusion gives the result. ◻

</div>

This proposition is useful. It proves that the MTT carrier is not too small to represent the target class. It can also test a proposed decoder and normalization. It does not select $`m`$, $`V`$, the boundary condition, or $`\hbar`$, because all of them entered the source record. Prediction begins only when an upstream theorem emits those entries from data that did not already contain the desired answer.

# Unitary dynamics, clocks, and uncertainty

## Autonomous and time-dependent dynamics

For a self-adjoint $`H`$, Stone’s theorem gives the strongly continuous unitary group
``` math
U(t)=e^{-itH/\hbar}.
```
Thus unitarity follows after self-adjointness and the time parameter have been established, not from projection alone . For a time-dependent family $`H(t)`$, a propagator requires common-domain, stability, and regularity hypotheses of the appropriate Kato theorem . Writing $`H(t)`$ is not by itself an existence proof.

## Time is not automatically an observable

In standard nonrelativistic mechanics, $`t`$ usually labels evolution. It is not therefore represented by a universal self-adjoint operator conjugate to every semibounded Hamiltonian. If a physical clock is part of an experiment, the clock row $`\mathcal T`$ may instead contain a covariant POVM $`E_T`$ satisfying a declared covariance convention such as
``` math
U(s)E_T(B)U(s)^*=E_T(B+s).
```
The clock system, its coupling, resolution, and calibration must then be part of the source record.

The valid energy–time statement used here is operational. For a time-independent observable $`A`$, a state in the necessary domains, and
``` math
\tau_A
=
\frac{\Delta_\psi A}
{\left|\frac{\mathrm d}{\mathrm dt}\langle A\rangle_\psi\right|},
```
the Robertson inequality applied to $`A`$ and $`H`$, together with the Heisenberg equation, gives
``` math
\tau_A\,\Delta_\psi H\geq\frac{\hbar}{2}.
```
This is the Mandelstam–Tamm form: $`\tau_A`$ is a characteristic evolution time for a chosen observable, not the standard deviation of an assumed universal time operator . Other clock or quantum speed-limit statements require their own hypotheses.

## Ordinary observable uncertainty

For self-adjoint $`A`$ and $`B`$ on a common state domain,
``` math
\Delta_\psi A\,\Delta_\psi B
\geq
\frac12\left|
\langle\psi,[A,B]\psi\rangle
\right|.
```
This is a consequence of the Hilbert-space inner product and the supplied operators. It does not derive their commutator from an MTT projector. A complete MTT source theorem must identify the lower operators and prove that their commutator or Weyl relations descend from the same upper structure.

# Three probability questions

The word “Born rule” can refer to three different achievements.

1.  A *characterization theorem* says that a probability assignment satisfying specified additivity or noncontextuality assumptions has trace form.

2.  An *operational source theorem* constructs a physical instrument and its output law from selected dynamics and a supplied quantum state.

3.  A *pre-quantum or ontic theorem* explains why probability has that semantics before quantum states are accepted, or why one sample history is uniquely actual.

These are not equivalent.

## What Gleason and Busch establish

Gleason’s theorem begins with a countably additive measure on the projection lattice of a Hilbert space of dimension at least three and concludes, under its hypotheses, that the measure has density-operator trace form . Busch’s effect-algebra formulation similarly characterizes generalized probability assignments on effects . These theorems are fundamental because they show how little freedom remains once Hilbert/effect structure and the relevant additivity assumptions are accepted.

They do not construct a detector, derive countable additivity from MTT closure, or explain why a physical preparation is represented by a positive normal functional. Consequently one cannot start with an arbitrary “re-coherence weight,” assume it is additive on every orthogonal partition, invoke Gleason, and then count the result as an independent MTT derivation of probability. The additivity assumption is already a major part of the probability contract.

## Effects and instruments

A POVM $`E`$ on an outcome space $`\Omega`$ assigns positive operators $`E(B)`$ with $`E(\Omega)=I`$. Given a density operator $`\rho`$, standard quantum probability is
``` math
\Pr_\rho(B)=\operatorname{Tr}\bigl(\rho E(B)\bigr).
```
An instrument carries more information: each event $`B`$ has a completely positive trace-nonincreasing map $`\mathcal I_B`$, with
``` math
\Pr_\rho(B)=\operatorname{Tr}\mathcal I_B(\rho),
\qquad
\rho_B
=\frac{\mathcal I_B(\rho)}{\operatorname{Tr}\mathcal I_B(\rho)}
```
when the denominator is nonzero. Measurement is therefore an ordinary physical interaction followed by a durable or readable record. It does not require consciousness or a fundamental observer boundary.

Naimark and Stinespring dilation theorems show that POVMs and completely positive maps admit larger-space representations . They do not say that the required ancilla, isometry, pointer algebra, and coupling are selected by MTT. Those remain source rows.

# The selected $`q=79`$ binary recorder

The present research corpus contains one result stronger than abstract Gleason characterization. It constructs a selected recorder on a declared binary apparatus domain and computes its full stopped output measure. The canonical theorem and its machine-readable certificate are owned by the MTT QM source-proof repository at commit `1615da7e1b2c917556fe04a44d073b905644071e` . We summarize the result here without transferring the theorem’s ownership.

## Input data

Let
``` math
\mathcal H_\Sigma=L^2(\Sigma,\mathrm d\mu_h;F_{q79}),
\qquad
P=P_\Sigma,
\qquad
Q=I-P,
```
with $`P`$ and $`Q`$ orthogonal. The selected one-anchor intrinsic clock has
``` math
\gamma=\log 448,
```
and the two recorder couplings are
``` math
L_p=\sqrt{\gamma}\,P,
\qquad
L_q=\sqrt{\gamma}\,Q.
```
The environment is the two-channel symmetric Fock recorder with vacuum input. The selected preparation ensemble $`\lambda`$ enters through its second moment
``` math
\rho_\lambda
=\int |z\rangle\langle z|\,\mathrm d\lambda(z).
```
The output number processes generate a commuting nondemolition algebra, so restriction of the selected normal joint state to that algebra has a classical spectral measure. This is standard quantum-stochastic machinery applied to MTT-selected projector, clock, preparation, and context data .

## Exact output law

For a horizon $`u`$, let $`r_u`$ mean no count by $`u`$, and let $`(s,a)`$, $`a\in\{p,q\}`$, denote the first count at time $`s`$ in channel $`a`$. The imported selected-source result gives the effects
``` math
F_u(r_u)=e^{-\gamma u}I,
\qquad
F_u(\mathrm ds,a)
=\gamma e^{-\gamma s}P_a\,\mathrm ds,
```
where $`P_p=P`$ and $`P_q=Q`$. Therefore
``` math
\mu_{\rho,u}(r_u)=e^{-\gamma u},
\qquad
\mu_{\rho,u}(\mathrm ds,a)
=\gamma e^{-\gamma s}\operatorname{Tr}(\rho P_a)\,\mathrm ds.
```
Conditional on a count by time $`u`$,
``` math
\Pr_\rho(a\mid\text{count by }u)
=\operatorname{Tr}(\rho P_a).
```
No fitted probability vector and no independently appended classical Poisson process enter this selected output law.

The corresponding nonselective channel is
``` math
\Phi_u(\rho)
=P\rho P+Q\rho Q
+e^{-\gamma u}(P\rho Q+Q\rho P).
```
For two upper ensembles with the same second moment,
``` math
\rho_{\lambda_1}=\rho_{\lambda_2},
```
the complete stopped output measures agree. This is the exact second-moment capture descent proved on the canonical binary context.

At $`u=1`$, the no-count probability is $`1/448`$. For the first selected carrier basis preparation, the conditional label weights are
``` math
\bigl(\Pr(p),\Pr(q)\bigr)
=\left(\frac13,\frac23\right).
```
These numbers are outputs of the selected projector and clock in that context, not empirical fits.

## What this closes and what it does not

The result closes the following statement:

> Given standard normal-state operational semantics, the selected $`q=79`$ binary $`P/Q`$ recorder supplies its own stopped output measure and exact second-moment Born descent.

It does not derive the operational meaning of a normal state from a deterministic pre-quantum theory. A probability measure on the commuting output algebra is also not a distinguished character of that algebra and does not select one sample path as the uniquely actual history.

The universal source blocker therefore remains open for:

- arbitrary allowed apparatus contexts and outcome multiplicities;

- finite-bandwidth, detector-memory, and non-Markov corrections;

- a demanded pre-quantum derivation of probability semantics; and

- objective selection of one ontic history.

This boundary is not a defect in the exact binary theorem. It is the difference between a selected finite-domain result and a universal measurement theory.

# Composition, entanglement, and locality

Once the record supplies
``` math
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B,
```
entangled states are simply states that are not product states or mixtures of product states, according to the chosen purity level. Their existence is a consequence of the tensor-product state space. Projection may preserve, remove, or induce effective correlations depending on the embedding, but it does not by itself derive the tensor product or its physical subsystem meaning.

Local no-signalling likewise belongs to the operational algebra. If $`\Lambda_A`$ is a trace-preserving completely positive map acting only on $`A`$, then for a bipartite density operator
``` math
\operatorname{Tr}_A\bigl[(\Lambda_A\otimes\operatorname{Id}_B)(\rho_{AB})\bigr]
=\operatorname{Tr}_A\rho_{AB}.
```
Thus the statistics of $`B`$ are unchanged by an unconditioned local operation on $`A`$. Conditioning on a communicated outcome can change the conditional state, but not produce superluminal signalling.

An MTT account may seek an upper-local explanation of Bell correlations. To establish it, the source map must still show which upper variables, settings, and record algebras descend to the lower tensor factors while preserving the relevant statistical-independence assumptions. That separate Bell-locality question is not solved by merely calling the upper space local.

# Open systems and alternative representations

## Weak-coupling master equations

Completely positive Markov semigroups have generators of Gorini–Kossakowski–Sudarshan–Lindblad form under the standard bounded or finite-dimensional hypotheses . Davies’ weak-coupling limit gives a rigorous route from a system–reservoir model to such a semigroup under spectral, correlation, scaling, and limiting assumptions . These theorems do not imply that every MTT disturbance has a Markov limit.

The $`q=79`$ recorder in <a href="#sec:q79" data-reference-type="ref+label" data-reference="sec:q79">9</a> is a selected quantum-stochastic instrument on one declared domain. A general MTT open-system theorem would need to emit the reservoir state, interaction, correlation decay, renormalization, bandwidth regime, and approximation error. Memory effects are not failures of quantum mechanics; they indicate that a Markovian generator is not the correct reduced object.

## Path integrals and semiclassical kernels

When a self-adjoint Hamiltonian and suitable action are already available, Trotter product formulas, Feynman–Kac formulas in imaginary time, or oscillatory integral constructions can provide kernel representations. Stationary phase can then recover classical trajectories and Van Vleck-type amplitudes in an appropriate semiclassical regime. These are alternative representations or asymptotic consequences of supplied dynamics. They do not select the Hamiltonian or establish a measure for an arbitrary real-time path integral .

This distinction matters for MTT. A closure path or modal history can be a valuable upper description, but calling it a path integral does not make the quantum measure, phase, boundary condition, or continuum limit automatic.

# Two concrete tests

## A two-level recorder

Choose one normalized vector in $`\operatorname{Ran}P`$ and one in $`\operatorname{Ran}Q`$, and restrict the selected binary recorder to their span. In the resulting two-dimensional model, let
``` math
\mathcal H=\mathbb C^2,
\qquad
P=|0\rangle\langle0|,
\qquad
Q=|1\rangle\langle1|,
```
and prepare
``` math
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\qquad
|\alpha|^2+|\beta|^2=1.
```
The canonical recorder formulas give
``` math
\mu_{\psi,u}(\mathrm ds,p)
=\gamma e^{-\gamma s}|\alpha|^2\,\mathrm ds,
\qquad
\mu_{\psi,u}(\mathrm ds,q)
=\gamma e^{-\gamma s}|\beta|^2\,\mathrm ds.
```
Conditional on a count, the labels have weights $`|\alpha|^2`$ and $`|\beta|^2`$. This example is useful for two reasons. First, it shows exactly how the selected output instrument turns a coherent superposition into record statistics and dephasing. Second, the Hilbert space is two-dimensional, outside the direct scope of the original projection-lattice Gleason theorem. The result here comes from the instrument calculation, not from pretending that Gleason alone supplied the detector law.

## A harmonic oscillator embedding

Let
``` math
H_{\mathrm{osc}}
=-\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2}
+\frac12m\omega^2x^2
```
on its standard self-adjoint domain. By <a href="#prop:embedding" data-reference-type="ref+label" data-reference="prop:embedding">4</a>, it can be placed as a reducing block of a larger upper Hamiltonian and recovered exactly on the coherent summand. The eigenvalues and propagator then agree with ordinary quantum mechanics.

This is an excellent decoder test: a wrong normalization, domain, or intertwiner is exposed immediately. It is not a prediction of $`m`$ or $`\omega`$. Those values were part of the inserted target block. To turn the example into a selected MTT result, an upstream source theorem must emit the oscillator scale and coupling without using the target spectrum as construction data.

# Relation to the current MTT program

The canonical MTT foundation now uses a ten-dimensional bundle over a four-dimensional Lorentzian base with compact six-dimensional fiber, not a literal product of three independent internal manifolds . The shared finite line and root-plane complex structure provide promising upstream data for a complex coherent sector, but matching dimensions or finite carriers is not yet a continuum operator-intertwining theorem.

The current quantization audit records conditional quantization results and constructive finite-domain QFT results while retaining open capture, BRST/gauge-orbit, continuum, and full four-dimensional obligations. The present paper is consistent with that status:

1.  *General coherent-sector QM:* conditional reconstruction.

2.  *Selected binary output law:* exact on the canonical $`q=79`$ recorder domain.

3.  *Universal Born source:* open.

4.  *Nonperturbative QFT and continuum physics:* separate, open obligations not promoted here.

The possible upstream “closure repair” or nonlinear stabilization program would fit one level before this paper. If a selected nonlinear repair flow has a fixed state and its linearization produces the self-adjoint or dissipative operators in <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">1</a>, then the operator row would become a theorem rather than an input. That is a promising research direction, but no such universal source theorem is assumed in the present reconstruction.

# Claim disposition

<div class="description">

Withdrawn. The general result is a conditional coherent-sector reconstruction.

Must be emitted as a complex Hilbert space or as a real Hilbert space with a compatible selected complex structure. It is not derived from projection alone.

Retained when a selected densely defined closed semibounded form or self-adjoint operator and its domain are proved. Bounded pullback alone is insufficient.

Retained as a standard consequence of self-adjointness and Stone’s theorem. Time-dependent propagators remain conditional on their regularity hypotheses.

Retained as exact representability when the target form is inserted. This is not source selection or parameter prediction.

Part of the supplied operator algebra or a separate source theorem. It is not created by an orthogonal projector.

Gleason–Busch gives characterization under probability assumptions. Selected exact Born descent is established only for the canonical binary $`q=79`$ output context. The universal source theorem remains open.

Standard mathematical representations. MTT must separately source the ancilla, interaction, pointer algebra, and context.

Corrected to an operational clock or Mandelstam–Tamm statement. No universal self-adjoint time operator is claimed.

Available once the tensor-product composition rule is supplied. Projection alone does not derive physical subsystem composition.

Conditional on an explicit open-system or weak-coupling limit. Not every modal disturbance is Markovian.

An alternative or asymptotic representation after the Hamiltonian and action are supplied, not an independent source theorem.

</div>

# Completion contract

To upgrade the general reconstruction to a selected derivation, one upper source must emit and certify the following rows without empirical replay of the desired answer:

1.  one complex coherent Hilbert space and its state cone;

2.  one noncommutative observable algebra with domains and symmetries;

3.  one self-adjoint Hamiltonian or closed semibounded form, including $`\hbar`$, masses, couplings, and boundary conditions;

4.  a proof that the coherent range reduces the dynamics, or a controlled Schur–Feshbach/residual theorem when it does not;

5.  a clock convention and physical calibration distinct from a compact phase circle unless an explicit relation is proved;

6.  a tensor-product or algebraic composition rule with locality;

7.  selected effects, instruments, record algebras, and apparatus couplings;

8.  a same-source output-measure theorem for the entire allowed context family, including finite-bandwidth and memory error control;

9.  any requested pre-quantum probability semantics or objective-history rule; and

10. a commuting evaluation diagram with held-out predictions and an uncertainty budget.

The $`q=79`$ recorder closes a nontrivial part of item 8 for one binary context. It does not close the other rows by implication. Conversely, future progress on the upper action, operator naturality, or closure-repair flow could source several earlier rows at once. The contract makes such progress visible without changing the meaning of already closed results.

# Discussion

## What has actually been achieved

MTT can host a mathematically exact coherent-sector reconstruction of nonrelativistic quantum mechanics when the full lower record is supplied and the source/evaluation diagrams commute. The form and compression analysis specifies when the Hamiltonian is genuinely self-adjoint and when coherent evolution is exact. The target-embedding result establishes broad expressiveness while explicitly separating it from prediction.

More importantly, the current selected $`q=79`$ program goes beyond a bare encoding on one measurement domain. It fixes a projector pair, intrinsic rate, recorder unitary, commuting output algebra, and stopped instrument. The resulting first-count law depends only on the preparation’s second moment and has exact trace-form label probabilities. No observed probabilities or free stochastic noise are added. This is a real selected-source achievement, but its domain matters.

## Why the narrower statement is stronger science

The former version appeared stronger because it called many standard theorems MTT derivations. In fact, it made the decisive source question harder to see. The corrected statement is more useful: it identifies which structures are standard consequences, which are MTT-selected in a finite domain, and which remain open.

The distinction also prevents two opposite mistakes. It avoids declaring victory after replaying a target Hamiltonian, and it avoids discarding a genuine finite-domain theorem merely because universality is unfinished. Scientific progress can be exact and important without being global.

## Best next theorem

The immediate mathematical target is not another abstract Gleason argument. It is a same-source extension of the selected recorder theorem. One should enlarge the apparatus class, derive the corresponding output algebra and instrument from the same upper source, and prove second-moment capture descent with explicit control of detector bandwidth and memory. In parallel, a nonlinear closure-repair flow whose linearization emits the Hamiltonian and recorder couplings would move the source boundary further upstream.

# Conclusion

Projection is not quantization, and reconstruction is not selection. Nonrelativistic quantum mechanics requires a complex Hilbert space, state cone, operator algebra, self-adjoint dynamics, clock convention, composition rule, and operational instruments. Version 4 makes each of these rows explicit and proves the corresponding conditional MTT reconstruction theorem.

The operator-theoretic part is rigorous once its standard hypotheses are met. Closed reducing forms give self-adjoint coherent Hamiltonians; Stone’s theorem gives unitary evolution; and arbitrary target forms can be embedded exactly. That last fact measures expressive capacity, not predictive power. Time is treated through evolution or clock observables, and the valid Mandelstam–Tamm relation replaces an unsupported universal time operator. Gleason and Busch characterize probability assignments but do not source a detector law.

The canonical $`q=79`$ binary recorder supplies the paper’s strongest selected result: an exact stopped output measure and second-moment Born descent on one commuting Fock output domain, without fitted probabilities or extra classical noise. The universal apparatus theorem, non-Markov control, pre-quantum probability semantics, and objective actualization remain open. MTT therefore reaches a conditional reconstruction of general nonrelativistic quantum mechanics and an exact selected measurement theorem on one important domain. That is the correct present frontier.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The curated strict-upgrade ledger is used only as a corpus-state cross-check that stronger no-knob and universal-source obligations remain open. It does not prove this paper's Hilbert, Hamiltonian, clock, instrument, or probability statements. The exact canonical q79 binary output-measure theorem is instead cited at its immutable source-proof repository commit and remains restricted to its declared P/Q Fock-output domain.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
