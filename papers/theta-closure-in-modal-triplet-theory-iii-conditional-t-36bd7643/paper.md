---
abstract: |
  We audit a conditional Route B representation of the leading–order nonabelian overlap integrals $`I_2^{(0)}`$ and $`I_3^{(0)}`$ in Modal Triplet Theory (MTT) using the self–dual Yang–Mills (SDYM) twistor corner. Fiber reduction gives the same quadratic $`L^2`$ functional used by Route A. The numerical normalization is not independent, however: the $`SU(2)`$ result additionally uses the bridge convention $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$ and the effective round-$`S^2`$ lens model, while the $`SU(3)`$ result uses the declared auxiliary nilmanifold, color harmonic, and factorization assumption of Paper II. Under these declared shared inputs Route B reproduces $`I_2^{(0)}=4\pi(f_2R_{\mathrm{lens}})^2`$ and $`I_3^{(0)}=\int\|\chi_{\mathrm{col}}\|^2d\mu=c`$. The result is therefore a conditional representation-level cross-check, not an independent selection of the overlap values or a completed nonabelian $`\Theta`$–closure theorem.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: d7134be2a7ebfd2c17fd1c6c366db5a6e6b63bec10321c2ffbf705f2d7f06dd7
paper_id: theta-closure-in-modal-triplet-theory-iii-conditional-t-36bd7643
release_state: zenodo_released
released_version: v1.0
title: "Theta Closure in Modal Triplet Theory III: Conditional Twistor–Action Matching and Normalization Audit"
zenodo_doi: 10.5281/zenodo.18262098
zenodo_record_id: 18262098
zenodo_url: "https://zenodo.org/records/18262098"
---

# Revision note for this edition

Supersedes.  
*Theta Closure in Modal Triplet Theory III: Twistor Action Matching and Independent Normalization*, first edition.

Reason.  
Route B was described as an independent normalization although its area convention, effective lens model, nil harmonic, and factorization were inherited from Route A.

Resolution.  
Version 2 exposes every shared input and proves only the conditional SDYM-to-quadratic-$`L^2`$ representation match.

Retained result.  
Under those declared bridge conventions, the twistor and direct descriptions reproduce the same leading overlap functionals.

Remaining boundary.  
An independently selected normalization or q79 source theorem is still required for redundant closure evidence.

# Relation to Papers I and II

This paper is the third component of the conservative $`\Theta`$–closure program:

- **Paper I** defines the selected common-scheme gauge profile and the corresponding overlap-ratio targets.

- **Paper II** realizes those targets in a calibrated effective round-$`S^2`$/nilmanifold ansatz (Route A).

- **Paper III** tests whether the same quadratic overlap functional is reproduced by the twistor–encoded gauge action (Route B), and audits which normalization inputs remain shared with Route A.

Agreement between Routes A and B is a conditional internal consistency check. It is not statistically or logically independent evidence when the routes share the internal metric, harmonic, normalization bridge, or target profile.

# Introduction

Modal Triplet Theory (MTT) proposes that observable four–dimensional physics arises from a coherent projection of a higher–dimensional modal configuration space. In this framework, inverse squared gauge couplings are represented by overlap integrals of internal harmonic representatives. Whether the values of those integrals are selected by MTT geometry or calibrated to an observed profile is a separate theorem question.

Paper I transports the measured Standard Model gauge profile in a common scheme to $`Q=M_t=172.5590883453979~\mathrm{GeV}`$. Paper II maps the resulting ratios into an auxiliary Lens–Nil operator model: a round-$`S^2`$ effective lens base and a compact Heisenberg nilmanifold, with one shared $`U(1)`$ phase/holonomy datum reused across the lanes. It does not use the seven-dimensional product $`S^1_{\mathrm{cen}}\times L(3,1)\times
\Gamma\backslash\mathrm{Nil}_3`$. Its parameters constitute a calibrated ansatz-level realization, not a unique geometry selection or an identification with the selected q79/Fu–Yau compactification.

