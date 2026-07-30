---
abstract: |
  We audit a conditional Route B representation of the leading–order nonabelian overlap integrals $`I_2^{(0)}`$ and $`I_3^{(0)}`$ in Modal Triplet Theory (MTT) using the self–dual Yang–Mills (SDYM) twistor corner. A standard SDYM twistor action is holomorphic BF-type; it does not by itself provide the positive Hermitian $`L^2`$ norm or relative coupling normalization used by Route A. We therefore isolate a reconstruction-and-norm bridge as an explicit assumption. The $`SU(2)`$ comparison additionally uses $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$ and the effective round-$`S^2`$ lens model, while the $`SU(3)`$ comparison uses the declared auxiliary nilmanifold, color harmonic, and factorization assumption of Paper II. Under these shared inputs Route B reproduces $`I_2^{(0)}=4\pi(f_2R_{\mathrm{lens}})^2`$ and $`I_3^{(0)}=\int\|\chi_{\mathrm{col}}\|^2d\mu=c`$. The result is therefore a conditional dictionary check, not an independent derivation or selection of the overlap values and not a completed nonabelian $`\Theta`$–closure theorem.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 86fdc659bb995483be2885b1e91dfe5d69c8914e74e94850e25abcc019bd8460
paper_id: theta-closure-in-modal-triplet-theory-iii-conditional-t-36bd7643
release_state: zenodo_released
released_version: v2
title: "Theta Closure in Modal Triplet Theory III: Conditional Twistor–Action Matching and Normalization Audit"
zenodo_doi: 10.5281/zenodo.21666011
zenodo_record_id: 21666011
zenodo_url: "https://zenodo.org/records/21666011"
---

# Revision note for this edition

Supersedes.
*Theta Closure in Modal Triplet Theory III: Twistor Action Matching and Independent Normalization*, first edition.

Reason.
Route B was described as an independent normalization although its area convention, effective lens model, nil harmonic, and factorization were inherited from Route A. In addition, the displayed twistor action was a schematic Hermitian curvature norm rather than a standard holomorphic BF-type SDYM action.

Resolution.
Version 2 exposes every shared input and proves only the conditional correspondence obtained after a reconstruction-and-norm bridge is imposed. The standard twistor action and the additional Hermitian norm bridge are now kept distinct.

Retained result.
Under those declared bridge conventions, the twistor and direct descriptions use compatible leading overlap functionals.

Remaining boundary.
An independently selected normalization or q79 source theorem is still required for redundant closure evidence.

# Relation to Papers I and II

This paper is the third component of the conservative $`\Theta`$–closure program:

- **Paper I** defines the selected common-scheme gauge profile and the corresponding overlap-ratio targets.

- **Paper II** realizes those targets in a calibrated effective round-$`S^2`$/nilmanifold ansatz (Route A).

- **Paper III** tests whether the same quadratic overlap functional is reproduced by the twistor–encoded gauge action (Route B), and audits which normalization inputs remain shared with Route A.

Agreement between Routes A and B is a conditional internal consistency check. It is not statistically or logically independent evidence when the routes share the internal metric, harmonic, normalization bridge, or target profile.

# Central picture and reading guide

The central picture is a dictionary between two descriptions. Twistor theory encodes a self-dual gauge field by holomorphic bundle data on twistor space. Route A encodes a gauge coefficient by a weighted norm of an internal representative. These are not automatically the same mathematical object. To compare them one must provide a bridge that turns reconstructed twistor data into the Hermitian quadratic form used by the effective gauge action.

The paper therefore has three logical stages. First, it states the standard Penrose–Ward and holomorphic-action input. Second, it declares the extra norm, coupling, direction-sphere, and color-factorization bridges. Third, it checks that those bridges reproduce the two Route A formulas. The final equality is useful as a compatibility audit, but it cannot be counted as a second measurement or a second source of the numerical values.

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

3.  a specified reconstruction map identifies the twistor fields with the spacetime self-dual gauge sector.

</div>

## Twistor action for SDYM

Standard twistor formulations of SDYM are holomorphic BF-type (or closely related holomorphic Chern–Simons-type) actions . Schematically, on a suitable twistor region one may write
``` math
S_{\mathrm{SDYM}}[{\cal A},{\cal B}]
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathbb{PT}}
\Omega\wedge\mathrm{Tr}\!\left({\cal B}\wedge{\cal F}^{(0,2)}\right),
```
where the bundle weights of $`\Omega`$ and $`{\cal B}`$ are chosen so that the integrand is globally defined. Here:

- $`\mathbb{PT}`$ is the relevant region of projective twistor space,

- $`{\cal F}^{(0,2)}`$ is the antiholomorphic curvature of the $`(0,1)`$ connection $`{\cal A}`$,

- $`{\cal B}`$ is the multiplier field imposing $`{\cal F}^{(0,2)}=0`$, and

- $`g_{\mathrm{tw}}`$ is the twistor–action coupling.

The Penrose–Ward correspondence relates the resulting holomorphic bundle data to the self-dual Yang–Mills equations. It does not, without further choices, produce a positive Hermitian fiber norm or fix its normalization relative to the full four-dimensional Yang–Mills kinetic term. That additional datum is the reconstruction-and-norm bridge introduced next.

# Reconstruction of the four–dimensional gauge action

## Ward correspondence and spacetime fields

By the Ward correspondence, holomorphic vector bundles on twistor space correspond to SDYM solutions on spacetime. The reconstruction map yields a spacetime gauge field $`A_\mu`$ whose kinetic term is obtained by integrating over the twistor fiber.

<div class="assumption">

**Assumption 2** (Reconstruction-and-norm bridge). For the selected massless sector, assume that the reconstructed field is assigned the quadratic four-dimensional functional
``` math
Q_4[A] = \frac{1}{4g_{\mathrm{eff}}^2}
\int_{Y^4} F_{\mu\nu}F^{\mu\nu}\,d\mathrm{vol}_4.
```
Assume further that its coefficient is related to a chosen Hermitian fiber metric by
``` math
\frac{1}{g_{\mathrm{eff}}^2}
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathcal F} \langle \psi, \psi\rangle\,d\mu_{\mathcal F},
```
where:

- $`\mathcal F`$ is the internal fiber associated with the gauge sector,

- $`\psi`$ is the period/bridge-normalized twistor harmonic corresponding to the massless mode, with any gauge-kinetic weight included in the displayed measure.

</div>

## Matching of couplings

Under this bridge assumption, the displayed fiber norm is the proposed twistor analogue of the internal overlap integral $`I_a^{(0)}`$ defined in Papers I and II. Neither the holomorphic SDYM field equation nor the Fubini–Study area convention alone proves this coupling identity.

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

We use the holomorphic BF-type SDYM action schematically as
``` math
\begin{equation}
S_{\mathrm{SDYM}}[{\cal A},{\cal B}]
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathbb{PT}}
\Omega\wedge\mathrm{Tr}\!\left(
{\cal B}\wedge{\cal F}^{(0,2)}
\right),
\label{eq:twistor_action_SU2}
\end{equation}
```
with the required line-bundle weights understood. This action supplies the holomorphic SDYM equations. The normalization of a positive Hermitian kinetic functional is additional data and is not fixed merely by choosing <a href="#eq:FS_norm" data-reference-type="eqref" data-reference="eq:FS_norm">[eq:FS_norm]</a>.

### Reconstruction to spacetime

By the Ward correspondence, solutions of the twistor field equations correspond to self–dual Yang–Mills fields on spacetime. Under the reconstruction-and-norm bridge, restricting to the selected massless sector assigns the four–dimensional quadratic functional
``` math
\begin{equation}
S_{4}[A]
=
\frac{1}{4g_{\mathrm{eff}}^2}
\int_{Y^4} F_{\mu\nu}F^{\mu\nu}\,d\mathrm{vol}_4,
\label{eq:4d_SU2}
\end{equation}
```
where the effective coupling is assumed to obey the fiber identity
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

For this comparison we choose the $`SU(2)`$ massless representative to be constant along the fiber and use the Hermitian normalization
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

**Theorem 3** (Conditional Route B $`SU(2)`$ normalization). *Assume the SDYM fiber reduction, the coupling identification, and the direction-sphere bridge $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$. For the $`SU(2)`$ gauge sector the resulting leading–order overlap is
``` math
I_2^{(0)} = 4\pi (f_2R_{\mathrm{lens}})^2,
```
without using the internal Laplacian bound. The metric scale and the direction-sphere bridge are nevertheless shared with the Route A ansatz.*

</div>

<div class="remark">

