---
abstract: |
  Modal Triplet Theory (MTT) derives quantum mechanics, quantum field theory, spacetime geometry, irreversibility, and cosmology from a projection-based architecture with finite admissibility. While these results are technically explicit and mutually consistent, questions naturally arise regarding the status of parameters, residual degrees of freedom, and falsifiability.

  In this work we provide a unified accounting of all parameters appearing in MTT. We classify them according to structural necessity, bounded geometric control, superset latent variables, and remaining bottleneck degrees of freedom, and explain how many apparent parameters collapse into a small set of invariant admissibility margins. We then develop a systematic falsifiability framework appropriate to projection-based theories, identifying exact no-go results, bounded inequality violations, cross-sector closure failures, and near-term physical discriminators.

  This paper does not extend the dynamics of Modal Triplet Theory. Its purpose is to make explicit the conditions under which the existing theory would fail.
author:
- Peter Nero
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: 2aed535c6bfeb44a143e4afbf94e4da2639bc7f20b217befcf64539db9535adc
paper_id: modal-triplet-theory-parameters-closure-and-structural-ae734bf0
release_state: zenodo_released
released_version: v1.0
title: "**Modal Triplet Theory: Parameters, Closure, and Structural Falsifiability**"
zenodo_doi: 10.5281/zenodo.18255574
zenodo_record_id: 18255574
zenodo_url: "https://zenodo.org/records/18255574"
---

# Introduction

Modal Triplet Theory has been developed across a corpus of technical papers establishing the emergence of quantum mechanics, quantum field theory, spacetime geometry, irreversibility, and cosmology from a common projection-based architecture. These results are mathematically explicit and mutually consistent, and they reproduce the successful predictions of established theories within their domains of validity.

At the same time, foundational scrutiny naturally focuses on two questions:

1.  What parameters remain free in the theory?

2.  In what precise sense is the theory falsifiable?

In conventional effective field theories, these questions are answered by listing couplings, masses, and scales and describing how experimental data exclude regions of parameter space. For projection-based theories such as MTT, this approach is inadequate. Many quantities that appear as parameters in intermediate descriptions are not tunable inputs but structural margins controlling the viability of effective description.

The purpose of this paper is to replace informal parameter counting with a precise structural analysis. We identify all parameters and degrees of freedom appearing in Modal Triplet Theory, classify their logical status, explain their interdependence, and articulate a falsifiability framework suited to projection-based physics.

# Two Levels of Description and the Meaning of “Parameter”

## Fundamental configuration versus effective observable description

All constructions in Modal Triplet Theory distinguish two levels of description.

At the fundamental level, the theory posits a high-dimensional configuration space equipped with deterministic and invertible dynamics. No stochasticity, irreversibility, or collapse is assumed at this level.

At the effective level, observable physics is defined via a noninjective projection from the configuration space to a space of effective states. This projection is stable only within a restricted admissible domain and is accompanied by controlled truncation of noncoherent degrees of freedom.

Observable physics is therefore identified not with individual microscopic configurations, but with equivalence classes defined by projection.

## Parameters in projection-based theories

In this setting, the notion of a “free parameter” differs fundamentally from its role in effective field theory. A parameter in Modal Triplet Theory is any degree of freedom that has not yet been fixed by:

- projection structure,

- admissibility constraints,

- fixed-point stability,

- or cross-sector closure.

A parameter is thus free only provisionally. Failure to eliminate such freedom does not invite tuning; it constitutes falsification of the present formulation.

This distinction underlies the parameter taxonomy developed in the following sections.

# Minimal Structural Axioms

We briefly recall the minimal axioms underlying Modal Triplet Theory, as identified explicitly in the closure analysis of the MTT corpus.

Axiom A1 (Invertible Fundamental Dynamics).  
The fundamental evolution on the configuration space is deterministic and invertible.

Axiom A2 (Noninjective Projection).  
Observable states are defined via a projection from the configuration space that identifies multiple microscopic configurations.

Axiom A3 (Admissible Domain).  
There exists a nonempty domain on which the projection-based effective description is stable and predictive.

Axiom A4 (Finite Admissibility Margin).  
Stability of the effective description is controlled by a finite margin that can be exhausted under disturbance.

These axioms introduce no stochasticity, collapse postulate, or fundamental irreversibility. They encode only the structural requirements for finite, stable, and predictive description. All subsequent phenomena derived in MTT follow from these assumptions alone.

