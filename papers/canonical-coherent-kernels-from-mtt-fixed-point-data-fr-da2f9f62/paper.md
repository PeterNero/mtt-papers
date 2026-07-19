---
abstract: |
  Earlier papers in the delta–projection sequence established a structural dictionary: Dirac delta distributions arise as singular limits of finite kernels, shells, filters, windows, measurement effects, and thin layers. That dictionary is mathematically legitimate but does not by itself determine new physics, because an arbitrary finite kernel is only a regulator. The execution-level problem is the reverse direction: derive the finite kernel from MTT data.

  This paper proves the canonical fixed-point version of that reverse direction. In an admissible MTT fixed-point regime, the data consist of a nonnegative self-adjoint linearized operator $`A`$, a bounded coherent projector $`P=\Pi_{\mathrm{coh}}`$, a complementary incoherent projector $`Q=I-P`$, a spectral gap on the incoherent sector, and a proper-time/coherence scale $`\tau>0`$. These data canonically define the coherent kernel
  ``` math
  K_{\mathrm{MTT}}(x,y;\tau)
          =
          \langle x|\,P e^{-\tau A}P\,|y\rangle .
  ```
  Equivalently, in a spectral representation,
  ``` math
  K_{\mathrm{MTT}}(x,y;\tau)
          =
          \sum_{n\in{\rm coh}} e^{-\tau\lambda_n}
          \phi_n(x)\phi_n^\ast(y).
  ```
  We prove that this kernel is smooth for positive proper time, is functorial under unitary re-encoding, acts as a controlled sector-identity on the coherent sector, suppresses incoherent components by the fixed-point spectral gap, and converges to the usual Dirac delta only in the joint limit of complete coherent bandwidth and vanishing proper-time width.

  Thus the delta replacement is not arbitrary:
  ``` math
  \delta(x-y)
          \quad\leadsto\quad
          K_{\mathrm{MTT}}(x,y;\tau),
  ```
  with finite corrections controlled by $`(A,P,\tau,\lambda^\ast)`$. This converts the previous delta dictionary into an execution rule: MTT fixed-point data determine the finite kernel, and the finite kernel determines the deviation from the sharp standard object.
author:
- Peter Nero
current_version: unversioned
date: 2026-07-19
generated_from_main_tex_sha256: 6a2e297137a1f3f58ead9ac5a392d7fc71fe486f16a0773160b38c58b71b6494
paper_id: canonical-coherent-kernels-from-mtt-fixed-point-data-fr-da2f9f62
release_state: not_matched_to_zenodo
title: |
  **Canonical Coherent Kernels from MTT Fixed-Point Data**  
  From the Delta Dictionary to Execution-Level Corrections
---

*Part VI of VI in the Fixed Points series. As both the cornerstone of the Modal Triplet Theory (MTT) collection and a stand-alone development, the series is intended to function simultaneously as a basis and as a self-contained study. Each paper in the series builds upon its predecessors, extending the fixed-point framework step by step.*

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

> **Central claim.** In an admissible fixed-point regime, the finite replacement of the Dirac delta is not chosen freely. It is the projected heat/proper-time kernel determined by the same operator and projector data that define coherent stabilization.

## What is proved

We prove, in a standard compact spectral setting and in the corresponding Hilbert-space operator language, that fixed-point data $`(A,P,\tau)`$ determine a canonical bounded/smoothing operator
``` math
B_\tau:=P e^{-\tau A}P
```
and hence a kernel $`K_{\mathrm{MTT}}`$. We give explicit error estimates comparing $`B_\tau`$ with the full identity and with the coherent-sector identity.

## What is not claimed

We do not claim here that all numerical values of $`\tau`$, spectral gaps, or carrier-induced operators have been computed in every physical sector. The point is sharper: once a fixed-point sector supplies $`(A,P,\tau)`$, the finite kernel is fixed by functional calculus and is no longer arbitrary.

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

<div id="def:Btau" class="definition">

**Definition 3** (Canonical MTT coherent operator). Under <a href="#ass:fpdata" data-reference-type="ref+label" data-reference="ass:fpdata">1</a>, define
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

**Theorem 4** (Kernel existence and smoothing). *Assume <a href="#ass:fpdata" data-reference-type="ref+label" data-reference="ass:fpdata">1</a>. For every $`\tau>0`$, $`e^{-\tau A}`$ is a smoothing trace-class operator. Consequently $`B_\tau=P e^{-\tau A}P`$ is bounded and trace class. If $`P`$ is a spectral projector of $`A`$, then $`B_\tau`$ has a smooth kernel
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

**Theorem 5** (Re-encoding covariance). *Let $`U:L^2(X)\to L^2(X')`$ be a unitary re-encoding. Define
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