*Remark 4*. This gives a compatible representation of the quadratic norm after the norm bridge has been imposed, but not an independent derivation or numerical value source. The Hermitian fiber metric, coupling identification, direction-sphere bridge, and effective lens metric remain declared inputs.

</div>

## $`SU(3)`$ sector: conditional color–twistor factorization

We next incorporate the selected internal color fiber into Route B. The resulting identity is conditional because neither the fiber nor its massless harmonic is selected by the twistor action in this paper.

### Color–twistor factorization of the massless mode

In the auxiliary Route A ansatz, the effective color support is the compact Heisenberg nilmanifold $`\Gamma\backslash\mathrm{Nil}_3`$. The shared $`U(1)`$ circle is common phase/holonomy data reused across the gauge lanes; it is not inserted here as a second Cartesian factor of the color support. In the high–coherence regime, the massless $`SU(3)`$ gauge mode admits a factorized representation
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

### Reconstructed quadratic normalization for $`SU(3)`$

Substituting the factorized form <a href="#eq:color_twistor_factorization" data-reference-type="eqref" data-reference="eq:color_twistor_factorization">[eq:color_twistor_factorization]</a> into the declared reconstruction-and-norm bridge gives the four–dimensional quadratic functional
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

**Theorem 5** (Conditional Route B $`SU(3)`$ overlap identity). *In the high–coherence twistor regime, assuming the reconstruction-and-norm bridge and canonical factorization of the massless $`SU(3)`$ gauge mode into a spacetime twistor harmonic and an internal color harmonic on $`\Gamma\backslash\mathrm{Nil}_3`$, the twistor–action reduction yields the conditional leading–order identity
``` math
I_3^{(0)}
=
\int_{\Gamma\backslash\mathrm{Nil}_3}
\|\chi_{\mathrm{col}}\|^2\, d\mu_{\mathrm{nil}},
```
which evaluates to $`I_3^{(0)}=c`$ for the isotropic metric $`a=b`$ and the Paper II harmonic convention.*

</div>

<div class="remark">

*Remark 6*. Together with the $`SU(2)`$ analysis, this supplies a conditional Route B compatibility check for the massless nonabelian sector. The assumed asymptotic order $`O(\lambda_Q^{-1})`$ is not yet accompanied here by a coefficient or uniform remainder bound and must not be read as a numerical error certificate.

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

**Theorem 7** (Conditional Route A/Route B agreement). *Assume the common coupling-overlap convention, the selected Paper I profile, the Paper II effective internal ansatz, the SDYM fiber reduction, the direction-sphere normalization bridge, and color–twistor factorization. Then both routes evaluate the same leading quadratic functional and give
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

## Worked example: what the agreement does and does not test

Set $`R_1=1`$ and import the calibrated Paper II scales
``` math
(f_2R_{\mathrm{lens}})^2=0.2555137,
\qquad
c=0.9948493.
```
Route A then gives
``` math
I_2^{(0)}=4\pi(0.2555137)\approx3.210880,
\qquad
I_3^{(0)}=0.9948493.
```
Route B returns the same numbers because the direction-sphere bridge, the nilmanifold harmonic, and the reconstruction-and-norm bridge identify its fiber expressions with those same two functionals. The example checks that the dictionary is internally consistent. It does not supply new data with which to test the values $`3.210880`$ or $`0.9948493`$.

# Dependency audit

The Route B comparison shares the following inputs with Papers I and II:

1.  the measured common-scheme gauge profile and $`I_1=2\pi R_1`$ convention;

2.  the relation $`g_a^{-2}=g_{10}^{-2}I_a`$ and its common normalization;

3.  the effective round-$`S^2`$ lens-base metric and scale $`f_2R_{\mathrm{lens}}`$;

4.  the compact nilmanifold, its metric parameter $`c`$, and the chosen color harmonic; and

5.  the identification of the twistor fiber norm with the selected internal overlap, including $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$.

Route B independently supplies the holomorphic SDYM representation of the self-dual field data. Its interpretation as the displayed quadratic norm is conditional on the reconstruction-and-norm bridge. A genuinely independent value derivation would have to select the bridges and internal representatives from twistor-corner MTT data without importing the Route A realization.

# Scope and limitations

This paper establishes conditional leading-order compatibility between two representations of the nonabelian overlap functional. It does not establish:

- a source theorem selecting the gauge profile or internal geometry;