# Parameter Taxonomy in Modal Triplet Theory

This section provides a complete classification of all parameters and degrees of freedom appearing in Modal Triplet Theory. The classification is exhaustive and mutually exclusive.

## Structural (Non–Tunable) Control Data

The following quantities are required for the existence of effective description and do not represent adjustable freedom:

- existence of a uniform spectral gap on internal bundles,

- boundedness and regularity of the coherent projection,

- contractivity of the projected flow (FCC),

- noninvertibility of effective evolution at admissibility collapse.

These are not continuous parameters. They are binary structural conditions: either they hold, or the theory ceases to apply. No tuning is possible.

#### Status.

Structural control data are either proved theorems or required hypotheses. They do not contribute to parameter freedom.

## Geometric and Coherence Degrees of Freedom

Internal geometric quantities appear throughout the MTT corpus, including:

- internal length and curvature scales,

- projector regularity gradients,

- truncation tolerances and error bounds.

Crucially, these quantities do not enter effective physics independently. Across the MTT corpus they are shown to quantify a single invariant resource: the remaining margin by which projection remains admissible.

We refer to this invariant as the *coherence capacity*, denoted $`C_{\mathrm{MTT}}(x)`$.

#### Interpretation.

Many apparent parameters collapse into this single scalar margin. Geometry functions as consistency bookkeeping for admissibility strain rather than as a source of new degrees of freedom.

#### Status.

Geometric and coherence quantities are bounded and derived. They do not represent free parameters.

## Superset Latent Parameters

At the level of the “MTT as a superset” formulation, a small number of continuous latent quantities remain. These are not structural necessities but bookkeeping parameters encoding how admissibility is distributed across sectors.

They consist of:

- an overall normalization scale $`K`$,

- two intrinsic dimensionless ratios $`\zeta_2/\zeta_1`$ and $`\zeta_3/\zeta_1`$.

Only the ratios are intrinsic. Absolute normalization collapses into a single scalar. These parameters are overconstrained by cross-sector closure conditions.

#### Interpretation.

These quantities do not represent new dynamics or interactions. They encode how equivalence classes under projection are weighted across different sectors.

#### Status.

Superset latent parameters are constrained but not yet derived. Failure to collapse them under a unifying principle falsifies the superset claim.

## Gauge–Flavor Bottleneck

Residual freedom associated with flavor appears in discrete or phase-like form:

- Wilson-line or holonomy choices,

- localization patterns of zero modes,

- mixing matrices and CP phases.

These are not continuous tunable parameters. They represent the final unresolved bottleneck in the present formulation.

#### Superset requirement.

In a closed formulation, these degrees of freedom must collapse into the same bottleneck data that fix the gauge and gravitational sectors. Their persistence constitutes falsification rather than tunability.

## Proxy Knobs and Forbidden Adjustments

Certain adjustments may mimic missing structure but are explicitly disallowed in a closed theory:

- entry-wise Yukawa rescalings,

- independent phase fitting,

- sector-local parameter adjustments.

Such proxy knobs may appear in intermediate explorations but must disappear in the final formulation. Their necessity signals failure of the present theory.

## Summary of Parameter Status

Modal Triplet Theory admits:

- no freely tunable structural parameters,

- no independent geometric parameters beyond coherence capacity,

- three continuous latent superset variables,

- one discrete gauge–flavor bottleneck.

The theory is therefore highly constrained. Residual freedom is sharply delimited, and failure to collapse it constitutes falsification.

# Dependency Structure of Remaining Freedom

The remaining degrees of freedom in Modal Triplet Theory are not independent. They are arranged in a strict hierarchical dependency structure. This structure is essential for understanding both the small number of parameters and the large number of falsifiers admitted by the theory.

## Hierarchical dependency graph

The logical dependency of quantities in MTT can be summarized schematically as follows:

<div class="center">

    Structural axioms
       ↓
    Admissibility and projection
       ↓
    Coherence capacity C_MTT
       ↓
    Effective gravity (G_eff)
       ↓
    Superset latent variables (K, ζ ratios)
       ↓
    Gauge normalization and couplings
       ↓
    Discrete gauge–flavor bottleneck

</div>

Each level depends on the consistency of the levels above it. No lower level can be freely adjusted without violating constraints imposed by higher levels.

## Consequences of hierarchical dependence

This structure has several immediate consequences:

- There is no independent tuning across sectors. Adjustments at lower levels necessarily affect higher-level consistency conditions.