**Assumption 6** (Coherent bandwidth). For some $`\Lambda_{\mathrm{coh}}\ge 0`$,
``` math
\sigma(A|_{\operatorname{Ran}P})\subset[0,\Lambda_{\mathrm{coh}}].
```

</div>

<div class="remark">

*Remark 7*. If $`P`$ is the harmonic zero-mode projector, then $`\Lambda_{\mathrm{coh}}=0`$ and $`B_\tau=P`$ exactly. If $`P`$ retains a finite coherent band, then $`\Lambda_{\mathrm{coh}}`$ is the largest retained coherent eigenvalue.

</div>

<div id="thm:sector" class="theorem">

**Theorem 8** (Coherent-sector identity estimate). *Assume <a href="#ass:fpdata,ass:band" data-reference-type="ref+label" data-reference="ass:fpdata,ass:band">[ass:fpdata,ass:band]</a>. For every $`f\in L^2(X)`$,
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

**Corollary 9** (Small-$`\tau`$ sector correction). *Under <a href="#ass:fpdata,ass:band" data-reference-type="ref+label" data-reference="ass:fpdata,ass:band">[ass:fpdata,ass:band]</a>,
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

**Theorem 10** (Incoherent damping estimate). *Assume <a href="#ass:fpdata" data-reference-type="ref+label" data-reference="ass:fpdata">1</a>. Then
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

**Theorem 11** (Joint sharp limit). *Let $`f\in C^\infty(X)`$. Suppose $`\Lambda_N\to\infty`$ and $`\tau_N\downarrow0`$. Then
``` math
B_{N,\tau_N}f\to f
```
in $`C^\infty(X)`$. Equivalently, the kernels of $`B_{N,\tau_N}`$ converge to $`\delta(x-y)`$ in the distributional sense on $`X\times X`$.*

</div>

<div class="proof">

*Proof.* Write
``` math
f-B_{N,\tau_N}f
        =
        (I-P_N)f
        +
        P_N(I-e^{-\tau_N A})P_Nf.
```
The first term tends to zero in all Sobolev norms because spectral projectors converge strongly to the identity on smooth functions, and smooth spectral coefficients decay rapidly. For the second term, fix a Sobolev index $`s`$. Choose $`M>s`$. Since $`f\in C^\infty`$,
``` math
\sum_n (1+\lambda_n)^M |\langle \phi_n,f\rangle|^2<\infty.
```
For each fixed $`n`$, $`1-e^{-\tau_N\lambda_n}\to0`$. The summand is dominated by a multiple of $`(1+\lambda_n)^M|\langle\phi_n,f\rangle|^2`$ for $`N`$ large enough and $`M`$ chosen above $`s`$. Dominated convergence gives convergence to zero in $`H^s`$. Since $`s`$ is arbitrary, Sobolev embedding gives convergence in $`C^\infty`$. The distributional kernel statement is the usual kernel form of convergence to the identity. ◻

</div>

<div id="cor:meaning" class="corollary">

**Corollary 12** (Meaning of the delta limit). *The Dirac delta is not the fixed-point kernel itself. It is the joint idealization in which:*

1.  *coherent bandwidth becomes complete;*

2.  *proper-time width tends to zero;*

3.  *the incoherent complement is no longer discarded.*

*In finite-capacity MTT, the physically selected object is $`K_{\mathrm{MTT}}`$, not $`\delta`$.*

</div>

# Execution rule for downstream delta replacements

We can now state the execution rule.

<div id="def:replacement" class="definition">

**Definition 13** (MTT delta replacement). In a fixed-point regime with data $`(A,P,\tau)`$, every downstream occurrence of an identity/source/constraint delta that belongs to the same coherent chart is replaced by the canonical kernel
``` math
\delta(x-y)
        \quad\rightsquigarrow\quad
        K_{\mathrm{MTT}}(x,y;\tau)
        =
        \langle x|Pe^{-\tau A}P|y\rangle.
```

</div>

This is not an arbitrary smoothing prescription. It is determined by the fixed-point data.

<div id="thm:heatunique" class="theorem">

**Theorem 14** (Uniqueness within the heat/proper-time class). *Among positive self-adjoint contraction semigroups generated by the fixed-point operator $`A`$, the one-parameter family $`e^{-\tau A}`$ is uniquely determined by $`A`$. Therefore, once $`P`$ and $`\tau`$ are fixed, the operator $`B_\tau=Pe^{-\tau A}P`$ is unique.*

</div>

<div class="proof">

