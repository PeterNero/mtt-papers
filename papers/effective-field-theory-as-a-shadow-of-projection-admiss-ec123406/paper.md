---
abstract: |
  Wilsonian effective field theory combines several operations that are often described by the single word “renormalization”: exact integration of unresolved modes, truncation to a finite operator basis, matching of couplings, and evolution of coordinates with scale. Those operations have different domains and different notions of reversibility. This paper replaces an earlier global identification with a typed structural comparison. A noninjective coarse-graining map has no exact decoder for the actual ultraviolet input, but it may have many right sections selecting representative ultraviolet completions. At the same time, a beta-function ordinary differential equation can be locally invertible wherever its vector field has a unique two-sided flow. These facts are compatible because coupling-space evolution does not restore eliminated microscopic data.

  We prove that noninjectivity alone does not imply universality, while a declared contraction on an invariant basin does. We separate regulator, matching, threshold, renormalization, and breakdown scales, and define an observable-specific EFT validity certificate with a quantitative stability margin. Its zero-margin surface is an admissibility boundary for that certificate, not automatically a universal physical cutoff. Finally, an approximate intertwining theorem gives the precise data required to identify a selected Modal Triplet Theory (MTT) descent with a Wilsonian reduction: a same-source commuting diagram, observable map, truncation error, and provenance-controlled scale correspondence. Current MTT provides typed projection and local Feshbach–resolvent control for selected operator problems, but it does not yet supply this certificate for arbitrary quantum field theories. The result is therefore a rigorous structural interpretation and a completion contract, not a derivation of every EFT or a new ultraviolet completion.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: fd382717b5422739071d0562322aabe7367081044798010496fe09519b6b79ed
paper_id: effective-field-theory-as-a-shadow-of-projection-admiss-ec123406
release_state: zenodo_released
released_version: v2
title: |
  **Wilsonian Coarse-Graining and Projection-Admissible Description:**
  Inverse Maps, RG Flow, Universality, and Model-Specific Validity in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21711197
zenodo_record_id: 21711197
zenodo_url: "https://zenodo.org/records/21711197"
---

# Revision note for Version 2

<div class="description">

