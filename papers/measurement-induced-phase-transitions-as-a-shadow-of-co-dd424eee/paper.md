---
abstract: |
  This paper replaces a universal identification of measurement-induced phase transitions, collapse thresholds, basin loss, and Zeno or anti-Zeno behavior by a typed, model-dependent framework. A hybrid monitored circuit is specified by its Hilbert space, unitary layers, measurement instrument, record law, conditioned trajectories, and averaged channel. The trajectory-averaged subsystem entropy is proved to differ from the entropy of the averaged state by a nonnegative Holevo quantity; consequently, the averaged channel does not retain the trajectory data that define the entanglement transition. Basin margins are retained as an effective model class only after a metric, boundary, generator, initial law, and stopping rule are fixed. For a stable Ornstein–Uhlenbeck coordinate with an absorbing boundary, we derive the exact mean first-passage integral and a basin-local contraction bound. The result is smooth in finite positive parameters and supplies no universal logistic knee. For a two-level system repeatedly projected at intervals of length tau, we derive the exact survival probability and its Zeno limit. Anti-Zeno enhancement is not universal and requires a specified reservoir or protocol. Measurement remains an ordinary physical interaction; outcome completion and the selection of one record are separate from an ensemble entanglement transition. The Modal Triplet Theory interpretation is conditional on a same-source map that emits the instrument, record weights, effective basin coordinate, and comparison errors.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 86b26c459c3a25de7fdcb999a77eada36dc6ac8ac716e03395dc9f1588ca984d
paper_id: measurement-induced-phase-transitions-as-a-shadow-of-co-dd424eee
release_state: zenodo_released
released_version: v2
title: |
  **Measurement-Induced Entanglement Transitions and Basin Diagnostics**
  Instruments, First Passage, and Protocol Limits
zenodo_doi: 10.5281/zenodo.21717359
zenodo_record_id: 21717359
zenodo_url: "https://zenodo.org/records/21717359"
---

# Version 2 Revision Note

Supersedes.
Version 1, *Measurement-Induced Phase Transitions as a Shadow of Coherence Basin Dynamics*.

Reason.
The earlier paper identified several inequivalent phenomena by definition and asserted universal finite-strength knees and Zeno/anti-Zeno crossovers without fixing an instrument, reduced generator, boundary geometry, reservoir, or first-passage problem.

Resolution.
Version 2 declares a hybrid monitored-circuit instrument, separates conditioned trajectories from the averaged channel, derives an exact first-passage model and an exact two-level Zeno law, and replaces universal thresholds by finite-size scaling and protocol-specific tests.

Retained content.
Basin-margin language is retained as one possible effective description of record dynamics when its state coordinate, metric, generator, boundary, and stopping rule are explicit.

Open boundary.
MTT has not yet selected the monitored-circuit instrument, its record probabilities for arbitrary apparatus contexts, the effective first-passage coefficients, or a thermodynamic critical point from one accepted upper source.

# Introduction

Measurement-induced entanglement transitions occur in quantum dynamics that combines entangling evolution with local monitoring. In a trajectory description, weak monitoring can permit volume-law entanglement, while sufficiently strong monitoring can support an area-law regime . Related purification transitions diagnose how rapidly a monitored system loses dependence on an initially mixed state . These are ensemble and thermodynamic statements about conditioned quantum trajectories.

They are not automatically statements about a single run “collapsing,” about an averaged density operator, or about a classical particle crossing a basin boundary. The distinctions matter:

1.  a quantum instrument gives record probabilities and conditional post-measurement states;

2.  averaging over records gives a completely positive trace-preserving channel;

3.  a trajectory entanglement statistic is nonlinear in the conditional state; and

4.  selecting or observing one record is a physical event whose probability law is an input to, or a theorem about, the instrument.

The earlier version of this paper compressed these layers into one projection-induced basin transition. That move obscured the actual mathematics and produced claims that were stronger than their assumptions. The revised paper asks a more precise question: which parts of basin language can be derived for a declared reduced model, and what additional map would be required for that model to explain a measurement-induced entanglement transition?

