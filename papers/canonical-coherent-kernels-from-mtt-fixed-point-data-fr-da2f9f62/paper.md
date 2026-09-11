---
abstract: |
  This paper isolates the exact projected-heat-kernel statement available from declared fixed-point data. On a specified compact Riemannian internal space, Euclidean problem, or spatial Cauchy-slice Hilbert space, let $`A`$ be a nonnegative self-adjoint elliptic operator, let $`P`$ be a reducing orthogonal projector, and let $`\tau>0`$. Functional calculus then uniquely defines
  ``` math
  K_{\mathrm{MTT}}(x,y;\tau)
          =
          \langle x|\,P e^{-\tau A}P\,|y\rangle .
  ```
  We prove smoothness in the elliptic spectral setting, covariance under unitary equivalence, coherent-band error estimates, and the joint distributional limit to the full identity. The harmonic case is important: if $`AP=0`$, then $`Pe^{-\tau A}P=P`$, so $`\tau`$ creates no additional smoothing on the retained sector. Gap damping concerns $`e^{-\tau A}Q`$; the projected operator $`Pe^{-\tau A}P`$ instead annihilates $`Q`$.

  These facts do not authorize a universal replacement of spacetime deltas, canonical commutators, gauge constraints, or local vertices. Such a replacement is a new physical model unless a selected realization supplies the operator domain, $`A`$, $`P`$, and $`\tau`$, and separately proves locality or causal support, covariance, gauge/BRST compatibility, and the relevant algebraic identities. The result is therefore a conditional execution interface, not a derivation of a universal MTT regulator.
author:
- Peter Nero
current_version: v2
date: September 2026, Version 2
generated_from_main_tex_sha256: a6372b278314f9f2f27c459905cd31808b848e577a5b0e255d980a6d2ac8dfb9
paper_id: canonical-coherent-kernels-from-mtt-fixed-point-data-fr-da2f9f62
release_state: current_revised_tex
released_version: v1
title: |
  **Projected Heat Kernels from MTT Fixed-Point Data**
  Conditional Sector Identities and the Physical-Replacement Boundary
zenodo_doi: 10.5281/zenodo.21703907
zenodo_record_id: 21703907
zenodo_url: "https://zenodo.org/records/21703907"
---

# Version 2 Revision Note

Supersedes
Version 1. The previous release remains public until a new release is approved.

Reason
Restrict all-orders boundary convergence to the compatible operator domain.

Resolution
Separates strong L2, distributional-kernel and compatible-domain smooth convergence, with a Dirichlet counterexample and graph-norm proof.

Retained result
Correctly scoped results and explanatory examples remain; no physical source-selection claim is promoted.

Remaining boundary
Realization hypotheses and physical source or apparatus bridges remain separate obligations. This is an unreleased authoring revision.

# Version 1 Revision Note

Supersedes
The unversioned manuscript *Canonical Coherent Kernels from MTT Fixed-Point Data*.

Reason
The earlier manuscript did not declare whether $`A`$ acted internally, on a spatial slice, or in Euclidean signature; it blurred harmonic projection with heat smoothing and promoted a sector kernel to a universal delta, CCR, source, and interaction replacement.

Resolution
This version types the operator domain, proves explicitly that $`AP=0`$ gives $`Pe^{-\tau A}P=P`$, separates $`Q`$-sector damping from the projected kernel, and adds locality, covariance, causal, gauge, and algebra-preservation gates to every physical use.

Retained result
Functional calculus uniquely determines the projected heat operator and displayed spectral error bounds from compatible realization data.

Remaining boundary
Current MTT fixed-point theory does not select one such triple for every physical sector or prove that replacing a standard distribution preserves the target theory’s causal and gauge structure.

# Purpose and claim discipline

The earlier delta–projection papers established statements of the form
``` math
K_\epsilon \longrightarrow \delta
```
or
``` math
\text{finite object} \longrightarrow \text{sharp standard object}.
```
Those statements explain why delta distributions recur across physics, but they do not yet select a physical finite kernel. The missing execution-level direction is
``` math
\text{MTT fixed-point data}
        \Longrightarrow
        K_{\mathrm{coh}}
        \Longrightarrow
        \text{finite correction}.
```

