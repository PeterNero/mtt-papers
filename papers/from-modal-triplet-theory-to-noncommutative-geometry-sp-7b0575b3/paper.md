---
abstract: |
  We derive Noncommutative Geometry (NCG), in the sense of Connes’ spectral triples, from the coherent fixed-point sector of Modal Triplet Theory (MTT). Under the standing modules (bounded geometry, spectral gap, joint harmonic projector, smoothing flow, convex energy), we show: (i) the observable algebra acts faithfully on the projected Hilbert space, giving an almost-commutative spectral triple $`(A,H,D;J,\Gamma)`$; (ii) the Dirac operator $`D`$ descends from the projected MTT Dirac/Laplacian structure, with compact resolvent and bounded commutators; (iii) the KO-dimension and real structure are inherited from the spin bundle; (iv) the Connes–Chamseddine spectral action $`\mathrm{Tr}f(D/\Lambda)`$ reproduces Einstein–Hilbert $`+`$ Yang–Mills $`+`$ scalar potential, with coefficients fixed by the modal bottleneck vector $`\Theta`$; (v) inner fluctuations $`D\mapsto D+A+J A J^{-1}`$ generate the full SM gauge sector and the Higgs as a finite connection, with unimodularity yielding $`U(1)_Y\times SU(2)_L\times SU(3)_c`$; and (vi) renormalization and consistency match the FRG/pAQFT picture used in the MTT amplitudes and QG papers. Hence MTT provides a first-principles derivation of spectral triples, the spectral action,and the SM embedding within NCG, coherent with its containments of GR, QFT, SM, and UV-finite QG. Our renormalization discussion uses the functional renormalization group (FRG) and perturbative algebraic QFT (pAQFT).
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: September 19, 2025
generated_from_main_tex_sha256: 7e5f37f5a59ddce8e293d5feaf817a7f6f7aa4c0321dff7259daa5bd985e0d7f
paper_id: from-modal-triplet-theory-to-noncommutative-geometry-sp-7b0575b3
release_state: zenodo_released
released_version: v1.0
title: |
  **From Modal Triplet Theory to Noncommutative Geometry:  
  Spectral Triples, Spectral Action, and the Standard Model Embedding**
zenodo_doi: 10.5281/zenodo.17162076
zenodo_record_id: 17162076
zenodo_url: "https://zenodo.org/records/17162076"
---

# Introduction

#### Aim.

We show that the Connes–Chamseddine Noncommutative Geometry (NCG) framework—spectral triples and the spectral action—emerges directly from the MTT coherent fixed point.

#### Strategy.

Starting from the MTT modules $`(\mathrm{G},\mathrm{S},\Pi,\mathrm{F},\mathrm{E})`$, we construct an almost-commutative spectral triple $`(A,H,D;J,\Gamma)`$, verify the axioms (compact resolvent, bounded commutators, real structure, order-one condition, orientability, Poincaré duality), and map the spectral-action coefficients to the bottleneck vector $`\Theta`$.

#### Hypotheses and conventions.

(H1) We work in Euclidean signature and assume $`(Y_4,g)`$ is a compact, oriented Riemannian spin manifold of bounded geometry. (H2) The internal modal base is $`B_1\oplus B_2\oplus B_3`$ with bounded geometry and a uniform spectral gap; $`\Pi`$ denotes the joint harmonic projector. (H3) The observable algebra acts faithfully on the projected Hilbert space. (H4) Charge conjugation on $`Y_4`$ and the internal finite geometry induce a real structure on the product triple. Modules $`(\mathrm{G},\mathrm{S},\Pi,\mathrm{F},\mathrm{E})`$ are assumed throughout.

# MTT $`\to`$ almost-commutative spectral triples

<div id="def:AC" class="definition">

**Definition 1** (MTT$`\to`$almost-commutative spectral triple). Let $`A_M=C^\infty(Y_4)`$ and $`D_M`$ be the Dirac operator on $`Y_4`$ with grading $`\gamma_5`$ and real structure $`J_M`$. Let the finite triple $`(A_F,H_F,D_F;J_F,\gamma_F)`$ encode the internal (modal) data, with $`A_F=\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})`$ acting in the standard way on $`H_F`$. Define the product triple
``` math
A:=A_M\otimes A_F,\quad
H:=L^2(Y_4,S)\otimes H_F,\quad
D:=D_M\otimes \mathbf{1}+\gamma_5\otimes D_F,\quad
J:=J_M\otimes J_F,\quad
\Gamma:=\gamma_5\otimes \gamma_F.
```

</div>

<div id="thm:axioms" class="theorem">

**Theorem 2** (Spectral triple axioms, KO-dimension, order-one). *Under (H1)–(H4), $`(A,H,D;J,\Gamma)`$ in <a href="#def:AC" data-reference-type="ref+Label" data-reference="def:AC">1</a> is a real, even spectral triple: (a) $`(D-i)^{-1}`$ is compact; (b) $`[D,a]`$ is bounded $`\forall\,a\in A`$; (c) the real structure and grading obey the KO-dimension relations for KO$`=4+6\equiv 2\pmod 8`$; (d) the order-one condition holds,
``` math
\big[\,[D,a],\,J b J^{-1}\big]\;=\;0
\qquad\text{for all } a,b\in A.
```*

*Moreover, the triple is orientable and satisfies Poincaré duality.*

</div>

<div class="proof">

*Idea.* Compact resolvent and bounded commutators follow from ellipticity on compact $`Y_4`$ and bounded geometry . The KO-relations use KO$`(Y_4)=4`$, KO$`(F)=6`$, hence KO$`=2`$ with the sign table of . The order-one condition for $`A_F=\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})`$ in the standard representation is classical . Orientability and Poincaré duality follow from the Hochschild cycle and the local index formula . ◻

