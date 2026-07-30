---
abstract: |
  This paper asks a deliberately narrower question than its predecessor: when does a Modal Triplet Theory (MTT) description reconstruct the standard nonrelativistic de Broglie–Bohm dynamics? We first specify the complete lower pilot–wave record. In addition to a complex Hilbert space and self-adjoint Schrodinger Hamiltonian, that record contains a physical configuration manifold, an actual configuration, a selected probability current, a guidance field and maximal flow, an equilibrium measure, subsystem and instrument data, a locality contract, and source and error certificates. For a regular spinless scalar Schrodinger model the standard current obeys a continuity equation, and $`v=j/|\psi|^2`$ defines the usual guidance law away from nodes. Equivariance then propagates an initially chosen $`|\psi|^2`$ distribution. These facts are standard lower-level mathematics: continuity alone neither selects the actual configuration nor derives the initial equilibrium distribution, and it does not uniquely select the current because divergence-free modifications preserve the same continuity equation.

  The MTT result is therefore conditional. If one selected upper state emits the full pilot–wave record and its state, dynamics, configuration decoder, current, instruments, and records form commuting descent diagrams, then MTT reconstructs Bohmian trajectories and their operational statistics on the declared interval. The current canonical geometry is a ten-dimensional bundle over a four-dimensional Lorentzian base with a compact six-dimensional fibre; the former literal $`Y^4\times B_1\times B_2\times B_3`$ product is not used. Failure of the reconstruction means that a required current, decoder, flow, or stable continuation is unavailable. It does not follow from the absence of a right inverse, and it does not establish that Bohmian mechanics is globally impossible. Standard global-existence results in fact cover broad Hamiltonian classes for almost every equilibrium initial configuration.

  Entangled guidance is explicitly nonlocal in physical configuration space. Operational no-signalling can nevertheless hold in quantum equilibrium, while an MTT claim of upper-world locality requires a separate descent theorem preserving settings, local algebras, records, and independence assumptions. Measurement is treated as an ordinary system–apparatus interaction with an effective conditional wavefunction, not automatically as an admissibility-barrier crossing. The selected $`q=79`$ binary recorder provides an exact stopped operational output measure on its declared commuting Fock domain, but it does not yet source arbitrary Bohmian equilibrium ensembles or one uniquely actual history. The paper thus establishes a precise regime-limited reconstruction and a finite completion contract, not a universal derivation or a no-hidden-variable theorem.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 526a94a428c2f79cea7ec6be60af0db9d2d0384d9dec36286e64809f67223e1d
paper_id: modal-triplet-theory-from-mtt-to-pilot-wave-dynamics
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and Pilot–Wave Dynamics:
  A Regime-Limited Configuration-Space Reconstruction
zenodo_doi: 10.5281/zenodo.21709225
zenodo_record_id: 21709225
zenodo_url: "https://zenodo.org/records/21709225"
---

# Revision note: Version 2

<div class="description">

