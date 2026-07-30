---
abstract: |
  This paper determines exactly how far the present Modal Triplet Theory (MTT) gravity program reaches into loop quantum gravity (LQG). It proves an exact conditional composition theorem. If the selected four-dimensional MTT action contains a normalized Holst term and if a global three-plus-one splitting, time gauge, nondegenerate tetrad, and required boundary conditions are supplied, then the standard canonical reduction yields the real Ashtekar–Barbero pair. In the convention used here, the coefficient ratio fixes the Immirzi parameter as its negative inverse. Current MTT results conditionally recover the two-derivative Einstein/TEGR tensor structure, but do not yet emit this parity-odd coefficient; therefore they do not yet predict the Immirzi parameter. The LOST representation, geometric spectra, constraint quantization, and EPRL/FK amplitudes are separately inherited only after their standard hypotheses and constructions are added. This establishes a precise LQG interface and a finite exit contract without treating imported LQG machinery as an MTT derivation.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v4
date: July 2026 Version 4
generated_from_main_tex_sha256: 08afaad4eed5ab632804a8ba435fc950e59fe8abcbdf1090f0616636d4b5a847
paper_id: modal-triplet-theory-from-mtt-to-loop-quantum-gravity-a-4ae4b130
release_state: zenodo_released
released_version: v4
title: |
  Modal Triplet Theory and Loop Quantum Gravity:
  A Conditional Holst/Canonical Embedding
zenodo_doi: 10.5281/zenodo.21665997
zenodo_record_id: 21665997
zenodo_url: "https://zenodo.org/records/21665997"
---

# Version 4 Revision Note

Supersedes:
The former canonical and spin-foam embedding manuscript, version 3.

Reason:
Standard LQG representation, constraint, spin-foam, and ultraviolet results had been counted as consequences of projection without their defining source data.

Resolution:
This paper is now the sole owner of the conditional Holst-to-Ashtekar–Barbero theorem and types every later LQG layer as a separate inheritance.

Retained result:
A complete normalized Holst action yields $`\gamma=-1/r_H`$ and the standard canonical pair under the declared canonical hypotheses.

Remaining boundary:
The selected Holst coefficient, LOST state, quantum constraints, EPRL/FK packet, and SPT-to-spin-foam map remain open.

# Purpose and reader orientation

Loop quantum gravity begins from a canonical rewriting of general relativity. After choosing a spatial foliation and an internal time gauge, the spatial geometry is described by a real $`\mathrm{SU}(2)`$ connection and its conjugate densitized triad. Holonomies of that connection and fluxes of the triad then generate the kinematical algebra used in LQG.

MTT approaches gravity from a different direction. Its present q79 proto-spinor program selects a finite internal carrier and proves a conditional route to the two-derivative Einstein/TEGR tensor structure. It is therefore natural to ask whether the same selected branch also supports the canonical variables of LQG. The answer is conditional:
``` math
\boxed{
 \text{selected normalized Holst action}
 \Longrightarrow
 \text{Ashtekar--Barbero canonical data}
}
```
but the premise has not yet been supplied by MTT.

This distinction matters. A dictionary can show that two constructions agree once their inputs exist. It cannot manufacture those inputs. In particular, an internal projector does not by itself select a foliation, a time gauge, a holonomy–flux state, a Hamiltonian-constraint operator, or a spin-foam measure.

## What this paper owns

The unique technical result of this paper is the conditional Holst-to-canonical composition theorem in Section <a href="#sec:canonical" data-reference-type="ref" data-reference="sec:canonical">3</a>. It also records exact inheritance conditions for later LQG layers. The companion paper on LQG as a fixed-point shadow is interpretive and imports this result; it does not own another derivation of the same variables.

# Typed inputs and present MTT status

## Imported geometric and canonical inputs

Let $`M`$ be an oriented and time-oriented four-manifold. The canonical reduction considered below requires the following data.

1.  A Lorentzian co-tetrad $`e^I`$ and a Lorentz connection $`\omega^{IJ}`$, with nondegenerate spatial triad.

