---
abstract: |
  This paper identifies the precise sense in which a Modal Triplet Theory (MTT) realization can reproduce classical four-dimensional General Relativity. The starting point is a ten-dimensional bundle over a Lorentzian four-manifold with compact six-dimensional fiber $`X_6`$, together with a local covariant action whose gravitational sector contains the higher-dimensional Einstein–Hilbert term. That metric and action are realization inputs; they are not derived here from projection alone. We formulate an exact consistent-truncation condition and an approximate gapped version that bounds discarded modes and the induced effective-action error. When all unwanted metric zero modes are absent, stabilized, or retained explicitly, the two-derivative metric sector reduces to Einstein–Hilbert form with $`\kappa_4^2=\kappa_{10}^2/V_W`$, where $`V_W`$ is the warped internal volume. Diffeomorphism invariance then gives the Einstein equation and covariant stress-energy conservation; universal minimal coupling supplies the usual geometric-optics and test-body limits. The current MTT calculation also provides an exact finite-branch transverse-traceless helicity-two support certificate. It does not yet determine the physical Newton/Planck normalization, the complete stress-energy response, the cosmological constant, or a projection-only source for the Lorentzian action. The result is therefore a controlled GR-limit theorem and a sharply delimited research bridge, not a first-principles derivation of gravity from MTT axioms alone.
author:
- Peter Nero
current_version: v3
date: July 2026
generated_from_main_tex_sha256: 65b0acc3e9f6610b4dc2d92a71ed0275b1438be36cd2d1087047e018d2a66673
paper_id: modal-triplet-theory-from-mtt-to-general-relativity
release_state: zenodo_released
released_version: v3
title: |
  **Controlled Coherent Reduction to
  Four-Dimensional Einstein Gravity**
zenodo_doi: 10.5281/zenodo.21665995
zenodo_record_id: 21665995
zenodo_url: "https://zenodo.org/records/21665995"
---

# Revision note for this edition

<div class="description">

*Modal Triplet Theory: From MTT to General Relativity*, version 2.

The previous edition called a standard dimensional reduction a first-principles derivation even though it inserted the ten-dimensional Einstein–Hilbert action at the outset. It also wrote $`Y_4\times B_1\times B_2\times B_3`$ with three three-dimensional factors and called the result ten-dimensional, omitted the nonlinear consistent-truncation test, and suppressed possible scalar and vector zero modes.

This edition uses $`M_{10}\to Y_4`$ with six-dimensional fiber $`X_6`$, separates imported causal/action data from derived reduction statements, supplies exact and approximate truncation criteria, treats moduli and Kaluza–Klein vectors explicitly, and restricts the uniqueness claim to the hypotheses of the four-dimensional two-derivative metric sector.

Given a higher-dimensional Einstein–Hilbert sector and a valid coherent truncation, the internal pushforward does yield a four-dimensional Einstein–Hilbert term and the standard Einstein equations with an effective coupling fixed by the warped volume.

MTT has not yet selected the physical Lorentzian principal symbol and action from projection alone, nor derived the SI value of Newton’s constant, the full matter stress response, or the observed cosmological constant from the same source. The exact finite-branch helicity-two support result closes an internal support gate only.

</div>

# Overview: Question, Answer, and Logical Status

## The question actually answered

The paper asks a conditional but important question:

> Given a ten-dimensional Lorentzian metric theory on a selected MTT carrier, when does its coherent low-energy sector reduce to four-dimensional Einstein gravity, and what is still needed before that reduction becomes an MTT source theorem?

There are four different operations in that sentence. Keeping them separate prevents a valid calculation from being assigned a stronger meaning than it has:
``` math
\begin{gathered}
\boxed{\text{source selects geometry and action}}
\longrightarrow
\boxed{\text{retain a coherent mode sector}}
\\[1mm]
\Downarrow
\\[-1mm]
\boxed{\text{compare the 4D observables with GR}}
\longleftarrow
\boxed{\text{integrate out discarded modes}} .
\end{gathered}
```
This paper proves implications in the last three boxes after the first has been supplied. It does not prove the first box.

## Current MTT status

<div class="center">

