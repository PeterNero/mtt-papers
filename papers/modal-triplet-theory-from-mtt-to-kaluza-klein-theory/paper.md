---
abstract: |
  We present a first-principles derivation of Kaluza–Klein (KK) compactification from Modal Triplet Theory (MTT), embedding the standard KK framework into MTT’s geometric/topological fixed-point structure. Starting from the MTT higher-dimensional configuration space and modal gap data, we show that the internal space $`B_{\rm KK}`$, its scale $`R_{\rm KK}`$, and the zero-mode spectrum are *selected* by a finite set of algebraic and integral constraints in a left-invariant basis. We formalize these constraints as a *fixed-point compactification condition (FCC)* and prove an equivalence (background level) between solving the higher-dimensional field equations in the left-invariant sector and solving the FCC. We then prove that the familiar 10D$`\to`$<!-- -->4D compactification (with a compact $`B_6`$) is *equivalent*, at background and zero-mode level, to the 9D$`\to`$<!-- -->3D *projection* description used in the fixed-point series (Riemannian submersion with compact six-dimensional fibers). The 4D Planck mass, gauge couplings, and KK masses are calculable geometric invariants of $`B_{\rm KK}`$ set by MTT gap parameters. Throughout we keep the presentation conservative and theory-agnostic on matter content, with a short outlook to phenomenology.
author:
- Peter Nero
current_version: v1.0
date: September 2, 2025
generated_from_main_tex_sha256: 347e75fa877868631dc871867be4e458d742985999d89c1a7c9e2a7f43483f4e
paper_id: modal-triplet-theory-from-mtt-to-kaluza-klein-theory
release_state: zenodo_released
released_version: v1.0
title: "**Modal Triplet Theory: From MTT to Kaluza–Klein Theory**"
zenodo_doi: 10.5281/zenodo.17038314
zenodo_record_id: 17038314
zenodo_url: "https://zenodo.org/records/17038314"
---

# Introduction and Motivation

## Kaluza–Klein theory in context

Kaluza–Klein (KK) theory unifies gravity with gauge interactions by starting from a higher-dimensional spacetime and compactifying the extra dimensions. The simplest 5D Einstein–Hilbert action compactified on a circle $`S^1`$ yields 4D gravity, a $`U(1)`$ gauge field from $`g_{\mu5}`$, and a scalar from $`g_{55}`$. Generalizing to more dimensions and nontrivial internal manifolds produces non-Abelian gauge groups and scalar sectors that match, at low energies, the bosonic content of known interactions (see  for classic references).

## MTT as a higher-dimensional superset

Modal Triplet Theory (MTT) posits a ten-dimensional modal configuration space $`M_{10}`$ equipped with a fixed-point field configuration determined by curvature–gap dynamics, topological superselection integers, and modal coherence conditions. In prior work, the MTT fixed-point has been shown to project onto GR, QM/QFT on curved spacetimes, Standard Model-like sectors, and higher-dimensional unifying frameworks. We use only structural inputs here: (i) topology/metric class of $`B_{\rm KK}`$, (ii) curvature–gap scales selecting characteristic radii, and (iii) superselection integers fixing bundles/holonomies. [^1]

#### Projection language used in the fixed-point series.

In the fixed-point series we often speak of “projecting nine spatial dimensions to the observed three”: work on a constant-time slice $`\Sigma^9`$ and use a Riemannian submersion $`\pi_{\rm sp}:\Sigma^9\to M_3`$ with compact six-dimensional fibers $`F_6`$. In Section <a href="#subsec:proj" data-reference-type="ref" data-reference="subsec:proj">3.5</a> we formalize this and prove it is *equivalent*, at background and zero-mode level, to the standard 10D$`\to`$<!-- -->4D compactification with internal space $`B_6=F_6`$; see also the explicit Iwasawa and Lens$`\times`$Nil realizations in the companion fixed-point paper.

#### Organisation.