2.  A global or patchwise-controlled splitting $`M\simeq\mathbb R\times\Sigma`$, together with lapse, shift, and boundary conditions that make the variational principle and symplectic form well-defined.

3.  Internal time gauge, reducing the relevant local rotational symmetry to $`\mathrm{SU}(2)`$.

4.  A four-dimensional first-order action with its overall Newton normalization and parity-even/parity-odd coefficient ratio fixed.

These are standard inputs to the real connection formulation; they are not consequences of the mere existence of a coherent projector.

## The normalized action datum

We use the convention
``` math
\begin{equation}
\label{eq:holst-action}
 S_{r_H}[e,\omega]
 =
 \frac{1}{16\pi G}
 \int_M
 \left[
  \frac12\varepsilon_{IJKL}\,
       e^I\wedge e^J\wedge F^{KL}[\omega]
  +r_H\,e_I\wedge e_J\wedge F^{IJ}[\omega]
 \right]
 +S_{\partial M}.
\end{equation}
```
For finite nonzero $`\gamma`$, our sign convention is
``` math
\begin{equation}
\label{eq:ratio}
 r_H=-\frac{1}{\gamma}.
\end{equation}
```
Different sign and factor conventions in the literature change the displayed conversion, so a purported prediction of $`\gamma`$ is meaningless unless the complete normalized action convention is stated. Holst’s construction shows how the generalized Hilbert–Palatini action yields the real Barbero canonical formulation .

## What the q79 branch currently supplies

The current MTT gravity ledger supplies:

1.  an exact finite internal transverse-traceless carrier at its declared algebraic tier;

2.  a selected q79 Fu–Yau compactification route compatible with a heterotic completion;

3.  a controlled, conditional reduction to the two-derivative Einstein/TEGR tensor shape after the required Lorentzian and normalization hypotheses are supplied; and

4.  fixed-order quantum-GR effective-field-theory parity after the renormalized action, Wilson coefficients, state, scale, gauge fixing, and scheme are declared.

No current selected result emits the parity-odd four-dimensional coefficient $`r_H`$ in <a href="#eq:holst-action" data-reference-type="eqref" data-reference="eq:holst-action">[eq:holst-action]</a>. Nor does it emit the global foliation, time gauge, LQG kinematical state, or quantum constraint operators. This is the status against which every theorem below is typed.

# The exact conditional canonical embedding

On a spatial slice $`\Sigma`$, let $`e^i_a`$ be the spatial triad and define the densitized triad
``` math
\begin{equation}
\label{eq:E}
 E^a_i=\frac12\varepsilon^{abc}\varepsilon_{ijk}e^j_b e^k_c.
\end{equation}
```
Let $`\Gamma^i_a(E)`$ be the torsion-free spin connection compatible with the triad and let $`K^i_a`$ be the extrinsic-curvature one-form. For real $`\gamma\ne0`$, define
``` math
\begin{equation}
\label{eq:A}
 A^i_a=\Gamma^i_a+\gamma K^i_a .
\end{equation}
```

<div id="thm:holst-canonical" class="theorem">

