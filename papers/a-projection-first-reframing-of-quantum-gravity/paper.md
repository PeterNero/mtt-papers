---
abstract: |
  This essay develops a projection-first research perspective on quantum gravity. It does not deny that metric perturbations have propagating helicity-two degrees of freedom, that they can be quantized perturbatively, or that General Relativity is a predictive low-energy quantum effective field theory. Instead, it asks whether the effective quantum geometry seen by an observer could be the retained response of a deeper quantum source and selection process. On that view, quantized matter and source action can place stress on an effective geometric medium, while projection determines which geometric distinctions remain observable. Horizons and singularities then become candidates for observer-relative or theory-relative limits of an effective description, not automatic proofs of projection failure. We separate this interpretation from established results, compare it with effective-field-theory, holographic, and background-independent approaches, and list the mathematical gates a constructive MTT realization must pass: a Lorentzian principal symbol, a positive physical spin-two sector, BRST or equivalent gauge consistency, universal stress-energy coupling, controlled local reduction, and global gluing. Current MTT work supplies an internal helicity-two support certificate and conditional reduction machinery, but not a completed ultraviolet theory, Newton normalization, or full matter response. Projection-first quantum gravity is therefore presented as a testable research program rather than a solved theory.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 9a99b9c9786f3b0105c776c2962d41ee28dbf88adb454f28ff9dcb675f20f06a
paper_id: a-projection-first-reframing-of-quantum-gravity
release_state: zenodo_released
released_version: v2
title: A Projection-First Reframing of Quantum Gravity
zenodo_doi: 10.5281/zenodo.21665936
zenodo_record_id: 21665936
zenodo_url: "https://zenodo.org/records/21665936"
---

# Revision note for this edition

Supersedes.
*A Projection-First Reframing of Quantum Gravity*, version 1.

Reason.
The first edition treated gravity as categorically unquantizable, described the metric as mere bookkeeping, portrayed existing quantum-gravity programs as repeated failures, and promoted horizons and singularities directly to projection breakdown. Those claims exceeded both standard results and the current MTT construction.

Resolution.
This edition distinguishes effective metric degrees of freedom from a proposed deeper source ontology, recognizes perturbative quantum GR as a valid low-energy EFT, treats horizon and singularity language as hypotheses with explicit limits, and turns the proposal into a list of constructive and falsifiable gates.

Retained content.
The projection-first question remains useful: noninvertible coarse description can explain why globally distinct states look identical to restricted observers, and geometry may be an effective response to selected quantum source data rather than the most fundamental object.

Remaining boundary.
No current MTT theorem derives the complete Lorentzian gravitational action, its physical normalization, universal stress response, or ultraviolet completion from projection alone.

# Overview and How to Read the Reframing

## The central picture

In plain language, the projection-first idea introduces three levels:
``` math
\begin{gathered}
\boxed{\text{upper source dynamics}}
\longrightarrow
\boxed{\text{selection and projection}}
\\[1mm]
\Downarrow
\\[-1mm]
\boxed{\text{effective quantum fields and geometry}} .
\end{gathered}
```
The first level contains whatever dynamics the underlying theory ultimately uses. The second specifies which distinctions survive into a particular effective description. The third is the world in which laboratory fields, clocks, rods, causal order, and gravitational waves are represented.

This separation suggests a possibility, not a conclusion. Quantized source action might generate stress, while the effective metric records the coherent response after projection. In that interpretation one need not regard the metric as the most fundamental variable. Nevertheless, the effective metric can still possess genuine propagating modes and quantum correlations. Being emergent does not mean being nondynamical or classical.

## What the paper does not claim

The essay does not claim that:

- quantizing metric perturbations is a category error;

- horizons locally destroy physical description;

- every singularity has divergent curvature;

- area laws prove a finite MTT projection capacity;

- existing quantum-gravity programs have failed mathematically; or

- MTT already supplies a complete ultraviolet theory of gravity.

Those stronger statements are neither needed nor currently justified. The purpose is to identify a different division of labor between quantum source dynamics, projection, and effective geometry, then ask what would make that division mathematically credible.

# What Established Quantum Gravity Already Tells Us

## The metric has physical perturbative degrees of freedom

General Relativity has two local propagating tensor polarizations around a regular four-dimensional background. Linearized metric perturbations can be quantized, and their quanta are gravitons. At energies well below the Planck scale, General Relativity is a consistent quantum effective field theory: higher-curvature operators encode short-distance uncertainty, while long-distance quantum corrections can be calculated without knowing the ultraviolet completion .