The purpose of this paper is to determine precisely what the twistor–action construction (Route B) adds. Unlike Route A, it represents the quadratic gauge norm through fiber reduction of an SDYM action. It does not, by itself, select the map from the Fubini–Study form to the effective lens area, the internal color fiber, or the color harmonic. Those bridges are stated as assumptions rather than hidden inside a claim of independent normalization.

We show that:

- twistor fiber reduction produces a quadratic $`L^2`$ norm of the massless representative;

- the declared direction-sphere bridge recovers the $`4\pi`$ coefficient used by the effective $`SU(2)`$ lens-base model;

- the selected color factorization reproduces the nilmanifold $`SU(3)`$ overlap functional; and

- numerical equality with Route A is conditional on these shared inputs, while a quantitative bound on omitted coherence corrections remains open.

The result is a representation-level compatibility theorem, not an independent value source or a completed nonabelian $`\Theta`$–closure theorem.

# Twistor corner and SDYM action

## High–coherence twistor regime

The twistor formulation of MTT identifies a high–coherence regime in which the effective dynamics of the massless gauge sector reduces to self–dual Yang–Mills (SDYM) theory encoded holomorphically on twistor space.

<div class="assumption">

**Assumption 1** (Twistor–corner regime). We assume the matching scale $`\mu_\Theta`$ lies in the high–coherence regime for the massless gauge sector, so that:

1.  SDYM provides the leading–order gauge dynamics;

2.  massive corrections are suppressed by $`O(\lambda_Q^{-1})`$;

3.  the twistor action yields a well–defined kinetic normalization.

</div>

## Twistor action for SDYM

The SDYM action admits a twistor–space formulation of the form
``` math
S_{\mathrm{tw}} = \frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathbb{PT}} \mathrm{Tr}\big(F^{(0,2)}\wedge \star F^{(0,2)}\big),
```
where:

- $`\mathbb{PT}`$ is the relevant region of projective twistor space,

- $`F^{(0,2)}`$ is the holomorphic curvature,

- $`g_{\mathrm{tw}}`$ is the twistor–action coupling.

The normalization of $`g_{\mathrm{tw}}`$ determines the effective four–dimensional gauge kinetic term upon reconstruction.

# Reconstruction of the four–dimensional gauge action

## Ward correspondence and spacetime fields

By the Ward correspondence, holomorphic vector bundles on twistor space correspond to SDYM solutions on spacetime. The reconstruction map yields a spacetime gauge field $`A_\mu`$ whose kinetic term is obtained by integrating over the twistor fiber.

At leading order, this produces a four–dimensional action
``` math
S_{\mathrm{4d}} = \frac{1}{4g_{\mathrm{eff}}^2}
\int_{Y^4} F_{\mu\nu}F^{\mu\nu}\,d\mathrm{vol}_4.
```

## Matching of couplings

The effective coupling $`g_{\mathrm{eff}}`$ is related to the twistor coupling $`g_{\mathrm{tw}}`$ by
``` math
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathcal F} \langle \psi, \psi\rangle\,d\mu_{\mathcal F},
```
where:

- $`\mathcal F`$ is the internal fiber associated with the gauge sector,

- $`\psi`$ is the period/bridge-normalized twistor harmonic corresponding to the massless mode, with any gauge-kinetic weight included in the displayed measure.

This integral is the twistor analogue of the internal overlap integral $`I_a^{(0)}`$ defined in Papers I and II.

# Identification of $`I_2^{(0)}`$ and $`I_3^{(0)}`$

## General matching principle

Comparing the twistor reconstruction with the overlap formulation
``` math
\frac{1}{g_a^2} = \frac{1}{g_{10}^2} I_a,
```
we identify
``` math
I_a^{(0)} \;\equiv\;
\int_{\mathcal F_a}
w_a^{(0)}\langle \psi_a^{(0)}, \psi_a^{(0)}\rangle\,
d\mu_{\mathcal F_a},
```
where $`\psi_a^{(0)}`$ is the massless twistor harmonic for the $`SU(a)`$ sector.

## $`SU(2)`$ sector: conditional Route B normalization

We evaluate the Route B quadratic norm for the $`SU(2)`$ sector. This avoids the internal spectral estimate used in Route A, but the numerical coefficient still depends on the coupling and direction-sphere bridge conventions stated below.

