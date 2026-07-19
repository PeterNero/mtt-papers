---
abstract: |
  Modal Triplet Theory (MTT) describes observable physics as arising from projection onto admissible coherent sectors of a higher–dimensional modal geometry. Within this framework, many quantities that are traditionally treated as independent or fundamentally distinct—inertia, gravitational coupling, mass generation, time ordering, and family multiplicity—arise as shadows of a single shared internal structure.

  In this paper we identify and analyze that structure: the central circle $`S^1_{\mathrm{cen}}`$, the unique internal component reused across all modal bundles in MTT. We argue that the spectral rigidity and universality of this circle force it to act as a global coherence bookkeeping channel. Distinct physical phenomena then emerge as different projections of the same underlying constraint: inertia as the cost of bending coherent histories, gravity as the spatial redistribution of coherence capacity, time as the monotonic ordering induced by noninvertible projection, and fermion families as holonomy sectors of the same circle.

  Each topic is developed in two stages. We first review the conventional understanding in standard physics, highlighting conceptual tensions and open questions. We then provide an MTT-based explanation centered on the role of the central circle, followed by a technical formulation showing how familiar results—including $`F=ma`$, the equivalence of inertial and gravitational mass, and the Einstein field equations—appear as constraint-preserving consistency conditions within the corresponding admissible encodings. Detailed derivations are collected in appendices.

  The purpose of this work is not to introduce new dynamics, but to make explicit a unifying structure that is already implicit across the MTT corpus. By isolating the role of the central circle, we clarify why mass, inertia, gravity, and time exhibit the universality and rigidity observed in nature, and why their standard descriptions break down coherently at admissibility boundaries such as horizons and selection fronts.
author:
- Peter Nero
current_version: v1.0
date: January 2026
generated_from_main_tex_sha256: 2d936c90b928278540aa9552579d94e21651c09a5936a28c01adc0175b52d696
paper_id: the-central-circle-inertia-mass-gravity-and-time-as-sha-5faa2369
release_state: zenodo_released
released_version: v1.0
title: |
  The Central Circle:  
  Inertia, Mass, Gravity, and Time as Shared Coherence Bookkeeping  
  in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.18283408
zenodo_record_id: 18283408
zenodo_url: "https://zenodo.org/records/18283408"
---

# Introduction and Motivation

Modern physics treats inertia, mass, gravity, and time as conceptually distinct ingredients. Inertia appears in Newtonian mechanics as resistance to acceleration; mass is generated in the Standard Model through electroweak symmetry breaking; gravity is described geometrically by spacetime curvature; and time is introduced as an external parameter with an arrow explained statistically or thermodynamically. Despite their empirical success, these descriptions leave unresolved tensions: the equality of inertial and gravitational mass, the absence of a local gravitational energy density, the gravitational coupling of massless radiation, and the structural origin of the arrow of time.

Modal Triplet Theory approaches these issues from a different starting point. Rather than postulating fundamental interactions or spacetime structure, MTT identifies the conditions under which stable physical description is possible. Observable physics arises only within admissible coherent sectors, selected by spectral gaps, bounded projectors, and contractive dynamics. Geometry, forces, and quantum structure appear as effective encodings valid within such regimes.

## Scope and claim discipline

This paper is a synthetic clarification of a unifying structure that is already present across the MTT corpus. To avoid category errors, we separate three layers of statements:

- **(L1) Internal derivations given here.** We include self-contained calculations where they serve exposition (e.g. the standard worldline limit leading to $`\mathbf{F}=m\mathbf{a}`$, and the constraint-preservation identities for Einstein/Maxwell/Yang–Mills systems).

- **(L2) Imported results from the MTT corpus.** The existence/uniqueness of the coherent sector, boundedness of the joint projector, controlled truncation, the MTT$`\Rightarrow`$GR and MTT$`\Rightarrow`$SM reconstructions, and the selection/barrier theorems are assumed from the corresponding technical papers and are not reproved here.

- **(L3) Structural identifications (interpretive synthesis).** The central claim of this paper is that the central circle $`S^1_{\mathrm{cen}}`$ acts as the unique shared coherence bookkeeping channel, and that inertia, gravity, time ordering, and family multiplicity are distinct shadows of that same constraint. These identifications are consistent with the proved spine, but are presented as a unifying explanatory map rather than as new standalone theorems.

Accordingly, “we show” in this paper should be read as “we make explicit / we synthesize” except where a self-contained derivation is provided in an appendix.

A recurring feature of the MTT construction is the presence of a single internal circle $`S^1_{\mathrm{cen}}`$, reused across all modal bundles. This circle has already been shown to underlie time ordering, fermion family multiplicity via $`\mathbb{Z}_3`$ holonomy, and global phase structure. In this paper we show that its role is more fundamental still: the central circle is the unique shared coherence channel, and its bookkeeping constraints give rise to inertia, gravity, mass, and time as distinct but inseparable projections.

The aim of this paper is to make that role explicit.

## Pointers to corpus results

Technical inputs used implicitly throughout include: (i) the bounded joint projector and coherent fixed-point spine (MTT Foundation; Fixed Points I–VI), (ii) the reconstruction of GR as an infrared encoding (MTT$`\Rightarrow`$GR), (iii) the reconstruction of the Standard Model and the $`\mathbb{Z}_3`$ family mechanism (MTT$`\Rightarrow`$SM), and (iv) the admissibility-barrier / horizon / measurement noninvertibility framework (Irreversibility, Horizons, and Cosmology; Projection–Admissibility / Projection-First series). This paper does not rederive those results, but reorganizes them around the central role of $`S^1_{\mathrm{cen}}`$.

We separate conceptual explanation from technical derivation, proceeding from familiar formulations to the MTT interpretation, and finally to precise equations. In doing so, we provide a unified account of several foundational notions without introducing new postulates or modifying established results. Instead, we show that their observed universality follows from the necessity of a shared coherence constraint in any admissible physical description.

# The Central Circle in Modal Triplet Theory

## Overview

A defining structural feature of Modal Triplet Theory is the presence of a single internal circle $`S^1_{\mathrm{cen}}`$ that is reused across all modal bundles. While this circle has appeared repeatedly in earlier derivations—for example in the construction of time ordering, in the emergence of three fermion families, and in the organization of global phases—its role has not previously been isolated and analyzed in its own right.

In this section we make explicit what has so far remained implicit: the central circle is not merely a convenient geometric ingredient, but the unique shared coherence channel of the theory. Because it is the only internal structure common to all sectors, any quantity that is universal, scalar, and resistant to local redefinition must ultimately be bookkept through this circle.

This observation will form the backbone of the remainder of the paper.

## Position of the Central Circle in the Modal Geometry

The starting point of MTT is a ten–dimensional product geometry of the form
``` math
M_{10} = Y^4 \times B_1 \times B_2 \times B_3 ,
```
where $`Y^4`$ is the emergent spacetime manifold and the $`B_i`$ are internal modal bundles associated with distinct sectors of the effective theory. Crucially, these bundles are not independent. They are organized so that each contains a common factor, the central circle $`S^1_{\mathrm{cen}}`$,
``` math
B_1 = S^1_{\mathrm{cen}}, \qquad
B_2 = S^1_{\mathrm{cen}} \times F_2, \qquad
B_3 = S^1_{\mathrm{cen}} \times F_3 ,
```
with $`F_2`$ and $`F_3`$ denoting additional internal structures specific to the weak and strong sectors respectively.

This reuse is rigid. No other internal component is shared across all bundles, and no alternative decomposition preserves the commuting Laplacian structure required for a bounded joint harmonic projector. As a result, the coherent projector
``` math
\Pi_{\mathrm{coh}} = \Pi_{B_1}\,\Pi_{B_2}\,\Pi_{B_3}
```
always includes the same harmonic condition along $`S^1_{\mathrm{cen}}`$.

From the perspective of admissibility, this has an immediate consequence: any coherent configuration, regardless of sector, must be compatible with the same circle constraint.

## Why a Circle, and Why Only One

The appearance of a circle rather than another compact space is not arbitrary. Among compact one–dimensional manifolds, the circle is unique in simultaneously supporting:

- nontrivial holonomy,

- conserved phase modulo $`2\pi`$,

- winding number,

- and a rigid, discrete harmonic spectrum.

An interval would admit drift rather than global phase; higher–dimensional compact spaces would introduce additional internal degrees of freedom that could carry direction–dependent or sector–dependent loads. Multiple independent circles would fragment universality, producing several inequivalent scalar bookkeeping channels.

By contrast, a single shared circle provides exactly one universal scalar resource. Anything that must be:

- invariant under internal gauge transformations,

- shared by all sectors,

- and resistant to local redefinition,

is forced to couple to this structure.

This fact will underlie the identification of the circle with inertia and gravity in later sections.

## The Circle as a Coherence Bookkeeping Channel

In MTT, physical description exists only where projection to the coherent sector is stable. That stability is controlled by spectral gaps and boundedness of the coherent projector. Because the central circle enters every factor of $`\Pi_{\mathrm{coh}}`$, any loss of control along this direction affects the entire effective description.

It is therefore natural to interpret the circle not as a carrier of dynamics, but as a carrier of *bookkeeping constraints*. The circle does not mediate interactions; instead, it records and enforces global compatibility conditions on coherent configurations.

This viewpoint immediately explains several otherwise puzzling features:

- quantities associated with the circle are universal and scalar,

- they cannot be screened or locally eliminated,

- and failures of coherence along this channel lead to irreversible loss of description.

In subsequent sections we will show that inertia, gravitational coupling, and time ordering are precisely of this type.

## From Shared Structure to Physical Shadows

The key thesis of this paper can now be stated in a precise but nontechnical form:

> The central circle $`S^1_{\mathrm{cen}}`$ is the unique shared internal structure of Modal Triplet Theory. Its spectral rigidity and universal reuse force it to act as a global coherence bookkeeping channel. Distinct physical concepts—inertia, gravity, mass scales, time ordering, and family multiplicity—arise as different projections of this same constraint into the four–dimensional effective description.

