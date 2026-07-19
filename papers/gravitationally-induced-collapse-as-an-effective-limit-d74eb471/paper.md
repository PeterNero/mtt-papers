---
abstract: |
  We show that gravitationally induced collapse in the sense of Penrose and the Diósi–Penrose (DP) model arises as a controlled effective limit of coherence breakdown in Modal Triplet Theory (MTT). Starting from projected coherent-sector dynamics, we derive a reduced nonunitary evolution whose leading contribution in a curvature-dominated regime reduces to a Newtonian double-commutator kernel of DP type, yielding the collapse timescale $`\tau \sim \hbar/E_G`$. We then prove that this regime is nongeneric: outside it, projection-induced reduced dynamics necessarily exhibits additional structure, including finite-strength threshold (“knee”) behavior, protocol dependence, and Zeno/anti-Zeno crossovers. We establish no-go results showing that gravity-only collapse generators depending solely on mass density cannot reproduce this structure without introducing state-dependent stabilization variables equivalent to a projection–basin mechanism. Finally, we formulate cross-sector closure: the parameters governing the reduced collapse dynamics are tied to the same spectral–geometric bottlenecks that control gravitational stability and effective field theory under controlled truncation. These results identify Penrose/DP collapse as a valid shadow law in a restricted universality class, but not a fundamental principle.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: b729be7593163f5782f4bdc41fd3772fd1093b17385f185268d63afef86d04e2
paper_id: gravitationally-induced-collapse-as-an-effective-limit-d74eb471
release_state: zenodo_released
released_version: v1.0
title: "**Gravitationally Induced Collapse as an Effective Limit of Coherence Breakdown in Modal Triplet Theory**"
zenodo_doi: 10.5281/zenodo.18261600
zenodo_record_id: 18261600
zenodo_url: "https://zenodo.org/records/18261600"
---

# Introduction

Penrose proposed that macroscopic quantum superpositions involving distinct spacetime geometries are unstable and reduce on a timescale $`\tau \sim \hbar/E_G`$, where $`E_G`$ is the Newtonian self-energy of the difference between mass distributions. The Diósi–Penrose (DP) model gives a related 4D master equation featuring a Newtonian double-commutator kernel. Such models provide useful effective diagnostics but raise three structural issues: (i) why the Newton kernel should be fundamental rather than emergent; (ii) why additional parameters (smearing, dissipation, colored noise) are required for mathematical and physical consistency; and (iii) why sharp threshold and protocol-dependent phenomena (including Zeno/anti-Zeno behavior and measurement-induced transitions) appear generically in controlled quantum experiments.

This paper treats Penrose/DP collapse as an effective phenomenon and derives it as a controlled limit of a broader reduced dynamics induced by projection in Modal Triplet Theory (MTT). We then prove that outside this limit additional structure is unavoidable and cannot be reproduced by gravity-only generators without introducing state-dependent stabilization variables that reconstruct the projection–basin mechanism.

# Minimal MTT Structure Used Here

## Geometry and Hilbert spaces

<div class="definition">

**Definition 1** (MTT product manifold). Let
``` math
M_{10} \;=\; Y_4 \times B_1 \times B_2 \times B_3,
```
where $`Y_4`$ is a smooth globally hyperbolic Lorentzian 4-manifold and each $`B_i`$ is a compact smooth Riemannian manifold of bounded geometry. Let $`\mathcal H_{10}:= L^2(M_{10};E)`$ be the Hilbert space of square-integrable sections of a fixed Hermitian bundle $`E\to M_{10}`$.

</div>

## Coherent projector and spectral gap

<div id="ass:cohproj" class="assumption">

**Assumption 2** (Commuting internal Laplace-type operators and coherent projector). For each $`i\in\{1,2,3\}`$ let $`\Delta_{B_i}\ge 0`$ be a self-adjoint Laplace-type operator acting along $`B_i`$. Assume the operators commute. Let $`\Pi_{B_i}`$ be the orthogonal projector onto $`\ker \Delta_{B_i}`$. Define
``` math
\Pi:= \Pi_{B_1}\Pi_{B_2}\Pi_{B_3}.
```
Assume $`\Pi`$ extends boundedly on the Sobolev scales needed below.

</div>

<div id="ass:gap" class="assumption">

**Assumption 3** (Uniform spectral gap). Let $`Q:= \mathrm{Id}- \Pi`$. There exists $`\lambda_\ast>0`$ such that for the internal operator
``` math
\Delta_{\mathrm{int}} := \Delta_{B_1}+\Delta_{B_2}+\Delta_{B_3},
```
we have
``` math
\Delta_{\mathrm{int}}\big|_{\mathrm{Ran}(Q)} \;\ge\; \lambda_\ast\,\mathrm{Id},
```
in the sense of quadratic forms.

</div>

<div class="definition">