Section <a href="#sec:MTT" data-reference-type="ref" data-reference="sec:MTT">2</a> summarizes the MTT higher-dimensional framework used here. Section <a href="#sec:ansatz" data-reference-type="ref" data-reference="sec:ansatz">3</a> develops the KK metric/field ansatz and the compactification vs. projection equivalence. Section <a href="#sec:FCC" data-reference-type="ref" data-reference="sec:FCC">4</a> states and proves the FCC–KK background equivalence in the left-invariant sector. Section <a href="#sec:4D" data-reference-type="ref" data-reference="sec:4D">5</a> derives the 4D effective action (Planck mass, gauge couplings, scalars, fermions, topological terms). Section <a href="#sec:mass" data-reference-type="ref" data-reference="sec:mass">6</a> gives the KK spectrum and mass formulas. Section <a href="#sec:gauge" data-reference-type="ref" data-reference="sec:gauge">7</a> discusses gauge couplings and unification patterns. Section <a href="#sec:pheno" data-reference-type="ref" data-reference="sec:pheno">8</a> sketches phenomenology. We conclude in Section <a href="#sec:concl" data-reference-type="ref" data-reference="sec:concl">9</a>.

# MTT Higher-Dimensional Framework

## Modal 10D structure

We consider a ten-dimensional manifold $`M_{10}\simeq M_4\times B_{\rm int}`$, with $`B_{\rm int}`$ a compact six-manifold encoding modal degrees of freedom. The field content includes: (i) a 10D Lorentzian metric $`g_{AB}`$, (ii) gauge connections $`A^{(n)}{}_A`$ for each factor $`G_n`$, (iii) fermions $`\Psi_{ij}`$ obeying a two-of-three family rule,[^2] (iv) coherent scalars $`\phi_n`$ with curvature–gap mass terms, and (v) topological superselection data $`(Q_{ij},k_2,k_3;g)`$ labeling sectors.

## Extension to $`D`$ dimensions

For KK we write $`M_D=M_4\times B_{\rm KK}`$ with $`d=D-4=\dim B_{\rm KK}`$. The MTT fixed point determines the topology and metric of $`B_{\rm KK}`$, together with curvature–gap parameters that fix characteristic scales and isometries.

## Action and gap data

We take a schematic $`D`$-dimensional action
``` math
\begin{equation}
S^{(D)}_{\rm MTT}=\frac{1}{2\kappa_D^2}\int_{M_D}\!\mathrm{d}^Dx\,\sqrt{-g}\,\Big(R_D-2\Lambda_D+{\cal L}_{\rm YM}+{\cal L}_{\rm Dirac}+{\cal L}_{\phi,\vartheta}\Big)+S_{\rm top}[Q_{ij},k_2,k_3;g],
\label{eq:MTTaction}
\end{equation}
```
with gap parameters correlating internal curvature radii and the internal mass scales. We remain agnostic about specific matter representations.

# Metric and Field Ansatz for KK Reduction

## Block-diagonal metric and isometries

Adopt the standard KK decomposition
``` math
\begin{equation}
\label{eq:metric}
\mathrm{d}s_D^2=g_{\mu\nu}(x)\,\mathrm{d}x^\mu\mathrm{d}x^\nu+h_{mn}(y)\Big(\mathrm{d}y^m+A^{(m)}{}_\mu(x)\,\mathrm{d}x^\mu\Big)\Big(\mathrm{d}y^n+A^{(n)}{}_\nu(x)\,\mathrm{d}x^\nu\Big),
\end{equation}
```
with internal coordinates $`y^m`$ ($`m=1,\dots,d`$) and internal metric $`h_{mn}(y)`$. Let $`\{\xi^{(a)}\}`$ be Killing vectors of $`(B_{\rm KK},h)`$; then
``` math
\begin{equation}
\label{eq:Killingexp}
A^{(m)}{}_\mu(x,y)=\sum_a A^{(a)}{}_\mu(x)\,\xi^{(a)m}(y)+\cdots,\qquad [\xi^{(a)},\xi^{(b)}]=f^{ab}{}_c\,\xi^{(c)}.
\end{equation}
```

## Internal metric deformations and scalars

Fluctuations of $`h_{mn}`$ around the fixed-point geometry $`h^*_{mn}`$ expand in Lichnerowicz eigenmodes $`Y^{(I)}_{mn}`$,
``` math
\begin{equation}
h_{mn}(x,y)=h^*_{mn}(y)+\sum_I \phi^I(x)\,Y^{(I)}_{mn}(y).
\end{equation}
```
The $`\phi^I`$ are 4D scalars (moduli). Gap terms lift some or all of them.

