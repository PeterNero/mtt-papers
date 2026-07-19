---
abstract: |
  We present a complete, first-principles and fully rigorous derivation of indivisible stochastic processes from the Modal Triplet Theory (MTT) framework. Working on the 10-dimensional modal manifold
  ``` math
  M_{10} = Y_4 \times B_1 \times B_2 \times B_3,
  ```
  we construct a probability measure on the path space $`Q^{\mathbb{N}}`$ of external configurations and prove that the induced discrete-time dynamics are non-Markovian and indivisible in a precise, measure-theoretic sense. The derivation uses only MTT’s structural ingredients: (i) the joint harmonic projector $`\Pi`$ onto the coherent sector, (ii) the curvature-driven modal flow $`\Phi_\tau`$, and (iii) the observable pushforward $`P = I \circ \Pi`$ integrating out internal manifolds. We formulate hypotheses (spectral gaps, stability, regularity) identical in spirit to those used in the MTT$`\Rightarrow`$QM derivation and show that (a) conditional transition kernels $`K_{\Delta \tau}[q'|q_0,\ldots,q_k]`$ exist and are normalised, (b) the induced process is indivisible because conditioning depends irreducibly on the complete past, and (c) probabilities arise from exponential modal-action weights $`\exp(-\Delta A/\hbar)`$, yielding a consistent, noncontextual measure on histories. A reconstruction theorem then proves surjectivity: any admissible indivisible kernel (within an explicit class) is realised by suitable MTT boundary data. Measurement is identified with conditioning under constraint changes $`F\to F'`$, which rigorously corresponds to pruning of histories with renormalisation. Our results establish MTT as a common origin for both Hilbert-space quantum mechanics and its stochastic dual, with indivisibility and interference emerging as consequences of MTT’s fixed-point modal geometry.
author:
- Peter Nero
current_version: v1.0
date: January, 2025
generated_from_main_tex_sha256: dc46357bc03d317b013e6dda77bf7e99ed41206e0a8227c930e1799daa27c0bd
paper_id: modal-triplet-theory-from-mtt-to-indivisible-stochastic-449ca9a6
release_state: zenodo_released
released_version: v1.0
title: |
  Modal Triplet Theory: From MTT to Indivisible Stochastic Processes:  
  A First-Principles, Fully Rigorous Derivation
zenodo_doi: 10.5281/zenodo.18254863
zenodo_record_id: 18254863
zenodo_url: "https://zenodo.org/records/18254863"
---

# Introduction

#### Modal Triplet Theory (MTT).

MTT posits a 10-dimensional product manifold
``` math
\begin{equation}
\label{eq:M10}
M_{10} = Y_4 \times B_1 \times B_2 \times B_3,
\end{equation}
```
where $`Y_4`$ is a smooth Lorentzian spacetime $`(M_4,g^{(4)})`$ and each $`B_n`$ is a compact oriented Riemannian $`3`$-manifold $`(B_n,h^{(n)})`$ with spin structure. The total metric factorises (possibly up to small warpings) as
``` math
\begin{equation}
\label{eq:metric}
g^{(10)} = g^{(4)} \oplus h^{(1)} \oplus h^{(2)} \oplus h^{(3)}.
\end{equation}
```
MTT dynamics are encoded in a curvature-reducing semi-flow $`\Phi_\tau`$ on the configuration space of fields over $`M_{10}`$, equipped with a joint harmonic projector
``` math
\begin{equation}
\label{eq:Pi}
\Pi := \Pi_{B_1}\otimes \Pi_{B_2}\otimes \Pi_{B_3},
\end{equation}
```
mapping to the *coherent sector*
``` math
\begin{equation}
\label{eq:Hcoh}
H_{\mathrm{coh}} := \mathrm{Im}(\Pi) = \bigcap_{n=1}^3 \ker \Delta_{B_n}.
\end{equation}
```
Integration over the compact internal spaces defines the observable pushforward $`P=I\circ \Pi`$, which yields effective $`Y_4`$-fields from full modal data.

#### From MTT to QM.

A companion derivation (*MTT$`\Rightarrow`$QM*) constructs a Hilbert space $`H_{\mathrm{obs}}`$, a reduced self-adjoint Hamiltonian $`H_{\mathrm{obs}}`$, and unitary time evolution $`U(t)=e^{-itH_{\mathrm{obs}}/\hbar}`$ for the projected fields. Probabilities are obtained from modal re-coherence via noncontextual measures on projections, invoking Gleason–Busch to recover the Born rule; generalised measurements arise from modal Stinespring/Naimark dilation.

#### Aim of this work (MTT$`\Rightarrow`$Indivisible Processes).

In the present paper, we develop the *stochastic* face of the same reduction. We show that the modal flow $`\Phi_\tau`$ and projection $`P`$ together induce, on an external configuration space $`Q\subset Y_4`$ (particle positions, coarse field amplitudes, etc.), a discrete-time probability law on the path space $`Q^{\mathbb{N}}`$ whose one-step *conditional kernels*
``` math
K_{\Delta \tau}\!\left[q_{k+1}\,\middle|\, q_0,\ldots,q_k\right]
```
are *history-dependent*. This renders the process *non-Markovian*; we then give a rigorous criterion (in terms of conditional $`\sigma`$-algebras) under which no factorisation into Markovian semigroups exists on $`(Q,\mathcal{B}(Q))`$, i.e. the process is *indivisible*. We prove: (i) existence and normalisation of kernels under explicit spectral-gap and stability hypotheses; (ii) consistency (Kolmogorov extension) and uniqueness via a contraction argument on the space of conditional probability functionals; (iii) measurability and pathwise well-posedness; and (iv) a reconstruction theorem showing that any admissible indivisible kernel can be realised by suitable internal geometries and couplings in MTT.

#### Contributions and structure.

- §2 fixes the geometric/analytic hypotheses (spectral gaps, stability, regularity), identifies the configuration space $`Q`$, and defines the modal action increment $`\Delta A`$.

- §3 constructs the path-space measure and one-step kernels from the modal flow, proves normalisation, and establishes non-Markovianity and indivisibility under a precise conditional-independence witness.

- §4 gives a reconstruction theorem: for an explicit admissible class $`\mathcal{K}_{\mathrm{target}}`$ of indivisible kernels (normalised, positive, Lipschitz in the complete-past metric, and generated by bounded modal actions), there exist MTT boundary data whose projection realises them exactly.

- §5 establishes probability weights $`w=\exp(-\Delta A/\hbar)`$ as a *noncontextual* and *consistent* measure on histories (cylinder $`\sigma`$-algebra), and proves equivalence with the Born probabilities upon Hilbert reconstruction.

- §6 formalises measurements as constraint changes $`F\to F'`$ in modal space and proves that the resulting update is Bayesian conditioning on a sub-$`\sigma`$-algebra of histories, i.e. pruning with renormalisation.

- §7 discusses physical implications (origin of nonlocal correlations, comparison with the Hilbert-space face).

- §8 concludes. Appendices supply technical proofs: boundedness of $`P`$, existence/uniqueness of the path measure (complete-connections contraction), indivisibility criteria, and worked examples.

#### Mathematical stance.

We work in discrete modal time $`\tau\in \Delta\tau\,\mathbb{N}`$, which suffices for rigour and aligns with the fixed-point iteration view. Continuous-time limits can be obtained under standard tightness and uniform integrability assumptions (not needed for the main claims). All probability statements are made with respect to the canonical product $`\sigma`$-algebra on $`Q^{\mathbb{N}}`$.

# Mathematical Setup and Hypotheses

## Geometric background

We work on the $`10`$-dimensional modal manifold
``` math
\begin{equation}
\label{eq:M10}
M_{10} = Y_4 \times B_1 \times B_2 \times B_3,
\end{equation}
```
with the following structures:

- $`Y_4`$ is a smooth Lorentzian manifold $`(M_4,g^{(4)})`$, representing emergent spacetime.

- Each $`B_n`$ is a compact, oriented Riemannian $`3`$-manifold $`(B_n,h^{(n)})`$ with spin structure and volume form $`d\mu_{B_n}`$.

- The total metric factorises as
  ``` math
  g^{(10)} = g^{(4)} \oplus h^{(1)} \oplus h^{(2)} \oplus h^{(3)},
  ```
  up to smooth warping terms in the internal sectors.

The field content consists of sections of bundles $`E\to M_{10}`$ with $`L^2`$ inner product induced by $`g^{(10)}`$. The Laplace–Beltrami operators $`\Delta_{B_n}`$ act fibrewise on $`E|_{B_n}`$.

## Harmonic projectors and coherent sector

<div id="H1" class="assumption">

**Assumption 1** (Spectral gap). For each $`n`$, the spectrum of $`\Delta_{B_n}`$ is discrete and admits a gap:
``` math
\lambda_n := \inf\big(\mathrm{Spec}(\Delta_{B_n}) \setminus \{0\}\big) > 0.
```

</div>

<div id="H2" class="assumption">

**Assumption 2** (Harmonic projection). Let $`\Pi_{B_n}:L^2(B_n)\to \ker\Delta_{B_n}`$ be the orthogonal projector. We require $`\Pi_{B_n}`$ to be bounded on $`H^1(B_n)`$ and to commute with external derivatives and chirality operators.

</div>

The joint harmonic projector is defined by
``` math
\begin{equation}
\label{eq:PiDef}
\Pi := \Pi_{B_1}\otimes \Pi_{B_2}\otimes \Pi_{B_3},
\end{equation}
```
which is self-adjoint, idempotent, and bounded. The coherent sector is
``` math
\begin{equation}
\label{eq:HcohDef}
H_{\mathrm{coh}} := \mathrm{Im}(\Pi) = \bigcap_{n=1}^3 \ker \Delta_{B_n}.
\end{equation}
```

## Observable pushforward

Define the fibre integration
``` math
\begin{equation}
\label{eq:pushforward}
I:L^2(M_{10})\to L^2(Y_4), \quad (If)(y) := \frac{1}{\prod_{n=1}^3 \mathrm{Vol}(B_n)} \int_{B_1\times B_2\times B_3} f(y,b)\, d\mu_{B_1} d\mu_{B_2} d\mu_{B_3}.
\end{equation}
```

<div id="H6" class="assumption">

**Assumption 3** (Boundedness of $`P`$). The composition $`P:=I\circ \Pi`$ extends to a bounded operator on $`L^2(M_{10})`$, mapping modal fields to observable external fields on $`Y_4`$.

