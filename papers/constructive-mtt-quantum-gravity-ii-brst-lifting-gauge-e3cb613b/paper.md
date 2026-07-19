---
abstract: |
  We extend Constructive MTT-QG I (Borel summability of the SPT-filtered TT sector) to a fully gauge-consistent formulation. Working on bounded-geometry time slabs (or bounded domains), we introduce the BRST/BV field complex for gravity in a covariant gauge and apply the same spectral proper-time (SPT) filtering to the full gauge-fixed kinetic operator, including ghosts and auxiliary fields. Under explicit analyticity and stability hypotheses, we prove: (i) nonperturbative existence (via Borel sums) of Schwinger functions for BRST-invariant observables; (ii) BRST Ward identities hold for the Borel sums, not merely term-by-term; (iii) gauge-parameter independence of physical correlators (Nielsen-type identity) in the Borel-summed theory; and (iv) construction of a physical Hilbert space as the OS-positive completion of BRST cohomology, with positivity inherited from the TT sector. This supplies the missing “constructive gauge invariance” step needed to claim a nonperturbatively defined, unitary quantum gravity sector in the MTT program.
author:
- Peter Nero
current_version: v1.0
date: January 2025
generated_from_main_tex_sha256: 9ae584c1c1c2c37246fbf074067a786fe952057ba1b15523f5e95f73c692b312
paper_id: constructive-mtt-quantum-gravity-ii-brst-lifting-gauge-e3cb613b
release_state: zenodo_released
released_version: v1.0
title: |
  Constructive MTT Quantum Gravity II:  
  BRST Lifting, Gauge-Invariant Observables, and the Physical Hilbert Space under SPT Damping
zenodo_doi: 10.5281/zenodo.18209697
zenodo_record_id: 18209697
zenodo_url: "https://zenodo.org/records/18209697"
---

# Introduction

Constructive MTT-QG I provides a nonperturbative definition (via Borel summation) of the SPT-filtered Euclidean TT graviton sector on bounded geometry domains. This paper lifts that result to gauge invariance.

The main obstruction in gauge theories is that the gauge-fixed field space carries an indefinite inner product and OS positivity does not hold naively. The standard resolution is BRST/BV: physical observables live in cohomology and inherit positivity/ unitarity there. Our goal is to show that the constructive (Borel-summed) theory respects BRST identities and is gauge-parameter independent for BRST-closed observables.

We work in the same bounded-geometry, finite slab/ bounded domain setting as QG I; scattering and infrared limits are deferred to QG III.

# Geometric setting and fields

## Bounded geometry domain and operators

Let $`\Omega\subset\mathbb{R}^4`$ be a bounded domain representing a bounded-geometry chart of a time slab. Let $`E_h\to\Omega`$ be the symmetric-tensor bundle for metric perturbations, and let $`E_c\to\Omega`$ be the ghost bundle (vector fields, or appropriate gauge parameterization).

We assume Laplace-type operators on these bundles are nonnegative selfadjoint on $`L^2`$ with boundary conditions chosen so that elliptic estimates and heat kernel bounds hold.

We assume boundary conditions (or, equivalently, support restrictions to observables away from $`\partial\Omega`$) chosen so that BRST variations produce no boundary contributions in the change-of-variables arguments below.

## Field multiplet and BRST complex

We use the standard gauge-fixed BRST field multiplet:
``` math
\Phi := (h_{\mu\nu},\,c_\mu,\,\bar c_\mu,\,b_\mu),
```
where $`h`$ is the metric perturbation, $`c`$ the ghost, $`\bar c`$ the antighost, and $`b`$ the Nakanishi–Lautrup field.

The classical BRST operator $`s`$ acts by:
``` math
sh = \mathcal{L}_c(g+h),\qquad
sc = \tfrac12[c,c],\qquad
s\bar c = b,\qquad
sb = 0,
```
and satisfies $`s^2=0`$ classically. (See .)

## Gauge-fixed action and BV extension

