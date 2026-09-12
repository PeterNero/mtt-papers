---
abstract: |
  We re-execute the Route A geometric overlap ansatz against the selected multi-loop gauge-profile targets of Paper I. In its stated dimensionless normalization, the round-$`S^2`$ effective lens base and isotropic compact Heisenberg nilmanifold can be retargeted analytically to
  ``` math
  (f_2R_{\mathrm{lens}})^2=0.2555137R_1,
   \qquad c=0.9948493R_1.
  ```
  The associated spectral lower bounds remain above the assumed dimensionless admissibility floor. This proves existence of a calibrated representative in the declared auxiliary ansatz. It does not prove that the full lens space reduces to this $`S^2`$ model, identify the Lens–Nil representative with the selected q79/Fu–Yau compactification, select a geometry uniquely by MTT, or make the gauge couplings held-out predictions. The shared circle is common $`U(1)`$ phase/holonomy data, not an additional factor in a $`S^1\times L(3,1)\times\mathrm{Nil}_3`$ manifold.
author:
- Peter Nero
current_version: v3
date: September 2026 (Version 3)
generated_from_main_tex_sha256: 2b599efd41a4f28b7bf2f39b478cbca32b0492fd7704d82ef61281401c444896
paper_id: theta-closure-in-modal-triplet-theory-ii-direct-geometr-303cc1ca
release_state: current_revised_tex
released_version: v2
title: "Theta Closure in Modal Triplet Theory II: Direct Geometric Realization of Selected Gauge-Profile Overlaps"
zenodo_doi: 10.5281/zenodo.21666008
zenodo_record_id: 21666008
zenodo_url: "https://zenodo.org/records/21666008"
---

# Version 3 Revision Note

Supersedes.
Version 2 of this paper; released identifiers are retained.

Reason.
The calibration boundary was present, but the selected-source owner results and their distinct scopes were not explicitly connected to it.

Resolution.
Version 3 imports the exact Gate 1, three-cycle and large-gauge-kernel conclusions through their owners, and also keeps both scalar spectral branches in the uniform lower bound.

Retained.
The existing calibrated or conditional result, its numerical inputs and all earlier revision notes are retained.

Open boundary.
A selected physical source, its action normalization and the paper-specific execution inputs remain necessary for a held-out prediction.

# Revision note for this edition

Supersedes.
*Theta Closure in Modal Triplet Theory II: Direct Geometric Realization of Nonabelian Overlaps*, first edition.

Reason.
The previous numerical target came from the retired few-TeV crossing and the auxiliary Lens–Nil ansatz was liable to be read as the selected q79 compactification or a literal circle product.

Resolution.
Version 2 retargets the analytic ansatz to the Paper I SMDR profile, counts the shared circle only as common holonomy data, and labels the round-$`S^2`$/nil model auxiliary and calibrated.

Retained result.
An explicit representative satisfying the two target ratios and dimensionless spectral-floor test exists in the declared ansatz.

Remaining boundary.
No uniqueness, full lens reduction, q79/Fu–Yau identification, or held-out gauge prediction is established.

# Purpose, central picture, and roadmap

Paper I supplies two dimensionless target ratios. This paper asks a deliberately narrow inverse question: can one choose the two scale parameters in a simple auxiliary geometry so that its overlap integrals reproduce those ratios while remaining above the declared spectral floor? The answer is yes.

The central picture is elementary. The weak coefficient is represented by the effective area of a round two-sphere, while the color coefficient is represented by the length of the central fiber of a compact Heisenberg nilmanifold. The shared-circle normalization fixes the common denominator. Thus two measured target ratios determine two auxiliary geometric scales. This is an existence and calibration calculation, not a uniqueness argument and not a prediction of the measured ratios.

The dependency chain is
``` math
\begin{gathered}
\text{Paper~I target ratios}
\longrightarrow
\text{two overlap equations}
\longrightarrow
\text{two auxiliary scales}\\
\longrightarrow
\text{spectral-floor check}.
\end{gathered}
```
The overlap sections execute the two equations separately. The interpretation section states exactly what the construction establishes, and the appendix derives the nilmanifold bound used in the final admissibility check.