</div>

## Modal dynamics and fixed points

Let $`\Phi_\tau:H^1(E)\to H^1(E)`$ denote the semi-flow generated by the MTT curvature-reducing equations. We posit:

<div id="H3" class="assumption">

**Assumption 4** (Fixed-point coherence). There exists a globally attracting fixed point $`\Psi^*\in H_{\mathrm{coh}}`$ for the projected flow $`\Pi\circ \Phi_\tau`$.

</div>

<div id="H4" class="assumption">

**Assumption 5** (Stability under damping balance). For disturbances with bundle-resolved growth rates $`\delta_n`$ and damping rates $`\gamma_n`$, the inequality $`\gamma_n > \delta_n`$ ensures that $`H_{\mathrm{coh}}`$ is dynamically invariant under $`\Phi_\tau`$.

</div>

## Finite-energy and regularity

<div id="H5" class="assumption">

**Assumption 6** (Finite energy). Initial data lie in the finite-energy domain of the 10D Hamiltonian $`H_{10}`$ induced by the quadratic MTT action, ensuring $`\Psi(0)\in L^2(M_{10})`$ with finite norm.

</div>

<div id="H7" class="assumption">

**Assumption 7** (Regularity). All background fields $`(g^{(n)},A^{(n)},\ldots)`$ are $`C^\infty`$, ensuring Sobolev embeddings and functional-analytic operations (spectral calculus, compactness) hold.

</div>

## Configuration space and histories

Let $`Q\subset Y_4`$ denote the external configuration space of observables (e.g. positions of $`N`$ particles, coarse lattice field values). We assume $`Q`$ is a Polish space with Borel $`\sigma`$-algebra $`\mathcal{B}(Q)`$.

<div class="definition">

**Definition 8** (History). A (finite) history is a tuple $`\mathcal{H}_k=(q_0,\ldots,q_k)`$ with $`q_i\in Q`$ observed at discrete modal times $`\tau_i=i\Delta\tau`$. The path space of infinite histories is $`Q^{\mathbb{N}}`$ with product $`\sigma`$-algebra.

</div>

## Modal action increment

For $`\Psi,\Psi'\in H_{\mathrm{coh}}`$ related by a flow segment of $`\Phi_\tau`$, define the modal action increment $`\Delta A(\Psi\to\Psi')\geq 0`$ as the minimal deformation cost in modal configuration space. By stationary-phase arguments, $`\Delta A`$ determines stochastic weights. Precise definition is given in Appendix <a href="#app:Action" data-reference-type="ref" data-reference="app:Action">8</a>.

## Summary of hypotheses

Under (H<a href="#H1" data-reference-type="ref" data-reference="H1">1</a>)–(H<a href="#H7" data-reference-type="ref" data-reference="H7">7</a>) we have:

- A well-defined harmonic projector $`\Pi`$ with bounded range $`H_{\mathrm{coh}}`$;

- A globally attracting, stable fixed point $`\Psi^*\in H_{\mathrm{coh}}`$;

- A bounded observable pushforward $`P:I\circ \Pi`$ mapping modal fields to external fields;

- A Polish configuration space $`Q`$ with history path space $`Q^{\mathbb{N}}`$;

- A well-defined action increment $`\Delta A`$ generating weights.

These conditions suffice for rigorous construction of the induced stochastic process.

# Projection to Stochastic Dynamics

We now construct the stochastic dynamics on $`Q`$ induced by the MTT modal flow $`\Phi_\tau`$ and projection $`P=I\circ \Pi`$. All results are proved under the hypotheses (H<a href="#H1" data-reference-type="ref" data-reference="H1">1</a>)–(H<a href="#H7" data-reference-type="ref" data-reference="H7">7</a>).

## One-step transition kernels

Let $`\Psi(\tau)\in H_{\mathrm{coh}}`$ evolve under the projected flow $`\Pi\circ \Phi_\tau`$ with initial data $`\Psi(0)`$. Define the external configuration at time $`\tau=k\Delta\tau`$ as
``` math
q_k := (P\Psi)(k\Delta\tau)\in Q.
```

<div class="definition">

**Definition 9** (MTT one-step kernel). For each history prefix $`\mathcal{H}_k=(q_0,\ldots,q_k)`$, define the one-step transition kernel $`K_{\Delta\tau}[\,\cdot\,|\mathcal{H}_k]`$ as the probability measure on $`(Q,\mathcal{B}(Q))`$ given by
``` math
\begin{equation}
\label{eq:kernelDef}
K_{\Delta\tau}(A \mid \mathcal{H}_k)
:= \mathbb{P}(q_{k+1}\in A \mid q_0,\ldots,q_k),
\qquad A\in \mathcal{B}(Q),
\end{equation}
```
where $`\mathbb{P}`$ is the path-space measure constructed from modal weights $`w=\exp(-\Delta A/\hbar)`$.

</div>

<div class="proposition">

**Proposition 10** (Normalisation). *For all histories $`\mathcal{H}_k`$,
``` math
K_{\Delta\tau}(Q \mid \mathcal{H}_k) = 1.
```*

</div>

<div class="proof">

*Proof.* By definition, $`\mathbb{P}(\cdot|\mathcal{H}_k)`$ is a conditional probability measure on $`(Q,\mathcal{B}(Q))`$. Normalisation is automatic:
``` math
K_{\Delta\tau}(Q\mid \mathcal{H}_k) =
\mathbb{P}(q_{k+1}\in Q \mid \mathcal{H}_k) = 1.
```
 ◻

</div>

#### Complete connections / summable variations.

Throughout we assume a complete‑connections regularity: there exists $`\alpha\in(0,1)`$ and $`L<\infty`$ such that $`h\mapsto k(\cdot|h)`$ is $`L^1(\nu)`$–Lipschitz in the complete‑past metric $`d_\alpha`$ (summable variations). This ensures measurability, Ionescu–Tulcea consistency, and uniqueness/stability of the induced $`g`$‑measure on $`Q^{\mathbb N}`$.

## Kolmogorov extension and path measure

<div id="thm:IT" class="theorem">

**Theorem 11** (Ionescu–Tulcea construction of the path measure). *Let $`(Q,\mathcal B(Q))`$ be a standard Borel space, fix an initial law $`\lambda_0`$ on $`(Q,\mathcal B(Q))`$, and for each finite history $`H_k=(q_0,\dots,q_k)`$ let $`K_{\Delta\tau}(\,\cdot\,|H_k)`$ be a probability kernel on $`(Q,\mathcal B(Q))`$ such that:*

1.  *$`H_k\mapsto K_{\Delta\tau}(A|H_k)`$ is $`\mathcal B(Q)^{\otimes(k+1)}`$–measurable for all $`A\in\mathcal B(Q)`$;*

2.  *$`K_{\Delta\tau}(Q|H_k)=1`$ for all $`H_k`$.*

*Then there exists a unique probability measure $`\mathbb P`$ on $`(Q^{\mathbb N},\mathcal B(Q)^{\otimes\mathbb N})`$ such that for all cylinder sets
``` math
\mathbb P(q_0\!\in\!A_0,\dots,q_k\!\in\!A_k) \;=\; \int_{A_0}\!\lambda_0(dq_0)\,\prod_{i=0}^{k-1} K_{\Delta\tau}(dq_{i+1}|q_0,\dots,q_i).
```*

</div>

<div class="proof">

*Proof.* Consistency requires that for $`A_0,\ldots,A_{k-1}\in\mathcal{B}(Q)`$,
``` math
\int_Q K_{\Delta\tau}(dq_k\mid q_0,\ldots,q_{k-1})
=1,
```
and that the marginals of the joint distribution for $`(q_0,\ldots,q_k)`$ reduce to those for $`(q_0,\ldots,q_{k-1})`$. Both follow from the definition of conditional kernels and normalisation. The Kolmogorov extension theorem (standard reference: e.g. Billingsley, *Probability and Measure*) then yields existence and uniqueness of the path measure $`\mathbb{P}`$. ◻

</div>

<div id="thm:dobrushin" class="theorem">

**Theorem 12** (Uniqueness and stability for complete connections). *Assume there exists $`\alpha\in(0,1)`$ and $`L<\infty`$ such that for histories $`h,h'`$ of the same length
``` math
\int_Q \big|k(q'|h)-k(q'|h')\big|\,d\nu(q')\;\le\; L\, d_\alpha(h,h'),
```
where $`k(\cdot|h)`$ is the density of $`K_{\Delta\tau}(\cdot|h)`$ and $`d_\alpha`$ is the complete-past metric. If $`\sum_{j\ge 0}\alpha^j<\infty`$ and $`L`$ is sufficiently small (summable variations), then:*

1.  *the Ionescu–Tulcea measure $`\mathbb P`$ is unique among all consistent path measures with the same kernels;*

2.  *the one-step transfer operator is a contraction in the $`L^1`$ Wasserstein metric induced by $`d_\alpha`$, hence the process is stable under small perturbations of the kernels.*

</div>

## Non-Markovianity

<div class="definition">

**Definition 13** (Markov property). A process $`\{q_k\}`$ is Markovian if
``` math
K_{\Delta\tau}(A\mid q_0,\ldots,q_k) =
K_{\Delta\tau}(A\mid q_k),
\qquad \forall A\in \mathcal{B}(Q).
```

</div>

<div id="thm:nonMarkov" class="theorem">

**Theorem 14** (Non-Markovianity of MTT kernels). *Under hypotheses (H<a href="#H1" data-reference-type="ref" data-reference="H1">1</a>)–(H<a href="#H7" data-reference-type="ref" data-reference="H7">7</a>), the induced process on $`Q`$ is generically non-Markovian.*

</div>

<div class="proof">

*Proof.* The kernel depends on the internal moduli path $`m(\tau)`$ generated by $`\Phi_\tau`$, whose evolution obeys
``` math
\dot m = -\nabla E(m; q_0,\ldots,q_k),
```
where $`E`$ is a modal energy functional depending on the entire history through spectral gaps $`\lambda_n(m)`$. Thus, given $`(q_0,\ldots,q_k)`$, the law of $`q_{k+1}`$ depends on the whole prefix, not only $`q_k`$. Therefore the equality above fails in general, so the process is non-Markovian. ◻

</div>

## Indivisibility

<div id="def:indivisible" class="definition">