### Twistor fiber normalization

In the high–coherence twistor corner, each spacetime point $`x\in Y^4`$ corresponds to a twistor line $`L_x\cong\mathbb{CP}^1`$. We equip $`L_x`$ with the standard Fubini–Study Kähler form $`\omega_{\mathrm{FS}}`$ normalized by
``` math
\begin{equation}
\int_{L_x}\omega_{\mathrm{FS}} = 2\pi.
\label{eq:FS_norm}
\end{equation}
```
This convention fixes the fiber measure once chosen. It does not by itself fix the relative normalization between $`g_{\mathrm{tw}}`$, $`g_{10}`$, and the internal MTT overlap.

### Twistor SDYM action

The self–dual Yang–Mills action in twistor space is taken to be
``` math
\begin{equation}
S_{\mathrm{tw}}[{\cal A}]
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathbb{PT}}
\mathrm{Tr}\!\left(
{\cal F}^{(0,2)}\wedge \star {\cal F}^{(0,2)}
\right),
\label{eq:twistor_action_SU2}
\end{equation}
```
where $`{\cal A}`$ is a $`(0,1)`$ connection on a rank–2 holomorphic bundle over $`\mathbb{PT}`$ and $`{\cal F}^{(0,2)}`$ is its $`(0,2)`$ curvature. The normalization of $`g_{\mathrm{tw}}`$ is fixed once <a href="#eq:FS_norm" data-reference-type="eqref" data-reference="eq:FS_norm">[eq:FS_norm]</a> is chosen.

### Reconstruction to spacetime

By the Ward correspondence, solutions of the twistor field equations correspond to self–dual Yang–Mills fields on spacetime. Linearizing <a href="#eq:twistor_action_SU2" data-reference-type="eqref" data-reference="eq:twistor_action_SU2">[eq:twistor_action_SU2]</a> about the trivial bundle and restricting to the massless sector yields a four–dimensional action
``` math
\begin{equation}
S_{4}[A]
=
\frac{1}{4g_{\mathrm{eff}}^2}
\int_{Y^4} F_{\mu\nu}F^{\mu\nu}\,d\mathrm{vol}_4,
\label{eq:4d_SU2}
\end{equation}
```
where the effective coupling is given by a fiber integral:
``` math
\begin{equation}
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{L_x}
\|\psi^{(0)}\|^2\,d\mu_{L_x}.
\label{eq:SU2_fiber_norm}
\end{equation}
```
Here $`\psi^{(0)}`$ is the massless twistor harmonic corresponding to the $`SU(2)`$ gauge zero mode.

### Evaluation of the fiber integral

For the $`SU(2)`$ sector, the massless twistor harmonic $`\psi^{(0)}`$ is constant along the fiber and normalized so that
``` math
\|\psi^{(0)}\|_{L^2(L_x)}^2
=
\int_{L_x}\|\psi^{(0)}\|^2\,d\mu_{L_x}
=
\int_{L_x}\omega_{\mathrm{FS}}
=
2\pi,
```
by <a href="#eq:FS_norm" data-reference-type="eqref" data-reference="eq:FS_norm">[eq:FS_norm]</a>. Substituting into <a href="#eq:SU2_fiber_norm" data-reference-type="eqref" data-reference="eq:SU2_fiber_norm">[eq:SU2_fiber_norm]</a> gives
``` math
\begin{equation}
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{2\pi}{g_{\mathrm{tw}}^2}.
\label{eq:SU2_eff_coupling}
\end{equation}
```

### Identification with the MTT overlap

In the MTT overlap formulation at the matching scale,
``` math
\frac{1}{g_2^2}
=
\frac{1}{g_{10}^2}
\int_{B_2}w_2\langle\omega_2,\omega_2\rangle\,d\mu_{B_2}
=
\frac{1}{g_{10}^2}\,I_2^{(0)}.
```
Comparing with <a href="#eq:SU2_eff_coupling" data-reference-type="eqref" data-reference="eq:SU2_eff_coupling">[eq:SU2_eff_coupling]</a>, we identify the leading–order $`SU(2)`$ overlap as
``` math
\begin{equation}
I_2^{(0)}
=
\int_{B_2}w_2^{(0)}
\langle\omega_2^{(0)},\omega_2^{(0)}\rangle\,d\mu_{B_2}
=
4\pi (f_2R_{\mathrm{lens}})^2,
\label{eq:SU2_overlap_final}
\end{equation}
```
where the factor $`4\pi`$ arises from the area of the unit two–sphere of directions associated with the twistor line.

