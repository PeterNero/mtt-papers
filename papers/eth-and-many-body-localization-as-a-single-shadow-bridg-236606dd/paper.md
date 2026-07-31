---
abstract: |
  This paper replaces a proposed universal equivalence among eigenstate thermalization, many-body localization, and projection-induced basins by a model-dependent operational bridge. We fix a finite random-field XXZ chain, an energy window, an initial-state class, and a family of local observables. Standard diagnostics—eigenstate matrix elements, adjacent-gap ratios, imbalance, and half-chain entanglement—are kept distinct. For a coarse channel followed by microscopic unitary evolution, we derive the exact failure of the reduced maps to form a semigroup. We prove that microscopic unitary dynamics preserves trace distance, that uniform contraction of an effective map is a sufficient but not necessary thermalization criterion, and that the mean-square thermalization error separates exactly into diagonal bias and temporal fluctuation. For a quasi-local integral of motion whose commutator with the Hamiltonian is bounded by $`\eta`$, we derive a memory bound linear in $`\eta |t|`$. These results explain when “mixing basin” and “memory basin” are useful operational descriptions without identifying them with ETH or MBL by definition. No universal logistic or Kramers-type knee follows for a closed quantum chain; a crossover must be estimated with a declared finite-size scaling model and uncertainty analysis. The Modal Triplet Theory interpretation is therefore a conditional pullback problem: its coherent projector, Hessian gap, and capacity margin become relevant only after an explicit intertwiner maps them to the Hamiltonian, coarse channel, observables, and diagnostics used here.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 0e87cda0c6cb602bde35a6107a77382512562d22b6af77baec4b6f290c15de0a
paper_id: eth-and-many-body-localization-as-a-single-shadow-bridg-236606dd
release_state: zenodo_released
released_version: v2
title: |
  **ETH and Many-Body Localization Through an Operational Basin Diagnostic**
  A Model-Dependent Bridge with Exact Coarse-Dynamics Identities
zenodo_doi: 10.5281/zenodo.21717186
zenodo_record_id: 21717186
zenodo_url: "https://zenodo.org/records/21717186"
---

# Version 2 Revision Note

Supersedes.
Version 1, *ETH and Many-Body Localization as a Single Shadow-Bridge Problem*.

Reason.
The earlier version treated thermalization, localization, and monitored transitions as universal basin equivalences; it did not declare a Hamiltonian family; and it imposed a Kramers-type crossover without deriving the stochastic escape process required for that law.

Resolution.
Version 2 fixes a random-field XXZ family and separate diagnostics, replaces equivalences by exact identities and sufficient criteria, derives a quasi-LIOM memory estimate, and gives a finite-size comparison protocol with no universal knee assumption.

Retained content.
The basin language is retained as a useful operational summary of coarse mixing and memory when its metric, map, time window, and state class are declared.

Open boundary.
No current theorem derives the XXZ Hamiltonian, coarse channel, disorder law, thermal reference, or scaling function from one selected MTT source. The thermodynamic ETH–MBL boundary and a general asymptotic MBL phase are not established here.

# Introduction

Thermalization and many-body localization are not merely opposite labels. They are statements about different mathematical objects. Eigenstate thermalization concerns matrix elements of chosen observables in energy eigenstates . Dynamical equilibration concerns the evolution of selected initial states and observables . Many-body localization may be diagnosed through level statistics, eigenstate entanglement, transport, persistent local memory, or quasi-local integrals of motion . These diagnostics are related under additional hypotheses, but they are not definitions of one another.

The earlier version of this paper compressed all of them into a single picture: one dominant basin represented ETH, while many fragmented basins represented MBL. The picture is suggestive but too strong. A basin is defined only after a state space, dynamics, metric, resolution, and time window have been chosen. Different choices can produce different partitions of the same microscopic system. Integrable systems can retain memory without being MBL. Conversely, finite systems can show long crossovers without establishing a thermodynamic phase.

The revised aim is narrower and more useful. We ask when basin language is a faithful *operational summary* of independently specified many-body diagnostics. The answer has three parts:

1.  a declared Hamiltonian and diagnostic record;

2.  exact statements about the relation between unitary and coarse dynamics; and