## KK mode expansions

For a generic field $`\Phi(x,y)`$,
``` math
\begin{equation}
\Phi(x,y)=\sum_n \varphi_n(x)\,Y_n(y),\qquad -\Delta Y_n=\lambda_n\,Y_n,\qquad m_n^2=\lambda_n/R_{\rm KK}^2.
\end{equation}
```

## Gauge and matter couplings

Overlap integrals over $`B_{\rm KK}`$ determine the 4D couplings:
``` math
\begin{equation}
g_{abc}\sim \int_{B_{\rm KK}}\!\mathrm{d}^dy\,\sqrt{h}\;Y_a(y)Y_b(y)Y_c(y).
\end{equation}
```

## Dimensional interpretation: compactification vs. projection

We now give a precise account of the two equivalent descriptions used in this series.

#### (A) Standard compactification (10D $`\to`$ 4D).

Write $`M_{10}=\mathbb{R}_t\times M_3\times B_6`$, with $`B_6`$ compact. Use the block form <a href="#eq:metric" data-reference-type="eqref" data-reference="eq:metric">[eq:metric]</a>, expand fields in harmonics on $`B_6`$, and integrate over $`B_6`$ to obtain the 4D effective theory.

#### (B) Spatial projection (9D $`\to`$ 3D).

Work on a constant-time slice $`\Sigma^9`$ and choose a *Riemannian submersion*
``` math
\pi_{\rm sp}:\ \Sigma^9\longrightarrow M_3,
```
with compact oriented six-dimensional fibers $`F_6=\pi_{\rm sp}^{-1}(x)`$. Let $`T\Sigma^9=\mathcal{H}\oplus\mathcal{V}`$ be the orthogonal horizontal/vertical split. An Ehresmann connection identifies $`\mathcal{H}`$ and defines horizontal lifts. In adapted coordinates
``` math
g_{\Sigma^9}=g_{M_3}+h_{mn}(y)\,(\mathrm{d}y^m+A^{(m)}{}_\mu\mathrm{d}x^\mu)(\mathrm{d}y^n+A^{(n)}{}_\nu\mathrm{d}x^\nu),
```
which is the KK metric <a href="#eq:metric" data-reference-type="eqref" data-reference="eq:metric">[eq:metric]</a> on $`\Sigma^9`$. Reattaching time gives $`M_{10}=\mathbb{R}_t\times\Sigma^9`$.

<div id="lem:dictionary" class="lemma">

**Lemma 1** (Zero-mode dictionary). Assume $`(F_6,h)`$ is compact and the background lies in the left-invariant sector on $`F_6`$. Then:

1.  Harmonic zero-modes on $`B_6`$ in (A) are in one-to-one correspondence with fiberwise constant horizontal sections in (B).

2.  The isometry-induced gauge bosons $`A^{(a)}{}_\mu`$ are obtained in both pictures by projecting $`g_{\mu m}`$ on Killing vectors $`\xi^{(a)m}`$; the kinetic matrix equals $`V_6^{-1}\!\int_{F_6}\sqrt{h}\,h_{mn}\,\xi^{(a)m}\xi^{(b)n}`$.

3.  The Planck mass and gauge couplings computed by fiber integration in (B) coincide with the $`B_6`$ integrals in (A).

</div>

<div class="proof">

*Proof.* (i) Left-invariance on $`F_6`$ restricts background tensors to a finite invariant basis; harmonic zero-modes are horizontal fiberwise constants. (ii) In both pictures $`g_{\mu m}`$ expands on the Killing frame, producing the same $`A^{(a)}{}_\mu`$ and inner product. (iii) Fubini’s theorem factorizes the time and fiber integrals, so reduced 4D couplings agree term-by-term with $`B_6`$ integration. ◻

</div>

<div id="prop:proj-compact" class="proposition">