The remainder of the paper develops this thesis systematically. We begin with inertia, which provides the simplest and most transparent entry point, before turning to mass generation, gravity, forces, and time.

# Inertia as Shared Coherence Cost

## The Traditional View of Inertia

In classical mechanics, inertia is introduced axiomatically. A body resists acceleration in proportion to a parameter called its mass, leading to Newton’s second law $`\mathbf{F} = m \mathbf{a}`$. In this formulation inertia is a primitive property, neither derived nor explained.

In relativistic physics the concept is refined but not fundamentally altered. A massive particle follows timelike worldlines and resists deviation from geodesic motion, while massless particles do not admit a rest frame. In quantum field theory inertia is identified with the rest mass parameter appearing in dispersion relations, yet the origin of that parameter remains external to the formalism.

Several persistent questions arise from this traditional picture:

- Why is inertia universal and scalar?

- Why is inertial mass equal to gravitational mass?

- Why does inertia resist acceleration but not uniform motion?

- Why do massless particles have no inertia but still gravitate?

In standard formulations these questions are answered partially or by appeal to experiment. In Modal Triplet Theory they receive a unified structural explanation.

## Inertia in Modal Triplet Theory: Conceptual Picture

In MTT, inertia is not a force and not a local field. It is a bookkeeping quantity associated with the shared coherence constraint encoded by the central circle $`S^1_{\mathrm{cen}}`$.

A coherent localized excitation—what is ordinarily called a “particle”— is defined as a stable fixed point of the projected modal dynamics. As long as this excitation moves along a geodesic of the emergent spacetime, its coherence structure remains aligned with neighboring regions. No additional bookkeeping is required.

Acceleration changes this situation. Bending a worldline relative to its neighbors forces the coherent projector to re–solve compatibility conditions slice by slice. Because the central circle is shared across all sectors, this re–solving incurs a universal cost.

> Inertia is the minimal coherence cost required to maintain an admissible projection when the history of a localized coherent structure is bent in spacetime.

This immediately explains several basic properties:

- inertia is scalar, because the circle is one–dimensional and shared,

- inertia is universal, because all sectors reuse the same circle,

- inertia vanishes for null trajectories, which do not admit rethreading of coherence along proper time.

Uniform motion does not require any reconfiguration of coherence, and therefore produces no inertial resistance. Only acceleration—deviation from geodesic coherence alignment—does.

## From Coherence Cost to Inertial Mass

The quantity ordinarily called “mass” arises in MTT as the lowest nonzero spectral cost associated with deforming a coherent configuration along the shared circle direction. It is not an independently adjustable parameter, but a property of the admissible coherent mode itself.

Schematically, if $`\Pi_{\mathrm{coh}}`$ denotes the joint harmonic projector and $`\lambda_\ast`$ the smallest spectral gap controlling deformations that involve the shared circle sector, then the inertial mass $`m`$ of a coherent excitation is fixed by that gap:
``` math
m \;\sim\; \lambda_\ast \, ,
```
up to representation–dependent overlap factors discussed later.

Because this gap is associated with the same circle in all bundles, the resulting mass parameter is independent of internal gauge charges. This universality is not imposed; it is forced by the geometry of the coherent sector.

## Worldline Stationarity and the Emergence of $`F=ma`$

The effective four–dimensional dynamics of a localized coherent excitation are obtained by taking the worldline limit of the projected stress–energy balance laws. In this limit the motion of the excitation extremizes an effective coherent action of the form
``` math
S_{\mathrm{wl}} = - m \int ds \;+\; S_{\mathrm{int}},
```
where $`ds`$ is the spacetime line element and $`S_{\mathrm{int}}`$ encodes interactions with gauge fields and external forces.

Stationarity of this action under variations of the worldline yields the geodesic equation in the absence of forces, and the familiar force law when interactions are present. In the nonrelativistic limit this reduces to
``` math
\mathbf{F} = m \mathbf{a}.
```

From the MTT perspective this equation does not introduce a new principle. It is simply the condition that the total coherence bookkeeping cost be stationary under small variations of the projected history.

A detailed derivation of this result from the projected conservation laws is given in Appendix A.

## Inertial and Gravitational Mass

Because inertia measures the cost of rethreading shared coherence, and gravity measures the redistribution of shared coherence capacity across space, the two quantities are necessarily identical.

No separate equivalence principle is required. The equality of inertial and gravitational mass follows from the fact that both are projections of the same central circle constraint into different aspects of the effective description.

This identity will be made explicit in the discussion of gravity in the next section.

## Summary

Inertia in Modal Triplet Theory is neither a primitive force nor a mysterious parameter. It is a structural consequence of maintaining admissible coherence in the presence of acceleration. The central circle provides the unique shared channel through which this cost is counted, explaining the universality, scalar nature, and rigidity of inertial mass.

With inertia understood in this way, we now turn to gravity, which represents the spatial redistribution of the same coherence bookkeeping across the emergent spacetime.

# Mass, the Higgs Vacuum Expectation Value, and the Central Circle

## The Traditional Picture: Mass from Symmetry Breaking

In the Standard Model, particle masses arise through electroweak symmetry breaking. A scalar Higgs field acquires a vacuum expectation value $`v`$, and fermions and gauge bosons obtain masses through Yukawa and gauge couplings:
``` math
m_f = \frac{v}{\sqrt{2}} |y_f|, \qquad
m_W = \frac{1}{2} g v, \qquad
m_Z = \frac{1}{2}\sqrt{g^2 + g'^2}\, v.
```

In this formulation, the Higgs vacuum expectation value sets a universal mass scale, while the Yukawa couplings encode particle–specific information. Although phenomenologically successful, this picture leaves several questions open:

- Why does the Higgs vev generate inertia rather than merely a rest–energy label?

- Why do Yukawa couplings exhibit strong hierarchies?

- Why does the Higgs mechanism fail to explain the equality of inertial and gravitational mass?

- Why do massless particles still participate in gravity?

Within Modal Triplet Theory these questions are resolved by separating the roles of the Higgs field and the central circle.

## Higgs vev as an Encoding Parameter

In MTT, the Higgs sector belongs to the four–dimensional effective encoding, not to the fundamental coherence bookkeeping. Electroweak symmetry breaking determines how internal coherent profiles are represented as massive fields in the 4D description, but it does not define inertia itself.

The Higgs vacuum expectation value therefore plays the role of a *conversion parameter*: it translates internal overlap data into four–dimensional mass parameters. The Higgs field does not create inertia; it assigns a mass scale to coherent modes that already exist.

This distinction is essential. The Higgs mechanism operates only within a particular admissible encoding of the coherent sector. In regimes where that encoding ceases to be valid—such as near selection fronts or in the early universe—inertia and gravitational coupling remain well defined even when the Higgs description does not.

## The Central Circle and the Origin of Yukawa Structure

While the Higgs vev sets the overall mass scale, the pattern of Yukawa couplings is determined by the internal geometry. In Modal Triplet Theory, fermion families arise from a $`\mathbb{Z}_3`$ holonomy of a flavor line bundle over the central circle $`S^1_{\mathrm{cen}}`$. This construction produces exactly three inequivalent coherent sectors, corresponding to the observed three families.

The same circle holonomy controls the allowed coherent profiles of left– and right–handed fermions, as well as their relative phases. Yukawa couplings arise as overlap integrals of these profiles with the Higgs mode:
``` math
y_f \sim \int_{X_6} \psi_{L,f}^\dagger\, \Phi_H \, \psi_{R,f},
```
where the admissible shapes and phases of the wavefunctions are restricted by the central circle sector.

Thus:

- the Higgs vev fixes the overall mass scale,

- the central circle fixes which Yukawas exist and how large they are,

- family hierarchies reflect geometric coherence constraints rather than arbitrary parameters.

## Why Higgs Mass and Inertia Coincide Numerically

For ordinary matter in the low–energy Standard Model regime, the dominant contribution to rest mass is the Higgs–generated term. As a result, the Higgs mass and inertial mass coincide numerically. However, in Modal Triplet Theory this coincidence is contingent, not fundamental.

Inertia is determined by the coherence cost associated with bending a worldline through the shared circle sector. The Higgs vev merely provides the dominant contribution to that cost within the electroweak encoding. Nothing in the structure of MTT requires this to remain true in all regimes.

This separation explains why:

- inertial mass remains meaningful even when the Higgs description fails,

- different encodings of the coherent sector may redistribute mass without changing inertia,

- mass renormalization is constrained by coherence rather than free counterterms.

## Photons, Zero Rest Mass, and Gravitational Coupling

The distinction between Higgs mass and inertia clarifies the status of massless particles. Photons do not acquire mass from the Higgs field and therefore possess no rest–mass inertia: they admit no proper–time parameterization and no $`m\int ds`$ term in a worldline action.

Nevertheless, photons gravitate. Gravity in MTT couples not to inertia alone, but to the total projected stress–energy content of coherent excitations. Massless radiation carries energy–momentum and therefore contributes to the bookkeeping of coherence capacity across spacetime.

This explains why photons bend spacetime and experience gravitational redshift despite having zero rest mass.

## Summary

The Higgs vacuum expectation value and inertial mass play distinct roles in Modal Triplet Theory. The Higgs vev determines how internal coherent modes are encoded as massive four–dimensional fields, while inertia reflects the universal coherence cost associated with the shared central circle.

Their numerical equality in the Standard Model is a feature of the low–energy electroweak encoding, not a fundamental identity. Recognizing this distinction is essential for understanding mass hierarchies, renormalization constraints, and the universality of gravity.

In the next section we show how the same central circle underlies gravity itself, which appears as the spatial redistribution of shared coherence capacity in the emergent spacetime geometry.

# Gravity as Coherence Bookkeeping