3.  an explicit interface that MTT would have to satisfy before its projector or stability margin can explain the observed many-body regime.

# Claim tier and scope

## What is proved

All exact results in this paper are finite-dimensional. They hold for a fixed chain length, a fixed disorder realization unless averaging is explicitly stated, and declared maps and observables. We prove:

1.  the exact semigroup defect of an evolve–coarse-grain construction;

2.  preservation of trace distance by microscopic unitary evolution;

3.  exponential convergence under an assumed effective contraction;

4.  an exact decomposition of mean-square thermalization error; and

5.  a memory estimate for an operator that nearly commutes with the Hamiltonian.

## What is not proved

We do not prove ETH or MBL for the entire XXZ family. We do not infer an asymptotic transition from finite exact diagonalization, derive a universal critical disorder, or identify a Hamiltonian level-spacing gap with an MTT fixed-point Hessian gap. Rigorous localization results exist for restricted one-dimensional spin-chain settings and assumptions ; rare-region and avalanche mechanisms make broader stability questions model- and dimension-dependent . The present bridge respects that scope.

# A complete many-body problem record

## Hamiltonian family

For $`L\geq 2`$, let
``` math
\mathcal M_L=(\mathbb{C}^2)^{\otimes L}
```
and impose open boundaries. We use the random-field XXZ Hamiltonian
``` math
\begin{equation}
\label{eq:xxz}
 H_L(\omega;W)
 =
 J\sum_{j=1}^{L-1}
 \left(
 S_j^xS_{j+1}^x+S_j^yS_{j+1}^y+
 \Delta S_j^zS_{j+1}^z
 \right)
 +\sum_{j=1}^{L}h_j(\omega)S_j^z ,
\end{equation}
```
where $`J\neq0`$, $`\Delta\in\mathbb{R}`$, and the $`h_j`$ are independent uniform random variables on $`[-W,W]`$. Numerical comparisons must fix the symmetry sector, here total $`S^z=0`$ for even $`L`$, because unresolved symmetry blocks can create misleading degeneracies and gap statistics. They must also state the boundary condition, energy-density window, disorder seed or sample list, number of samples, and diagonalization tolerance.

## Diagnostic record

Let $`H_L|n\rangle=E_n|n\rangle`$ within the selected sector and energy window. A minimally complete record contains the following distinct rows.

#### Eigenstate matrix elements.

For each declared local observable $`O`$,
``` math
\begin{equation}
\label{eq:eth-matrix}
 O_{mn}=\langle m|O|n\rangle .
\end{equation}
```
An ETH analysis specifies a smooth microcanonical target for $`O_{nn}`$, the width of diagonal residuals, and a scaling test for off-diagonal elements. A statement that trajectories approach one coarse state is not by itself the ETH ansatz.

#### Adjacent-gap ratio.

For ordered levels, define $`\delta_n=E_{n+1}-E_n`$ and
``` math
\begin{equation}
\label{eq:ratio}
 r_n=\frac{\min(\delta_n,\delta_{n+1})}
 {\max(\delta_n,\delta_{n+1})}.
\end{equation}
```
The familiar reference means are approximately $`0.5307`$ for the Gaussian orthogonal ensemble and $`2\log 2-1\approx0.3863`$ for Poisson statistics . These are ensemble diagnostics, not proofs of ETH or MBL.

#### Memory and entanglement.

For the Néel state $`|\psi_{\mathrm N}\rangle`$, one may use
``` math
\begin{equation}
\label{eq:imbalance}
 I_L(t)=\frac{2}{L}\sum_{j=1}^{L}(-1)^j
 \langle\psi_{\mathrm N}|S_j^z(t)|\psi_{\mathrm N}\rangle ,
\end{equation}
```
and the von Neumann entropy $`S_{L/2}(t)`$ of one half of the chain. Persistent imbalance, slow entanglement growth, Poisson-like levels, and area-law eigenstates are complementary evidence. None should silently stand in for all the others.

<div id="def:capsule" class="definition">