This paper proves that direction in the fixed-point regime.

> **Conditional construction.** After a realization has specified the operator domain and compatible data $`(A,P,\tau)`$, the projected heat operator is not chosen freely. Whether that operator represents a physical source, identity, or regulator is a separate theorem for the target sector.

## What is proved

We prove, in a standard compact spectral setting and in the corresponding Hilbert-space operator language, that fixed-point data $`(A,P,\tau)`$ determine a canonical bounded/smoothing operator
``` math
B_\tau:=P e^{-\tau A}P
```
and hence a kernel $`K_{\mathrm{MTT}}`$. We give explicit error estimates comparing $`B_\tau`$ with the full identity and with the coherent-sector identity.

## What is not claimed

We do not claim that all numerical values of $`\tau`$, spectral gaps, or carrier-induced operators have been computed, or that an internal stabilization operator automatically acts on external spacetime variables. Once a fixed-point sector supplies a typed $`(A,P,\tau)`$, the corresponding projected heat kernel is fixed within that realization. No statement about an unrelated delta distribution follows without an intertwiner identifying the two domains.

# Analytic setting

Let $`X`$ be a compact smooth Riemannian manifold without boundary, or a compact manifold with boundary equipped with a self-adjoint elliptic boundary condition. More generally, one may replace scalar functions by sections of a Hermitian vector bundle; for readability we use the scalar notation.

Let
``` math
A\ge 0
```
be a nonnegative self-adjoint Laplace-type operator on $`L^2(X)`$ with compact resolvent. Let
``` math
A\phi_n=\lambda_n\phi_n,\qquad
        0\le \lambda_0\le \lambda_1\le \cdots,
```
be an orthonormal spectral resolution, with eigenvalues repeated according to multiplicity.

<div id="ass:fpdata" class="assumption">

**Assumption 1** (Fixed-point spectral data). We are given:

1.  a bounded orthogonal projector $`P`$ on $`L^2(X)`$;

2.  $`Q:=I-P`$;

3.  commutation $`PA=AP`$ on $`\operatorname{Dom}(A)`$;

4.  an incoherent-sector gap
    ``` math
    A|_{\operatorname{Ran}Q}\ge \lambda^\ast Q
            \quad\text{for some}\quad \lambda^\ast>0;
    ```

5.  a proper-time/coherence scale $`\tau>0`$.

</div>

<div class="remark">

*Remark 2*. In the fixed-point papers $`P`$ is the coherent projector $`\Pi_{\mathrm{coh}}`$, often defined by Riesz spectral calculus on the fiber/internal operator. The gap $`\lambda^\ast`$ is the uniform positive spectral gap above the coherent modes. The operator $`A`$ is the linearized damping or elliptic operator controlling stabilization near the fixed-point sector.

</div>

<div id="rem:typing" class="remark">

*Remark 3* (Domain typing). The compact elliptic theorem is Riemannian. It may describe an internal fiber, a Euclidean problem, or an operator on a spatial Cauchy slice after those data are supplied. It is not by itself a Lorentzian spacetime heat kernel. Passing to a hyperbolic or retarded problem requires a separate domain, support, and wavefront-set analysis.

</div>

<div id="def:Btau" class="definition">

**Definition 4** (Canonical MTT coherent operator). Under <a href="#ass:fpdata" data-reference-type="ref+label" data-reference="ass:fpdata">1</a>, define
``` math
B_\tau:=P e^{-\tau A}P .
```
When $`B_\tau`$ has an integral kernel, we write
``` math
K_{\mathrm{MTT}}(x,y;\tau)
        :=
        \langle x|B_\tau|y\rangle .
```

</div>

Because $`P`$ commutes with $`A`$, the spectral form is transparent. If $`P\phi_n=p_n\phi_n`$ with $`p_n\in\{0,1\}`$, then
``` math
B_\tau f
        =
        \sum_{n}p_n e^{-\tau\lambda_n}\langle \phi_n,f\rangle\phi_n,
```
and the kernel is
``` math
K_{\mathrm{MTT}}(x,y;\tau)
        =
        \sum_{n:p_n=1}
        e^{-\tau\lambda_n}\phi_n(x)\phi_n^\ast(y).
```