*Proof.* By the spectral theorem, a nonnegative self-adjoint operator $`A`$ determines a unique strongly continuous contraction semigroup $`T_\tau=e^{-\tau A}`$. Conversely, the generator of such a semigroup is unique by the Hille–Yosida theorem. Therefore the proper-time filter associated with the fixed-point generator is fixed. Multiplying on the left and right by the fixed coherent projector $`P`$ gives a unique $`B_\tau`$. ◻

</div>

<div class="remark">

*Remark 15*. The theorem does not say that no other regulator can be written down. It says that if the kernel is required to be the heat/proper-time filter generated by the same operator governing MTT stabilization, then the kernel is fixed by the fixed-point data.

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

**Proposition 16** (Green-function correction). *Assume $`L^{-1}`$ is bounded on the Hilbert space under consideration. Then
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
The second estimate uses <a href="#thm:sector" data-reference-type="ref+label" data-reference="thm:sector">8</a>. ◻

</div>

## Canonical commutators

The sharp canonical commutator
``` math
[\phi(x),\pi(y)]=i\hbar\delta(x-y)
```
is replaced inside the coherent chart by
``` math
[\phi_{\mathrm{coh}}(x),\pi_{\mathrm{coh}}(y)]
        =
        i\hbar K_{\mathrm{MTT}}(x,y;\tau).
```
The correction is controlled by the same sector error estimates. This is not loss of locality as arbitrary nonlocality; it is finite coherent-sector locality determined by $`A,P,\tau`$.

## Contact vertices

A local $`n`$-point contact vertex can be written schematically as
``` math
V_\delta^{(n)}(x_1,\ldots,x_n)
        =
        \int_X\prod_{j=1}^n \delta(x-x_j)\,\mathrm{d}x.
```
The fixed-point replacement is
``` math
V_{\mathrm{MTT}}^{(n)}(x_1,\ldots,x_n;\tau)
        =
        \int_X\prod_{j=1}^n K_{\mathrm{MTT}}(x,x_j;\tau)\,\mathrm{d}x.
```
Thus the contact interaction is not softened by an arbitrary profile; it is softened by the coherent kernel selected by the same fixed-point data.

## Measurement effects

The distributional position effect
``` math
|x\rangle\langle x|
```
is replaced by a finite coherent effect with kernel
``` math
E_x^{\mathrm{MTT}}(y,z;\tau)
        =
        K_{\mathrm{MTT}}(y,x;\tau)K_{\mathrm{MTT}}^\ast(z,x;\tau).
```
The width of the measurement effect is therefore controlled by the proper-time/coherence scale and spectral structure of the fixed-point sector.

## Noise kernels

A temporal fixed-point operator $`A_t`$ with memory scale $`\tau`$ selects the correlation kernel
``` math
C_{\mathrm{MTT}}(t,s)
        =
        \langle t|e^{-\tau A_t}|s\rangle
```
rather than an exact white-noise delta. In Markov limits this may approach
``` math
D\delta(t-s),
```
but the finite-memory kernel is the execution-level object.

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

> **Execution principle.** In any admissible fixed-point chart, replace delta distributions not by arbitrary mollifiers, but by the projected heat/proper-time kernel selected by the fixed-point operator and coherent projector.

This is the point at which the delta dictionary becomes predictive in principle. Once a sector supplies numerical or geometric data for $`A`$, $`P`$, $`\tau`$, and $`\lambda^\ast`$, the corrections to point sources, commutators, contact interactions, measurement effects, and noise kernels are fixed.

# Conclusion

The central problem after the delta–projection dictionary was not whether finite kernels can converge to Dirac deltas. They can. The execution problem was whether MTT selects a specific finite kernel.

In the fixed-point regime, the answer is yes. The fixed-point data determine
``` math
B_\tau=P e^{-\tau A}P
```
and hence
``` math
K_{\mathrm{MTT}}(x,y;\tau)
        =
        \langle x|Pe^{-\tau A}P|y\rangle.
```
This kernel is smooth for positive proper time, covariant under admissible re-encoding, identity-like on the coherent sector with explicit error bounds, suppresses incoherent modes by the spectral gap, and tends to the Dirac delta only under the idealizing limit of complete bandwidth and vanishing proper-time width.

Thus the program is no longer merely:
``` math
\delta=\text{singular limit of some finite object}.
```
It becomes:
``` math
\boxed{
        \text{MTT fixed-point data select the finite object.}
        }
```

<div class="thebibliography">

9

T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995.

M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980.

E. B. Davies, *Heat Kernels and Spectral Theory*, Cambridge University Press, 1989.

M. E. Taylor, *Partial Differential Equations II: Qualitative Studies of Linear Equations*, Springer, 2011.

E. Hille and R. S. Phillips, *Functional Analysis and Semi-Groups*, American Mathematical Society, 1957.

</div>
