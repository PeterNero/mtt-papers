---
abstract: |
  We present a rigorous selection principle for heterotic flux compactifications in the torsional $`\mathrm{SU}(3)`$ slice. In a left-invariant ansatz, the coherent-sector contraction condition (FCC) of a general fixed-point framework is shown to be equivalent to the standard anomaly/primitivity/quantization system evaluated componentwise on invariant $`(2,2)`$ bases. Consequently, FCC selects discrete loci on explicit compact examples: the complex balanced Iwasawa threefold (fixing $`r_3`$) and a balanced non-integrable $`\text{Lens}\times\text{Nil}`$ background (fixing $`R_1/R`$). We provide coefficient-level decompositions of $`dH`$, $`\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}`$, and $`\mathrm{Tr}F^{2}`$ in invariant frames, and record a normalized cubic Yukawa on Iwasawa. These results clarify how a rigorous selection mechanism organizes heterotic flux vacua without new dynamics beyond the torsional $`\mathrm{SU}(3)`$ system with $`R_{+}`$.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: September 7 2025
generated_from_main_tex_sha256: a54e4edb0e641c37a1b7940ecfc76031ff4485160919a9e80da390e7988bf8ab
paper_id: modal-triplet-theory-mtt-as-a-selection-principle-for-h-56b22927
release_state: zenodo_released
released_version: v1.0
title: |
  **Modal Triplet Theory: MTT as a Selection Principle for Heterotic Flux Compactifications  
  Equivalence in the Left-Invariant Slice and Two Explicit Case Studies**
zenodo_doi: 10.5281/zenodo.17072927
zenodo_record_id: 17072927
zenodo_url: "https://zenodo.org/records/17072927"
---

# Introduction

#### Motivation.

Classifying and selecting physically meaningful heterotic vacua with nonzero $`H`$ remains a central problem. We show that, in the left-invariant torsional $`\mathrm{SU}(3)`$ slice, a rigorous fixed-point/contraction criterion (FCC) *reduces to and equals* the usual anomaly/primitivity/quantization constraints solved componentwise on invariant $`(2,2)`$ forms.

#### Contributions (summary).

\(i\) *Equivalence theorem:* projection $`\equiv`$ compactification in the invariant slice and FCC $`\equiv`$ componentwise anomaly system (<a href="#prop:proj,def:FCC,thm:FCC" data-reference-type="ref+Label" data-reference="prop:proj,def:FCC,thm:FCC">[prop:proj,def:FCC,thm:FCC]</a>). (ii) *Discrete loci:* Iwasawa fixes $`r_3`$; $`\text{Lens}\times\text{Nil}`$ fixes $`R_1/R`$ (<a href="#cor:discrete" data-reference-type="ref+Label" data-reference="cor:discrete">4</a>). (iii) *Coefficient catalogues & reproducibility:* invariant-frame decompositions of $`dH`$, $`\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}`$, $`\mathrm{Tr}F^{2}`$ (App. <a href="#app:coeffs" data-reference-type="ref" data-reference="app:coeffs">10</a>). (iv) *Minimal EFT read-off:* normalized $`E_6`$ cubic on Iwasawa ($`\lambda_{123}=1`$).

#### Positioning.

We do not claim a new class of solutions; rather, we supply a *selection mechanism* compatible with the Strominger system, grounded in explicit, coefficient-level case studies.[^1]

# Background

#### Torsional $`\bm{\mathrm{SU}(3)}`$ slice (Strominger system).

Balanced metric $`d(J^{2})=0`$ at constant dilaton; $`H=\mathrm{i}(\bar\partial-\partial)J`$; $`R_{+}`$ the Bismut connection; Hermitian Yang–Mills on the gauge bundle; and the Bianchi identity
``` math
\begin{equation}
\label{eq:bianchi}
dH=\frac{\alpha'}{4}\big(\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}-\mathrm{Tr}F^2\big).
\end{equation}
```

#### Left-invariant truncation.