**Definition 1** (Comparison capsule). A finite-volume ETH–MBL comparison capsule is the tuple
``` math
\mathfrak C_L=(H_L,\mathcal S_L,\mathcal W_L,\mathcal R_L,
 \mathcal O_L,\mathcal I_L,\mathcal D_L,\mathcal U_L),
```
where $`\mathcal S_L`$ is the symmetry sector, $`\mathcal W_L`$ the energy window, $`\mathcal R_L`$ the disorder law and realized samples, $`\mathcal O_L`$ the observable family, $`\mathcal I_L`$ the initial-state class, $`\mathcal D_L`$ the diagnostics, and $`\mathcal U_L`$ the numerical and statistical uncertainty record.

</div>

Without these rows, a reported crossover cannot be reproduced or compared across sizes.

# Coarse dynamics and its exact defect

## Typed construction

Let $`\mathcal D(\mathcal M_L)`$ and $`\mathcal D(\mathcal K_L)`$ denote microscopic and effective density operators. Let
``` math
\mathcal E:\mathcal D(\mathcal M_L)\to\mathcal D(\mathcal K_L),\qquad
 \mathcal I:\mathcal D(\mathcal K_L)\to\mathcal D(\mathcal M_L)
```
be completely positive trace-preserving maps with $`\mathcal E\mathcal I=\mathbf 1_{\mathcal K}`$. The microscopic channel is
``` math
\mathcal A_t(X)=U_tXU_t^\dagger,\qquad U_t=e^{-itH_L},
```
and the reduced family is
``` math
\begin{equation}
\label{eq:reduced}
 \mathcal T_t=\mathcal E\mathcal A_t\mathcal I.
\end{equation}
```
This is a family of quantum channels. It is not automatically a semigroup.

<div id="thm:defect" class="theorem">

**Theorem 2** (Exact reduced-semigroup defect). *For all $`s,t`$,
``` math
\begin{equation}
\label{eq:defect}
 \mathcal T_{t+s}-\mathcal T_t\mathcal T_s
 =
 \mathcal E\mathcal A_t(\mathbf 1_{\mathcal M}-\mathcal I\mathcal E)\mathcal A_s\mathcal I.
\end{equation}
```
Consequently, $`\{\mathcal T_t\}`$ is a semigroup exactly when the right-hand side vanishes for every $`s,t`$ on the effective state span.*

</div>

<div class="proof">

*Proof.* Using $`\mathcal A_{t+s}=\mathcal A_t\mathcal A_s`$,
``` math
\mathcal T_{t+s}-\mathcal T_t\mathcal T_s
=
\mathcal E\mathcal A_t\mathcal A_s\mathcal I-\mathcal E\mathcal A_t\mathcal I\mathcal E\mathcal A_s\mathcal I,
```
and factoring the middle term gives <a href="#eq:defect" data-reference-type="ref+label" data-reference="eq:defect">[eq:defect]</a>. ◻

</div>

The defect has a direct meaning. Evolving an embedded effective state can generate microscopic information outside the selected representative subspace. Coarse-graining after the first interval discards that information, while uninterrupted evolution can later return some of it. A Markov approximation is therefore an additional approximation, not a consequence of projection notation.

<div id="cor:defect" class="corollary">

**Corollary 3** (Norm control of the defect). *For any submultiplicative superoperator norm,
``` math
\left\lVert \mathcal T_{t+s}-\mathcal T_t\mathcal T_s \right\rVert
 \leq
 \left\lVert \mathcal E \right\rVert\,\left\lVert \mathcal A_t \right\rVert\,
 \left\lVert (\mathbf 1_{\mathcal M}-\mathcal I\mathcal E)\mathcal A_s\mathcal I \right\rVert.
```*

</div>

## Where contraction can enter

Write $`D(\rho,\sigma)=\frac12\left\lVert \rho-\sigma \right\rVert_1`$ for trace distance.

<div id="prop:isometry" class="proposition">

**Proposition 4** (Unitary evolution is not strict mixing). *For all microscopic states $`\rho,\sigma`$,
``` math
D(\mathcal A_t\rho,\mathcal A_t\sigma)=D(\rho,\sigma).
```
If $`\mathcal E\mathcal I=\mathbf 1_{\mathcal K}`$ and both maps are channels, then $`D(\mathcal I\rho,\mathcal I\sigma)=D(\rho,\sigma)`$. Any strict reduction of distinguishability under <a href="#eq:reduced" data-reference-type="ref+label" data-reference="eq:reduced">[eq:reduced]</a> therefore comes from the coarse channel acting after microscopic excursion, not from unitary evolution alone.*

