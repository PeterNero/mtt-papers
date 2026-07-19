---
abstract: |
  We replace the former universal “MTT as a Superset” theorem with a typed atlas of relationships between Modal Triplet Theory (MTT) and established frameworks. A derivation, reconstruction, embedding, controlled reduction, conditional bridge, calibration, and interpretive correspondence are different claims and require different certificates. The corrected MTT Foundation and Fixed Points series establish an internal spectral/control spine, but do not by themselves derive General Relativity, the Born rule, interacting quantum field theory, the Standard Model, string theory, a unique heterotic vacuum, or a UV-finite unitary quantum gravity. The strongest current cross-framework results are conditional operator reductions, coherent locality descent, and product-action internal-mode reconstructions. We give a formal containment-certificate checklist and prove an underdetermination theorem: if inequivalent MTT realizations have the same target observables, target agreement cannot select a unique realization. Shared parameter names likewise do not prove shared physical knobs without one sourced map into all sectors. This atlas records the present status of GR, QM, QFT/AQFT, SM, EFT, KK, NCG, string/flux, quantum-gravity, LQG, asymptotic-safety, and causal-set links, and sets explicit gates for upgrading any of them. MTT remains a unification program with several rigorous internal modules, not a proved superset of all listed theories.
author:
- Peter Nero
current_version: v3
date: July 2026
generated_from_main_tex_sha256: aae85312757bd71c5fdd7c07925587fdfba076380d22bc3d4eedcdf4342d18e2
paper_id: modal-triplet-theory-a-typed-relationship-atlas-reconst-e1b59731
release_state: zenodo_released
released_version: v2.0
title: |
  Modal Triplet Theory: A Typed Relationship Atlas  
  Reconstructions, Embeddings, Reductions, and Open Bridges
zenodo_doi: 10.5281/zenodo.18206006
zenodo_record_id: 18206006
zenodo_url: "https://zenodo.org/records/18206006"
---

# Revision note for this edition

Supersedes.  
*Modal Triplet Theory: MTT as a Superset*, version 2.

Reason.  
A universal superset claim merged derivation, reconstruction, embedding, reduction, calibration, and analogy without the certificates needed for mathematical containment.

Resolution.  
Version 3 replaces that theorem by a typed relationship atlas, a containment checklist, an underdetermination theorem, and the current q79/local-carrier status.

Retained result.  
MTT remains a common architecture for comparing and constructing multiple framework-specific realizations.

Remaining boundary.  
No target theory is declared derived until its full same-source state, dynamics, observable, and equivalence certificate is given.

# Why the superset claim is reclassified

The previous version used “containment” for many inequivalent relationships and then combined them into one Superset Containment Theorem. Several inputs to that theorem are now withdrawn or open: exact Born-rule emergence, exact Standard Model closure, unique Strominger-vacuum selection, all-loop BV/QME quantum gravity, constructive unitarity, and a common numerical global fit.

Even when two frameworks share a projector, spectral gap, fixed point, or effective action, the shared motif does not prove equivalence or containment. The state spaces, dynamics, observables, constraints, symmetries, and error domains must be connected by typed maps.

This paper therefore reports a relationship atlas. It does not use repaired or unrepaired downstream claims as evidence for its own conclusion.

# Typed relationship vocabulary

Let an MTT realization be denoted
``` math
\mathfrak M=(\mathcal S_M,\mathcal D_M,\mathcal O_M,\Theta_M)
```
and a target framework by
``` math
\mathfrak T=(\mathcal S_T,\mathcal D_T,\mathcal O_T,\Theta_T),
```
where $`\mathcal S`$ is a state/configuration space, $`\mathcal D`$ is a dynamics or equation class, $`\mathcal O`$ is an observable algebra or map, and $`\Theta`$ records parameters and branches.

<div class="definition">

**Definition 1** (Embedding). *An embedding is an injective typed map $`E:\mathcal S_T\to\mathcal S_M`$ that preserves a declared list of target structures and observables. It shows that a target model can be represented inside one MTT realization. It does not show that MTT selects that image.*

</div>

<div class="definition">

**Definition 2** (Controlled reduction). *A controlled reduction is a map $`R:\mathcal S_M^{\rm adm}\to\mathcal S_T`$ on a declared admissible domain such that dynamics and observables commute up to a quantified error:
``` math
d_T(R\mathcal D_M^t x,\mathcal D_T^tRx)\le\varepsilon_D(t,x),
 \qquad
 \|\mathcal O_M(x)-\mathcal O_T(Rx)\|\le\varepsilon_O(x).
```*

</div>

<div class="definition">

**Definition 3** (Reconstruction). *A reconstruction begins with target-compatible data and builds an MTT realization whose reduced state, dynamics, or observables reproduce the target within a declared domain. It is not a source-independent derivation when the target structure is supplied as input.*

