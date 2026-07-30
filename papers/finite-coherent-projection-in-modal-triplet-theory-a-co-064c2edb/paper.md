---
abstract: |
  Finite coherent filtering is a useful common language for several Modal Triplet Theory constructions, but it does not by itself derive every physical sector in which a filter can be written. This paper gives the operator statement a precise domain. It distinguishes an orthogonal projector, a smooth spectral filter, and a positive measurement effect; proves positivity and contraction of the sandwiched filter without assuming commutativity; states the additional hypothesis needed for a modal eigenvalue formula; and derives the Euclidean heat kernel and its sharp delta limit. The current finite q79 Hessian supplies an exact six-mode illustration with a rank-two coherent kernel and rank-four complement. A separate no-go theorem proves that filtering only internal modes cannot suppress arbitrarily high four-dimensional momenta. Gauge, gravitational, Lorentzian, and measurement applications therefore require their own compatible operators, constraints, and source maps. The result is a rigorous operator toolkit and a clear list of transfer obligations, not a universal derivation of quantum field theory or quantum gravity.
author:
- Peter Nero
current_version: v3
date: July 2026 Version 3
generated_from_main_tex_sha256: dc7a64311b2802dd50ccbb141c8fa8959ec4ab428c7139030debfef6ed3a6f3c
paper_id: finite-coherent-projection-in-modal-triplet-theory-a-co-064c2edb
release_state: zenodo_released
released_version: v3
title: |
  Finite Coherent Filters in Modal Triplet Theory:
  Operator Types, Exact Kernels, and Sectoral Boundaries
zenodo_doi: 10.5281/zenodo.21665970
zenodo_record_id: 21665970
zenodo_url: "https://zenodo.org/records/21665970"
---

# Version 3 Revision Note

<div class="description">

Version 2, *Finite Coherent Projection in Modal Triplet Theory: A Common Architecture for Duality, Gauge, Gravity, Quantization, Entanglement, and Measurement*.

The earlier paper did not keep a sharp projector, a smooth filter, and a positive measurement effect consistently separate. It also risked transferring an internal spectral cutoff into four-dimensional ultraviolet claims without a bridge theorem.

The operator variables and spectra are now typed explicitly. The central analytic theorem is corrected, the q79 finite example is imported at its established tier, and an internal-to-spacetime no-go theorem is added.

The positive-contraction filter, its local and spectral representations, and the heat-kernel delta limit remain valid under the stated assumptions.

Physical gauge, gravitational, Lorentzian, and measurement uses still require selected same-source operators and compatibility theorems. No four-dimensional UV completion follows from the internal projector alone.

</div>

# Why the distinctions matter

The phrase “finite coherent projection” originally served as an umbrella for three operations. They are related, but they answer different questions.

1.  A *sharp projector* decides membership in a closed subspace.

2.  A *smooth filter* attenuates spectral components by different amounts.

3.  A *measurement effect* assigns an outcome probability in a specified quantum model.

Conflating them creates immediate errors. A smooth heat filter is usually not idempotent, so it is not a projector. A positive filter may be used as one effect of a measurement, but it does not specify the state update or the other outcomes. An internal filter can remove internal modes while leaving four-dimensional momentum untouched.

The corrected role of this paper is consequently modest but useful. It provides the common operator calculus, gives an exact finite MTT instantiation, and lists the extra data needed before the same notation can be used in a physical sector.

# Three operator types

<div class="definition">

**Definition 1** (Sharp projector). An orthogonal projector on a Hilbert space $`\mathcal H`$ is a bounded operator
``` math
P=P^\ast=P^2.
```
It represents the exact closed subspace $`\operatorname{Ran}P`$.

</div>

<div class="definition">

**Definition 2** (Smooth spectral filter). Let $`A`$ be a nonnegative self-adjoint operator on $`\mathcal H`$. For a bounded Borel function $`f:[0,\infty)\to[0,1]`$, functional calculus defines
``` math
F=f(A), \qquad 0\leq F\leq I.
```
Unless $`f`$ takes only the values zero and one on $`\operatorname{spec}A`$, $`F`$ is not a projector.

</div>

<div class="definition">