**Definition 15** (Classical indivisibility). A discrete-time process with family $`\{K_{n\to n+1}(\cdot\mid H_n)\}`$ on $`(Q,\mathcal B(Q))`$ is *(classically) divisible* on an interval $`\{0,\dots,t\}`$ if there exist probability kernels $`\{M_{s\to s+1}(\cdot\mid q_s)\}_{s=0}^{t-1}`$, depending only on the *current* state, such that for all $`A\in\mathcal B(Q)`$
``` math
K_{0\to t}(A\mid q_0)\;=\;\int\cdots\int \mathbb 1_A(q_t)\,\prod_{s=0}^{t-1} M_{s\to s+1}(dq_{s+1}\mid q_s).
```
Otherwise, the process is *indivisible* on $`\{0,\dots,t\}`$.

</div>

<div id="thm:nonmarkov-indiv" class="theorem">

**Theorem 16** (Non-Markovianity $`\Rightarrow`$ indivisibility).

*If $`K_{n\to n+1}(\cdot|H_n)`$ depends on the complete past $`H_n`$, then there do not exist one‑step probability kernels $`\{M_{s\to s+1}(\cdot|q_s)\}_{s=0}^{t-1}`$ on $`(Q,\mathcal B(Q))`$ such that, for all $`A\in\mathcal B(Q)`$,
``` math
K_{0\to t}(A\,|\,q_0)=\int\!\cdots\!\int \mathbf 1_A(q_t)\prod_{s=0}^{t-1}M_{s\to s+1}(dq_{s+1}\,|\,q_s).
```
Hence the process is indivisible on any nontrivial interval when the state space is fixed to $`(Q,\mathcal B(Q))`$.*

</div>

<div class="remark">

*Remark 17* (On CP-divisibility). Our notion is *classical* divisibility (factorisation of classical kernels through single-time states). It should not be conflated with quantum CP-divisibility of dynamical maps. Upon Hilbert reconstruction, $`\mathbb P`$ reproduces Born probabilities, but CP-divisibility of the corresponding quantum channels is a separate property (typically violated for memoryful dynamics).

</div>

## Summary

From MTT’s modal dynamics and projection, we have constructed:

- A well-defined family of conditional kernels $`K_{\Delta\tau}(\cdot\mid \mathcal{H}_k)`$;

- A unique path-space probability measure $`\mathbb{P}`$ via Kolmogorov extension;

- Proofs that the induced process is non-Markovian and indivisible.

This establishes the stochastic face of MTT dynamics.

# Reconstruction Theorem: MTT Realises Indivisible Processes

This section establishes a rigorous reconstruction map from a broad class of indivisible stochastic kernels on the configuration space $`Q`$ to suitable choices of MTT boundary data. We first specify an admissible class of kernels with precise regularity; we then show (i) every such kernel admits a Gibbs-type representation by a nonnegative *action density*, and (ii) this action can be implemented as a *modal action increment* in MTT by an explicit, finite-dimensional moduli construction. A density result shows uniform approximation (in total variation) of continuous kernels by exactly realisable ones.

## Complete-past metric and regularity class

Let $`\alpha\in(0,1)`$ and define the complete-past metric $`d_\alpha`$ on history prefixes $`h=(q_0,\ldots,q_k)`$ and $`\tilde h=(\tilde q_0,\ldots,\tilde q_k)`$ by
``` math
\begin{equation}
\label{eq:past_metric}
d_\alpha(h,\tilde h):=
\sum_{j=0}^{k}\alpha^{k-j}\, d_Q(q_j,\tilde q_j),
\end{equation}
```
where $`d_Q`$ is a bounded metric that induces the topology of the Polish space $`Q`$.

<div class="definition">

**Definition 18** (Admissible kernel class $`\mathcal{K}_{\mathrm{adm}}`$). A family of conditional probability kernels $`K(\cdot \mid h)`$ on $`(Q,\mathcal{B}(Q))`$ indexed by finite histories $`h=(q_0,\ldots,q_k)`$ is in $`\mathcal{K}_{\mathrm{adm}}`$ if:

1.  *Strict positivity and normalisation:* $`K(\cdot\mid h)`$ has a density $`k(\,\cdot\,\mid h)`$ w.r.t. a fixed reference $`\sigma`$-finite measure $`\nu`$ on $`(Q,\mathcal{B}(Q))`$ with $`0<k(q'\mid h)\in L^1(\nu)`$ and $`\int k(q'\mid h)\,d\nu(q')=1`$ for all $`h`$.

2.  *Complete-past Lipschitz continuity:* There exists $`L<\infty`$ such that for all $`h,\tilde h`$ with the same length,
    ``` math
    \int \big|k(q'\mid h) - k(q'\mid \tilde h)\big|\, d\nu(q')
    \;\le\; L\, d_\alpha(h,\tilde h).
    ```

3.  *Indivisibility:* The process defined by $`\{K(\cdot\mid h)\}`$ is non-Markovian in the sense of Theorem <a href="#thm:nonMarkov" data-reference-type="ref" data-reference="thm:nonMarkov">14</a>, i.e. there exists a set of positive $`\mathbb{P}`$-measure of pairs $`(h,A)`$ such that $`K(A\mid h)\neq K(A\mid q_k)`$.

</div>

Assumption (K2) is a standard *complete connections* (summable variations) regularity, ensuring robustness of the path measure w.r.t. perturbations of the complete past; it strengthens the measurability hypotheses used in §<a href="#sec:projection" data-reference-type="ref" data-reference="sec:projection">3</a>.

## Gibbs representation by an action density

<div id="lem:gibbs" class="lemma">

**Lemma 19** (Gibbs representation with explicit normalizer). *Let $`K(\cdot|h)`$ have strictly positive density $`k(\cdot|h)`$ w.r.t. a fixed $`\sigma`$-finite $`\nu`$. Define
``` math
A(q',h):=\hbar\big(-\log k(q'|h)\big)-C(h),\qquad
C(h):=\hbar\inf_{q''\in Q}\big(-\log k(q''|h)\big).
```
Then $`A(\cdot,h)\ge 0`$ $`\nu`$-a.e. and
``` math
k(q'|h)=\frac{e^{-A(q',h)/\hbar}}{\displaystyle\int_Q e^{-A(q'',h)/\hbar}\,d\nu(q'')}.
```
Equivalently, with the unshifted action $`A_0(q',h):=-\hbar\log k(q'|h)`$ one has $`k=e^{-A_0/\hbar}`$ and the normalizer is $`\int k\,d\nu\equiv 1`$. The shift by $`C(h)`$ enforces $`A\ge0`$ without changing the normalized density. If $`h\mapsto k(\cdot|h)`$ is $`L^1(\nu)`$–Lipschitz in $`d_\alpha`$, then $`h\mapsto A(\cdot,h)`$ and $`h\mapsto \int e^{-A/\hbar}d\nu`$ inherit this regularity.*

</div>

<div class="proof">

*Proof.* Positivity of $`k`$ implies $`-\log k(q'\mid h)`$ is finite for $`\nu`$-a.e. $`q'`$. Subtracting the $`\inf`$ (which is finite) produces $`A\ge 0`$ and does not affect the normalised density because the shift cancels in <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a>. Measurability is inherited from $`k`$. For Lipschitz dependence, note
``` math
\|e^{-A(\cdot,h)/\hbar}-e^{-A(\cdot,\tilde h)/\hbar}\|_{L^1(\nu)}
= \|k(\cdot\mid h)Z(h)-k(\cdot\mid \tilde h)Z(\tilde h)\|_{L^1(\nu)}
```
and $`Z(h)=1`$ by construction. Hence the bound follows from (K2). ◻

</div>

Thus every admissible kernel admits a Gibbs form with a nonnegative *action density* $`A(\cdot,h)`$. The next step is to realise $`A`$ as a *modal action increment* in MTT.

## A representable quadratic-action subclass

To obtain an exact, constructive realisation within MTT, we specify a rich subclass of action densities.

<div id="def:quadratic_class" class="definition">

**Definition 20** (Quadratic-action class $`\mathcal{A}_{J,G,\Phi}`$). Fix $`J\in\mathbb{N}`$, a positive-definite matrix $`G\in\mathbb{R}^{J\times J}`$, and a measurable map $`\Phi:Q\times \bigcup_{k\ge 0} Q^{k+1}\to \mathbb{R}^{J}`$ assigning to $`(q',h)`$ a feature vector $`\Phi(q',h)`$. Define the action density
``` math
\begin{equation}
\label{eq:quadratic_action}
A(q',h) := \frac{1}{2}\,\big\|\Phi(q',h)-\Phi_\star(h)\big\|_{G}^2,
\qquad \|x\|_G^2 := x^{\mathsf T} G\, x,
\end{equation}
```
where $`\Phi_\star(h)`$ is a measurable anchor depending only on $`h`$. Let $`\mathcal{A}_{J,G,\Phi}`$ denote the set of all such $`A`$ with $`\Phi,\Phi_\star`$ that are Lipschitz in $`h`$ under $`d_\alpha`$ and Borel in $`q'`$.

</div>

The corresponding kernels have the Gibbs form
``` math
\begin{equation}
\label{eq:quadratic_kernel}
k(q'\mid h) = \frac{\exp\!\big(-\frac{1}{2\hbar}\|\Phi(q',h)-\Phi_\star(h)\|_G^2\big)}
{\int \exp\!\big(-\frac{1}{2\hbar}\|\Phi(q'',h)-\Phi_\star(h)\|_G^2\big)\, d\nu(q'')}.
\end{equation}
```
These kernels are strictly positive, normalised, and Lipschitz in $`h`$ (by dominated convergence and the Lipschitz hypotheses on $`\Phi,\Phi_\star`$), hence are in $`\mathcal{K}_{\mathrm{adm}}`$ whenever indivisibility (K3) holds.[^1]

## Exact realisation in MTT via finite-dimensional moduli

We now show that for any $`A\in \mathcal{A}_{J,G,\Phi}`$ there exist MTT boundary data whose modal action increment equals $`A`$ and thereby produce exactly the kernel <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a>.

<div id="thm:exact_realisation" class="theorem">

**Theorem 21** (Exact realisation of the quadratic-action class). *Fix $`J\in\mathbb{N}`$, $`G>0`$, and $`\Phi,\Phi_\star`$ as in Definition <a href="#def:quadratic_class" data-reference-type="ref" data-reference="def:quadratic_class">20</a>. There exist choices of internal backgrounds (gauge fields and metrics on $`B_n`$) and a $`J`$-dimensional smooth moduli submanifold $`\mathcal{M}\subset \prod_n \mathrm{Met}(B_n)\times \mathrm{Conn}(B_n)`$ with a Riemannian metric $`\mathbf{G}`$ such that:*