</div>

<div class="definition">

**Definition 4** (Conditional bridge). *A conditional bridge proves a target relation after adding hypotheses not selected by the MTT core, such as a gauge group, physical action, complex Hilbert representation, compactification, noise law, or branch.*

</div>

<div class="definition">

**Definition 5** (Interpretive correspondence). *An interpretive correspondence identifies analogous structures or explanatory language without a structure-preserving state/dynamics/observable map.*

</div>

<div class="definition">

**Definition 6** (Calibration and postdiction). *A calibration fixes parameters or branches using measured or target-derived data. Reproducing those data is a postdiction or round-trip check. A held-out prediction uses no target information in construction, calibration, scale setting, error choice, or branch selection.*

</div>

An exact derivation is stronger than all of these: the target structure and observables must follow from source data that do not already encode the target.

# Containment certificate

<div id="def:certificate" class="definition">

**Definition 7** (Containment certificate). *A claim that $`\mathfrak M`$ contains $`\mathfrak T`$ must specify:*

1.  *the exact MTT realization and target model;*

2.  *typed state/configuration maps $`E`$ or $`R`$;*

3.  *operator domains, constraints, gauges, and boundary conditions;*

4.  *a dynamics-commutation diagram, exact or with error $`\varepsilon_D`$;*

5.  *an observable map and error $`\varepsilon_O`$;*

6.  *symmetry, locality, positivity, anomaly, and conservation obligations;*

7.  *the validity domain and failure conditions;*

8.  *parameter, scale, and branch provenance;*

9.  *whether target data entered construction or selection; and*

10. *a canonicality statement explaining whether the realization is unique, selected, or one among many.*

</div>

<div class="proposition">

**Proposition 8** (Motif reuse is not containment). *Sharing a spectral gap, projector, fixed point, variational functional, or effective field vocabulary does not imply a containment certificate.*

</div>

<div class="proof">

*Proof.* The shared object supplies none of the missing typed state, dynamics, observable, domain, error, or canonicality data in Definition <a href="#def:certificate" data-reference-type="ref" data-reference="def:certificate">7</a>. ◻

</div>

Relationships also do not compose automatically. An embedding of $`T_1`$ into an MTT model and a reduction of a different MTT model to $`T_2`$ provide no map from $`T_1`$ to $`T_2`$ unless the two realizations and their domains are connected.

# Underdetermination and canonical selection

Let $`\mathfrak R`$ be a class of admissible MTT realizations and let
``` math
\mathcal P:\mathfrak R\to\mathcal D
```
map each realization to the target observables compared with data.

<div id="thm:under" class="theorem">

**Theorem 9** (Realization underdetermination). *If $`\mathcal P`$ is noninjective, agreement with a datum $`d\in\mathcal D`$ selects at most the fiber $`\mathcal P^{-1}(d)`$ and does not select a unique MTT realization. A unique physical model requires additional source-independent selection data or a canonicality theorem.*

</div>

<div class="proof">

*Proof.* If $`\mathcal P`$ is noninjective, there are inequivalent $`\mathfrak M_1\ne\mathfrak M_2`$ with $`\mathcal P(\mathfrak M_1)=\mathcal P(\mathfrak M_2)`$. The target datum cannot distinguish them. Any rule choosing one uses information beyond that datum. ◻

</div>

<div class="corollary">

The existence of one target-compatible MTT reconstruction proves realizability, not that the target is forced or that the reconstruction is unique.

</div>

Multiple compatible encodings are useful for comparison but increase underdetermination until a canonical source theorem relates or selects them.

# Authoritative internal MTT spine

The corrected internal results currently available are:

- a dimension-neutral Hilbert-bundle Foundation with the canonical $`M_{10}\to Y_4`$ physical realization;

- a strongly commuting joint vertical operator or one total internal operator and coherent projector;

- conditional projected time-step fixed points and strict-Lyapunov equilibrium promotion;

- complementary damping, deterministic/stochastic disturbance floors, curved-cluster persistence, leakage, and intrinsic first-order modulation;

- frozen linear OU covariance and correctly normalized correlation bounds;

- typed projection, descent, section, decoder, and admissibility results;

- principal-symbol signature compatibility and locality descent; and

- an internal/physical scale and provenance ledger;

- the local world-in-world decomposition $`\operatorname{Mat}(3,\mathbb R)=\mathfrak{so}(3)\oplus
  \operatorname{Sym}(3,\mathbb R)`$ with strain dimensions $`1+2+3`$; and

- the selected q79 trace-split carrier $`L_{\rm shared}\otimes(\mathcal O\oplus\mathcal A_0\oplus\mathcal A)`$ of rank $`1+2+3=6`$.