# Existence, smoothness, and covariance of the canonical kernel

<div id="thm:smoothing" class="theorem">

**Theorem 5** (Kernel existence and smoothing). *Assume <a href="#ass:fpdata" data-reference-type="ref+label" data-reference="ass:fpdata">1</a>. For every $`\tau>0`$, $`e^{-\tau A}`$ is a smoothing trace-class operator. Consequently $`B_\tau=P e^{-\tau A}P`$ is bounded and trace class. If $`P`$ is a spectral projector of $`A`$, then $`B_\tau`$ has a smooth kernel
``` math
K_{\mathrm{MTT}}(\cdot,\cdot;\tau)\in C^\infty(X\times X).
```
If $`P`$ is finite rank, the same conclusion holds even at $`\tau=0`$, with $`B_0=P`$.*

</div>

<div class="proof">

*Proof.* Since $`A`$ is a nonnegative self-adjoint elliptic operator with compact resolvent, the spectral theorem gives
``` math
e^{-\tau A}f
        =
        \sum_n e^{-\tau\lambda_n}\langle \phi_n,f\rangle\phi_n.
```
For every $`N\ge 0`$,
``` math
A^N e^{-\tau A}
```
is bounded, because $`\lambda^N e^{-\tau\lambda}`$ is bounded on $`[0,\infty)`$. Elliptic regularity then implies that $`e^{-\tau A}`$ maps distributions to smooth functions. On a compact manifold, $`e^{-\tau A}`$ is trace class for $`\tau>0`$, and has a smooth heat kernel. Multiplication on both sides by the bounded spectral projector $`P`$, which commutes with $`A`$, preserves trace class and smoothness of the kernel. If $`P`$ is finite rank, $`P`$ is a finite sum of smooth eigenfunction projectors, hence has a smooth kernel at $`\tau=0`$. ◻

</div>

<div id="thm:covariance" class="theorem">

**Theorem 6** (Re-encoding covariance). *Let $`U:L^2(X)\to L^2(X')`$ be a unitary re-encoding. Define
``` math
A'=UAU^{-1},\qquad P'=UPU^{-1}.
```
Then the canonical coherent operator transforms as
``` math
B'_\tau=P'e^{-\tau A'}P'=UB_\tau U^{-1}.
```
Thus the construction of $`B_\tau`$ depends only on the fixed-point operator data up to unitary re-encoding.*

</div>

<div class="proof">

*Proof.* Functional calculus is covariant under unitary conjugation:
``` math
e^{-\tau A'}=e^{-\tau UAU^{-1}}=Ue^{-\tau A}U^{-1}.
```
Therefore
``` math
P'e^{-\tau A'}P'
        =
        (UPU^{-1})(Ue^{-\tau A}U^{-1})(UPU^{-1})
        =
        U(Pe^{-\tau A}P)U^{-1}.
```
 ◻

</div>

# Sector identity and error estimates

The canonical kernel should not be confused with the full Dirac identity kernel. It is an identity-like object on the retained coherent sector, with explicit error terms.

<div id="ass:band" class="assumption">

**Assumption 7** (Coherent bandwidth). For some $`\Lambda_{\mathrm{coh}}\ge 0`$,
``` math
\sigma(A|_{\operatorname{Ran}P})\subset[0,\Lambda_{\mathrm{coh}}].
```

</div>

<div class="remark">

*Remark 8*. If $`P`$ is the harmonic zero-mode projector, then $`\Lambda_{\mathrm{coh}}=0`$ and $`B_\tau=P`$ exactly. If $`P`$ retains a finite coherent band, then $`\Lambda_{\mathrm{coh}}`$ is the largest retained coherent eigenvalue.

</div>

<div id="prop:harmonic" class="proposition">

**Proposition 9** (Harmonic-projector degeneracy). *If $`AP=PA=0`$, then
``` math
Pe^{-\tau A}P=P
```
for every $`\tau\ge0`$. Thus the proper-time parameter produces no further smoothing inside the harmonic sector.*

</div>

<div class="proof">

*Proof.* Functional calculus gives $`e^{-\tau A}P=P`$ when $`AP=0`$, and left multiplication by $`P`$ leaves $`P`$ unchanged. ◻

</div>