On nil/solvmanifolds (Iwasawa; $`\text{Lens}\times\text{Nil}`$) the Nomizu complex yields a finite invariant basis: all four-forms in <a href="#eq:bianchi" data-reference-type="eqref" data-reference="eq:bianchi">[eq:bianchi]</a> lie in the invariant $`(2,2)`$ subspace. Coefficient-level solutions are then obtained by expanding $`dH`$, $`\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}`$, and $`\mathrm{Tr}F^{2}`$ on the invariant basis.

#### Fixed-point framework (minimal).

We use only the following standard ingredients from a fixed-point/coherent-sector framework: a bounded coherent projector $`\Pi_{\rm coh}`$ onto fiber-harmonic modes; an FCC margin $`q=C_\Pi e^{-(\eta-L)\tau}<1`$ ensuring contraction of the time–$`\tau`$ map; and Ornstein–Uhlenbeck (OU) damping $`\mathrm{Var}=\delta/(2\gamma)`$ modewise for unresolved fluctuations, with $`\gamma=\kappa\lambda-L-\Delta_{\rm curv}`$ capturing curvature remainders. See .

# Equivalence and FCC in the invariant slice

<div id="prop:proj" class="proposition">

**Proposition 1** (Projection $`\equiv`$ compactification). *Let $`\Sigma_9 \xrightarrow{\ \pi_{\mathrm{sp}}\ } M_3`$ be a Riemannian submersion with compact fibers $`F_6 \simeq X_6`$ and Ehresmann connection $`\mathcal{H}`$. In the left-invariant ansatz (Nomizu complex on $`X_6`$), fiber integration of the 10D heterotic action equals KK compactification on $`X_6`$; the KK gauge fields arise from $`\mathcal{H}`$.*

</div>

<div id="def:FCC" class="definition">

**Definition 2** (FCC in the torsional $`\mathrm{SU}(3)`$ slice). *In the invariant sector,
``` math
\begin{equation}
\label{eq:FCC}
d(J^{2})=0, \qquad J\lrcorner F=0, \qquad \text{flux quantization}, \qquad
dH=\frac{\alpha'}{4}\big(\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}-\mathrm{Tr}F^{2}\big),
\end{equation}
```
evaluated componentwise on an invariant $`(2,2)`$ basis.*

</div>

<div id="thm:FCC" class="theorem">

**Theorem 3** (FCC $`\Leftrightarrow`$ componentwise anomaly system). *For left-invariant backgrounds on $`X_6`$, the FCC reduces to a finite linear system $`u_i - v_i = -(4/\alpha')\,w_i`$ on an invariant $`(2,2)`$ basis, with $`(u_i),(v_i),(w_i)`$ the coefficients of $`\mathrm{Tr}F^{2}`$, $`\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}`$, and $`dH`$ respectively. Solutions are precisely the componentwise Bianchi solutions obtained by invariant expansion.*

</div>

<div id="cor:discrete" class="corollary">

**Corollary 4** (Discrete invariant loci). *On Iwasawa, with the abelian flux choice below, $`u_2=u_3=v_2=v_3=0`$ and the single nontrivial component fixes $`r_3`$ for fixed integers. On $`\text{Lens}\times\text{Nil}`$, the two independent components fix $`R_1/R`$ for integer $`(f,h)`$; no invariant moduli remain in the invariant sector.*

</div>

# Case I: Iwasawa (complex, balanced)

#### Invariant structure and normalization.

Let $`(\omega_1,\omega_2,\omega_3)`$ be a left-invariant $`(1,0)`$-frame on $`H_3(\mathbb{C})`$ with $`d\omega_1=d\omega_2=0`$, $`d\omega_3=\omega_1\wedge\omega_2`$. Set
``` math
J=\frac{\mathrm{i}}{2}\sum_{j=1}^3 r_j^2\,\omega_j\wedge\bar\omega_j,\qquad
\Omega=\omega_1\wedge\omega_2\wedge\omega_3,
```
and define
``` math
a:=\frac{\mathrm{i}}{2}\,\omega_1\wedge\bar\omega_1,\quad
b:=\frac{\mathrm{i}}{2}\,\omega_2\wedge\bar\omega_2,\quad
c:=\frac{\mathrm{i}}{2}\,\omega_3\wedge\bar\omega_3,
```
``` math
\alpha_1:=a\wedge b,\quad \alpha_2:=a\wedge c,\quad \alpha_3:=b\wedge c,\qquad
\int_X a\wedge b\wedge c=1.
```
Then $`H=\mathrm{i}(\bar\partial-\partial)J`$ and
``` math
\begin{equation}
\label{eq:iwa-dH}
dH=-4\,r_3^2\,\alpha_1,\qquad\text{(no components on $\alpha_{2,3}$).}
\end{equation}
```