</div>

<div class="proof">

*Proof.* The trace norm is invariant under unitary conjugation. Contractivity of trace distance under channels gives
``` math
D(\rho,\sigma)=D(\mathcal E\mathcal I\rho,\mathcal E\mathcal I\sigma)
\leq D(\mathcal I\rho,\mathcal I\sigma)\leq D(\rho,\sigma),
```
so both inequalities are equalities. ◻

</div>

<div id="thm:contraction" class="theorem">

**Theorem 5** (Uniform effective contraction is sufficient). *Let $`\mathcal T`$ be a sampled effective channel, let $`\rho_\ast`$ be a fixed point, and let $`\mathcal B\subset\mathcal D(\mathcal K_L)`$ be invariant. If
``` math
d(\mathcal T\rho,\rho_\ast)\leq q\,d(\rho,\rho_\ast)
 \quad\text{for all }\rho\in\mathcal B,\qquad 0\leq q<1,
```
then
``` math
d(\mathcal T^n\rho,\rho_\ast)\leq q^n d(\rho,\rho_\ast).
```
If $`d`$ controls every observable in $`\mathcal O_L`$, their expectation values converge at the same rate.*

</div>

<div class="proof">

*Proof.* Iteration gives the first inequality. The observable statement follows from the declared domination of expectation-value differences by $`d`$. ◻

</div>

This is a useful basin theorem, but it is one-way. ETH does not require one globally contractive channel, and a chosen coarse channel can be contractive even when the microscopic eigenstate matrix elements fail an ETH test.

# Thermalization without a basin tautology

Fix an initial state $`\rho`$, a bounded observable $`O`$, and an energy window with microcanonical state $`\rho_{\mathrm{mc}}`$. Suppose the infinite-time Cesàro averages below exist and define the diagonal ensemble
``` math
\omega=\overline{\rho(t)}
 =\lim_{T\to\infty}\frac1T\int_0^T\rho(t)\,\mathrm{d}t.
```
Define
``` math
\epsilon_{\mathrm{diag}}(O)
 =\mathop{\mathrm{Tr}}[O(\omega-\rho_{\mathrm{mc}})]
```
and the temporal fluctuation
``` math
f_O(t)=\mathop{\mathrm{Tr}}[O(\rho(t)-\omega)].
```

<div id="thm:decomposition" class="theorem">

**Theorem 6** (Exact thermalization-error decomposition). *The mean-square deviation from the microcanonical value is
``` math
\begin{equation}
\label{eq:decomposition}
 \overline{\left|\mathop{\mathrm{Tr}}[O(\rho(t)-\rho_{\mathrm{mc}})]\right|^2}
 =
 |\epsilon_{\mathrm{diag}}(O)|^2+
 \overline{|f_O(t)|^2}.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The quantity inside the absolute value is $`\epsilon_{\mathrm{diag}}(O)+f_O(t)`$. By definition $`\overline{f_O}=0`$, so the two cross terms vanish after time averaging. ◻

</div>

<a href="#eq:decomposition" data-reference-type="ref+Label" data-reference="eq:decomposition">[eq:decomposition]</a> separates two obligations often conflated by basin language. Small diagonal bias requires the populated eigenstates to give the correct equilibrium expectation. Small temporal variance requires dephasing or an effective-dimension condition. A useful thermalization claim must control both, for declared states and observables. Existing equilibration theorems provide such bounds under specific spectral and population hypotheses ; the basin metaphor does not replace them.

<div id="def:thermal-basin" class="definition">

**Definition 7** (Operational thermal basin). For tolerances $`\varepsilon_{\rm d},\varepsilon_{\rm f}>0`$, define
``` math
\mathcal B_{\rm th}(O)=
\left\{\rho:
|\epsilon_{\rm diag}(O)|\leq\varepsilon_{\rm d},\
\overline{|f_O|^2}\leq\varepsilon_{\rm f}^2
\right\}.
```
For a finite observable family, intersect these sets over $`O\in\mathcal O_L`$.

</div>

This definition is deliberately diagnostic. Membership records verified thermal behavior at the selected resolution; it does not explain why the Hamiltonian has that behavior.

# Memory and quasi-local integrals of motion

Many-body localization is often described using quasi-local integrals of motion. The following elementary estimate makes the time scale explicit.

<div id="thm:liom" class="theorem">

**Theorem 8** (Quasi-conserved memory bound). *Let $`\tau=\tau^\dagger`$ be bounded and suppose
``` math
\left\lVert [H_L,\tau] \right\rVert\leq\eta.
```
Then, for every density operator $`\rho`$ and every $`t\in\mathbb{R}`$,
``` math
\begin{equation}
\label{eq:liom}
 \left|\mathop{\mathrm{Tr}}[\rho\,\tau(t)]-\mathop{\mathrm{Tr}}[\rho\,\tau]\right|
 \leq \eta |t|.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The Heisenberg equation gives
