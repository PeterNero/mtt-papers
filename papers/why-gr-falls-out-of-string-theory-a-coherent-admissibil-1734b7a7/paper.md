---
author:
- Peter Nero
current_version: v2
date: July 2026, Version 2
generated_from_main_tex_sha256: 79d64f02f02218a6e859a06b20225a245e24d610c01bb4346fce361ab39f1711
paper_id: why-gr-falls-out-of-string-theory-a-coherent-admissibil-1734b7a7
release_state: zenodo_released
released_version: v2
title: |
  **Why General Relativity Appears in Perturbative String Theory:**
  A careful MTT interpretation of worldsheet consistency and target-space dynamics
zenodo_doi: 10.5281/zenodo.21719670
zenodo_record_id: 21719670
zenodo_url: "https://zenodo.org/records/21719670"
---

<div class="center">

**Abstract**

</div>

> The statement that General Relativity “falls out of string theory” is memorable but easy to misunderstand. A perturbative string background is described by a two-dimensional quantum field theory. Its couplings include the target-space metric, antisymmetric tensor, dilaton, and, in appropriate models, gauge and fermionic data. Requiring quantum Weyl consistency constrains these couplings. At leading order those constraints agree, after the required conventions and field redefinitions, with equations derived from a target-space effective action containing the Einstein-Hilbert term. Pure Einstein gravity appears only in a further low-energy and restricted field corner. This paper explains that chain without treating measurement, observation, or mathematical representation as physically privileged acts. It then gives the restrained Modal Triplet Theory (MTT) interpretation: the worldsheet and spacetime equations may be two diagnostics emitted by one preprojection source, but this is established only when explicit source maps and a controlled comparison square are constructed. The formal theorem is owned by the companion technical paper and is not repeated here. Current q79 work provides five of twelve worldsheet contract rows, partially provides two, and leaves five open. The result is therefore an explanatory bridge and a concrete completion program, not a proof that GR and string theory are the same theory or that MTT has already derived either one in full.

# Version 2 Revision Note

<div class="description">

Version 1.0, released in January 2026.

The previous version repeated an equivalence theorem, assumed the relation between MTT proper-time flow and worldsheet RG, and presented spectral-gap suppression as if it controlled every string and spacetime correction.

Version 2 is an explanatory companion. It gives the standard derivation in ordinary language, distinguishes each approximation, and refers the formal diagnostic-square result to its technical owner.

The motivating intuition remains: agreement between worldsheet and spacetime consistency conditions may point to a shared upstream description.

The physical q79 worldsheet, its visible–hidden bundle, the exact infrared conformal theory, GSO and modular data, and the selected upper MTT action are not yet complete.

</div>

# The phrase and the possible misunderstanding

Physicists often say that General Relativity falls out of string theory. What they mean is not that the Einstein equations are hidden in a string and can be read off without assumptions. They mean that consistency of the quantized string worldsheet constrains the background through which the string propagates, and that the leading target-space equation contains Einstein’s curvature dynamics.

This is a striking result because the calculation begins in two dimensions. The object being quantized is a map
``` math
X:\Sigma\longrightarrow Y
```
from a worldsheet $`\Sigma`$ into a target space $`Y`$. The metric of $`Y`$ appears as a coupling in the two-dimensional theory. Quantum consistency of that theory then becomes an equation for the target metric.

The slogan becomes misleading when it erases the intermediate steps. The worldsheet is not four-dimensional spacetime. Its renormalization scale is not automatically physical time. The target equations contain more than the metric. Their relation to an effective action is perturbative and scheme-aware. Four-dimensional GR appears only after a compactification and low-energy reduction.

## Four statements of increasing strength

<div class="center">

<div class="tabularx">

@L0.27X@ Statement & Status
The metric beta function contains Ricci curvature & Standard leading-order sigma-model result.
Vanishing Weyl-anomaly coefficients agrees with target effective equations & Standard perturbative result at a declared order and scheme.
Pure four-dimensional Einstein gravity follows & Conditional on field restrictions, compactification, scale separation, and truncation.
Worldsheet and spacetime equations descend from one selected MTT source & An open source-construction problem, formalized conditionally in the companion technical paper.