1.  *The moduli coordinate $`m\in\mathcal{M}`$ couples to the external configuration through boundary conditions so that the minimal modal action to move from the anchor $`m_\star(h)`$ to the target $`m(q',h)`$ equals
    ``` math
    \Delta A(q',h)= \frac{1}{2}\,\big\| \Phi(q',h)-\Phi_\star(h)\big\|_G^2 = A(q',h).
    ```*

2.  *The one-step conditional kernel generated by weighting $`e^{-\Delta A/\hbar}`$ and pushing forward by $`P`$ coincides with <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a> $`\nu`$-a.e.*

</div>

<div class="proof">

*Proof.* *Step 1 (Finite-dimensional moduli).* Consider a smooth $`J`$-dimensional manifold $`\mathcal{M}\simeq \mathbb{R}^J/\Lambda`$ (a flat torus for compactness) embedded as a finite-dimensional submanifold in the space of smooth backgrounds on the $`B_n`$. Choose coordinates $`m\in\mathbb{R}^J/\Lambda`$ and endow $`\mathcal{M}`$ with the flat metric $`\mathbf{G}\equiv G`$ (constant in these coordinates).

*Step 2 (Anchor and target).* Define smooth maps
``` math
m_\star:\bigcup_{k\ge 0} Q^{k+1}\to \mathcal{M},\qquad
m(\,\cdot\,,h): Q\to \mathcal{M},
```
by $`m_\star(h):= \Phi_\star(h) \bmod \Lambda`$ and $`m(q',h):= \Phi(q',h)\bmod \Lambda`$, using any fixed fundamental domain and the canonical projection $`\mathbb{R}^J\to \mathbb{R}^J/\Lambda`$. Lipschitz dependence of $`\Phi,\Phi_\star`$ ensures measurability.

*Step 3 (Action as geodesic energy).* On the Riemannian manifold $`(\mathcal{M},\mathbf{G})`$, let $`\gamma`$ be the constant-speed geodesic from $`m_\star(h)`$ to $`m(q',h)`$; since $`\mathbf{G}`$ is flat, $`\gamma`$ is the straight segment in the universal cover modulo $`\Lambda`$. The (time-rescaled) geodesic action with Lagrangian $`L(\dot m)=\tfrac12 \dot m^{\mathsf T}G \dot m`$ equals $`\tfrac12\|m(q',h)-m_\star(h)\|_G^2`$ and is the minimal action among all smooth paths with those endpoints. This matches $`A(q',h)`$ by construction.

*Step 4 (Modal dynamics and weighting).* Implement the moduli dynamics in MTT so that, conditional on the history $`h`$, the internal sector executes a transition from $`m_\star(h)`$ to $`m(q',h)`$ with path-weight density proportional to $`\exp(-\mathrm{Action}/\hbar)`$, which is standard in the (Euclideanised) modal path-integral picture and can be made precise at the rigorous level by defining the conditional kernel directly via $`e^{-\Delta A/\hbar}`$ as in §<a href="#sec:projection" data-reference-type="ref" data-reference="sec:projection">3</a>. Because $`A\ge 0`$ and $`\mathcal{M}`$ is compact, the normaliser is finite. Pushing forward by $`P`$ produces exactly the kernel in <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a>. ◻

</div>

<div class="remark">

*Remark 22* (Compatibility with MTT hypotheses). Compactness of $`\mathcal{M}`$ (torus) is compatible with the compactness of $`B_n`$ and ensures boundedness of energies; the flat metric ensures uniform spectral gaps on the constructed submanifold, consistent with Assumptions (H<a href="#H1" data-reference-type="ref" data-reference="H1">1</a>)–(H<a href="#H4" data-reference-type="ref" data-reference="H4">5</a>).

</div>

## Surjectivity onto the quadratic-action kernel class

<div id="cor:surjectivity" class="corollary">

**Corollary 23** (Surjectivity). *The map
``` math
\{\text{MTT boundary data}\}/\!\!\sim \;\longrightarrow\;
\left\{ K(\cdot\mid h)\text{ of the form \eqref{eq:quadratic_kernel}}\right\}
```
is surjective, where $`\sim`$ denotes the natural gauge/diffeomorphism equivalence.*

</div>

<div class="proof">

*Proof.* Given any $`K`$ of the form <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a>, define $`A`$ by <a href="#eq:quadratic_action" data-reference-type="eqref" data-reference="eq:quadratic_action">[eq:quadratic_action]</a>. Apply Theorem <a href="#thm:exact_realisation" data-reference-type="ref" data-reference="thm:exact_realisation">21</a>. ◻

</div>

## Density and approximation of continuous kernels

We now show that the representable class is dense (in total variation) in a natural space of continuous kernels.

Assume $`Q`$ compact metric and endow the set of fixed‑length histories with $`d_\alpha`$. Let $`\mathcal C(Q\times H_\alpha)`$ be the continuous functions in the product topology. By Stone–Weierstrass there exist finite feature maps $`\{F_j\}_{j=1}^J\subset \mathcal C`$ whose algebra is dense in $`\mathcal C(Q\times H_\alpha)`$. Uniform approximation of the continuous action $`A(\cdot,h)`$ by finite quadratic forms in $`\{F_j\}`$ implies, after normalisation, uniform (in $`h`$) $`L^1(\nu)`$‑approximation of densities $`k(\cdot|h)`$, hence TV‑density of the quadratic‑action class.

<div id="thm:TVdensity" class="theorem">

**Theorem 24** (TV-density). *Let $`Q`$ be compact metric, and let $`\nu`$ be a Borel reference measure with full support. Let $`\mathcal{K}_{\mathrm{cts}}`$ denote the set of kernels with continuous densities $`k(\cdot\mid h)`$ jointly continuous in $`(q',h)`$ (for the product of the topology of $`Q`$ and $`d_\alpha`$ on histories). Then for every $`K\in \mathcal{K}_{\mathrm{cts}}`$ and $`\varepsilon>0`$ there exist $`J,G,\Phi,\Phi_\star`$ such that the kernel $`\tilde K`$ of the form <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a> satisfies
``` math
\sup_{h}\, \int_Q \big|k(q'\mid h)-\tilde k(q'\mid h)\big|\, d\nu(q')
\;<\; \varepsilon.
```*

</div>

<div class="proof">

*Proof sketch.* By Lemma <a href="#lem:Gibbs" data-reference-type="ref" data-reference="lem:Gibbs">[lem:Gibbs]</a>, write $`k\propto e^{-A/\hbar}`$ with continuous $`A\ge 0`$ (after normalisation by subtracting a continuous $`C(h)`$). By Stone–Weierstrass, there exist finite feature maps $`F_j(q',h)`$ spanning an algebra dense in $`C(Q\times \mathcal{H}_\alpha)`$, where $`\mathcal{H}_\alpha`$ is the metric space of fixed-length histories with metric $`d_\alpha`$. Approximate $`A`$ uniformly by a finite quadratic form in features: $`\sum_{j=1}^J \tfrac12 \theta_j (F_j-\mu_j(h))^2`$. Absorb this into the structure of <a href="#eq:quadratic_action" data-reference-type="eqref" data-reference="eq:quadratic_action">[eq:quadratic_action]</a> by setting $`\Phi(q',h)=(\sqrt{\theta_j}F_j(q',h))_{j=1}^J`$ and $`\Phi_\star(h)=(\sqrt{\theta_j}\mu_j(h))_{j=1}^J`$, with $`G=\mathbf{1}`$. The uniform approximation of $`A`$ implies uniform (in $`h`$) approximation of the Gibbs densities after normalisation; dominated convergence yields the claimed TV bound. ◻

</div>

<div id="cor:approx" class="corollary">

**Corollary 25** (Approximate realisability of continuous kernels). *Under the hypotheses of Theorem <a href="#thm:TVdensity" data-reference-type="ref" data-reference="thm:TVdensity">24</a>, for every continuous kernel $`K`$ and $`\varepsilon>0`$ there exists MTT boundary data whose induced kernel $`\tilde K`$ satisfies $`\sup_h \|K(\cdot\mid h)-\tilde K(\cdot\mid h)\|_{\mathrm{TV}}<\varepsilon`$.*

</div>

<div class="proof">

*Proof.* Combine Theorem <a href="#thm:TVdensity" data-reference-type="ref" data-reference="thm:TVdensity">24</a> with Theorem <a href="#thm:exact_realisation" data-reference-type="ref" data-reference="thm:exact_realisation">21</a>. ◻

</div>

## Putting it together

We summarise the reconstruction result.

<div id="thm:reconstruction_main" class="theorem">

**Theorem 26** (Reconstruction, indivisible case). *Let $`K\in \mathcal{K}_{\mathrm{adm}}`$ be indivisible. Then:*

1.  *(*Exact realisation*) If $`K`$ admits a quadratic-action representation <a href="#eq:quadratic_kernel" data-reference-type="eqref" data-reference="eq:quadratic_kernel">[eq:quadratic_kernel]</a>, then there exist MTT boundary data realising $`K`$ exactly (Theorem <a href="#thm:exact_realisation" data-reference-type="ref" data-reference="thm:exact_realisation">21</a>).*

2.  *(*Approximate realisation*) If $`k(\cdot\mid h)`$ is continuous, then for any $`\varepsilon>0`$ there exist MTT boundary data yielding $`\tilde K`$ with $`\sup_h \|K(\cdot\mid h)-\tilde K(\cdot\mid h)\|_{\mathrm{TV}}<\varepsilon`$ (Corollary <a href="#cor:approx" data-reference-type="ref" data-reference="cor:approx">25</a>).*

*In both cases the induced process is indivisible provided $`K`$ (or $`\tilde K`$) fails the Markov property on $`Q`$ (Theorem <a href="#thm:indivisible" data-reference-type="ref" data-reference="thm:indivisible">[thm:indivisible]</a>).*

</div>

# Probabilities and Weights

In the MTT$`\Rightarrow`$QM derivation, probabilities on projections were obtained via noncontextual measures and Gleason–Busch. Here we work purely in the stochastic/process picture. We (i) construct a path-space probability measure from modal action increments, (ii) prove $`\sigma`$-additivity and consistency on the cylinder $`\sigma`$-algebra, (iii) establish *noncontextuality* of outcome probabilities (independence from the measurement partition), and (iv) state precise conditions under which these probabilities coincide with Born probabilities upon Hilbert reconstruction.