## The Traditional View of Gravity

In general relativity, gravity is described as the curvature of spacetime sourced by the stress–energy tensor. The Einstein field equations,
``` math
G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu},
```
relate local geometry to local matter content. This description is remarkably successful, yet conceptually unusual: gravity is not mediated by a force field in spacetime, has no local gauge–invariant energy density, and couples universally to all forms of energy.

Several longstanding questions arise naturally:

- Why is gravity universal and unscreenable?

- Why is inertial mass equal to gravitational mass?

- Why does gravity lack a local energy density?

- Why does gravity appear to encode memory and irreversibility?

Modal Triplet Theory resolves these questions by identifying gravity not as a force, but as a bookkeeping structure associated with the shared coherence constraint encoded by the central circle.

## Gravity in Modal Triplet Theory: Conceptual Picture

In MTT, physical description exists only within admissible coherent sectors. Admissibility is controlled by spectral gaps and boundedness of the coherent projector. Because the central circle $`S^1_{\mathrm{cen}}`$ is reused across all modal bundles, any strain on coherence along this direction affects every sector simultaneously.

Gravity arises when the coherence cost associated with localized excitations cannot be accommodated uniformly across spacetime. In such situations, the effective description must redistribute coherence capacity spatially in order to remain admissible.

> Gravity is the spatial redistribution of shared coherence capacity required to maintain admissible projection.

This interpretation immediately explains several distinctive features of gravity:

- gravity is universal because the circle is shared by all sectors,

- gravity cannot be screened because coherence capacity is global,

- gravity carries memory because projection is noninvertible at admissibility boundaries.

## Why Gravity Is Not a Force

Forces in MTT arise from bundle–specific connections and track internal compatibility rules. They govern how coherent excitations may be reconfigured within a fixed admissible basin. Gravity, by contrast, governs whether a given configuration remains admissible at all.

This difference is reflected mathematically. Gauge fields are described by connections on internal bundles and admit local gauge–invariant energy densities. Gravity is described by the spacetime metric itself, which defines the effective encoding rather than living on top of it.

As a result, gravity cannot be assigned a local energy density without breaking diffeomorphism invariance. This is not a deficiency of general relativity, but a direct consequence of gravity’s role as bookkeeping for the encoding itself.

## Gravity and the Central Circle

The central circle is the only internal structure common to all coherent modes. Any deformation that affects this circle therefore alters the admissibility of the entire configuration. Such deformations cannot be localized to a single sector or screened by internal rearrangements.

From this perspective, gravity measures how much the shared circle coherence is strained by the presence and motion of matter. Inertial mass quantifies the cost of bending a coherent history through the circle, while gravity quantifies how that cost must be distributed across space to maintain global compatibility.

This identity explains the equality of inertial and gravitational mass without invoking an independent equivalence principle.

## The Einstein Equations as Bookkeeping Closure

The effective four–dimensional gravitational dynamics arise from coherent projection and internal integration of the ten–dimensional MTT action. To leading order in admissibility–preserving approximations, the resulting action is of Einstein–Hilbert form:
``` math
S_{\mathrm{eff}} = \frac{1}{16\pi G_{\mathrm{eff}}}
\int (R - 2\Lambda_{\mathrm{eff}})\sqrt{-g}\,d^4x
+ S_{\mathrm{matter}}.
```

Variation with respect to the metric yields the Einstein field equations. In the MTT interpretation, these equations do not describe the dynamics of a force field. They represent the unique local, diffeomorphism–invariant, two–derivative closure of the coherence bookkeeping problem.

The contracted Bianchi identity,
``` math
\nabla_\mu G^{\mu\nu} \equiv 0,
```
ensures that if the matter sector obeys its own conservation laws, the gravitational bookkeeping remains consistent under evolution. In the language of the $`3+1`$ decomposition, this identity guarantees that the Hamiltonian and momentum constraints are preserved from slice to slice.

A detailed discussion of constraint preservation and its relation to admissibility is given in Appendix C.

## Memory, Irreversibility, and Horizons

Because coherent projection is noninvertible, the redistribution of coherence capacity encoded by gravity is inherently one–way. Once incompatible configurations are projected out, the bookkeeping cannot be reversed.

This irreversibility is normally invisible in weak–field regimes, where coherence capacity is large and redistribution is smooth. Near admissibility boundaries—such as black hole horizons or selection fronts associated with measurement—the loss of invertibility becomes manifest.

In these regimes gravity exhibits memory effects and entropy bounds, reflecting the exhaustion of coherence capacity along the central circle.

## Summary

In Modal Triplet Theory, gravity is not an interaction added to otherwise independent degrees of freedom. It is the bookkeeping structure that enforces global coherence compatibility through the shared central circle. The Einstein field equations arise as the minimal consistency conditions for this bookkeeping in the four–dimensional encoding.

With gravity understood in this way, we are now prepared to contrast it explicitly with the bookkeeping of forces, which operate within admissible basins rather than at their boundaries.

# Forces as Bundle–Specific Bookkeeping

## The Traditional View of Forces

In conventional physics, forces are described as interactions mediated by fields. Electromagnetism and the nonabelian gauge forces are formulated as local gauge theories, with dynamical gauge fields propagating on spacetime and coupling to conserved currents. These theories admit local stress–energy tensors and support familiar notions such as field energy density, radiation, and screening.

Despite their differences from gravity, gauge theories share several structural features with general relativity: they possess constraints, gauge redundancies, and consistency conditions that must be preserved under time evolution. However, unlike gravity, gauge forces do not exhibit universal coupling, irreversibility, or global capacity limits.

Modal Triplet Theory explains this contrast by showing that forces and gravity perform fundamentally different kinds of bookkeeping.

## Gauge Forces in Modal Triplet Theory

In MTT, gauge forces arise from internal bundle connections rather than from spacetime geometry. Each force corresponds to a specific modal bundle with its own internal structure, holonomy, and harmonic modes. After coherent projection, these internal connections appear as gauge fields in the four–dimensional effective description.

The key point is that gauge forces operate *within* an admissible coherent basin. They govern how coherent excitations may be reconfigured, transported, or exchanged without threatening the existence of the effective description itself.

> Forces are bookkeeping rules for internal compatibility within a fixed admissible coherent sector.

This sharply distinguishes them from gravity, which governs whether a configuration remains admissible at all.

## Constraint Structure of Maxwell and Yang–Mills Theories

Gauge theories are constrained systems. In the $`3+1`$ decomposition of electromagnetism, Maxwell’s equations split into:

- an instantaneous constraint (Gauss’s law),
  ``` math
  \nabla\cdot\mathbf{E} = \rho,
  ```

- and hyperbolic evolution equations for $`\mathbf{E}`$ and $`\mathbf{B}`$.

The constraint is preserved under time evolution provided the electric current satisfies the continuity equation,
``` math
\partial_\mu J^\mu = 0.
```
If Gauss’s law holds on one time slice and charge is conserved, it holds on all subsequent slices.

Yang–Mills theories exhibit the same structure, with Gauss’s law generalized to a covariant constraint involving the gauge–covariant divergence of the nonabelian electric field. Constraint preservation follows from covariant current conservation and the Yang–Mills Bianchi identity.

This is exactly the same logical structure that appears in general relativity: constraints are imposed on each spatial slice, and identities ensure their preservation under evolution.

## Why Gauge Constraints Do Not Lead to Capacity Collapse

Despite this formal similarity, gauge forces do not encounter the same breakdowns as gravity. The reason is structural.

Gauge constraints enforce compatibility *within* a bundle. Violations typically indicate missing charged degrees of freedom, an inconsistent gauge choice, or an incomplete effective description. Once the missing elements are restored, the theory regains consistency.

In Modal Triplet Theory, this reflects the fact that gauge forces do not act on the shared coherence channel. They rearrange internal degrees of freedom without straining the central circle. As long as the shared coherence constraint remains intact, gauge bookkeeping can always be repaired locally.

Gravity, by contrast, operates on the shared circle itself. When coherence capacity is exhausted along this channel, no local repair is possible, and the encoding must change irreversibly.

## Local Energy Density of Forces

Gauge forces admit local, gauge–invariant energy densities constructed from internal curvature invariants, such as $`F_{\mu\nu}F^{\mu\nu}`$. This is possible because gauge symmetry acts in internal fiber directions, leaving the spacetime point itself invariant.

From the MTT perspective this is natural: gauge fields live *on top of* the spacetime encoding. Their energy is a property of configurations within a fixed admissible geometry and can therefore be localized.

## Why Gravity Has No Local Energy Density

Gravity does not admit an analogous local energy density. Any attempt to define one can be eliminated locally by a diffeomorphism, reflecting the equivalence principle.

In MTT this is not an accident. Gravity is the bookkeeping layer of the encoding itself. Its “gauge symmetry” is spacetime diffeomorphism invariance, which moves points rather than rotating internal fibers. A local gravitational energy density would therefore be a gauge artifact rather than an observable quantity.

Only global or quasilocal measures of gravitational energy—such as ADM or Bondi charges—are meaningful, because they compare different asymptotic or boundary encodings.

## Forces and Gravity in a Unified Bookkeeping Picture

The contrast between forces and gravity can now be stated succinctly:

- Forces bookkeep allowed reconfigurations within an admissible coherent sector.

- Gravity bookkeeps whether those configurations remain admissible at all.

Both are constraint–preserving PDE systems, but they operate on different layers of the coherent structure. Forces act on bundle–specific degrees of freedom and remain reversible. Gravity acts on the shared coherence channel and becomes irreversible at admissibility boundaries.

## Summary

Maxwell and Yang–Mills theories exhibit the same formal constraint–preservation logic as general relativity, but they do not encounter coherence capacity collapse. This difference is not dynamical but structural. Gauge forces rearrange internal compatibility, while gravity governs global coherence viability.

With this distinction in place, we are prepared to address time and irreversibility, which arise when the shared coherence bookkeeping becomes noninvertible under projection.