</div>

</div>

Only the first two are part of the ordinary perturbative string derivation.

# The worldsheet as an ordinary physical system

## Background fields become couplings

At lowest order, the sigma-model action contains terms of the form
``` math
\begin{align}
S_\Sigma[X]
\sim{}&\frac{1}{4\pi\alpha'}\int_\Sigma
\sqrt h\,h^{ab}g_{\mu\nu}(X)
\partial_aX^\mu\partial_bX^\nu\,d^2\sigma \nonumber\\
&+\frac{i}{4\pi\alpha'}\int_\Sigma
\epsilon^{ab}B_{\mu\nu}(X)
\partial_aX^\mu\partial_bX^\nu\,d^2\sigma
+\frac{1}{4\pi}\int_\Sigma\sqrt h\,R^{(2)}\Phi(X)\,d^2\sigma .
\label{eq:sigma}
\end{align}
```
The target metric $`g`$, two-form $`B`$, and dilaton $`\Phi`$ are therefore couplings from the worldsheet point of view. In heterotic theory there are also gauge-bundle couplings and chiral worldsheet fields. Ghosts, spin structures, a path-integral measure, and global data are essential parts of the quantum theory.

Nothing about this description gives measurement a special ontological role. The worldsheet theory is a physical quantum system. A detector is another physical system coupled to it. The consistency condition discussed here is about quantum symmetries and renormalization, not about an observer causing an outcome.

## Why Weyl symmetry matters

The worldsheet metric $`h`$ is partly redundant: locally rescaling it should not change physical string propagation. Quantization can spoil this Weyl symmetry. The failure is encoded in anomaly coefficients, commonly described through beta functions for the couplings.

For one conventional choice of fields and scheme, the metric coefficient begins as
``` math
\bar\beta^g_{\mu\nu}
=\alpha'\left(
R_{\mu\nu}+2\nabla_\mu\nabla_\nu\Phi
-\frac14H_{\mu\rho\sigma}H_\nu{}^{\rho\sigma}
\right)+O(\alpha'^2).
```
This formula immediately corrects a common oversimplification. The equation is not normally $`R_{\mu\nu}=0`$. It is coupled to the dilaton and the flux $`H`$, and the other background fields have their own equations.

## A fixed point is not the whole string theory

Vanishing anomaly coefficients identifies a consistent background in the perturbative framework. A complete string construction also asks whether the worldsheet has the correct central charge, modular and GSO properties, factorization, anomaly cancellation, infrared limit, and higher-genus behavior. A local beta-function calculation can be right while the proposed global string background is incomplete.

# How the target-space action enters

At string tree level and leading derivative order, the NS–NS sector is organized by an effective action of the schematic form
``` math
S_{\mathrm{eff}}
\sim\int_Y\sqrt{-g}\,e^{-2\Phi}
\left[
R+4|\nabla\Phi|^2-\frac1{12}|H|^2+O(\alpha')
\right]d^Dx .
```
Its Euler–Lagrange equations match the worldsheet Weyl conditions after compatible field redefinitions at the calculated order .

This agreement is the real content behind the slogan. It is stronger than a visual resemblance between formulas: two calculations in one perturbative string construction lead to compatible conditions on the background. It is weaker than identity of the worldsheet and target theories.

## Why field redefinitions matter

Coordinates on the space of couplings are not unique. A local redefinition of $`g`$, $`B`$, and $`\Phi`$ changes the component form of beta functions and of the effective action. Comparisons are therefore made in a fixed scheme or through an explicit redefinition. A coefficient mismatch may be a convention mismatch, but that possibility must be demonstrated rather than assumed.

## The expansions are separate

Two perturbative controls are often compressed into one phrase:

- the alpha-prime expansion controls higher derivatives relative to the string length; and

- the string-coupling expansion controls worldsheet genus and quantum loops in target spacetime.

A background can be weakly curved in string units while the string coupling is not small, or conversely. Compactification and Kaluza–Klein truncation introduce further scales. An MTT projection estimate would be another, logically separate error.