**Definition 3** (Effect and instrument). An effect is an operator $`E`$ satisfying $`0\leq E\leq I`$. A finite POVM is a family $`\{E_i\}`$ with $`\sum_iE_i=I`$. An instrument additionally specifies completely positive maps whose outcome probabilities and post-measurement states agree with the effects.

</div>

Thus every projector is an effect, but not every effect is a projector. Neither object alone specifies a measurement instrument. This distinction is important in MTT because admissibility, attenuation, and record formation belong to different logical layers.

# Specified filter data

The abstract data used in the rest of the paper are:
``` math
(\mathcal H,A,P,\chi,\tau),
```
where

- $`\mathcal H`$ is a complex Hilbert space;

- $`A\geq0`$ is self-adjoint, with its domain fixed;

- $`P`$ is an orthogonal projector;

- $`\chi:[0,\infty)\to[0,1]`$ is bounded and Borel measurable;

- $`\tau\geq0`$ is a declared filter parameter.

Define
``` math
\begin{equation}
 G_\tau=\chi(A)e^{-\tau A/2},
 \qquad
 B_{\mathrm{adm}}=P\,G_\tau^2P
       =P\chi(A)e^{-\tau A}\chi(A)P.
 \label{eq:Badm}
\end{equation}
```
The symbol $`A`$ is not universal. On a compact internal manifold $`Y`$ it may be a nonnegative elliptic operator on $`L^2(Y,E)`$, in which case its spectrum is discrete under standard hypotheses. On Euclidean spacetime it may be $`-\Delta`$. On a Cauchy slice it may be a positive spatial operator. These are different choices on different Hilbert spaces and may not be silently identified.

# The finite-filter theorem

<div id="thm:filter" class="theorem">

**Theorem 4** (Sandwiched finite filter). *For the data above, no commutation assumption between $`P`$ and $`A`$ is needed to conclude
``` math
0\leq B_{\mathrm{adm}}\leq I,
 \qquad
 \operatorname{Ran}B_{\mathrm{adm}}\subseteq\operatorname{Ran}P.
```
If in addition $`[P,A]=0`$, and
``` math
A\phi_n=\lambda_n\phi_n,\qquad
 P\phi_n=p_n\phi_n,\qquad p_n\in\{0,1\},
```
then
``` math
B_{\mathrm{adm}}\phi_n
 =p_n\chi(\lambda_n)^2e^{-\tau\lambda_n}\phi_n.
```*

</div>

<div class="proof">

*Proof.* Because $`\chi(A)`$ and $`e^{-\tau A/2}`$ are commuting bounded functions of $`A`$, $`G_\tau`$ is a positive contraction. Hence
``` math
B_{\mathrm{adm}}=(G_\tau P)^\ast(G_\tau P)\geq0
```
and
``` math
\|B_{\mathrm{adm}}\|\leq\|G_\tau P\|^2\leq1.
```
The outer factor $`P`$ places the range in $`\operatorname{Ran}P`$. Under the additional commutation hypothesis, $`A`$ and $`P`$ admit the displayed common modal action, and functional calculus gives the eigenvalue formula. ◻

</div>

<div id="cor:idempotence" class="corollary">

**Corollary 5** (When the filter is actually a projector). *In the commuting pure-point setting of <a href="#thm:filter" data-reference-type="ref+label" data-reference="thm:filter">4</a>, $`B_{\mathrm{adm}}`$ is a projector exactly when every retained weight
``` math
p_n\chi(\lambda_n)^2e^{-\tau\lambda_n}
```
is zero or one. In particular, for $`\tau>0`$, every retained mode with $`\lambda_n>0`$ has weight strictly below one whenever $`\chi(\lambda_n)\neq0`$.*

</div>

This is why $`B_{\mathrm{adm}}`$ should be called a finite coherent filter, not the coherent projector. The sharp object is $`P`$; the attenuation is carried by $`G_\tau`$.

## Kernel representation