<div class="theorem">

**Theorem 2** (Conditional Route B $`SU(2)`$ normalization). *Assume the SDYM fiber reduction, the coupling identification, and the direction-sphere bridge $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$. For the $`SU(2)`$ gauge sector the resulting leading–order overlap is
``` math
I_2^{(0)} = 4\pi (f_2R_{\mathrm{lens}})^2,
```
without using the internal Laplacian bound. The metric scale and the direction-sphere bridge are nevertheless shared with the Route A ansatz.*

</div>

<div class="remark">

*Remark 3*. This gives an independent representation of the quadratic norm, but not an independent numerical value source. The Fubini–Study normalization, coupling identification, and effective lens metric remain declared bridge inputs.

</div>

## $`SU(3)`$ sector: conditional color–twistor factorization

We next incorporate the selected internal color fiber into Route B. The resulting identity is conditional because neither the fiber nor its massless harmonic is selected by the twistor action in this paper.

### Color–twistor factorization of the massless mode

In Modal Triplet Theory, color degrees of freedom reside on the third internal factor
``` math
B_3 \simeq S^1_{\mathrm{cen}} \times \Gamma\backslash\mathrm{Nil}_3.
```
In the high–coherence regime, the massless $`SU(3)`$ gauge mode admits a factorized representation
``` math
\begin{equation}
\Psi^{(0)}(Z,u)
=
\psi_{\mathrm{tw}}(Z)\otimes \chi_{\mathrm{col}}(u),
\label{eq:color_twistor_factorization}
\end{equation}
```
where:

- $`Z\in L_x\simeq\mathbb{CP}^1`$ is the spacetime twistor coordinate,

- $`u\in \Gamma\backslash\mathrm{Nil}_3`$ is the internal color coordinate,

- $`\psi_{\mathrm{tw}}`$ is the normalized massless twistor harmonic,

- $`\chi_{\mathrm{col}}`$ is a normalized massless color harmonic on $`\Gamma\backslash\mathrm{Nil}_3`$.

This factorization is an explicit Route B assumption. The present paper does not derive it, select the compact nilmanifold, or prove uniqueness of the color harmonic from the twistor action alone.

### Normalization of the factorized harmonics

The twistor harmonic $`\psi_{\mathrm{tw}}`$ is normalized using the standard Fubini–Study measure $`\omega_{\mathrm{FS}}`$ on $`\mathbb{CP}^1`$:
``` math
\begin{equation}
\int_{L_x} \|\psi_{\mathrm{tw}}\|^2\, d\mu_{\mathrm{FS}}
=
\int_{L_x} \omega_{\mathrm{FS}}
=
2\pi.
\label{eq:SU3_twistor_norm}
\end{equation}
```

The color harmonic $`\chi_{\mathrm{col}}`$ is normalized intrinsically on the internal color fiber by its $`L^2`$ norm:
``` math
\begin{equation}
\|\chi_{\mathrm{col}}\|_{L^2(\Gamma\backslash\mathrm{Nil}_3)}^2
:=
\int_{\Gamma\backslash\mathrm{Nil}_3}
\|\chi_{\mathrm{col}}\|^2\, d\mu_{\mathrm{nil}}.
\label{eq:SU3_color_norm}
\end{equation}
```

### Twistor–action normalization for $`SU(3)`$