- Apparent parameters at intermediate stages are revealed as bookkeeping devices rather than physical degrees of freedom.

- Cross-sector consistency becomes a primary diagnostic of validity.

In particular, the coherence capacity functions as a unifying invariant that mediates between geometry, dynamics, and effective gravitational response.

## Absence of landscape freedom

Because all continuous degrees of freedom are either structural prerequisites or latent variables subject to cross-sector closure, MTT does not admit a continuous landscape of equally valid low-energy effective theories. Distinct admissible configurations belong to the same universality class rather than representing tunable alternatives.

Failure of this collapse would falsify the present formulation.

# Why Few Parameters Imply Many Falsifiers

The combination of few parameters and many falsifiers is a characteristic feature of projection-based theories. This section explains why this feature arises naturally in MTT.

## Structural overconstraint

MTT imposes a large number of independent constraints on a small set of degrees of freedom. Once structural prerequisites are fixed, each additional observable becomes a redundant consistency check.

As a result, falsification does not require fine-grained numerical disagreement. Structural or bounded violations suffice.

## Superset multiplication

In the superset formulation, gauge, gravitational, flavor, and cosmological sectors depend on the same latent parameters. Each sector therefore constrains the others.

If a single sector requires additional freedom not shared by the others, the entire superset construction fails. This produces a multiplicative growth of falsifiers as more observables are considered.

## Structural versus numerical falsifiability

Most falsifiers in MTT do not take the form “observable $`X`$ differs from predicted value $`X_0`$”. Instead, they assert:

- impossibility of certain constructions,

- violation of derived bounds,

- failure of cross-sector closure.

This form of falsifiability is both stronger and more fragile than parameter exclusion. It admits many independent failure modes despite minimal parameter freedom.

## Falsifier templates

Rather than enumerating all possible falsifiers, MTT organizes them into templates. Each template generates families of concrete tests as regimes and observables are specified.

The templates and representative exemplars are collected in Appendix C.

## Interpretation

The large number of falsifiers admitted by MTT is not evidence of arbitrariness. It is the expected consequence of a theory whose effective descriptions are controlled by projection with finite admissibility margins.

Few parameters imply that failure cannot be absorbed by retuning. Instead, failure manifests as violation of structure.

# Structural Falsifiability Catalogue

This section summarizes the principal classes of falsifiability admitted by Modal Triplet Theory. A detailed template-based catalogue is provided in Appendix C; here we present the main classes and their conceptual significance.

## Exact and Structural No-Go Falsifiers

The strongest falsifiers in MTT are exact no-go results. These assert the impossibility of certain constructions within the stated axioms.

Representative examples include:

- the non-existence of a global measurable right inverse of the coherent projection across admissibility collapse;

- the impossibility of globally reversible measurement completion once admissibility is exhausted;

- stability of universality classes under admissible microscopic variation.

Violation of any such no-go result falsifies the present formulation without recourse to parameter adjustment.

## Bounded and Inequality-Based Falsifiers

A second class of falsifiers arises from bounds and inequalities derived in the theory. These include:

- representation-correct curvature–gap drift bounds;

- disturbance–damping stability inequalities;

- separation of coherent contraction from internal spectral suppression.

These falsifiers test whether observed behavior lies within admissible bounds in regimes where the MTT assumptions apply. Persistent violation falsifies the corresponding mechanism.

## Superset Closure Falsifiers

In the superset formulation, multiple physical sectors depend on the same latent parameters. This produces a powerful class of falsifiers based on overconstraint.

Examples include:

- failure of redundant constraints after fixing latent parameters in one sector;

- necessity of proxy knobs to reproduce flavor observables;

- incompatibility between gauge-sector fits and gravitational behavior.

Any such failure falsifies the superset claim rather than enlarging the parameter space.

## Near-Term Physical Discriminators

Finally, MTT admits falsifiers that connect directly to observation without requiring full numerical execution. These include:

- state-selection constraints in curved backgrounds;

- irreversibility signatures associated with admissibility bottlenecks and horizons.

These discriminators provide concrete avenues for empirical stress-testing.

# Why Exhaustive Enumeration Is Neither Possible Nor Useful

Given the structure of MTT, an exhaustive list of falsifiers is neither feasible nor desirable.

## Combinatorial growth of falsifiers

Each admissibility condition generates families of no-go and bounded falsifiers. When combined with multiple physical sectors and regimes, the number of concrete falsifiers grows combinatorially.