| Status | Content |
|:---|:---|
| Established internally | The selected finite exact branch has a two-dimensional helicity-two transverse-traceless support carrier and normalized internal eigenvalue $`\lambda_{\mathrm{GR},\mathrm{TT}}=15`$. |
| Conditional bridge | A supplied ten-dimensional Lorentzian action reduces to a four-dimensional metric action under the consistency, gap, stabilization, and locality conditions stated below. |
| Not selected here | The Lorentzian metric or principal symbol, the Einstein–Hilbert source coefficient, the selected compactification solution, and the boundary and quantization data. |
| Still open physically | Newton/Planck normalization, complete stress-energy response, the observed cosmological constant, and a same-source derivation connecting the internal TT carrier to the normalized spacetime graviton. |

</div>

The distinction matters. A helicity-two carrier is necessary for a graviton sector, but it is not by itself a kinetic action, a universal coupling law, or Einstein’s nonlinear equation.

#### In plain language.

The compact geometry can tell us which internal patterns survive and how a supplied gravitational action is averaged. It cannot manufacture a Lorentzian causal law or its physical coupling merely by deleting modes. The paper therefore treats “which pattern survives,” “which equation governs it,” and “how strongly it couples” as three separate questions.

# Typed Ten-Dimensional Geometry

## Base, fiber, and the $`1<2<3`$ filtration

Let
``` math
\pi:M_{10}\longrightarrow Y_4
```
be a smooth bundle whose base $`Y_4`$ is a time-oriented Lorentzian four-manifold and whose compact fiber is a six-manifold $`X_6`$. In a local trivialization one may write $`M_{10}\simeq Y_4\times X_6`$, but the global bundle need not be a Cartesian product.

The MTT rank flag
``` math
1<2<3,\qquad 1+2+3=6,
```
is a filtration of internal carrier data. It is not a product of three independent three-manifolds. The shared circle is represented by one common $`U(1)`$ line bundle and connection reused by the relevant lanes; it is counted once and is not identified with Lorentzian time. The selected q79 Fu–Yau branch is the present compactification candidate. The auxiliary Lens–Nil model can still test local operators, but it is not interchangeable with that global six-manifold.

## Why the Lorentzian metric is an input

A local comparison field
``` math
Q_{\rm WW}\in\Gamma\!\left(\operatorname{Hom}(TP,TI)\right)
```
may define a positive comparison tensor $`Q_{\rm WW}^{T}Q_{\rm WW}`$. Such a Gram tensor is positive semidefinite and therefore cannot, without additional structure, be the Lorentzian spacetime metric. A physical realization must supply a Lorentzian principal symbol, or equivalently suitable frame/coframe and soldering data, before causal cones and hyperbolic propagation are defined. Projecting a positive internal norm does not change its signature by itself.

## A useful local metric ansatz

For the reduction calculation, take a background of the form
``` math
\begin{equation}
 \mathrm ds_{10}^{\,2}
 =e^{2A(y)}g_{\mu\nu}(x)\mathrm dx^\mu\mathrm dx^\nu
  h_{mn}(y)\mathrm dy^m\mathrm dy^n ,
\label{eq:warpedmetric}
\end{equation}
```
with fixed warp factor $`A`$ and fixed internal metric $`h`$ in the strict metric-only truncation. More general off-diagonal components and $`x`$-dependent moduli are not errors; they become four-dimensional vector and scalar fields and must be retained or consistently stabilized.

# The Higher-Dimensional Action Is a Realization Input

Consider a local covariant effective action
``` math
\begin{equation}
 S_{10}
 =\frac{1}{2\kappa_{10}^{2}}
  \int_{M_{10}}\!\sqrt{|g_{10}|}\,
  \bigl(R_{10}-2\Lambda_{10}\bigr)\,\mathrm d^{10}X
 +S_{\rm bulk}[g_{10},\Phi]
 +S_{\rm bdy}.
\label{eq:S10}
\end{equation}
```
The boundary term must make the chosen variational problem well posed. $`S_{\rm bulk}`$ can contain gauge fields, spinors, scalars, flux, torsion, and higher-derivative operators. Equation <a href="#eq:S10" data-reference-type="eqref" data-reference="eq:S10">[eq:S10]</a> is a declared action ansatz in the relevant regime. Varying it rigorously derives its field equations; that variation does not explain why MTT selects this action rather than another diffeomorphism-invariant action.