Substituting the factorized form <a href="#eq:color_twistor_factorization" data-reference-type="eqref" data-reference="eq:color_twistor_factorization">[eq:color_twistor_factorization]</a> into the quadratic twistor action and performing the fiber integration yields the four–dimensional gauge kinetic term
``` math
\begin{equation}
S_4[A]
=
\frac{1}{4g_{\mathrm{eff}}^2}
\int_{Y^4} F_{\mu\nu}F^{\mu\nu}\, d\mathrm{vol}_4,
\end{equation}
```
with effective coupling
``` math
\begin{equation}
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{1}{g_{\mathrm{tw}}^2}
\left(
\int_{L_x}\|\psi_{\mathrm{tw}}\|^2\, d\mu_{\mathrm{FS}}
\right)
\left(
\int_{\Gamma\backslash\mathrm{Nil}_3}
\|\chi_{\mathrm{col}}\|^2\, d\mu_{\mathrm{nil}}
\right).
\label{eq:SU3_eff_coupling}
\end{equation}
```

Using <a href="#eq:SU3_twistor_norm" data-reference-type="eqref" data-reference="eq:SU3_twistor_norm">[eq:SU3_twistor_norm]</a> and <a href="#eq:SU3_color_norm" data-reference-type="eqref" data-reference="eq:SU3_color_norm">[eq:SU3_color_norm]</a>, we obtain
``` math
\begin{equation}
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{2\pi}{g_{\mathrm{tw}}^2}
\int_{\Gamma\backslash\mathrm{Nil}_3}
\|\chi_{\mathrm{col}}\|^2\, d\mu_{\mathrm{nil}}.
\label{eq:SU3_eff_coupling_final}
\end{equation}
```

### Identification with the MTT overlap formulation

In the MTT overlap formulation at the matching scale,
``` math
\begin{equation}
\frac{1}{g_3^2}
=
\frac{1}{g_{10}^2}
\int_{B_3}
w_3\langle \omega_3, \omega_3 \rangle\, d\mu_{B_3}.
\end{equation}
```

Comparing with <a href="#eq:SU3_eff_coupling_final" data-reference-type="eqref" data-reference="eq:SU3_eff_coupling_final">[eq:SU3_eff_coupling_final]</a>, we define the leading–order $`SU(3)`$ overlap intrinsically by
``` math
\begin{equation}
I_3^{(0)}
:=
\int_{\Gamma\backslash\mathrm{Nil}_3}
\|\chi_{\mathrm{col}}\|^2\, d\mu_{\mathrm{nil}}.
\label{eq:SU3_overlap_def}
\end{equation}
```

For the isotropic left–invariant metric $`a=b`$ on $`\Gamma\backslash\mathrm{Nil}_3`$ and choosing $`\chi_{\mathrm{col}}`$ to be a canonical left–invariant harmonic one–form, this evaluates explicitly to
``` math
\begin{equation}
I_3^{(0)} = c.
\label{eq:SU3_overlap_value}
\end{equation}
```

<div class="theorem">

**Theorem 4** (Conditional Route B $`SU(3)`$ overlap identity). *In the high–coherence twistor regime, assuming canonical factorization of the massless $`SU(3)`$ gauge mode into a spacetime twistor harmonic and an internal color harmonic on $`\Gamma\backslash\mathrm{Nil}_3`$, the twistor–action reduction yields the conditional leading–order identity
``` math
I_3^{(0)}
=
\int_{\Gamma\backslash\mathrm{Nil}_3}
\|\chi_{\mathrm{col}}\|^2\, d\mu_{\mathrm{nil}},
```
which evaluates to $`I_3^{(0)}=c`$ for the isotropic metric $`a=b`$.*

</div>

<div class="remark">

*Remark 5*. Together with the $`SU(2)`$ analysis, this supplies a conditional Route B compatibility check for the massless nonabelian sector. The assumed asymptotic order $`O(\lambda_Q^{-1})`$ is not yet accompanied here by a coefficient or uniform remainder bound and must not be read as a numerical error certificate.

</div>

## Nil sector ($`SU(3)`$)

For the $`SU(3)`$ sector, the twistor harmonic reconstructs to a left–invariant massless gauge mode on the compact nilmanifold $`\Gamma\backslash\mathrm{Nil}_3`$.

The twistor fiber integral reduces to the $`L^2`$ norm of the reconstructed spacetime harmonic:
``` math
I_3^{(0)} = \int_{\Gamma\backslash\mathrm{Nil}_3}
|\omega^{(0)}|^2\,d\mathrm{vol}.
```