**Definition 4** (Coherent and noncoherent subspaces). Define $`\mathcal H_{\mathrm{coh}}:= \mathrm{Ran}(\Pi)\subset \mathcal H_{10}`$ and $`\mathcal H_{\mathrm{nc}}:= \mathrm{Ran}(Q)\subset \mathcal H_{10}`$, so $`\mathcal H_{10}= \mathcal H_{\mathrm{coh}}\oplus \mathcal H_{\mathrm{nc}}`$.

</div>

## Dynamics and observable pushforward

<div id="ass:flow" class="assumption">

**Assumption 5** (Well-posed 10D evolution). Let $`\Phi_t:\mathcal H_{10}\to \mathcal H_{10}`$ be a deterministic evolution map generated by a well-posed analytic flow on a bounded-geometry slab, strongly continuous in $`t`$, and such that the induced evolution on density operators is well-defined on the trace-class domain considered.

</div>

<div id="def:P" class="definition">

**Definition 6** (Observable map). Let $`I`$ denote normalized fiber integration over $`B_1\times B_2\times B_3`$ (defined on a dense subspace and extending boundedly on the domains of interest). Define the observable map
``` math
P := I\circ \Pi.
```
Let $`\mathcal H_{4}`$ denote the $`L^2(Y_4)`$-closure of $`\mathrm{Ran}(P)`$.

</div>

<div class="remark">

*Remark 7*. The map $`P`$ is generally many-to-one. Consequently, induced effective dynamics on observables need not be invertible or unitary even when $`\Phi_t`$ is deterministic and unitary on an extended space; this is a structural feature of reduction by projection.

</div>

# Reduced Dynamics and an Induced Nonunitary Generator

## Reduced density operator

Let $`\Psi(t)\in\mathcal H_{10}`$ be a (pure) 10D state along the evolution $`\Phi_t`$. Define the reduced (observable) density operator
``` math
\begin{equation}
\label{eq:rho}
\rho(t) \;:=\; P\,\left|\Psi(t)\right\rangle\!\left\langle\Psi(t)\right|\,P^\dagger,
\end{equation}
```
interpreted as a positive trace-class operator on $`\mathcal H_{4}`$ for initial data in the controlled domain.

## Coherent/noncoherent splitting of the generator

We work with the evolution of density operators on $`\mathcal H_{10}`$. Let $`\mathcal{L}_{10}`$ denote the generator on trace-class operators (e.g. Liouvillian form in the unitary case, or more general). Assume a splitting consistent with $`\mathcal H_{10}=\mathcal H_{\mathrm{coh}}\oplus \mathcal H_{\mathrm{nc}}`$.

<div id="ass:gensplit" class="assumption">

**Assumption 8** (Generator splitting). There exist (densely defined) linear maps on trace-class operators such that
``` math
\mathcal{L}_{10} = \mathcal{L}_{\mathrm{coh}} + \mathcal{L}_{\mathrm{nc}} + \mathcal{V},
```
where $`\mathcal{L}_{\mathrm{nc}}`$ generates relaxation on $`\mathrm{Ran}(Q)`$ controlled by $`\lambda_\ast`$, and $`\mathcal{V}`$ couples coherent and noncoherent sectors. The coupling is such that a second-order weak-coupling expansion is valid on the slab (Assumption <a href="#ass:weakcoupling" data-reference-type="ref" data-reference="ass:weakcoupling">9</a>).

</div>

## Projection equation and Markovian approximation

Define the superoperator $`\mathcal{P}`$ by $`\mathcal{P}(X)=PXP^\dagger`$ and $`\mathcal{Q}:=\mathrm{Id}-\mathcal{P}`$.

The Nakajima–Zwanzig identity yields an exact reduced equation for $`\rho(t)=\mathcal{P}\varrho(t)`$, where $`\varrho(t)`$ is the 10D density operator:
``` math
\begin{equation}
\label{eq:NZ}
\frac{\mathrm{d} }{\mathrm{d} t}\rho(t) \;=\; \mathcal{P}\mathcal{L}_{10}\mathcal{P}\rho(t)\;+\;\int_0^t \mathcal{K}(t-s)\rho(s)\,\mathrm{d}s \;+\; \mathcal{I}(t),
\end{equation}
```
with memory kernel $`\mathcal{K}(t)=\mathcal{P}\mathcal{L}_{10}\,e^{t\mathcal{Q}\mathcal{L}_{10}\mathcal{Q}}\mathcal{Q}\mathcal{L}_{10}\mathcal{P}`$, and inhomogeneity $`\mathcal{I}(t)`$ determined by $`\mathcal{Q}\varrho(0)`$.

<div id="ass:weakcoupling" class="assumption">

**Assumption 9** (Controlled truncation / weak coupling / rapid decay). On the time slab of interest:

1.  The semigroup on the noncoherent sector decays: there exist $`C>0`$ such that
    ``` math
    \left\lVert e^{t\mathcal{Q}\mathcal{L}_{10}\mathcal{Q}} \right\rVert \le C e^{-\lambda_\ast t}\quad (t\ge 0),
    ```
    on the operator norms used for the memory bound.