# Relation to the revised $`\Theta`$-closure core paper

Paper I now transports measured source coordinates with SMDR v1.3 to the full-Standard-Model $`\overline{\mathrm{MS}}`$ profile at $`Q=M_t`$. In the same GUT-normalized overlap convention it supplies
``` math
\frac{I_2}{I_1}=0.5110273\pm0.0001231,
 \qquad
 \frac{I_3}{I_1}=0.158335\pm0.001098.
```
The scale $`Q=M_t`$ is a matching convention, not an internal gap or coherence scale. This paper asks only whether the explicit Route A ansatz contains a representative with those overlap ratios and the stated dimensionless gap margin. Because the gauge rows select the target, success is a calibrated realization and round-trip test.

# Overlap definitions

We recall the effective gauge-kinetic coefficients defined in Paper I:
``` math
I_a = \int_{B_a}
w_a\langle \omega_a, \omega_a\rangle\,d\mu_{B_a},
\qquad a=1,2,3,
```
where $`B_a`$ denotes a sector support after spectator integrations. The three supports are not asserted to be simultaneous Cartesian factors of one compactification. The same shared-circle phase datum is reused in all lanes and counted once.

In the auxiliary coefficient ansatz, the abelian coefficient $`I_1`$ is fixed by the declared shared-circle normalization:
``` math
I_1 = 2\pi R_1.
```

We compute $`I_2^{(0)}`$ and $`I_3^{(0)}`$ below.

# Lens sector: computation of $`I_2^{(0)}`$

#### Dimensional and geometric convention.

All radii and overlaps below are dimensionless after one common internal length unit has been factored out. The “lens layer” used in the calculation is an effective two-dimensional constant-curvature base modeled by a round $`S^2`$; it is not the full three-dimensional lens space $`L(3,1)`$. A full lens-space realization requires a separate reduction theorem.

## Lens geometry

The declared auxiliary lens-base ansatz uses the spectral bound
``` math
\lambda_{\mathrm{lens}} \ge \frac{2}{(f_2R_{\mathrm{lens}})^2}.
```

<div class="remark">

*Remark 1* (Why the round $`S^2`$ model is used here). The coefficient $`2/R^2`$ is the exact first nonzero Laplace–Beltrami eigenvalue on the round two-sphere of radius $`R`$. Thus modeling the lens layer as a constant-curvature $`S^2`$ scaled by the effective radius $`f_2R_{\mathrm{lens}}`$ supplies one explicit geometry with the stated spectral bound. It is not selected uniquely by that eigenvalue.

</div>

The coefficient “2” motivates the round two–sphere as the baseline effective model within this ansatz; it is not a global uniqueness theorem. We take
``` math
\Sigma_2 \simeq S^2,
\qquad
g_{\Sigma_2} = (f_2R_{\mathrm{lens}})^2 g_{S^2}.
```

## Lens harmonic

The massless gauge representative is taken to have unit pointwise norm on $`\Sigma_2`$ after gauge fixing. The shared-circle phase is a common spectator whose normalization is absorbed into Paper I’s coefficient convention. With the auxiliary weight $`w_2^{(0)}=1`$, this gives
``` math
I_2^{(0)} = \mathrm{Area}(\Sigma_2) = 4\pi(f_2R_{\mathrm{lens}})^2.
```

## Matching to $`\Theta`$-target

From Paper I,
``` math
\frac{I_2}{I_1} \approx 0.5110273,
\qquad I_1 = 2\pi R_1.
```

Hence
``` math
\frac{4\pi(f_2R_{\mathrm{lens}})^2}{2\pi R_1} = 0.5110273
\quad\Rightarrow\quad
(f_2R_{\mathrm{lens}})^2 = 0.2555137\,R_1.
```

<div class="proposition">

**Proposition 2** (Lens overlap closure). *The lens overlap $`I_2^{(0)}`$ matches the $`\Theta`$–target for $`(f_2R_{\mathrm{lens}})^2 = 0.2555137\,R_1`$.*

</div>

## Lens admissibility