<div id="thm:sector" class="theorem">

**Theorem 10** (Coherent-sector identity estimate). *Assume <a href="#ass:fpdata,ass:band" data-reference-type="ref+label" data-reference="ass:fpdata,ass:band">[ass:fpdata,ass:band]</a>. For every $`f\in L^2(X)`$,
``` math
\left\lVert Pf-B_\tau f \right\rVert_{L^2}
        \le
        \bigl(1-e^{-\tau\Lambda_{\mathrm{coh}}}\bigr)\left\lVert Pf \right\rVert_{L^2}.
```
Consequently,
``` math
\left\lVert f-B_\tau f \right\rVert_{L^2}
        \le
        \left\lVert Qf \right\rVert_{L^2}
        +
        \bigl(1-e^{-\tau\Lambda_{\mathrm{coh}}}\bigr)\left\lVert Pf \right\rVert_{L^2}.
```*

</div>

<div class="proof">

*Proof.* Since $`P`$ commutes with $`A`$, $`B_\tau f=e^{-\tau A}Pf`$. Thus
``` math
Pf-B_\tau f
        =
        (I-e^{-\tau A})Pf.
```
On $`\operatorname{Ran}P`$, the spectral values of $`A`$ lie in $`[0,\Lambda_{\mathrm{coh}}]`$. Hence
``` math
\left\lVert (I-e^{-\tau A})P \right\rVert_{L^2\to L^2}
        =
        \sup_{\lambda\in\sigma(A|_{\operatorname{Ran}P})}
        |1-e^{-\tau\lambda}|
        \le
        1-e^{-\tau\Lambda_{\mathrm{coh}}}.
```
This proves the first estimate. The second follows from
``` math
f-B_\tau f
        =
        Qf+(Pf-B_\tau f)
```
and the triangle inequality. ◻

</div>

<div id="cor:smalltau" class="corollary">

**Corollary 11** (Small-$`\tau`$ sector correction). *Under <a href="#ass:fpdata,ass:band" data-reference-type="ref+label" data-reference="ass:fpdata,ass:band">[ass:fpdata,ass:band]</a>,
``` math
\left\lVert Pf-B_\tau f \right\rVert_{L^2}
        \le
        \tau\Lambda_{\mathrm{coh}}\left\lVert Pf \right\rVert_{L^2}.
```*

</div>

<div class="proof">

*Proof.* Use $`1-e^{-x}\le x`$ for $`x\ge0`$. ◻

</div>

<div id="thm:gap" class="theorem">

**Theorem 12** (Incoherent damping estimate). *Assume <a href="#ass:fpdata" data-reference-type="ref+label" data-reference="ass:fpdata">1</a>. Then
``` math
\left\lVert e^{-\tau A}Q \right\rVert_{L^2\to L^2}
        \le
        e^{-\tau\lambda^\ast}.
```
More generally, for $`s\ge0`$,
``` math
\left\lVert A^{s/2}e^{-\tau A}Q \right\rVert_{L^2\to L^2}
        \le
        \sup_{\lambda\ge\lambda^\ast}\lambda^{s/2}e^{-\tau\lambda}.
```*

</div>

<div class="proof">

*Proof.* On $`\operatorname{Ran}Q`$, the spectral theorem and the gap assumption give $`\lambda\ge\lambda^\ast`$. Therefore
``` math
\left\lVert e^{-\tau A}Q \right\rVert
        =
        \sup_{\lambda\in\sigma(A|_{\operatorname{Ran}Q})}e^{-\tau\lambda}
        \le e^{-\tau\lambda^\ast}.
```
The higher estimate is identical after multiplying the spectral multiplier by $`\lambda^{s/2}`$. ◻

</div>

# Recovery of the Dirac delta

The canonical MTT kernel is finite. The Dirac delta is recovered only under an idealizing limit.

Let $`P_N:=\mathbf 1_{[0,\Lambda_N]}(A)`$ be an increasing family of spectral projectors with $`\Lambda_N\to\infty`$. Let
``` math
B_{N,\tau}:=P_Ne^{-\tau A}P_N.
```

<div id="thm:sharp" class="theorem">