When $`B_{\mathrm{adm}}`$ has an integral kernel,
``` math
(B_{\mathrm{adm}}\psi)(x)=\int K_{\mathrm{adm}}(x,y)\psi(y)\,dy.
```
In a commuting discrete eigenbasis,
``` math
\begin{equation}
 K_{\mathrm{adm}}(x,y)=
 \sum_n p_n\chi(\lambda_n)^2e^{-\tau\lambda_n}
 \phi_n(x)\overline{\phi_n(y)}.
 \label{eq:spectral-kernel}
\end{equation}
```
The coordinate-space kernel and spectral sum are two representations of the same operator. Calling one a “particle shadow” and the other a “wave shadow” is an MTT interpretation of that dual representation. The equation alone does not derive complementarity, the Born rule, or detector dynamics.

# The exact heat-kernel benchmark

<div id="thm:heat" class="theorem">

**Theorem 6** (Euclidean heat kernel and delta limit). *Let $`\mathcal H=L^2(\mathbb R^d)`$, $`A=-\Delta`$, $`P=I`$, and $`\chi=1`$. For $`\tau>0`$,
``` math
B_{\mathrm{adm}}=e^{\tau\Delta}
```
has kernel
``` math
\begin{equation}
 K_\tau(x,y)=
 (4\pi\tau)^{-d/2}
 \exp\!\left(-\frac{|x-y|^2}{4\tau}\right).
 \label{eq:heat-kernel}
\end{equation}
```
Moreover $`e^{\tau\Delta}\psi\to\psi`$ strongly in $`L^2`$, and $`K_\tau(x,\cdot)\to\delta_x`$ in the distributional sense as $`\tau\downarrow0`$.*

</div>

<div class="proof">

*Proof.* The Fourier transform diagonalizes $`-\Delta`$, so
``` math
\widehat{e^{\tau\Delta}\psi}(k)=e^{-\tau|k|^2}\widehat\psi(k).
```
Fourier inversion gives <a href="#eq:heat-kernel" data-reference-type="eqref" data-reference="eq:heat-kernel">[eq:heat-kernel]</a>. Dominated convergence proves strong $`L^2`$ convergence. Pairing the normalized Gaussian with a test function and rescaling $`y=x+\sqrt{\tau}\,z`$ proves the distributional limit. ◻

</div>

This theorem is exact, but it is a Euclidean spacetime benchmark. It is not obtained merely by selecting internal q79 modes. It also says nothing by itself about Lorentzian support, reflection positivity, unitarity, gauge identities, or removal of a quantum-field-theory regulator.

# The exact finite q79 illustration

The current MTT Foundation establishes, on its selected finite q79 flat-symbol carrier, a normalized Hessian
``` math
A_{\mathrm{fin}}=\kappa_{\mathrm{fin}}^{-1}H_{\mathrm{fin}}
```
with
``` math
\operatorname{spec}A_{\mathrm{fin}}
 =\{0\text{ with multiplicity }2,\;
    1\text{ with multiplicity }4\}.
```
It also identifies the rank-two Haar projector $`P_{\mathrm{Haar}}`$ with the zero eigenspace and proves compatibility with the shared finite line and the $`1+2+3`$ sector projectors. Those are imported Foundation results; this paper does not claim ownership of them.

Writing $`Q=I-P_{\mathrm{Haar}}`$, functional calculus is completely explicit:
``` math
\begin{align}
 e^{-\tau A_{\mathrm{fin}}}
 &=P_{\mathrm{Haar}}+e^{-\tau}Q,\\
 \chi(A_{\mathrm{fin}})
 &=\chi(0)P_{\mathrm{Haar}}+\chi(1)Q.
\end{align}
```
Consequently, with $`P=I`$,
``` math
\begin{equation}
 B_{\mathrm{adm}}=
 \chi(0)^2P_{\mathrm{Haar}}
 +\chi(1)^2e^{-\tau}Q.
 \label{eq:q79-filter}
\end{equation}
```
If instead $`P=P_{\mathrm{Haar}}`$, then
``` math
B_{\mathrm{adm}}=\chi(0)^2P_{\mathrm{Haar}}.
```

Equation <a href="#eq:q79-filter" data-reference-type="eqref" data-reference="eq:q79-filter">[eq:q79-filter]</a> is a genuine exact finite filter. It distinguishes a two-dimensional coherent kernel from a four-dimensional penalized complement. It does not select a physical value of $`\tau`$, a continuum HYM operator, a four-dimensional propagator, or a detector effect. Those identifications require further source maps.