## Regime qualification

Proper falsifiers must specify the regime in which they apply. Listing all regime-qualified instantiations would obscure, rather than clarify, the logical structure of the theory.

## Template-based organization

For these reasons, falsifiers are best organized by templates. Templates capture the structural origin of falsifiability and generate many concrete tests as regimes and observables are specified.

This approach is both more honest and more informative than an exhaustive enumeration.

# Comparison with Parameterized Frameworks

It is instructive to contrast the parameter and falsifiability structure of Modal Triplet Theory with that of more conventional theoretical frameworks.

## Effective field theories

In effective field theories, physical predictions are expressed in terms of a large number of couplings and masses. Falsification proceeds by excluding regions of parameter space while leaving the underlying framework intact.

In such theories, the presence of many parameters weakens falsifiability: failure of a prediction typically motivates retuning rather than structural revision.

## Numerical unification schemes

Frameworks that attempt unification through early commitment to Hamiltonians or specific phenomenological structures often reduce parameter counts but retain calibration dependence. Falsifiability is sharp at the level of specific numerical predictions, but structural freedom remains in the choice of calibration and truncation schemes.

## Modal Triplet Theory

MTT differs qualitatively from both approaches.

- It admits no freely tunable structural parameters.

- Apparent geometric freedom collapses into an invariant admissibility margin.

- Remaining continuous freedom is confined to a small set of latent bookkeeping variables.

- Cross-sector closure transforms additional observables into redundant consistency checks.

As a result, MTT is not falsified by numerical mismatch alone, but by violation of structure, bounds, or closure.

# What Remains to Be Proved

The present formulation of Modal Triplet Theory is not complete. Its incompleteness, however, is sharply localized.

The remaining open problems are:

1.  Collapse of superset latent variables $`(K,\zeta_2/\zeta_1,\zeta_3/\zeta_1)`$ via a unifying principle rather than calibration.

2.  Collapse of the gauge–flavor bottleneck without introducing proxy knobs.

3.  Identification of a canonical representative for coherence capacity suitable for numerical and phenomenological work.

4.  Proof of uniform admissibility inheritance across entire universality classes.

Each of these items corresponds to a specific, identifiable obstruction. Resolution would constitute completion; failure would constitute falsification.

# Conclusion

This paper has provided a unified accounting of parameters, degrees of freedom, and falsifiability in Modal Triplet Theory.

We have shown that:

- MTT contains no freely tunable structural parameters.

- Apparent geometric freedom collapses into a single invariant coherence capacity.

- Only three continuous latent variables remain at the superset level, alongside a discrete gauge–flavor bottleneck.

- Failure of these degrees of freedom to collapse falsifies the theory rather than enlarging its parameter space.

- MTT admits a large number of falsifiers despite its minimal parameter content, due to structural overconstraint and cross-sector closure.

Modal Triplet Theory is therefore not a framework that trades predictivity for flexibility. It is a theory that trades early numerical specificity for structural inevitability.

The purpose of this work has not been to extend the dynamics of MTT, but to make explicit the conditions under which it would fail. In doing so, we aim to clarify both the power and the limits of projection-based physics as a foundation for effective description.

# Appendix A: Master Constants and Parameter Status in Modal Triplet Theory

This appendix provides a centralized accounting of all constants, control parameters, and latent quantities appearing in Modal Triplet Theory (MTT). Each item is classified according to its logical status within the theory and its role in technical results.

Throughout, we distinguish between:

- **Structural control data**, which are not tunable parameters but prerequisites for the existence of effective description;

- **Bounded geometric quantities**, which enter only through inequalities and admissibility margins;

- **Latent superset variables**, which remain continuous at the present stage but are overconstrained;

- **Open bottleneck degrees of freedom**, whose collapse or persistence constitutes falsification.

We use the following status labels:

**P**  
Proved or defined in a theorem or construction.

**B**  
Bounded under stated assumptions; numerical value depends on geometry or regime.

**L**  
Latent (introduced for Tier–3 closure; intended to collapse).

**O**  
Open (remaining bottleneck; not yet collapsed).

## A.1 Structural Control Constants (Non–Tunable)

These quantities are required for the theory to exist. They are not adjustable and do not represent physical freedom.

<div class="center">