The spectral bound gives
``` math
\lambda_{\mathrm{lens}} \ge \frac{2}{0.2555137\,R_1}.
```

Since admissibility of the circle sector requires $`R_1\le 2`$, we obtain
``` math
\lambda_{\mathrm{lens}}
\ge \frac{2}{0.2555137\cdot 2}
\approx 3.9137 \gg 0.25.
```
Thus the lens sector is safely admissible.

# Nil sector: computation of $`I_3^{(0)}`$

## Nil geometry

We take $`\Sigma_3`$ to be the standard compact Heisenberg nilmanifold $`\Gamma\backslash\mathrm{Nil}_3`$ with integer lattice and left–invariant metric
``` math
g_{\mathrm{nil}} = a^2\sigma_1^2 + b^2\sigma_2^2 + c^2\sigma_3^2,
```
where
``` math
\sigma_1=dx,\quad \sigma_2=dy,\quad \sigma_3=dz-x\,dy.
```

## Canonical massless harmonics

The first cohomology is generated by the closed forms $`dx`$ and $`dy`$. We choose the isotropic convention
``` math
a=b,
```
which renders the overlap independent of the basis in $`\mathrm{span}\{dx,dy\}`$.

## Overlap computation

For $`\omega^{(0)}=dx`$ or $`dy`$, auxiliary weight $`w_3^{(0)}=1`$, and the unit coordinate fundamental domain,
``` math
|\omega^{(0)}|^2 = \frac{1}{a^2},
\qquad
d\mathrm{vol} = a^2 c\,(\sigma_1\wedge\sigma_2\wedge\sigma_3).
```

Hence
``` math
I_3^{(0)} = \int |\omega^{(0)}|^2\,d\mathrm{vol} = c.
```

## Matching to $`\Theta`$-target

From Paper I,
``` math
\frac{I_3}{I_1}\approx 0.158335
\quad\Rightarrow\quad
I_3 \approx 0.9948493\,R_1.
```

Therefore
``` math
\boxed{c = 0.9948493\,R_1.}
```

<div class="proposition">

**Proposition 3** (Nil overlap closure). *For the isotropic nil metric $`a=b`$ with $`c=0.9948493\,R_1`$, the leading–order nil overlap $`I_3^{(0)}`$ matches the $`\Theta`$–target.*

</div>

## Nil admissibility

The scalar Laplacian on $`\Gamma\backslash\mathrm{Nil}_3`$ has spectrum
``` math
\lambda_1 \ge \min\left\{\frac{4\pi^2}{a^2},
\;\frac{2\pi}{a^2}+\frac{4\pi^2}{c^2}\right\}.
```

With $`a=b=1`$ and $`c\le 1.989699`$ (from $`R_1\le 2`$),
``` math
\lambda_1
\ge
\min\left\{4\pi^2,\,
2\pi+\frac{4\pi^2}{(1.989699)^2}\right\}
\approx 16.2553 \gg 0.25.
```

Thus the nil sector satisfies the MTT admissibility bound $`\lambda_{\mathrm{nil}}\ge 0.25`$ with large margin.

# Interpretation of the Route-A result and scope

Within the declared dimensionless ansatz, the selected profile targets admit an explicit lens-base/nil representative and the assumed spectral inequalities remain satisfied. This closes the algebraic retargeting and ansatz-level existence check. It does not close source selection of the geometry, a literal $`L(3,1)`$ reduction, global HYM connection data, or a held-out gauge-coupling prediction. In particular, this auxiliary representative is not the q79 Fu–Yau compactification and supplies no theorem identifying the two spaces.

# Worked case: unit abelian radius

Taking $`R_1=1`$ makes the normalization and the role of each parameter transparent:
``` math
f_2R_{\mathrm{lens}}=\sqrt{0.2555137}\approx0.505484,
\qquad
c=0.9948493.
```
The three overlap coefficients are then
``` math
I_1=2\pi\approx6.283185,\qquad
I_2=4\pi(0.2555137)\approx3.210880,\qquad
I_3=0.9948493.
```
Consequently
``` math
\frac{I_2}{I_1}=0.5110274,
\qquad
\frac{I_3}{I_1}=0.1583352,
```
up to the displayed rounding. The lens lower bound is approximately $`7.8274`$. For the nilmanifold, the torus branch gives $`4\pi^2\approx39.4784`$ and the Landau branch is larger, so the lower bound is $`39.4784`$. This example shows concretely how the target ratios determine the auxiliary scales; it does not turn those fitted scales into independent predictions.