**Proposition 2** (Projection–compactification equivalence). *Let $`\pi_{\rm sp}:\Sigma^9\to M_3`$ be a Riemannian submersion with compact fibers $`F_6`$, and assume the background and zero-modes lie in the left-invariant sector on $`F_6`$. Then (B) is equivalent, at background and zero-mode level, to (A) with $`B_6=F_6`$: (a) the KK metric is <a href="#eq:metric" data-reference-type="eqref" data-reference="eq:metric">[eq:metric]</a>; (b) the set of zero-modes and their masses/couplings coincide; (c) the 4D action from integrating over $`F_6`$ equals that from integrating over $`B_6`$.*

</div>

<div class="proof">

*Proof.* Combine Lemma <a href="#lem:dictionary" data-reference-type="ref" data-reference="lem:dictionary">1</a> with $`M_{10}=\mathbb{R}_t\times\Sigma^9`$ and <a href="#eq:metric" data-reference-type="eqref" data-reference="eq:metric">[eq:metric]</a>. Masses $`m_n^2=\lambda_n/R_{\rm KK}^2`$ depend only on the fiber spectrum and $`R_{\rm KK}`$; couplings follow from the same fiber integrals (see §<a href="#sec:4D" data-reference-type="ref" data-reference="sec:4D">5</a>). ◻

</div>

#### Triplet geometry and “one $`3`$D + internal $`(3{+}3)`$D.”

In the modal triplet setting, nine spatial directions organize as three orthogonal 3D bundles. Selecting *one* as the observed $`M_3`$, the remaining two combine into $`F_6`$: “every 3D point carries an internal $`(3{+}3)`$D fiber”, which is exactly the KK internal $`B_6`$.

#### Remarks on twisting/warping/boundaries.

Nontrivial fibrations (monodromies/Wilson lines) contribute to the effective gauging; warping alters fiber measures; orbifolds/boundaries project modes. The equivalence above persists at background/zero-mode level.

# FCC–KK Background Equivalence (Left-Invariant Sector)

<div class="definition">

**Definition 3** (Left-invariant ansatz). Let $`\{\omega^A\}`$ be a finite left-invariant basis of forms on $`B_{\rm KK}`$. A *left-invariant background* is one for which the metric, torsion (if any), gauge fields, and curvature tensors expand entirely on $`\{\omega^A\}`$ and their wedge products.

</div>

<div class="remark">

**Remark 4** (Nomizu and invariant cohomology). On nilmanifolds and many homogeneous spaces the left-invariant complex computes de Rham cohomology (Nomizu’s theorem ). In such cases, expanding $`\mathrm{d}H`$, $`\mathrm{Tr}R^2`$, $`\mathrm{Tr}F^2`$ and similar tensors on a left-invariant basis is *cohomologically complete*. This justifies the componentwise FCC analysis in explicit fixed-point examples.

</div>

<div id="def:FCC" class="definition">

**Definition 5** (Fixed-point compactification condition (FCC)). Fix integer data $`\mathbf{n}\in\mathbb{Z}^N`$ (fluxes/holonomies) and continuous parameters $`\bm{\lambda}\in\mathbb{R}^M`$ (radii/torsion constants). The *FCC* is the finite algebraic/Diophantine system
``` math
\begin{equation}
\label{eq:FCC}
\mathbf{F}(\bm{\lambda};\mathbf{n})=0,
\end{equation}
```
consisting of (i) componentwise background equations (Einstein and, where relevant, Bianchi/duality) projected on left-invariant bases, together with (ii) primitivity and (iii) quantization/integrality constraints.

</div>

<div id="prop:alg" class="proposition">

**Proposition 6** (Algebraic reduction). *In the left-invariant ansatz, the higher-dimensional background equations for $`M_4\times B_{\rm KK}`$ reduce exactly to the finite algebraic/Diophantine system <a href="#eq:FCC" data-reference-type="eqref" data-reference="eq:FCC">[eq:FCC]</a>.*

</div>

<div class="proof">

*Proof.* Each tensor (Ricci, stress tensors, topological densities) wedges and contracts to a finite combination of invariant basis elements; so do flux/holonomy contributions. Projecting yields a *finite* set of scalar equations in the expansion coefficients. Primitivity and quantization add linear/integral constraints. Conversely, a solution of <a href="#eq:FCC" data-reference-type="eqref" data-reference="eq:FCC">[eq:FCC]</a> reconstructs all tensors as invariant combinations obeying the background equations. No PDE remains. ◻