#### Torsional spin curvature (gravitational trace).

In a real orthonormal invariant frame adapted to the above choice,
``` math
\begin{equation}
\label{eq:iwa-Rplus}
\mathrm{Tr}_{\mathrm{grav}}\,R_{+}^{2}=\tilde v_1(R,r_3)\,\alpha_1,\qquad
\tilde v_1(R,r_3)=8\,\frac{r_3^2}{r_1^2 r_2^2},
\end{equation}
```
with no support on $`\alpha_{2,3}`$.

#### Abelian flux and primitivity.

Embed an abelian line in the commutant of $`\mathrm{SU}(3)\subset E_8`$ with
``` math
F^{(1)}=2\pi\,T\,(n_1 a+n_2 b+n_3 c),\qquad \mathrm{Tr}(T^2)=1,\ n_i\in\mathbb{Z},
```
so that
``` math
\begin{equation}
\label{eq:iwa-flux}
\mathrm{Tr}\!\big(F^{(1)}\!\wedge F^{(1)}\big)=2(2\pi)^2\big(n_1 n_2\,\alpha_1+n_1 n_3\,\alpha_2+n_2 n_3\,\alpha_3\big).
\end{equation}
```
Primitivity $`J\lrcorner F^{(1)}=0`$ is equivalent to
``` math
n_1\,\frac{r_2^2}{r_3^2}+n_2\,\frac{r_1^2}{r_3^2}+n_3\,\frac{r_1^2}{r_2^2}=0.
```
A convenient choice that enforces $`u_2=u_3=0`$ is two-line embedding with $`(n^{(1)}_1,n^{(1)}_2,n^{(1)}_3)=(1,2,0)`$ and $`(n^{(2)}_1,n^{(2)}_2,n^{(2)}_3)=(-1,-2,0)`$, giving $`u_1=8(2\pi)^2`$, $`u_2=u_3=0`$.

#### Componentwise Bianchi/anomaly system and solution.

Expanding $`\mathrm{Tr}F^{2}=\sum_i u_i\alpha_i`$, $`\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}=\sum_i v_i\alpha_i`$, $`dH=\sum_i w_i\alpha_i`$ with $`w_1=-4 r_3^2`$, $`w_{2,3}=0`$, the Bianchi identity <a href="#eq:bianchi" data-reference-type="eqref" data-reference="eq:bianchi">[eq:bianchi]</a> becomes, componentwise,
``` math
\begin{equation}
\label{eq:iwa-comp}
u_2=v_2,\qquad u_3=v_3,\qquad u_1-v_1=\frac{16}{\alpha'}\,r_3^2.
\end{equation}
```
If the non-abelian $`\mathrm{Tr}F(E)^2`$ vanishes in the invariant sector (as in the HYM choice we use), then $`v_{2,3}=0`$ and $`v_1=\tilde v_1`$. With $`r_1=r_2=:R`$ this yields
``` math
\begin{equation}
\label{eq:iwa-r3}
8(2\pi)^2-\frac{8\,r_3^2}{R^4}=\frac{16}{\alpha'}\,r_3^2
\quad\Longrightarrow\quad
r_3^2=\frac{8(2\pi)^2}{\,16/\alpha'+8/R^4\,}.
\end{equation}
```

#### Normalized cubic Yukawa.

On complex-parallelizable Iwasawa, any harmonic $`(0,3)`$-form is proportional to $`\bar\Omega`$; with $`\int_X\Omega\wedge\bar\Omega=1`$ and the $`E_6`$ cubic normalized ($`d_{abc}`$ basis), the trilinear coupling
``` math
\lambda_{123}=\int_X \Omega\wedge \mathrm{Tr}(\Psi_1\wedge\Psi_2\wedge\Psi_3)
```
is a pure phase removable by a chiral rephasing, hence $`\lambda_{123}=1`$ at tree level.