# Time and the Arrow as Projection Ordering

## The Traditional Status of Time

In most physical theories, time is introduced as an external parameter. In classical mechanics it labels trajectories; in quantum mechanics it governs unitary evolution; in quantum field theory it indexes operator ordering. The arrow of time is then explained separately, typically through thermodynamics, statistical mechanics, or cosmological initial conditions.

This division leaves a conceptual gap. While microscopic laws are largely time–reversal invariant, macroscopic phenomena exhibit irreversibility, and measurement outcomes are recorded irreversibly. The status of time itself—as a background parameter or an emergent ordering—remains unclear.

Modal Triplet Theory resolves this gap by identifying time not as a fundamental coordinate, but as an ordering induced by projection.

## Time in Modal Triplet Theory

In MTT the fundamental evolution is the modal flow $`\Phi_\tau`$, defined on the full configuration space. This evolution is invertible and does not itself single out a preferred temporal direction. Physical time emerges only after projection onto the coherent sector, where admissibility and stability restrict which configurations can be represented consistently.

The effective evolution is therefore not $`\Phi_\tau`$ itself, but
``` math
T_\tau = \Pi_{\mathrm{coh}} \circ \Phi_\tau ,
```
where $`\Pi_{\mathrm{coh}}`$ is the joint coherent projector. Unlike the underlying modal flow, this projected evolution is generally noninvertible.

> Time in MTT is the ordering of successive admissible projections.

The arrow of time arises because projection discards incompatible configurations. Once discarded, they cannot be recovered by any operation in the effective description.

## The Role of the Central Circle

The emergence of time ordering is intimately tied to the central circle $`S^1_{\mathrm{cen}}`$. This circle is the only internal structure shared across all coherent sectors, and therefore the only place where a global ordering constraint can be enforced consistently.

Coherent configurations must align their internal phase along the central circle in order to remain admissible. When the system evolves under $`\Phi_\tau`$, successive projections enforce a monotonic ordering of this alignment. This produces a preferred direction in the effective description, even though the underlying modal dynamics remain reversible.

Because the central circle is reused everywhere, this ordering is universal: all sectors share the same arrow of time.

## Irreversibility from Noninvertible Projection

The irreversibility of time in MTT does not arise from dissipation or coarse–graining alone. It arises structurally from the fact that $`\Pi_{\mathrm{coh}}`$ does not admit a global right inverse.

When a configuration approaches an admissibility boundary, multiple distinct modal states may project to the same coherent state. The effective description loses the information required to distinguish their pasts. No further evolution within the effective theory can reconstruct what was lost.

This mechanism applies uniformly:

- in measurement, where incompatible outcomes are pruned,

- in thermodynamic processes, where microstate distinctions are irretrievably lost,

- near horizons, where reconstruction fails across an admissibility barrier.

In all cases, irreversibility reflects the same projection–induced noninvertibility.

## Time, Constraints, and Consistency

In the four–dimensional encoding, the ordering induced by projection appears as the familiar temporal structure of relativistic field theory. The Einstein equations, Maxwell equations, and Yang–Mills equations are all constraint–preserving systems: they ensure that admissibility conditions imposed on one spatial slice remain valid on subsequent slices.

The preservation of constraints under evolution guarantees that the effective ordering remains consistent. When this preservation fails, the encoding ceases to be valid, signaling the approach to a selection front or horizon.

From the MTT perspective, time evolution is therefore not a fundamental flow, but a bookkeeping procedure that sequences admissible states.

## Why the Arrow Is Universal

Because the central circle is shared across all modal bundles, any loss of admissibility along this channel affects every sector simultaneously. There is no separate clock for different forces or particle types. The arrow of time is therefore universal and cannot be reversed locally.

This universality explains why:

- all physical processes share the same temporal ordering,

- local manipulations cannot reverse macroscopic irreversibility,

- time reversal symmetry is at best approximate in effective descriptions.

## Summary

Time in Modal Triplet Theory is not a background parameter, but the ordering induced by successive coherent projections. The arrow of time reflects the noninvertibility of this projection, which is enforced through the shared central circle. Irreversibility, measurement, and horizon behavior are all manifestations of the same structural mechanism.

With time understood in this way, we are prepared to discuss the most extreme manifestations of coherence bookkeeping: admissibility boundaries, horizons, and selection fronts.

# Admissibility Boundaries, Horizons, and Selection Fronts

## The Limits of Admissible Description

Throughout the preceding sections we have emphasized that physical description in Modal Triplet Theory exists only within admissible coherent sectors. Admissibility is controlled by spectral gaps, boundedness of the coherent projector, and stability margins that ensure small perturbations do not destroy the effective encoding.

These conditions are not guaranteed globally. There exist regions of configuration space where admissibility degrades and eventually fails. The boundary between admissible and inadmissible regimes plays a central role in understanding irreversibility, entropy, and gravitational horizons.

> Admissibility boundaries mark the limits of coherent physical description.

## Coherence Capacity and Its Exhaustion

A convenient way to characterize admissibility is through the notion of *coherence capacity*. This is a scalar measure of how much coherent deformation a configuration can sustain before the projection ceases to be well controlled.

Because the central circle $`S^1_{\mathrm{cen}}`$ is the shared coherence channel, coherence capacity is fundamentally associated with this direction. Exhaustion of coherence capacity corresponds to the closing of spectral gaps or the loss of projector regularity along the circle sector.

When coherence capacity is large, the effective description is robust and reversible to excellent approximation. When it approaches zero, the effective description becomes ill–conditioned and noninvertible.

## Selection Fronts

When a trajectory in modal configuration space approaches an admissibility boundary, the coherent projector identifies multiple distinct modal configurations with a single effective state. At this point the effective evolution loses its right inverse.

This transition defines a *selection front*. Across a selection front, the system is forced into a new admissible basin, and alternative configurations are irreversibly pruned.

Selection fronts appear in several familiar contexts:

- quantum measurement, where incompatible outcomes are eliminated,

- decoherence and thermalization, where microstate distinctions are lost,

- strong gravitational regimes, where global reconstruction fails.

In all cases the mechanism is the same: exhaustion of coherence capacity along the central circle.

## Horizons as Admissibility Barriers

Gravitational horizons provide a particularly clear example of an admissibility boundary. In the presence of a horizon, the effective description available to an observer restricted to one side of the horizon cannot be globally extended.

From the MTT perspective, a horizon is not a physical membrane or a repository of information. It is a *coherence bottleneck*: a surface across which the shared circle coherence cannot be aligned while preserving bounded projection.

As a result:

- reconstruction across the horizon fails,

- effective evolution becomes noninvertible,

- entropy bounds emerge naturally as limits on coherence capacity.

The area scaling of black hole entropy reflects the fact that coherence capacity is redistributed across a codimension–one surface in spacetime.

## Entropy and Irreversibility

Entropy in Modal Triplet Theory measures the volume of configuration space that has been irreversibly projected out. It is not a measure of disorder, but of lost distinguishability under admissible projection.

Because selection fronts and horizons correspond to irreversible pruning of coherent alternatives, entropy increase is a direct consequence of coherence capacity exhaustion. No additional statistical assumptions are required.

This perspective unifies:

- thermodynamic entropy increase,

- black hole entropy,

- and the entropy associated with measurement outcomes.

All arise from the same projection–induced loss of invertibility along the central circle.

## Why Admissibility Failure Is One–Way

Once coherence capacity is exhausted and a selection front is crossed, there exists no operation within the effective description that can reconstruct the discarded alternatives. This irreversibility is structural rather than dynamical.

The underlying modal evolution remains invertible. What is lost is the ability of the effective encoding to track that evolution uniquely.

Because the central circle is shared across all sectors, loss of coherence along this channel cannot be repaired locally or by internal rearrangement. The effective arrow of time is therefore enforced globally.

## Summary

Admissibility boundaries represent the ultimate limits of coherent physical description. Horizons, measurement collapse, and entropy production are not independent phenomena, but different manifestations of the same structural mechanism: exhaustion of coherence capacity along the shared central circle.

With the role of admissibility boundaries made explicit, the unifying picture of the central circle is now complete. In the final section we summarize the implications of this perspective and outline directions for further development.

# Synthesis and Outlook: One Circle, Many Shadows

## Summary of the Central Result

In this paper we have isolated and analyzed the role of the central circle $`S^1_{\mathrm{cen}}`$ in Modal Triplet Theory. Although this structure has appeared repeatedly in earlier derivations, its unifying significance has not previously been made explicit.

We have shown that the central circle is the unique shared internal structure across all modal bundles, and therefore the only viable carrier of universal coherence bookkeeping. As a consequence, a wide range of physical concepts that are traditionally treated as independent emerge as different projections of the same underlying constraint.

Specifically:

- inertia arises as the coherence cost of bending a localized history,

- mass reflects the lowest spectral cost associated with shared coherence,

- gravity encodes the spatial redistribution of coherence capacity,

- time ordering emerges from noninvertible projection along the circle,

- fermion families arise as holonomy sectors of the same structure,

- irreversibility and entropy reflect exhaustion of coherence capacity.

No new dynamical principles are required to obtain these results. They follow from the existence of a shared coherence channel and the requirement that physical description remain admissible.

## Resolution of Conceptual Tensions

The central circle perspective resolves several longstanding conceptual tensions in physics:

- The equality of inertial and gravitational mass is explained without invoking an independent equivalence principle.

- The absence of a local gravitational energy density follows from the fact that gravity is the bookkeeping layer of the encoding itself.

- The gravitational coupling of massless radiation is natural, since gravity responds to coherence load rather than rest mass alone.

- The arrow of time and entropy increase arise structurally from projection, not from special initial conditions or coarse–graining assumptions.

These features are often treated as separate puzzles. In Modal Triplet Theory they are unified by a single geometric fact.

## Relation to Established Results