2.  The inhomogeneous term $`\mathcal{I}(t)`$ is negligible on the slab (e.g. by preparation in the controlled manifold) or can be absorbed into a renormalization of initial conditions.

3.  The coupling is weak enough that truncation at second order in $`\mathcal{V}`$ is consistent and yields a completely positive reduced generator (standard Davies-type condition).

</div>

<div id="thm:lindblad" class="theorem">

**Theorem 10** (Induced Lindblad-type reduced generator (controlled approximation on a slab)). *Assume <a href="#ass:cohproj" data-reference-type="ref" data-reference="ass:cohproj">2</a>–<a href="#ass:weakcoupling" data-reference-type="ref" data-reference="ass:weakcoupling">9</a>. Then on the slab, the reduced evolution admits the following *controlled Markovian approximation*:*

*``` math
\begin{equation}
\label{eq:lindblad}
\frac{\mathrm{d} }{\mathrm{d} t}\rho(t) \;=\; -\frac{i}{\hbar}\left[H_{\mathrm{eff}},\rho(t)\right] \;+\; \mathcal{D}_{\mathrm{ind}}[\rho(t)] \;+\; \mathcal{R}_{\lambda_\ast}[\rho(t)],
\end{equation}
```
where:*

1.  *$`H_{\mathrm{eff}}`$ is an effective self-adjoint Hamiltonian on $`\mathcal H_{4}`$;*

2.  *$`\mathcal{D}_{\mathrm{ind}}`$ is a completely positive dissipator of Gorini–Kossakowski–Sudarshan–Lindblad (GKSL) type;*

3.  *the remainder satisfies $`\left\lVert \mathcal{R}_{\lambda_\ast} \right\rVert \le C'\lambda_\ast^{-1}`$ on the slab for some constant $`C'`$ determined by the bounded-geometry and coupling norms.*

*In particular, the statement is not an exact identity but an approximation with an explicit remainder bounded by $`C'\lambda_\ast^{-1}`$ on the slab.*

</div>

<div class="proof">

*Proof.* Under Assumption <a href="#ass:weakcoupling" data-reference-type="ref" data-reference="ass:weakcoupling">9</a>(W1)–(W3), the memory kernel in <a href="#eq:NZ" data-reference-type="eqref" data-reference="eq:NZ">[eq:NZ]</a> is integrable and dominated by an exponentially decaying bound. Define the time-local generator by replacing $`\rho(s)`$ with $`\rho(t)`$ in the memory integral and extending the upper limit to infinity; the error is bounded by the exponential tail and the Lipschitz continuity of the reduced flow on the slab. This produces a bounded correction of order $`\lambda_\ast^{-1}`$. Complete positivity of $`\mathcal{D}_{\mathrm{ind}}`$ follows from the standard weak-coupling limit construction (Davies) when the coupling and decay hypotheses hold; equivalently, one may employ the second-order cumulant expansion with a positive Kossakowski matrix. The Hamiltonian part arises from the anti-self-adjoint component of the reduced generator. ◻

</div>

# Penrose–Diósi Limit in a Curvature-Dominated Regime

## Curvature-dominated (Penrose) regime

Consider two semiclassical 4D branches $`A,B`$ with mass densities $`\rho_A(\mathbf x)`$, $`\rho_B(\mathbf x)`$ on a spatial hypersurface, and let $`\delta\rho := \rho_A-\rho_B`$.

<div id="def:Sigma" class="definition">

**Definition 11** (Coherence-stress decomposition). We decompose coherence stress into
``` math
\Sigma \;=\; \Sigma_{\mathrm{curv}}+\Sigma_{\mathrm{env}}+\Sigma_{\mathrm{meas}},
```
where $`\Sigma_{\mathrm{curv}}`$ is curvature-induced stress (dominant when spacetime response differs significantly between branches), $`\Sigma_{\mathrm{env}}`$ arises from environment-induced monitoring/noise, and $`\Sigma_{\mathrm{meas}}`$ encodes explicit measurement protocol back-action.

</div>

<div class="remark">

*Remark 12*. In this paper, $`\Sigma_{\mathrm{curv}}`$ is extracted from the *linearized (Newtonian/weak-field) gravitational response* of the emergent 4D geometry to branch-dependent mass densities, i.e. from the Poisson/linearized-Einstein Green’s function; we do not invoke semiclassical backreaction through $`\langle T_{\mu\nu}\rangle`$ as an input in defining $`\Sigma_{\mathrm{curv}}`$.

</div>

<div id="def:PenroseRegime" class="definition">

**Definition 13** (Penrose regime). We say the system lies in the Penrose regime on a slab if:

1.  $`\Sigma_{\mathrm{curv}} \gg \Sigma_{\mathrm{env}},\Sigma_{\mathrm{meas}}`$ throughout the episode;

2.  the Newtonian approximation to the gravitational response on relevant scales is valid;