</div>

<div id="thm:equiv" class="theorem">

**Theorem 7** (FCC–KK equivalence (background level)). *Let $`B_{\rm KK}`$ admit a left-invariant basis and let the background lie in the left-invariant sector. Then any left-invariant solution of the higher-dimensional equations is a solution of <a href="#eq:FCC" data-reference-type="eqref" data-reference="eq:FCC">[eq:FCC]</a>, and any solution of <a href="#eq:FCC" data-reference-type="eqref" data-reference="eq:FCC">[eq:FCC]</a> yields a left-invariant background solving the higher-dimensional equations.*

</div>

<div class="proof">

*Proof.* Forward: project a solution on the finite basis to obtain <a href="#eq:FCC" data-reference-type="eqref" data-reference="eq:FCC">[eq:FCC]</a>. Converse: given $`(\bm{\lambda},\mathbf{n})`$ solving <a href="#eq:FCC" data-reference-type="eqref" data-reference="eq:FCC">[eq:FCC]</a>, assemble tensors from invariant coefficients; the equations hold componentwise on the spanning basis. ◻

</div>

<div id="cor:implicit" class="corollary">

**Corollary 8** (Local existence/uniqueness). *Assume $`\mathbf{F}`$ is $`C^1`$ in $`\bm{\lambda}`$ for fixed $`\mathbf{n}`$ and the Jacobian $`\partial \mathbf{F}/\partial\bm{\lambda}`$ is invertible at $`(\bm{\lambda}_*,\mathbf{n}_*)`$. Then a unique solution branch $`\bm{\lambda}(\mathbf{n})`$ exists locally (implicit function theorem).*

</div>

<div class="remark">

**Remark 9** (Concrete illustrations). On Iwasawa the FCC reduces to one scalar equation fixing a radius in terms of integer flux data; on Lens$`\times`$Nil it fixes a ratio of radii in the invariant sector. See the companion fixed-point paper for coefficient-level solutions (explicit bases, integers, anomaly matching).

</div>

# Effective 4D Action from MTT

## Planck mass and Weyl frame

Define $`V_d=\int_{B_{\rm KK}}\mathrm{d}^dy\,\sqrt{h}`$. Reducing <a href="#eq:MTTaction" data-reference-type="eqref" data-reference="eq:MTTaction">[eq:MTTaction]</a> and rescaling to 4D Einstein frame yield
``` math
\begin{equation}
\label{eq:Mpl}
M_{\rm Pl}^2=\frac{V_d}{\kappa_D^2}.
\end{equation}
```

## Gravitational sector

The $`D`$-dimensional Ricci scalar splits as
``` math
\begin{equation}
\label{eq:Rsplit}
R_D=R_4+R_h-\frac14 h_{mn}F^{(m)}_{\ \mu\nu}F^{(n)\,\mu\nu}-\frac14 \mathrm{Tr}\!\big(h^{-1}\partial_\mu h\,h^{-1}\partial^\mu h\big)+\cdots,
\end{equation}
```
with $`F^{(m)}{}_{\mu\nu}=\partial_\mu A^{(m)}{}_\nu-\partial_\nu A^{(m)}{}_\mu+\cdots`$. Integration and Weyl rescaling give the 4D Einstein term, gauge kinetic terms from isometries, sigma-model terms for moduli, and a geometric potential from $`R_h`$ and Weyl terms.

## Gauge sector from isometries