At energies $`E\ll\Lambda_{10}`$, the omitted operators are organized as a derivative expansion. Terms such as
``` math
R_{10}^{2},\quad R_{AB}R^{AB},\quad
 R_{ABCD}R^{ABCD},\quad R_{10}F^2,\quad F^4
```
are generally allowed unless a symmetry or a source theorem removes them. Their coefficients cannot be inferred from a spectral gap alone.

# Coherent Modes and Consistent Truncation

## Retained and discarded fields

Let $`\mathcal P`$ be the selected coherent projector and $`\mathcal Q=1-\mathcal P`$. Decompose every field, including metric fluctuations, as
``` math
\Phi=\Phi_{\mathcal P}+\eta_{\mathcal Q}.
```
Equivalently, for normalized internal modes $`\chi_n`$,
``` math
\Phi(x,y)=
 \sum_{a\in I_{\rm keep}}\phi_a(x)\chi_a(y)
 +\sum_{r\in I_{\rm disc}}\eta_r(x)\chi_r(y).
```
A harmonic projector is useful for identifying zero modes, but harmonicity alone does not prove that nonlinear products of retained modes fail to source discarded ones.

<div class="definition">

**Definition 1** (Exact coherent truncation). The retained ansatz is an exact consistent truncation when
``` math
\begin{equation}
 \left.
 \mathcal Q\,\frac{\delta S_{10}}{\delta\Phi}
 \right|_{\eta_{\mathcal Q}=0}=0
\label{eq:exacttrunc}
\end{equation}
```
for every retained configuration in the stated domain. Then every solution of the reduced equations uplifts to a solution of the full equations within that ansatz.

</div>

For an effective rather than exact truncation, define the discarded source
``` math
J_{\mathcal Q}(\Phi_{\mathcal P})
 :=
 \left.
 \mathcal Q\,\frac{\delta S_{10}}{\delta\Phi}
 \right|_{\eta_{\mathcal Q}=0}.
```
This is the object that a projection calculation must bound. The condition $`\|J_{\mathcal Q}\|\le\epsilon`$ is the explicit form of the source-leakage gate.

<div id="thm:controlled" class="theorem">

**Theorem 2** (Gapped approximate coherent reduction). *Fix Banach norms on retained and discarded fields in a neighborhood $`\mathcal U`$. Suppose:*

1.  *$`S_{10}`$ is twice differentiable on $`\mathcal U`$;*

2.  *the discarded linearized operator
    ``` math
    L_{\mathcal Q}
     =\left.
     \mathcal Q\,\frac{\delta^2S_{10}}{\delta\Phi^2}\,\mathcal Q
     \right|_{\eta_{\mathcal Q}=0}
    ```
    has an inverse on the gauge-fixed discarded subspace with $`\|L_{\mathcal Q}^{-1}\|\le m_{\rm gap}^{-2}`$;*

3.  *the nonlinear remainder in the discarded equation is Lipschitz in $`\eta_{\mathcal Q}`$ with constant $`L_N<m_{\rm gap}^{2}`$; and*

4.  *$`\|J_{\mathcal Q}(\Phi_{\mathcal P})\|\le\epsilon`$ uniformly.*

*Then the discarded equation has a unique local solution satisfying
``` math
\begin{equation}
 \|\eta_{\mathcal Q}\|
 \le
 \frac{\epsilon}{m_{\rm gap}^{2}-L_N}.
\label{eq:etabound}
\end{equation}
```
Substitution into the action gives the Schur–Feshbach correction
``` math
\begin{equation}
 S_{\mathrm{eff}}[\Phi_{\mathcal P}]
 =S_{10}[\Phi_{\mathcal P},0]
 -\frac12\langle J_{\mathcal Q},L_{\mathcal Q}^{-1}J_{\mathcal Q}\rangle
 +\mathcal O\!\left(\frac{\epsilon^3}{m_{\rm gap}^{6}}\right)
\label{eq:schur}
\end{equation}
```
whenever the stated expansion is uniform. Exact consistency is the special case $`J_{\mathcal Q}=0`$.*

</div>

<div class="proof">