3.  controlled truncation (Assumption <a href="#ass:weakcoupling" data-reference-type="ref" data-reference="ass:weakcoupling">9</a>) holds on the slab.

</div>

## Coherent resolution scale

In the coherent truncation, the reduced description cannot resolve arbitrarily sharp densities. We encode this by an effective spatial resolution (smearing) scale.

<div id="prop:ellcoh" class="proposition">

**Proposition 14** (Coherent resolution scale). *Under Assumption <a href="#ass:gap" data-reference-type="ref" data-reference="ass:gap">3</a>, there exists a characteristic length $`\ell_{\mathrm{coh}}`$ such that observables in $`\mathcal H_{4}`$ are effectively band-limited at spatial frequencies above $`\sim \lambda_\ast^{1/2}`$, and one may take
``` math
\ell_{\mathrm{coh}} \asymp \lambda_\ast^{-1/2},
```
up to constants depending on representation and bounded geometry.*

</div>

<div class="proof">

*Proof.* The uniform gap $`\lambda_\ast`$ separates coherent (harmonic) and noncoherent modes of $`\Delta_{\mathrm{int}}`$. Controlled truncation bounds the contribution of noncoherent components by resolvent estimates proportional to $`\lambda_\ast^{-1}`$. Translating the spectral bound into an effective spatial resolution on 4D observables yields a minimal length scale inversely proportional to the square root of the gap (standard in elliptic/spectral truncations). ◻

</div>

## Emergence of the DP kernel

Let $`\hat\mu(\mathbf x)`$ be the $`\ell_{\mathrm{coh}}`$-smeared mass density operator on $`\mathcal H_{4}`$.

<div id="prop:DP" class="proposition">

**Proposition 15** (Newtonian DP kernel). *Assume Definition <a href="#def:PenroseRegime" data-reference-type="ref" data-reference="def:PenroseRegime">13</a> and Theorem <a href="#thm:lindblad" data-reference-type="ref" data-reference="thm:lindblad">10</a>. Then the leading gravitational contribution to $`\mathcal{D}_{\mathrm{ind}}`$ is
``` math
\begin{equation}
\label{eq:DP}
\mathcal{D}_{\mathrm{grav}}[\rho]
=
-\frac{1}{\hbar}\int_{\mathbb R^3}\!\!\int_{\mathbb R^3}
\frac{G}{|\mathbf x-\mathbf y|}\;
\left[\hat\mu(\mathbf x),\left[\hat\mu(\mathbf y),\rho\right]\right]\;
\mathrm{d}^3x\,\mathrm{d}^3y
\;+\; \mathcal{R}_{\lambda_\ast}[\rho],
\end{equation}
```
with $`\left\lVert \mathcal{R}_{\lambda_\ast} \right\rVert \le C'\lambda_\ast^{-1}`$ on the slab.*

</div>

<div class="proof">

*Proof.* In the Penrose regime, the dominant contribution to the coupling $`\mathcal{V}`$ entering the second-order reduced dissipator arises from curvature-sensitive channels sourced by mass density differences. The second-order term in $`\mathcal{V}`$ produces a quadratic form in the coupling observable. In the Newtonian limit, the relevant Green’s function is the Poisson kernel $`G/|\mathbf x-\mathbf y|`$. The GKSL structure yields the double commutator. Smearing at scale $`\ell_{\mathrm{coh}}`$ is inherited from the coherent truncation (Proposition <a href="#prop:ellcoh" data-reference-type="ref" data-reference="prop:ellcoh">14</a>). The remainder is bounded by the same $`\lambda_\ast^{-1}`$ estimate as in Theorem <a href="#thm:lindblad" data-reference-type="ref" data-reference="thm:lindblad">10</a>. A detailed expansion is provided in Appendix <a href="#app:B" data-reference-type="ref" data-reference="app:B">11</a>. ◻

</div>

## Penrose self-energy and timescale

Define the gravitational self-energy of the difference distribution:
``` math
\begin{equation}
\label{eq:EG}
E_G(\delta\rho)
:= \frac{G}{2}\int_{\mathbb R^3}\!\!\int_{\mathbb R^3}
\frac{\delta\rho(\mathbf x)\,\delta\rho(\mathbf y)}{|\mathbf x-\mathbf y|}\;\mathrm{d}^3x\,\mathrm{d}^3y,
\end{equation}
```
with $`\delta\rho`$ implicitly smeared at $`\ell_{\mathrm{coh}}`$.

<div id="cor:PenroseShadow" class="corollary">

**Corollary 16** (Penrose shadow law). *Under the assumptions of Proposition <a href="#prop:DP" data-reference-type="ref" data-reference="prop:DP">15</a>, off-diagonal reduced coherences decay with characteristic rate proportional to $`E_G/\hbar`$, and the corresponding timescale satisfies
``` math
\tau \asymp \frac{\hbar}{E_G},
```
up to order-one universality factors and the controlled truncation remainder $`\mathcal{O}(\lambda_\ast^{-1})`$.*