# Claim tier and ownership

The exact results below are finite-dimensional or one-dimensional stochastic statements. We prove:

1.  the instrument normalization and trajectory/ensemble distinction;

2.  an exact entropy identity showing what is lost by record averaging;

3.  a basin-local contraction estimate and exact mean first-passage formula for a declared Ornstein–Uhlenbeck model;

4.  smoothness rather than a universal knee for that finite model; and

5.  an exact repeated-projection survival law and Zeno limit.

We do not prove the existence or universality class of a thermodynamic MIPT for arbitrary circuits. We do not derive an anti-Zeno regime, an objective single-history law, or the Born rule for every apparatus context. The exact reduced-semigroup defect for evolve–coarse-grain maps belongs to the companion ETH/MBL paper and is not duplicated here . Standard monitored-circuit and replica results are imported from their primary sources .

# A typed monitored-circuit model

## Circuit and instrument

Let $`\mathcal H_L=(\mathbb{C}^q)^{\otimes L}`$. A depth-$`T`$ hybrid circuit consists of brickwork unitary layers $`U_t`$ and local measurements. At each eligible site and layer, a Bernoulli choice with parameter $`p`$ either applies no measurement or one of the projectors $`\{P_a\}_{a=1}^q`$, where
``` math
P_aP_b=\delta_{ab}P_a,\qquad \sum_aP_a=\mathbf 1.
```
The complete record $`r\in\mathcal R_{L,T}`$ contains both the measurement locations and their outcomes. It determines a Kraus operator $`K_r(p)`$. The Bernoulli weights can be absorbed into the Kraus operators so that
``` math
\begin{equation}
\label{eq:complete}
 \sum_{r\in\mathcal R_{L,T}}K_r(p)^\dagger K_r(p)=\mathbf 1.
\end{equation}
```

<div id="def:instrument" class="definition">

**Definition 1** (Trajectory instrument). For an initial state $`\rho_0`$, the record probability and conditioned state are
``` math
\begin{equation}
\label{eq:trajectory}
 \pi_r=\mathop{\mathrm{Tr}}[K_r\rho_0K_r^\dagger],\qquad
 \rho_r=\frac{K_r\rho_0K_r^\dagger}{\pi_r}
\end{equation}
```
whenever $`\pi_r>0`$. The family of completely positive maps $`\mathfrak I_r(\rho)=K_r\rho K_r^\dagger`$ is the instrument.

</div>

<a href="#eq:complete" data-reference-type="ref+Label" data-reference="eq:complete">[eq:complete]</a> implies $`\sum_r\pi_r=1`$. Nothing in the normalization makes measurement metaphysically special. It is simply the mathematical record of a physical coupling and readout protocol.

<div id="def:channel" class="definition">

**Definition 2** (Record-averaged channel). Discarding the record gives
``` math
\begin{equation}
\label{eq:channel}
 \mathcal N_{p,T}(\rho)=\sum_rK_r(p)\rho K_r(p)^\dagger
 =\sum_r\pi_r\rho_r .
\end{equation}
```
This map is completely positive and trace preserving.

</div>

## The transition observable

For a bipartition $`A\cup\bar A`$, define
``` math
\rho_{A,r}=\mathop{\mathrm{Tr}}_{\bar A}\rho_r,\qquad
 \bar\rho_A=\sum_r\pi_r\rho_{A,r}.
```
The trajectory-averaged von Neumann entropy is
``` math
\begin{equation}
\label{eq:traj-entropy}
 \overline S_A=\sum_r\pi_r S(\rho_{A,r}),
\end{equation}
```
while the averaged-state entropy is $`S(\bar\rho_A)`$. A MIPT analysis uses quantities such as <a href="#eq:traj-entropy" data-reference-type="ref+label" data-reference="eq:traj-entropy">[eq:traj-entropy]</a>, trajectory mutual information, purification time, or replica moments. It is not defined by $`S(\bar\rho_A)`$ alone.