**Theorem 1** (Conditional Holst-to-canonical composition). *Suppose a selected MTT branch supplies the complete normalized action <a href="#eq:holst-action" data-reference-type="eqref" data-reference="eq:holst-action">[eq:holst-action]</a> with $`r_H\ne0`$, together with the tetrad, connection, $`3+1`$ splitting, time gauge, nondegeneracy, and boundary data listed in Section <a href="#sec:inputs" data-reference-type="ref" data-reference="sec:inputs">2</a>. Assume also that torsion is either absent or treated consistently with all matter and boundary contributions. Then the standard canonical reduction of that action yields the real Ashtekar–Barbero variables <a href="#eq:E" data-reference-type="eqref" data-reference="eq:E">[eq:E]</a>–<a href="#eq:A" data-reference-type="eqref" data-reference="eq:A">[eq:A]</a>, with
``` math
\gamma=-\frac1{r_H},
```
and canonical bracket
``` math
\begin{equation}
\label{eq:bracket}
 \{A^i_a(x),E^b_j(y)\}
 =
 8\pi G\,\gamma\,
 \delta^i_j\delta^b_a\delta^{(3)}(x,y)
\end{equation}
```
in the stated normalization.*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:holst-action" data-reference-type="eqref" data-reference="eq:holst-action">[eq:holst-action]</a>, with $`r_H=-1/\gamma`$, is the Holst generalization of the Hilbert–Palatini action in the chosen convention. Perform its $`3+1`$ decomposition, impose the time gauge, solve the second-class connection conditions in the nondegenerate sector, and retain the boundary term required by the variational principle. The resulting symplectic potential has the canonical form
``` math
\Theta_{\Sigma}
 =
 \frac{1}{8\pi G\gamma}
 \int_{\Sigma} E^a_i\,\delta A^i_a\,\mathrm d^3x
 +\delta B,
```
where $`\delta B`$ is an exact field-space variation determined by the boundary convention. Its exterior field-space derivative removes $`\delta B`$ and gives
``` math
\Omega_{\Sigma}
 =
 \frac{1}{8\pi G\gamma}
 \int_{\Sigma}
 \delta E^a_i\wedge\delta A^i_a\,\mathrm d^3x .
```
Inverting this symplectic form gives <a href="#eq:bracket" data-reference-type="eqref" data-reference="eq:bracket">[eq:bracket]</a>. This is the standard Holst canonical reduction ; MTT enters only by supplying the theorem’s premise. ◻

</div>

<div class="corollary">

**Corollary 2** (Exact location of the Immirzi blocker). *Current MTT gravity results do not determine a numerical Barbero–Immirzi parameter. They would determine one through $`\gamma=-1/r_H`$ if and only if the same selected four-dimensional source that fixes the Einstein normalization also emits a nonzero normalized parity-odd coefficient $`r_H`$.*

</div>

<div class="proof">

*Proof.* The theorem converts a supplied coefficient into $`\gamma`$, but does not compute that coefficient. The present ledger contains no selected $`r_H`$-source row. Therefore the conversion map is exact and its input is open. ◻

</div>

## Why an overlap symbol is not yet a prediction

One may formally write coefficients $`\alpha_{\mathrm{even}}(\Theta)`$ and $`\alpha_{\mathrm{odd}}(\Theta)`$ and take their ratio. This is useful notation only after both functionals, their domains, normalization, branch, and evaluated values are supplied by the same source. Naming the second coefficient a “modal overlap” does not prove its existence or select its value. The earlier edition crossed precisely this gap.

# Holonomy–flux kinematics and the LOST boundary

Given the canonical pair, one may define holonomies $`h_e[A]\in\mathrm{SU}(2)`$ along suitable edges $`e\subset\Sigma`$ and fluxes $`E_i(S)`$ through suitable surfaces $`S`$. These generate a holonomy–flux algebra. This construction additionally chooses:

1.  the category of edges and surfaces;

2.  the precise algebra and its domains;

3.  the action of spatial diffeomorphisms; and

4.  a state or representation.

<div id="prop:lost" class="proposition">

**Proposition 3** (Conditional representation inheritance). *If the canonical data of Theorem <a href="#thm:holst-canonical" data-reference-type="ref" data-reference="thm:holst-canonical">1</a> are supplied and the resulting holonomy–flux algebra, diffeomorphism action, cyclic state, regularity, and domain data satisfy the exact hypotheses of a chosen LOST-type uniqueness theorem, then its GNS representation is the corresponding Ashtekar–Lewandowski representation.*

</div>

<div class="proof">

*Proof.* This is direct application of the uniqueness theorem to the supplied algebraic data . No additional MTT step is involved. ◻

</div>