</div>

<div class="proof">

*Proof.* In the basis diagonalizing $`\hat\mu(\mathbf x)`$ and for branch superpositions with difference distribution $`\delta\rho`$, the double commutator produces exponential damping of off-diagonal terms with exponent given by the quadratic form induced by the Newton kernel, which is exactly $`E_G/\hbar`$ at leading order. The remainder term yields bounded corrections suppressed by $`\lambda_\ast^{-1}`$ on the slab. ◻

</div>

# Threshold (Knee) Behavior from Basin Geometry

## Admissible basins

<div id="ass:basins" class="assumption">

**Assumption 17** (Admissible basin decomposition). The coherent reduced state space relevant to the experiment decomposes into admissible basins $`\{\mathcal{B}_\alpha\}`$ such that:

1.  For each basin $`\mathcal{B}_\alpha`$, the induced map (or continuous-time generator) is contractive on $`\mathcal{B}_\alpha`$ with a strictly positive margin.

2.  Basin boundaries correspond to loss of contractivity along at least one direction.

3.  Under small perturbations of protocol parameters, the local boundary structure varies continuously.

</div>

## OU reduction near boundary and knee theorem

Let $`u`$ parametrize the locally least stable direction near a boundary point, and let $`s`$ denote a scalar protocol strength.

<div id="ass:OU" class="assumption">

**Assumption 18** (Local OU reduction). Near a basin boundary and on the time window of interest, the reduced dynamics of $`u`$ is approximated by
``` math
\dot u(t) = -\gamma(s)\,u(t) + \eta(t),
```
where $`\gamma(s)`$ is continuous in $`s`$, and $`\eta(t)`$ is mean-zero Gaussian white noise with covariance $`2D\,\delta(t-t')`$, with $`D>0`$.

</div>

<div id="lem:crit" class="lemma">

**Lemma 19** (Existence of finite critical point). *Under Assumptions <a href="#ass:basins" data-reference-type="ref" data-reference="ass:basins">17</a> and <a href="#ass:OU" data-reference-type="ref" data-reference="ass:OU">18</a>, there exists $`s_\ast`$ such that $`\gamma(s_\ast)=0`$, with $`\gamma(s)>0`$ for stable basin confinement and $`\gamma(s)<0`$ for deterministic expulsion.*

</div>

<div class="proof">

*Proof.* By (B1) there exists a stable region where $`\gamma(s)>0`$. By (B2), at boundary contact contractivity fails along the least stable direction, implying $`\gamma(s)\le 0`$. Continuity in $`s`$ (B3) implies a zero crossing $`s_\ast`$. ◻

</div>

<div id="thm:knee" class="theorem">

**Theorem 20** (Threshold (knee) behavior). *Under Assumptions <a href="#ass:basins" data-reference-type="ref" data-reference="ass:basins">17</a> and <a href="#ass:OU" data-reference-type="ref" data-reference="ass:OU">18</a>, for times $`t`$ long compared to microscopic correlation times but within the slab, the basin-exit probability admits an exponential survival form
``` math
P_{\mathrm{coll}}(s,t) = 1-e^{-\Gamma(s)t},
```
with an exit rate $`\Gamma(s)`$ that exhibits a finite-strength crossover at $`s=s_\ast`$. Moreover, $`\Gamma(s)`$ admits an interpolation of sigmoid type:
``` math
\Gamma(s)\approx \Gamma_0\frac{1}{1+\exp\left(\frac{s_\ast-s}{\delta s}\right)},
```
where $`\delta s`$ is proportional to the diffusion scale $`D`$ divided by $`\left|\gamma'(s_\ast)\right|`$.*

</div>

<div class="proof">

*Proof.* For $`s<s_\ast`$, $`\gamma(s)>0`$ and the OU process admits a stationary distribution; first-exit from $`u<0`$ into $`u>0`$ is noise-activated. Standard Kramers theory bounds the exit rate by $`\Gamma(s)\sim \exp(-\Delta V(s)/D)`$, with $`\Delta V(s)\propto \gamma(s)`$. For $`s>s_\ast`$, $`\gamma(s)<0`$ and the deterministic drift term drives $`u(t)`$ away from the boundary, producing rapid exit on timescale $`\sim |\gamma(s)|^{-1}`$. Matching these regimes yields a crossover whose width is set by the diffusion scale and the slope at criticality. Appendix <a href="#app:A" data-reference-type="ref" data-reference="app:A">10</a> provides a detailed derivation of the OU/Kramers bounds and the interpolation scale. ◻

</div>

<div id="prop:noknee" class="proposition">

**Proposition 21** (No knee from mass-density-only linear generators). *Let a collapse model on $`\mathcal H_{4}`$ be generated by a linear, time-homogeneous dissipator that depends only on mass density (including fixed-parameter DP-type kernels). If protocol parameters $`s`$ enter only through state preparation (not through the generator), then the collapse/exponential decay rate varies smoothly in $`s`$ and cannot display a finite-strength nonanalytic threshold of the form in Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">20</a>.*