<div id="thm:holevo" class="theorem">

**Theorem 3** (Exact record-information gap). *For every finite instrument,
``` math
\begin{equation}
\label{eq:holevo}
 S(\bar\rho_A)-\overline S_A
 =
 \sum_r\pi_r
 D\!\left(\rho_{A,r}\middle\Vert\bar\rho_A\right)
 =:\chi(A{:}R)\geq0 ,
\end{equation}
```
where $`D(\cdot\Vert\cdot)`$ is quantum relative entropy. Moreover,
``` math
0\leq\chi(A{:}R)\leq H(\{\pi_r\}).
```*

</div>

<div class="proof">

*Proof.* Expanding the relative entropies gives
``` math
\sum_r\pi_r\mathop{\mathrm{Tr}}[\rho_{A,r}\log\rho_{A,r}]
-\mathop{\mathrm{Tr}}[\bar\rho_A\log\bar\rho_A],
```
which is $`S(\bar\rho_A)-\sum_r\pi_rS(\rho_{A,r})`$. Nonnegativity follows from positivity of relative entropy. The upper bound is the standard Holevo bound for the classical–quantum state $`\sum_r\pi_r|r\rangle\langle r|\otimes\rho_{A,r}`$. ◻

</div>

<a href="#thm:holevo" data-reference-type="ref+Label" data-reference="thm:holevo">3</a> is the decisive type check. Record averaging can change an entanglement diagnostic by a positive information term. Many different ensembles can have the same average state, so the averaged channel does not reconstruct the conditioned ensemble without the instrument decomposition and record.

<div id="ex:ensembles" class="example">

**Example 4** (Same state, different records). The maximally mixed qubit has both decompositions
``` math
\frac{\mathbf 1}{2}
=\frac12|0\rangle\langle0|+\frac12|1\rangle\langle1|
=\frac12|+\rangle\langle+|+\frac12|-\rangle\langle-|.
```
The average state is identical, while the record-conditioned states and their correlations with a chosen apparatus basis differ.

</div>

# Finite circuits and thermodynamic transitions

For fixed $`L`$ and $`T`$, the record set is finite. The unnormalized weights $`\mathfrak I_r(\rho_0)`$ are finite products of unitary matrices, projectors, and Bernoulli factors. Away from parameter values where a record probability or a reduced-state eigenvalue vanishes, finite trajectory observables are smooth functions of $`p`$. Singular behavior associated with a phase transition requires a declared limiting procedure, commonly $`L\to\infty`$ followed by a long-time or steady-state limit.

<div id="prop:no-knee" class="proposition">

**Proposition 5** (Finite records do not imply a universal knee). *Let $`F_{L,T}(p)`$ be a finite-record statistic built from smooth Kraus operators on an interval where all terms entering its logarithms have a uniform positive lower bound. Then $`F_{L,T}`$ is smooth on that interval. No interior nonanalytic threshold follows from instrument normalization or noninvertibility alone.*

</div>

<div class="proof">

*Proof.* Finite sums, products, partial traces, and spectral functions restricted away from zero eigenvalues preserve smooth parameter dependence. ◻

</div>

The finite-size transition question is therefore empirical and model-specific. A report should state the circuit ensemble, local dimension, boundary conditions, initial state, record sampling, entanglement estimator, disorder or circuit realizations, numerical uncertainty, and order of limits. One may test a scaling form such as
``` math
X_L(p)=F\!\left((p-p_c)L^{1/\nu}\right)
 +L^{-\omega}G\!\left((p-p_c)L^{1/\nu}\right),
```
but the functions, exponents, corrections, fit window, and covariance model are part of the hypothesis. Large-$`q`$ mappings can select special critical values in special circuit ensembles ; those values are not universal consequences of projection.

# Basin margins as a declared model class

## Complete stochastic record