The proposition is intentionally conditional. A bounded projector commuting with some diffeomorphisms does not automatically construct a positive normalized state on the full holonomy–flux algebra, establish its regularity, or verify all domain assumptions. The earlier “MTT to LOST” proof replaced these objects by an assertion that projection furnished them. That argument is withdrawn.

# What is inherited after the representation exists

## Spin networks and geometric operators

In the Ashtekar–Lewandowski representation, spin networks provide a standard orthonormal basis of the kinematical Hilbert space $`\mathcal H_{\mathrm{kin}}=L^2(\overline{\mathcal A},\mathrm d\mu_{\mathrm{AL}})`$. The usual area operator acts schematically as
``` math
\begin{equation}
\label{eq:area}
 \widehat A(S)\psi
 =
 8\pi\gamma\ell_P^2
 \sum_{e\cap S}
 \sqrt{j_e(j_e+1)}\,\psi ,
\end{equation}
```
subject to the standard intersection and operator conventions. Volume operators are graph-local expressions in fluxes at vertices .

These spectra are inherited results of the chosen LQG representation and operator definitions. Compactness or finite projection alone does not imply the holonomy–flux commutation relations, the Ashtekar–Lewandowski measure, or the area and volume operators. Their discreteness is therefore not yet an independent prediction of MTT.

## Classical and quantum constraints

The time-gauge canonical reduction also produces the standard Gauss, spatial-diffeomorphism, and Hamiltonian constraint functions. Their quantization is a separate layer. It requires regularized operators, common or controlled domains, anomaly analysis, group averaging where applicable, and a construction of physical states. Choosing Thiemann’s Hamiltonian or master-constraint program imports a particular LQG proposal ; it is not forced by the MTT projector.

Consequently, this paper does not claim that the kernel of an MTT-induced master constraint has been constructed. It records that such a continuation becomes available only after the representation and operator data are selected.

# Covariant spin foams are a further construction

The EPRL/FK route requires more than the Holst coefficient. At minimum one must provide:

1.  a BF/Plebanski rewriting and the relevant simplicity constraints;

2.  a discretization or two-complex and boundary Hilbert spaces;

3.  the map from Lorentz representations to $`\mathrm{SU}(2)`$ boundary data;

4.  face, edge, and vertex amplitudes, normalization, and measure; and

5.  control of refinement, semiclassical asymptotics, and any continuum limit being claimed.

With these inputs, standard EPRL/FK amplitudes and their established large-spin results may be studied . Neither the action <a href="#eq:holst-action" data-reference-type="eqref" data-reference="eq:holst-action">[eq:holst-action]</a> nor an MTT fixed point uniquely selects this packet.

<div class="proposition">

**Proposition 4** (Conditional EPRL/FK continuation). *If, in addition to Theorem <a href="#thm:holst-canonical" data-reference-type="ref" data-reference="thm:holst-canonical">1</a>, a selected MTT branch supplies the five items above in exactly the standard EPRL/FK form, then the resulting amplitudes inherit the corresponding EPRL/FK theorems, including only those asymptotic statements whose boundary data and nondegeneracy hypotheses are met.*

</div>

<div class="proof">

*Proof.* Once the complete amplitude equals the standard amplitude on the same domain, the result follows by substitution into the established EPRL/FK analysis. The proposition is an equality-and-inheritance statement, not a derivation of the amplitude packet from MTT. ◻

</div>

# No automatic ultraviolet transfer

The MTT SPT construction is presently a finite Euclidean transverse-traceless filter at its declared tier. A function that damps a perturbative propagator does not automatically become a spin-foam face or vertex weight. Such a transfer would have to prove:

1.  a map from the filtered continuum or internal operator to the representation labels of a two-complex;

2.  cylindrical or refinement consistency of the induced weights;

3.  compatibility with gauge and simplicity constraints; and

4.  preservation of the intended semiclassical and unitarity properties.

No such map is currently selected. The old claim that SPT suppression persists in the background-independent spin-foam sum is therefore withdrawn.

# Relation to the q79 heterotic route