# Where Einstein gravity appears

The target action contains the Einstein–Hilbert term $`R`$, but it also contains the dilaton, flux, gauge fields, fermions, sources, higher-curvature terms, and loop corrections. To reach ordinary four-dimensional GR one typically needs:

1.  a background whose extra dimensions can be consistently reduced;

2.  energies well below the omitted Kaluza–Klein and string modes;

3.  a controlled treatment or stabilization of moduli;

4.  a specified four-dimensional frame and Newton normalization;

5.  a suitable restriction of fluxes, sources, and additional fields; and

6.  small or explicitly retained higher-derivative and loop corrections.

In that corner, the leading metric equation takes the familiar form
``` math
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G_{\mathrm N}T_{\mu\nu}+\text{controlled corrections}.
```
The result is an effective limit. Calling it effective is not dismissive. Effective theories can be precise, predictive, and fundamental to the scale at which their variables are appropriate.

## Does string theory derive GR?

There are two reasonable answers, depending on what “derive” means.

If it means that perturbative string consistency predicts target equations whose low-energy metric sector includes Einstein dynamics, then yes. This is a standard and important derivation.

If it means that string theory uniquely selects our four-dimensional background, matter content, couplings, state, and all gravitational observables, then no such general statement follows from the beta-function calculation alone.

# The restrained MTT interpretation

MTT asks whether the worldsheet and spacetime descriptions can be understood as projections of one preprojection object. This suggestion is attractive because it turns a relation between lower theories into a question about commuting maps:
``` math
\begin{array}{ccc}
&\text{selected upper source}&\\
\swarrow&&\searrow\\
\text{worldsheet record}&&\text{spacetime record}\\
\downarrow&&\downarrow\\
\text{Weyl diagnostic}&\longleftrightarrow&
\text{effective field equation}.
\end{array}
```

The diagram is not a proof. Every arrow needs a definition. The two lower records must carry the same source provenance rather than being chosen independently to agree. The bottom comparison needs an error estimate and must not discard an uncontrolled equation.

## The technical result lives elsewhere

The companion paper *Worldsheet and Spacetime Consistency as a Conditional Diagnostic Square* gives the formal statement. In brief, if the two diagnostics intertwine through an explicit comparison map with a bounded inverse on the compared subspace, then an exact or small worldsheet residual transfers to an exact or controlled target residual. It also proves that merely sharing a fixed point is insufficient.

This paper does not repeat that theorem. Its job is to explain what the maps mean physically and why their hypotheses are necessary.

## What a spectral gap can and cannot do

A spectral gap may help control leakage from a retained coherent sector. It cannot by itself create:

- the target manifold or its Lorentzian structure;

- the worldsheet fields, measure, BRST complex, or GSO projection;

- the sigma-model beta functions;

- the target effective action and its normalization; or

- the comparison between worldsheet and target diagnostics.

For the same reason, alpha-prime is not automatically the inverse of an MTT gap. A source theorem may relate the scales, but the relation must be derived with dimensions and coefficients intact.

# The q79 position

The current q79 Fu–Yau route is the strongest physical compactification candidate in the MTT program. It is not the auxiliary literal product $`S^1\times\mathrm{Lens}\times\mathrm{Nil}`$. Circle–Lens–Nil language is best retained as a local rank or operator filtration, while the physical worldsheet question is posed on the selected q79 geometric branch.

<div class="center">

<div class="tabularx">

@L0.23X L0.18@ Group & Required content & Status
Available rows & Time-oriented target, Fu–Yau charge/Bianchi data, curvature-level visible cancellation, universal heterotic central charge, and declared low-energy parity limit & 5 of 12
Partial rows & Exact infrared conformal theory and modular/GSO factorization & 2 of 12
Open rows & Global differential gerbe, all-orders target, string-field vertices, infrared/soft completion, and all-genus or nonperturbative definition & 5 of 12

</div>

</div>