For the isotropic horizontal metric choice $`a=b`$, this evaluates to
``` math
I_3^{(0)} = c,
```
in agreement with the direct geometric computation of Paper II.

# Consistency with the selected gauge profile

Paper I gives the selected common-scheme targets at $`Q=M_t=172.5590883453979~\mathrm{GeV}`$:
``` math
\frac{I_2}{I_1}=0.5110273\pm0.0001231,
\qquad
\frac{I_3}{I_1}=0.158335\pm0.001098,
\qquad
I_1=2\pi R_1.
```
With the leading identities used in Papers II and III, these imply
``` math
(f_2R_{\mathrm{lens}})^2=0.2555137\,R_1,
\qquad
c=0.9948493\,R_1.
```
The former $`5~\mathrm{TeV}`$ profile and the values $`0.560`$, $`0.229`$, $`0.280R_1`$, and $`1.439R_1`$ are withdrawn.

<div class="theorem">

**Theorem 6** (Conditional Route A/Route B agreement). *Assume the common coupling-overlap convention, the selected Paper I profile, the Paper II effective internal ansatz, the SDYM fiber reduction, the direction-sphere normalization bridge, and color–twistor factorization. Then both routes evaluate the same leading quadratic functional and give
``` math
I_2^{(0)}=4\pi(f_2R_{\mathrm{lens}})^2,
\qquad
I_3^{(0)}=c.
```
Consequently both reproduce the displayed profile ratios.*

</div>

<div class="proof">

*Proof.* Under the listed assumptions, both constructions evaluate the $`L^2`$ norm of the same selected massless representative. Equality follows from the shared normalization bridges. It is an exact round-trip identity within the selected ansatz, not an independent derivation of the input profile or internal metric. ◻

</div>

# Dependency audit

The Route B comparison shares the following inputs with Papers I and II:

1.  the measured common-scheme gauge profile and $`I_1=2\pi R_1`$ convention;

2.  the relation $`g_a^{-2}=g_{10}^{-2}I_a`$ and its common normalization;

3.  the effective round-$`S^2`$ lens-base metric and scale $`f_2R_{\mathrm{lens}}`$;

4.  the compact nilmanifold, its metric parameter $`c`$, and the chosen color harmonic; and

5.  the identification of the twistor fiber norm with the selected internal overlap, including $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$.

Route B independently supplies only the twistor/SDYM representation of the quadratic norm conditional on these bridges. A genuinely independent value derivation would have to select the bridges and internal representatives from twistor-corner MTT data without importing the Route A realization.

# Scope and limitations

This paper establishes conditional leading-order compatibility between two representations of the nonabelian overlap functional. It does not establish:

- a source theorem selecting the gauge profile or internal geometry;

- an independent $`SU(2)`$ or $`SU(3)`$ numerical normalization;

- a coefficient-level bound for corrections denoted $`O(\lambda_Q^{-1})`$;

- Yukawa/flavor structure, ultraviolet completion, or string embedding.

# Conclusion

The SDYM twistor reduction and the direct internal calculation can be placed on the same quadratic $`L^2`$ footing. Once the shared normalization and geometry bridges are declared, the two descriptions agree exactly at leading order and reproduce the selected Paper I overlap profile. This is a useful consistency result because it checks that the twistor encoding does not alter the gauge kinetic functional.

It is not a second independent determination of the numerical overlaps. The $`SU(2)`$ coefficient uses the direction-sphere bridge and effective lens metric; the $`SU(3)`$ identity uses the declared auxiliary nilmanifold and color harmonic. The strongest justified conclusion is therefore conditional representation-level compatibility. Independent geometric selection and a quantitative coherence-remainder estimate remain separate theorem targets.

# Normalization proof: twistor action $`\Rightarrow`$ overlap coefficient

This appendix supplies the missing Route B ingredient: an explicit normalization match between a twistor-space SDYM action and the four-dimensional gauge kinetic term, showing that the effective coupling is determined by the same fiber $`L^2`$ overlap integral used in Route A.

## A.1 Twistor geometry and canonical fiber measure