| **Symbol** | **Meaning** | **Role in Theory** | **Status** |
|:---|:---|:---|:--:|
| $`\lambda_\ast`$ | Uniform spectral gap on internal bundles | Controls suppression of noncoherent modes; enables Riesz projection | P/B |
| $`\Pi_{B_n}`$ | Riesz projector on bundle $`B_n`$ | Defines harmonic sector on each internal factor | P |
| $`\Pi_{\mathrm{coh}}`$ | Joint coherent projector | Defines coherent sector $`H_{\mathrm{coh}}`$ | P |
| $`Q := I-\Pi_{\mathrm{coh}}`$ | Noncoherent projector | Separates decaying modes from coherent dynamics | P |
| $`T_\tau`$ | Projected flow $`T_\tau=\Pi_{\mathrm{coh}}\circ\Phi_\tau`$ | Defines effective evolution | P |
| $`q_{\mathrm{coh}}(\tau)`$ | Coherent contraction factor | Ensures uniqueness and convergence of coherent fixed point (FCC) | P/B |

</div>

#### Remarks.

- The spectral gap $`\lambda_\ast>0`$ is not a tunable parameter. If it fails, admissibility fails and effective physics ceases to exist.

- The contraction factor $`q_{\mathrm{coh}}`$ is *not* derived from $`\lambda_\ast`$ alone; it requires base dissipation or coherent monotonicity. This separation is structural.

## A.2 Projector Regularity and Truncation Control

These constants quantify how stable projection and truncation remain under perturbation.

<div class="center">

| **Symbol** | **Meaning** | **Role in Theory** | **Status** |
|:---|:---|:---|:--:|
| $`C_\Pi`$ | Projector norm bound | Controls amplification of errors under projection | P/B |
| $`\|\partial_y g_{B_n}\|`$ | Base variation norm | Enters bounds on $`\|\Pi_{B_n}\|`$ | B |
| $`\Delta`$ | Coherent–noncoherent separation | Ensures controlled truncation | P |
| $`C_{\mathrm{trunc}}`$ | Truncation error constant | Bounds truncation corrections $`\|\Delta T\|`$ | P/B |

</div>

#### Upgrade path.

To upgrade these from bounded to fully explicit, one would need:

- uniform bounds on base variation for a canonical geometry class;

- a numerical evaluation of $`C_\Pi`$ and $`C_{\mathrm{trunc}}`$ on that class.

## A.3 Disturbance–Damping and Stability Constants

These appear in the OU stability and admissibility analyses.

<div class="center">

| **Symbol** | **Meaning** | **Role in Theory** | **Status** |
|:---|:---|:---|:--:|
| $`\delta_{n,k}`$ | Disturbance amplitudes | Strength of off–harmonic driving | B/E |
| $`\gamma_{n,k}`$ | Damping rates | Ensures variance suppression | B |
| $`\gamma_{\min}`$ | Uniform damping bound | Stability margin for OU control | B |
| $`\varepsilon`$ | Summability exponent | Ensures convergence of disturbance sums | E |

</div>

## A.4 Coherence Capacity (Invariant Compression)

Coherence capacity is the central invariant controlling all effective description.

<div class="center">

| **Symbol** | **Meaning** | **Role in Theory** | **Status** |
|:---|:---|:---|:--:|
| $`C_{\mathrm{MTT}}(x)`$ | Coherence capacity | Invariant admissibility margin; collapses multiple controls | P |
| $`G_{\mathrm{eff}}`$ | Effective Newton coupling | $`G_{\mathrm{eff}}\propto 1/C_{\mathrm{MTT}}`$ in Einstein limit | P (cond.) |

</div>

#### Remarks.

- $`C_{\mathrm{MTT}}`$ is not unique as a functional but unique in meaning.

- It replaces many apparent parameters (gap size, truncation tolerance, projector norm) with a single scalar margin.

## A.5 Superset Latent Variables (Tier–3)

These quantities appear in the “MTT as a superset” formulation and are the only remaining continuous degrees of freedom.

<div class="center">

| **Symbol** | **Meaning** | **Role in Theory** | **Status** |
|:---|:---|:---|:--:|
| $`K`$ | Overall normalization scale | Fixes absolute gauge coupling normalization | L |
| $`\zeta_1,\zeta_2,\zeta_3`$ | Harmonic normalization weights | Relative overlap strengths of modal bundles | L |
| $`\zeta_2/\zeta_1,\;\zeta_3/\zeta_1`$ | Intrinsic ratios | Gauge–sector intrinsic data | L |