**Theorem 13** (Joint sharp limit). *Fix the self-adjoint elliptic realization of $`A`$, including its boundary conditions. Suppose $`\Lambda_N\to\infty`$ and $`\tau_N\downarrow0`$. Then $`B_{N,\tau_N}f\to f`$ strongly in $`L^2(X)`$ for every $`f\in L^2(X)`$. For
``` math
D_\infty(A):=\bigcap_{m\geq0}\operatorname{Dom}(A^m),
```
convergence holds in every graph norm $`\|(I+A)^m\cdot\|_2`$, and hence in $`C^\infty`$ by elliptic estimates and Sobolev embedding. On a closed manifold $`D_\infty(A)=C^\infty(X)`$; with boundary this domain imposes compatibility at every order. Independently, the kernels converge to the identity distribution on the interior product (and on $`X\times X`$ when $`X`$ is closed). Distributional convergence is weaker than smooth convergence on inputs; these statements are not equivalent.*

</div>

<div class="proof">

*Proof.* In an eigenbasis the multiplier is $`b_N(\lambda)=\mathbf1_{[0,\Lambda_N]}(\lambda)e^{-\tau_N\lambda}`$. It lies in $`[0,1]`$ and tends to one at each fixed eigenvalue. Dominated convergence applied to
``` math
\sum_n(1+\lambda_n)^{2m}|1-b_N(\lambda_n)|^2|f_n|^2
```
proves the $`L^2`$ assertion for $`m=0`$ and all graph-norm assertions for $`f\in D_\infty(A)`$. The elliptic realization supplies the comparison with geometric Sobolev norms. For a smooth compactly supported test kernel, the associated smoothing operator is trace class. Uniform boundedness and strong convergence of $`B_{N,\tau_N}`$ imply convergence of its pairing with that trace-class operator, proving distributional kernel convergence. ◻

</div>

For example, the constant function on a Dirichlet interval is smooth but violates the boundary condition. Each finite spectral output vanishes at the endpoints, so it cannot converge uniformly there to that constant. The strong $`L^2`$ and interior distributional limits still hold. This is why specifying the realization changes the permitted convergence topology, not the underlying heat-kernel identity.

<div id="cor:meaning" class="corollary">

**Corollary 14** (Meaning of the delta limit). *The Dirac delta is not the fixed-point kernel itself. It is the joint idealization in which:*

1.  *coherent bandwidth becomes complete;*

2.  *proper-time width tends to zero;*

3.  *the incoherent complement is no longer discarded.*

*At finite bandwidth the declared model object is $`K_{\mathrm{MTT}}`$, not the full identity distribution. Calling it physically selected requires a source theorem for the particular realization.*

</div>

# Eligibility contract for downstream use

The mathematical construction gives an execution rule only after the target distribution has been identified with the same typed sector.

<div id="def:replacement" class="definition">

**Definition 15** (Eligible projected-kernel substitution). A downstream identity or source distribution is eligible for substitution only when: (i) it acts on the same Hilbert or bundle domain as $`A`$ and $`P`$; (ii) a selected intertwiner identifies the target variables with that domain; and (iii) the substitution preserves every required symmetry, constraint, support, and algebraic identity. Under those hypotheses the declared model may use
``` math
\delta(x-y)
        \quad\rightsquigarrow\quad
        K_{\mathrm{MTT}}(x,y;\tau)
        =
        \langle x|Pe^{-\tau A}P|y\rangle.
```

</div>

Within the heat/proper-time class this is not an arbitrary smoothing prescription. The eligibility hypotheses, however, are additional physical content and cannot be inferred from functional calculus alone.

<div id="thm:heatunique" class="theorem">

**Theorem 16** (Uniqueness within the heat/proper-time class). *Among positive self-adjoint contraction semigroups generated by the fixed-point operator $`A`$, the one-parameter family $`e^{-\tau A}`$ is uniquely determined by $`A`$. Therefore, once $`P`$ and $`\tau`$ are fixed, the operator $`B_\tau=Pe^{-\tau A}P`$ is unique.*

</div>

<div class="proof">

*Proof.* By the spectral theorem, a nonnegative self-adjoint operator $`A`$ determines a unique strongly continuous contraction semigroup $`T_\tau=e^{-\tau A}`$. Conversely, the generator of such a semigroup is unique by the Hille–Yosida theorem. Therefore the proper-time filter associated with the fixed-point generator is fixed. Multiplying on the left and right by the fixed coherent projector $`P`$ gives a unique $`B_\tau`$. ◻