``` math
\frac{\mathrm{d}}{\mathrm{d}t}\tau(t)=i\,U_t^\dagger[H_L,\tau]U_t.
```
After integration, trace duality, and unitary norm invariance,
``` math
\left|\mathop{\mathrm{Tr}}\!\left[\rho(\tau(t)-\tau)\right]\right|
\leq\int_0^{|t|}\left\lVert [H_L,\tau] \right\rVert\,\mathrm{d}s
\leq\eta|t|.
```
 ◻

</div>

If $`\tau`$ is quasi-local near site $`i`$ and has a nonzero overlap with a measured local spin, <a href="#eq:liom" data-reference-type="ref+label" data-reference="eq:liom">[eq:liom]</a> yields an operational memory lower bound up to the approximation and overlap errors. A family with $`\eta_L\to0`$ can support growing memory times. The converse does not hold without further hypotheses: exact symmetries, integrability, prethermal conservation, or kinetic bottlenecks can also preserve memory.

<div id="def:memory-basin" class="definition">

**Definition 9** (Operational memory basin). For an initial-state class $`\mathcal I_L`$, observable $`O`$, threshold $`m_0>0`$, and time window $`[0,T_L]`$, define
``` math
\mathcal B_{\rm mem}(O)=
\left\{\rho\in\mathcal I_L:
\inf_{0\leq t\leq T_L}
\left|\mathop{\mathrm{Tr}}[O\rho(t)]-\mathop{\mathrm{Tr}}[O\rho_{\rm ref}]\right|\geq m_0
\right\}.
```

</div>

This records memory relative to a declared reference. It does not by itself establish MBL, exponential basin multiplicity, or a complete LIOM algebra.

# Why there is no universal knee

For finite $`L`$, <a href="#eq:xxz" data-reference-type="ref+label" data-reference="eq:xxz">[eq:xxz]</a> is a finite matrix depending analytically on its parameters. Away from degeneracies, its eigenvalues and spectral projectors vary locally analytically. Disorder-averaged finite-volume diagnostics are therefore generally smooth functions of $`W`$ under mild domination assumptions. A sharp thermodynamic transition, if present, appears only after a specified order of large-$`L`$, long-time, and disorder limits.

The previous paper imported a Kramers escape law. Kramers theory requires a stochastic process, a barrier, a noise scale, and a small-noise asymptotic. None is supplied by the closed unitary Hamiltonian <a href="#eq:xxz" data-reference-type="ref+label" data-reference="eq:xxz">[eq:xxz]</a>. Coarse-graining may motivate a stochastic effective model, but then its generator and approximation error must be derived or declared. A logistic curve is likewise only a fitting family. Under a monotone reparameterization of $`W`$, its midpoint and width change, so they cannot be universal geometric invariants.

<div id="prop:interpolation" class="proposition">

**Proposition 10** (Finite data do not select a unique crossover law). *Given finitely many distinct disorder values $`W_1,\ldots,W_N`$ and diagnostic means $`y_1,\ldots,y_N`$, infinitely many smooth functions $`g(W)`$ interpolate the data exactly while having different inflection points and asymptotic behavior.*

</div>

<div class="proof">