A basin model begins only after the following data are fixed:
``` math
\begin{equation}
\label{eq:basin-record}
 \mathfrak B=(X,\mathsf d,\mathcal L,\mu_0,B,\partial_{\rm abs}B,
 \partial_{\rm ref}B,\tau_B,\mathcal O,\mathcal E).
\end{equation}
```
Here $`X`$ is the reduced state space, $`\mathsf d`$ its metric, $`\mathcal L`$ the generator, $`\mu_0`$ the initial law, $`B`$ the basin, the two boundary parts carry absorbing and reflecting conditions, $`\tau_B`$ is the stopping time, $`\mathcal O`$ the reported observables, and $`\mathcal E`$ the approximation/error certificate. A scalar “margin” without these rows is not a first-passage problem.

## An exact local model

To exhibit what can actually be derived, consider
``` math
\begin{equation}
\label{eq:ou}
 \mathrm{d}X_t=-\kappa X_t\,\mathrm{d}t+\sqrt{2D}\,\mathrm{d}W_t,
 \qquad \kappa>0,\ D>0,
\end{equation}
```
on $`(-\infty,b)`$ with $`b>0`$, absorbing at $`b`$, and with the natural boundary condition at $`-\infty`$. The stable point $`0`$ lies inside the basin, and
``` math
\tau_b=\inf\{t\geq0:X_t=b\}
```
is the exit time.

<div id="prop:ou-contraction" class="proposition">

**Proposition 6** (Basin-local synchronous contraction). *Let $`X_t^x`$ and $`X_t^y`$ solve <a href="#eq:ou" data-reference-type="ref+label" data-reference="eq:ou">[eq:ou]</a> with the same Brownian path and initial values $`x,y<b`$. Before either process is stopped,
``` math
|X_t^x-X_t^y|=e^{-\kappa t}|x-y|.
```
Consequently, the unrestricted OU transition kernel contracts the one-Wasserstein distance by at most $`e^{-\kappa t}`$.*

</div>

<div class="proof">

*Proof.* The noise cancels in the difference, which solves $`\mathrm{d}(X_t^x-X_t^y)=-\kappa(X_t^x-X_t^y)\mathrm{d}t`$. The Wasserstein statement follows by applying the synchronous coupling to an optimal initial coupling. ◻

</div>

The statement is deliberately basin-local. Stopping, conditioning on survival, or resetting after exit changes the transition law and must be specified separately.

<div id="thm:mfpt" class="theorem">

**Theorem 7** (Exact OU mean first-passage time). *For $`x<b`$, the mean exit time $`T(x)=\mathop{\mathrm{\mathbb E}}_x[\tau_b]`$ is
``` math
\begin{equation}
\label{eq:mfpt}
 T(x)=\frac1D\int_x^b
 e^{\kappa y^2/(2D)}
 \left(\int_{-\infty}^{y}e^{-\kappa z^2/(2D)}\,\mathrm{d}z\right)\mathrm{d}y .
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The backward equation is
``` math
DT''(x)-\kappa xT'(x)=-1,\qquad T(b)=0,
```
with the natural condition $`T'(x)e^{-\kappa x^2/(2D)}\to0`$ as $`x\to-\infty`$. Multiplying the differential equation by $`e^{-\kappa x^2/(2D)}`$ and integrating from $`-\infty`$ to $`y`$ gives
``` math
T'(y)=-\frac1D e^{\kappa y^2/(2D)}
\int_{-\infty}^{y}e^{-\kappa z^2/(2D)}\,\mathrm{d}z .
```
Integrating from $`x`$ to $`b`$ and using $`T(b)=0`$ yields <a href="#eq:mfpt" data-reference-type="ref+label" data-reference="eq:mfpt">[eq:mfpt]</a>. ◻

</div>

<div id="cor:smooth" class="corollary">

**Corollary 8** (No universal logistic law). *For $`\kappa,D,b>0`$ and $`x<b`$, $`T(x)`$ is smooth in the finite parameters on compact subsets of that domain. A logistic crossover is not implied by the OU generator.*