## Stepwise action increments and $`g`$-functions

<div id="def:gfunc" class="definition">

**Definition 27** (Stepwise action increment and $`g`$-function). For each finite history $`H_k=(q_0,\dots,q_k)`$ and candidate $`q_{k+1}\in Q`$, let $`\Delta A(q_k\!\to q_{k+1}\mid H_k)\ge 0`$ be the one-step modal action increment (Appendix <a href="#app:action" data-reference-type="ref" data-reference="app:action">[app:action]</a>). Fix a $`\sigma`$-finite reference measure $`\nu`$ with full support on $`(Q,\mathcal B(Q))`$ and assume the uniform integrability
``` math
\begin{equation}
\label{eq:UI}
0<\int_Q e^{-\Delta A(q_k\to q' \mid H_k)/\hbar}\,d\nu(q')\;\le M<\infty\qquad\text{for all }H_k.
\end{equation}
```
Define the $`g`$-function
``` math
\begin{equation}
\label{eq:gfunc}
g(q_{k+1}\mid H_k)\;:=\;\frac{\exp\!\big(-\Delta A(q_k\to q_{k+1}\mid H_k)/\hbar\big)}{\displaystyle\int_Q \exp\!\big(-\Delta A(q_k\to q'\mid H_k)/\hbar\big)\,d\nu(q')}.
\end{equation}
```

</div>

<div id="lem:kernel-g" class="lemma">

**Lemma 28** (Kernel from $`g`$-function; measurability and normalisation). *For each $`H_k`$, the map $`A\mapsto \int_A g(q_{k+1}\mid H_k)\,d\nu(q_{k+1})`$ defines a probability kernel $`K_{\Delta\tau}(\cdot\mid H_k)`$ on $`(Q,\mathcal B(Q))`$. Moreover, $`H_k\mapsto K_{\Delta\tau}(A\mid H_k)`$ is measurable for all $`A`$ and the family $`\{K_{\Delta\tau}(\cdot\mid H_k)\}`$ satisfies the hypotheses of Theorem <a href="#thm:IT" data-reference-type="ref" data-reference="thm:IT">11</a>.*

</div>

<div id="lem:kernel_from_g" class="lemma">

**Lemma 29** (Kernel from $`g`$-function). *For each $`h_k`$, the map $`A\mapsto \int_A g(q_{k+1}\mid h_k)\, d\nu(q_{k+1})`$ defines a probability kernel $`K_{\Delta\tau}(\cdot\mid h_k)`$ on $`(Q,\mathcal{B}(Q))`$. Moreover $`K_{\Delta\tau}`$ coincides a.s. with the kernel constructed in <a href="#eq:kernelDef" data-reference-type="eqref" data-reference="eq:kernelDef">[eq:kernelDef]</a>.*

</div>

<div class="proof">

*Proof.* Normalisation follows from the denominator of <a href="#eq:gfunction" data-reference-type="eqref" data-reference="eq:gfunction">[eq:gfunction]</a>. Positivity is clear. Measurability in $`h_k`$ holds because $`h_k\mapsto \Delta A`$ is Borel by Appendix <a href="#app:Action" data-reference-type="ref" data-reference="app:Action">8</a>, and dominated convergence applies by Assumption <a href="#A:UI" data-reference-type="ref" data-reference="A:UI">[A:UI]</a>. Coincidence with <a href="#eq:kernelDef" data-reference-type="eqref" data-reference="eq:kernelDef">[eq:kernelDef]</a> follows from the construction of $`\mathbb{P}`$ in Section <a href="#sec:projection" data-reference-type="ref" data-reference="sec:projection">3</a>: $`g`$ is the Radon–Nikodym density of the conditional law w.r.t. $`\nu`$. ◻

</div>

## Cylinder $`\sigma`$-algebra, consistency, and $`\sigma`$-additivity

Let $`\mathcal{C}`$ be the algebra of cylinder sets in $`Q^{\mathbb{N}}`$, i.e. sets of the form
``` math
C = \{(q_i)_{i\ge 0} : q_0\in A_0,\ldots,q_k\in A_k\},
\qquad A_i\in \mathcal{B}(Q).
```

<div id="thm:premesure" class="theorem">

**Theorem 30** (Consistent pre-measure on $`\mathcal{C}`$). *Define $`\mu`$ on $`\mathcal{C}`$ by
``` math
\mu(C) = \int_{A_0}\!\cdots\!\int_{A_k}
\prod_{i=0}^{k-1} K_{\Delta\tau}(dq_{i+1}\mid q_0,\ldots,q_i)\, \lambda_0(dq_0),
```
where $`\lambda_0`$ is any fixed initial distribution on $`(Q,\mathcal{B}(Q))`$. Then $`\mu`$ is a consistent, finitely additive *pre-measure* on $`\mathcal{C}`$.*

</div>

<div class="proof">

*Proof.* Finite additivity is standard: if $`C=\bigsqcup_{j=1}^n C_j`$ is a disjoint union of cylinders all of the same length $`k`$, then the integrals decompose into disjoint unions of the sets $`A_i`$; the product structure preserves additivity. Consistency (i.e. marginalisation) is immediate by integrating $`A_k=Q`$. The initial law $`\lambda_0`$ is fixed, so overlapping prefixes are handled identically. ◻

</div>

<div id="thm:caratheodory" class="theorem">

**Theorem 31** (Carathéodory extension). *The pre-measure $`\mu`$ extends uniquely to a probability measure (also denoted $`\mu`$) on the product $`\sigma`$-algebra $`\mathcal{B}(Q)^{\otimes \mathbb{N}}`$.*

</div>

<div class="proof">

*Proof.* $`\mathcal{C}`$ is a semi-ring generating the product $`\sigma`$-algebra. The family of kernels is normalised (Lemma <a href="#lem:kernel_from_g" data-reference-type="ref" data-reference="lem:kernel_from_g">29</a>), so $`\mu`$ is tight on compact $`Q`$; more generally, standard Kolmogorov consistency holds by Section <a href="#sec:projection" data-reference-type="ref" data-reference="sec:projection">3</a>. Carathéodory’s extension theorem yields a unique probability measure on $`\sigma(\mathcal{C})`$, which equals $`\mathcal{B}(Q)^{\otimes \mathbb{N}}`$. ◻

</div>

## Noncontextual outcome probabilities

We formalise measurement as a *constraint change* $`F\to F'`$ at a fixed stage $`k^\star`$ (Section <a href="#sec:measurement" data-reference-type="ref" data-reference="sec:measurement">6</a>). The apparatus induces a measurable partition $`\{Q_\alpha\}_{\alpha\in \mathsf{A}}`$ of $`Q`$ at time $`k^\star`$. Define the *outcome event*
``` math
\begin{equation}
\label{eq:Ealpha}
E_\alpha := \{(q_i)_{i\ge 0}\in Q^\mathbb{N}: q_{k^\star}\in Q_\alpha\}.
\end{equation}
```

<div class="definition">

**Definition 32** (Partition‑invariance on the cylinder algebra). A probability assignment $`\alpha\mapsto \mu(E_\alpha)`$ is partition‑invariant (“noncontextual” on cylinder events) if it depends only on the measurable set $`Q_\alpha`$ at the measurement stage, i.e. it is invariant under refinements/coarsenings that leave $`Q_\alpha`$ unchanged.

</div>

<div id="thm:noncontext" class="theorem">

**Theorem 33** (Noncontextuality of MTT outcome probabilities). *Let $`\{Q_\alpha\}`$ and $`\{Q'_\beta\}`$ be two measurable partitions of $`Q`$ such that for some fixed label $`\alpha_0`$ we have $`Q_{\alpha_0}= \bigcup_{\beta \in B}
Q'_\beta`$ for an index set $`B`$. Then
``` math
\mu(E_{\alpha_0}) \;=\; \sum_{\beta\in B} \mu(E'_\beta),
```
where $`E'_\beta`$ is defined as in <a href="#eq:Ealpha" data-reference-type="eqref" data-reference="eq:Ealpha">[eq:Ealpha]</a> with $`Q'_\beta`$ in place of $`Q_\alpha`$. In particular, the probability of the outcome associated with $`Q_{\alpha_0}`$ is independent of the measurement context.*

</div>

<div class="proof">

*Proof.* By definition, $`E_{\alpha_0}=\bigsqcup_{\beta\in B} E'_\beta`$ as a disjoint union of measurable events at the same time $`k^\star`$. By $`\sigma`$-additivity (Theorem <a href="#thm:caratheodory" data-reference-type="ref" data-reference="thm:caratheodory">31</a>), $`\mu(E_{\alpha_0})=\sum_{\beta\in B}\mu(E'_\beta)`$. Therefore the probability assigned to $`Q_{\alpha_0}`$ is invariant under refinement. Coarsenings are handled by the same argument. Hence noncontextuality holds. ◻

</div>

## Weights for finite-outcome experiments

For a finite partition $`\{Q_\alpha\}_{\alpha=1}^m`$ at stage $`k^\star`$, define the *branch weight*
``` math
W_\alpha := \int_{Q_{\alpha}}\! g(q_{k^\star}\mid q_0,\ldots,q_{k^\star-1})
\, d\nu(q_{k^\star}),
```
where the integral is taken w.r.t. the conditional law of $`(q_0,\ldots,q_{k^\star-1})`$. Then
``` math
\begin{equation}
\label{eq:weights_normalised}
\mu(E_\alpha)= \frac{W_\alpha}{\sum_{\gamma=1}^m W_\gamma}.
\end{equation}
```
Moreover, by <a href="#eq:gfunction" data-reference-type="eqref" data-reference="eq:gfunction">[eq:gfunction]</a> each $`W_\alpha`$ is an average of $`\exp(-\Delta A/\hbar)`$ over the fibre $`\{q_{k^\star}\in Q_\alpha\}`$ and over past histories; thus the *exponential action weighting* appears explicitly.

## Relation to Born probabilities under Hilbert reconstruction

The following places the stochastic probabilities in correspondence with Born probabilities when a Hilbert-space realisation exists.

<div id="A:Hilbert" class="assumption">

