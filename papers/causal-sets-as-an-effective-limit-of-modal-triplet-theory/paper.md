---
abstract: |
  A causal set can be obtained from an effective Modal Triplet Theory spacetime once a sampling rule is supplied, but the sampling rule is additional data. For a globally hyperbolic four-dimensional spacetime, any locally finite set of sampled events inherits a partial order from the spacetime causal relation. A Poisson process with intensity proportional to the spacetime volume measure is almost surely locally finite on every relatively compact region; in Minkowski spacetime its law is Lorentz invariant because the intensity measure is invariant. These are exact kinematic statements. They do not identify the causal set as fundamental, derive the sprinkling intensity, or convert an internal q79 spectral gap into a four-dimensional event density. Such a conversion requires a base-resolution theorem with metric normalization and an explicit internal-to-spacetime map. Causal sets therefore remain a valid conditional coarse-graining or observational encoding of an MTT spacetime, not a currently selected consequence of the internal finite geometry.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: f1111f4d18604bb848ce49fb4d1cb7ac82f579262799dff08b3a65bcc17ecb0d
paper_id: causal-sets-as-an-effective-limit-of-modal-triplet-theory
release_state: zenodo_released
released_version: v2
title: |
  Causal Sets as a Conditional Coarse-Graining of Modal Triplet Theory:
  Kinematic Construction, Sampling Choices, and Scale-Typing Boundary
zenodo_doi: 10.5281/zenodo.21665949
zenodo_record_id: 21665949
zenodo_url: "https://zenodo.org/records/21665949"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *Causal Sets as an Effective Limit of Modal Triplet Theory*.

The original paper identified an internal modal gap with a four-dimensional sprinkling density and described Poisson sampling as derived rather than chosen.

The spacetime, point process, intensity measure, causal order, and local-finiteness assumptions are now typed separately. The exact kinematic construction is proved without a cross-sector scale claim.

A locally finite sample of a causal spacetime inherits a causal-set order, and covariant Poisson sprinkling gives the standard Lorentz-invariant kinematic model in Minkowski spacetime.

MTT must derive a physical event/sampling law and its four-dimensional intensity from the selected branch before the causal set can be called an MTT prediction.

</div>

# Causal sets and effective spacetime

A causal set is a pair $`(C,\preceq)`$ such that:

1.  $`\preceq`$ is reflexive;

2.  $`\preceq`$ is antisymmetric;

3.  $`\preceq`$ is transitive;

4.  every order interval
    ``` math
    I(x,y)=\{z\in C:x\preceq z\preceq y\}
    ```
    is finite.

The order represents causal precedence, while local finiteness supplies discreteness .

MTT currently reaches a selected globally hyperbolic four-dimensional spacetime at a conditional gravity/QFT tier. The question in this paper is not whether spacetime is fundamentally discrete. It is whether a causal-set description can be extracted from that effective spacetime.

# The exact kinematic construction

<div id="thm:inherit" class="theorem">

**Theorem 1** (Inherited causal-set order). *Let $`(Y_4,g)`$ be a causal spacetime, and let $`C\subset Y_4`$ be a set such that $`C\cap K`$ is finite for every compact $`K\subset Y_4`$. Define
``` math
x\preceq y
 \quad\Longleftrightarrow\quad
 y\in J^+(x).
```
If every causal diamond $`J^+(x)\cap J^-(y)`$ is compact, then $`(C,\preceq)`$ is a causal set.*

</div>

<div class="proof">

*Proof.* The causal relation is reflexive and transitive. Causality excludes a nontrivial closed causal curve, giving antisymmetry. For $`x\preceq y`$,
``` math
I(x,y)
 =
 C\cap J^+(x)\cap J^-(y).
```
The diamond is compact, so the assumed local finiteness of $`C`$ makes this intersection finite. ◻

</div>

Global hyperbolicity supplies the compact-diamond hypothesis. The theorem is purely kinematic: it uses a continuum causal spacetime and a locally finite sample. It does not determine how the sample is generated.

# Poisson sprinkling

Let $`\mu_g`$ be the spacetime volume measure and let $`\rho>0`$. A Poisson point process with intensity measure
``` math
\Lambda(B)=\rho\,\mu_g(B)
```
has
``` math
\Pr[N(B)=n]
 =
 e^{-\Lambda(B)}\frac{\Lambda(B)^n}{n!}
```
for measurable regions of finite volume, with independent counts on disjoint regions.

<div id="thm:poisson" class="theorem">

**Theorem 2** (Poisson local finiteness). *On a sigma-finite spacetime measure space, a Poisson process with locally finite intensity measure has finitely many points in every relatively compact finite-volume region almost surely. Combined with <a href="#thm:inherit" data-reference-type="ref+label" data-reference="thm:inherit">1</a> on a globally hyperbolic spacetime, it produces a causal set almost surely.*

</div>

<div class="proof">

*Proof.* For such a region $`B`$, $`N(B)`$ is a Poisson random variable with finite mean $`\Lambda(B)`$, and therefore takes a finite integer value almost surely. A countable exhaustion by relatively compact regions gives local finiteness simultaneously. ◻

</div>

## Lorentz invariance