Version 2 supersedes Version 1.0, DOI [10.5281/zenodo.18262378](https://doi.org/10.5281/zenodo.18262378).

The former paper combined standard continuity and guidance formulas with unsupported MTT source claims. It began from the retired literal three-factor internal product, called the Bohmian configuration no additional hidden variable, treated equivariance as an independent derivation of the Born measure, and inferred measurement, horizon, and cosmological transitions from the absence of a measurable right inverse. It also asserted a no-global-guidance theorem contradicted in scope by standard almost-sure global-existence results.

This revision defines the full lower pilot–wave record, separates standard Bohmian mathematics from MTT source selection, and proves a typed conditional reconstruction theorem. It makes nodal and regularity domains explicit, records the current-selection ambiguity, replaces the right-inverse criterion by failures of current descent, configuration decoding, flow existence, or stable continuation, and separates configuration-space nonlocality from operational no-signalling and any claimed upper-world locality.

For a supplied scalar Schrodinger model, the standard probability current, guidance field, polar Hamilton–Jacobi representation, and equivariance calculation remain valid under their usual hypotheses. They provide a useful lower target for MTT reconstruction.

MTT has not yet selected a universal pilot–wave record from one source. In particular, the actual configuration, the standard current rather than an equivariant alternative, the initial equilibrium distribution, arbitrary apparatus contexts, relativistic foliation data, and one actual history are not all derived. The universal Born-source blocker remains open outside the selected $`q=79`$ binary recorder domain.

</div>

# The question in its correct order

Pilot–wave mechanics is not merely the Schrodinger equation written in polar form. It is a theory with two coupled pieces of state:

1.  a wavefunction $`\psi_t`$ evolving on configuration space; and

2.  an actual configuration $`Q_t`$ guided by that wavefunction.

The first piece is shared with ordinary nonrelativistic quantum mechanics. The second is additional ontic data relative to a wavefunction-only account. Calling it “hidden” does not make it fictitious; the term means that the configuration is not generally available with arbitrary precision while it still enters the law of motion. Bohm’s original construction was explicitly presented in those terms .

MTT begins elsewhere: with an upper state, admissibility conditions, geometric or operator carriers, and evaluation maps to observable records . The corrected MTT-to-QM paper distinguishes encoding, reconstruction, source selection, and universality . The same distinction is indispensable here:

1.  *Encoding:* can upper data represent a wavefunction and a configuration trajectory?

2.  *Reconstruction:* if all lower rows are supplied, do the MTT and Bohmian evaluations agree?

3.  *Selection:* does a selected MTT source emit the Hamiltonian, wavefunction, current, actual configuration, and equilibrium law?

4.  *Universality:* does the same construction work for every allowed preparation, apparatus, interaction, and relativistic regime?

This paper answers the second question under explicit hypotheses. It also identifies exactly which parts of the third question are presently closed on a finite domain and which remain open. It does not convert a conditional reconstruction into a universal derivation by changing vocabulary.

# The complete pilot–wave record

A useful audit begins by writing down everything the lower theory needs. This avoids silently treating a wavefunction, a continuity equation, or a projector as the whole theory.

<div id="def:record" class="definition">

**Definition 1** (Spinless nonrelativistic pilot–wave record). A pilot–wave record on a time interval $`I`$ is a tuple
``` math
\mathcal R_{\mathrm{PW}}
=
\bigl(
\mathcal Q,\mathrm dq,\mathcal H,\mathcal D,H,\hbar,\psi,U,
j,v,\mathcal N,\Phi,Q_0,\mu_{\mathrm{eq}},
\mathcal I,\mathcal L,\mathcal X
\bigr)
```
with the following typed rows.

1.  $`\mathcal Q`$ is the physical configuration manifold and $`\mathrm dq`$ its reference measure. For $`N`$ distinguishable spinless particles in Euclidean space, $`\mathcal Q=\mathbb R^{3N}`$.

2.  $`\mathcal H=L^2(\mathcal Q,\mathrm dq)`$ is the complex wavefunction Hilbert space. The dense domain $`\mathcal D`$ and the self-adjoint Hamiltonian $`H`$ are specified, including masses, potentials, boundary conditions, and any gauge connection.

3.  $`\hbar>0`$, $`U(t)`$, and $`\psi_t=U(t-t_0)\psi_{t_0}`$ specify the wave evolution on $`I`$.

4.  $`j^{\psi}`$ is a selected configuration-space current satisfying the relevant continuity equation. The velocity $`v^\psi=j^\psi/|\psi|^2`$ is defined on its declared nonnodal domain.

5.  $`\mathcal N_t=\{q:\psi_t(q)=0\}`$ is the nodal set, and $`\Phi^\psi_{t,t_0}`$ is the maximal measurable or classical flow of $`v^{\psi}`$ on its domain.

6.  $`Q_0\in\mathcal Q\setminus\mathcal N_{t_0}`$ is the actual initial configuration, and $`Q_t=\Phi^\psi_{t,t_0}(Q_0)`$ whenever the flow exists.

7.  $`\mu_{\mathrm{eq},t}(\mathrm dq)=|\psi_t(q)|^2\mathrm dq`$, after normalization, is the candidate quantum-equilibrium measure. The record states whether this is an assumption, a typicality postulate, a selected source result, or only an operational distribution.

8.  $`\mathcal I`$ contains subsystem, apparatus, pointer, conditional wavefunction, and output-instrument data.

9.  $`\mathcal L`$ records composition, configuration-space nonlocality, physical-space causal structure, operational no-signalling, and any relativistic foliation or covariance data.

10. $`\mathcal X`$ contains provenance, source, regularity, and error certificates, together with the precise interval and context family on which the comparison is exact.

</div>

The tuple is intentionally larger than $`(\psi,Q)`$. A formula for $`v^\psi`$ is meaningless before the configuration manifold and current are chosen. A self-adjoint Hamiltonian does not by itself select an actual configuration. Equivariance does not state why an ensemble began in equilibrium. A nonrelativistic configuration-space flow does not supply a relativistic foliation. Measurement requires a system–apparatus dynamics and a pointer record, not merely a reference to a “basin boundary.”

## Scope of the present lower model

The detailed formulas below concern scalar, spinless particles with a real potential. Spin, magnetic vector potentials, identical-particle configuration spaces, field ontologies, stochastic jump models, and relativistic extensions require modified currents and additional rows. The paper does not infer those extensions from the scalar case.

On $`\mathcal Q=\mathbb R^{3N}`$, take
``` math
\begin{equation}
H
=
\sum_{k=1}^{N}
-\frac{\hbar^2}{2m_k}\Delta_k
+V(q,t),
\label{eq:H}
\end{equation}
```
where the domain, boundary conditions, and hypotheses needed for self-adjoint propagation are supplied. Time-dependent Hamiltonians need their own propagator theorem; writing $`H(t)`$ is not enough .

# The standard lower dynamics

## Continuity and current

Let $`\psi`$ be regular enough that the following operations are justified and suppose
``` math
\begin{equation}
i\hbar\,\partial_t\psi=H\psi.
\label{eq:schrodinger}
\end{equation}
```
For the scalar Hamiltonian <a href="#eq:H" data-reference-type="ref+label" data-reference="eq:H">[eq:H]</a>, define
``` math
\begin{equation}
\rho^\psi(q,t)=|\psi(q,t)|^2,
\qquad
j_k^\psi(q,t)
=
\frac{\hbar}{m_k}
\operatorname{Im}\!\left(
\psi(q,t)^*\nabla_k\psi(q,t)
\right).
\label{eq:current}
\end{equation}
```
Multiplying <a href="#eq:schrodinger" data-reference-type="ref+label" data-reference="eq:schrodinger">[eq:schrodinger]</a> by $`\psi^*`$, subtracting its complex conjugate, and using that $`V`$ is real gives
``` math
\begin{equation}
\partial_t\rho^\psi
+\sum_{k=1}^{N}\nabla_k\!\cdot j_k^\psi=0.
\label{eq:continuity}
\end{equation}
```
This is local conservation on configuration space. Conservation of the integral additionally requires the appropriate boundary flux to vanish.

Where $`\rho^\psi>0`$, the standard Bohmian velocity is
``` math
\begin{equation}
v_k^\psi(q,t)
=
\frac{j_k^\psi(q,t)}{\rho^\psi(q,t)}
=
\frac{\hbar}{m_k}
\operatorname{Im}
\frac{\nabla_k\psi(q,t)}{\psi(q,t)}.
\label{eq:velocity}
\end{equation}
```
An actual configuration then obeys
``` math
\begin{equation}
\frac{\mathrm dQ_k(t)}{\mathrm dt}
=v_k^{\psi_t}(Q_t).
\label{eq:guidance}
\end{equation}
```
The trajectory is an integral curve of a selected velocity field. It is not the same object as the probability current, and neither object is an observable record by definition.

## Polar form and the quantum potential

On a simply connected nonnodal patch, write
``` math
\psi=R\,e^{iS/\hbar},
\qquad R>0.
```
Then
``` math
j_k^\psi=R^2\frac{\nabla_kS}{m_k},
\qquad
v_k^\psi=\frac{\nabla_kS}{m_k}.
```
Separating the real and imaginary parts of the Schrodinger equation yields
``` math
\begin{align}
\partial_t(R^2)
+\sum_k\nabla_k\!\cdot
\left(R^2\frac{\nabla_kS}{m_k}\right)&=0,
\label{eq:polar-continuity}\\
\partial_tS
+\sum_k\frac{|\nabla_kS|^2}{2m_k}
+V+Q^\psi&=0,
\label{eq:quantum-hj}\\
Q^\psi
&=
-\sum_k\frac{\hbar^2}{2m_k}\frac{\Delta_kR}{R}.
\label{eq:quantum-potential}
\end{align}
```
These identities are a useful representation of the supplied Schrodinger dynamics. They do not show that $`Q^\psi`$ is an independently selected MTT force or curvature. Such an identification would require a source map equating a particular upper geometric quantity with <a href="#eq:quantum-potential" data-reference-type="ref+label" data-reference="eq:quantum-potential">[eq:quantum-potential]</a>.

## Why the guidance law is not forced by continuity alone

The standard current in <a href="#eq:current" data-reference-type="ref+label" data-reference="eq:current">[eq:current]</a> is natural and has the expected Euclidean and Galilean behavior. Nevertheless, the continuity equation alone does not make it unique. If a sufficiently regular field $`w=(w_1,\ldots,w_N)`$ satisfies
``` math
\sum_k\nabla_k\!\cdot w_k=0,
```
then $`j'=j+w`$ obeys the same continuity equation, and
``` math
v'=\frac{j+w}{\rho}
```
is also equivariant wherever it is defined. Boundary, covariance, minimality, locality-in-configuration-space, and subsystem conditions can reduce this freedom, but they are additional selection criteria.

This matters for MTT. Reconstructing the standard pilot–wave theory requires the source map to emit the standard current, or a theorem showing that the MTT symmetries and composition rules select it. Defining $`v=j/\rho`$ after choosing $`j`$ is a valid construction; it is not a proof that MTT uniquely derived the choice.

# Equivariance and the probability boundary

Suppose the flow $`\Phi^\psi_{t,t_0}`$ exists and is unique on the interval under consideration. If an ensemble density $`f_t`$ is transported by <a href="#eq:guidance" data-reference-type="ref+label" data-reference="eq:guidance">[eq:guidance]</a>, it obeys
``` math
\partial_tf_t+\sum_k\nabla_k\!\cdot(f_tv_k^\psi)=0.
```
By <a href="#eq:continuity" data-reference-type="ref+label" data-reference="eq:continuity">[eq:continuity]</a>, $`\rho^\psi_t=|\psi_t|^2`$ obeys the same transport equation. Under the relevant uniqueness conditions,
``` math
\begin{equation}
f_{t_0}=|\psi_{t_0}|^2
\quad\Longrightarrow\quad
f_t=|\psi_t|^2.
\label{eq:equivariance}
\end{equation}
```
This is equivariance. It is central to Bohmian mechanics and to the quantum-equilibrium analysis of Durr, Goldstein, and Zanghi .

Equivariance propagates a distribution; it does not select the initial distribution. An MTT source theorem would have to explain why the preparation ensemble, typicality measure, or operational state has the equilibrium form before <a href="#eq:equivariance" data-reference-type="ref+label" data-reference="eq:equivariance">[eq:equivariance]</a> can be called a derivation of the Born law. This is the same distinction made in the corrected MTT-to-QM record between:

1.  characterization of a probability assignment;

2.  physical sourcing of an instrument and its output law; and

3.  selection of one ontic history.

## The selected $`q=79`$ binary recorder

One current MTT result is stronger than an abstract probability characterization. On a selected binary $`P/Q`$ apparatus domain, the canonical $`q=79`$ one-anchor recorder constructs a commuting Fock output algebra and gives the stopped effects
``` math
\begin{equation}
F_u(r_u)=e^{-\gamma u}I,
\qquad
F_u(\mathrm ds,a)
=\gamma e^{-\gamma s}P_a\,\mathrm ds,
\qquad
\gamma=\log448,
\label{eq:q79-effects}
\end{equation}
```
where $`a\in\{p,q\}`$, $`P_p=P`$, and $`P_q=I-P`$. Thus its selected normal state gives
``` math
\begin{equation}
\mu_{\rho,u}(r_u)=e^{-\gamma u},
\qquad
\mu_{\rho,u}(\mathrm ds,a)
=\gamma e^{-\gamma s}\operatorname{Tr}(\rho P_a)\,\mathrm ds.
\label{eq:q79-law}
\end{equation}
```
The source theorem and certificate are owned by the dedicated source-proof repository ; the corrected MTT-to-QM paper explains their operational role .

Equations <a href="#eq:q79-effects,eq:q79-law" data-reference-type="ref+label" data-reference="eq:q79-effects,eq:q79-law">[eq:q79-effects,eq:q79-law]</a> are not a fitted probability vector. They close an exact stopped output measure and second-moment capture descent on that declared binary domain. They do not choose a Bohmian configuration $`Q_0`$, prove that all configuration ensembles have density $`|\psi|^2`$, cover arbitrary apparatuses, or select one sample history as uniquely actual. The universal Born-source problem therefore remains open even though this finite-domain operational result is exact.

# Conditional MTT reconstruction

## Current geometric setting

The canonical MTT geometry used here is a bundle
``` math
\pi_X:X^{10}\longrightarrow Y^4
```
over a four-dimensional Lorentzian base, with a compact six-dimensional internal fibre and whatever connection, metric, and operator data the selected source supplies . The old literal expression
``` math
Y^4\times B_1\times B_2\times B_3
```
is not used as a physical proof source. Rank-$`1<2<3`$ filtrations and Circle–Lens–Nil encodings may organize operator sectors, but they are not three independent compact manifolds whose harmonic projectors automatically generate a Bohmian theory.

Let $`\mathcal U_{\mathrm{adm}}`$ be the declared upper domain. A partial source map
``` math
\mathcal S_{\mathrm{PW}}\colon
\mathcal U_{\mathrm{adm}}\dashrightarrow
\{\text{pilot--wave records}\}
```
may be undefined when one or more rows of <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">1</a> cannot be emitted. Let $`\operatorname{Eval}_{\mathrm{MTT}}(z,C)`$ denote the MTT prediction for an allowed context $`C`$, and let $`\operatorname{Eval}_{\mathrm{PW}}(\mathcal R,C)`$ denote the standard pilot–wave evaluation of a complete record.

<div id="thm:conditional" class="theorem">

**Theorem 2** (Conditional MTT–pilot–wave reconstruction). *Fix $`z\in\mathcal U_{\mathrm{adm}}`$, a time interval $`I`$, and a family $`\mathfrak C_z`$ of preparation–apparatus contexts. Assume:*

1.  *the selected source map emits a complete record $`\mathcal S_{\mathrm{PW}}(z)=\mathcal R_{\mathrm{PW}}(z)`$ for the rows needed by $`\mathfrak C_z`$;*

2.  *a unitary identification of the coherent wave sector with $`L^2(\mathcal Q,\mathrm dq)`$ intertwines the supplied state and Hamiltonian, exactly or with a declared propagation error;*

3.  *a configuration decoder $`D_z`$ emits $`Q_0`$ and intertwines the upper continuation with the maximal lower flow:
    ``` math
    D_z\!\left(\Phi^{\mathrm{up}}_{t,t_0}(u_0)\right)
          =
          \Phi^{\psi}_{t,t_0}\!\left(D_z(u_0)\right)
    ```
    on the stated domain, exactly or with a declared trajectory error;*

4.  *the selected lower current is the standard current <a href="#eq:current" data-reference-type="ref+label" data-reference="eq:current">[eq:current]</a>, or an explicitly declared alternative, and its descent diagram commutes;*

5.  *allowed apparatus couplings, pointer records, and conditional states descend to the lower instrument data in $`\mathcal I`$; and*

6.  *for every $`C\in\mathfrak C_z`$,
    ``` math
    \operatorname{Eval}_{\mathrm{MTT}}(z,C)
          =
          \operatorname{Eval}_{\mathrm{PW}}
          \bigl(\mathcal R_{\mathrm{PW}}(z),C\bigr)+r_C,
          \qquad |r_C|\leq\delta_C .
    ```*

*Then MTT reconstructs the declared pilot–wave dynamics and context statistics on $`I`$, exactly when all displayed errors vanish and with the declared control otherwise.*

</div>

<div class="proof">

*Proof.* Condition (PW1) supplies every typed lower object instead of inferring it from a projector. Condition (PW2) transports the wave evolution. Conditions (PW3) and (PW4) transport the actual configuration and selected guidance law. Condition (PW5) supplies the physical experiment rather than identifying measurement with a geometric slogan. Substitution into (PW6) gives the asserted equality or error bound for each allowed context. No claim outside $`I`$ or $`\mathfrak C_z`$ follows. ◻

</div>

The theorem is a reconstruction theorem, not a source theorem. Its value is that it exposes every place where the stronger claim can fail. It also prevents a decoded trajectory from being counted twice: once as an assumed upper coordinate and again as a derived lower configuration.

## Representation, reconstruction, and selection

<div class="center">

| Object | What lower mathematics supplies | What an MTT source must still establish |
|:---|:---|:---|
| Wavefunction | Evolution once $`\mathcal H,H,\psi_0`$ are supplied | Selection of $`\mathcal H,H,\psi_0`$, domains, and normalization |
| Current | Formula <a href="#eq:current" data-reference-type="ref+label" data-reference="eq:current">[eq:current]</a> for the scalar Hamiltonian | Why that current, rather than an equivariant modification, descends |
| Configuration | A trajectory once $`Q_0`$ and $`v^\psi`$ are supplied | Physical decoder and selection or provenance of $`Q_0`$ |
| Equilibrium | Propagation of $`|\psi|^2`$ by equivariance | Initial equilibrium, typicality, or preparation source |
| Measurement | Conditional/effective wavefunction from a complete apparatus model | Apparatus, pointer, record, and source diagrams |
| No-signalling | Standard operational marginals in equilibrium | Upper-to-lower locality map preserving settings and records |

</div>

# Nodes, existence, and the corrected boundary

## The nodal problem

The quotient in <a href="#eq:velocity" data-reference-type="ref+label" data-reference="eq:velocity">[eq:velocity]</a> is undefined on $`\mathcal N_t=\{\psi_t=0\}`$, and singular interactions can introduce further singular sets. A pointwise guidance formula therefore does not by itself give a global flow. One needs:

- a self-adjoint Hamiltonian and a wavefunction with the required regularity;

- local existence and uniqueness of the velocity ODE off the singular set;

- control of escape to infinity and approach to nodes or collision sets; and

- a measure statement identifying the exceptional initial configurations.

These issues have been studied directly in Bohmian mechanics. Berndl, Durr, Goldstein, Peruzzi, and Zanghi prove global existence for a large class of potentials for typical equilibrium initial configurations, despite the singular velocity at nodes . Therefore the former paper’s unconditional theorem that no global guidance law can exist was too strong.

## What can genuinely fail in an MTT reconstruction

For a chosen upper state and context, the reconstruction can cease to be certified if any of the following occurs:

1.  the lower Hamiltonian or wavefunction leaves its declared regularity domain;

2.  the selected current no longer descends or the continuity error exceeds its bound;

3.  the actual lower trajectory reaches the boundary of the maximal flow;

4.  the configuration decoder is undefined, nonphysical, or no longer intertwines upper and lower continuation;

5.  the coherent wave-sector identification ceases to be stable within its error budget; or

6.  an apparatus context lies outside the family for which the instrument diagram was proved.

These are meaningful failures of a theorem’s hypotheses. They say that the present MTT-to-pilot-wave comparison has ended or must be replaced by a different effective record.

By contrast, a right inverse of the projection is not required for a Bohmian velocity field. The lower field depends on the lower $`\psi_t`$, current, and configuration. Many upper states may decode to the same lower state without making $`j^\psi/|\psi|^2`$ undefined. Noninjectivity may obstruct recovering the upper history from lower data, but that is an inverse problem, not a no-guidance theorem.

## Stable continuation rather than a universal barrier

An “admissibility boundary” can still be useful terminology when it is defined by a concrete loss of regularity, spectral gap, decoder, or error control. It must not automatically be identified with every measurement, black-hole horizon, or cosmological selection event. Each such physical identification requires its own model and theorem.

The correct conclusion is modest and useful:

> Pilot–wave reconstruction is certified only on the interval and context family for which the wave, current, decoder, flow, and instrument diagrams remain defined and controlled.

This is regime limitation. It is not a proof that the underlying Bohmian model or the upper MTT state must terminate there.

# Measurement and effective collapse

Measurement is a physical interaction. Let $`x`$ denote subsystem coordinates and $`y`$ apparatus coordinates. A measurement-like unitary interaction can produce
``` math
\begin{equation}
\Psi(x,y)
=
\sum_\alpha c_\alpha\,
\varphi_\alpha(x)\,\Phi_\alpha(y),
\label{eq:measurement-state}
\end{equation}
```
where the pointer packets $`\Phi_\alpha`$ have macroscopically disjoint supports in $`y`$. In Bohmian mechanics the apparatus has an actual configuration $`Y`$. If $`Y`$ lies in the support of one packet $`\Phi_{\alpha_0}`$, the conditional subsystem wavefunction is, after normalization,
``` math
\psi_{\mathrm{cond}}(x)=\Psi(x,Y)
\approx\varphi_{\alpha_0}(x).
```
The universal wavefunction need not undergo a fundamental collapse. The subsystem has an effective wavefunction associated with the branch occupied by the actual apparatus configuration .

This account still needs an initial ensemble or typicality law to recover Born frequencies. It also needs the complete apparatus dynamics and pointer partition. The apparatus does not gain a special metaphysical status because it is called a measuring device.

For MTT, two comparison routes are possible:

1.  reconstruct the standard Bohmian apparatus account, including its actual pointer configuration and effective wavefunction; or

2.  construct a different selected MTT instrument and prove that its operational records agree with the target experiment.

The $`q=79`$ binary recorder realizes the second route on one selected domain. It does not automatically provide the first route’s actual configuration. Conversely, a Bohmian effective collapse does not prove that an MTT spectral gap closed or that the upper state crossed a universal admissibility barrier.

# Entanglement, nonlocality, and no-signalling

## Configuration-space nonlocality is explicit

For an entangled $`N`$-particle wavefunction, the velocity of particle $`k`$ depends on the full configuration:
``` math
\dot Q_k(t)
=
\frac{\hbar}{m_k}
\operatorname{Im}
\frac{\nabla_k\psi_t}{\psi_t}
\bigl(Q_1(t),\ldots,Q_N(t)\bigr).
```
This is not local dynamics in ordinary three-space. As a simple instantaneous illustration in one dimension, take
``` math
\psi(x_1,x_2)
=C\,e^{-a(x_1^2+x_2^2)}e^{i\kappa x_1x_2},
\qquad a>0 .
```
Then
``` math
v_1=\frac{\hbar\kappa}{m_1}x_2,
\qquad
v_2=\frac{\hbar\kappa}{m_2}x_1.
```
Each velocity depends on the distant coordinate. Replacing the phrase “physical-space nonlocal” by “global projection” does not remove this mathematical fact.

## Three distinct locality statements

The following claims must be separated:

1.  *Upper dynamical locality:* the fundamental MTT equations use local differential operators or causal propagation on their upper base.

2.  *Bell factorization:* conditioned on a complete variable, joint outcome probabilities factor into local response probabilities.

3.  *Operational no-signalling:* changing an unconditioned operation in one laboratory does not change the observed marginal statistics in a spacelike separated laboratory.

Bell experiments exclude the usual measurement-independent factorizable completion of the observed correlations. They do not imply controllable superluminal signalling. The corrected MTT Bell paper therefore adopts the consistent package of upper-local dynamics, microcausality, operational no-signalling, and globally nonfactorizing states .

Standard Bohmian mechanics is nonlocal in the second, physical configuration-space sense. In quantum equilibrium it reproduces standard quantum marginal statistics and hence operational no-signalling. Away from equilibrium, hidden-variable signalling can in general reappear; equilibrium is therefore part of the no-signalling contract rather than an optional decoration .

## What an upper-local MTT explanation must prove

Let $`a,b`$ be laboratory settings, $`A,B`$ their records, and $`z`$ an upper state. A satisfactory descent theorem must identify:
``` math
(z,a,b)
\longmapsto
\bigl(\psi_{a,b},Q_{a,b},\mathcal I^A_a,\mathcal I^B_b,A,B\bigr)
```
while preserving the claimed upper causal structure, the lower local algebras, the setting choices, the relevant independence assumptions, and the operational marginal identities. It must also explain where the lower configuration-space nonlocal dependence enters.

Without that commuting diagram, “local upstairs” and “no-signalling downstairs” are separate statements. A global coherent projector can be part of a proposed mechanism, but merely naming it does not prove either Bell factorization or no-signalling.

# A worked nonnodal example

Consider a one-dimensional free particle with initial width $`\sigma_0>0`$, mean position $`x_0`$, and mean momentum $`p_0`$. Write
``` math
\tau=\frac{\hbar t}{2m\sigma_0^2},
\qquad
x_c(t)=x_0+\frac{p_0}{m}t .
```
Up to the standard normalization and global phase, the evolved Gaussian is
``` math
\begin{equation}
\psi(x,t)
=
(1+i\tau)^{-1/2}
\exp\!\left[
-\frac{(x-x_c(t))^2}{4\sigma_0^2(1+i\tau)}
+\frac{i}{\hbar}
\left(p_0(x-x_0)-\frac{p_0^2t}{2m}\right)
\right].
\label{eq:gaussian}
\end{equation}
```
It has no nodes. Differentiating its phase gives
``` math
\begin{equation}
v^\psi(x,t)
=
\frac{p_0}{m}
+\frac{\hbar\tau}{2m\sigma_0^2(1+\tau^2)}
\bigl(x-x_c(t)\bigr).
\label{eq:gaussian-velocity}
\end{equation}
```
The integral curve through $`X_0`$ is
``` math
\begin{equation}
X(t)
=x_c(t)+(X_0-x_0)\sqrt{1+\tau^2}.
\label{eq:gaussian-flow}
\end{equation}
```
Substitution verifies $`\dot X=v^\psi(X,t)`$. If the initial ensemble is Gaussian with density $`|\psi(x,0)|^2`$, the scaling in <a href="#eq:gaussian-flow" data-reference-type="ref+label" data-reference="eq:gaussian-flow">[eq:gaussian-flow]</a> transports it to $`|\psi(x,t)|^2`$.

This example demonstrates exactly what the lower mathematics does. Given the Hamiltonian, wavefunction, standard current, and $`X_0`$, the trajectory is computable and equivariance is explicit. It does not explain why MTT selected the free Hamiltonian, the width, the momentum, the standard current, the actual $`X_0`$, or the equilibrium ensemble. A successful MTT source map must emit those rows or state which are experimental preparations.

# Relation to other MTT encodings

## The corrected QM reconstruction

The MTT-to-QM paper supplies the controlling lower quantum record and the conditional coherent-sector reconstruction theorem . The present paper does not re-prove that work. It adds the rows specific to a pilot–wave completion:
``` math
\text{physical configuration}
+\text{actual point}
+\text{selected current}
+\text{guidance flow}
+\text{equilibrium provenance}.
```
Thus pilot–wave reconstruction is strictly stronger in data than wavefunction reconstruction. It may be conceptually attractive, but it is not obtained for free.

## Wave–particle operator duality

The corrected wave–particle paper shows how a supplied positive filtered operator can have local-kernel and spectral-coherence representations, with instruments needed for operational outcome claims . A Bohmian trajectory is not identical to that paper’s local kernel. To connect them, one would need a theorem mapping the selected operator’s state and current to the configuration decoder and guidance flow in <a href="#def:record" data-reference-type="ref+label" data-reference="def:record">1</a>. The two encodings are compatible targets, not already-proved identical objects.

## Indivisible stochastic processes

A history-dependent kernel may concentrate around a deterministic flow in a small-noise or large-deviation limit. To identify that limiting flow with <a href="#eq:guidance" data-reference-type="ref+label" data-reference="eq:guidance">[eq:guidance]</a>, one must prove:

1.  the kernel and scaling are selected from the same MTT source;

2.  the rate functional has the Bohmian flow as its unique minimizer on the declared domain;

3.  concentration is uniform enough to pass to the desired observables; and

4.  nodes and basin changes remain controlled.

Without these rows, “pilot wave is the zero-noise limit” is a research proposal, not a theorem. Version 2 therefore removes the former unqualified zero-noise claim.

# Claim disposition

<div class="center">

| Former claim | Decision | Current statement |
|:---|:---|:---|
| Literal $`Y^4\times B_1\times B_2\times B_3`$ is the physical source | Retire | Use the current ten-dimensional bundle over a four-dimensional base with compact six-dimensional fibre. |
| Projection derives the Schrodinger record | Withdraw globally | The corrected QM theorem is a conditional coherent-sector reconstruction with one selected binary recorder domain. |
| Guidance follows with no additional ontology | Correct | The standard velocity follows after a current is selected, but the actual configuration is additional ontic data relative to $`\psi`$ alone. |
| Continuity uniquely selects Bohmian guidance | Withdraw | Divergence-free current modifications preserve continuity; current selection is a source row. |
| Equivariance derives the Born measure | Narrow | Equivariance propagates an initially supplied equilibrium density. |
| No right inverse implies no global guidance | Withdraw | Guidance requires lower wave/current/flow data, not inversion of the upper projection. |
| Measurement is an admissibility crossing | Reclassify | Measurement is an ordinary interaction and record; an MTT boundary mechanism requires a separate theorem. |
| Pilot wave necessarily fails at horizons and cosmological selection | Withdraw | No such conclusion follows from the nonrelativistic reconstruction. |
| Upper locality resolves Bohmian nonlocality | Narrow | The lower guidance remains configuration-space nonlocal; operational no-signalling and upper locality need an explicit descent contract. |
| Pilot wave is an MTT zero-noise limit | Open | A selected kernel, rate functional, concentration theorem, and domain control are required. |

</div>

# Completion contract

The reconstruction becomes a selected MTT pilot–wave theorem only when the following rows are supplied from one controlled source or are explicitly declared experimental inputs.

<div class="center">

| Row | Required object | Exit certificate |
|:---|:---|:---|
| PW1 | Quantum record | Selected or imported $`\mathcal H,H,\psi_0,\hbar,U`$, with domains and errors. |
| PW2 | Physical configuration | A configuration manifold and position ontology compatible with the selected particle sector. |
| PW3 | Actual configuration | A same-source decoder emitting $`Q_0`$, without replaying the desired lower trajectory as an input. |
| PW4 | Current selection | A symmetry/composition theorem selecting $`j^\psi`$, or a declared alternative with empirical equivalence bounds. |
| PW5 | Flow | Existence, uniqueness, nodal/collision control, and exceptional-set measure on the claimed interval. |
| PW6 | Equilibrium source | A preparation, typicality, or operational theorem supplying the initial $`|\psi|^2`$ law on the claimed context family. |
| PW7 | Apparatus descent | System–apparatus coupling, pointer partition, conditional state, and record instrument from the same source. |
| PW8 | Locality | A commuting upper-to-lower map preserving settings, local algebras, records, independence assumptions, and no-signalling marginals. |
| PW9 | Regime boundary | A concrete regularity, decoder, current, flow, or error criterion; no right-inverse surrogate. |
| PW10 | Relativistic extension | A covariant or foliation-equipped law with an explicit empirical and causal contract. |
| PW11 | Stochastic limit | Selected kernel and rate functional with a proved concentration limit to the same guidance flow. |
| PW12 | Objective history | If demanded, a theorem selecting one actual history rather than only a measure on output records. |

</div>

The present status is mixed. Standard lower mathematics supplies <a href="#eq:continuity,eq:velocity,eq:equivariance" data-reference-type="ref+label" data-reference="eq:continuity,eq:velocity,eq:equivariance">[eq:continuity,eq:velocity,eq:equivariance]</a> under its hypotheses. The $`q=79`$ recorder supplies an exact selected operational output measure for one binary domain. The full same-source rows PW2–PW8 and PW10–PW12 are not all closed. This paper therefore does not close the universal Born-source blocker.

# Discussion

## What has actually been achieved

Version 2 preserves a concrete positive result. Whenever MTT emits a regular scalar quantum record, a physical configuration, the standard current, an initial actual point, and commuting dynamics, the resulting lower characteristic flow is exactly the standard de Broglie–Bohm flow. This gives a clean target for simulations and for future source theorems. The worked Gaussian shows that the target is computationally explicit, not merely verbal.

The paper also gives a more useful negative diagnosis than the former right-inverse argument. The reconstruction boundary is now a finite list of typed failures: wave regularity, current descent, configuration decoding, flow existence, coherent continuation, or instrument scope. Each can be tested separately.

## Why the narrower result is stronger science

The former paper appeared stronger because it described every lower object as already derived. That wording hid the real research frontier. Once the configuration and current-selection rows are exposed, the next theorem is sharply posed:

> Construct one selected MTT source whose canonical physical configuration decoder and symmetry/composition data select the standard Bohmian current, and prove that its continuation intertwines with the maximal guidance flow.

This theorem would be genuinely new. Repeating the continuity equation would not discharge it.

## Relation to the Born-source program

The exact binary recorder is relevant because it demonstrates that MTT can source a nontrivial operational output law without fitting its probability weights. But an operational normal-state measure and a Bohmian equilibrium ensemble answer different questions. A future unification must show that the same selected source emits:
``` math
\rho_{\mathrm{upper}}
\longmapsto
\begin{cases}
\text{normal output state on the recorder algebra},\\
\text{actual configuration or history},\\
\text{equilibrium/typicality measure on configurations},
\end{cases}
```
and that these outputs agree for every admitted apparatus context. Until then, neither result should be used to overstate the other.

# Conclusion

The standard pilot–wave equations are mathematically clear once their complete lower record is supplied. The Schrodinger equation gives the standard current, the current and density define a velocity away from nodes, an actual configuration follows that velocity, and an initially $`|\psi|^2`$-distributed ensemble remains equivariant. The existence of this chain does not by itself source its inputs or make the guidance current unique.

MTT can reconstruct that chain on a declared domain if one selected upper state emits the wave, Hamiltonian, physical configuration, actual point, current, flow, instruments, and locality data and if the descent diagrams commute. That is the paper’s theorem. It is conditional, precise, and testable.

The corrected interpretation is therefore:

> Pilot–wave dynamics are a possible regime-limited lower reconstruction of MTT, not yet a universally selected consequence of MTT and not a no-hidden-variable reformulation.

The selected $`q=79`$ recorder is genuine finite-domain progress on operational probability. The next decisive step is a same-source configuration-and-current theorem, followed by equilibrium, apparatus, and locality descent on the same branch.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The curated strict-upgrade ledger is used only as a corpus-state cross-check that stronger universal source-selection obligations remain open. It does not prove this paper's physical-configuration decoder, actual configuration, current selection, equilibrium source, guidance flow, apparatus descent, or locality contract. The exact canonical q79 binary output-measure theorem is instead cited at its immutable source-proof repository commit and remains restricted to its declared P/Q Fock-output domain; it is not a universal Bohmian equilibrium or one-history theorem.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