# Case II: $`\text{Lens}\times\text{Nil}`$ (balanced, non-integrable)

#### Invariant structure.

Take $`X_6=L(3,1)\times(\Gamma\backslash \mathrm{Nil}_3)`$ with left-invariant coframes $`\{\eta_1,\eta_2,\eta_3\}`$ on $`L(3,1)`$ and $`\{\sigma_4,\sigma_5,\sigma_6\}`$ on $`\mathrm{Nil}_3`$:
``` math
d\eta_i=\tfrac{1}{2}\,\epsilon_{ijk}\,\eta_j\wedge\eta_k,\qquad
d\sigma_4=d\sigma_5=0,\qquad d\sigma_6=\sigma_4\wedge\sigma_5.
```
Define
``` math
J=R_1^2\,\eta_1\wedge\eta_2+R_2^2\,\eta_3\wedge\sigma_6+R_3^2\,\sigma_4\wedge\sigma_5,\qquad
\Omega=(\eta_1+\mathrm{i}\eta_2)\wedge(\eta_3+\mathrm{i}\sigma_4)\wedge(\sigma_6+\mathrm{i}\sigma_5).
```
Then $`d(J^{2})=0`$ iff $`R_2=R_3=:R`$ (balanced), while $`d\Omega\neq 0`$ (non-integrable).

#### Invariant $`(2,2)`$ basis and coefficients.

Let
``` math
\beta_1:=\eta_{12}\wedge\eta_3\wedge\sigma_6,\qquad
\beta_3:=\eta_3\wedge\sigma_{45}\wedge\sigma_6,
```
and set the scale one-forms via $`d\eta_i=\lambda\,\epsilon_{ijk}\eta_j\wedge\eta_k`$ and $`d\sigma_6=\nu\,\sigma_4\wedge\sigma_5`$, with $`\lambda\sim R_1^{-1}`$, $`\nu\sim R^{-1}`$. A left-invariant computation gives
``` math
\begin{equation}
\label{eq:lens-dH}
dH=W_1(R_1,R)\,\beta_1+W_3(R_1,R)\,\beta_3,\quad
W_1=2\lambda^2 R^2,\quad W_3=\lambda\nu\,R^2,
\end{equation}
```
and (with the gravitational trace)
``` math
\begin{equation}
\label{eq:lens-Rplus}
\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}=A(R_1,R)\,\beta_1+B(R_1,R)\,\beta_3,\quad
A=4\lambda^2+O(\lambda^2\nu^2),\quad B=4\nu^2+O(\lambda^2\nu^2).
\end{equation}
```

#### Abelian flux and anomaly equations (discrete ratio).

For an abelian embedding with integers $`(f,h)\in\mathbb{Z}^2`$,
``` math
\mathrm{Tr}F^2=2(2\pi)^2\big(f^2\,\beta_1+h^2\,\beta_3\big),
```
and the two independent Bianchi components read
``` math
\begin{equation}
\label{eq:lens-anom}
2(2\pi)^2 f^2 - A(R_1,R)= -\,\frac{4}{\alpha'}\,W_1(R_1,R),\qquad
2(2\pi)^2 h^2 - B(R_1,R)= -\,\frac{4}{\alpha'}\,W_3(R_1,R).
\end{equation}
```
These two scalar equations fix the ratio $`R_1/R`$ for any fixed $`(f,h)\neq (0,0)`$, leaving no invariant moduli in the left-invariant sector.

# Stability and control

<div id="prop:OU" class="proposition">

**Proposition 5** (OU mode control). *If each non-harmonic mode obeys $`da=-\gamma\,a\,dt+\sqrt{\delta}\,dW_t`$ with $`\gamma=\kappa\,\lambda-L-\Delta_{\mathrm{curv}}>0`$, then $`\mathrm{Var}(a)=\delta/(2\gamma)`$, and bundlewise stability holds iff $`\sum (1+\lambda)\,\delta/(2\gamma) < \infty`$.*