Perturbative nonrenormalizability therefore does not mean that quantum gravity is meaningless. It means that the Einstein–Hilbert action is not expected to be the last term in a fundamental ultraviolet description. This is the same EFT logic used throughout particle physics, with gravity’s very high suppression scale making the low-energy expansion especially successful.

## Universal spin-two coupling is a real constraint

Massless helicity-two consistency strongly constrains how a graviton couples. Soft-graviton arguments connect Lorentz invariance and factorization to universal coupling, while nonlinear completion leads toward Einstein dynamics . A projection-first theory cannot evade these results by changing vocabulary. It must recover the same physical pole, gauge redundancy, conserved source, and self-coupling in the regime where GR is observed.

## There is no single established ultraviolet completion

String theory, loop and spin-foam approaches, asymptotic safety, causal sets, holography, group-field and tensor models, and other programs attack different parts of the problem. Several contain rigorous or highly developed mathematical sectors; none currently has a unique, experimentally confirmed description of Planck-scale gravity. It is more accurate to call the ultraviolet problem open than to call all these programs failures.

# The Projection-First Hypothesis

## Geometry as response rather than fundamental substance

The proposed MTT reading is that effective geometry records the coherent response to source action and closure strain. Schematically, after a selected projection $`\mathcal P`$,
``` math
\begin{equation}
 S_{\rm eff}[g,\psi]
 =S_{\rm geom}[g]+S_{\rm source}[g,\mathcal P\psi]
 +\Delta S_{\rm proj}[g,\psi],
\label{eq:Seff}
\end{equation}
```
and the metric response is determined by
``` math
\begin{equation}
 \frac{\delta S_{\rm eff}}{\delta g^{\mu\nu}}=0.
\label{eq:response}
\end{equation}
```
This is compatible with the familiar Einstein equation when $`S_{\rm geom}`$ contains the Einstein–Hilbert term and the projected source has a conserved stress tensor. Equations <a href="#eq:Seff" data-reference-type="eqref" data-reference="eq:Seff">[eq:Seff]</a>–<a href="#eq:response" data-reference-type="eqref" data-reference="eq:response">[eq:response]</a> do not derive either ingredient. They display the location of the missing source theorem.

The phrase “quantized action stresses the medium” can therefore be made precise in two stages:

1.  construct quantum source observables and their selected state or functional; and

2.  prove that their variation induces a local, conserved, positive geometric response with the observed normalization.

Until both stages are supplied, the phrase is an interpretation rather than a calculation.

## Emergent and quantum are compatible

An effective variable may be emergent and still require quantization. Sound waves are collective yet quantized as phonons; hydrodynamic variables are coarse yet fluctuate. Likewise, if metric perturbations are the low-energy collective modes of a deeper MTT carrier, their quantum correlations remain part of the effective theory. The meaningful distinction is not “quantum versus geometric” but:
``` math
\text{fundamental source variable}
\quad\hbox{versus}\quad
\text{effective collective variable}.
```
The projection-first proposal concerns this ontology and the map between levels. It does not repeal low-energy graviton physics.

# A Concrete Model of Noninvertible Description

Consider a bipartite Hilbert space $`\mathcal H_{\rm full}=\mathcal H_{\rm obs}\otimes\mathcal H_{\rm hidden}`$. A restricted observer assigns
``` math
\rho_{\rm obs}
 =\operatorname{Tr}_{\rm hidden}\rho_{\rm full}.
```
Many distinct full states have the same reduced density operator, so the partial trace has no inverse on the full state space. Entropy can increase for the restricted description even though the full state evolves unitarily. This is an exact and familiar example of effective information loss without fundamental destruction of information.

The example captures the intuition behind projection-first horizon language: an observer may lack an inverse map from accessible data to the global state. It does *not* prove that a gravitational horizon is literally a partial trace, nor that the hidden factor is an MTT bundle. A gravity construction must derive the relevant observable algebra, state restriction, modular structure, and causal domain rather than import the analogy.

# Horizons: A Careful Projection Interpretation

## What a horizon is in GR

An event horizon is a global causal boundary defined relative to the future of the spacetime. A freely falling observer need not encounter any local singularity at a large regular horizon. The horizon therefore cannot be identified in general with local failure of admissibility or local breakdown of physics.

For a restricted exterior observer, however, the inaccessible region changes which observables can be reconstructed. Quantum field theory in such restricted regions, black-hole thermodynamics, and holographic dualities all make this restriction physically important. Bekenstein–Hawking entropy scales with horizon area , but the area law alone does not identify the microscopic states or prove a particular MTT capacity functional.

## The admissibility hypothesis

A defensible projection-first hypothesis is:

> A horizon may mark a boundary of an observer’s reconstructible effective algebra even when the local field equations and freely falling description remain regular.

This statement is observer- and algebra-relative. To promote it to a theorem, one must construct a restriction map, characterize its kernel, show how the area law arises, and recover the known Hawking and generalized-entropy relations. Saying simply that all interior states project to one exterior state would be false and far too coarse: exterior observables can retain substantial information about charges, radiation, correlations, and the black-hole state.

# Singularities: Boundary of a Theory, Not Yet a Projection Theorem

The singularity theorems establish geodesic incompleteness under stated causal and energy conditions . A singular spacetime need not contain a point of infinite scalar curvature, and a “singularity” is not ordinarily a point belonging to the manifold. It is therefore better to say that classical spacetime evolution becomes inextendible in a specified sense than to say that every distinction categorically disappears.

Projection-first language can still be useful. If the effective carrier, principal symbol, or observable map loses the estimates required for continuation, then the effective description has reached a mathematical boundary. A constructive theory should identify which estimate fails:

- hyperbolicity or causal stability;

- boundedness of the projection;

- positivity of the physical state space;

- control of curvature and stress-energy;

- invertibility of a reconstruction map; or

- convergence of the effective expansion.

This replaces a metaphorical “failure of description” with a list of objects that can actually be tested.

# Relationship to Other Approaches

<div class="center">

| Approach | Shared ground | Distinct projection-first question |
|:---|:---|:---|
| Gravity as EFT | Low-energy gravitons and higher-curvature corrections are valid. | Can their coefficients and source map descend from one selected upper carrier? |
| Semiclassical gravity | Quantum matter sources an effective classical geometry. | What state-selection and fluctuation terms replace a bare expectation-value source when that approximation fails? |
| Holography and quantum error correction | Bulk reconstruction can be observer- or code-subspace dependent . | Is the MTT projection an explicit encoding/reconstruction map with the same entropy and locality properties? |
| String theory | Consistent ten-dimensional quantum systems can yield gravity and gauge sectors after compactification. | Can MTT select the compactification, normalized zero modes, and effective action rather than merely reinterpret them? |
| Loop/spin-network approaches | Geometric observables can have discrete kinematics. | Does an MTT finite carrier reproduce the physical constraint algebra and continuum dynamics, not only a discrete support pattern? |

</div>

The projection-first proposal is most credible when it acts as a precise bridge among these established structures. It is least credible when it declares them unnecessary without reproducing their successful limits.

# Constructive Gates for an MTT Quantum-Gravity Sector

A local admissible QG sector is not complete merely because all loop integrals in one representation are finite. At minimum, one must provide:

1.  **Selected causal carrier.** A Lorentzian principal symbol and well-posed local evolution, not a positive Gram tensor relabeled as spacetime.

2.  **Physical spin-two sector.** Two helicity-two polarizations, a positive pole residue, and no unremoved negative-norm modes.

3.  **Gauge consistency.** Diffeomorphism/BRST or an equivalent constraint complex with anomaly control and a positive physical state space.

4.  **Universal source response.** A normalized coupling to a conserved stress tensor and the nonlinear self-coupling required in the GR limit.

5.  **Controlled reduction.** A consistent-truncation equation or an explicit error bound for discarded modes, including moduli and vector zero modes.

6.  **Ultraviolet statement.** A regulator-independent construction or a clearly delimited EFT, with analyticity, unitarity, and causality checked in the same theory.

7.  **Global gluing.** Compatibility of local sectors on overlaps, including state, connection, holonomy, and observable maps.

8.  **Empirical dictionary.** A Newton and Planck normalization, the post-Newtonian and gravitational-wave limits, and at least one discriminating prediction not used as input.

These gates are interdependent. For example, a damped Euclidean propagator does not establish Lorentzian unitarity by itself, and a finite helicity carrier does not fix the pole residue or stress response. A successful construction must make the same selected source pass all gates.

# Where MTT Currently Stands

The current MTT corpus contains three relevant levels:

- a corrected ten-dimensional action paper that explicitly treats the metric and Einstein–Hilbert sector as a regime-local ansatz;

- a controlled coherent-reduction paper that gives the exact discarded equation and an approximate gap/error theorem; and

- a successor calculation that closes internal $`\mathbb Z_{64}`$ transverse-traceless support with two real helicity-two directions and a normalized internal eigenvalue.

This is real progress in organizing the gravity bridge. It establishes that the finite selected carrier can host the right internal TT support and that a supplied metric action has a mathematically controlled route to a four-dimensional GR sector.