The authoritative blocker $`B.\mathrm{QG}.01`$ requires all twelve rows on the same physical nonpullback visible–hidden bundle. The upper-action blocker $`B.\mathrm{ACTION}.01`$ requires the common source whose descendants produce the accepted lower structures. Neither is closed by explaining the standard beta-function result again.

# What would count as progress

The most useful next result would not be another general shadow-bridge statement. It would fill a missing object:

1.  construct the physical visible and hidden holomorphic bundles in one HYM chamber;

2.  close the global differential Green–Schwarz data;

3.  construct the q79 heterotic worldsheet theory and its infrared SCFT;

4.  calculate analytic characters and the modular-invariant GSO sum;

5.  derive worldsheet anomaly coefficients and target equations from the same source at the same order;

6.  publish the comparison map, residual, inverse estimate, conventions, and hashes; and

7.  only then compare states and observables.

This sequence is intentionally concrete. It makes failure informative. Perhaps the bundle does not exist in the required chamber, the GSO sum fails, or the comparison becomes singular. Such an outcome would narrow or reject the proposed MTT string encoding rather than being rephrased as success.

# Questions the slogan often hides

## Is the worldsheet literally spacetime?

No. It is the two-dimensional surface traced by the string. Its coordinates and RG scale are not the coordinates and time of target spacetime.

## Does vanishing of one beta function suffice?

No. The full background, anomaly, ghost, modular, GSO, factorization, and global data matter. In heterotic theory the bundle and Green–Schwarz sector are indispensable.

## Does this quantize gravity in the usual sense?

Perturbative closed strings contain a massless spin-two excitation and provide quantum gravitational amplitudes in their regime. The MTT interpretation explored here is different: it asks whether quantized upper dynamics and projection produce the gravitational effective medium and its stress response. That proposal still needs the selected upper action and quantum transport.

## Are GR and string theory equally fundamental?

The beta-function bridge does not decide ontology. It establishes a controlled relation between descriptions. MTT’s preprojection proposal would place both downstream of an upper source, but only after that source is constructed.

# Conclusion

General Relativity appears in perturbative string theory through a beautiful but qualified chain. Target fields are worldsheet couplings; quantum Weyl consistency constrains those couplings; the constraints agree with target effective equations; and a restricted low-energy compactified corner yields Einstein gravity.

MTT may eventually explain why the worldsheet and spacetime diagnostics agree by deriving both from one selected preprojection structure. The technical conditions for such an explanation are now stated in the companion diagnostic-square paper. The physical q79 source is not complete: five worldsheet rows are available, two are partial, and five are open.

The right conclusion is therefore neither “string theory and GR are the same” nor “the relation is only an analogy.” The standard perturbative bridge is real. The MTT common-source explanation is a precise, testable, unfinished program.

<div class="thebibliography">

99

D. Friedan, “Nonlinear models in $`2+\epsilon`$ dimensions,” *Physical Review Letters* **45** (1980), 1057–1060. <https://doi.org/10.1103/PhysRevLett.45.1057>

C. G. Callan, D. Friedan, E. J. Martinec, and M. J. Perry, “Strings in background fields,” *Nuclear Physics B* **262** (1985), 593–609. <https://doi.org/10.1016/0550-3213(85)90506-1>

R. R. Metsaev and A. A. Tseytlin, “Order $`\alpha'`$ (two-loop) equivalence of the string equations of motion and the sigma-model Weyl invariance conditions,” *Nuclear Physics B* **293** (1987), 385–419. <https://doi.org/10.1016/0550-3213(87)90077-0>

C. M. Hull and P. K. Townsend, “String effective actions from sigma-model conformal anomalies,” *Nuclear Physics B* **301** (1988), 197–223. <https://doi.org/10.1016/0550-3213(88)90692-5>

P. Nero, *Worldsheet and Spacetime Consistency as a Conditional Diagnostic Square*, Version 2, 2026. <https://doi.org/10.5281/zenodo.21719524>

P. Nero, *A Projection-First Reframing of String Theory: Conditional Encodings, Worldsheet Gates, and the q79 Boundary*, Version 2, 2026.

</div>