Version 1, DOI [10.5281/zenodo.18262361](https://doi.org/10.5281/zenodo.18262361).

Version 1 treated a noninjective reduction as if it ruled out a right inverse, treated Wilsonian coarse-graining and a beta-function ODE as the same map, identified every cutoff with an exact admissibility boundary, and inferred universality, fixed points, and irreversible scale flow from projection alone.

Version 2 separates representative sections, exact decoders, exact coarse-graining, finite truncation, and coupling-coordinate flow. It supplies counterexamples to the generic claims, defines a quantitative validity certificate, and proves a conditional MTT–Wilsonian intertwining bound.

Integrating out unresolved modes is naturally many-to-one at the level of retained data; ultraviolet inputs need not be uniquely recoverable from infrared data; fixed-point basins explain universality when their stability hypotheses hold; and MTT coherent reduction remains a plausible source of model-specific EFT descriptions.

No selected MTT construction currently identifies all Wilsonian scales, observables, and errors for a general interacting quantum field theory. The bridge remains conditional on the certificate in <a href="#sec:mtt" data-reference-type="ref+label" data-reference="sec:mtt">8</a>.

</div>

# The corrected question

Effective field theory is successful because it organizes predictions by resolution and accuracy. A low-energy observer need not retain every microscopic variable. Heavy modes can be integrated out, local operators can be ordered by power counting, and a finite number of coefficients can be matched to a more complete description or to experiment . Wilsonian renormalization makes this change of resolution systematic .

The earlier version asked whether all of this follows from noninjective projection. That question compresses too many objects into one word. Consider the following five statements:

1.  high-frequency variables have been integrated out;

2.  only finitely many effective operators have been retained;

3.  infrared data do not identify one unique ultraviolet input;

4.  running couplings satisfy a scale-dependent differential equation; and

5.  a family of microscopic descriptions approaches one observable universality class.

None of these statements is identical to another. The corrected question is:

> Under which explicit maps, domains, error bounds, and stability hypotheses does a Wilsonian effective description instantiate the projection–admissibility language used by MTT?

This paper answers that question without modifying standard EFT. The aim is to type the comparison, prove the implications that are genuinely mathematical, and mark the data that a physical MTT realization must still supply.

# The Wilsonian objects

## Exact reduction and finite truncation

For each ultraviolet scale $`\Lambda`$, let $`\mathcal D_\Lambda`$ denote a declared space of actions, measures, Hamiltonians, or other complete descriptions at that scale. For $`0<\mu<\Lambda`$, an exact coarse-graining map has the type
``` math
C_{\Lambda\to\mu}:\mathcal D_\Lambda\longrightarrow\mathcal D_\mu.
```
In a Euclidean path-integral presentation, a schematic representative is
``` math
\begin{equation}
 e^{-S_\mu[\phi_<]}
 =
 Z_{\Lambda,\mu}^{-1}
 \int \mathcal D\phi_>\,
 e^{-S_\Lambda[\phi_<+\phi_>]} .
\label{eq:wilsonian}
\end{equation}
```
The input and output of <a href="#eq:wilsonian" data-reference-type="ref+label" data-reference="eq:wilsonian">[eq:wilsonian]</a> are actions or measures. It is not, by itself, a map taking one ultraviolet field configuration to one infrared field configuration.

When nested integrations are compatible, one has
``` math
\begin{equation}
 C_{\nu\to\mu}\circ C_{\Lambda\to\nu}
 =
 C_{\Lambda\to\mu},
 \qquad
 0<\mu<\nu<\Lambda.
\label{eq:composition}
\end{equation}
```
Rescaling fields and momenta can be included in the definition of $`C_{\Lambda\to\mu}`$, but the convention must then be fixed before <a href="#eq:composition" data-reference-type="ref+label" data-reference="eq:composition">[eq:composition]</a> is asserted.

A practical EFT usually adds a second operation:
``` math
Q_{\mu,N}:\mathcal D_\mu\longrightarrow\mathcal T_{\mu,N},
```
where $`\mathcal T_{\mu,N}`$ is a finite or otherwise controlled family of operators and couplings. The implemented reduction is therefore
``` math
\mathcal R_{\Lambda\to\mu}^{(N)}
 =
 Q_{\mu,N}\circ C_{\Lambda\to\mu}.
```
Exact integration and finite truncation have different errors. A calculation can use an exact functional flow but an approximate truncation, or a controlled perturbative matching formula without explicitly constructing an exact functional flow .

## Observables and comparison

Let $`\mathcal O_\mu:\mathcal D_\mu\to\mathbb{R}^r`$ be a declared observable map and let $`\widehat{\mathcal O}_{\mu,N}:\mathcal T_{\mu,N}\to\mathbb{R}^r`$ be its EFT evaluator. The physically relevant question is not whether the effective coefficients remember every ultraviolet detail. It is whether
``` math
\begin{equation}
 \left\|
 \mathcal O_\mu(C_{\Lambda\to\mu}d)
 -
 \widehat{\mathcal O}_{\mu,N}
 (\mathcal R_{\Lambda\to\mu}^{(N)}d)
 \right\|
 \leq \varepsilon_{\mu,N}(d)
\label{eq:observable-error}
\end{equation}
```
on a stated input domain. The norm, observables, and error function are part of the theorem. Without them, “the EFT is valid” is an incomplete statement.

# Sections, decoders, and a concrete reduction

The revised Projection–Admissibility paper owns the general inverse taxonomy . For a reduction $`R:X\to Y=R(X)`$:

- a *representative section* $`S:Y\to X`$ satisfies $`R\circ S=\operatorname{id}_Y`$ and chooses one compatible source;

- an *exact decoder* $`D:Y\to X`$ satisfies $`D\circ R=\operatorname{id}_X`$ and recovers the actual source; and

- an autonomous reduced law requires the source evolution to be constant on the relevant initial reduction fibers.

A noninjective surjection can have a right section. It cannot have an exact decoder. Thus the correct Wilsonian statement is:

> Coarse-graining may be many-to-one and therefore fail to determine a unique ultraviolet input. A chosen ultraviolet completion is a representative section, not recovery of the input that actually produced the infrared data.

<div id="ex:gaussian" class="example">

**Example 1** (Gaussian mode elimination). Let
``` math
S_{a,b,c}(x,z)
 =
 \frac12\left(ax^2+2bxz+cz^2\right),
 \qquad
 c>0,
 \qquad
 k:=a-\frac{b^2}{c}>0.
```
Integrating out $`z`$ gives
``` math
\int_{\mathbb{R}}e^{-S_{a,b,c}(x,z)}\,dz
 =
 \sqrt{\frac{2\pi}{c}}\,
 e^{-kx^2/2}.
```
After quotienting the field-independent normalization, the retained coupling is $`k`$. The map
``` math
\Gamma(a,b,c)=a-\frac{b^2}{c}
```
is noninjective. The choice $`s(k)=(k,0,1)`$ is a right section, but it does not recover the original triple. Even this elementary exact integration already separates representative completion from exact ultraviolet decoding.

</div>

The Appelquist–Carazzone theorem gives a physically important but hypothesis-dependent version of decoupling: in its declared renormalizable setting, heavy fields decouple from low-momentum behavior apart from renormalization effects and suppressed contributions . It is not a theorem that every heavy mode in every theory can be removed with one universal error law.

# Scale composition is not coupling-space irreversibility

## A semigroup of reductions

Suppose compatible identifications place the scale-dependent description spaces in one space $`\mathcal D`$, and write
``` math
C_\tau:\mathcal D\to\mathcal D,
 \qquad
 \tau=\log(\Lambda/\mu)\geq0.
```
Then <a href="#eq:composition" data-reference-type="ref+label" data-reference="eq:composition">[eq:composition]</a> becomes
``` math
C_{\tau+\sigma}=C_\sigma\circ C_\tau,
 \qquad
 C_0=\operatorname{id}.
```

<div id="prop:semigroup" class="proposition">

**Proposition 2** (Noninjective coarse-graining cannot be a group action). *If $`C_{\tau_0}`$ is noninjective for some $`\tau_0>0`$, then the family $`\{C_\tau\}_{\tau\geq0}`$ cannot extend to a group of maps on $`\mathcal D`$ having $`C_{-\tau_0}`$ as a two-sided inverse.*

</div>

<div class="proof">

*Proof.* Every map possessing a left inverse is injective. A two-sided inverse would in particular be a left inverse of $`C_{\tau_0}`$, contradicting noninjectivity. ◻

</div>

This is the precise semigroup statement. It concerns the full declared description data on which $`C_\tau`$ acts.

## The beta-function ODE

A finite set of running couplings may instead satisfy
``` math
\begin{equation}
 \frac{d g}{dt}=\beta(g),
 \qquad
 t=\log\mu,
\label{eq:beta}
\end{equation}
```
on an open domain $`U\subset\mathbb{R}^n`$.

<div id="prop:ode" class="proposition">

**Proposition 3** (Local reversibility of regular coupling flow). *If $`\beta`$ is locally Lipschitz, then wherever solutions of <a href="#eq:beta" data-reference-type="ref+label" data-reference="eq:beta">[eq:beta]</a> exist for both $`t`$ and $`-t`$, the flow map $`\varphi_t`$ is locally invertible and
``` math
\varphi_t^{-1}=\varphi_{-t}.
```
If the vector field is complete, the family is a one-parameter group on $`U`$.*

</div>

<div class="proof">

*Proof.* Existence and uniqueness imply $`\varphi_{-t}(\varphi_t(g))=g`$ and $`\varphi_t(\varphi_{-t}(g))=g`$ whenever both compositions are defined. ◻

</div>

There is no contradiction between Propositions <a href="#prop:semigroup" data-reference-type="ref" data-reference="prop:semigroup">2</a> and <a href="#prop:ode" data-reference-type="ref" data-reference="prop:ode">3</a>. The couplings $`g`$ are coordinates in a selected reduced theory space. Reversing their ODE does not reconstruct the high-frequency field history, the discarded operators, or the microscopic action within a coarse-graining fiber.

<div class="example">

**Example 4** (Invertible coordinate flow after information loss). Continue Example <a href="#ex:gaussian" data-reference-type="ref" data-reference="ex:gaussian">1</a> and let the retained coefficient satisfy
``` math
\dot k=-k,
 \qquad
 k(t)=e^{-t}k(0).
```
For every finite $`t`$, this coordinate flow is invertible: $`k(0)=e^tk(t)`$. The original $`(a,b,c)`$ is still not determined by $`k(t)`$. Local reversibility of a beta-function ODE and nonunique ultraviolet decoding can therefore coexist in the same model.

</div>

The scale parameter is not physical time. A monotone coarse-graining parameter does not establish thermodynamic entropy production, measurement collapse, or an arrow of time. Those require their own dynamics, states, and monotonicity theorems.

# What universality actually requires

Noninjectivity says that at least one pair of source descriptions has the same reduced image. Universality is stronger: an entire family must approach the same long-distance observables or scaling data.

<div class="definition">

**Definition 5** (Observable universality on a basin). Let $`R:B\to B`$ be a coarse-graining map on an invariant set $`B`$, and let $`\mathcal O:B\to Z`$ take values in a metric space $`(Z,d_Z)`$. The set $`B`$ is observable-universal with rate $`\epsilon_n\to0`$ if
``` math
\sup_{x,y\in B}
 d_Z\!\left(\mathcal O(R^nx),\mathcal O(R^ny)\right)
 \leq\epsilon_n .
```

</div>

<div id="prop:not-universal" class="proposition">

**Proposition 6** (Noninjectivity alone is insufficient). *There is a noninjective projection for which no observable-universality conclusion holds on the full source set.*

</div>

<div class="proof">

*Proof.* Take $`B=\{0,1\}^2`$ and
``` math
R(a,b)=(a,0).
```
This is a noninjective self-map of $`B`$. Let $`\mathcal O(a,b)=a`$ with the discrete metric on $`\{0,1\}`$. Since $`R^n=R`$ for every $`n\geq1`$, the observable images of $`(0,0)`$ and $`(1,0)`$ remain distance one apart under every iterate. Thus no sequence $`\epsilon_n\to0`$ can satisfy the universality bound on $`B`$. ◻

</div>

<div id="prop:contraction" class="proposition">

**Proposition 7** (A contraction supplies a universality theorem). *Suppose $`B`$ is invariant and
``` math
d_Z\!\left(\mathcal O(Rx),\mathcal O(Ry)\right)
 \leq q\,
 d_Z\!\left(\mathcal O(x),\mathcal O(y)\right)
```
for all $`x,y\in B`$ and some $`0\leq q<1`$. Then
``` math
d_Z\!\left(\mathcal O(R^nx),\mathcal O(R^ny)\right)
 \leq
 q^n d_Z\!\left(\mathcal O(x),\mathcal O(y)\right).
```
If the observable diameter of $`B`$ is finite, $`B`$ is observable-universal with rate $`\epsilon_n=q^n\operatorname{diam}_Z(\mathcal O(B))`$.*

</div>

<div class="proof">

*Proof.* Iterate the contraction inequality $`n`$ times and take the supremum. ◻

</div>

The contraction can arise from a stable fixed point, a stable manifold, or a more general attracting set. It does not arise from projection syntax alone. Near an RG fixed point $`g_\ast`$, relevant and irrelevant directions are defined by the linearized coarse-graining map. With scale factor $`b>1`$, one commonly writes eigenvalues as $`b^{y_i}`$: directions with $`y_i>0`$ grow toward the infrared and are relevant, while directions with $`y_i<0`$ shrink and are irrelevant. This is a dynamical classification, not an automatic classification by an MTT margin.

Likewise, $`R(g_\ast)=g_\ast`$ is the fixed-point equation. Calling $`g_\ast`$ a point of “maximal admissibility” requires a separate theorem relating the selected EFT error or stability margin to distance from $`g_\ast`$. A fixed point can lie outside the domain of a particular truncation, and a useful EFT trajectory need not terminate at a fixed point.

# Cutoffs and validity certificates

## Several scales that must not be identified

<div class="tabularx">

@\>

p0.24Y Y@

Scale or datum & Role & Why it is not automatically a physical boundary
Regulator cutoff & Suppresses or excludes modes in a chosen calculation & Exact observables should be independent of the regulator convention.
Renormalization scale & Labels a parametrization of running couplings & Residual scale dependence often measures truncation error.
Matching scale & Point at which two descriptions are related & It may be moved within a window while coefficients transform.
Mass threshold & Energy at which a degree of freedom can no longer be treated as heavy & Threshold location and EFT breakdown need not coincide.
Power-counting scale & Suppresses higher-dimensional operators & Its operational meaning depends on observables and target precision.
Breakdown scale & Point where a declared approximation no longer meets its tolerance & It is certificate- and observable-dependent unless a stronger invariant theorem is supplied.

</div>

Functional RG formulations make the distinction particularly visible. Polchinski and Wetterich equations provide exact scale-dependent functional equations, while practical work uses regulator choices and truncations . Different exact RG schemes can be related by field redefinitions; residual scheme dependence in a truncated calculation is not itself a new physical scale.

## An observable-specific certificate

<div id="def:eft-certificate" class="definition">

**Definition 8** (EFT validity certificate). Fix an input set $`K\subseteq\mathcal D_\Lambda`$, observables $`\mathcal O_\mu`$, tolerance $`\tau>0`$, exact reduction $`C_{\Lambda\to\mu}`$, truncation $`Q_{\mu,N}`$, and evaluator $`\widehat{\mathcal O}_{\mu,N}`$. An EFT validity certificate is a machine-checkable or analytic bound
``` math
\varepsilon_{\mu,N}:K\to[0,\infty)
```
for which <a href="#eq:observable-error" data-reference-type="ref+label" data-reference="eq:observable-error">[eq:observable-error]</a> holds. Its certified admissible set is
``` math
\mathcal A_{\tau}
 =
 \left\{(\mu,d):d\in K,\ \varepsilon_{\mu,N}(d)<\tau\right\},
```
and its margin is
``` math
m_{\tau}(\mu,d)=\tau-\varepsilon_{\mu,N}(d).
```

</div>

<div id="prop:validity" class="proposition">

**Proposition 9** (Local stability of a validity certificate). *Suppose, at fixed $`\mu`$, the error bound is $`L`$-Lipschitz on a metric input domain:
``` math
\left|\varepsilon_{\mu,N}(d)-\varepsilon_{\mu,N}(d')\right|
 \leq L\,d_K(d,d').
```
If $`m_{\tau}(\mu,d_0)>0`$, then every $`d`$ satisfying
``` math
d_K(d,d_0)<\frac{m_{\tau}(\mu,d_0)}{L}
```
is certified admissible when $`L>0`$. For $`L=0`$, the bound is constant on the entire declared domain, so every point in that domain is certified admissible whenever $`d_0`$ is.*

</div>

<div class="proof">

*Proof.* The Lipschitz inequality gives
``` math
\varepsilon_{\mu,N}(d)
 <
 \varepsilon_{\mu,N}(d_0)+m_{\tau}(\mu,d_0)
 =
 \tau.
```
 ◻

</div>

The zero set $`m_\tau=0`$ is a precise boundary for this certificate. It is not automatically a singularity of the underlying theory, a universal ultraviolet scale, or the boundary of every other observable family. A different truncation, nonperturbative method, or target tolerance can move it.

# Breakdown has several meanings

The phrase “the EFT breaks down” must identify what failed.

1.  *Power-counting failure:* the nominal expansion parameter is no longer small.

2.  *Perturbative failure:* a coupling is large or a perturbation series is not useful, while a nonperturbative formulation of the same EFT may remain valid.

3.  *Truncation failure:* omitted operators exceed the declared error tolerance.

4.  *Threshold crossing:* new degrees of freedom become kinematically or dynamically relevant and should be included explicitly.

5.  *Matching or scheme failure:* the chosen coordinates, regulator, or matching prescription are poorly conditioned.

6.  *Physical inconsistency:* unitarity, positivity, locality, or another required physical condition fails in the claimed domain.

7.  *MTT admissibility exit:* a selected MTT margin reaches zero under a proved identification with the EFT error.

Only the last item is an MTT statement. It cannot be inferred merely because a perturbative series becomes inconvenient. Strong coupling can demand a new calculation, a dual set of variables, or a new EFT, but it need not mean that the underlying theory or every effective description has ceased to exist. Likewise, trans-Planckian sensitivity is a warning about an extrapolation; its interpretation depends on the selected state, observable, and ultraviolet assumptions.

The decoupling and power-counting literature explains why many EFTs are controlled in scale-separated regimes . It does not replace the error certificate for a particular model.

# The conditional MTT–Wilsonian bridge

## A typed comparison diagram

Let $`\mathcal U_\Lambda`$ be a selected upper MTT source domain and let
``` math
P_{\Lambda\to\mu}:\mathcal U_\Lambda\to\mathcal Y_\mu
```
be a selected MTT descent. Let
``` math
E_\Lambda:\mathcal U_\Lambda\to\mathcal D_\Lambda,
 \qquad
 E_\mu:\mathcal Y_\mu\to\mathcal D_\mu
```
encode the upper and descended descriptions into the Wilsonian theory spaces. The proposed square is
``` math
\begin{array}{ccc}
\mathcal U_\Lambda
& \xrightarrow{\quad P_{\Lambda\to\mu}\quad} &
\mathcal Y_\mu
\\[2mm]
\downarrow E_\Lambda && \downarrow E_\mu
\\[2mm]
\mathcal D_\Lambda
& \xrightarrow{\quad C_{\Lambda\to\mu}\quad} &
\mathcal D_\mu .
\end{array}
```
The square need not commute exactly, but its defect must be bounded in a declared metric.

<div id="thm:bridge" class="theorem">

**Theorem 10** (Observable transfer through an approximate bridge). *Assume that for every $`u`$ in a declared domain $`K\subseteq\mathcal
U_\Lambda`$,
``` math
\begin{equation}
 d_\mu\!\left(
 E_\mu P_{\Lambda\to\mu}u,\,
 C_{\Lambda\to\mu}E_\Lambda u
 \right)
 \leq\delta(u).
\label{eq:intertwiner}
\end{equation}
```
Let $`\mathcal O_\mu:(\mathcal D_\mu,d_\mu)\to\mathbb{R}^r`$ be $`L_{\mathcal O}`$-Lipschitz, and suppose the EFT evaluator satisfies
``` math
\begin{equation}
 \left\|
 \mathcal O_\mu(C_{\Lambda\to\mu}E_\Lambda u)
 -
 \widehat{\mathcal O}_{\mu,N}
 (Q_{\mu,N}C_{\Lambda\to\mu}E_\Lambda u)
 \right\|
 \leq\varepsilon(u).
\label{eq:eft-bound}
\end{equation}
```
Then
``` math
\begin{align}
 &\left\|
 \mathcal O_\mu(E_\mu P_{\Lambda\to\mu}u)
 -
 \widehat{\mathcal O}_{\mu,N}
 (Q_{\mu,N}C_{\Lambda\to\mu}E_\Lambda u)
 \right\|
 \nonumber\\
 &\hspace{35mm}
 \leq L_{\mathcal O}\delta(u)+\varepsilon(u).
\label{eq:bridge-bound}
\end{align}
```*

</div>

<div class="proof">

*Proof.* Insert $`\mathcal O_\mu(C_{\Lambda\to\mu}E_\Lambda u)`$, apply the triangle inequality, use the Lipschitz estimate with <a href="#eq:intertwiner" data-reference-type="ref+label" data-reference="eq:intertwiner">[eq:intertwiner]</a>, and then apply <a href="#eq:eft-bound" data-reference-type="ref+label" data-reference="eq:eft-bound">[eq:eft-bound]</a>. ◻

</div>

<a href="#thm:bridge" data-reference-type="ref+Label" data-reference="thm:bridge">10</a> is deliberately modest. It proves agreement of declared observables on one domain. It does not prove that the microscopic theories are identical, that every EFT arises from the same MTT carrier, or that the effective coordinates determine a unique ultraviolet state.

## The certificate rows

A physical MTT–Wilsonian identification requires at least the following rows.

<div class="tabularx">

@p0.24Y@ Row & Required content
Selected source & One MTT carrier, state/action, domain, and provenance hash.
Scale family & A defined $`\Lambda\mapsto\mu`$ reduction family with composition law or controlled defect.
Wilsonian target & Theory spaces, regulator convention, fields, operator basis, and renormalization scheme.
Encoding maps & Explicit $`E_\Lambda`$ and $`E_\mu`$, including domains and conventions.
Intertwining & Exact commutation or the verified defect $`\delta`$ in <a href="#eq:intertwiner" data-reference-type="ref+label" data-reference="eq:intertwiner">[eq:intertwiner]</a>.
Observable evaluator & A declared observable family, Lipschitz or continuity control, matching, and truncation error $`\varepsilon`$.
Scale interpretation & A proof distinguishing regulator, matching, threshold, and physical breakdown scales.
Boundary identification & A theorem relating the MTT margin to $`\tau-(L_{\mathcal O}\delta+\varepsilon)`$, not a verbal analogy.
Scheme covariance & The transformation of the certificate under allowed field, regulator, and coordinate changes.

</div>

If all rows hold and
``` math
L_{\mathcal O}\delta(u)+\varepsilon(u)<\tau,
```
then <a href="#thm:bridge" data-reference-type="ref+label" data-reference="thm:bridge">10</a> gives an EFT validity certificate for the selected MTT descent. To identify a cutoff surface with an MTT admissibility boundary, one must additionally prove that the positive MTT margin and the positive observable margin have the same domain or a controlled implication in the claimed direction.

## What current MTT supplies

The current MTT corpus supplies three relevant but separate layers.

1.  Foundations specifies coherent projection, stabilization, and typed claim boundaries .

2.  Projection–Admissibility separates sections, decoders, autonomous descent, and effective mergers; its Wilsonian discussion already states that universality requires a basin or fixed-point theorem .

3.  Coherent-Sector Reduction proves local Feshbach–Schur and resolvent-error control for declared operators, projectors, spectral parameters, and common resolvent regions .

Those results can populate parts of <a href="#tab:bridge" data-reference-type="ref+label" data-reference="tab:bridge">[tab:bridge]</a> for a selected model. A Feshbach reduction is not automatically Wilsonian mode integration, and a spectral gap is not automatically an EFT breakdown scale. The Conditional-Classification paper likewise requires separate witness records for projection, ultraviolet, event, and matter claims .

Accordingly, this paper makes no new promotion of MTT’s QFT or ultraviolet completion status. It supplies the map and error contract against which a future selected construction can be checked.

# Relation to the established literature

<div class="tabularx">

@\>

p0.24Y Y@

Source & What it establishes & What it does not establish
Kadanoff; Wilson; Wilson–Kogut & Coarse-graining, scaling, fixed points, relevant/irrelevant directions, and universality in specified statistical and field-theoretic settings & A generic MTT admissibility boundary or universality from noninjectivity alone
Appelquist–Carazzone & Heavy-field decoupling under its renormalizable-theory hypotheses & Uniform decoupling in every strongly coupled or nonlocal theory
Weinberg; Georgi; Burgess & Symmetry-based EFT construction, matching, scale hierarchy, and power counting & A unique ultraviolet completion or one universal physical cutoff
Polchinski; Wetterich; Rosten & Exact functional scale equations, regulator-dependent formulations, and controlled approximation programs & Identity of functional flow, finite truncation, and microscopic decoding

</div>

The external literature therefore supports the central analogy: Wilsonian reduction is a disciplined loss of unresolved detail with controlled long-distance predictions. It also enforces the correction. Universality, decoupling, fixed points, and truncation control are model-dependent theorems, not consequences of writing down a many-to-one map.

# Completion and falsifiability

The structural bridge can fail in precise ways.

1.  The proposed MTT descent and Wilsonian coarse-graining do not satisfy the intertwining bound on the claimed source domain.

2.  The selected observable map is discontinuous or lacks the stated Lipschitz/control bound.

3.  Truncation or matching errors exceed the advertised tolerance.

4.  Regulator or scheme changes move the claimed physical boundary without a compensating transformation of observables.

5.  The proposed universality class lacks an invariant basin or contraction estimate.

6.  A claimed fixed point does not solve the selected RG fixed-point equation, or its relevant/irrelevant spectrum is not controlled.

7.  Strong coupling is labeled “EFT failure” even though a nonperturbative formulation remains predictive in the same observable domain.

8.  The MTT margin and the EFT validity margin reach zero on different domains.

A successful computational packet should therefore contain the rows in <a href="#tab:bridge" data-reference-type="ref+label" data-reference="tab:bridge">[tab:bridge]</a>, the input hashes, the regulator and scheme conventions, the observable list, interval or analytic error bounds, and held-out checks not used to choose the truncation. A plot of running couplings or a small training residual is not by itself an equivalence certificate.

# Conclusion

Wilsonian EFT and projection-admissible description are compatible, but they are not synonyms. Exact mode integration, finite operator truncation, running-coupling coordinates, observable universality, and physical breakdown each require their own map and hypothesis. Noninjective coarse-graining rules out an exact decoder of the actual ultraviolet input; it does not rule out representative sections, make every beta-function flow irreversible, or generate universality by itself.

The corrected MTT claim is conditional and useful. If one selected MTT source, Wilsonian family, encoding square, observable map, and quantitative error budget satisfy <a href="#thm:bridge" data-reference-type="ref+label" data-reference="thm:bridge">10</a>, then the corresponding EFT is a controlled shadow of that MTT descent on the certified domain. If the MTT and EFT margins are also proved to select the same boundary, the admissibility interpretation becomes physical rather than metaphorical. Until those rows are supplied for a model, the paper remains a structural comparison and a precise research contract.