</div>

<div class="remark">

*Remark 17*. The theorem does not say that no other regulator can be written down. It says that if the kernel is required to be the heat/proper-time filter generated by the same operator governing MTT stabilization, then the kernel is fixed by the fixed-point data.

</div>

# Finite corrections in standard structures

## Green functions

Let $`L`$ be a positive self-adjoint invertible operator commuting with $`A`$ and $`P`$. The ordinary point-source Green equation
``` math
LG=I
```
has kernel form
``` math
LG(x,y)=\delta(x-y).
```
The MTT coherent Green operator is
``` math
G_\tau^{\mathrm{MTT}}:=L^{-1}B_\tau.
```
It satisfies
``` math
LG_\tau^{\mathrm{MTT}}=B_\tau,
```
or in kernels,
``` math
L_xG_\tau^{\mathrm{MTT}}(x,y)=K_{\mathrm{MTT}}(x,y;\tau).
```

<div id="prop:green" class="proposition">

**Proposition 18** (Green-function correction). *Assume $`L^{-1}`$ is bounded on the Hilbert space under consideration. Then
``` math
\left\lVert L^{-1}-G_\tau^{\mathrm{MTT}} \right\rVert
        \le
        \left\lVert L^{-1} \right\rVert\,
        \left\lVert I-B_\tau \right\rVert.
```
On a coherent-band input $`f=Pf`$,
``` math
\left\lVert L^{-1}f-G_\tau^{\mathrm{MTT}}f \right\rVert
        \le
        \left\lVert L^{-1} \right\rVert\,
        \bigl(1-e^{-\tau\Lambda_{\mathrm{coh}}}\bigr)\left\lVert f \right\rVert.
```*

</div>

<div class="proof">

*Proof.* The first estimate follows from
``` math
L^{-1}-L^{-1}B_\tau=L^{-1}(I-B_\tau).
```
The second estimate uses <a href="#thm:sector" data-reference-type="ref+label" data-reference="thm:sector">10</a>. ◻

</div>

## Canonical commutators

The sharp canonical commutator
``` math
[\phi(x),\pi(y)]=i\hbar\delta(x-y)
```
belongs to the symplectic algebra of the field theory. Writing instead
``` math
[\phi_{\mathrm{coh}}(x),\pi_{\mathrm{coh}}(y)]
        =
        i\hbar K_{\mathrm{MTT}}(x,y;\tau).
```
defines a projected or modified symplectic algebra; it is not a consequence of the heat-kernel theorem. A physical use must prove nondegeneracy on the retained quotient, covariance, microcausality, and compatibility with the field equations. Without those checks the formula is only a candidate finite-sector model.

## Contact vertices

A local $`n`$-point contact vertex can be written schematically as
``` math
V_\delta^{(n)}(x_1,\ldots,x_n)
        =
        \int_X\prod_{j=1}^n \delta(x-x_j)\,\mathrm{d}x.
```
A finite-overlap candidate is
``` math
V_{\mathrm{MTT}}^{(n)}(x_1,\ldots,x_n;\tau)
        =
        \int_X\prod_{j=1}^n K_{\mathrm{MTT}}(x,x_j;\tau)\,\mathrm{d}x.
```
At nonzero width this is generally a nonlocal effective interaction. It requires a local parent mediator or an independent EFT, gauge/BRST, and causality analysis before it can replace a local vertex.

## Measurement effects

The distributional position effect
``` math
|x\rangle\langle x|
```
suggests a positive finite candidate effect with kernel
``` math
E_x^{\mathrm{MTT}}(y,z;\tau)
        =
        K_{\mathrm{MTT}}(y,x;\tau)K_{\mathrm{MTT}}^\ast(z,x;\tau).
```
To obtain a measurement model, these effects must form a normalized POVM and must be coupled to a declared apparatus instrument. The projected kernel alone does not supply either requirement.

## Noise kernels