# Spectral lower bound on $`\Gamma\backslash\mathrm{Nil}_3`$ for the left-invariant metric

This appendix justifies the spectral estimate used in the nil admissibility check.

## Heisenberg nilmanifold and left-invariant metric

Let $`\mathrm{Nil}_3`$ be the Heisenberg group with global coordinates $`(x,y,z)\in\mathbb{R}^3`$ and left-invariant 1-forms
``` math
\sigma_1 = dx,\qquad
\sigma_2 = dy,\qquad
\sigma_3 = dz - x\,dy,
```
satisfying $`d\sigma_1=d\sigma_2=0`$ and $`d\sigma_3=-\sigma_1\wedge\sigma_2`$.

Let $`\Gamma`$ be the standard integer lattice so $`\Gamma\backslash\mathrm{Nil}_3`$ is compact. Equip it with the left-invariant metric
``` math
g = a^2\sigma_1^2 + b^2\sigma_2^2 + c^2\sigma_3^2,
\qquad a,b,c>0.
```

The dual left-invariant vector fields are
``` math
X=\partial_x,\qquad
Y=\partial_y + x\,\partial_z,\qquad
Z=\partial_z,
```
with $`[X,Y]=Z`$ and other brackets zero. An orthonormal frame is
``` math
e_1=\frac{1}{a}X,\qquad e_2=\frac{1}{b}Y,\qquad e_3=\frac{1}{c}Z.
```

## Scalar Laplacian

For a left-invariant orthonormal frame, the scalar Laplacian on functions may be written as
``` math
\Delta f = -(e_1^2+e_2^2+e_3^2)f
```
(up to sign convention; we use the nonnegative operator $`-\sum e_i^2`$). Substituting the frame gives
``` math
\begin{equation}
\Delta
=
-\frac{1}{a^2}\partial_x^2
-\frac{1}{b^2}(\partial_y + x\partial_z)^2
-\frac{1}{c^2}\partial_z^2.
\label{eq:nil_laplacian}
\end{equation}
```

## Fourier decomposition in the central direction

Because $`z`$ is periodic on $`\Gamma\backslash\mathrm{Nil}_3`$, expand
``` math
f(x,y,z)=\sum_{p\in\mathbb{Z}} e^{2\pi i p z}\,g_p(x,y).
```
On the $`p`$-th mode, $`\partial_z\mapsto 2\pi i p`$ and <a href="#eq:nil_laplacian" data-reference-type="eqref" data-reference="eq:nil_laplacian">[eq:nil_laplacian]</a> becomes
``` math
\begin{equation}
\Delta_p
=
-\frac{1}{a^2}\partial_x^2
-\frac{1}{b^2}(\partial_y + 2\pi i p\,x)^2
+\frac{(2\pi p)^2}{c^2}.
\label{eq:nil_laplacian_p}
\end{equation}
```

We bound the lowest nonzero eigenvalue by analyzing $`p=0`$ and $`p\neq 0`$ separately.

## The $`p=0`$ sector (torus bound)

For $`p=0`$,
``` math
\Delta_0 = -\frac{1}{a^2}\partial_x^2-\frac{1}{b^2}\partial_y^2
```
on the flat 2-torus $`(x,y)\in(\mathbb{R}/\mathbb{Z})^2`$. Its eigenvalues are
``` math
\lambda^{(0)}_{m,n} = 4\pi^2\left(\frac{m^2}{a^2}+\frac{n^2}{b^2}\right),
\qquad (m,n)\in\mathbb{Z}^2.
```
Hence the smallest nonzero eigenvalue in this sector satisfies
``` math
\begin{equation}
\lambda_{\min}^{(0)} \ge \frac{4\pi^2}{\max(a^2,b^2)}.
\label{eq:lambda_p0}
\end{equation}
```