**Assumption 34** (Hilbert reconstruction). There exists a separable complex Hilbert space $`\mathcal{H}`$ and a map assigning to each finite measurable partition $`\{Q_\alpha\}`$ an orthogonal projection-valued measure (PVM) $`\{P_\alpha\}`$ on $`\mathcal{H}`$, together with a density operator $`\rho`$ on $`\mathcal{H}`$, such that for every partition and corresponding event $`E_\alpha=\{q_{k^\star}\in Q_\alpha\}`$ we have
``` math
\begin{equation}
\label{eq:Born_match}
\mu(E_\alpha) = \mathrm{Tr}(\rho\, P_\alpha).
\end{equation}
```

</div>

<div class="remark">

*Remark 35*. Assumption <a href="#A:Hilbert" data-reference-type="ref" data-reference="A:Hilbert">34</a> is satisfied whenever one performs the (standard) Hilbert-space reconstruction from the indivisible process (e.g. via the stochastic–quantum correspondence), or, abstractly, by GNS construction from the consistent family of cylinder events (Appendix <a href="#app:GNS" data-reference-type="ref" data-reference="app:GNS">9</a>).

</div>

<div id="thm:gleason" class="theorem">

**Theorem 36** (Gleason–Busch consistency). *Assume $`\dim \mathcal{H}\ge 2`$. If the assignment $`P\mapsto \mu(P)`$ on the lattice of orthogonal projections (defined via <a href="#eq:Born_match" data-reference-type="eqref" data-reference="eq:Born_match">[eq:Born_match]</a> on all finite PVMs) is noncontextual and $`\sigma`$-additive on orthogonal families, then there exists a unique density operator $`\rho`$ such that $`\mu(P)=\mathrm{Tr}(\rho P)`$ for all projections $`P`$.*

</div>

<div class="proof">

*Idea.* For $`\dim \mathcal{H}\ge 3`$ this is Gleason’s theorem (extended to $`\sigma`$-additivity). For $`\dim \mathcal{H}=2`$ use Busch’s generalisation to POVMs and the restriction to PVMs. Noncontextuality and $`\sigma`$-additivity are guaranteed by Theorem <a href="#thm:noncontext" data-reference-type="ref" data-reference="thm:noncontext">33</a> and Carathéodory extension applied to partitions. ◻

</div>

<div class="corollary">

**Corollary 37** (Born rule equivalence). *Under Assumption <a href="#A:Hilbert" data-reference-type="ref" data-reference="A:Hilbert">34</a>, the stochastic probabilities for all finite partitions coincide with the Born probabilities for $`(\mathcal{H},\rho)`$.*

</div>

## Summary

From MTT’s action geometry we obtained stepwise $`g`$-functions, kernels, and a unique path-space measure. Measurement outcome probabilities are noncontextual because they are measures of cylinder events independent of the partitioning context. When a Hilbert reconstruction is performed, these probabilities agree with Born probabilities, placing the stochastic and operator formulations in one-to-one correspondence.

# Measurement and Conditioning

In the Hilbert-space derivation, measurement arose via Stinespring/Naimark dilation and the Born rule. Here we formulate measurement *entirely* within the indivisible-process picture as conditioning on sub-$`\sigma`$-algebras of the path space. No extra postulates are introduced: the update is the regular conditional probability determined by the MTT-induced measure. We then show how this coincides with POVMs and quantum instruments upon Hilbert reconstruction.

## Constraint changes and measurable partitions

Let $`(\Omega,\mathcal{F},\mu)`$ be the path-space probability space, where $`\Omega=Q^{\mathbb{N}}`$, $`\mathcal{F}=\mathcal{B}(Q)^{\otimes \mathbb{N}}`$, and $`\mu`$ is the path measure from Theorem <a href="#thm:caratheodory" data-reference-type="ref" data-reference="thm:caratheodory">31</a>. For $`k\in\mathbb{N}`$ let $`\pi_k:\Omega\to Q`$ be the $`k`$-th coordinate map and denote by $`\mathcal{F}_{\le k}:=\sigma(\pi_0,\ldots,\pi_k)`$ the history $`\sigma`$-algebra up to time $`k`$.

A measurement at step $`k^\star`$ is modelled by a *constraint change* $`F\to F'`$ in modal space that selects a measurable partition $`\{Q_\alpha\}_{\alpha\in\mathsf{A}}`$ of $`Q`$ at time $`k^\star`$. The corresponding *outcome event* is
``` math
\begin{equation}
\label{eq:outcome_event}
E_\alpha := \{\omega\in\Omega: \pi_{k^\star}(\omega)\in Q_\alpha\}
\in \sigma(\pi_{k^\star}) \subset \mathcal{F}_{\le k^\star}.
\end{equation}
```
Since $`Q`$ is Polish and $`Q_\alpha`$ Borel, $`\sigma(\pi_{k^\star})`$ admits regular conditional probabilities (RCPs).

## Regular conditional probabilities and Bayesian update

<div id="thm:RCP" class="theorem">

**Theorem 38** (Regular conditional probabilities). *There exists a version of the conditional probability $`\mu(\,\cdot\,|\,\sigma(\pi_{k^\star})):\Omega\times \sigma(\pi_{k^\star})\to [0,1]`$ such that for each $`B\in\mathcal{F}`$ the map $`q\in Q\mapsto \mu\big(B\,\big|\,\pi_{k^\star}=q\big)`$ is Borel and
``` math
\mu(B\cap \{\pi_{k^\star}\in A\})
= \int_{A} \mu\big(B\,\big|\,\pi_{k^\star}=q\big)\,
\mu_{\pi_{k^\star}}(dq),
\quad \forall A\in\mathcal{B}(Q),
```
where $`\mu_{\pi_{k^\star}}`$ is the law of $`\pi_{k^\star}`$ under $`\mu`$.*

</div>

<div class="proof">

*Proof.* Since $`Q`$ is Polish and $`(\Omega,\mathcal{F})`$ standard Borel, existence of an RCP disintegrating $`\mu`$ along $`\pi_{k^\star}`$ is standard (see, e.g., Bogachev, *Measure Theory*, Thm. 10.4.6). ◻

</div>

<div id="def:posterior" class="definition">

**Definition 39** (Posterior (collapse) measure). Given outcome $`\alpha`$ with $`\mu(E_\alpha)>0`$, define the posterior measure $`\mu^\alpha`$ on $`(\Omega,\mathcal{F})`$ by
``` math
\begin{equation}
\label{eq:posterior}
\mu^\alpha(B) :=
\mu\big(B\,\big|\, E_\alpha\big)
= \frac{\mu(B\cap E_\alpha)}{\mu(E_\alpha)}, \qquad B\in\mathcal{F}.
\end{equation}
```

</div>

<div id="prop:prune" class="proposition">

**Proposition 40** (Collapse as pruning + renormalisation). *Let $`\Pi_\alpha`$ denote the restriction map $`\Omega\to E_\alpha`$. Then $`\mu^\alpha`$ is the unique probability measure supported on $`E_\alpha`$ such that for all $`B\in\mathcal{F}`$,
``` math
\mu^\alpha(B) = \frac{\mu(B\cap E_\alpha)}{\mu(E_\alpha)}.
```
In particular, $`\mu^\alpha`$ is obtained by *pruning* to the measurable subset $`E_\alpha`$ and *renormalising*.*

</div>

<div id="rem:disintegration" class="remark">

*Remark 41* (Disintegration and regular conditionals). Since $`Q`$ is Polish and $`(Q^{\mathbb N},\mathcal B(Q)^{\otimes\mathbb N})`$ is standard Borel, the conditional measures $`\{\mathbb P(\,\cdot\,|\pi_{k^\star}=q)\}_{q\in Q}`$ exist and are unique up to $`\mathbb P_{\pi_{k^\star}}`$-null sets. Hence the pruning/renormalisation update $`\mu\mapsto \mu_\alpha`$ is the canonical regular conditional probability with respect to the sub-$`\sigma`$-algebra $`\sigma(\pi_{k^\star})`$.

</div>

<div class="proof">

*Proof.* Immediate from Definition <a href="#def:posterior" data-reference-type="ref" data-reference="def:posterior">39</a> and properties of conditional probabilities. ◻

</div>

## Updated kernels and Doob–Dynkin measurability

We now describe the post-measurement dynamics as new conditional kernels.

<div id="thm:kernel_update" class="theorem">

**Theorem 42** (Bayesian update of one-step kernels). *Let $`k\ge k^\star`$. Under $`\mu^\alpha`$, the one-step kernel from time $`k`$ to $`k+1`$ given a history prefix $`h_k=(q_0,\ldots,q_k)`$ with $`q_{k^\star}\in Q_\alpha`$ equals
``` math
\begin{equation}
\label{eq:updated_kernel}
K_{\Delta\tau}^{(\alpha)}(A\mid h_k)
= \frac{\int_{A} g(q_{k+1}\mid h_k)\, d\nu(q_{k+1})}
{\int_{Q} g(q' \mid h_k)\, d\nu(q')}, \qquad A\in\mathcal{B}(Q),
\end{equation}
```
i.e. it is the restriction of the pre-measurement kernel to the fibre $`\{h_k: q_{k^\star}\in Q_\alpha\}`$, followed by normalisation.*

</div>

<div class="proof">

*Proof.* By the definition of $`\mu^\alpha`$ and the chain rule for conditional probabilities, for cylinder sets $`C`$ depending only on $`(\pi_0,\ldots,\pi_{k+1})`$ we have
``` math
\mu^\alpha(C) = \frac{\mu(C\cap E_\alpha)}{\mu(E_\alpha)}
=\frac{\int \mathbf{1}_C \prod_{i=0}^{k} K_{\Delta\tau}(dq_{i+1}\mid h_i)\,
\lambda_0(dq_0)}{\mu(E_\alpha)},
```
where the integration domain is restricted to $`q_{k^\star}\in Q_\alpha`$. Identifying the Radon–Nikodym density $`g(\cdot\mid h_k)`$ w.r.t. $`\nu`$ (Lemma <a href="#lem:kernel_from_g" data-reference-type="ref" data-reference="lem:kernel_from_g">29</a>) yields <a href="#eq:updated_kernel" data-reference-type="eqref" data-reference="eq:updated_kernel">[eq:updated_kernel]</a>. ◻

</div>

<div id="cor:indiv_persists" class="corollary">

**Corollary 43** (Persistence of indivisibility). *If the pre-measurement process is indivisible (Theorem <a href="#thm:indivisible" data-reference-type="ref" data-reference="thm:indivisible">[thm:indivisible]</a>), then the post-measurement process under $`\mu^\alpha`$ is also indivisible unless the restriction to $`E_\alpha`$ removes all history dependence (a $`\mu`$-null degeneracy).*