</div>

(Statements by citation to the FP series; see App. <a href="#app:lemmas" data-reference-type="ref" data-reference="app:lemmas">11</a>.)

# Minimal EFT extraction

#### Gauge kinetic function.

At tree level in the heterotic string the four-dimensional gauge kinetic function is $`f=S`$ (the complex dilaton), so $`g^{-2}=\mathrm{Re}\,S`$ up to threshold corrections. Our backgrounds preserve this standard relation in the left-invariant truncation; torsional effects enter through higher-order $`\alpha'`$ and one-loop thresholds, which we do not attempt to compute here.

#### Iwasawa cubic Yukawa.

On complex-parallelizable Iwasawa, with $`\int_X \Omega\wedge\bar\Omega=1`$ and the $`E_6`$ cubic normalized ($`d_{abc}`$), the trilinear coupling
``` math
\lambda_{123}=\int_X \Omega\wedge \mathrm{Tr}(\Psi_1\wedge\Psi_2\wedge\Psi_3)
```
is a pure phase that can be removed by a chiral rephasing; thus $`\lambda_{123}=1`$ at tree level. This provides a convenient normalized starting point for hierarchical textures once small corrections (e.g. worldsheet instantons or flux-induced mixings) are included.

# Related work

Work on torsional heterotic compactifications includes the original Strominger/Hull system with $`R_+`$, non-Kähler solutions on torus bundles and the Fu–Yau class, and many nil/solvmanifold $`\mathrm{SU}(3)`$-structures . Our contribution is orthogonal: we do not enlarge the solution class but rather give a rigorous *selection* mechanism that reduces, in the left-invariant slice, to the familiar anomaly/primitivity/quantization system, and we exhibit two compact, fully worked examples with coefficient-level control and discrete parameter loci.

# Conclusions

We established that, in the left-invariant torsional $`\mathrm{SU}(3)`$ slice, the coherent-sector contraction condition (FCC) coincides with the standard anomaly/primitivity/quantization system when evaluated componentwise on invariant $`(2,2)`$ bases. As a result, selection picks discrete parameter loci on two explicit compact examples: Iwasawa (fixing $`r_3`$) and $`\text{Lens}\times\text{Nil}`$ (fixing $`R_1/R`$). The coefficient catalogues and normalized Iwasawa Yukawa provide reproducible anchors for further work. Natural extensions include non-abelian visible flux breaking, higher $`\alpha'`$ corrections, other nil/solv examples, and worldsheet checks.

# Coefficient catalogues

## A.1 Iwasawa coefficients (invariant frame)

``` math
\begin{align*}
& a=\frac{\mathrm{i}}{2}\,\omega_1\wedge\bar\omega_1,\quad
  b=\frac{\mathrm{i}}{2}\,\omega_2\wedge\bar\omega_2,\quad
  c=\frac{\mathrm{i}}{2}\,\omega_3\wedge\bar\omega_3,\\
& \alpha_1=a\wedge b,\ \alpha_2=a\wedge c,\ \alpha_3=b\wedge c,\qquad
  \int_X a\wedge b\wedge c=1,\\[2pt]
& dH=-4\,r_3^2\,\alpha_1,\qquad
  \mathrm{Tr}_{\mathrm{grav}}R_{+}^2=\tilde v_1\,\alpha_1,\quad
  \tilde v_1=8\,\frac{r_3^2}{r_1^2 r_2^2},\\[2pt]
& \mathrm{Tr}\!\big(F^{(1)}\!\wedge F^{(1)}\big)=2(2\pi)^2\big(n_1 n_2\,\alpha_1+n_1 n_3\,\alpha_2+n_2 n_3\,\alpha_3\big),\\[2pt]
& \text{Bianchi (components):}\quad
  u_2=v_2,\ u_3=v_3,\ u_1-v_1=\frac{16}{\alpha'}\,r_3^2.
\end{align*}
```

## A.2 $`\text{Lens}\times\text{Nil}`$ coefficients (balanced, non-integrable)