All results presented here are compatible with, and in many cases directly recover, standard formulations:

- Newton’s second law emerges as the stationarity condition of the coherent worldline action.

- The Einstein field equations arise as the unique local, diffeomorphism– invariant, two–derivative closure of the coherence bookkeeping problem.

- Maxwell and Yang–Mills theories appear as constraint–preserving bookkeeping systems within admissible coherent basins.

The technical content of these recoveries has been established elsewhere in the MTT corpus; the present work clarifies their common structural origin.

## Implications and Open Directions

Making the role of the central circle explicit suggests several directions for future investigation:

- quantitative constraints on mass renormalization from coherence capacity bounds,

- refined treatments of black hole entropy and information flow as coherence bottlenecks,

- early–universe regimes where the Higgs encoding is not valid but inertia and gravity persist,

- possible observational signatures of coherence capacity exhaustion in strong–gravity or high–energy settings.

More broadly, the analysis presented here illustrates how apparently disparate physical concepts can be unified by examining the structural requirements of admissible description rather than by introducing additional dynamics.

## Concluding Remarks

The central circle is not an auxiliary ingredient of Modal Triplet Theory. It is the structural backbone that makes a universal, local, and stable physical description possible.

By recognizing inertia, mass, gravity, time, and irreversibility as shadows of the same shared coherence constraint, we obtain a conceptually economical and technically consistent picture of fundamental physics. The simplicity of this unification suggests that the circle’s role is not an artifact of a particular construction, but a necessary feature of any theory in which physical description is both local and finite.

**Appendices** collect detailed derivations and technical results supporting the arguments in the main text.

# Derivation of $`\mathbf{F}=m\mathbf{a}`$ from Coherent Stress–Energy Balance

This appendix provides an explicit derivation of Newton’s second law $`\mathbf{F}=m\mathbf{a}`$ as the worldline limit of coherent stress–energy balance. No assumptions beyond those already used elsewhere in the Modal Triplet Theory corpus are introduced. In particular, we do not postulate inertia as a primitive quantity; instead it emerges as the coefficient multiplying worldline curvature in the effective coherent action.

## Projected Balance Law

In the coherent sector of Modal Triplet Theory, the effective four–dimensional description obeys a local balance law of the form
``` math
\begin{equation}
\nabla_\mu T^{\mu\nu} = f^\nu ,
\label{eq:balance}
\end{equation}
```
where $`T^{\mu\nu}`$ is the projected stress–energy tensor and $`f^\nu`$ denotes the force density arising from gauge or external interactions. In the absence of such interactions, $`f^\nu=0`$ and the motion reduces to geodesic flow.

Equation <a href="#eq:balance" data-reference-type="eqref" data-reference="eq:balance">[eq:balance]</a> is the pushforward of the underlying modal dynamics under coherent projection and is identical in form to the standard conservation law used in relativistic continuum mechanics.

## Localization and Worldtube Approximation

Consider a localized coherent excitation whose support is confined to a narrow worldtube around a timelike curve $`X^\mu(\tau)`$. In the worldline limit, the stress–energy tensor may be approximated distributionally as
``` math
\begin{equation}
T^{\mu\nu}(x) \simeq m\, u^\mu u^\nu \,\delta^{(3)}\!\bigl(x-X(\tau)\bigr),
\label{eq:stressworldline}
\end{equation}
```
where $`u^\mu = dX^\mu/d\tau`$ is the four–velocity and $`\tau`$ is proper time along the curve. The parameter $`m`$ is the invariant mass associated with the coherent excitation; its origin is discussed in Section 3 of the main text.

Similarly, if the excitation carries a conserved charge $`q`$, the associated current takes the form
``` math
\begin{equation}
J^\mu(x) \simeq q\,u^\mu\,\delta^{(3)}\!\bigl(x-X(\tau)\bigr).
\end{equation}
```

## Integrated Momentum Balance

Define the four–momentum of the excitation on a spacelike hypersurface $`\Sigma_\tau`$ intersecting the worldline at proper time $`\tau`$ by
``` math
\begin{equation}
p^\nu(\tau) = \int_{\Sigma_\tau} T^{\nu\mu} n_\mu \, d^3x ,
\end{equation}
```
where $`n_\mu`$ is the future–directed unit normal to $`\Sigma_\tau`$. Using <a href="#eq:stressworldline" data-reference-type="eqref" data-reference="eq:stressworldline">[eq:stressworldline]</a>, this reduces to
``` math
\begin{equation}
p^\nu(\tau) = m\,u^\nu(\tau).
\end{equation}
```

Integrating the balance law <a href="#eq:balance" data-reference-type="eqref" data-reference="eq:balance">[eq:balance]</a> over the worldtube and applying Gauss’ theorem yields
``` math
\begin{equation}
\frac{d p^\nu}{d\tau}
=
\int_{\Sigma_\tau} f^\nu \, d^3x .
\label{eq:dpdt}
\end{equation}
```

## Gauge Forces and Covariant Force Law

For interactions mediated by gauge fields, the force density takes the standard form
``` math
\begin{equation}
f^\nu = F^{\nu}{}_{\mu}\,J^\mu ,
\end{equation}
```
with $`F_{\mu\nu}`$ the field strength of the relevant gauge connection. Substituting the localized current and performing the spatial integral gives
``` math
\begin{equation}
\int_{\Sigma_\tau} f^\nu \, d^3x
=
q\,F^{\nu}{}_{\mu}(X(\tau))\,u^\mu(\tau).
\end{equation}
```

Equation <a href="#eq:dpdt" data-reference-type="eqref" data-reference="eq:dpdt">[eq:dpdt]</a> therefore becomes
``` math
\begin{equation}
\frac{d}{d\tau}\!\left(m\,u^\nu\right)
=
q\,F^{\nu}{}_{\mu}\,u^\mu .
\label{eq:covforce}
\end{equation}
```
This is the standard covariant force law combining inertial motion and gauge interactions.

## Nonrelativistic Limit

In a weak–field, low–velocity regime, the four–velocity reduces to $`u^\mu \simeq (1,\mathbf{v})`$ and proper time coincides with coordinate time, $`\tau\simeq t`$. The spatial components of <a href="#eq:covforce" data-reference-type="eqref" data-reference="eq:covforce">[eq:covforce]</a> then reduce to
``` math
\begin{equation}
m\,\frac{d\mathbf{v}}{dt} = \mathbf{F},
\end{equation}
```
where $`\mathbf{F}`$ is the usual three–force. This is Newton’s second law,
``` math
\begin{equation}
\mathbf{F}=m\mathbf{a}.
\end{equation}
```

## Interpretation in Modal Triplet Theory

Within Modal Triplet Theory, the derivation above has a clear structural interpretation. The balance law <a href="#eq:balance" data-reference-type="eqref" data-reference="eq:balance">[eq:balance]</a> expresses the fact that coherent projection preserves stress–energy bookkeeping up to controlled force terms. The parameter $`m`$ is not introduced by hand, but appears as the coefficient multiplying the proper–time line element in the effective worldline action
``` math
\begin{equation}
S_{\mathrm{wl}} = -m\int ds + S_{\mathrm{int}}.
\end{equation}
```

Stationarity of this action under variations of the worldline is equivalent to <a href="#eq:covforce" data-reference-type="eqref" data-reference="eq:covforce">[eq:covforce]</a>. From the perspective developed in the main text, the mass $`m`$ measures the minimal coherence cost associated with bending a localized coherent history through spacetime. Newton’s second law is therefore not an independent axiom, but the nonrelativistic limit of coherent stress–energy bookkeeping.

## Massless Limit

For null excitations such as photons, the proper time element vanishes ($`ds=0`$), and no term proportional to $`m\int ds`$ exists. Consequently there is no rest–mass inertia and no equation of the form $`\mathbf{F}=m\mathbf{a}`$. Nevertheless, massless excitations carry stress–energy and therefore enter the gravitational bookkeeping discussed in Section 5 of the main text.

This completes the derivation.

# Central Circle Holonomy, Fermion Families, and Yukawa Structure

This appendix makes explicit the role of the central circle $`S^1_{\mathrm{cen}}`$ in organizing fermion families and Yukawa couplings in Modal Triplet Theory. The results summarized here are implicit in earlier derivations of the Standard Model sector, but are presented in a unified form to support the interpretation developed in the main text.

## Flavor Bundles and Central Circle Holonomy

In the MTT construction of the Standard Model, fermions arise as coherent modes of internal bundles defined over the modal geometry
``` math
M_{10} = Y^4 \times B_1 \times B_2 \times B_3 .
```
Each internal bundle includes the central circle $`S^1_{\mathrm{cen}}`$, which is the only internal structure shared across all sectors.

Flavor degrees of freedom are encoded by a line bundle $`L_F \rightarrow S^1_{\mathrm{cen}}`$ with discrete holonomy. Consistency of the coherent projector and anomaly cancellation restrict the allowed holonomy group to a finite subgroup of $`U(1)`$. In the Standard Model construction this subgroup is $`\mathbb{Z}_3`$, yielding holonomy phases
``` math
\mathrm{Hol}(L_F) \;=\; \{1,\;\omega,\;\omega^2\}, \qquad
\omega = e^{2\pi i/3}.
```

Sections of $`L_F`$ therefore decompose into three inequivalent character sectors, corresponding to the three observed fermion families. No continuous family symmetry is introduced; the multiplicity arises entirely from global consistency of the circle bundle.

## Family Sectors as Coherent Modes

Let $`\psi_f`$ denote a fermionic coherent mode. Its dependence on the central circle coordinate $`\theta`$ takes the form
``` math
\psi_f(\theta) \;=\; e^{i q_f \theta}\,\tilde{\psi}_f,
```
where $`q_f \in \{0,1,2\} \bmod 3`$ labels the $`\mathbb{Z}_3`$ holonomy sector and $`\tilde{\psi}_f`$ is independent of $`\theta`$.