</div>

<div class="proof">

*Proof.* If the generator $`\mathcal{L}`$ is independent of $`s`$, then $`\rho(t)=e^{t\mathcal{L}}\rho(0;s)`$. Any dependence on $`s`$ arises solely through $`\rho(0;s)`$. For linear semigroups on trace-class operators, decay rates are determined by the spectrum of $`\mathcal{L}`$, which is independent of $`s`$; thus no sign change of an internal restoring rate $`\gamma(s)`$ can occur. Finite-strength knees require $`s`$-dependence of the generator or additional state-dependent structure. ◻

</div>

# Protocol Dependence and Zeno/Anti-Zeno Crossover

## Protocol map

Let $`s`$ denote probe strength and $`\Delta t`$ probe interval. Define a protocol-cycle reduced map
``` math
\mathcal{M}_{s,\Delta t}(\rho) := P\,\Phi^{(s)}_{\Delta t}\!\big(P^\dagger\rho P\big)\,P^\dagger.
```
After $`n`$ cycles (time $`t=n\Delta t`$), $`\rho(t)=(\mathcal{M}_{s,\Delta t})^n(\rho_0)`$.

<div id="thm:zeno" class="theorem">

**Theorem 22** (Zeno/anti-Zeno crossover). *Under Assumptions <a href="#ass:cohproj" data-reference-type="ref" data-reference="ass:cohproj">2</a>–<a href="#ass:weakcoupling" data-reference-type="ref" data-reference="ass:weakcoupling">9</a> and basin structure (Assumption <a href="#ass:basins" data-reference-type="ref" data-reference="ass:basins">17</a>), there exist finite protocol scales $`(s_Z,\Delta t_Z)`$ such that:*

1.  *(Zeno regime) For sufficiently large $`s`$ and sufficiently small $`\Delta t`$, basin exit is suppressed and $`\Gamma_{\mathrm{coll}}(s,\Delta t)\to 0`$.*

2.  *(Anti-Zeno regime) For intermediate $`(s,\Delta t)`$ near $`(s_Z,\Delta t_Z)`$, basin exit is enhanced: $`\Gamma_{\mathrm{coll}}(s,\Delta t)>\Gamma_{\mathrm{coll}}(0)`$.*

</div>

<div class="proof">

*Proof.* For large $`s`$ and small $`\Delta t`$, repeated application of $`\mathcal{M}_{s,\Delta t}`$ confines the state to the most stable subspace associated with the basin, suppressing excursions along unstable directions; this is the standard Zeno mechanism in a reduced map setting. For intermediate $`(s,\Delta t)`$, the probe injects fluctuations aligned with the least stable direction and effectively lowers the Kramers barrier, increasing the exit rate; this is the anti-Zeno enhancement. The existence of a finite crossover scale follows from continuity of the induced generator in $`s`$ and $`\Delta t`$ together with the sign-change structure near basin boundaries (Lemma <a href="#lem:crit" data-reference-type="ref" data-reference="lem:crit">19</a>). ◻

</div>

<div id="prop:noprotocol" class="proposition">

**Proposition 23** (No protocol dependence for gravity-only generators). *Let $`\dot\rho=\mathcal{L}\rho`$ with $`\mathcal{L}`$ a fixed linear generator depending only on mass density (e.g. DP kernel with fixed parameters) and independent of $`(s,\Delta t)`$. Then $`\Gamma_{\mathrm{coll}}`$ cannot depend on protocol parameters $`(s,\Delta t)`$ except through initial-state preparation; Zeno/anti-Zeno crossovers require generator dependence on the protocol or additional state variables.*

</div>

<div class="proof">

*Proof.* If $`\mathcal{L}`$ is independent of $`(s,\Delta t)`$, then the semigroup $`e^{t\mathcal{L}}`$ has fixed spectral decay structure. Protocol variation affects only $`\rho_0`$. Any systematic dependence of decay rates on $`(s,\Delta t)`$ (including suppression/enhancement regimes) requires $`(s,\Delta t)`$-dependence of the generator or nonlinear state dependence. ◻

</div>

# Cross-Sector Closure

<div id="def:Theta" class="definition">

**Definition 24** (Bottleneck vector). Let $`\Theta`$ denote the finite set of spectral–geometric parameters controlling coherent-sector reduction on the slab, including: $`\lambda_\ast`$ (uniform gap), projector bounds, curvature–gap coefficients, and damping/disturbance margins.

</div>

<div id="thm:closure" class="theorem">

**Theorem 25** (Cross-sector closure). *Assume controlled truncation and coherent-sector universality on the slab. Then the parameters governing:*

1.  *the DP/Penrose shadow kernel (Section 4), including the effective smearing scale $`\ell_{\mathrm{coh}}`$;*