</div>

#### Remarks.

- Only ratios of $`\zeta_r`$ are intrinsic; absolute normalization is absorbed into $`K`$.

- These variables are overconstrained by cross–sector closure; failure to collapse falsifies the superset claim.

## A.6 Gauge–Flavor Bottleneck (Open)

<div class="center">

| **Quantity** | **Description** | **Role** | **Status** |
|:---|:---|:---|:--:|
| Holonomy phases | Wilson–line / flat connection data | Flavor mixing and CP structure | O |
| Localization data | Zero–mode overlap structure | Yukawa hierarchies | O |

</div>

#### Interpretation.

These quantities are discrete or phase–like and are not continuous tunable parameters. They constitute the final unresolved bottleneck. Their collapse under admissibility or unifying principles is required for full closure.

## A.7 Summary

Modal Triplet Theory contains:

- no freely tunable structural parameters;

- bounded geometric quantities compressed into coherence capacity;

- three latent continuous variables at the superset level;

- one discrete gauge–flavor bottleneck.

The theory is therefore highly constrained. Failure of the remaining degrees of freedom to collapse constitutes falsification rather than parameter tuning.

# Appendix B: Knob Taxonomy and Residual Degrees of Freedom

This appendix classifies all adjustable or seemingly adjustable quantities appearing in Modal Triplet Theory (MTT) into a small number of conceptually distinct categories, which we refer to as *knobs*. The purpose of this taxonomy is to distinguish genuine freedom from structural control data, to make explicit where residual degrees of freedom remain, and to specify which forms of adjustment are forbidden in a closed formulation.

Throughout this appendix, a *knob* does not mean a tunable parameter in the sense of effective field theory. A knob is any degree of freedom that could, in principle, be varied independently unless constrained by admissibility, projection, or cross-sector closure.

## B.1 Overview of Knob Classes

All knobs in MTT fall into exactly one of the following five classes:

1.  Structural (Non–Tunable) Knobs,

2.  Geometric and Coherence Knobs,

3.  Gauge and Flavor Bottleneck Knobs,

4.  Proxy Knobs (Forbidden in a Closed Theory),

5.  Unifying Knobs (Explicitly Conjectural).

This classification is exhaustive. No additional categories of freedom appear in the MTT corpus.

## B.2 Structural (Non–Tunable) Knobs

Structural knobs are prerequisites for the existence of effective description. They are not adjustable and do not represent physical freedom.

<div class="center">

| **Knob** | **Description** | **Why Non–Tunable** |
|:---|:---|:---|
| Projection structure | Noninjective mapping to observables | Required for any finite, stable description |
| Admissibility | Existence of a stable domain | Without it, no effective physics exists |
| Spectral suppression | Gap separating coherent/noncoherent modes | Failure implies breakdown of description |
| FCC contractivity | Coherent-sector contraction | Ensures uniqueness and stability of fixed points |
| Finite capacity | Bounded admissibility margin | Structural necessity of projection |

</div>

#### Interpretation.

Structural knobs are binary conditions rather than continuous parameters. They cannot be tuned: if any of them fails, the theory ceases to apply. They therefore do not contribute to parameter freedom.

## B.3 Geometric and Coherence Knobs

Geometric and coherence knobs arise from the internal realization of the theory. They include quantities such as internal radii, curvature scales, warp factors, and projector regularity measures.

<div class="center">

| **Knob** | **Description** | **Status** |
|:---|:---|:---|
| Internal length scales | Fiber radii, compactification scales | Bounded by admissibility |
| Curvature scales | Scalar and Ricci curvature | Enter drift bounds only |
| Projector gradients | $`\|\nabla \Pi\|`$ regularity | Bounded for admissibility |
| Truncation tolerances | Error control margins | Bounded by spectral separation |

</div>

#### Key result.

All geometric and coherence knobs collapse into a single invariant quantity: the coherence capacity $`C_{\mathrm{MTT}}`$. They do not survive as independent degrees of freedom in effective physics.

#### Consequence.

Variation of these knobs within admissible bounds does not produce qualitatively different effective theories. They define universality classes rather than tunable parameters.

## B.4 Gauge and Flavor Bottleneck Knobs

Gauge and flavor structure introduces the only remaining unresolved freedom in the current formulation.

<div class="center">