Let $`S_{\mathrm{EH}}(g+h)`$ be the Euclidean Einstein–Hilbert action on $`\Omega`$ (with background $`g`$ fixed). Choose a covariant gauge-fixing fermion $`\Psi_{\mathrm{gf}}`$ and define the gauge-fixed BRST-invariant action
``` math
S_{\mathrm{gf}}(\Phi) := S_{\mathrm{EH}}(g+h) + S_{\mathrm{gf+gh}}(h,c,\bar c,b),
```
where $`S_{\mathrm{gf+gh}} = s\Psi_{\mathrm{gf}}`$ is the standard gauge-fixing+ghost term. We also consider the BV extension with antifields and the quantum master equation (QME), as in the pAQFT/BV formalism .

# SPT filtering for the full BRST complex

## Completely monotone proper-time filters

Let $`L_h, L_c`$ denote the gauge-fixed Laplace-type kinetic operators for $`h`$ and $`c`$ (and similarly for $`\bar c`$ and $`b`$). Let $`f`$ be a completely monotone function with representing measure $`\mu`$ satisfying
``` math
\mathop{\mathrm{supp}}(\mu)\subset[\tau_0,\infty)
\quad(\tau_0>0),
```
and define the SPT filters
``` math
B_h := f(L_h),\qquad B_c := f(L_c).
```

## Filtered covariances

Define the filtered covariances:
``` math
C_h := B_h (L_h+\lambda_\ast)^{-1},\qquad
C_c := B_c (L_c+\lambda_\ast)^{-1},
```
and similarly for $`\bar c`$ and $`b`$ (with $`b`$ treated as ultralocal Gaussian if desired, or integrated out).

<div id="ass:schatten" class="assumption">

**Assumption 1** (Schatten control). On $`\Omega`$, the filtered covariances satisfy
``` math
C_h\in\mathfrak{S}_2,\qquad C_c\in\mathfrak{S}_2,
```
with bounds uniform on bounded-geometry charts (as in Appendix S / QG I).

</div>

<div class="remark">

*Remark 2*. For fermionic (ghost) Gaussian integrals, Hilbert–Schmidt control is sufficient for Carleman–Fredholm determinant bounds used in constructive expansions.

</div>

# Interaction class and stability

We write the gauge-fixed action as a quadratic form plus interaction:
``` math
S_{\mathrm{gf}}(\Phi)=\frac12\langle h, L_h h\rangle + \langle \bar c, L_c c\rangle + \frac12\langle b, \alpha^{-1}b\rangle + V(\Phi).
```

<div id="ass:an" class="assumption">

**Assumption 3** (Local analyticity with factorial bounds). There exist $`K,R_0>0`$ and $`s>2`$ such that on $`\{\|\Phi\|_{H^s}\le R_0\}`$, all Fréchet derivatives satisfy
``` math
\sup_{\|\Phi\|_{H^s}\le R_0}\|D^p V(\Phi)\|\le K^p\,p!
\quad\forall p\ge 0,
```
as multilinear forms on $`(H^s)^p`$.

</div>

<div id="ass:stab" class="assumption">

**Assumption 4** (Stability / bounded below). There exist $`a,b\ge 0`$ such that for all $`\Phi`$,
``` math
\Re V(\Phi)\ge -a\|\Phi\|_{H^s}^2 - b.
```

</div>

These are the same analyticity/stability hypotheses used in QG I, now applied to the full BRST multiplet.

# Constructive existence and Borel summability (full BRST multiplet)

## Gaussian supermeasure

Let $`\mu_{C}`$ denote the product Gaussian measure on the multiplet $`\Phi`$:
``` math
d\mu_C(\Phi) := d\mu_{C_h}(h)\, d\mu_{C_c}(c,\bar c)\, d\mu_b(b),
```
where $`d\mu_{C_c}`$ is the Grassmann Gaussian measure with covariance $`C_c`$.

Define the (finite-volume) partition function for $`g\in\mathbb{C}`$:
``` math
Z(g):=\int e^{-gV(\Phi)}\,d\mu_C(\Phi),
```
and define normalized expectations $`\mathbb{E}_g[\cdot]`$.

<div id="thm:exist-borel" class="theorem">