Let $`\{\xi^{(a)}\}`$ generate $`G_{\rm KK}`$ with inner products
``` math
\begin{equation}
\label{eq:gammaab}
\gamma_{ab}=\frac{1}{V_d}\int_{B_{\rm KK}}\mathrm{d}^dy\,\sqrt{h}\,h_{mn}\,\xi^{(a)m}\xi^{(b)n}.
\end{equation}
```
From <a href="#eq:Rsplit" data-reference-type="eqref" data-reference="eq:Rsplit">[eq:Rsplit]</a> one finds
``` math
\begin{equation}
\label{eq:gaugecoupling}
S^{(4)}_{\rm gauge}=-\frac14\int\mathrm{d}^4x\,\sqrt{-g}\,\Big(\frac{M_{\rm Pl}^2}{2}\,\gamma^{ab}\Big)F^{(a)}_{\mu\nu}F^{(b)\,\mu\nu},\qquad \frac{1}{g_{ab}^2}=\frac{M_{\rm Pl}^2}{2}\,\gamma^{ab}.
\end{equation}
```
*Dimensional check.* With $`[\kappa_D^{-2}]=L^{-(D-2)}`$ and $`[V_d]=L^d`$, $`M_{\rm Pl}^2`$ has $`L^{-2}`$; $`\gamma^{ab}`$ is dimensionless. Hence $`g_{ab}`$ is dimensionless.

## Scalars and moduli

Write $`h_{mn}=h^*_{mn}+\sum_I \phi^I Y^{(I)}_{mn}`$. Then
``` math
\begin{equation}
S^{(4)}_{\rm moduli}=-\frac12\int\mathrm{d}^4x\,\sqrt{-g}\,G_{IJ}\,\partial_\mu\phi^I\partial^\mu\phi^J - \int\mathrm{d}^4x\,\sqrt{-g}\,V_{\rm mod}(\phi),
\end{equation}
```
with $`G_{IJ}`$ from the trace term in <a href="#eq:Rsplit" data-reference-type="eqref" data-reference="eq:Rsplit">[eq:Rsplit]</a> and $`V_{\rm mod}`$ induced by $`R_h`$ plus gap terms. The FCC typically fixes some ratios and may leave an overall scale at this order.

## Fermions and chirality

Internal eigenspinors of the Dirac operator $`D_h`$ give 4D spinors with masses $`m_r=|\lambda_r|/R_{\rm KK}`$; chiral zero-modes occur when $`{\rm index}(D_h)\neq 0`$, fixed by topology and bundle data on $`B_{\rm KK}`$.

## Topological terms

Higher-dimensional topological terms reduce to 4D Chern–Simons and $`\theta`$-like couplings with coefficients given by internal characteristic class integrals.

## Truncation consistency and gap control

Let $`\lambda_*>0`$ be the first nonzero eigenvalue of the relevant internal operator (Laplacian/Dirac/Lichnerowicz). Define
``` math
\begin{equation}
\label{eq:eps}
M_{\rm KK}:=\frac{\sqrt{\lambda_*}}{R_{\rm KK}},\qquad \varepsilon:=\frac{M_{\rm KK}}{\Lambda_{\rm gap}}\ll 1,
\end{equation}
```
where $`\Lambda_{\rm gap}`$ is the modal gap scale (MTT). Then mixings that source heavy modes are suppressed by $`\varepsilon`$ at tree level, justifying a zero-mode truncation. On homogeneous cosets $`B_{\rm KK}=G/H`$ the standard group-theoretic consistent truncation applies; the FCC selects the discrete invariant vacuum within that truncation.

# Mass Spectrum and Mode Expansion

## Eigenmodes and masses

Scalars: $`-\Delta_0Y_n=\lambda_n^{(0)}Y_n\Rightarrow m_n^2=M_D^2+\lambda_n^{(0)}/R_{\rm KK}^2`$. Coexact vectors: $`-\Delta_1Y^{(n)}_m=\lambda_n^{(1)}Y^{(n)}_m`$, $`\nabla^mY^{(n)}_m=0\Rightarrow m_n^2=\lambda_n^{(1)}/R_{\rm KK}^2`$. Dirac: $`D_h\eta_r=\lambda_r^{(1/2)}\eta_r\Rightarrow m_r=|\lambda_r^{(1/2)}|/R_{\rm KK}`$.

## Degeneracies and selection rules

If $`B_{\rm KK}`$ is homogeneous, harmonics furnish $`G_{\rm KK}`$ representations; overlap integrals obey Clebsch–Gordan selection rules.

## Mixings from curvature and background fields