# Why internal filtering is not a spacetime UV cutoff

<div id="thm:no-go" class="theorem">

**Theorem 7** (Internal-filter UV no-go). *Let $`\mathcal H=\mathcal H_4\otimes\mathcal H_{\mathrm{int}}`$. Let $`A_4`$ be an unbounded nonnegative self-adjoint operator on $`\mathcal H_4`$ whose spectral subspace above every finite threshold is nonzero. If $`B_{\mathrm{int}}\neq0`$ is bounded, then
``` math
R=I_4\otimes B_{\mathrm{int}}
```
does not annihilate or attenuate all sufficiently high $`A_4`$-modes. Therefore an internal finite-rank projector or smooth filter, acting alone, is not a four-dimensional ultraviolet regulator.*

</div>

<div class="proof">

*Proof.* For any cutoff $`\Lambda`$, choose a nonzero $`u_\Lambda`$ in the spectral subspace $`\mathbf 1_{(\Lambda,\infty)}(A_4)\mathcal H_4`$. Since $`B_{\mathrm{int}}\neq0`$, choose $`v`$ with $`B_{\mathrm{int}}v\neq0`$. Then
``` math
R(u_\Lambda\otimes v)
 =u_\Lambda\otimes B_{\mathrm{int}}v\neq0.
```
The four-dimensional spectral label of $`u_\Lambda`$ is unchanged, and $`\Lambda`$ was arbitrary. ◻

</div>

The theorem leaves open a useful route. A derived four-dimensional filter could arise after reduction if a proved intertwiner maps internal geometry to a spacetime operator $`A_4`$, including its normalization and constraints. But that map is precisely an additional theorem. It cannot be replaced by using the same letter $`A`$ in both settings.

# What sectoral promotion requires

## Gauge theory

A gauge-sector filter must be defined on a gauge-covariant complex or on the physical quotient. At minimum one needs a relation such as
``` math
[F,C_a]=0
```
on a common invariant domain for the constraints $`C_a`$, or a chain-map identity with the BRST differential. A generic spectral filter can violate Ward or Slavnov–Taylor identities. The presence of a Lens-like quotient in the MTT vocabulary does not establish these analytic identities.

## Gravity

For linearized gravity one may specify a transverse-traceless projector and a positive spatial or Euclidean operator. Nonlinear gravity additionally requires diffeomorphism constraints, lapse and shift treatment, boundary terms, and a selected action. A filter on internal bundle modes does not automatically define a diffeomorphism-compatible graviton propagator.

## Lorentzian evolution

The heat kernel in <a href="#thm:heat" data-reference-type="ref+label" data-reference="thm:heat">6</a> is Euclidean. Replacing $`-\Delta`$ by a hyperbolic wave operator does not automatically produce a positive, retarded, or causal filter. A bounded spatial filter can be used on Cauchy data, but if it is nonlocal it may still alter support properties. A physical claim therefore needs a retarded kernel, a support estimate, or a preparation/readout interpretation.

## Measurement

By <a href="#thm:filter" data-reference-type="ref+label" data-reference="thm:filter">4</a>, $`B_{\mathrm{adm}}`$ is an effect. It can define the binary POVM $`\{B_{\mathrm{adm}},I-B_{\mathrm{adm}}\}`$ in standard quantum mechanics. This does not select an instrument, derive quadratic probabilities from pre-quantum MTT data, or pick one ontic outcome. Those are separate source and dynamics questions.

## Entanglement

On a bipartite Hilbert space, a joint filter need not factor:
``` math
B_{AB}\neq B_A\otimes B_B.
```
That observation permits correlated or entangled coherent sectors, but nonfactorization alone does not derive a particular state, Bell correlations, or no-signaling. Those properties must be checked in the chosen state and observable algebra.

# Circle, Lens, and Nil after reconciliation

The safest use of Circle–Lens–Nil in this paper is an operator and filtration language:

<div class="description">

phase or holonomy data carried by a specified line bundle and connection;

quotient, identification, or invariant-sector data implemented by a specified projector or group action;

survivor, shear, or non-semisimple data implemented by a specified operator and domain.