Because the coherent projector enforces compatibility across all bundles, modes belonging to different holonomy sectors cannot be continuously deformed into one another. They represent distinct admissible coherent configurations rather than components of a single multiplet.

This construction explains:

- why there are exactly three families,

- why family replication is universal across all fermions,

- why no additional family gauge bosons are required.

## Yukawa Couplings as Overlap Integrals

Yukawa couplings arise from overlap integrals of left–handed fermion, right–handed fermion, and Higgs coherent modes. Schematically,
``` math
\begin{equation}
y_{ij} \;\sim\;
\int_{X_6}
\psi_{L,i}^\dagger \, \Phi_H \, \psi_{R,j},
\label{eq:yukawa}
\end{equation}
```
where $`X_6`$ denotes the internal space.

The integrand includes factors of the form
``` math
e^{i(q_{L,i} - q_{R,j} + q_H)\theta},
```
where $`q_{L,i}`$, $`q_{R,j}`$, and $`q_H`$ are the central–circle charges of the corresponding modes. The integral over $`S^1_{\mathrm{cen}}`$ therefore enforces a selection rule:
``` math
\begin{equation}
q_{L,i} - q_{R,j} + q_H \;\equiv\; 0 \pmod{3}.
\label{eq:selection}
\end{equation}
```

Only Yukawa couplings satisfying this condition are nonvanishing. All others are forbidden by global coherence.

Thus the central circle holonomy simultaneously determines:

- which Yukawa couplings are allowed,

- which are suppressed or absent,

- and how family mixing can occur.

## Hierarchy and Phase Structure

Beyond selection rules, the magnitude and phase of Yukawa couplings are controlled by detailed overlap geometry. Relative phases acquired along the central circle contribute directly to CP–violating phases in the effective theory.

Because the central circle is shared across all bundles, these phases are globally correlated rather than arbitrary. This explains why CP violation appears coherently across different sectors and why its structure is tightly constrained.

Hierarchies among Yukawa couplings arise from:

- differing localization of coherent modes in the remaining internal directions,

- relative phase alignment along $`S^1_{\mathrm{cen}}`$,

- and admissibility constraints imposed by the coherent projector.

Importantly, these hierarchies do not require fine tuning of parameters. They are geometric consequences of coherence compatibility.

## Relation to Mass and Inertia

The Higgs vacuum expectation value converts Yukawa couplings into rest masses in the four–dimensional effective theory,
``` math
m_f = \frac{v}{\sqrt{2}}\,|y_f|.
```
However, as emphasized in the main text, this conversion does not define inertia itself.

The role of the central circle is twofold:

- it determines which fermionic coherent modes exist and how they couple,

- it provides the shared coherence channel whose deformation cost appears as inertia.

Thus family structure, Yukawa hierarchies, and inertial mass are not independent phenomena. They are different projections of the same underlying circle constraint.

## Summary

A discrete $`\mathbb{Z}_3`$ holonomy of the central circle explains the existence of three fermion families without introducing additional symmetries. The same holonomy governs Yukawa selection rules, phases, and mixing patterns through overlap integrals.

While the Higgs vacuum expectation value sets the overall mass scale in the four–dimensional encoding, the structure of masses and families is fixed by coherence constraints associated with the shared central circle. This provides a unified geometric origin for flavor and mass hierarchy in Modal Triplet Theory.

# Constraint Preservation, the Bianchi Identity, and Admissibility

This appendix makes precise the relationship between the Bianchi identity in general relativity, the preservation of Hamiltonian and momentum constraints in the $`3+1`$ formulation, and the notion of admissibility in Modal Triplet Theory. The goal is to show that “constraint preservation” is not an additional dynamical assumption, but the mathematical expression of consistent coherence bookkeeping.

## Einstein Equations and the Contracted Bianchi Identity

The Einstein field equations are
``` math
\begin{equation}
G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu},
\label{eq:einstein}
\end{equation}
```
where $`G_{\mu\nu}`$ is the Einstein tensor and $`T_{\mu\nu}`$ is the stress–energy tensor of matter.

A purely geometric identity holds for any Lorentzian metric:
``` math
\begin{equation}
\nabla_\mu G^{\mu\nu} \equiv 0.
\label{eq:bianchi}
\end{equation}
```
This is the contracted Bianchi identity and does not depend on the dynamical content of the theory.

Applying the covariant divergence to both sides of <a href="#eq:einstein" data-reference-type="eqref" data-reference="eq:einstein">[eq:einstein]</a> and using <a href="#eq:bianchi" data-reference-type="eqref" data-reference="eq:bianchi">[eq:bianchi]</a> yields
``` math
\begin{equation}
\nabla_\mu T^{\mu\nu} = 0.
\label{eq:covcons}
\end{equation}
```
Thus, consistency of the Einstein equations requires covariant conservation of stress–energy.

In Modal Triplet Theory this conservation law arises as the pushforward of diffeomorphism invariance of the projected effective action, rather than as an independent postulate.

## The $`3+1`$ Decomposition and Gravitational Constraints

To make the role of <a href="#eq:bianchi" data-reference-type="eqref" data-reference="eq:bianchi">[eq:bianchi]</a> explicit, it is convenient to perform a $`3+1`$ decomposition of spacetime. Let $`\Sigma_t`$ denote a foliation of spacetime by spacelike hypersurfaces with induced metric $`h_{ij}`$ and extrinsic curvature $`K_{ij}`$.

In this formulation, the Einstein equations split into:

- evolution equations for $`(h_{ij}, K_{ij})`$,

- constraint equations that must hold on each hypersurface.

The constraint equations are:
``` math
\begin{align}
\mathcal{H} &:= {}^{(3)}R + K^2 - K_{ij}K^{ij} - 16\pi G\,\rho = 0,
\label{eq:hamiltonian}\\
\mathcal{M}_i &:= D_j\!\left(K^{j}{}_i - \delta^{j}{}_i K\right)
- 8\pi G\,j_i = 0,
\label{eq:momentum}
\end{align}
```
where $`{}^{(3)}R`$ is the scalar curvature of $`\Sigma_t`$, $`\rho = T_{\mu\nu}n^\mu n^\nu`$ is the energy density, and $`j_i = -T_{\mu\nu}n^\mu h^\nu{}_i`$ is the momentum density.

These constraints do not generate time evolution. They restrict which initial data are admissible.

## Propagation of the Constraints

A central theorem of the $`3+1`$ formulation is that the constraints <a href="#eq:hamiltonian" data-reference-type="eqref" data-reference="eq:hamiltonian">[eq:hamiltonian]</a>–<a href="#eq:momentum" data-reference-type="eqref" data-reference="eq:momentum">[eq:momentum]</a> are preserved under time evolution if and only if the Einstein equations and <a href="#eq:covcons" data-reference-type="eqref" data-reference="eq:covcons">[eq:covcons]</a> hold.

Schematically, one finds evolution equations of the form
``` math
\begin{align}
\partial_t \mathcal{H} &= A\,\mathcal{H} + B^i \mathcal{M}_i
+ C_\nu\,\nabla_\mu T^{\mu\nu},\\
\partial_t \mathcal{M}_i &= D_i \mathcal{H}
+ E_i{}^j \mathcal{M}_j
+ F_{i\nu}\,\nabla_\mu T^{\mu\nu},
\end{align}
```
where $`A,B^i,D_i,E_i{}^j,C_\nu,F_{i\nu}`$ are functions of the lapse, shift, and geometric variables.

If the constraints vanish on one slice and $`\nabla_\mu T^{\mu\nu}=0`$, then the right–hand sides vanish identically, and the constraints remain satisfied on all subsequent slices.

This is the precise sense in which the contracted Bianchi identity implements “constraint preservation.”

## Interpretation in Modal Triplet Theory

In Modal Triplet Theory, the four–dimensional Einstein equations are not fundamental. They arise as the leading–order effective description obtained by coherent projection and internal integration of the ten–dimensional modal dynamics.

From this perspective:

- the constraints <a href="#eq:hamiltonian" data-reference-type="eqref" data-reference="eq:hamiltonian">[eq:hamiltonian]</a>–<a href="#eq:momentum" data-reference-type="eqref" data-reference="eq:momentum">[eq:momentum]</a> express compatibility conditions for coherent projection on each spatial slice,

- the evolution equations propagate this compatibility forward in the effective ordering parameter,

- the Bianchi identity guarantees that the bookkeeping closes.

Constraint preservation therefore corresponds to the statement that admissibility is maintained under effective evolution.

## Constraint Violation and Loss of Admissibility

If the effective description fails to satisfy $`\nabla_\mu T^{\mu\nu}=0`$, or if additional terms appear in <a href="#eq:einstein" data-reference-type="eqref" data-reference="eq:einstein">[eq:einstein]</a> that are not captured by the Einstein–Hilbert truncation, then constraint preservation fails.

In Modal Triplet Theory this signals that the system is approaching or crossing an admissibility boundary. The coherent projector ceases to be bounded or regular, and the four–dimensional encoding is no longer closed under evolution.

Persistent constraint violation is therefore not a physical inconsistency of the underlying modal dynamics, but a diagnostic that the effective encoding has ceased to be valid.

## Relation to Horizons and Selection Fronts

Gravitational horizons provide a canonical example of admissibility boundaries. Across a horizon, no single four–dimensional description can serve as a global right inverse of the coherent projection.

In such regimes, the $`3+1`$ constraints cannot be globally propagated in a single encoding. This manifests as irreversibility, entropy bounds, and the failure of reconstruction across the horizon.

## Summary

The contracted Bianchi identity ensures that the Einstein equations form a self–consistent bookkeeping system: constraints imposed on one spatial slice are preserved under evolution. In Modal Triplet Theory this property reflects the maintenance of admissibility of the coherent projection.

When constraint preservation fails, the breakdown is not dynamical but structural. It marks the boundary of validity of the four–dimensional encoding and the onset of selection fronts or horizon behavior.