These are rigorous internal modules under their hypotheses. They are not a master physical action and do not select target-framework data automatically. In particular, equality of the two $`1+2+3`$ dimension profiles does not identify their bundles, metrics, connections, or operators. That step requires an explicit same-source intertwiner. The q79 signed sheet representation has a local binary-dihedral spin lift, while a strict global Spin lift still requires the branch-relator sign or obstruction-class calculation.

The q79 Fu–Yau branch is the current selected global compactification candidate. The model $`L(3,1)\times\mathrm{Nil}_3`$ remains an auxiliary or effective geometry. Literal $`S^1\times\mathrm{Lens}\times\mathrm{Nil}`$ and literal manifold nesting are not used as proof sources in this atlas.

# Current cross-framework atlas

## General Relativity

**Current relationship: conditional physical completion and controlled reduction target.**

The corrected spine can host a globally hyperbolic Lorentzian base and preserve the principal symbol under coherent compression. A GR relationship requires a selected local gravitational action or equations, constraint propagation, gauge control, a stress tensor, and an error-controlled infrared map. The positive Gram construction does not derive the metric, and the FP stabilization flow is not Einstein evolution. GR is therefore not derived by the present atlas.

## Quantum Mechanics

**Current relationship: reconstruction/interpretive bridge with open probability source.**

Projection and basin structure can represent reduced alternatives and stable states. A quantum reconstruction must additionally supply a complex Hilbert space, linear unitary dynamics or a specified open-system law, observables, CCR where relevant, and the Born probability functional. Projection alone does not create a measure. The Born rule and full quantum equivalence remain separate theorems.

## Quantum Field Theory and AQFT

**Current relationship: conditional reconstruction with one locality descent theorem.**

Fiberwise coherent compression of a compatible upper local net preserves isotony and spacelike commutation. This is a meaningful AQFT-style bridge. A full interacting QFT still requires fields/operator algebras, states, renormalized dynamics, covariance, spectrum/positivity, scattering or local observables, and anomaly control. Modal diagrammatic resemblance is not a derivation of Feynman rules.

## Standard Model

**Current relationship: candidate reconstruction and computational matching program.**

Gauge, representation, family, Yukawa, CKM/PMNS, Higgs, anomaly, threshold, and precision data must arise from one selected source realization. Benchmark matrices, parity checks, fitted scalar rows, or measured-input replay can test a construction but do not establish same-source equivalence. Exact SM closure is not used as evidence in this atlas pending repaired source and observable certificates.

## Effective Field Theory

**Current relationship: local controlled reduction template.**

The Foundation Schur–Feshbach theorem bounds a local linear eliminated-sector correction under explicit domain and inverse assumptions. The Baseline Scales paper separates the internal gap from the four-dimensional EFT cutoff. A full EFT relationship must control nonlinear remainders, symmetries, power counting, matching, RG evolution, and the validity interval.

## Kaluza–Klein theory

**Current relationship: conditional reconstruction.**

For a supplied product action $`-\Box_4\otimes I+I\otimes A_{\rm int}+m_0^2`$, internal eigenfunctions produce $`m_k^2=m_0^2+\lambda_k`$. Warping, mixing, interactions, and boundary conditions require further matching. This is one of the clearest current cross-framework bridges, but it does not select the compactification.

## Noncommutative geometry and spectral triples

**Current relationship: possible embedding/reformulation.**

Given an algebra, Hilbert representation, Dirac operator, grading, and real structure satisfying the spectral-triple axioms, those data can be compared or embedded in an MTT internal operator model. The MTT triplet and gap alone do not select the algebra, real structure, KO dimension, or spectral action.

## String/M-theory and Calabi–Yau compactification

**Current relationship: encoding/reconstruction program.**

An MTT realization may encode a supplied compactification, worldsheet, flux, or moduli problem. Full containment requires worldsheet consistency, modular invariance, anomaly cancellation, dualities, branes/fluxes, and the relevant low-energy matching. The canonical MTT geometry does not by itself derive string theory or select a Calabi–Yau manifold.

## Heterotic Hull–Strominger systems

**Current relationship: conditional solution-slice reconstruction.**

Known Hull–Strominger or Fu–Yau solutions may provide target-compatible backgrounds and inspiration for source operators. A unique minimizer requires a proved functional, domain, coercivity/compactness, strictness modulo gauge, and a demonstration that its Euler–Lagrange equations equal the selected system. No unique-vacuum or landscape-elimination theorem is asserted here.

## Quantum gravity

**Current relationship: open conditional program.**

Filtered propagators or proper-time factors can improve individual integrals, but UV finiteness of every graph, BV/QME validity, reflection positivity, causal support, BRST lifting, nonperturbative existence, Borel summability, physical Hilbert space, and unitary scattering are independent obligations. The former all-loop constructive-QG conjunction is withdrawn as evidence for the superset claim.