*Proof.* Write the discarded Euler–Lagrange equation as
``` math
L_{\mathcal Q}\eta_{\mathcal Q}+J_{\mathcal Q}+N(\eta_{\mathcal Q})=0 .
```
The map $`T(\eta)=-L_{\mathcal Q}^{-1}[J_{\mathcal Q}+N(\eta)]`$ is a contraction on the ball of radius $`\epsilon/(m_{\rm gap}^{2}-L_N)`$. The Banach fixed-point theorem gives the unique solution and bound <a href="#eq:etabound" data-reference-type="eqref" data-reference="eq:etabound">[eq:etabound]</a>. Taylor expansion of the action at $`\eta_{\mathcal Q}=0`$, followed by $`\eta_{\mathcal Q}=-L_{\mathcal Q}^{-1}J_{\mathcal Q}+\mathcal O(\epsilon^2/m_{\rm gap}^4)`$, gives <a href="#eq:schur" data-reference-type="eqref" data-reference="eq:schur">[eq:schur]</a>. ◻

</div>

## The zero-mode audit

The gap in Theorem <a href="#thm:controlled" data-reference-type="ref" data-reference="thm:controlled">2</a> applies only on the complement of all zero modes. A compactification must therefore inventory them before claiming pure GR:

- deformations of $`h_{mn}`$ can produce scalar moduli;

- off-diagonal metric components $`g_{\mu m}`$ can produce vector fields, especially along internal isometries or invariant one-forms;

- form fields can produce additional scalars, vectors, and antisymmetric tensors; and

- gauge and diffeomorphism zero modes must be removed or treated by a declared gauge-fixing and ghost complex.

Each unwanted physical zero mode must be absent, stabilized above the working scale, or retained in the four-dimensional theory. Declaring it “incoherent” is not a substitute for checking its equation of motion.

# Four-Dimensional Einstein Sector

## Warped volume and Newton coupling

For the metric <a href="#eq:warpedmetric" data-reference-type="eqref" data-reference="eq:warpedmetric">[eq:warpedmetric]</a>, the coefficient of $`R_4(g)`$ is controlled by the warped volume
``` math
\begin{equation}
 V_W:=\int_{X_6}\sqrt{h}\,e^{2A(y)}\,\mathrm d^6y .
\label{eq:VW}
\end{equation}
```
If the volume and warp modes are fixed, the leading four-dimensional metric term is
``` math
\begin{equation}
 S_{\rm grav}^{(4)}
 =\frac{1}{2\kappa_4^2}
 \int_{Y_4}\sqrt{-g}\,(R_4-2\Lambda_4)\,\mathrm d^4x,
\qquad
 \kappa_4^2=\frac{\kappa_{10}^2}{V_W}.
\label{eq:kappa4}
\end{equation}
```
In the unwarped direct-product case, $`V_W=\operatorname{Vol}(X_6)`$. Internal curvature, flux, vacuum energy, branes, and higher-dimensional $`\Lambda_{10}`$ all contribute to the four-dimensional potential. Consequently $`\Lambda_4`$ is not, in general, just minus one half of an averaged internal scalar curvature.

Equation <a href="#eq:kappa4" data-reference-type="eqref" data-reference="eq:kappa4">[eq:kappa4]</a> is a dictionary, not yet a prediction. It predicts Newton’s constant only when both $`\kappa_{10}`$ and the normalized selected volume are derived independently. With the reduced Planck convention,
``` math
M_{\rm Pl,red}^{2}
 =\kappa_4^{-2}
 =\frac{V_W}{\kappa_{10}^{2}}.
```

## Why Einstein–Hilbert is the leading metric action

Suppose the low-energy retained gravitational field is only $`g_{\mu\nu}`$, the action is local and four-dimensionally diffeomorphism invariant, and the metric field equations contain no derivatives above second order. Under the standard natural-tensor assumptions, Lovelock’s four-dimensional result restricts the field equation to a linear combination of $`G_{\mu\nu}`$ and $`g_{\mu\nu}`$. Equivalently, the leading action is Einstein–Hilbert plus a cosmological term, up to a boundary term and a four-dimensional topological Gauss–Bonnet contribution.

This is a conditional uniqueness statement. It does not apply unchanged when additional light fields survive, locality is relaxed, higher derivatives are retained, or the causal principal symbol is not the metric one.

<div id="cor:GR" class="corollary">