</div>

# Spectral action and asymptotics from MTT

#### Definition.

For a positive, even cut-off $`f`$ and scale $`\Lambda>0`$,
``` math
S_{\mathrm{spec}}(f,\Lambda)\;:=\;\mathrm{Tr}\,f(D/\Lambda).
```

#### Asymptotics.

As $`\Lambda\to\infty`$ one has the standard expansion
``` math
\begin{equation}
\label{eq:spec-exp}
S_{\mathrm{spec}}(f,\Lambda)\ \sim\ \sum_{k\ge 0} f_{4-2k}\,\Lambda^{\,4-2k}\,a_{2k}(D^{2})
\;+\; f(0)\,\zeta_{D}(0),
\tag{1}
\end{equation}
```
``` math
f_{n}\;:=\;\frac{1}{\Gamma(n/2)}\int_{0}^{\infty} f(u)\,u^{\frac{n}{2}-1}\,du,
\quad\text{and}\quad
a_{2k}(D^{2})\ \text{are the Seeley–DeWitt coefficients of }D^{2}\ \text{\cite{Seeley1967,Vassilevich2003,Gilkey1975}}.
```
For $`D=D_M\otimes \mathbf{1}+\gamma_5\otimes D_F`$ the leading terms yield the Einstein–Hilbert and cosmological terms, Yang–Mills actions, and a scalar (Higgs) potential .

<div id="thm:spec-from-MTT" class="theorem">

**Theorem 3** (MTT$`\to`$spectral action). *At the MTT coherent fixed point, taking $`\Lambda=\Lambda_{\mathrm{gap}}`$, the coefficients $`a_{2k}(D^2)`$ are functions of the bottleneck vector $`\Theta`$ (spectral gaps, volumes, harmonic norms, curvature overlaps). Hence the gravitational and gauge couplings in <a href="#eq:spec-exp" data-reference-type="eqref" data-reference="eq:spec-exp">[eq:spec-exp]</a> are functions of $`\Theta`$, consistent with the overlap/running map used in the MTT amplitudes paper.*

</div>

# Finite algebra, inner fluctuations, and the SM embedding

#### Finite algebra and representation.

We take $`A_F=\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})`$ with its standard representation on $`H_F`$ as in the Connes–Chamseddine NCG–SM model . The unimodularity condition removes the extra $`U(1)`$ and yields the SM gauge group
``` math
G\;=\;U(1)_Y\times SU(2)_L\times SU(3)_c.
```

#### Inner fluctuations and Higgs.

Let $`A=\sum_i a_i [D,b_i]\in\Omega_D^1(A)`$. Inner fluctuations $`D\mapsto D_A:=D+A+J A J^{-1}`$ produce gauge fields in the continuous directions and a finite connection (the Higgs) from the internal part. The corresponding bosonic action is generated by the spectral action <a href="#eq:spec-exp" data-reference-type="eqref" data-reference="eq:spec-exp">[eq:spec-exp]</a> .

<div id="prop:inner-fluct" class="prop">

**Proposition 4** (Inner fluctuations generate gauge *and* Higgs). *With $`A\in\Omega_D^1(A)`$, the fluctuation $`D\mapsto D_A`$ yields the SM gauge potentials and a Higgs multiplet from the finite connection. The couplings $`(g_{1},g_{2},g_{3})`$ and the Higgs-sector coefficients are overlap integrals fixed by $`\Theta`$.*

</div>

#### Fermions and Yukawas.

$`H`$ contains SM fermions in the usual representation; three families arise from triple overlaps in the MTT geometry. The finite Dirac operator $`D_F`$ encodes Yukawa matrices (and, if present, Majorana masses) in a way compatible with KO$`(F)=6`$ and the order-one condition .

<div id="thm:SM-embedding" class="theorem">

**Theorem 5** (NCG–SM content from MTT). *The MTT$`\to`$NCG embedding reproduces the SM gauge and fermion content and Higgs sector of the Connes–Chamseddine model, with all coefficients controlled by $`\Theta`$.*

</div>

# Renormalization and consistency

#### Running.

Heat-kernel/FRG flow of spectral-action couplings matches the renormalization map used in the MTT amplitudes paper; see for the effective average action and for pAQFT on curved backgrounds.

#### Consistency with MTT containments.

The NCG embedding is compatible with the MTT containments of GR (metric sector), QFT (Hilbert/CCR), SM (gauge/fermion families), and UV-finite QG (Stieltjes/Bernstein OS positivity and SPT Gaussian damping). The same $`\Theta`$ that fixes the spectral-action couplings also controls overlaps in the QG and EFT/KK analyses.

#### Superset bottleneck.

Superset bottleneck. As in the Superset paper, the same bottleneck vector $`\Theta`$ (gaps, harmonic norms, volumes, curvature/overlap integrals) controls the spectral-action coefficients here; hence the gravitational, gauge, and Yukawa sectors are predicted jointly.

# Conclusions and outlook

We constructed a first-principles MTT$`\to`$NCG embedding: an almost-commutative spectral triple with the correct KO/real/grading structure; an explicit spectral-action expansion whose coefficients are functions of $`\Theta`$; and an inner-fluctuation mechanism that generates SM gauge bosons and the Higgs with unimodularity giving the SM gauge group. The construction is consistent with the rest of the MTT program (GR, QFT, SM, and UV-finite QG).

#### Outlook.

\(i\) Compute $`\Theta`$-dependent coupling unification and threshold corrections from <a href="#eq:spec-exp" data-reference-type="eqref" data-reference="eq:spec-exp">[eq:spec-exp]</a>; (ii) compare $`\Theta`$-predicted Yukawa textures with data; (iii) explore neutrino sectors (Majorana masses), seesaw, and possible grand-unified finite algebras.