- an independent $`SU(2)`$ or $`SU(3)`$ numerical normalization;

- a coefficient-level bound for corrections denoted $`O(\lambda_Q^{-1})`$;

- Yukawa/flavor structure, ultraviolet completion, or string embedding.

# Conclusion

The SDYM twistor description and the direct internal calculation can be placed on the same quadratic $`L^2`$ footing only after a reconstruction-and-norm bridge is declared. Once that bridge and the shared geometry conventions are imposed, the two descriptions agree exactly at leading order and reproduce the selected Paper I overlap profile. This checks the internal consistency of the proposed dictionary; it is not a derivation of that dictionary from the holomorphic action.

It is not a second independent determination of the numerical overlaps. The $`SU(2)`$ coefficient uses the direction-sphere bridge and effective lens metric; the $`SU(3)`$ identity uses the declared auxiliary nilmanifold and color harmonic. The strongest justified conclusion is therefore conditional representation-level compatibility. Independent geometric selection and a quantitative coherence-remainder estimate remain separate theorem targets.

# Normalization-bridge audit: twistor data to overlap coefficient

This appendix records the Route B normalization dictionary without promoting it to a theorem of the holomorphic SDYM action. The standard twistor correspondence supplies the self-dual field data. A Hermitian norm, its relation to the four-dimensional kinetic coefficient, and its identification with the MTT internal overlap are additional bridge choices.

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

*Remark 8*. Equation <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a> is a normalization convention: any rescaling would correspond to a rescaling of the twistor coupling, and therefore must be fixed once. We fix it as above; a separate bridge is still required to compare the twistor coupling and fiber norm with the MTT internal overlap.

</div>

## A.2 Holomorphic SDYM action

A standard twistor-space action for self-dual Yang–Mills has the schematic holomorphic BF form
``` math
\begin{equation}
S_{\mathrm{SDYM}}[{\cal A},{\cal B}]
=
\frac{1}{g_{\mathrm{tw}}^2}
\int_{\mathbb{PT}}
\Omega\wedge\mathrm{Tr}\!\left(
{\cal B}\wedge{\cal F}^{(0,2)}
\right),
\label{eq:twistor_action}
\end{equation}
```
with appropriate bundle weights . Here $`{\cal A}`$ is a $`(0,1)`$ connection, $`{\cal F}^{(0,2)}`$ is its curvature, and $`{\cal B}`$ enforces holomorphicity.

The field equations enforce holomorphicity and correspond, under the Penrose–Ward transform and the usual triviality condition on twistor lines, to the self-dual gauge equations on spacetime. Equation <a href="#eq:twistor_action" data-reference-type="eqref" data-reference="eq:twistor_action">[eq:twistor_action]</a> is not a positive Hermitian curvature norm and does not alone imply the $`L^2`$ identity used below.

## A.3 Reconstruction to spacetime and fiber reduction

Let $`A_\mu(x)`$ be the reconstructed spacetime gauge field. The declared reconstruction-and-norm bridge assigns the quadratic functional
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

<div class="proposition">

**Proposition 9** (Conditional fiber identity). *Assume the reconstruction-and-norm bridge and normalize its chosen Hermitian fiber measure by <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a>. Then the effective coupling satisfies
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

*Proof.* This is the coupling clause of the declared bridge, specialized to the selected massless representative and the displayed fiber convention. ◻

</div>

<div class="remark">

*Remark 10*. A derivation rather than an assumption would require a specified twistor action for the intended spacetime theory, reality structure, Hermitian metric, gauge fixing, functional measure, and pushforward calculation. None is supplied by the Fubini–Study area convention alone.

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

**Proposition 11** (Conditional recovery of $`\kappa_\ell=4\pi`$). *Let the $`SU(2)`$ massless gauge mode be constant on the twistor fiber. In addition to <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a>, assume the direction-sphere bridge $`dA_{\mathrm{dir}}=2\omega_{\mathrm{FS}}`$ and scale that metric by $`(f_2R_{\mathrm{lens}})^2`$. Then the induced MTT overlap is
``` math
I_2^{(0)} = 4\pi(f_2R_{\mathrm{lens}})^2.
```*

</div>

<div class="proof">