**Corollary 3** (Controlled Einstein limit). *Assume the hypotheses of Theorem <a href="#thm:controlled" data-reference-type="ref" data-reference="thm:controlled">2</a>, stabilization or retention of every physical zero mode, universal minimal coupling of retained matter, and the metric-only two-derivative conditions above. Then, throughout the controlled regime, the leading metric equation is
``` math
\begin{equation}
 G_{\mu\nu}+\Lambda_4g_{\mu\nu}
 =\kappa_4^2T_{\mu\nu}
 +\Delta_{\mu\nu},
\label{eq:einstein}
\end{equation}
```
where $`\Delta_{\mu\nu}=0`$ for an exact two-derivative truncation and is bounded by the discarded-mode and higher-derivative errors in the approximate case.*

</div>

<div class="proof">

*Proof.* Theorem <a href="#thm:controlled" data-reference-type="ref" data-reference="thm:controlled">2</a> supplies a controlled local effective action. The field-content and derivative assumptions reduce its leading metric part to <a href="#eq:kappa4" data-reference-type="eqref" data-reference="eq:kappa4">[eq:kappa4]</a>. Varying with respect to $`g^{\mu\nu}`$ gives Eq. <a href="#eq:einstein" data-reference-type="eqref" data-reference="eq:einstein">[eq:einstein]</a>; the remaining terms define $`\Delta_{\mu\nu}`$. ◻

</div>

## Bianchi identity and stress-energy

For
``` math
T_{\mu\nu}
 :=-\frac{2}{\sqrt{-g}}
   \frac{\delta S_{\rm matter}^{(4)}}{\delta g^{\mu\nu}},
```
four-dimensional diffeomorphism invariance gives the Noether identity
``` math
\nabla^\mu T_{\mu\nu}=0
```
on the retained matter equations. This conservation law follows from the symmetry of the reduced action and the matter equations; it is not produced merely by averaging over $`X_6`$. In an approximate truncation the complete effective stress tensor, including the correction terms, is conserved.

# Motion, Equivalence, and Classical Tests

If all retained matter sectors couple to the same metric, a minimally coupled scalar in the WKB form $`\phi=a\,e^{iS/\varepsilon}`$ obeys at leading order
``` math
g^{\mu\nu}\partial_\mu S\,\partial_\nu S+m^2=0.
```
Its rays are timelike geodesics; the corresponding massless equation gives null geodesics. The same principal-symbol argument applies to standard minimally coupled wave equations. This establishes the geometric-optics limit and the weak equivalence principle within the declared universal coupling regime.

The statement has ordinary limits. Spinning bodies, extended bodies, self-gravitating objects, and fields with nonminimal curvature couplings can obey corrected motion equations. Projection alone does not prove universal minimal coupling; the common matter-metric source map must supply it.

Once Corollary <a href="#cor:GR" data-reference-type="ref" data-reference="cor:GR">3</a> applies with negligible $`\Delta_{\mu\nu}`$, the Newtonian, post-Newtonian, redshift, lensing, and gravitational-wave predictions are those of GR with $`G_N=\kappa_4^2/(8\pi)`$. This is agreement by reduction. It is not a new numerical prediction until the right-hand side of <a href="#eq:kappa4" data-reference-type="eqref" data-reference="eq:kappa4">[eq:kappa4]</a> is selected without importing $`G_N`$.

# The Exact MTT Helicity-Two Support Result

The current GR successor calculation establishes, on its selected finite exact branch,
``` math
\begin{equation}
 \Pi_{\rm exact64}B^\ast P_{\mathrm{TT}}=B^\ast P_{\mathrm{TT}},
\label{eq:TTsupport}
\end{equation}
```
or equivalently
``` math
\begin{equation}
 \operatorname{supp}(J_{\mathrm{TT}})
 =|d_\ast\rangle\otimes
 \operatorname{span}\{c_2,s_2\},
\qquad
 \lambda_{\mathrm{GR},\mathrm{TT}}=15
\label{eq:TTlambda}
\end{equation}
```
in normalized internal exact-branch units. The real $`k=2`$ and $`k=62`$ character plane of $`\mathbb C[\mathbb Z_{64}]`$ carries the two same-angle helicity-two directions. The associated certificate checks rank two, no support leakage outside the selected carrier, and the required finite central-shift intertwining.

## What this closes