*Proof.* Let $`p`$ be the interpolating polynomial. For any smooth $`h`$,
``` math
g_h(W)=p(W)+h(W)\prod_{j=1}^{N}(W-W_j)
```
matches every data point. Varying $`h`$ changes the shape between and outside the sampled values. ◻

</div>

The correct numerical question is not whether a curve looks like a knee. It is whether a declared scaling family gives stable, cross-validated parameters as sizes and fit windows change.

# Finite-size and uncertainty protocol

A reproducible comparison for <a href="#eq:xxz" data-reference-type="ref+label" data-reference="eq:xxz">[eq:xxz]</a> should report:

1.  $`L`$, $`J`$, $`\Delta`$, boundary conditions, symmetry sector, energy window, disorder distribution, random seeds, and sample counts;

2.  $`\langle r\rangle`$, diagonal ETH residuals, imbalance, and entanglement with sample-level data or sufficient statistics;

3.  numerical residuals for eigenpairs and convergence checks;

4.  disorder confidence intervals obtained from independent samples;

5.  at least two plausible finite-size scaling models, including a smooth-crossover null model;

6.  sensitivity to omitted sizes, shifted energy windows, and changed fit ranges; and

7.  a held-out prediction, such as one larger size or a second observable not used to locate the crossover.

For a candidate dimensionless diagnostic $`X_L(W)`$, one may test
``` math
X_L(W)=F\!\left((W-W_c)L^{1/\nu}\right)
 +L^{-\omega}G\!\left((W-W_c)L^{1/\nu}\right),
```
but this is a model, not a theorem. The functions or their parameterizations, the correction exponent, covariance model, and fit window all belong to the parameter ledger. Drift in fitted $`W_c`$ with $`L`$ is evidence about finite-size effects, not permission to fix the desired answer. Large exact-diagonalization studies illustrate both the power and limitations of this procedure .

# Interface with Modal Triplet Theory

## What MTT supplies at its current tier

The MTT foundation defines a coherent sector through spectral projection and distinguishes stabilization, physical time, and coarse effective dynamics . Its controlled-truncation paper states the domain and resolvent data required for a valid coherent-sector reduction . These structures motivate asking whether a many-body experiment sees only a stable projected sector. They do not, by themselves, select <a href="#eq:xxz" data-reference-type="ref+label" data-reference="eq:xxz">[eq:xxz]</a> or prove ETH or MBL.

In particular, the following gaps must not be identified by notation:

<div class="center">

| Object | Meaning | Required comparison |
|:---|:---|:---|
| MTT Hessian gap | local stability of a selected fixed-point problem | an explicit source map and transported operator norm |
| Hamiltonian level spacing | differences among many-body energies | symmetry-resolved spectral statistics |
| Liouvillian or channel gap | mixing rate of an open or coarse dynamics | a declared generator or channel |
| mobility edge | energy-dependent localization boundary | a thermodynamic diagnostic and scaling theorem |

</div>

## The missing pullback theorem

Let $`Q_{\rm MTT}`$ denote a selected MTT coherent projector on an upper space and let $`\mathfrak C_L`$ be the capsule in <a href="#def:capsule" data-reference-type="ref+label" data-reference="def:capsule">1</a>. A genuine MTT derivation would require a map $`V_L`$ and channel-level construction satisfying, with controlled errors,
``` math
\begin{align}
 V_L Q_{\rm MTT} V_L^\dagger &\longmapsto
 \text{the selected effective sector},\\
 V_L A_{\rm MTT} V_L^\dagger &\longmapsto H_L(\omega;W),\\
 (\Pi_{\rm MTT},\text{margin}) &\longmapsto
 (\mathcal E,\mathcal I,\mathcal O_L,\mathcal I_L,\mathcal D_L).
\end{align}
```
It must also preserve or quantitatively transport connections, domains, holonomies, and the relevant operator bounds. Only then could an MTT stability statement imply one of the operational criteria proved here.

<div id="thm:transport" class="theorem">

**Theorem 11** (Conditional diagnostic transport). *Suppose a selected MTT model supplies maps into $`\mathfrak C_L`$ such that:*

1.  *its physical evolution is intertwined with $`\mathcal A_t`$ up to channel error $`\epsilon_t`$;*