Background curvature, torsion, and internal gauge backgrounds induce mixings among near-degenerate modes; the mass matrix schematically reads
``` math
M^2_{mn}=\frac{\lambda_n}{R_{\rm KK}^2}\delta_{mn}+\langle Y_m|\delta\mathcal{O}(R_h,\text{torsion},F;\text{gap})|Y_n\rangle.
```

## Examples

Flat $`T^d`$: $`\lambda_{\vec n}=(2\pi)^2\sum_i n_i^2/L_i^2\Rightarrow m^2_{\vec n}=\sum_i(2\pi n_i)^2/L_i^2+M_D^2`$. Sphere $`S^d(R)`$: $`\lambda_\ell^{(0)}=\ell(\ell+d-1)`$, $`m_\ell^2=\ell(\ell+d-1)/R^2+M_D^2`$.

## Chirality and index

Chiral 4D fermions correspond to zero-modes of $`D_h`$ with $`{\rm index}(D_h)=\int_{B_{\rm KK}}\widehat{A}(TB_{\rm KK})\wedge \mathrm{ch}(V)`$, fixed by internal topology and bundle data.

# Gauge Coupling Structure

## Isometry–gauge correspondence

Zero-mode gauge bosons originate from internal metric components along Killing vectors of $`B_{\rm KK}`$. Equations <a href="#eq:gammaab" data-reference-type="eqref" data-reference="eq:gammaab">[eq:gammaab]</a>–<a href="#eq:gaugecoupling" data-reference-type="eqref" data-reference="eq:gaugecoupling">[eq:gaugecoupling]</a> give the 4D kinetic matrix and couplings.

## Higher-dimensional gauge fields

If $`D`$-dimensional Yang–Mills fields are present, singlet internal profiles supply additional gauge factors with $`g_{n,4D}^{-2}=V_d\,g_{n,D}^{-2}`$.

## Unification patterns and kinetic mixing

In symmetric compactifications (e.g. cosets) $`\gamma_{ab}\propto\delta_{ab}`$ and gauge couplings unify at $`\mu=M_{\rm KK}`$. For anisotropic $`B_{\rm KK}`$, $`\gamma_{ab}`$ can be non-diagonal; diagonalization fixes physical couplings and generator alignments. The FCC fixes the moduli entering $`\gamma_{ab}`$ at the compactification point, so $`g_{ab}(\mu=M_{\rm KK})`$ are predicted numbers.

# Phenomenology and Symmetry Breaking

## Sources of symmetry breaking

Symmetry breaking can arise from scalar vevs, geometric asymmetries of $`B_{\rm KK}`$, Wilson lines, flux backgrounds, and orbifold/boundary projections. The FCC constrains which patterns are compatible.

## Hierarchy of scales

Key scales: $`M_{\rm Pl}\sim V_d^{1/2}/\kappa_D`$, $`M_{\rm KK}\sim 1/R_{\rm KK}`$, $`\Lambda_{\rm gap}\gg M_{\rm KK}`$. The FCC correlates $`R_{\rm KK}`$ with gap parameters.

## Chirality and families

Anomaly-safe chiral spectra follow from the index; superselection integers fix family number (e.g. $`N_{\rm chiral}=3`$ in SM-like sectors).

## Thresholds and running

Below $`M_{\rm KK}`$, standard RG running applies from initial conditions set by <a href="#eq:gaugecoupling" data-reference-type="eqref" data-reference="eq:gaugecoupling">[eq:gaugecoupling]</a>; threshold corrections are controlled by $`\varepsilon`$ in <a href="#eq:eps" data-reference-type="eqref" data-reference="eq:eps">[eq:eps]</a>.

# Conclusion and Outlook

#### Summary.

We have shown that, in the left-invariant sector, MTT’s fixed point selects KK backgrounds via a finite algebraic/Diophantine system—the FCC—which is equivalent to the higher-dimensional background equations. The 4D Planck mass, gauge couplings, and mass spectra are geometric invariants determined by the selected $`B_{\rm KK}`$ and $`R_{\rm KK}`$. We proved that the 9D$`\to`$<!-- -->3D projection language used in the fixed-point series is equivalent to the standard 10D$`\to`$<!-- -->4D compactification at background/zero-mode level.

#### Outlook.