## The $`p\neq 0`$ sector (Landau/oscillator lower bound)

For $`p\neq 0`$, the operator <a href="#eq:nil_laplacian_p" data-reference-type="eqref" data-reference="eq:nil_laplacian_p">[eq:nil_laplacian_p]</a> is the magnetic Laplacian on a 2-torus with constant magnetic field proportional to $`p`$, plus a strictly positive shift $`(2\pi p)^2/c^2`$. A lower bound follows from the magnetic covariant-derivative commutator: the nonnegative square of the corresponding raising or lowering combination bounds the two-dimensional magnetic energy below by $`2\pi|p|/(ab)`$. Thus one must retain, not discard, the magnetic term:
``` math
\begin{equation}
\lambda_{\min}^{(p)} \;\ge\; \frac{2\pi |p|}{ab} + \frac{(2\pi p)^2}{c^2},
\qquad p\neq 0.
\label{eq:lambda_pnonzero}
\end{equation}
```
(For our purposes it suffices to retain the $`|p|=1`$ bound.)

Under the isotropic convention $`a=b`$, this yields
``` math
\begin{equation}
\lambda_{\min}^{(1)} \ge \frac{2\pi}{a^2}+\frac{4\pi^2}{c^2}.
\label{eq:lambda_p1}
\end{equation}
```

## Combined lower bound

Combining <a href="#eq:lambda_p0" data-reference-type="eqref" data-reference="eq:lambda_p0">[eq:lambda_p0]</a> and <a href="#eq:lambda_p1" data-reference-type="eqref" data-reference="eq:lambda_p1">[eq:lambda_p1]</a>, we obtain
``` math
\begin{equation}
\lambda_1\big(\Delta_{\Gamma\backslash\mathrm{Nil}_3}\big)
\;\ge\;
\min\left\{
\frac{4\pi^2}{a^2},
\;
\frac{2\pi}{a^2}+\frac{4\pi^2}{c^2}
\right\},
\qquad (a=b).
\label{eq:lambda_min_final}
\end{equation}
```

In particular, for $`a=b=1`$ and any $`c\le 1.989699`$, one has
``` math
\lambda_1 \ge
\min\left\{4\pi^2,2\pi+\frac{4\pi^2}{c^2}\right\}
\ge\min\left\{4\pi^2,2\pi+\frac{4\pi^2}{(1.989699)^2}\right\}
\approx16.2553,
```
which is much larger than the admissibility floor $`0.25`$ used in Paper I. The minimum is essential: at $`c=1`$ the torus branch supplies an eigenvalue $`4\pi^2`$, so the larger Landau expression alone cannot bound the full gap from below. The uniform admissibility conclusion is unchanged.

<div class="remark">

*Remark 4*. The estimates above are intentionally conservative and suffice only to demonstrate a large spectral margin. A complete scalar spectrum for the three-dimensional Heisenberg nilmanifold is available in Ref. , but is not required for the present admissibility verification.

</div>

# Conclusion

The Route A formulas have been evaluated in the same normalization and scheme as revised Paper I. The new central representative is
``` math
(f_2R_{\mathrm{lens}})^2=0.2555137R_1,
 \qquad c=0.9948493R_1,
```
with uncertainties inherited from the two profile ratios. The nil spectral estimate and lens lower bound continue to exceed the assumed dimensionless floor for the stated parameter range.

The earlier numbers $`0.280R_1`$ and $`1.439R_1`$ belonged to the withdrawn $`5~\mathrm{TeV}`$ profile and are not retained. The present construction is a calibrated existence result: the target gauge rows were used to determine the geometry. Selection of this geometry before empirical comparison, literal lens-space reduction, and a global HYM representative remain separate proof obligations.

# Selected-source results and this paper’s boundary