# Maxwell and Yang–Mills Theories as Constraint–Preserving Systems

This appendix analyzes Maxwell and Yang–Mills theories from the same constraint–preservation perspective used for gravity in Appendix <a href="#app:bianchi" data-reference-type="ref" data-reference="app:bianchi">12</a>. The purpose is to make explicit the precise structural similarity between gauge theories and general relativity, while also clarifying why gauge forces do not encounter coherence capacity collapse in the manner of gravity.

## Maxwell Equations and Gauss Constraint

Maxwell’s equations in covariant form are
``` math
\begin{align}
\partial_\mu F^{\mu\nu} &= J^\nu, \label{eq:maxwell1}\\
\partial_{[\alpha}F_{\beta\gamma]} &= 0. \label{eq:maxwell2}
\end{align}
```

Performing a $`3+1`$ decomposition with electric and magnetic fields $`\mathbf{E}`$ and $`\mathbf{B}`$, these equations split into:

- the Gauss constraint,
  ``` math
  \begin{equation}
  \nabla\cdot \mathbf{E} = \rho, \label{eq:gauss}
  \end{equation}
  ```

- and evolution equations,
  ``` math
  \begin{align}
  \partial_t \mathbf{B} &= -\nabla\times \mathbf{E},\\
  \partial_t \mathbf{E} &= \nabla\times \mathbf{B} - \mathbf{j}.
  \end{align}
  ```

The Gauss constraint <a href="#eq:gauss" data-reference-type="eqref" data-reference="eq:gauss">[eq:gauss]</a> restricts admissible initial data on each spatial slice. It does not generate time evolution.

## Constraint Preservation in Electromagnetism

Taking the time derivative of the Gauss constraint yields
``` math
\begin{equation}
\partial_t(\nabla\cdot\mathbf{E}) =
\nabla\cdot(\partial_t\mathbf{E})
= -\nabla\cdot\mathbf{j}.
\end{equation}
```
Thus
``` math
\begin{equation}
\partial_t(\nabla\cdot\mathbf{E}-\rho)
= -(\partial_t\rho + \nabla\cdot\mathbf{j}).
\end{equation}
```

If the current satisfies the continuity equation
``` math
\begin{equation}
\partial_\mu J^\mu = 0,
\label{eq:continuity}
\end{equation}
```
then the right–hand side vanishes identically, and the Gauss constraint is preserved under time evolution.

This establishes Maxwell theory as a constraint–preserving system: if the constraint holds on one spatial slice and charge is conserved, it holds on all subsequent slices.

## Yang–Mills Theory and Nonabelian Gauss Law

Yang–Mills theory generalizes electromagnetism to nonabelian gauge groups. The field equations are
``` math
\begin{equation}
D_\mu F^{\mu\nu} = J^\nu,
\label{eq:ym}
\end{equation}
```
where $`D_\mu`$ denotes the gauge–covariant derivative.

In the $`3+1`$ formulation, the Gauss constraint becomes
``` math
\begin{equation}
\mathcal{G} := D_i E^i - \rho = 0,
\label{eq:ymgauss}
\end{equation}
```
with $`E^i = F^{i0}`$ and $`\rho`$ the nonabelian charge density.

As in electromagnetism, this constraint restricts admissible initial data but does not govern evolution.

## Constraint Preservation in Yang–Mills Theory

Applying the covariant derivative to <a href="#eq:ym" data-reference-type="eqref" data-reference="eq:ym">[eq:ym]</a> yields
``` math
\begin{equation}
D_\nu D_\mu F^{\mu\nu} = D_\nu J^\nu.
\end{equation}
```
The left–hand side vanishes identically as a consequence of the antisymmetry of $`F^{\mu\nu}`$ and the Yang–Mills Bianchi identity. Consistency therefore requires
``` math
\begin{equation}
D_\nu J^\nu = 0,
\label{eq:ymcons}
\end{equation}
```
which is the statement of covariant current conservation.

Under this condition, the Gauss constraint <a href="#eq:ymgauss" data-reference-type="eqref" data-reference="eq:ymgauss">[eq:ymgauss]</a> is preserved under time evolution. Yang–Mills theory is therefore a constraint–preserving system in exactly the same formal sense as electromagnetism and general relativity.

## Comparison with General Relativity

The logical structure of Maxwell, Yang–Mills, and general relativity can now be summarized uniformly:

- Each theory imposes constraints on initial data.

- Each theory has identities (Bianchi or gauge identities) that ensure constraint preservation.

- Each theory requires conservation laws for consistency.

However, the physical meaning of the constraints differs. In gauge theories, the constraints enforce internal compatibility within a fixed spacetime encoding. Violations typically indicate missing charged degrees of freedom or an incomplete description.

In general relativity, the constraints enforce compatibility of the spacetime encoding itself. Violations therefore signal loss of admissibility of the encoding rather than incomplete internal bookkeeping.

## Why Gauge Theories Do Not Exhibit Capacity Collapse

From the perspective of Modal Triplet Theory, the distinction is clear. Gauge forces arise from bundle–specific internal connections. They do not act on the shared coherence channel represented by the central circle.

As a result:

- gauge constraints can always be repaired locally by restoring missing degrees of freedom,

- no global coherence capacity is exhausted,

- the effective encoding remains invertible.

Gravity, by contrast, operates on the shared coherence channel. When coherence capacity is exhausted along this channel, no local repair is possible, and the effective description becomes noninvertible.

## Local Energy Density of Gauge Fields

Gauge theories admit local, gauge–invariant stress–energy tensors constructed from internal curvature invariants such as $`F_{\mu\nu}F^{\mu\nu}`$. This reflects the fact that gauge symmetry acts in internal fiber directions and leaves spacetime points fixed.

Energy stored in gauge fields is therefore a property of configurations within a fixed admissible spacetime encoding.

## Summary

Maxwell and Yang–Mills theories are constraint–preserving PDE systems, closely paralleling the formal structure of general relativity. The difference lies not in the mathematics of constraint preservation, but in the layer of coherence on which the constraints act.

Gauge theories enforce internal compatibility and remain reversible within admissible basins. General relativity enforces global coherence compatibility and encounters capacity limits that manifest as irreversibility, horizons, and entropy.

# Time Ordering, Projection Noninvertibility, and the Arrow of Time

This appendix formalizes the emergence of time ordering and irreversibility in Modal Triplet Theory. The analysis clarifies how a directed temporal structure arises despite the invertibility of the underlying modal dynamics, and why the arrow of time is enforced by projection rather than by microscopic dissipation.

## Underlying Modal Evolution

At the fundamental level, Modal Triplet Theory posits an evolution $`\Phi_\tau`$ on the full modal configuration space. This evolution is invertible: for every admissible configuration there exists a unique predecessor and successor under $`\Phi_\tau`$.

No preferred direction of time is selected at this level. The parameter $`\tau`$ serves only as an ordering label for the modal flow and does not correspond directly to physical time.

## Projected Evolution and Loss of Invertibility

Observable physics is obtained by projection onto the coherent sector, followed by pushforward to four–dimensional fields. The effective evolution is therefore
``` math
\begin{equation}
T_\tau = \Pi_{\mathrm{coh}} \circ \Phi_\tau .
\end{equation}
```

Unlike $`\Phi_\tau`$, the map $`T_\tau`$ is generically noninvertible. Distinct modal configurations may project to the same coherent state, particularly near admissibility boundaries.

This noninvertibility is not accidental. It reflects the finite coherence capacity of the effective description.

## Time as an Ordering of Admissible Projections

Because $`T_\tau`$ lacks a global right inverse, the effective description cannot reconstruct the past uniquely from a given state. Physical time therefore emerges as the ordering of successive admissible projections.

> Time in Modal Triplet Theory is the ordering induced by noninvertible projection onto the coherent sector.

Each application of $`T_\tau`$ discards incompatible modal alternatives. Once discarded, these alternatives are irretrievable within the effective theory. The ordering of projections thus acquires an intrinsic direction.

## The Central Circle and Universal Time Orientation

The emergence of a universal arrow of time is tied to the central circle $`S^1_{\mathrm{cen}}`$. Because this circle is the only internal structure shared across all modal bundles, any loss of coherence along this direction affects every sector simultaneously.

Coherent configurations must align their internal phase along the central circle to remain admissible. As the system evolves, successive projections enforce a monotonic ordering of this alignment. This produces a universal temporal orientation in the effective description.

No separate clock field or external time parameter is required. Time ordering is enforced structurally by the shared coherence constraint.

## Irreversibility and Entropy

Irreversibility arises when projection identifies multiple modal histories with a single effective state. The volume of configuration space eliminated by this identification provides a natural measure of entropy.

From this perspective:

- entropy increase reflects the cumulative loss of distinguishable modal alternatives,

- irreversibility is a structural consequence of projection,

- thermodynamic, measurement, and gravitational arrows of time share a common origin.

This mechanism does not rely on coarse–graining assumptions or special initial conditions. It follows from the existence of finite coherence capacity.

## Relation to Constraint Preservation

In the four–dimensional encoding, time evolution is implemented by constraint–preserving PDE systems such as Einstein’s equations and gauge theories. As shown in Appendices <a href="#app:bianchi" data-reference-type="ref" data-reference="app:bianchi">12</a> and <a href="#app:gaugeconstraints" data-reference-type="ref" data-reference="app:gaugeconstraints">13</a>, constraints imposed on one spatial slice are propagated consistently to subsequent slices.

This propagation corresponds to maintaining admissibility under the projected evolution. When constraint preservation fails, the effective description ceases to be valid, signaling the approach to an admissibility boundary.

## Selection Fronts and Temporal Direction

At selection fronts, coherence capacity is exhausted. The effective description must transition to a new admissible basin, and the projected evolution loses any approximate invertibility.

Across such fronts:

- the effective arrow of time is reinforced,

- entropy increases discontinuously,