If an independently selected temporal operator $`A_t`$ and memory scale $`\tau`$ are supplied, they define the candidate correlation kernel
``` math
C_{\mathrm{MTT}}(t,s)
        =
        \langle t|e^{-\tau A_t}|s\rangle
```
rather than an exact white-noise delta. In Markov limits this may approach
``` math
D\delta(t-s),
```
but neither $`A_t`$ nor its identification with the internal fixed-point operator follows from the elliptic theorem above.

# Worked example: circle with massive operator

Let $`X=S^1`$ with coordinate $`\theta\in[0,2\pi)`$, and take
``` math
A_m=-\partial_\theta^2+m^2,\qquad m>0.
```
The eigenfunctions are
``` math
\phi_n(\theta)=\frac{1}{\sqrt{2\pi}}e^{in\theta},
        \qquad
        \lambda_n=n^2+m^2.
```
Let
``` math
P_N=\sum_{|n|\le N}|\phi_n\rangle\langle\phi_n|.
```
Then
``` math
K_{N,\tau}^{\mathrm{MTT}}(\theta,\theta')
        =
        \frac{1}{2\pi}
        \sum_{|n|\le N}
        e^{-\tau(n^2+m^2)}e^{in(\theta-\theta')}.
```
For fixed $`N`$, this is a smooth finite kernel. For $`N\to\infty`$, it becomes the heat kernel of $`A_m`$:
``` math
K_{\infty,\tau}^{\mathrm{MTT}}(\theta,\theta')
        =
        e^{-\tau m^2}
        \frac{1}{2\pi}
        \sum_{n\in\mathbb{Z}}e^{-\tau n^2}e^{in(\theta-\theta')}.
```
As $`\tau\downarrow0`$, this tends distributionally to the periodic delta
``` math
\delta_{S^1}(\theta-\theta').
```

The finite correction to a coherent-band identity is explicit:
``` math
\left\lVert P_Nf-B_{N,\tau}f \right\rVert_{L^2}^2
        =
        \sum_{|n|\le N}
        \left(1-e^{-\tau(n^2+m^2)}\right)^2|f_n|^2.
```
Thus the correction is mode-resolved and directly computable from the fixed-point spectral data.

# Programmatic consequence

The previous delta papers established the forward structural dictionary:
``` math
\text{finite kernel}\longrightarrow \delta.
```
This paper supplies the fixed-point reverse direction:
``` math
(A,P,\tau,\lambda^\ast)
        \longrightarrow
        K_{\mathrm{MTT}}
        \longrightarrow
        \text{finite correction}.
```

> **Execution principle.** For an eligible same-domain occurrence, use the projected heat/proper-time kernel supplied by the declared realization and retain the target theory’s symmetry, support, and algebra checks as explicit obligations.

This makes the delta dictionary computational inside a declared sector. Point sources, commutators, contact interactions, measurement effects, and noise kernels are not thereby identified with one another; each requires its own admissible intertwiner and consistency theorem.

# Conclusion

The central mathematical question is whether declared fixed-point data determine a specific projected heat kernel. They do:
``` math
B_\tau=P e^{-\tau A}P
```
and hence
``` math
K_{\mathrm{MTT}}(x,y;\tau)
        =
        \langle x|Pe^{-\tau A}P|y\rangle.
```
This kernel is smooth in the compact elliptic setting, covariant under unitary equivalence, and identity-like on a retained finite band with explicit error bounds. In the harmonic case it reduces exactly to $`P`$. The separate semigroup $`e^{-\tau A}Q`$ is gap-damped. A family with complete bandwidth and vanishing proper time tends to the full identity distribution.

Thus the program is no longer merely:
``` math
\delta=\text{singular limit of some finite object}.
```
The rigorous conclusion is therefore:
``` math
\boxed{
        \text{typed fixed-point data determine a conditional sector kernel.}
        }
```
Promoting that kernel to a physical modification remains a realization-specific source and consistency problem.

<div class="thebibliography">

9

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980.

E. B. Davies, *Heat Kernels and Spectral Theory*, Cambridge University Press, 1989.

M. E. Taylor, *Partial Differential Equations II: Qualitative Studies of Linear Equations*, Springer, 2011.

E. Hille and R. S. Phillips, *Functional Analysis and Semi-Groups*, American Mathematical Society, 1957.

</div>