</div>

This is not a claim that the physical compactification is the literal nested manifold “circle inside Lens inside Nil.” The selected q79 Fu–Yau branch and the finite shared line have their own topology. Equality of suggestive roles does not establish equality of bundles, connections, Hessians, or spectra.

# Status ledger

<div class="center">

| Statement | Status | Evidence or missing object |
|:---|:---|:---|
| Positive-contraction theorem | Exact | <a href="#thm:filter" data-reference-type="ref+label" data-reference="thm:filter">4</a>, by functional calculus. |
| Projector/filter/effect distinction | Exact | Definitions and <a href="#cor:idempotence" data-reference-type="ref+label" data-reference="cor:idempotence">5</a>. |
| Euclidean Gaussian kernel and delta limit | Exact | <a href="#thm:heat" data-reference-type="ref+label" data-reference="thm:heat">6</a>. |
| Finite q79 two-plus-four filter | Exact, imported | Foundation finite Hessian and Haar-projector theorem. |
| Internal filter is not a 4D UV cutoff | Exact | <a href="#thm:no-go" data-reference-type="ref+label" data-reference="thm:no-go">7</a>. |
| Physical continuum q79 filter | Open | Selected nonflat HYM operator, domain, spectrum, and normalization. |
| Gauge-compatible filter | Conditional | Constraint or BRST chain-map theorem is required. |
| Gravity-compatible filter | Conditional | Selected action, constraints, causal kernel, and continuum limit are required. |
| Measurement model | Conditional/open | POVM use is standard; selected MTT instrument and general Born source remain separate. |
| Universal projection-shadow theorem | Withdrawn | One operator template does not derive all sectoral physics. |

</div>

# Discussion

The corrected result is stronger than a broad analogy because it is falsifiable at each transfer. Once $`\mathcal H`$, $`A`$, $`P`$, $`\chi`$, and $`\tau`$ are declared, positivity, idempotence, spectral weights, and kernel limits can be checked. When a proposed application changes Hilbert space, constraints, signature, or observable algebra, the required bridge becomes visible rather than being hidden in notation.

The q79 finite carrier is particularly informative. It shows that MTT currently has an exact finite spectral decomposition, not merely a verbal picture of coherence. At the same time, <a href="#thm:no-go" data-reference-type="ref+label" data-reference="thm:no-go">7</a> identifies the precise limit of that success: the finite internal spectrum is not yet a four-dimensional UV theorem. A future derivation must transport the selected geometry into a physical spacetime operator while preserving the relevant connections, constraints, Hessians, and causal structure.

This separation also clarifies the role of finite cutoff exactness. If the selected physical object is itself a finite projected algebra, its trace and functional calculus are exact at that tier. Exactness of the finite object does not imply that it approximates a continuum theory with zero error. A continuum claim needs either an equivalence theorem or explicit convergence and error bounds.

# Conclusion

Finite coherent filtering survives corpus reconciliation as a rigorous and useful MTT tool. The central operator is a positive contraction; it has well-defined modal and kernel representations; its Euclidean heat-kernel specialization converges to a delta distribution; and the current finite q79 Hessian gives an exact two-plus-four example.

The same analysis closes an important loophole. An internal projector does not suppress high four-dimensional momentum merely because both operations are called filters. Physical promotion requires a selected operator on the correct Hilbert space together with gauge, gravitational, Lorentzian, or measurement compatibility as appropriate. That is the right frontier for this architecture.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, current revised MTT paper corpus, 2026.

P. Nero, *A Projection-First Reframing of Quantum Gravity*, current revised MTT paper corpus, 2026.

P. Nero, *A Conditional Euclidean Transverse-Traceless Filter Model in Modal Triplet Theory*, current revised MTT paper corpus, 2026.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980.

E. B. Davies, *Heat Kernels and Spectral Theory*, Cambridge University Press, 1989.

A. S. Holevo, *Probabilistic and Statistical Aspects of Quantum Theory*, North-Holland, 1982.

M. Henneaux and C. Teitelboim, *Quantization of Gauge Systems*, Princeton University Press, 1992.

C. Bär, N. Ginoux, and F. Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007.

</div>