2.  *its selected coarse map is intertwined with $`\mathcal E`$ and $`\mathcal I`$ up to diamond-norm error $`\epsilon_{\rm c}`$; and*

3.  *its selected observable $`O^{\rm MTT}`$ is transported to $`O\in\mathcal O_L`$ with operator-norm error $`\epsilon_O`$.*

*Then every finite-time expectation-value statement transports with an explicit error bounded by the sum of the channel and observable errors. In particular, for normalized states,
``` math
|\Delta\langle O\rangle|
 \leq \epsilon_t+\epsilon_{\rm c}+2\epsilon_O
```
under a convention in which channel errors are evaluated in diamond norm and $`\left\lVert O \right\rVert\leq1`$.*

</div>

<div class="proof">

*Proof.* Insert and subtract the exactly transported state and observable. Use trace duality for the observable terms and the defining diamond-norm bound for the channel terms. The two observable replacements contribute at most $`2\epsilon_O`$; the evolution and coarse-channel replacements contribute at most $`\epsilon_t+\epsilon_{\rm c}`$. ◻

</div>

This theorem says what a bridge can legitimately do. It transports a verified result after the source and error bounds are supplied. It does not create those source rows.

# Relation to monitored transitions

Measurement-induced entanglement transitions involve stochastic measurement records, conditional trajectories, nonlinear normalization, and an ensemble prescription. Their area- and volume-law regimes can also be summarized by operational basins, but that shared vocabulary is not a theorem that they are the same transition as ETH–MBL. The Hamiltonian channel <a href="#eq:reduced" data-reference-type="ref+label" data-reference="eq:reduced">[eq:reduced]</a> and a trajectory ensemble have different state spaces and generators. They should be compared only after a separate typed map identifies the observables and limiting procedures. The companion paper on measurement-induced transitions is the proper place for that construction.

# Falsifiers and next calculations

The operational bridge is useful because it can fail cleanly.

1.  If a proposed effective channel is claimed to be Markovian but <a href="#eq:defect" data-reference-type="ref+label" data-reference="eq:defect">[eq:defect]</a> is not small on the tested states, the reduction fails.

2.  If contraction is claimed to explain thermalization while microscopic trace distance is said to contract under unitary evolution, <a href="#prop:isometry" data-reference-type="ref+label" data-reference="prop:isometry">4</a> identifies the type error.

3.  If a thermal basin is claimed but either term in <a href="#eq:decomposition" data-reference-type="ref+label" data-reference="eq:decomposition">[eq:decomposition]</a> remains large, the thermalization claim fails for that state and observable.

4.  If a quasi-LIOM is claimed, its commutator norm must support the reported memory time through <a href="#eq:liom" data-reference-type="ref+label" data-reference="eq:liom">[eq:liom]</a>.

5.  If a universal knee is claimed, stability under alternative scaling models and reparameterizations must be demonstrated on held-out sizes.

6.  If the MTT explanation is claimed, the source and intertwining rows in <a href="#thm:transport" data-reference-type="ref+label" data-reference="thm:transport">11</a> must be emitted from selected geometry rather than fitted to the many-body output.

The immediate computational program is therefore modest: construct $`\mathfrak C_L`$ for a sequence of tractable sizes, publish sample-level diagnostics and uncertainty, quantify the semigroup defect for one declared coarse channel, and test whether the resulting operational basin labels add predictive information beyond the standard diagnostics. No numerical result is claimed in this paper.

# Conclusion

ETH and MBL can be discussed in one operational language, but they have not been proved to be one universal projection phenomenon. The useful common structure is a declared record of states, observables, time windows, coarse maps, and errors. Within that record, uniform contraction is a sufficient mixing criterion; diagonal bias and temporal fluctuation are exactly separable; and an approximately conserved quasi-local operator yields a quantitative memory time. Those are rigorous bridges because their assumptions and conclusions are visible.

MTT adds a potentially deeper question: can one selected upper geometry emit the Hamiltonian sector, coarse channel, observables, and stability data together? At present that is an open pullback theorem. Stating it explicitly strengthens rather than weakens the program: it distinguishes an explanatory source from an adaptable after-the-fact description and turns the next step into a concrete mathematical construction.