Equations <a href="#eq:TTsupport" data-reference-type="eqref" data-reference="eq:TTsupport">[eq:TTsupport]</a>–<a href="#eq:TTlambda" data-reference-type="eqref" data-reference="eq:TTlambda">[eq:TTlambda]</a> close the internal transverse-traceless support question for that exact branch. They provide a nontrivial compatibility test: the selected finite carrier has precisely the two real polarizations required by a four-dimensional massless helicity-two sector. This result establishes carrier compatibility, not the full dynamics of the carrier.

## What it does not close

The support certificate does not by itself establish:

1.  the spacetime kinetic operator and its Lorentzian principal symbol;

2.  the residue and positivity of the physical graviton pole;

3.  the normalization $`\kappa_4`$ or the SI value of $`G_N`$;

4.  universal coupling to the complete conserved stress tensor;

5.  the nonlinear Einstein self-coupling; or

6.  the absence of extra scalar, vector, ghost, or massive spin-two modes.

Those are distinct gates. Conflating support with normalization was one of the reasons the earlier GR claim was too strong.

# Corrections Beyond the Strict Limit

The controlled four-dimensional effective action can contain
``` math
\begin{align}
 S_{\mathrm{eff}}
 =\int\sqrt{-g}\,\mathrm d^4x\,
 \Big[
 &\frac{M_{\rm Pl,red}^{2}}{2}(R-2\Lambda_4)
 +c_1R^2+c_2R_{\mu\nu}R^{\mu\nu}
 +c_3R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
 \nonumber\\
 &+\mathcal L_{\rm light}(g,\varphi,A,\psi)+\cdots
 \Big].
\label{eq:EFT}
\end{align}
```
In four dimensions one curvature-squared combination is topological, leaving two local combinations before field redefinitions and matter couplings are considered. The coefficients $`c_i`$ depend on the supplied higher-dimensional action, thresholds, background, and matching scheme. They are not universally proportional to a projector gap.

Around Minkowski space, a local Lorentz-invariant higher-derivative kinetic operator often factors schematically as
``` math
k^2\bigl(1+\alpha k^2+\cdots\bigr).
```
The ordinary massless pole $`k^2=0`$ remains luminal; the additional factor can introduce heavy poles or signal the limit of the EFT. It is therefore incorrect to read the expression automatically as a frequency-dependent speed for the massless graviton. Background curvature, Lorentz-violating operators, or nonlocal terms require their own principal-symbol analysis.

# Worked Direct-Product Example

Take $`A=0`$, a fixed compact $`X_6`$, and the action <a href="#eq:S10" data-reference-type="eqref" data-reference="eq:S10">[eq:S10]</a> with no light scalar or vector zero modes. Then
``` math
\sqrt{|g_{10}|}=\sqrt{-g_4}\sqrt{h_6},
\qquad
 R_{10}=R_4+R_6,
```
and direct integration gives
``` math
\begin{align}
 S_{10}
 &=
 \frac{V_6}{2\kappa_{10}^2}
 \int_{Y_4}\sqrt{-g_4}\,
 \bigl(R_4+\overline R_6-2\Lambda_{10}\bigr)\,\mathrm d^4x
 +S_{\rm matter}^{(4)}
\nonumber\\
 &=
 \frac{1}{2\kappa_4^2}
 \int_{Y_4}\sqrt{-g_4}\,
 (R_4-2\Lambda_4)\,\mathrm d^4x
 +S_{\rm matter}^{(4)},
\end{align}
```
with
``` math
\kappa_4^2=\frac{\kappa_{10}^2}{V_6},
\qquad
 \Lambda_4=\Lambda_{10}-\frac12\overline R_6
 +\text{(matter/flux vacuum terms)}.
```
This calculation is exact for the declared direct-product ansatz. It is not yet a proof that the ansatz solves the full ten-dimensional equations. Equation <a href="#eq:exacttrunc" data-reference-type="eqref" data-reference="eq:exacttrunc">[eq:exacttrunc]</a> supplies that additional test.

Now allow $`V_6=V_6(x)`$. The volume becomes a four-dimensional scalar, and a Weyl transformation to Einstein frame generates its kinetic term and couplings. Pure GR is recovered only after this modulus is stabilized or shown to decouple. This simple comparison explains why “integrate over the fiber” is not, by itself, a complete compactification proof.

# Claim Ledger and Research Frontier

<div class="center">