Combining this with explicit matter sectors and specific $`B_{\rm KK}`$ (e.g. group/coset manifolds) yields phenomenology-ready models. The companion fixed-point constructions supply detailed exemplars where the FCC is solved at the coefficient level; the same template extends to other settings.

# Projection formalism cheat-sheet

#### Data.

A Riemannian submersion $`\pi_{\rm sp}:\Sigma^9\to M_3`$ with compact fiber $`(F_6,h)`$, horizontal distribution $`\mathcal{H}`$ (Ehresmann connection), vertical distribution $`\mathcal{V}=\ker\,\mathrm{d}\pi_{\rm sp}`$.

#### Metric.

In horizontal/vertical adapted frames,
``` math
g_{\Sigma^9}=g_{M_3}+h_{mn}(y)\,(\mathrm{d}y^m + A^{(m)}{}_\mu\,\mathrm{d}x^\mu)(\mathrm{d}y^n + A^{(n)}{}_\nu\,\mathrm{d}x^\nu).
```

#### Gauge bosons.

Expand $`A^{(m)}{}_\mu`$ on Killing vectors $`\xi^{(a)m}(y)`$: $`A^{(m)}{}_\mu = A^{(a)}{}_\mu\,\xi^{(a)m} + \cdots`$. Then
``` math
\frac{1}{g_{ab}^2}=\frac{M_{\rm Pl}^2}{2}\,\gamma^{ab},\qquad
\gamma_{ab}=\frac{1}{V_6}\int_{F_6}\!\sqrt{h}\,h_{mn}\,\xi^{(a)m}\xi^{(b)n},
```
identical to the compactification formula <a href="#eq:gaugecoupling" data-reference-type="eqref" data-reference="eq:gaugecoupling">[eq:gaugecoupling]</a>.

#### Masses.

Zero-modes: fiberwise constant harmonics on $`F_6`$; KK tower: $`m_n^2=\lambda_n/R_{\rm KK}^2`$, with $`\lambda_n`$ eigenvalues on $`F_6`$.

#### FCC.

In left-invariant backgrounds the higher-dimensional equations reduce to a finite algebraic/Diophantine system in fiber radii/torsion constants and integer data (flux/holonomy). Solving this system *selects* the background, independent of whether one speaks the compactification or projection language (Thm. <a href="#thm:equiv" data-reference-type="ref" data-reference="thm:equiv">7</a>).

<div class="thebibliography">

99

T. Kaluza, *Zum Unitätsproblem der Physik*, Sitzungsber. Preuss. Akad. Wiss. Berlin (Math. Phys.) (1921) 966–972.

O. Klein, *Quantentheorie und fünfdimensionale Relativitätstheorie*, Z. Phys. **37** (1926) 895–906.

M. J. Duff, B. E. W. Nilsson and C. N. Pope, *Kaluza–Klein Supergravity*, Phys. Rept. **130** (1986) 1–142.

T. Appelquist, A. Chodos and P. G. O. Freund (eds.), *Modern Kaluza–Klein Theories*, Addison–Wesley (1987).

I. Chavel, *Eigenvalues in Riemannian Geometry*, Academic Press (1984).

K. Nomizu, *On the cohomology of compact homogeneous spaces*, Ann. Math. **59** (1954) 531–538.

P. Nero, *Fixed-Point Flux Compactifications in Heterotic String Theory: Explicit Solutions on the Iwasawa Manifold and Lens$`\times`$Nil Geometries* (2025).

P. Nero. *Modal Triplet Theory: Foundation* Zenodo, 2025.

P. Nero. *Fixed Points VI: Formal Synthesis and Physical Interpretations* Zenodo, 2025.

</div>

[^1]: For explicit fixed-point compactifications (Iwasawa and Lens$`\times`$Nil) solved coefficient-by-coefficient in a left-invariant basis, see the companion work on heterotic fixed points; we reference it for context, but do not import string-specific formulae.

[^2]: *Two-of-three rule.* Only two family indices may be simultaneously active in any local interaction monomial in the internal sector, ensuring anomaly-safe representations and forbidding dangerous cubic couplings. At 4D level it induces selection rules in overlap integrals but does not modify the KK reduction.