2.  *threshold scales $`s_\ast,\delta s`$ (Section 6);*

3.  *protocol crossover scales $`(s_Z,\Delta t_Z)`$ (Section 7);*

*are functions of the common bottleneck vector $`\Theta`$, up to controlled truncation errors of order $`\lambda_\ast^{-1}`$.*

</div>

<div class="proof">

*Proof.* The DP/Penrose kernel depends on the coherent resolution scale, fixed by $`\lambda_\ast`$ via Proposition <a href="#prop:ellcoh" data-reference-type="ref" data-reference="prop:ellcoh">14</a>, and on the same coupling norms that enter the truncation control. Threshold behavior depends on the sign change of the effective restoring rate $`\gamma(s)`$, whose slope and noise floor are determined by damping and disturbance parameters arising from the truncated sector, hence by $`\Theta`$. Protocol crossover scales depend on the interplay between probing and contraction margins, again fixed by the same stability parameters. Controlled truncation ensures that dependence on microscopic details beyond $`\Theta`$ is suppressed by $`\lambda_\ast^{-1}`$. ◻

</div>

<div id="prop:noclosure" class="proposition">

**Proposition 26** (Absence of closure in gravity-only models). *Penrose/DP collapse models treated as fundamental laws introduce collapse parameters (e.g. smearing length, effective noise temperature) that are not constrained by gravitational coupling, EFT thresholds, or stability margins. Thus they do not enforce cross-sector closure unless augmented by additional structure equivalent to $`\Theta`$.*

</div>

<div class="proof">

*Proof.* In gravity-only collapse models, the collapse kernel parameters are set independently (or fitted) and are not derived from a unified spectral–geometric control structure. There is no mechanism tying these parameters to stability margins or EFT truncation errors. Therefore cross-sector consistency is not enforced and must be imposed externally, which is precisely the absence of closure. ◻

</div>

# Experimental Diagnostics and Falsifiability

The theoretical results yield concrete, falsifiable diagnostics:

1.  **Penrose regime scaling:** In curvature-dominated conditions, decay rates scale with $`E_G/\hbar`$ (Corollary <a href="#cor:PenroseShadow" data-reference-type="ref" data-reference="cor:PenroseShadow">16</a>).