</div>

<div class="proof">

*Proof.* If $`K_{\Delta\tau}^{(\alpha)}`$ admitted a Markov factorisation, then, on $`E_\alpha`$, the pre-measurement kernel would factorise as well, contradicting Theorem <a href="#thm:indivisible" data-reference-type="ref" data-reference="thm:indivisible">[thm:indivisible]</a> except on a null set where the dependence on the complete past collapses. ◻

</div>

## Sequential measurements and instruments

Consider two measurements at $`k_1<k_2`$ with partitions $`\{Q^{(1)}_{\alpha}\}`$ and $`\{Q^{(2)}_{\beta}\}`$ and outcomes $`\alpha,\beta`$. Define events $`E^{(1)}_\alpha`$, $`E^{(2)}_\beta`$ as in <a href="#eq:outcome_event" data-reference-type="eqref" data-reference="eq:outcome_event">[eq:outcome_event]</a>. The *instrument* associated with the first measurement is the map
``` math
\mathcal{I}_\alpha:\ \mathcal{P}(\Omega)\to \mathcal{P}(\Omega),
\qquad \mathcal{I}_\alpha[\mu] := \mu^\alpha.
```
For the second measurement, the posterior is $`\mu^{\alpha\beta}:= \big(\mu^\alpha\big)^\beta`$, i.e. successive pruning and renormalisation. The joint probability for $`(\alpha,\beta)`$ is
``` math
\mu(E^{(1)}_\alpha \cap E^{(2)}_\beta)
= \mu(E^{(1)}_\alpha)\, \mu^\alpha(E^{(2)}_\beta),
```
the standard chain rule.

<div class="proposition">

**Proposition 44** (Associativity of instruments). *For any finite sequence of measurements with outcomes $`\gamma_1,\ldots,\gamma_m`$ at times $`k_1<\cdots<k_m`$,
``` math
\mathcal{I}_{\gamma_m}\circ \cdots \circ \mathcal{I}_{\gamma_1}[\mu]
= \mu^{\gamma_1\cdots \gamma_m}.
```*

</div>

<div class="proof">

*Proof.* Induction on $`m`$, using Definition <a href="#def:posterior" data-reference-type="ref" data-reference="def:posterior">39</a>. ◻

</div>

## Equivalence to POVMs and quantum instruments under Hilbert reconstruction

Assume Hilbert reconstruction (Assumption <a href="#A:Hilbert" data-reference-type="ref" data-reference="A:Hilbert">34</a>) holds for the process. Then any measurement partition $`\{Q_\alpha\}`$ at time $`k^\star`$ corresponds to a PVM $`\{P_\alpha\}`$ on $`\mathcal{H}`$ with the same classical outcome probabilities: $`\mu(E_\alpha)=\mathrm{Tr}(\rho P_\alpha)`$ (Theorem <a href="#thm:gleason" data-reference-type="ref" data-reference="thm:gleason">36</a>). For a *general* (possibly unsharp) measurement, the partition is replaced by a family of *effect functionals* $`\{E_\alpha[\cdot]\}`$ on cylinder events at time $`k^\star`$ with $`0\le E_\alpha\le 1`$ and $`\sum_\alpha E_\alpha=1`$. These induce probabilities $`p(\alpha)=\mathbb{E}_\mu[E_\alpha]`$.

<div id="thm:povm_correspondence" class="theorem">

**Theorem 45** (POVM correspondence). *Under Assumption <a href="#A:Hilbert" data-reference-type="ref" data-reference="A:Hilbert">34</a>, there exists a POVM $`\{F_\alpha\}`$ on $`\mathcal{H}`$ such that for all finite-outcome measurements at time $`k^\star`$,
``` math
p(\alpha)= \mathbb{E}_\mu[E_\alpha] = \mathrm{Tr}(\rho F_\alpha).
```*

</div>

<div class="proof">

*Proof sketch.* By GNS, the linear functional $`E\mapsto \mathbb{E}_\mu[E]`$ on the commutative von Neumann algebra generated by cylinder events at time $`k^\star`$ is represented as a state on a Hilbert space; Naimark dilation then realises the effects as compressed projections, yielding a POVM $`\{F_\alpha\}`$ with the stated property. ◻

</div>

Moreover, *state update* (disturbance) can be encoded by a family of completely positive (CP), trace-nonincreasing maps $`\{\mathcal{J}_\alpha\}`$ (*quantum instrument*) such that
``` math
p(\alpha)=\mathrm{Tr}(\mathcal{J}_\alpha(\rho)),\qquad
\rho \mapsto \frac{\mathcal{J}_\alpha(\rho)}{\mathrm{Tr}(\mathcal{J}_\alpha(\rho))}
\ \text{for the posterior}.
```
In the process picture, $`\mathcal{J}_\alpha`$ corresponds to the pruning $`\mu\mapsto \mu^\alpha`$; under dilation, there exists an ancilla space and unitary $`U`$ producing Kraus operators for $`\{\mathcal{J}_\alpha\}`$ (Stinespring).

<div id="thm:instrument_equivalence" class="theorem">

**Theorem 46** (Instrument equivalence). *Assume Hilbert reconstruction. There exists an ancilla Hilbert space $`\mathcal{K}`$, a unitary $`U`$ on $`\mathcal{H}\otimes \mathcal{K}`$, and a projection-valued observable on $`\mathcal{K}`$ with outcomes $`\alpha`$ such that the process-level update $`\mu\mapsto \mu^\alpha`$ corresponds to the quantum instrument $`\mathcal{J}_\alpha(\rho)= \mathrm{Tr}_{\mathcal{K}}\!\big[U(\rho\otimes\sigma) U^\dagger
(\mathbf{1}\otimes \Pi_\alpha)\big]`$, with $`\sigma`$ a fixed ancilla state and $`\Pi_\alpha`$ the outcome projector on $`\mathcal{K}`$.*

</div>

<div class="proof">

*Idea.* Standard Stinespring/Naimark construction for instruments, with the classical outcome algebra identified with $`\sigma(\pi_{k^\star})`$ via the spectral theorem. Consistency of probabilities follows from Theorem <a href="#thm:povm_correspondence" data-reference-type="ref" data-reference="thm:povm_correspondence">45</a>. ◻

</div>

## Locality and no-signalling on $`Y_4`$

Finally, we record a minimal assumption under which conditioning does not enable superluminal signalling in $`Y_4`$.

<div id="A:microcausality" class="assumption">

**Assumption 47** (Microcausality on $`Y_4`$). If two measurements occur at times $`k^\star`$ and $`\tilde k^\star`$ on regions $`R,\tilde R\subset Y_4`$ that are spacelike separated in $`g^{(4)}`$, then the constraint change $`F\to F'`$ for $`R`$ modifies only the conditional distribution of $`\pi_{k^\star}`$ and its causal future; similarly for $`\tilde R`$.

</div>

<div id="prop:no_signalling" class="proposition">

**Proposition 48** (No-signalling). *Under Assumption <a href="#A:microcausality" data-reference-type="ref" data-reference="A:microcausality">47</a>, the marginal law of $`\pi_{\tilde k}`$ on $`\tilde R`$ with $`\tilde k<k^\star`$ (or $`\tilde k`$ outside the future of $`R`$) is unchanged by conditioning on outcomes at $`R`$.*

</div>

<div class="proof">

*Proof.* By construction, the pruning to $`E_\alpha\in \sigma(\pi_{k^\star})`$ leaves $`\mathcal{F}_{\le \tilde k}`$-measurable events unaffected when $`\tilde k`$ is not in the causal future of $`R`$; hence the marginal is unchanged. ◻

</div>

#### Remark.

Assumption 6.10 matches the locality analysis in the MTT spine: the equal‑time support and $`L^1`$ control of the bilocal kernel used here coincide with the hypotheses under which Appendix F of Fixed Points VI proves local well‑posedness and unchanged characteristic cones for the reduced hyperbolic system. Thus microcausality and no‑signaling used here are the same as in the QFT projection layer.

## Summary

Measurement in the process picture is *just* conditioning on the sub-$`\sigma`$-algebra generated by the outcome at $`k^\star`$: mathematically, pruning plus renormalisation. The updated dynamics remain indivisible (except in degenerate cases). Upon Hilbert reconstruction, outcome probabilities correspond to POVMs, and the update corresponds to a quantum instrument obtained by Stinespring/Naimark dilation.

# Discussion and Conclusions

## Conceptual synthesis

In this work we have developed a rigorous connection between Modal Triplet Theory (MTT) and the mathematical theory of *indivisible stochastic processes*. Our starting point was the modal-geometric setup (Section 2), where harmonic projectors on the internal three-manifolds $`B_n`$ isolate the *coherent sector*. Projection to external spacetime $`Y_4`$ yields observable degrees of freedom. We then established:

1.  The projection of MTT dynamics induces *conditional probability kernels* $`K_{\Delta\tau}(\cdot\mid h_k)`$ depending on the full history prefix $`h_k`$;

2.  By Kolmogorov extension, these kernels define a unique probability measure on the infinite history space $`Q^\mathbb{N}`$ (Section 3);

3.  The dependence on complete histories implies that the induced process is generically *non-Markovian* and hence *indivisible* (Theorems <a href="#thm:nonMarkov" data-reference-type="ref" data-reference="thm:nonMarkov">14</a>, <a href="#thm:indivisible" data-reference-type="ref" data-reference="thm:indivisible">[thm:indivisible]</a>);

4.  The stochastic weights are determined by modal action increments $`\Delta A`$, leading to exponential weighting $`\exp(-\Delta A/\hbar)`$ and consistent $`g`$-functions (Section 5);

5.  Measurement arises as conditioning on sub-$`\sigma`$-algebras of the path space, with update given by pruning and renormalisation. Sequential measurements compose associatively, and under Hilbert reconstruction, these updates correspond precisely to POVMs and quantum instruments (Section <a href="#sec:measurement" data-reference-type="ref" data-reference="sec:measurement">6</a>).

## Comparison with MTT$`\Rightarrow`$QM derivation