</div>

This model can be a useful local surrogate if a monitored-circuit coordinate is independently shown to obey <a href="#eq:ou" data-reference-type="ref+label" data-reference="eq:ou">[eq:ou]</a> with a controlled error. It does not derive a MIPT, and its parameters cannot be read from a generic capacity margin.

# Protocol-specific Zeno behavior

Consider a two-level system with
``` math
H=\frac{\Omega}{2}\sigma_x,\qquad
 P_0=|0\rangle\langle0|,
```
initially in $`|0\rangle`$. Evolve for time $`\tau`$, measure $`\{P_0,\mathbf 1-P_0\}`$, and repeat. Condition on obtaining the survival record $`0`$ at every step.

<div id="thm:zeno" class="theorem">

**Theorem 9** (Exact repeated-projection survival law). *For $`n=t/\tau\in\mathbb{N}`$,
``` math
\begin{equation}
\label{eq:zeno}
 P_{\rm surv}(t;\tau)
 =
 \left[\cos^2\!\left(\frac{\Omega\tau}{2}\right)\right]^{t/\tau}.
\end{equation}
```
At fixed $`t`$,
``` math
\log P_{\rm surv}(t;\tau)
 =-\frac{\Omega^2t}{4}\tau+O(t\tau^3),
 \qquad
 \lim_{\tau\downarrow0}P_{\rm surv}(t;\tau)=1 .
```*

</div>

<div class="proof">

*Proof.* One interval has amplitude $`\langle0|e^{-iH\tau}|0\rangle=\cos(\Omega\tau/2)`$. Conditional survival over independent repeated projections multiplies the interval probabilities, giving <a href="#eq:zeno" data-reference-type="ref+label" data-reference="eq:zeno">[eq:zeno]</a>. The expansion follows from $`\log\cos^2 u=-u^2+O(u^4)`$. ◻

</div>

This is a genuine Zeno theorem because the Hamiltonian, projector, timing, conditioning, and comparison quantity are explicit. It is not a theorem that every measurement protocol has an anti-Zeno regime.

<div id="prop:anti" class="proposition">

**Proposition 10** (Anti-Zeno behavior is not unavoidable). *If a measured projector $`P`$ commutes with $`H`$ and the initial state lies in $`\operatorname{Ran}P`$, then repeated measurements preserve the state for every measurement interval. There is no intermediate enhancement of escape.*

</div>

<div class="proof">

*Proof.* Commutation makes $`\operatorname{Ran}P`$ invariant under the unitary evolution, so every survival probability equals one. ◻

</div>

Anti-Zeno enhancement can occur in models where measurement broadening overlaps a reservoir spectrum, but its presence and crossover scale depend on that spectral density and protocol . It cannot be inferred from noncommutativity or noninvertibility alone.

# Outcome completion is not the entanglement transition

The instrument in <a href="#def:instrument" data-reference-type="ref+label" data-reference="def:instrument">1</a> supplies a normalized law for records and a conditional state for each record. The MIPT concerns the large-system behavior of nonlinear statistics across that record ensemble. An actual detector run realizes one record as an ordinary physical process. These statements should not be collapsed:

1.  decoherence or record averaging suppresses selected coherences;

2.  conditioning updates the state associated with an observed record;

3.  basin contraction can stabilize a record after it exists;

4.  none of those facts alone derives the probability law from an upper geometry; and

5.  an ensemble phase transition does not select one ontic history.

The companion MTT measurement paper gives the general completion-kernel and record-stabilization framework and records the current limited q79 one-anchor result . Its arbitrary-context Born source and objective one-history obligations remain open. This paper neither re-proves nor enlarges those claims.

# Conditional interface with MTT

MTT contains coherent spectral projectors and stability margins at its current foundation tier . A coherent projector is not automatically a measurement instrument. To derive the monitored model above from MTT, one same-source construction must emit:

1.  the physical Hilbert space and circuit or continuous generator;

2.  the outcome-indexed completely positive maps $`\mathfrak I_r`$;

3.  the normalization and record weights $`\pi_r`$;

4.  the map from upper observables to trajectory entanglement diagnostics;

5.  any reduced basin coordinate, metric, generator, and absorbing boundary; and

6.  finite-volume and limiting comparison errors.

<div id="thm:transport" class="theorem">

**Theorem 11** (Conditional instrument transport). *Suppose an upper MTT instrument $`\{\widehat{\mathfrak I}_r\}`$ and a channel isometry $`V`$ satisfy, for every allowed input state,
``` math
\left\|
 V\widehat{\mathfrak I}_r(\widehat\rho)V^\dagger
 -\mathfrak I_r(V\widehat\rho V^\dagger)
 \right\|_1\leq\epsilon_r
```
and $`\sum_r\epsilon_r\leq\epsilon`$. Then the total-variation distance between the two record laws is at most $`\epsilon/2`$, and every bounded record statistic $`f`$ satisfies
``` math
\left|\mathop{\mathrm{\mathbb E}}_{\widehat\pi}f-\mathop{\mathrm{\mathbb E}}_{\pi}f\right|
 \leq \epsilon\,\left\lVert f \right\rVert_\infty .
```*

</div>

<div class="proof">

*Proof.* Taking traces and using $`|\mathop{\mathrm{Tr}}A|\leq\left\lVert A \right\rVert_1`$ gives $`\sum_r|\widehat\pi_r-\pi_r|\leq\epsilon`$. The first statement is the definition of total variation. The second follows by summing $`f(r)(\widehat\pi_r-\pi_r)`$ and applying the same bound. ◻

</div>

Transporting trajectory entropies additionally requires control of the normalized conditional states when $`\pi_r`$ is small; a probability floor or weighted continuity theorem must therefore be declared. The theorem shows exactly where an MTT source would enter, without pretending that basin vocabulary already supplies the source.

# Validation and falsification protocol

A serious numerical or experimental claim should publish:

1.  the complete instrument or enough circuit data to reconstruct its Kraus maps;

2.  record-resolved data or sufficient statistics, not only the averaged density operator;

3.  the distinction between $`\overline S_A`$ and $`S(\bar\rho_A)`$;

4.  sizes, depths, samples, seeds, error bars, fit windows, and correlated covariance;

5.  at least one alternative crossover model and a held-out size or observable;

6.  for a basin claim, every row of <a href="#eq:basin-record" data-reference-type="ref+label" data-reference="eq:basin-record">[eq:basin-record]</a>;

7.  for a Zeno or anti-Zeno claim, the unmeasured comparison dynamics, projector, timing convention, and reservoir spectrum if present; and

8.  for an MTT claim, the source hashes and transport errors required by <a href="#thm:transport" data-reference-type="ref+label" data-reference="thm:transport">11</a>.

The framework is falsified as an explanation if its selected basin coordinate does not predict record-resolved observables beyond the standard instrument model, if the first-passage approximation fails its error certificate, or if the proposed MTT source map is chosen only after seeing the target critical data.

# Conclusion

Measurement-induced entanglement transitions, averaged decoherence, record completion, first passage, and Zeno physics can interact in one experiment, but they are not one theorem. The correct common language is a typed physical instrument plus explicitly declared effective models. The trajectory/ensemble entropy identity proves why records cannot be discarded when studying a MIPT. The OU calculation shows what a genuine basin theorem requires and why it does not produce a universal knee. The repeated-projection calculation shows how a Zeno limit is derived from a protocol, while a commuting counterexample rules out unavoidable anti-Zeno behavior.

MTT may ultimately explain why a particular instrument and effective basin model are selected together. That claim now has a precise exit: construct the same-source instrument, record law, observable transport, and error bounds. Until then, basin margins are a useful model class, not a universal identification of measurement phenomena.