The q79 Fu–Yau branch and the LQG interface answer different questions. The former is the current candidate for a selected internal compactification and a conditional heterotic ultraviolet completion. The latter is a canonical quantization interface for an effective four-dimensional gravitational sector. They may be compatible, but neither contains the other automatically.

For a same-source bridge, the q79 reduction must emit the complete four-dimensional first-order action, including $`G`$, boundary terms, torsion/matter contributions, and $`r_H`$. Only then can Theorem <a href="#thm:holst-canonical" data-reference-type="ref" data-reference="thm:holst-canonical">1</a> transport the result into real connection variables. A worldsheet completion would still not prove the LOST state or a spin-foam continuum limit; those remain distinct lower-dimensional quantization choices.

# Result ledger and exit contract

<div class="center">

| Layer | Status | Required object or result |
|:---|:---|:---|
| Finite internal TT carrier | Available | Exact at its declared finite algebraic tier |
| Einstein/TEGR tensor shape | Conditional | Lorentzian branch and normalization hypotheses |
| Normalized Holst ratio $`r_H`$ | Open | Same-source parity-odd four-dimensional coefficient |
| Ashtekar–Barbero pair | Conditional exact | Theorem <a href="#thm:holst-canonical" data-reference-type="ref" data-reference="thm:holst-canonical">1</a> |
| LOST/AL representation | Open inheritance | Exact algebra, state, symmetry, regularity, and domains |
| Area/volume spectra | Open inheritance | AL representation and standard operators |
| Quantum constraints | Open | Regularization, domains, anomalies, and physical-state construction |
| EPRL/FK amplitudes | Open | BF/simplicity/discretization/amplitude packet |
| SPT-to-spin-foam UV map | Open | Explicit cylindrically consistent weight map |

</div>

The shortest decisive next calculation is not a numerical entropy fit. It is the emission, from the same selected q79 source as the parity-even gravitational term, of the normalized parity-odd coefficient $`r_H`$ with a proven four-dimensional reduction and convention certificate. A successful result would immediately select $`\gamma`$ through $`\gamma=-1/r_H`$. A proof that the coefficient vanishes would instead show that this particular Holst-derived finite-$`\gamma`$ bridge is unavailable.

# Discussion

The corrected conclusion is still useful. MTT and LQG are not being declared equivalent, and LQG is not being derived from projection alone. Rather, the two programs meet at a sharply typed interface. MTT is asked to select a specific normalized effective action. LQG supplies a well-developed canonical and quantum-geometric continuation once its own hypotheses are chosen.

This division makes the comparison testable. A selected MTT action with a nonzero parity-odd ratio predicts a value of $`\gamma`$, which then enters LQG geometric spectra and any chosen horizon-state counting. If no such coefficient is emitted, there is no MTT Immirzi prediction. If the selected action or state fails the canonical or representation hypotheses, the LQG embedding fails at the corresponding row rather than being rescued by a change of interpretation.

# Version 4 revision note

This edition replaces the former derivation claim with a conditional embedding theorem. It removes the unsupported assertions that the coherent projector supplies the LOST state, quantum constraints, master-constraint kernel, EPRL/FK amplitudes, spin-foam ultraviolet damping, black-hole entropy normalization, or loop-cosmology parameters. It also withdraws the claimed computed Immirzi parameter. The exact Holst coefficient-to-$`\gamma`$ map is retained, with its normalization convention and missing MTT source identified explicitly.

# Conclusion

MTT currently has a precise route to LQG, not a completed derivation of LQG. The route is:
``` math
\begin{aligned}
 \text{q79 selected four-dimensional action}
 &\longrightarrow \text{normalized Holst coefficient}\\
 &\longrightarrow \text{Ashtekar--Barbero variables}\\
 &\longrightarrow \text{separately supplied LQG quantization layers}.
\end{aligned}
```
Only the middle implication is proved here, conditional on its input. This places the frontier at a concrete source coefficient and prevents standard LQG results from being counted twice as MTT results.