The practical content of the result is also limited. The corpus does not yet derive the physical Newton constant, Planck scale, complete matter stress-energy response, positive graviton pole, or a unique ultraviolet completion from one MTT source. Earlier constructive-QG packets should therefore be read as conditional contracts unless their hypotheses have been closed independently.

# What Would Count as Success or Failure

## Success

The program would become substantially stronger if one selected source operator produced, without importing measured gravity data:

- the physical Lorentzian spin-two Hessian and its positive residue;

- a conserved universal matter-response map;

- $`\kappa_4`$ from normalized internal data;

- a controlled GR infrared limit; and

- a finite or UV-complete quantum construction with common gauge and analytic-continuation policies.

Agreement among these outputs would turn the projection-first picture from an interpretation into a constructive theory.

## Failure

The proposal would fail in its strong form if no common source can produce the physical spin-two and stress sectors, if the selected projection violates unitarity or causality, if extra light modes contradict observation, or if all numerical agreement requires replaying the measured constants it claims to derive. These are useful failure conditions because they keep the reframing answerable to physics.

# Discussion: What This Reframing Means

The projection-first perspective does not remove quantum gravity. It reorganizes the problem. The quantum object may be a deeper source and selection structure, while spacetime geometry is its effective collective response. The resulting metric must still reproduce every successful low-energy statement ordinarily described as quantum gravity.

This interpretation gives hope for a specific reason: it permits one common selection map to organize matter, gauge, and geometric response before their complicated projected rules are checked separately. Its risk is equally clear: unless that map is constructed, the language merely redescribes known effective physics. The frontier is therefore an operator and normalization problem, not a philosophical declaration that gravity should never be quantized.

# Conclusion

A defensible projection-first reframing says neither that gravity is unreal nor that metric quantization is meaningless. It asks whether effective quantum geometry can be derived as the coherent response of deeper selected quantum source data. Restricted descriptions are naturally noninvertible, so this viewpoint may illuminate why observer-dependent reconstruction, entropy, and causal boundaries recur in gravitational physics.

The idea remains a research program. Current MTT results provide internal helicity-two support and conditional reduction machinery, not full constructive quantum-gravity closure. The next decisive advance is a same-source Lorentzian Hessian and conserved stress-response theorem with physical normalization. That object would let the interpretation meet the successful mathematics of GR, QFT, and existing quantum-gravity approaches on equal terms.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, revised edition, 2026.

P. Nero, *Controlled Coherent Reduction to Four-Dimensional Einstein Gravity*, third edition, 2026.

P. Nero, *Closure Geometry and a Regime-Local Ten-Dimensional Action Ansatz*, fourth edition, 2026.

J. F. Donoghue, “General relativity as an effective field theory: The leading quantum corrections,” *Physical Review D* **50** (1994) 3874–3888, [doi:10.1103/PhysRevD.50.3874](https://doi.org/10.1103/PhysRevD.50.3874).

S. Weinberg, “Photons and gravitons in S-matrix theory: Derivation of charge conservation and equality of gravitational and inertial mass,” *Physical Review* **135** (1964) B1049–B1056, [doi:10.1103/PhysRev.135.B1049](https://doi.org/10.1103/PhysRev.135.B1049).

S. Deser, “Self-interaction and gauge invariance,” *General Relativity and Gravitation* **1** (1970) 9–18, [doi:10.1007/BF00759198](https://doi.org/10.1007/BF00759198).

J. D. Bekenstein, “Black holes and entropy,” *Physical Review D* **7** (1973) 2333–2346, [doi:10.1103/PhysRevD.7.2333](https://doi.org/10.1103/PhysRevD.7.2333).

S. W. Hawking, “Particle creation by black holes,” *Communications in Mathematical Physics* **43** (1975) 199–220, [doi:10.1007/BF02345020](https://doi.org/10.1007/BF02345020).

G. W. Gibbons and S. W. Hawking, “Action integrals and partition functions in quantum gravity,” *Physical Review D* **15** (1977) 2752–2756, [doi:10.1103/PhysRevD.15.2752](https://doi.org/10.1103/PhysRevD.15.2752).

S. W. Hawking and R. Penrose, “The singularities of gravitational collapse and cosmology,” *Proceedings of the Royal Society A* **314** (1970) 529–548, [doi:10.1098/rspa.1970.0021](https://doi.org/10.1098/rspa.1970.0021).

A. Almheiri, X. Dong, and D. Harlow, “Bulk locality and quantum error correction in AdS/CFT,” *Journal of High Energy Physics* **04** (2015) 163, [doi:10.1007/JHEP04(2015)163](https://doi.org/10.1007/JHEP04(2015)163).

</div>