Let $`R_2=R_3=:R`$, and define the scale parameters by $`d\eta_i=\lambda\,\epsilon_{ijk}\eta_j\wedge\eta_k`$, $`d\sigma_6=\nu\,\sigma_4\wedge\sigma_5`$. With
``` math
\beta_1:=\eta_{12}\wedge\eta_3\wedge\sigma_6,\qquad
\beta_3:=\eta_3\wedge\sigma_{45}\wedge\sigma_6,
```
one has
``` math
\begin{align*}
& dH=W_1(R_1,R)\,\beta_1+W_3(R_1,R)\,\beta_3,\qquad
  W_1=2\lambda^2 R^2,\quad W_3=\lambda\nu R^2,\\[2pt]
& \mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}=A(R_1,R)\,\beta_1+B(R_1,R)\,\beta_3,\qquad
  A=4\lambda^2+O(\lambda^2\nu^2),\ \ B=4\nu^2+O(\lambda^2\nu^2),\\[2pt]
& \mathrm{Tr}F^2=2(2\pi)^2\big(f^2\beta_1+h^2\beta_3\big),\\[2pt]
& \text{Bianchi (components):}\quad
  2(2\pi)^2 f^2 - A= -\,\frac{4}{\alpha'}\,W_1,\qquad
  2(2\pi)^2 h^2 - B= -\,\frac{4}{\alpha'}\,W_3.
\end{align*}
```

# OU and curvature lemmas (statements)

#### OU variance and summability.

For a mode obeying $`da=-\gamma a\,dt+\sqrt{\delta}\,dW_t`$ with $`\gamma>0`$, the stationary variance is $`\mathrm{Var}(a)=\delta/(2\gamma)`$. Bundlewise stability is equivalent to positivity of all $`\gamma`$ and the summability condition $`\sum (1+\lambda)\,\delta/(2\gamma)<\infty`$.

#### Curvature remainder.

In a bounded-geometry regime the effective damping gains a representation-correct Bochner contribution, so that $`\gamma=\kappa\,\lambda-L-\Delta_{\mathrm{curv}}`$, where $`\Delta_{\mathrm{curv}}`$ depends on curvature bounds of the base/fiber and the representation (e.g. spinors vs. forms). In particular, for large radii the curvature remainder is small and the invariant sector remains dynamically closed provided $`\gamma>0`$ modewise.

(Proofs by citation to the FP series listed in the References.)

# Worldsheet $`\sigma`$–model check

#### Aim.

To record a succinct, self-contained worldsheet verification that the fixed-point background $`(G,B,\Phi;A)`$ in the heterotic flux slice is conformal at leading order in $`\alpha'`$, i.e. $`\beta=0`$, with the torsional choice $`R_+`$ for the tangent-bundle connection.

## Setup and conventions

We use the heterotic Polyakov action in conformal gauge with target data $`(G,B,\Phi;A)`$ and left-moving fermions coupled to $`A`$; see . We adopt the supersymmetric torsional connection $`R_+`$ on $`TX`$, so that curvature terms in the beta-functions are built from $`R_+`$ .

## One-loop $`\beta`$–functions (bosonic sector)

To leading order in $`\alpha'`$ and suppressing scheme-dependent local redefinitions,
``` math
\begin{align}
\beta^{(G)}_{MN} &= R_{MN}(G) - \tfrac14 H_{MPQ}H_N{}^{PQ} + 2\nabla_M\nabla_N\Phi \,+\, O(\alpha'),\\
\beta^{(B)}_{MN} &= -\tfrac12 \nabla^P H_{PMN} + \nabla^P\Phi\, H_{PMN} \,+\, O(\alpha'),\\
\beta^{(\Phi)}   &= \tfrac{D-26}{6} - \tfrac12 \nabla^2\Phi + (\nabla\Phi)^2 - \tfrac1{24}H^2 \,+\, O(\alpha'),
\end{align}
```
with $`D=10`$ and $`H`$ the gauge-invariant Green–Schwarz 3-form. The heterotic gauge beta-function vanishes for a Hermitian–Yang–Mills (HYM) bundle on a Gauduchon metric. Standard derivations: .

## Equivalence to target-space equations at the fixed point