## Loop quantum gravity

**Current relationship: interpretive/encoding correspondence.**

Graphs, holonomies, fluxes, and discrete spectra can be compared with coherent network or spectral structures, but a containment needs the LQG kinematical and physical Hilbert spaces, constraints, operator algebra, dynamics, and semiclassical map. No Barbero–Immirzi prediction is established here.

## Asymptotic safety and functional RG

**Current relationship: conditional truncation-shadow interpretation.**

An MTT coherent-sector flow may be projected into an FRG truncation if a scale-dependent effective action and map are constructed. Similar fixed-point language does not identify stabilization time with RG scale or prove an asymptotically safe UV fixed point.

## Causal sets

**Current relationship: effective encoding correspondence.**

Poisson sprinkling of an already selected Lorentzian spacetime gives a causal set by a standard external construction. Event-selection histories may also define partial orders after a physical causal relation is supplied. MTT admissibility alone does not derive local finiteness, a causal order, or causal set dynamics.

# Shared quantities and the same-source requirement

Writing one symbol $`\Theta`$ in several sector formulas does not prove that the same physical primitive controls those sectors. A same-source claim requires one selected source space $`\Theta_{\rm src}`$ and maps
``` math
F_a:\Theta_{\rm src}\to\mathcal O_a
```
for every sector $`a`$, with common units, normalization, branch, and uncertainty provenance.

<div class="proposition">

**Proposition 10** (Shared-symbol insufficiency). *If sector formulas use parameters with the same name but no equality theorem from a common source, cross-sector fitting does not test one shared knob.*

</div>

<div class="proof">

*Proof.* Without a source equality, the sector parameters are independent coordinates that happen to share notation. Adjusting them separately cannot falsify a common-source hypothesis because no such hypothesis has been defined. ◻

</div>

The Baseline Scales consistency set is the appropriate next gate. A global fit becomes meaningful only after all response maps are emitted from the same realization. Synthetic or mock fits validate software and identifiability, not physical closure.

# Predictive closure ladder

The status of a cross-framework link should be reported on the following ladder:

1.  interpretive analogy;

2.  typed state or operator map;

3.  structural embedding or reduction;

4.  dynamics and constraint compatibility;

5.  observable matching with controlled error;

6.  one common consistency witness with full provenance;

7.  source-independent canonical selection; and

8.  held-out empirical prediction.

Skipping a rung changes the claim rather than completing it. In particular, observable replay does not prove canonical selection, and canonical selection without held-out data is not empirical prediction.

# Falsifiability and upgrade protocol

A specific relationship claim is falsified if its typed map cannot be defined, its domains are inconsistent, its commutation/error bound fails, an anomaly or positivity obligation fails, or a held-out observable misses its acceptance set. The broad MTT program is not tested by one vague superset assertion; each certificate supplies a local, checkable target.

To upgrade an atlas row, a downstream paper must:

1.  name the current relationship type;

2.  fill every item in the containment certificate;

3.  identify all target-derived inputs;

4.  prove or compute one common realization;

5.  compare inequivalent branches and state residual underdetermination; and

6.  reserve “derivation,” “containment,” and “prediction” for the rung actually reached.

# Scoped atlas theorem

<div id="thm:atlas" class="theorem">

**Theorem 11** (Typed MTT relationship atlas). *The corrected MTT spine supports conditional fixed-point/control results and several typed cross-framework bridges, including local operator reduction, coherent locality descent, and product-action internal-mode reconstruction. Each broader relationship listed in this paper is valid only at its declared type and under its own certificate. No universal containment theorem follows from the collection of partial relationships. If multiple inequivalent MTT realizations reproduce the same target data, the physical realization remains underdetermined until a source-independent canonicality theorem is supplied.*

</div>

# Conclusion

MTT can still function as a serious unification program without claiming to have already derived every framework it can describe. The corrected atlas makes progress measurable: embeddings, reconstructions, reductions, physical bridges, same-source maps, and predictions each have explicit gates. The current corpus contains a rigorous internal spectral/control spine and several promising conditional bridges. Completing the superset ambition requires constructing the remaining certificates, selecting one physical realization, and testing genuinely held-out consequences.

<div class="thebibliography">

99

P. Nero, *Modal Triplet Theory: Foundations*, revised v7, 2026.

P. Nero, *Fixed Points I–VI*, corrected theorem spine, 2026.

P. Nero, *The Projection–Admissibility Principle: Descent, Recovery, and Structural Constraints on Effective Description*, revised v2, 2026.

P. Nero, *Baseline Scales and Phenomenological Consistency in Modal Triplet Theory*, revised v2, 2026.

</div>