2.  **Knee behavior:** Varying probe strength produces finite-strength threshold structure in exit probabilities (Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">20</a>).

3.  **Protocol dependence:** At fixed geometry (fixed $`E_G`$), varying $`(s,\Delta t)`$ modifies collapse behavior, including Zeno/anti-Zeno crossover (Theorem <a href="#thm:zeno" data-reference-type="ref" data-reference="thm:zeno">22</a>).

4.  **Closure constraints:** Parameters inferred from reduced dynamics must be consistent with independent stability constraints encoded by $`\Theta`$ (Theorem <a href="#thm:closure" data-reference-type="ref" data-reference="thm:closure">25</a>).

A gravity-only collapse model cannot reproduce (D2)–(D4) without adding protocol/state dependence equivalent to a projection–basin mechanism.

# Conclusions

We derived the DP double-commutator kernel and Penrose timescale $`\tau\asymp \hbar/E_G`$ as a controlled effective limit of projection-induced reduced dynamics in MTT, valid in a curvature-dominated universality regime. We proved that outside this regime, admissible basin structure and noninvertible projection imply finite-strength threshold behavior and protocol dependence, including Zeno/anti-Zeno crossovers, which cannot arise from gravity-only mass-density-dependent linear generators. Finally, we established cross-sector closure: the parameters governing the reduced collapse dynamics are functions of the same spectral–geometric bottlenecks that control truncation and stability. Therefore Penrose/DP collapse is a valid shadow law in a restricted universality class, not a fundamental principle. All statements are slab-local and admissibility-conditioned: the controlled truncation, the Markovian approximation, and the basin/threshold analysis are asserted only on bounded-geometry time slabs where the coherent projector is bounded and the stability margins defining admissible basins remain positive.

# OU/Kramers Reduction Near Basin Boundaries

We justify the OU/Kramers mechanism underlying Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">20</a>.

## Linearization and diffusion

Under Assumption <a href="#ass:OU" data-reference-type="ref" data-reference="ass:OU">18</a>, the boundary-normal coordinate satisfies
``` math
\dot u = -\gamma(s)u + \eta(t),
\qquad
\mathbb{E}[\eta(t)]=0,
\qquad
\mathbb{E}[\eta(t)\eta(t')]=2D\delta(t-t').
```
For $`\gamma(s)>0`$, the OU process is stationary with variance $`\mathbb{E}[u^2]=D/\gamma(s)`$.

## Exit rate for $`s<s_\ast`$

Fix an absorbing boundary at $`u=0`$ (exit). Standard first-passage analysis for OU processes yields an exponentially small exit rate as $`D\to 0`$ or as the basin stability increases. In the presence of a smooth effective potential $`V_s(u)=\frac12\gamma(s)u^2`$ on $`u<0`$, Kramers theory bounds the mean exit time by
``` math
\mathbb{E}[\tau_{\mathrm{exit}}] \sim \exp\!\left(\frac{\Delta V(s)}{D}\right),
```
with $`\Delta V(s)\propto \gamma(s)`$ for fixed basin thickness scale.

## Exit for $`s>s_\ast`$

For $`\gamma(s)<0`$, the drift is unstable and $`u(t)`$ is expelled from the basin with characteristic time $`|\gamma(s)|^{-1}`$, producing rapid exit.

## Crossover

Because $`\gamma(s)`$ crosses zero at $`s_\ast`$ and varies continuously, the exit rate transitions sharply between noise-activated and drift-dominated regimes. The crossover width is controlled by the diffusion scale $`D`$ and the slope $`\gamma'(s_\ast)`$, yielding a sigmoid interpolation consistent with Theorem <a href="#thm:knee" data-reference-type="ref" data-reference="thm:knee">20</a>.

# Weak-Coupling Derivation of the DP Kernel

We detail the second-order reduction leading to <a href="#eq:DP" data-reference-type="eqref" data-reference="eq:DP">[eq:DP]</a>.

## Second-order reduced generator

Under Assumption <a href="#ass:weakcoupling" data-reference-type="ref" data-reference="ass:weakcoupling">9</a>, the Markovian reduced dissipator can be written (formally) as
``` math
\mathcal{D}_{\mathrm{ind}}[\rho]
=
\int_0^\infty \mathcal{P}\mathcal{V}\,e^{t\mathcal{Q}\mathcal{L}_{10}\mathcal{Q}}\,\mathcal{V}\mathcal{P}\,\rho\;\mathrm{d}t
\;+\;\text{h.c.},
```
where exponential decay of $`e^{t\mathcal{Q}\mathcal{L}_{10}\mathcal{Q}}`$ is controlled by $`\lambda_\ast`$.

## Curvature-dominated coupling observable

In the Penrose regime, the dominant coupling observable is the (smeared) mass density $`\hat\mu(\mathbf x)`$, because curvature-sensitive noncoherent modes couple primarily through mass-energy content in the Newtonian limit. Thus, to leading order, $`\mathcal{V}`$ contributes quadratically in $`\hat\mu`$.

## Newtonian Green’s function

In the nonrelativistic limit, the gravitational response is governed by the Poisson equation, whose Green’s function is $`1/|\mathbf x-\mathbf y|`$. Therefore the quadratic form induced by the coupling yields the kernel $`G/|\mathbf x-\mathbf y|`$ in the reduced dissipator, giving
``` math
\mathcal{D}_{\mathrm{grav}}[\rho]
=
-\frac{1}{\hbar}\int\!\!\int \frac{G}{|\mathbf x-\mathbf y|}\;\left[\hat\mu(\mathbf x),\left[\hat\mu(\mathbf y),\rho\right]\right]\,\mathrm{d}^3x\,\mathrm{d}^3y,
```
matching <a href="#eq:DP" data-reference-type="eqref" data-reference="eq:DP">[eq:DP]</a>.

## Smearing from coherent resolution

The coherent truncation imposes a resolution scale $`\ell_{\mathrm{coh}}\asymp \lambda_\ast^{-1/2}`$, so $`\hat\mu`$ and $`\delta\rho`$ are understood as smeared at $`\ell_{\mathrm{coh}}`$. This regularizes short-distance divergences and fixes the effective smearing scale in the DP limit.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255621>

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.16949762>

P. Nero, *Fixed Points I–VI: Complete Coherence Spine*, Zenodo preprints, August 2025. <https://doi.org/10.5281/zenodo.16948748>

P. Nero, *The Projection–Admissibility Principle: Structural Constraints on Effective Physical Description*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255838>

P. Nero, *Closure and Inevitability in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255510>

P. Nero, *Coherence Capacity as the Fundamental Resource of Effective Physics*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18255905>

P. Nero, *Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256048>

P. Nero, *Modal Triplet Theory: From MTT to Quantum Mechanics*, Zenodo preprint, September 2025. <https://doi.org/10.5281/zenodo.17074246>

P. Nero, *From MTT to Quantum Field Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17068816>

P. Nero, *Modal Triplet Theory: From MTT to General Relativity*, Zenodo preprint, October 2025. <https://doi.org/10.5281/zenodo.16950597>

P. Nero, *Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17077671>

P. Nero, *Measurement as Disturbance and Stabilization in Modal Triplet Theory*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17177404>

P. Nero, *Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18256408>

P. Nero, *Modal Fixed Points, Bell’s Beables, and the Limits of Factorization*, Zenodo preprint, 2025. <https://doi.org/10.5281/zenodo.17076300>

P. Nero, *Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory*, Zenodo preprint, August 2025. <https://doi.org/10.5281/zenodo.18208884>

P. Nero, *From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