At the MTT coherent fixed point we impose: (i) conformally balanced $`d(e^{-2\Phi}J\wedge J)=0`$, (ii) complex integrability ($`W_1=W_2=0`$), and (iii) $`H_b=dB-\tfrac{\alpha'}4(\omega_3(A)-\omega_3(\omega_+))`$ with $`R_+`$. Using the dictionary in §3 and §5, the conditions $`\beta^{(G)}=\beta^{(B)}=0`$ are equivalent to the Hull–Strominger equations (conformally balanced metric and $`H=i(\bar\partial-\partial)J`$ up to the Green–Schwarz correction), while $`\beta^{(\Phi)}=0`$ is automatic for $`D=10`$ up to a constant shift absorbed by $`e^{-2\Phi}`$ normalization .

## Gauge sector and HYM

On a Gauduchon metric the HYM equations are the vanishing of the heterotic gauge $`\beta`$ to leading order; see . This matches our EL equation for $`A`$ from the selection functional $`\Xi`$ (Theorem 5.2).

## Global issues: Bianchi identity and Freed–Witten

The worldsheet theory is globally well-defined when the gerbe curvature $`H_b`$ satisfies the Bianchi identity $`dH_b=\tfrac{\alpha'}4\big(\mathrm{Tr}F\wedge F - \mathrm{Tr}R_+\wedge R_+\big)`$. This coincides with the $`K`$–multiplier constraint in $`\Xi`$; Freed–Witten consistency follows from the integral cohomology class of $`H_b`$ chosen in the topological sector fixed in §5 (*cf.* ).

## Scheme dependence and the $`R_+`$ choice

Differences between $`R_+`$ and $`R_-`$ correspond to local field redefinitions at $`O(\alpha')`$; our selection functional uses $`R_+`$, which is the supersymmetric choice and matches the heterotic $`\beta`$–function scheme used in .

## Higher orders (remarks)

At $`O(\alpha'^2)`$, curvature-squared and higher-derivative terms appear in both spacetime equations and $`\beta`$–functions; these can be incorporated in $`\Xi`$ by additional local functionals. The contraction/Lyapunov parts of the selection proof rely on sectoriality and bounded geometry and are robust under such perturbative additions.

## Explicit checks on Fu–Yau and Iwasawa models

For the Fu–Yau class, conformal balance and the HYM condition are satisfied; the Bianchi identity holds with $`R_+`$ for appropriate topological data. For Iwasawa, $`d(J^2)=0`$, $`H=i(\bar\partial-\partial)J`$, and an HYM bundle exist; the Bianchi identity is solved componentwise in the invariant $`(2,2)`$ sector. These match the assumptions used in our selection theorem and provide concrete worldsheet-consistent backgrounds (see §8 and Appendix E for models).

# Reproducibility notes

Frames, orientations, normalizations, sign conventions, and parameter choices match the conventions used in the main text. In particular: (1) Iwasawa orientation $`\int_X a\wedge b\wedge c=1`$, with $`dH`$ as in <a href="#eq:iwa-dH" data-reference-type="eqref" data-reference="eq:iwa-dH">[eq:iwa-dH]</a> and $`\mathrm{Tr}_{\mathrm{grav}}R_{+}^2`$ as in <a href="#eq:iwa-Rplus" data-reference-type="eqref" data-reference="eq:iwa-Rplus">[eq:iwa-Rplus]</a>; (2) $`\text{Lens}\times\text{Nil}`$ scale parameters $`\lambda \sim R_1^{-1}`$ and $`\nu \sim R^{-1}`$, with coefficients as in <a href="#eq:lens-dH" data-reference-type="eqref" data-reference="eq:lens-dH">[eq:lens-dH]</a>–<a href="#eq:lens-anom" data-reference-type="eqref" data-reference="eq:lens-anom">[eq:lens-anom]</a>. All numbers needed to reproduce the componentwise anomaly solutions are tabulated in App. <a href="#app:coeffs" data-reference-type="ref" data-reference="app:coeffs">10</a>.

[^1]: For a concise synthesis of the fixed-point framework see, e.g., ; for the explicit heterotic Iwasawa and $`\text{Lens}\times\text{Nil}`$ backgrounds with full anomaly match see .