- reconstruction across the transition is impossible.

Selection fronts therefore represent the sharpest manifestation of projection–induced time ordering.

## Summary

Time in Modal Triplet Theory is not a primitive coordinate. It is the ordering induced by successive noninvertible projections onto the coherent sector. The arrow of time reflects the structural loss of invertibility enforced by finite coherence capacity, particularly along the shared central circle.

Irreversibility, entropy, and temporal orientation are therefore unified as aspects of the same projection mechanism.

# Photons, Null Worldlines, and Gravitational Coupling

This appendix clarifies the status of massless excitations in Modal Triplet Theory, with particular emphasis on photons. We explain why photons possess no inertial mass, why Newtonian notions of inertia do not apply to them, and why they nevertheless gravitate. The analysis is fully consistent with standard general relativity and quantum field theory, while admitting a unified interpretation in terms of shared coherence bookkeeping.

## Null Worldlines and the Absence of Proper Time

In relativistic physics, the motion of a massive particle is parameterized by proper time $`\tau`$, with line element
``` math
ds^2 = -g_{\mu\nu} dX^\mu dX^\nu > 0.
```
The worldline action contains a term proportional to $`\int ds`$, whose coefficient defines the inertial mass.

For a massless excitation, such as a photon, the worldline is null:
``` math
ds^2 = 0.
```
No proper time parameter exists along such a trajectory, and there is no term of the form $`m\int ds`$ in an effective worldline action.

As a result, there is no invariant notion of rest mass or rest–frame acceleration for photons. In particular, an equation of the form $`\mathbf{F}=m\mathbf{a}`$ is not defined for null trajectories.

## Zero Inertia in the Coherent Action

From the perspective of the coherent action discussed in Appendix <a href="#app:Fma" data-reference-type="ref" data-reference="app:Fma">10</a>, inertial mass arises as the coefficient multiplying the proper–time line element in the effective action,
``` math
S_{\mathrm{wl}} = -m\int ds + S_{\mathrm{int}}.
```
Because $`ds=0`$ for null worldlines, the inertial term vanishes identically.

In Modal Triplet Theory this reflects a deeper fact: null excitations do not require rethreading of shared coherence along the central circle. There is no cost associated with bending a null history in proper time, because no proper time exists.

Photons therefore have zero inertia in precisely the sense relevant to Newton’s second law.

## Stress–Energy of Massless Fields

Despite having zero rest mass, photons carry stress–energy. In classical electromagnetism the stress–energy tensor is
``` math
T_{\mu\nu}^{\mathrm{EM}}
=
F_{\mu\alpha}F_{\nu}{}^{\alpha}
-
\frac{1}{4} g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta},
```
which is nonvanishing for propagating radiation.

In quantum field theory this generalizes to the expectation value of the stress–energy operator in photon states. In either case, massless radiation contributes to $`T_{\mu\nu}`$ and therefore to the source term in the Einstein equations.

## Gravitational Coupling of Photons

General relativity couples gravity to stress–energy rather than to rest mass alone. Consequently, photons gravitate despite having zero inertial mass.

From the MTT perspective, this is natural. Gravity does not measure inertia directly. It measures the load imposed on shared coherence capacity by the projected stress–energy content of a configuration.

Photons contribute to this load through their energy–momentum flux, even though they do not contribute an inertial term proportional to proper–time curvature.

This distinction explains:

- gravitational lensing of light,

- gravitational redshift,

- the contribution of radiation to cosmological expansion,

- the universality of gravitational coupling.

## Why Photons Still Follow Geodesics

In the absence of nongravitational interactions, photons follow null geodesics of the spacetime metric. This follows from the geometric optics limit of Maxwell’s equations in curved spacetime, which yields the null geodesic equation.

In Modal Triplet Theory, this behavior reflects the fact that null coherent excitations propagate along directions that do not strain the shared coherence channel. Their trajectories are determined entirely by the spacetime encoding that maintains global coherence compatibility.

## Relation to Inertial and Gravitational Mass

The analysis above makes clear that inertial mass and gravitational coupling are distinct but related concepts:

- inertial mass measures the coherence cost of bending timelike histories,

- gravitational coupling measures the redistribution of coherence capacity in response to stress–energy.

For massive particles these quantities coincide numerically because the same shared coherence channel underlies both effects. For massless particles the inertial contribution vanishes, while the gravitational contribution remains finite.

This distinction resolves apparent paradoxes in which photons “gravitate without having mass.”

## Summary

Photons possess no inertial mass because they follow null worldlines and do not admit a proper–time action. Nevertheless, they gravitate because gravity couples to stress–energy rather than to rest mass alone.

In Modal Triplet Theory, this distinction is understood structurally: null excitations do not strain shared coherence along the central circle in the manner required to produce inertia, but they do contribute to the global bookkeeping of coherence capacity through their energy–momentum content.

# Mass Renormalization and Coherence Capacity Bounds

This appendix explains how mass renormalization and running are constrained in Modal Triplet Theory by coherence capacity, with particular emphasis on the role of the shared central circle. The purpose is not to replace standard renormalization group methods, but to clarify why only certain renormalization trajectories are physically realizable within an admissible coherent description.

## Renormalization in Conventional Quantum Field Theory

In conventional quantum field theory, masses and couplings depend on a renormalization scale $`\mu`$. For a fermion mass, one writes schematically
``` math
\begin{equation}
\mu\frac{d m(\mu)}{d\mu} = \gamma_m(\mu)\, m(\mu),
\label{eq:massRG}
\end{equation}
```
where $`\gamma_m`$ is the anomalous dimension.

Formally, renormalization permits a wide range of trajectories in parameter space, with counterterms adjusted to match physical observables. Consistency is enforced order by order in perturbation theory, but the underlying framework does not itself restrict which RG flows are physically meaningful.

## MTT Perspective: Renormalization as Encoding Deformation

In Modal Triplet Theory, renormalization does not represent arbitrary redefinitions of parameters. Instead, it corresponds to a deformation of the effective encoding of the coherent sector as the resolution scale changes.

The effective four–dimensional description is valid only as long as:

- the coherent projector remains bounded,

- spectral gaps controlling the coherent sector remain nonzero,

- truncation errors remain controlled.

These conditions define an admissible universality class. Renormalization group flow must remain within this class to correspond to a valid physical description.

## Projector Control and Spectral Gaps

Let $`\Pi_{\mathrm{coh}}`$ denote the joint coherent projector and $`\lambda_\ast`$ the smallest spectral gap controlling deformations of the coherent sector, including those involving the central circle.

Perturbation theory for spectral projectors implies that variations of $`\Pi_{\mathrm{coh}}`$ scale as
``` math
\begin{equation}
\|\delta \Pi_{\mathrm{coh}}\| \;\sim\;
\frac{\|\delta L\|}{\lambda_\ast^2},
\label{eq:projbound}
\end{equation}
```
where $`L`$ denotes the relevant Laplace–type operators.

As renormalization scale changes, effective masses and couplings change the operator $`L`$ through loop corrections and threshold effects. If these changes are too large, the bound <a href="#eq:projbound" data-reference-type="eqref" data-reference="eq:projbound">[eq:projbound]</a> is violated, and the coherent projector ceases to be well defined.

Thus, renormalization is constrained by the requirement that $`\lambda_\ast`$ remain bounded away from zero.

## Role of the Central Circle

The central circle $`S^1_{\mathrm{cen}}`$ enters every modal bundle and therefore every spectral gap. Any renormalization effect that effectively alters the spectrum associated with this circle affects all sectors simultaneously.

Consequently:

- mass renormalization cannot be tuned independently in different sectors,

- large running would imply large deformations of the shared coherence channel,

- such deformations are forbidden once coherence capacity is finite.

This explains why inertial mass, once generated, exhibits remarkable stability across wide ranges of scale. Renormalization effects are present, but they are constrained to remain within the admissible deformation range of the central circle sector.

## Curvature–Mass Drift Bounds

In curved backgrounds, effective masses acquire curvature–dependent shifts. A typical form appearing in the MTT effective description is
``` math
\begin{equation}
m^2(x) = m_0^2 + \beta R(x),
\label{eq:curvmass}
\end{equation}
```
where $`R`$ is the Ricci scalar and $`\beta`$ a representation–dependent coefficient.

As long as coherence capacity remains positive, the drift of $`m(x)`$ is bounded:
``` math
\begin{equation}
\left|\nabla_\mu \log m(x)\right|
\;\le\;
\frac{|\beta|}{2\lambda_{\min}}\,|\nabla_\mu R(x)|,
\end{equation}
```
where $`\lambda_{\min}`$ is a lower bound on the relevant spectral gap.

This inequality makes explicit that rapid or unbounded mass variation is incompatible with admissible coherent projection.

## Thresholds, Decoupling, and Universality

Heavy degrees of freedom decouple from the effective description when their masses exceed the scale at which coherent projection can resolve them. In MTT this decoupling is not merely a kinematic statement, but a structural one: modes whose excitation would exceed coherence capacity are excluded from the admissible sector.

As a result:

- threshold effects are smooth within admissible regimes,

- universality of low–energy physics follows from stability of the shared coherence channel,

- apparent fine tuning is replaced by admissibility selection.

## Implications for Naturalness

The coherence capacity perspective offers a reformulation of naturalness problems. Large radiative corrections are not forbidden mathematically, but they are physically meaningless if they drive the system outside the admissible universality class.

Inertia and mass parameters are therefore protected not by symmetry alone, but by the finite coherence capacity associated with the central circle.

## Summary

Renormalization group flow in Modal Triplet Theory is constrained by the requirement that coherent projection remain admissible. The central circle, as the shared coherence channel, imposes universal bounds on mass renormalization and curvature–induced drift.

Masses may run, but only within the deformation range permitted by coherence capacity. This explains both the robustness of inertial mass and the universality of low–energy physics without invoking arbitrary counterterm tuning.

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