| **Knob** | **Description** | **Nature** |
|:---|:---|:---|
| Holonomy phases | Wilson-line or flat-connection data | Discrete / phase-like |
| Localization patterns | Zero-mode overlap structure | Topological / geometric |
| Mixing matrices | CKM / PMNS structure | Derived, not fundamental |

</div>

#### Interpretation.

These knobs are not continuous parameters. They are discrete or phase-like features tied to topology and global structure.

#### Superset requirement.

In a closed superset formulation, these knobs must collapse into the same bottleneck data that fixes gauge and gravitational sectors. If they do not, the superset claim fails.

## B.5 Proxy Knobs (Forbidden)

Proxy knobs are adjustments that mimic missing structure. They are explicitly disallowed in a closed formulation.

<div class="center">

| **Proxy Knob**               | **Why Forbidden**           |
|:-----------------------------|:----------------------------|
| Entry-wise Yukawa rescaling  | Introduces hidden tuning    |
| Independent phase fitting    | Breaks cross-sector closure |
| Sector-local parameter fixes | Violates universality       |

</div>

#### Interpretation.

Proxy knobs may appear in intermediate phenomenological explorations, but must disappear in a closed theory. Their necessity constitutes falsification of the present formulation rather than an invitation to tuning.

## B.6 Unifying Knobs (Explicitly Conjectural)

Unifying knobs are proposed mechanisms intended to collapse the remaining bottlenecks. They are not yet derived and are explicitly labeled conjectural.

<div class="center">

| **Unifying Knob**         | **Proposed Role**                 | **Status**  |
|:--------------------------|:----------------------------------|:------------|
| Global stability extremum | Selects admissible configurations | Conjectural |
| Spectral extremality      | Maximizes minimal gap             | Conjectural |
| Inter-sector rigidity     | Prevents sector-by-sector tuning  | Conjectural |

</div>

#### Interpretation.

These unifying knobs represent the final step toward full closure. Their success would eliminate the remaining freedom; their failure would falsify the superset claim.

## B.7 Summary and Logical Status

Modal Triplet Theory admits:

- no freely tunable structural knobs;

- no independent geometric parameters beyond coherence capacity;

- three latent continuous variables at the superset level;

- a discrete gauge–flavor bottleneck;

- no permitted proxy tuning.

The knob taxonomy makes explicit where freedom remains and why it is limited. Crucially, it also specifies how and where the theory can fail.

#### Conclusion.

In MTT, remaining knobs do not represent adjustable inputs but unresolved structural bottlenecks. Their persistence or collapse determines the fate of the theory.

# Appendix C: Falsifier Templates

This appendix specifies the classes of falsifiability native to Modal Triplet Theory (MTT) and provides canonical templates from which large families of concrete falsifiers can be generated. The goal is not exhaustive enumeration, but structural clarity.

A *falsifier* is any observation, construction, or consistency failure that contradicts a claim of the present formulation of MTT *within its stated regime of validity*. Introducing new degrees of freedom or relaxing axioms to accommodate such failures constitutes abandonment of the present theory rather than tuning.

## C.1 Philosophy of Structural Falsifiability

In parameterized theories, falsification typically excludes regions of parameter space. MTT differs in that most of its claims are structural, bounded, or cross-sectoral. As a result, falsification often takes the form of impossibility or overconstraint rather than numerical mismatch.

Accordingly, falsifiers in MTT fall into four classes:

1.  Exact or structural no-go falsifiers,

2.  Bounded or inequality-violation falsifiers,

3.  Superset (cross-sector) closure falsifiers,

4.  Near-term physical discriminators.

Each falsifier template specifies:

- the *statement* asserted by MTT,

- the *regime of validity* under which it applies,

- and the explicit *failure condition*.

## C.2 Class A: Exact / Structural No-Go Falsifiers

These falsifiers do not depend on numerical values or model choices.

#### Template A1: No Global Section Across Admissibility Collapse

Statement:  
If coherence capacity vanishes along an effective trajectory, no global measurable right-inverse of the coherent projection exists.

Regime:  
Admissible slabs satisfying the standing assumptions (spectral gap, bounded projector, FCC).

Fail Condition:  
A constructive, measurable section $`S`$ such that $`\Pi_{\mathrm{coh}}\circ S = \mathrm{Id}`$ exists across domains containing coherence-capacity collapse points.

#### Template A2: No Reversible Measurement Completion

Statement:  
Measurement-like selection events that exhaust admissibility are structurally non-invertible at the effective level.