| Claim | Status | Required evidence |
|:---|:---|:---|
| $`M_{10}\to Y_4`$ with six-dimensional $`X_6`$ | Declared realization | Global bundle, metric, connection, and selected compactification solution. |
| Einstein–Hilbert reduction | Proved conditionally | Action <a href="#eq:S10" data-reference-type="eqref" data-reference="eq:S10">[eq:S10]</a>, zero-mode audit, and Eq. <a href="#eq:exacttrunc" data-reference-type="eqref" data-reference="eq:exacttrunc">[eq:exacttrunc]</a> or Theorem <a href="#thm:controlled" data-reference-type="ref" data-reference="thm:controlled">2</a>. |
| Einstein equation and Bianchi identity | Proved conditionally | Local diffeomorphism invariance, metric variation, and retained matter equations. |
| Two TT polarizations on the exact finite branch | Derived exactly | The $`\mathbb Z_{64}`$ support and intertwining certificate. |
| Physical $`G_N`$ and Planck scale | Open | Selected $`\kappa_{10}`$, normalized $`V_W`$, pole residue, and unit map. |
| Full stress-energy response | Open | One normalized source operator coupling all retained matter to the TT and constraint sectors. |
| Projection-only emergence of GR | Open | Selection of Lorentzian principal symbol, local action, and nonlinear universal coupling from one upper source. |

</div>

The next decisive theorem is therefore not another dimensional-reduction identity. It is a same-source gravity theorem that constructs the Lorentzian principal symbol, normalized spin-two kinetic operator, and conserved matter response from the selected MTT geometry, while proving the zero-mode and consistent-truncation conditions used here.

# Conclusion

The corrected result is substantial but narrower than the previous title suggested. MTT currently has a valid conditional path from a ten-dimensional metric realization to four-dimensional Einstein gravity and an exact internal helicity-two support certificate. The dimensional reduction, effective Newton-coupling dictionary, Einstein variation, Bianchi identity, and geometric-optics limit all follow once their stated inputs are present.

What remains is the genuinely theory-defining step: selecting those inputs from one MTT source and fixing their physical normalization. Until that step is complete, this paper establishes controlled compatibility with GR, not a complete derivation of GR from projection alone.

#### Rows used directly in this paper.

- (*derived exact*).

  Exact-branch internal TT support certificate; physical normalization remains open.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The internal transverse-traceless certificate is used directly as support for the declared exact branch. Its own boundary is preserved: physical normalization remains open. The paper's four-dimensional Einstein reduction still depends on the stated coherent-reduction and action hypotheses.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A13/gr_tt_support` (**DERIVED_EXACT**): Exact-branch internal TT support certificate; physical normalization remains open.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, revised edition, 2026.

P. Nero, *Closure Geometry and a Regime-Local Ten-Dimensional Action Ansatz*, fourth edition, 2026.

P. Nero, *The Modal Triplet Theory Program B1: Loop-Transport Consistency and the Conditional Gravity Realization*, second edition, 2026.

D. Lovelock, “The Einstein tensor and its generalizations,” *Journal of Mathematical Physics* **12** (1971) 498–501, [doi:10.1063/1.1665613](https://doi.org/10.1063/1.1665613).

M. J. Duff, B. E. W. Nilsson, and C. N. Pope, “Kaluza–Klein supergravity,” *Physics Reports* **130** (1986) 1–142, [doi:10.1016/0370-1573(86)90163-8](https://doi.org/10.1016/0370-1573(86)90163-8).

M. Petrini, “A systematic approach to consistent truncations of supergravity theories,” *Universe* **7** (2021) 485, [doi:10.3390/universe7120485](https://doi.org/10.3390/universe7120485).

J. F. Donoghue, “General relativity as an effective field theory: The leading quantum corrections,” *Physical Review D* **50** (1994) 3874–3888, [doi:10.1103/PhysRevD.50.3874](https://doi.org/10.1103/PhysRevD.50.3874).

R. M. Wald, *General Relativity*, University of Chicago Press, 1984.

G. W. Gibbons and S. W. Hawking, “Action integrals and partition functions in quantum gravity,” *Physical Review D* **15** (1977) 2752–2756, [doi:10.1103/PhysRevD.15.2752](https://doi.org/10.1103/PhysRevD.15.2752).

</div>