The eta9 imports are owned contextually by *Flux Compactifications in Heterotic String Theory*, in the sections on the selected source and the integral comparison, and completed local tests and the global endpoint. Gate 1 closes the original-Jacobian campaign at all 30 groups and 225 selected columns . This is an exact finite source calculation, not the global integral meridian, the 248-coordinate readout or the analytic Deligne class $`\beta_{\mathbb C}`$.

The completed three-cycle transport has independent cycles with Gram matrix $`-2I_3`$ and zero detected affine pairings . Its scope is a non-detecting subsystem: it does not prove global triviality of the twist, and rerunning that same subsystem is not the missing detection theorem. Neither this conclusion nor the finite gate identifies an auxiliary Circle–Lens–Nil model with the physical q79 topology.

The large-gauge result is owned by *Cohesive Closure Repair and Its Hodge, Kernel, and Projection Shadows*, in its subsection on the rank-zero large-gauge kernel. It gives an injective immersion $`b_{K3}:\mathbb R^2\to\mathbb T^{20}`$ with dense nonclosed image . Rank zero counts periodic gauge identifications, not source coordinates or physical modes. It removes a kernel ambiguity without requiring numerical periods, but does not provide kinetic normalization, the selected shared-circle action or the unrelated eta9 affine lift.

For Route A, these imports do not identify the auxiliary round-$`S^2`$/nil supports with the global q79/Fu–Yau space or derive their radii from it. The calibrated representative and its dimensionless spectral margin survive. The hidden projective rank-nine carrier and existential HYM connection are already established; the visible bundle, a common metric chamber and executable physical overlap data remain distinct obligations.

The managed evidence block below retains its earlier frozen profile snapshot. Its historical source-status labels do not supersede the current exact, local and open boundaries just stated or reopen the retained hidden-HYM existence and shared-primitive Standard Model results.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The HYM contraction, finite-matrix realization, precision transport, and electroweak row are used directly to assess the selected overlap realization. The remaining profile packets locate that realization within the broader closure program but do not prove its geometry. The strict source upgrade remains open.

The referenced rows are frozen to the curated results repository state identified below. Hashes are grouped in eight-character blocks for line breaking.

> **Repository:** <https://github.com/PeterNero/mtt-results-repro>
> **Commit:** `31247ebb 5c22f3fb b5443024 365433c6 ee0bff4a`
> **Manifest:**
> **Manifest SHA-256:**
> `fb399689 60b00584 631dbf53 1a708e18`
> `ef928d6b 6d935119 c185d7f6 32b1e7cd`

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper’s local theorems; and an open row is evidence of an unresolved obligation, never of closure.

= by -
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

#### Rows used directly in this paper.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Corpus-state cross-checks.

- (*profile replay*).

  Versioned Yu, Yd, Ye and lambda_H profile packet.

- (*numeric certified*).

  Three selected CKM profile rows and uncertainty comparison.

- (*profile replay*).

  Current non-looping global status and source-certificate map.

- (*derived exact*).

  Promoted direct K_threshold.Omega_H.lambda row.

- (*derived exact*).

  E6 Qpsi matter/exotic QCD anomaly cancellation audit.

- (*profile replay*).

  Twelve-obligation embedded renormalized-SM equivalence audit.

- (*profile replay*).

  Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<div class="thebibliography">

99

P. Nero, *Selected eta9 original-Jacobian Gate 1 campaign* (2026). Frozen source at curated manifest commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7`: [source artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/eta9_gate1_campaign/artifact.json).

P. Nero, *Complete selected three-cycle non-detection decision* (2026). Frozen source at curated manifest commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7`: [source artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/eta9_three_cycle_b96_nondetection/artifact.json).

P. Nero, *Selected K3 rank-zero large-gauge kernel* (2026). Frozen source at curated manifest commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7`: [source artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/q79_bk3_rank_zero_kernel/artifact.json).

D. Andriot and D. Tsimpis, *Laplacian spectrum on a nilmanifold, truncations and effective theories*, JHEP **09** (2018) 096. <https://doi.org/10.1007/JHEP09(2018)096>

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

P. Nero, *Modal Triplet Theory and History-Dependent Stochastic Processes: Fixed-State Indivisibility, Markov Order, and the Quantum Boundary*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