Regime:  
Effective descriptions derived via $`\Pi_{\mathrm{coh}}`$ with finite admissibility margin.

Fail Condition:  
A physically realized measurement protocol whose effective description admits a global inverse without hidden degrees of freedom or basin ambiguity.

#### Template A3: Universality Class Stability

Statement:  
Within an admissible universality class, effective physics is insensitive to microscopic realization.

Regime:  
Small perturbations of internal geometry preserving admissibility.

Fail Condition:  
Macroscopically distinct effective theories arise from admissible micro-variations without barrier crossing.

## C.3 Class B: Bounded / Inequality Falsifiers

These falsifiers test inequalities and bounds derived in MTT.

#### Template B1: Curvature–Gap Drift Violation

Statement:  
Representation-correct curvature–gap drift coefficients must lie within the bounds dictated by Bochner–Weitzenböck/Lichnerowicz identities.

Regime:  
Slowly varying curvature, preserved spectral gap, valid adiabatic tracking.

Fail Condition:  
Observed effective mass drift coefficients incompatible with the predicted representation-dependent bounds.

#### Template B2: Disturbance–Damping Instability

Statement:  
In OU-controlled regimes, off-harmonic variances remain finite under the stated summability conditions.

Regime:  
Positive damping margin and summable disturbance amplitudes.

Fail Condition:  
Persistent variance growth while all admissibility assumptions remain satisfied.

#### Template B3: FCC Contraction Source Confusion

Statement:  
Contraction on the coherent sector cannot arise from the internal spectral gap alone.

Regime:  
Systems satisfying the FCC hypotheses.

Fail Condition:  
Coherent contraction observed in the absence of base dissipation or coherent monotonicity, driven solely by the internal gap.

## C.4 Class C: Superset Closure Falsifiers

These falsifiers are specific to the “MTT as a superset” formulation.

#### Template C1: Redundant Constraint Failure (Theta Closure)

Statement:  
Latent overlap parameters fixed in one sector must satisfy redundant constraints in others without introducing new degrees of freedom.

Regime:  
Tier–3 superset closure assumptions.

Fail Condition:  
After fixing $`\Theta`$ from one sector (e.g. gauge couplings), independent cross-checks fail unless additional proxy knobs are introduced.

#### Template C2: No-Proxy-Knob Flavor Failure

Statement:  
Flavor observables must reduce to the same bottleneck data as gauge and gravitational sectors.

Regime:  
Superset formulation with admissibility enforced.

Fail Condition:  
Reproduction of CKM/PMNS structure requires independent entry-wise Yukawa or phase tuning.

#### Template C3: Gravity–Gauge Inconsistency

Statement:  
A single coherence-capacity or bottleneck profile cannot fit gauge data while violating gravitational constraints in the same admissible regime.

Regime:  
Combined gauge–gravity analysis under superset assumptions.

Fail Condition:  
The same $`\Theta`$ implied by gauge data forces $`G_{\mathrm{eff}}`$ behavior inconsistent with observed gravitational tests.

## C.5 Class D: Near-Term Physical Discriminators

These falsifiers connect directly to observation without requiring full numerical execution.

#### Template D1: State Selection in Curved Backgrounds

Statement:  
Admissible-state selection restricts the physically realized state class in certain curved spacetimes.

Regime:  
Curved backgrounds satisfying projection and admissibility assumptions.

Fail Condition:  
Robust observational evidence requires physical states outside the admissible class without invoking barrier events.

#### Template D2: Horizon / Bottleneck Irreversibility

Statement:  
Horizons correspond to admissibility bottlenecks that preclude observer-accessible reconstruction of interior microstates.

Regime:  
Observers confined to one side of a capacity bottleneck.

Fail Condition:  
A physically implementable protocol reconstructs full interior microstate information from exterior observables alone.

## C.6 Why Templates, Not Exhaustive Lists

The number of concrete falsifiers implied by MTT grows combinatorially with:

- the number of admissibility conditions,

- the number of physical sectors,

- the number of regimes,

- and the number of observables.

For clarity and honesty, we therefore provide falsifier templates and representative exemplars. Each template instantiates to many concrete tests as data and regimes are specified.

## C.7 Summary

Modal Triplet Theory admits few free parameters but many independent falsifiers. This is not a contradiction. It is the expected consequence of a theory whose effective descriptions are controlled by projection with finite admissibility margins. Failure of any template above falsifies the present formulation rather than expanding its parameter space.