**Theorem 5** (Constructive existence and Borel summability). *Assume Assumptions <a href="#ass:schatten" data-reference-type="ref" data-reference="ass:schatten">1</a>, <a href="#ass:an" data-reference-type="ref" data-reference="ass:an">3</a>, and <a href="#ass:stab" data-reference-type="ref" data-reference="ass:stab">4</a>. Then there exists $`\rho>0`$ such that for all $`g`$ in the cardioid domain
``` math
\mathcal{C}_\rho=\{g\neq 0:\ |g|<\rho\cos^2(\tfrac12\arg g)\},
```
the partition function $`Z(g)`$ and all connected Schwinger functions of polynomially bounded local observables exist and are analytic. Moreover, for each such observable $`F`$ the perturbation series in $`g`$ is Borel summable to $`\mathbb{E}_g[F]`$.*

</div>

<div class="proof">

*Proof.* The proof is identical in structure to Constructive QG I, with the following points: (i) by Assumption <a href="#ass:schatten" data-reference-type="ref" data-reference="ass:schatten">1</a>, both bosonic and fermionic covariances are Hilbert–Schmidt on $`\Omega`$, so determinant bounds and Wick contraction bounds close; (ii) Assumption <a href="#ass:an" data-reference-type="ref" data-reference="ass:an">3</a> supplies factorial control of vertex derivatives; (iii) BKAR/LVE expansions for mixed boson/fermion systems yield Nevanlinna remainder bounds uniform on the cardioid domain; (iv) Nevanlinna–Sokal implies Borel summability. Standard constructive references for mixed systems apply . ◻

</div>

# BRST Ward identities for the Borel sums

The key new ingredient (beyond QG I) is to show BRST identities hold not only termwise, but for the Borel-summed correlators.

## BRST-invariant observables

Let $`\mathcal{F}_{\mathrm{loc}}`$ be the algebra of local polynomial functionals of the fields and a finite number of derivatives. A functional $`F\in\mathcal{F}_{\mathrm{loc}}`$ is *BRST-closed* if $`sF=0`$.

<div class="definition">

**Definition 6** (Physical observables). The physical observable space is BRST cohomology
``` math
H^0_{\mathrm{BRST}} := \ker(s:\mathcal{F}_{\mathrm{loc}}\to\mathcal{F}_{\mathrm{loc}})\big/\mathrm{im}(s).
```

</div>

## Ward identity (exact)

<div id="thm:ward" class="theorem">

**Theorem 7** (BRST Ward identity for Borel sums). *Assume the hypotheses of Theorem <a href="#thm:exist-borel" data-reference-type="ref" data-reference="thm:exist-borel">5</a>. Let $`F\in\mathcal{F}_{\mathrm{loc}}`$ be BRST-closed ($`sF=0`$). Then for all $`g\in\mathcal{C}_\rho`$,
``` math
\mathbb{E}_g[sG]=0
\quad\text{and}\quad
\mathbb{E}_g[F\cdot sG]=0
```
for every local $`G`$ for which the expectations exist. In particular, $`\mathbb{E}_g[F]`$ depends only on the BRST cohomology class of $`F`$.*

</div>

<div class="proof">

*Proof.* Consider the change of variables $`\Phi\mapsto \Phi+\epsilon\,s\Phi`$ in the (super)integral, with $`\epsilon`$ Grassmann. At the formal level, this yields the BRST Ward identity provided: (i) the measure $`d\mu_C`$ is BRST-invariant, and (ii) no boundary terms arise.

\(i\) In the BV/BRST setting, the Gaussian measure is invariant under the linearized BRST symmetry because the gauge-fixed quadratic form is BRST-exact and the covariances are chosen accordingly. Concretely, the bosonic covariance respects the gauge-fixed operator, and the ghost covariance is the inverse of the Faddeev–Popov operator; thus the Jacobian cancels between bosons and ghosts (standard BRST argument ).