In Minkowski spacetime, the volume measure is invariant under proper orthochronous Poincare transformations. Therefore the law of a homogeneous Poisson process with intensity $`\rho\,d^4x`$ is invariant. Individual realizations are not symmetric configurations; the probability law is.

On a generic curved spacetime the analogous statement is covariance under isometries of $`(Y_4,g)`$, not global Lorentz invariance. A deterministic lattice or foliation-based sampling can select a preferred frame.

# Why the density is not derived from an internal gap

Suppose $`\lambda_{\mathrm{int}}`$ is an eigenvalue of an operator on the internal compactification $`X_6`$. A four-dimensional sprinkling intensity has units of inverse four-volume. The relation
``` math
\rho\stackrel{?}{=}f(\lambda_{\mathrm{int}})
```
is not defined until the internal metric normalization, four-dimensional metric normalization, reduction moduli, and a cross-sector response map are fixed.

<div id="prop:scale" class="proposition">

**Proposition 3** (Scale-typing obstruction). *An internal spectral gap alone cannot canonically determine a four-dimensional sprinkling intensity.*

</div>

<div class="proof">

*Proof.* Rescale the internal and external metrics independently. The internal eigenvalue and the external four-volume transform with independent powers. No relation between them is invariant unless additional reduction data constrain the rescalings and define a unit-preserving map. ◻

</div>

The same obstruction appears in the finite-filter and gravitational-collapse papers. It does not say that a relation is impossible. It identifies the missing theorem.

# Alternative coarse-grainings

Poisson sprinkling is not the only way to produce a locally finite sample. Examples include:

- detector records in a bounded observational protocol;

- a covariantly defined point process with non-Poisson correlations;

- a finite event set produced by a hybrid selection dynamics;

- an adaptive cover or net used only for numerical approximation.

Each choice answers a different question. Detector records describe an operational history. A Poisson process is a statistically Lorentz-invariant encoding. A numerical net is a discretization tool. None should be called the fundamental event ontology without an additional physical argument.

The companion event-selection paper gives sufficient dwell-time and hazard conditions for dynamically generated events to be locally finite. That dynamic problem is deliberately not duplicated here.

# What is and is not reconstructed

The order plus number principle of causal-set theory suggests that causal order and counting density can encode much of Lorentzian geometry under appropriate manifoldlike conditions. The present construction starts from the continuum geometry, so it does not prove the reverse reconstruction or manifoldlikeness of an arbitrary causal set.

<div class="center">

| Statement | Status | Boundary |
|:---|:---|:---|
| Locally finite sample inherits causal order | Exact | <a href="#thm:inherit" data-reference-type="ref+label" data-reference="thm:inherit">1</a>. |
| Poisson sprinkling is locally finite | Exact | <a href="#thm:poisson" data-reference-type="ref+label" data-reference="thm:poisson">2</a>. |
| Minkowski Poisson law is Lorentz invariant | Exact | Invariance is statistical, not realization-wise. |
| Causal set reconstructs the input continuum | Not shown | Requires manifoldlikeness and reconstruction results. |
| MTT selects Poisson statistics | Open | No selected event or sampling law. |
| MTT selects the density from q79 gap | Open/ill-typed without bridge | Needs base-resolution and unit map. |
| Causal set is fundamental in MTT | Not claimed | Current role is effective encoding. |

</div>

# Discussion

The corrected relation between MTT and causal sets is straightforward:
``` math
\text{selected effective }(Y_4,g)
\;+\;
\text{declared locally finite sampling law}
\longrightarrow
\text{causal set}.
```
That result is useful. It permits causal-set observables and reconstruction tools to be applied to an MTT spacetime, and it provides a concrete way to compare continuum and discrete descriptions.

The missing density theorem is also a productive target. A valid derivation would map selected q79 geometry and the four-dimensional metric to an event intensity or detector-resolution functional with units and covariance preserved. Until that map exists, varying $`\rho`$ is an encoding parameter, not a prediction.

# Conclusion

Causal sets are compatible with MTT as a conditional coarse-graining of its effective spacetime sector. The inherited order and Poisson local-finiteness results are exact. The physical sampling law and its density are not.

This distinction preserves both programs. Causal-set mathematics can be used without claiming that MTT has derived fundamental discreteness, and MTT can seek a dynamical event law without building Poisson statistics into its premises.

<div class="thebibliography">

99

L. Bombelli, J. Lee, D. Meyer, and R. D. Sorkin, “Space-time as a causal set,” *Physical Review Letters* **59** (1987), 521–524.

R. D. Sorkin, “Causal sets: Discrete gravity,” in A. Gomberoff and D. Marolf, eds., *Lectures on Quantum Gravity*, Springer, 2005, pp. 305–327.

G. Brightwell and R. Gregory, “Structure of random discrete spacetime,” *Physical Review Letters* **66** (1991), 260–263.

D. J. Daley and D. Vere-Jones, *An Introduction to the Theory of Point Processes, Volume I*, Springer, 2003.

P. Nero, *Modal Triplet Theory: Foundations*, current revised MTT paper corpus, 2026.

P. Nero, *Controlled Coherent Reduction to Four-Dimensional Einstein Gravity*, current revised MTT paper corpus, 2026.

</div>