*Proof.* By the bridge assumption, $`\int_{L_x}dA_{\mathrm{dir}}=2\int_{L_x}\omega_{\mathrm{FS}}=4\pi`$. Metric scaling multiplies this area by $`(f_2R_{\mathrm{lens}})^2`$, which gives the stated overlap. The factor of two is part of the explicit bridge and is not derived from <a href="#eq:FSnorm" data-reference-type="eqref" data-reference="eq:FSnorm">[eq:FSnorm]</a> alone. ◻

</div>

This recovers the Route A coefficient conditionally; it does not select the direction-sphere bridge or lens scale entirely within Route B.

## A.6 SU(3) remark and Route B completion criterion

Twistor theory naturally encodes massless SDYM sectors irrespective of the internal realization of color, but the explicit reduction of the SU(3) overlap requires specifying the internal color fiber and its harmonic representative. Given such a choice (e.g. $`\Gamma\backslash\mathrm{Nil}_3`$ with left-invariant harmonic 1-forms), the same bridge <a href="#eq:fiber_identity" data-reference-type="eqref" data-reference="eq:fiber_identity">[eq:fiber_identity]</a> applies after the relative coupling normalization is declared. In particular, if the $`SU(3)`$ massless harmonic is chosen as a unit $`L^2`$ representative on the internal color fiber, then Route B matches Route A.

<div class="remark">

*Remark 12* (What remains for a fully independent SU(3) Route B). To make SU(3) completely independent of Route A, one must (i) specify the twistor-corner representation of the color fiber as a canonical twistor bundle, and (ii) compute the corresponding $`L^2`$ harmonic norm directly on that bundle. Until those steps are supplied, the $`SU(3)`$ result is a conditional cross-check and not an independent normalization theorem.

</div>

#### Rows used directly in this paper.

- (*numeric certified*).

  Weighted-theta Fourier-tail and Wiener contraction certificate.

- (*profile replay*).

  Fifteen measured source coordinates, Jacobian and covariance transport.

- (*profile replay*).

  Eight-coordinate SMDR output with positive-definite 8x8 covariance.

- (*derived exact*).

  Sparse 27x27 qutrit-Weyl left-action realization.

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

- (*derived exact*).

  Promoted P_EW source row at the declared one-shared-primitive standard.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The HYM, finite-matrix, and common-scheme precision rows provide the computational target for the conditional twistor-action audit. They do not supply the missing action normalization or prove that the twistor corner is the physical branch. Other sector rows are context, and the strict upgrade remains open.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Rows used directly in this paper

- `A19/hym_wiener_contraction` (**NUMERIC_CERTIFIED**): Weighted-theta Fourier-tail and Wiener contraction certificate.
- `A02/precision_15_source_transport` (**PROFILE_REPLAY**): Fifteen measured source coordinates, Jacobian and covariance transport.
- `A02/precision_8x8_workspace` (**PROFILE_REPLAY**): Eight-coordinate SMDR output with positive-definite 8x8 covariance.
- `A01/qutrit_weyl_27_matrix` (**DERIVED_EXACT**): Sparse 27x27 qutrit-Weyl left-action realization.

## Corpus-state cross-checks

- `A01/charged_yukawa_higgs_profile` (**PROFILE_REPLAY**): Versioned Yu, Yd, Ye and lambda_H profile packet.
- `A14/ckm_prediction_profile` (**NUMERIC_CERTIFIED**): Three selected CKM profile rows and uncertainty comparison.
- `A01/current_global_lock` (**PROFILE_REPLAY**): Current non-looping global status and source-certificate map.
- `A01/direct_k_higgs_row` (**DERIVED_EXACT**): Promoted direct K_threshold.Omega_H.lambda row.
- `A22/e6_qpsi_qcd_anomaly` (**DERIVED_EXACT**): E6 Qpsi matter/exotic QCD anomaly cancellation audit.
- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.
- `A40/neutral_two_primitive_profile` (**PROFILE_REPLAY**): Measured two-splitting neutrino profile, masses and Dirac Yukawa rows.
- `A01/strict_pew_row` (**DERIVED_EXACT**): Promoted P_EW source row at the declared one-shared-primitive standard.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

L. J. Mason, *Twistor actions for non-self-dual fields: a derivation of twistor-string theory*, JHEP **10** (2005) 009. <https://doi.org/10.1088/1126-6708/2005/10/009>

M. V. Movshev, *A note on self-dual Yang–Mills theory*, <https://arxiv.org/abs/0812.0224>

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