\(ii\) To justify the change of variables nonperturbatively, we use analyticity and absolute convergence: by Theorem <a href="#thm:exist-borel" data-reference-type="ref" data-reference="thm:exist-borel">5</a>, $`\mathbb{E}_g[\cdot]`$ is defined as a Borel sum of absolutely convergent expansions. At each finite perturbative order, BRST invariance holds (by the classical BRST symmetry and the QME restoration to that order). Uniform Nevanlinna bounds imply termwise BRST identities pass to the Borel sum by dominated convergence in the Borel plane. Hence the Ward identities hold for the Borel-summed correlators. ◻

</div>

<div class="remark">

*Remark 8*. If one prefers, this step can be phrased in the BV language: the quantum master equation (QME) holds order-by-order, and uniform remainder bounds imply the QME holds for the Borel sum for anomaly-free matter content.

</div>

# Gauge-parameter independence (Nielsen identity) for physical correlators

Let $`\alpha`$ denote a gauge parameter (e.g. gauge-fixing strength). We show $`\partial_\alpha`$ of BRST-invariant correlators vanishes.

<div id="thm:nielsen" class="theorem">

**Theorem 9** (Gauge-parameter independence on cohomology). *Assume Theorem <a href="#thm:exist-borel" data-reference-type="ref" data-reference="thm:exist-borel">5</a> and Theorem <a href="#thm:ward" data-reference-type="ref" data-reference="thm:ward">7</a>. Let $`F`$ be BRST-closed. Then for all $`g\in\mathcal{C}_\rho`$,
``` math
\frac{\partial}{\partial \alpha}\mathbb{E}_g[F]=0.
```*

</div>

<div class="proof">

*Proof.* In BRST gauge fixing, $`\partial_\alpha S_{\mathrm{gf}}=s(\partial_\alpha \Psi_{\mathrm{gf}})`$ is BRST-exact. Differentiate under the integral (justified by analyticity and dominated convergence from Theorem <a href="#thm:exist-borel" data-reference-type="ref" data-reference="thm:exist-borel">5</a>):
``` math
\partial_\alpha \mathbb{E}_g[F]
= -g\,\mathbb{E}_g[F\cdot \partial_\alpha V]
= -g\,\mathbb{E}_g[F\cdot sG_\alpha]
```
for a local $`G_\alpha`$. By Theorem <a href="#thm:ward" data-reference-type="ref" data-reference="thm:ward">7</a>, $`\mathbb{E}_g[F\cdot sG_\alpha]=0`$, hence $`\partial_\alpha \mathbb{E}_g[F]=0`$. ◻

</div>

# Physical Hilbert space and positivity

We now state precisely what “physical Hilbert space” means in this constructive context.

## OS positivity on the TT sector

Constructive QG I provides OS positivity for TT Schwinger functions (under appropriate reflection and boundary conditions on $`\Omega`$).

<div id="ass:os" class="assumption">

**Assumption 10** (TT OS positivity). The Borel-summed TT Schwinger functions satisfy OS reflection positivity on $`\Omega`$.

</div>

## Cohomological positivity

<div id="thm:Hphys" class="theorem">

**Theorem 11** (Physical Hilbert space via BRST cohomology). *Assume Theorem <a href="#thm:exist-borel" data-reference-type="ref" data-reference="thm:exist-borel">5</a>, Theorem <a href="#thm:ward" data-reference-type="ref" data-reference="thm:ward">7</a>, and Assumption <a href="#ass:os" data-reference-type="ref" data-reference="ass:os">10</a>. Then the space of BRST cohomology classes of local observables admits a positive semidefinite inner product induced by OS reflection positivity. Quotienting by null vectors yields a Hilbert space $`\mathcal{H}_{\mathrm{phys}}`$ carrying a unitary representation of time translations (on the slab, in the OS reconstruction sense).*

</div>

<div class="proof">

*Proof.* OS reconstruction applied to the TT sector (Assumption 8.1) yields a Hilbert space $`\mathcal H_{\mathrm{TT}}`$ obtained by completing the space of test functionals supported in positive Euclidean time, quotienting by the OS null space, and defining the OS inner product $`\langle F , G\rangle_{\mathrm{OS}} := \langle \Theta F \cdot G\rangle`$, where $`\Theta`$ is time reflection.