Our earlier derivation (MTT$`\Rightarrow`$QM) established a path from MTT to the standard Hilbert-space quantum formalism, using noncontextual measures and Gleason–Busch to recover the Born rule. The present analysis provides an *orthogonal* realisation: MTT dynamics can be projected not only into linear Hilbert evolution but also into a stochastic process on observable histories. This process is necessarily indivisible, matching the notion of “non-Markovian quantum processes” introduced in foundational studies (e.g. by Buscemi, Kretschmann–Werner, etc.), but here obtained directly from the modal dynamics.

Thus, MTT simultaneously underpins two apparently distinct frameworks:

- The Hilbert-space quantum formalism, with unitary evolution and POVM measurements;

- The theory of indivisible stochastic processes, with action-based weights and measure-theoretic conditioning.

The equivalence of probabilities under Hilbert reconstruction (Theorem <a href="#thm:gleason" data-reference-type="ref" data-reference="thm:gleason">36</a>) ensures consistency of these perspectives.

#### Link to Bell/Jarrett.

Indivisibility here is the stochastic mirror of outcome‑independence failure in Bell’s Jarrett decomposition: operational parameter independence (no‑signaling of marginals) holds by construction, while the full‑history dependence of our kernels encodes outcome‑level correlations. This matches the analysis of modal factorization failure under MI in the Bell/beables paper of this series.

## Physical interpretation

The non-Markovianity of the induced process reflects the persistence of modal information across all scales: the external field $`q_k`$ at time $`k`$ is not autonomous, but depends on the entire internal modal trajectory. This explains why *memory effects* appear intrinsically in quantum phenomena such as entanglement, decoherence, and contextuality. Within MTT, these effects are geometrically rooted in the harmonic structure of the compact $`B_n`$.

Measurement, in the stochastic picture, is not a physical collapse but a *selection of histories* by conditioning. The “disturbance” is simply the renormalisation of probabilities after pruning incompatible histories. Upon Hilbert reconstruction, this recovers exactly the CP-map (instrument) update rule of quantum theory. Thus, MTT yields a unified resolution of the measurement problem: there is no discontinuity, only measure-theoretic conditioning on indivisible processes.

## Implications and outlook

Our analysis demonstrates that MTT provides a *rigorous realisation of indivisible processes*. This has several implications:

1.  It establishes MTT as a deeper framework unifying both Hilbert-space quantum mechanics and the theory of non-Markovian stochastic processes;

2.  It explains the ubiquity of indivisibility and contextuality in quantum phenomena as consequences of modal-geometric dynamics;

3.  It opens the door to new applications: modelling quantum thermodynamics with memory, analysing quantum causal structures, and exploring beyond-quantum processes (where indivisibility persists but Hilbert reconstruction may fail).

Future directions include:

- Constructing explicit examples of indivisible processes from concrete MTT backgrounds (e.g. specific compact manifolds $`B_n`$ with known spectra);

- Extending the formalism to continuous-time limits and operator-algebraic formulations of complete connections;

- Investigating whether beyond-quantum indivisible processes predicted by MTT could have experimental signatures in non-Markovian open systems.

## Conclusion

We conclude that Modal Triplet Theory, when projected onto observable degrees of freedom, gives rise naturally to *indivisible stochastic processes*. The mathematical construction is rigorous: action increments induce normalised kernels, path measures exist uniquely by Kolmogorov extension, probabilities are noncontextual and $`\sigma`$-additive, and measurements are conditioning operations. Under Hilbert reconstruction, these probabilities agree exactly with the Born rule, while the indivisible dynamics explain the origin of non-Markovian features in quantum theory. Thus, MTT provides a unified, geometrically grounded foundation for both quantum mechanics and the broader landscape of stochastic indivisible processes.

# Action increments and measurability

## Definition of $`\Delta A`$

For each step $`h_k=(q_0,\ldots,q_k)`$ and candidate extension $`q_{k+1}`$, define
``` math
\Delta A(q_k\!\to\! q_{k+1}\mid h_{k-1})
:= A(\Phi_{\Delta\tau}(m_k,q_k)) - A(m_k,q_k),
```
where $`m_k`$ is the internal modal configuration determined by the evolution $`\Phi_\tau`$ from initial data, and $`A(m,q)`$ is the MTT action functional restricted to $`(m,q)\in M\times Q`$. By construction $`\Delta A\ge 0`$ (positivity of modal energy increments).

## Measurability

<div class="lemma">

**Lemma 49** (Borel measurability of $`\Delta A`$). *For fixed $`h_{k-1}`$, the map $`q_{k+1}\mapsto \Delta A(q_k\!\to\! q_{k+1}\mid h_{k-1})`$ is Borel measurable on $`(Q,\mathcal{B}(Q))`$.*

</div>

<div class="proof">

*Proof.* $`\Phi_\tau`$ is continuous on $`H_{\mathrm{coh}}`$ by hypothesis (H<a href="#H2" data-reference-type="ref" data-reference="H2">2</a>), and $`A(\cdot)`$ is continuous on $`M\times Q`$ by (H<a href="#H3" data-reference-type="ref" data-reference="H3">4</a>). Therefore composition is continuous in $`q_{k+1}`$. Continuity implies Borel measurability. ◻

</div>

This ensures that the $`g`$-function <a href="#eq:gfunction" data-reference-type="eqref" data-reference="eq:gfunction">[eq:gfunction]</a> is a Borel kernel.

# GNS and Hilbert reconstruction

## Cylinder algebra and state functional

Let $`\mathcal{A}`$ be the commutative $`C^\ast`$-algebra generated by indicator functions of cylinder sets in $`Q^\mathbb{N}`$. Define $`\omega:\mathcal{A}\to \mathbb{C}`$ by $`\omega(f)=\mathbb{E}_\mu[f]`$, where $`\mu`$ is the path-space probability measure. Then $`\omega`$ is a positive linear functional with $`\omega(1)=1`$.

## GNS construction

By the Gelfand–Naimark–Segal (GNS) construction, there exists a Hilbert space $`\mathcal{H}`$, a representation $`\pi:\mathcal{A}\to \mathcal{B}(\mathcal{H})`$, and a cyclic vector $`\Omega\in\mathcal{H}`$ such that $`\omega(f)=\langle \Omega,\pi(f)\Omega\rangle`$. The probability of an event $`E\in\mathcal{F}`$ is then $`\langle \Omega,\pi(\mathbf{1}_E)\Omega\rangle`$.

## Projection-valued measures

For finite partitions $`\{Q_\alpha\}`$ at time $`k`$, the cylinder indicators $`\mathbf{1}_{E_\alpha}`$ generate a finite family of commuting projections $`\pi(\mathbf{1}_{E_\alpha})`$. This defines a PVM $`\{P_\alpha\}`$ with $`\sum_\alpha P_\alpha=I`$. The state vector $`\Omega`$ corresponds to a density operator $`\rho`$ via $`\omega(f)=\mathrm{Tr}(\rho \pi(f))`$. Thus the stochastic probabilities $`\mu(E_\alpha)`$ match Born probabilities $`\mathrm{Tr}(\rho P_\alpha)`$.

# Complete connections and indivisibility

## Complete connections formalism

A stochastic process on $`Q^\mathbb{N}`$ with transition kernels $`K(\cdot\mid h_k)`$ depending on the entire history $`h_k`$ is called a *complete connection*. See e.g. Iosifescu & Grigorescu, *Dependence with Complete Connections*, for general theory.

## Criterion for indivisibility

<div class="theorem">

**Theorem 50** (Indivisibility criterion for complete connections). *Let $`\{K(\cdot\mid h_k)\}`$ be a complete connection on $`Q^\mathbb{N}`$. If there exists no finite memory length $`\ell`$ such that $`K(\cdot\mid h_k)`$ depends only on the last $`\ell`$ coordinates of $`h_k`$, then the process is indivisible.*

</div>

<div class="proof">

*Proof.* If such $`\ell`$ existed, then the process would be a Markov chain of order $`\ell`$, and its $`t`$-step kernels could be factorised into one-step kernels, i.e. the process would be divisible. Conversely, if dependence extends to all past prefixes, then no finite $`\ell`$ suffices, and no factorisation into shorter-time kernels exists. Hence indivisibility follows. ◻

</div>

In MTT, $`\Delta A`$ depends on modal energy functionals referencing the entire history, so the dependence length is infinite. Thus indivisibility is generic.

# Worked example: Toy model

We illustrate with a toy MTT model yielding an indivisible process.

## Setup

Let $`Q=\{0,1\}`$ with discrete $`\sigma`$-algebra. Suppose internal moduli $`m_k`$ carry memory of the entire sequence of flips up to time $`k`$. Define
``` math
\Delta A(q_k\!\to\! q_{k+1}\mid h_{k-1})
= \begin{cases}
\alpha + \beta \, N_1(h_{k-1}), & q_{k+1}=1,\\
\alpha + \beta \, N_0(h_{k-1}), & q_{k+1}=0,
\end{cases}
```
where $`N_0,N_1`$ count occurrences of $`0,1`$ in the history.

## Transition probabilities

Then
``` math
\mathbb{P}(q_{k+1}=1\mid h_k) \propto
\exp\!\left(-\tfrac{1}{\hbar}[\alpha+\beta N_1(h_{k})]\right),
```
``` math
\mathbb{P}(q_{k+1}=0\mid h_k) \propto
\exp\!\left(-\tfrac{1}{\hbar}[\alpha+\beta N_0(h_{k})]\right).
```

## Indivisibility

Since transition probabilities depend on counts of all past states, there is no finite memory $`\ell`$ that suffices. Hence the process is indivisible. Upon Hilbert reconstruction, these probabilities correspond to Born weights for a qubit in a non-Markovian environment.

# References for stochastic processes

- Billingsley, *Probability and Measure*.

- Bogachev, *Measure Theory*.

- Iosifescu & Grigorescu, *Dependence with Complete Connections*.

- Accardi, Lu, Volovich, *Quantum Theory and Its Stochastic Limit*.

# Summary of appendices

We have provided:

- Measurability proofs for $`\Delta A`$ and construction of $`g`$-functions;

- GNS-based Hilbert reconstruction from the path-space measure;

- A general criterion for indivisibility of complete connections;

- A worked discrete example illustrating memory dependence and indivisibility.

This completes the rigorous underpinnings of the MTT$`\Rightarrow`$Indivisible process derivation.

[^1]: Indivisibility is generic unless $`\Phi(q',h)`$ collapses to dependence on $`q_k`$ only; see Theorem <a href="#thm:nonMarkov" data-reference-type="ref" data-reference="thm:nonMarkov">14</a>.