Let $`Y^4`$ be a (local) conformally flat spacetime patch so that its twistor space $`\mathbb{PT}`$ is a $`\mathbb{CP}^1`$ bundle over $`Y^4`$. Write the projection as
``` math
\pi:\mathbb{PT}\to Y^4.
```
Each point $`x\in Y^4`$ corresponds to a twistor line
``` math
L_x \cong \mathbb{CP}^1.
```

We use the standard Fubini–Study Kähler form $`\omega_{\mathrm{FS}}`$ on $`\mathbb{CP}^1`$ normalized by
``` math
\begin{equation}
\int_{\mathbb{CP}^1}\omega_{\mathrm{FS}} = 2\pi.
\label{eq:FSnorm}
\end{equation}
```
This fixes the fiber measure within the adopted Fubini–Study convention.

<div class="remark">

*Remark 7*. Equation <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a> is a normalization convention: any rescaling would correspond to a rescaling of the twistor coupling, and therefore must be fixed once. We fix it as above; a separate bridge is still required to compare the twistor coupling and fiber norm with the MTT internal overlap.

</div>

## A.2 Twistor SDYM action with fixed normalization

A standard twistor-space action for self-dual Yang–Mills has the schematic form
``` math
\begin{equation}
S_{\mathrm{tw}}[{\cal A}]
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathbb{PT}}
\mathrm{Tr}\!\left(
{\cal F}^{(0,2)} \wedge \star {\cal F}^{(0,2)}
\right),
\label{eq:twistor_action}
\end{equation}
```
where $`{\cal A}`$ is a $`(0,1)`$ connection on a holomorphic bundle over $`\mathbb{PT}`$ and $`{\cal F}^{(0,2)}`$ is its $`(0,2)`$ curvature.

The field equations of <a href="#eq:twistor_action" data-reference-type="eqref" data-reference="eq:twistor_action">[eq:twistor_action]</a> enforce holomorphicity along twistor lines and are equivalent (under Ward correspondence) to SDYM on spacetime.

## A.3 Reconstruction to spacetime and fiber reduction

Let $`A_\mu(x)`$ be the reconstructed spacetime gauge field. At leading (quadratic) order, the corresponding spacetime action is
``` math
\begin{equation}
S_{4}[A]
=
\frac{1}{4g_{\mathrm{eff}}^2}
\int_{Y^4}
F_{\mu\nu}F^{\mu\nu}\,d\mathrm{vol}_4,
\label{eq:4d_action}
\end{equation}
```
for some effective coupling $`g_{\mathrm{eff}}`$ determined by the twistor normalization.

<div class="lemma">

**Lemma 8** (Fiber-to-spacetime normalization identity). *Assuming the fiber measure is normalized by <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a>, the effective coupling satisfies
``` math
\begin{equation}
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{L_x}
\|\psi^{(0)}\|^2\, d\mu_{L_x},
\label{eq:fiber_identity}
\end{equation}
```
where $`\psi^{(0)}`$ is the massless twistor harmonic (the fiber representative of the zero-mode) and $`d\mu_{L_x}`$ is the measure induced by $`\omega_{\mathrm{FS}}`$.*

</div>

<div class="proof">

*Proof sketch (standard reduction argument).* Linearize <a href="#eq:twistor_action" data-reference-type="eqref" data-reference="eq:twistor_action">[eq:twistor_action]</a> about the trivial bundle and restrict to the massless cohomology along each twistor line $`L_x`$. The quadratic form reduces to the fiber $`L^2`$ norm of the corresponding harmonic representative $`\psi^{(0)}`$ multiplied by the spacetime $`L^2`$ norm of the reconstructed field strength. The coefficient of the spacetime kinetic term is therefore exactly the fiber integral shown in <a href="#eq:fiber_identity" data-reference-type="eqref" data-reference="eq:fiber_identity">[eq:fiber_identity]</a>. The measure normalization fixes the overall constant. ◻

</div>

<div class="remark">

*Remark 9*. A fully detailed proof can be presented by writing $`{\cal A}`$ in a basis of Dolbeault harmonics on $`L_x`$ and performing the fiber integral explicitly; the only nontrivial constant is fixed by <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a>.

</div>