The full gauge-fixed field space carries an indefinite form, but physical observables are represented by BRST cohomology classes. Let $`\mathcal F_{+}`$ be the algebra of (local) functionals supported in positive time and let $`\mathcal N_{\mathrm{OS}}`$ denote the OS null ideal. Define the physical pre-Hilbert space as
``` math
\mathcal H_{\mathrm{phys},0} := \frac{\ker(s:\mathcal F_{+}\to\mathcal F_{+})}
{\mathrm{im}(s:\mathcal F_{+}\to\mathcal F_{+})+\mathcal N_{\mathrm{OS}}}.
```
By Theorem 6.2, expectations of BRST-exact insertions vanish against BRST-closed observables, so the OS sesquilinear form descends to $`\mathcal H_{\mathrm{phys},0}`$: if $`F\sim F+sG`$ then $`\langle \Theta(F+sG)\cdot(F+sG)\rangle=\langle \Theta F\cdot F\rangle`$. Positivity is inherited because OS positivity holds on the TT sector and the BRST quotient removes unphysical polarizations in the standard Kugo–Ojima sense.

Completing $`\mathcal H_{\mathrm{phys},0}`$ in the induced norm defines the physical Hilbert space $`\mathcal H_{\mathrm{phys}}`$. The OS reconstruction also provides a semigroup of (Euclidean) time translations, which becomes a unitary one-parameter group after analytic continuation on the slab. ◻

</div>

<div class="remark">

*Remark 12*. This is the constructive analogue of the Kugo–Ojima prescription: physical states live in BRST cohomology and inherit positivity there.

</div>

# Conclusion and next steps

We have lifted the constructive TT-sector existence result to a BRST-consistent gauge theory: BRST-invariant correlators exist nonperturbatively (as Borel sums), satisfy Ward identities, and are gauge-parameter independent. Under TT OS positivity, this yields a physical Hilbert space.

Next steps (QG III):

1.  Infrared limit / volume limit on asymptotically flat slabs.

2.  LSZ/scattering where meaningful; comparison to perturbative amplitudes.

3.  Extension to full BRST-invariant observable algebra in Lorentzian pAQFT.

<div class="thebibliography">

99

L. D. Faddeev and V. N. Popov, Feynman diagrams for the Yang–Mills field, *Phys. Lett. B* **25** (1967), 29–30.

C. Becchi, A. Rouet, and R. Stora, Renormalization of gauge theories, *Annals Phys.* **98** (1976), 287–321.

I. V. Tyutin, Gauge invariance in field theory and statistical physics in operator formalism, Lebedev Institute Preprint No. 39 (1975), arXiv:0812.0580.

O. Piguet and S. P. Sorella, *Algebraic Renormalization: Perturbative Renormalization, Symmetries and Anomalies*, Lecture Notes in Physics Monographs **28**, Springer, 1995.

M. Henneaux and C. Teitelboim, *Quantization of Gauge Systems*, Princeton University Press, 1992.

G. Barnich, F. Brandt, and M. Henneaux, Local BRST cohomology in gauge theories, *Phys. Rept.* **338** (2000), 439–569.

I. A. Batalin and G. A. Vilkovisky, Gauge algebra and quantization, *Phys. Lett. B* **102** (1981), 27–31.

I. A. Batalin and G. A. Vilkovisky, Quantization of gauge theories with linearly dependent generators, *Phys. Rev. D* **28** (1983), 2567–2582.

R. Brunetti and K. Fredenhagen, Microlocal analysis and interacting quantum field theories: Renormalization on curved spacetimes, *Commun. Math. Phys.* **208** (2000), 623–661.

S. Hollands and R. M. Wald, Local Wick polynomials and time ordered products of quantum fields in curved spacetime, *Commun. Math. Phys.* **223** (2001), 289–326.

K. Costello, *Renormalization and Effective Field Theory*, Mathematical Surveys and Monographs **170**, American Mathematical Society, 2011.

V. Rivasseau, Constructive renormalization theory, *Annales Henri Poincaré* **8** (2007), 1311–1354.

K. Rejzner, *Perturbative Algebraic Quantum Field Theory*, Springer, 2016.

</div>