## A.4 Identification with MTT overlap integrals

In MTT, the gauge overlap formulation at the matching scale is
``` math
\begin{equation}
\frac{1}{g_a^2} = \frac{1}{g_{10}^2} I_a,
\qquad
I_a = \int_{B_a}\langle\omega_a,\omega_a\rangle\, d\mu_{B_a}.
\label{eq:MTT_overlap}
\end{equation}
```

To compare with <a href="#eq:fiber_identity" data-reference-type="eqref" data-reference="eq:fiber_identity">[eq:fiber_identity]</a>, note that in the high-coherence corner the massless gauge mode factorizes into a spacetime field and a fiber harmonic. Under this identification,
``` math
\int_{L_x}\|\psi^{(0)}\|^2 d\mu_{L_x}
\quad \leftrightarrow \quad
\int_{B_a}\langle\omega_a^{(0)},\omega_a^{(0)}\rangle d\mu_{B_a}
= I_a^{(0)}.
```

Thus Route B yields the same functional form as Route A after imposing the bridge between the twistor fiber norm and the internal overlap. The Fubini–Study convention fixes a fiber measure, but does not alone determine the relative coupling normalization or select the internal metric scale.

## A.5 Explicit SU(2) normalization: recovery of the $`4\pi`$ lens factor

We now carry out the only place in Route A where a constant could have been ambiguous: the lens coefficient $`\kappa_\ell`$.

In Route A (Paper II), one used the coefficient $`2/(f_2R_{\mathrm{lens}})^2`$ in the lens spectral bound to motivate the round sphere model, yielding
``` math
I_2^{(0)} = \mathrm{Area}(S^2_{f_2R_{\mathrm{lens}}}) = 4\pi (f_2R_{\mathrm{lens}})^2.
```

Route B reproduces the same factor without reference to that spectral heuristic:

<div class="proposition">

**Proposition 10** (Conditional recovery of $`\kappa_\ell=4\pi`$). *Let the $`SU(2)`$ massless gauge mode be constant on the twistor fiber. In addition to <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a>, assume the direction-sphere bridge $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$ and scale that metric by $`(f_2R_{\mathrm{lens}})^2`$. Then the induced MTT overlap is
``` math
I_2^{(0)} = 4\pi(f_2R_{\mathrm{lens}})^2.
```*

</div>

<div class="proof">

*Proof.* By the bridge assumption, $`\int_{L_x}dA_{\mathrm{dir}}=2\int_{L_x}\omega_{\mathrm{FS}}=4\pi`$. Metric scaling multiplies this area by $`(f_2R_{\mathrm{lens}})^2`$, which gives the stated overlap. The factor of two is part of the explicit bridge and is not derived from <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a> alone. ◻

</div>

This recovers the Route A coefficient conditionally; it does not select the direction-sphere bridge or lens scale entirely within Route B.

## A.6 SU(3) remark and Route B completion criterion

Twistor theory naturally encodes massless SDYM sectors irrespective of the internal realization of color, but the explicit reduction of the SU(3) overlap requires specifying the internal color fiber and its harmonic representative. Given such a choice (e.g. $`\Gamma\backslash\mathrm{Nil}_3`$ with left-invariant harmonic 1-forms), the same fiber reduction <a href="#eq:fiber_identity" data-reference-type="eqref" data-reference="eq:fiber_identity">[eq:fiber_identity]</a> applies after the relative coupling normalization is declared. In particular, if the $`SU(3)`$ massless harmonic is chosen as a unit $`L^2`$ representative on the internal color fiber, then Route B matches Route A.

<div class="remark">

*Remark 11* (What remains for a fully independent SU(3) Route B). To make SU(3) completely independent of Route A, one must (i) specify the twistor-corner representation of the color fiber as a canonical twistor bundle, and (ii) compute the corresponding $`L^2`$ harmonic norm directly on that bundle. Until those steps are supplied, the $`SU(3)`$ result is a conditional cross-check and not an independent normalization theorem.

</div>

<div class="thebibliography">

99

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

P. Nero, *From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*, Zenodo preprint, January 2026. <https://doi.org/10.5281/zenodo.18254862>

</div>
