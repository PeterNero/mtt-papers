---
abstract: |
  A scattering amplitude is not determined by field content or an action symbol alone. It requires a quantum observable algebra, state or asymptotic representation, gauge reduction, renormalized products, a kinematic regime, parameter values, and external-state conventions. On generic curved or time-dependent spacetimes, a global $`S`$-matrix may not exist and in–in observables replace amplitudes.

  This paper gives Modal Triplet Theory (MTT) a rigorous amplitude interface. We define the complete typed record required for perturbative correlators, LSZ amplitudes, and in–in observables. We prove a coefficient-transport theorem: an intertwiner that preserves the algebra, state, free contractions, interaction, renormalized time-ordered products, gauge identities, and external-state maps preserves every declared perturbative coefficient. Under the additional LSZ or Haag–Ruelle hypotheses it preserves scattering amplitudes. We also prove two nonselection results. The action and graph grammar do not select a state or scattering regime, and replaying observed parameters inside a standard amplitude formula is equivalence at those inputs rather than a new prediction.

  The current MTT ledger then has a precise interpretation. The selected q79 twisted-Dirac source composes with standard CAR/AQFT machinery to give a free even local net. A formal perturbative BV/QME bridge and embedded renormalized-Standard-Model profile equivalence are available at their declared tiers. Standard gauge quantization is imported, measured profile coordinates remain inputs, and a geometry-selected upper action, fixed-coupling interacting gauge–BRST $`C^*`$-completion, full RG and threshold transport, uncertainty budget, and held-out observable packet remain open. Thus MTT has a coherent conditional amplitude pipeline, not yet a no-input first-principles phenomenology.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, July 2026
generated_from_main_tex_sha256: 6a014ddb181bd264184982f900600fd524393139b45afe20aec8d2f535162fbe
paper_id: modal-triplet-theory-quantum-amplitudes-from-modal-geom-3b4eaef7
release_state: zenodo_released
released_version: v3
title: |
  **Conditional Quantum Amplitudes in Modal Triplet Theory:**
  Typed Inputs, Regime Selection, and the Prediction Boundary
zenodo_doi: 10.5281/zenodo.21715418
zenodo_record_id: 21715418
zenodo_url: "https://zenodo.org/records/21715418"
---

# Version 3 revision note

#### Supersedes.

Version 2.0, DOI [10.5281/zenodo.18329567](https://doi.org/10.5281/zenodo.18329567).

#### Reason.

The earlier version described a complete first-principles derivation of amplitudes, running, anomaly cancellation, and phenomenology from modal geometry. That description conflated a conditional pAQFT construction, imported gauge quantization, and same-input Standard-Model replay with selected source derivation and held-out prediction.

#### Resolution.

Version 3 defines every required input, proves a conditional coefficient and amplitude transport theorem, distinguishes scattering from in–in observables, and adds exact state/regime and parameter-provenance nonselection results. Benchmark formulas are retained only as illustrations of the typed pipeline.

#### Retained result.

The paper retains the valid statement that, once the same renormalized quantum data and parameter values are supplied, MTT and Standard-Model presentations produce the same perturbative coefficients on the common domain.

#### Remaining boundary.

A selected upper action, nonperturbative interacting gauge–BRST completion, no-knob parameter source, full multi-loop transport, covariance and uncertainty packet, and held-out observable comparison remain open.

# What an amplitude actually depends on

The word “amplitude” often compresses a long construction. In Minkowski-space textbook calculations the background, vacuum, asymptotic states, gauge fixing, and renormalization convention are so familiar that they become invisible. They cannot be omitted in a derivation claim.

At least three outputs must be distinguished:

1.  local or time-ordered correlation functions;

2.  in–in expectation values for a specified initial state and closed-time contour;

3.  in–out scattering amplitudes between asymptotic particle states.

The first can exist without either of the latter. The second is natural in cosmology and nonequilibrium settings . The third requires a suitable asymptotic regime and, for LSZ, poles and residues associated with one-particle states .

The purpose of this paper is to state exactly what MTT must provide, what standard QFT supplies after that point, and what current MTT results actually close.

# The typed amplitude record

<div id="def:record" class="definition">

**Definition 1** (Perturbative quantum record). A perturbative quantum record on a declared domain is
``` math
\mathfrak Q=
(Y_4,\mathcal A,\omega,D_0,G,\mathcal S_{\mathrm{int}},
\mathcal B_{\mathrm{BV}},\mathcal T^{\mathcal R},\mathfrak p,\mathfrak c,\mathfrak P),
```
where:

1.  $`Y_4`$ is a globally hyperbolic spacetime or a specified local causal domain;

2.  $`\mathcal A`$ is a local quantum observable or field algebra;

3.  $`\omega`$ is a state, with Hadamard regularity when local curved spacetime renormalization requires it;

4.  $`D_0`$ is the free Green-hyperbolic operator and $`G`$ denotes the declared causal, two-point, or time-ordered kernels;

5.  $`\mathcal S_{\mathrm{int}}`$ is the interaction functional;

6.  $`\mathcal B_{\mathrm{BV}}`$ records gauge fixing, ghosts, the BV/BRST complex, and its identities;

7.  $`\mathcal T^{\mathcal R}`$ is a family of renormalized time-ordered products in scheme $`\mathcal R`$;

8.  $`\mathfrak p`$ is the complete parameter and matching record;

9.  $`\mathfrak c`$ is the calculation regime and observable map;

10. $`\mathfrak P`$ records source provenance, fitted inputs, held-out data, conventions, and uncertainty.

</div>

No component is decorative. Removing $`\omega`$ loses the state-dependent two-point function. Removing $`\mathcal B_{\mathrm{BV}}`$ loses the physical gauge quotient. Removing $`\mathcal T^{\mathcal R}`$ leaves singular products undefined. Removing $`\mathfrak c`$ obscures whether the output is in–in or in–out. Removing $`\mathfrak P`$ makes a replay look like a prediction.

## The regime record

For scattering, $`\mathfrak c_{\mathrm{scatt}}`$ must include:

1.  asymptotically stationary or otherwise controlled in/out regions;

2.  a physical Hilbert-space or algebraic scattering construction;

3.  stable one-particle sectors and a mass gap or suitable replacement;

4.  external wave packets, normalization, and LSZ residues;

5.  an infrared prescription for massless fields;

6.  the observable and inclusive/exclusive definition.

Haag–Ruelle theory gives a rigorous route under its spectral and locality hypotheses . Those hypotheses are not automatic on a generic curved spacetime.

For an in–in calculation, $`\mathfrak c_{\mathrm{inin}}`$ instead records the initial state, time contour, switching functions, final-time observable, and any finite-time detector model.

## The parameter record

Write
``` math
\mathfrak p=(p_{\mathrm{src}},p_{\mathrm{fit}},
p_{\mathrm{obs}},p_{\mathrm{scheme}},p_{\mathrm{nuis}}).
```
The separation means:

1.  $`p_{\mathrm{src}}`$: values derived from a selected source without using the target observable;

2.  $`p_{\mathrm{fit}}`$: parameters fitted on declared training data;

3.  $`p_{\mathrm{obs}}`$: measured coordinates replayed as inputs;

4.  $`p_{\mathrm{scheme}}`$: scale and scheme coordinates;

5.  $`p_{\mathrm{nuis}}`$: experimental or theoretical nuisance parameters.

An honest result must declare which set each number belongs to.

# Formal perturbative construction

Given $`\mathfrak Q`$, pAQFT constructs interacting fields as formal power series using renormalized time-ordered products. In schematic notation,
``` math
\mathcal S_{\mathcal R}(V)
 =
 \sum_{n\geq0}\frac{i^n}{n!\hbar^n}
 \mathcal T_n^{\mathcal R}(V^{\otimes n}).
```
The relative $`S`$-matrix and Bogoliubov map then define interacting local observables. Causal perturbation theory and local covariance control the renormalization freedom .

This is a formal construction unless convergence or another completion is proved. It can be mathematically rigorous order by order while still not selecting a unique theory at fixed nonzero coupling.

## Graph expansion

The companion modal-diagrammatics paper proves the finite graded graph expansion and exact all-retained projection theorem . This paper does not duplicate those results. Here the graph datum is one component of $`\mathfrak Q`$. A physical coefficient additionally depends on state, gauge, renormalization, external states, and parameters.

# The coefficient-transport theorem

<div class="definition">

**Definition 2** (Typed amplitude intertwiner). Let $`\mathfrak Q`$ and $`\mathfrak Q'`$ be perturbative quantum records. A typed amplitude intertwiner is a family of maps
``` math
\Phi=(\Phi_Y,\Phi_{\mathcal A},\Phi_{\mathrm{test}},
\Phi_{\mathrm{BV}},\Phi_{\mathfrak p},\Phi_{\mathfrak c})
```
that preserves:

1.  localization, products, involution, and grading of the algebras;

2.  the state: $`\omega' \circ \Phi_{\mathcal A}=\omega`$;

3.  free operators and every declared contraction kernel;

4.  the interaction tensors or functionals;

5.  the BV/BRST differential, bracket, and declared Ward/QME identities;

6.  renormalized time-ordered products:
    ``` math
    \Phi_{\mathcal A}\mathcal T_n^{\mathcal R}
    =
    \mathcal T_n^{\mathcal R'}\Phi_{\mathcal A}^{\otimes n};
    ```

7.  parameter values and scheme/matching conventions;

8.  the chosen observable and, where applicable, external-state maps and residues.

</div>

<div id="thm:transport" class="theorem">

**Theorem 3** (Coefficient transport). *If $`\Phi:\mathfrak Q\to\mathfrak Q'`$ is a typed amplitude intertwiner, then every perturbative coefficient of every observable in the declared common domain agrees after transport. The equality includes graded signs, counterterm insertions, state contractions, and parameter factors.*

</div>

<div class="proof">

*Proof.* At order $`n`$, a coefficient is a finite sum of compositions of renormalized time-ordered products, interaction insertions, contractions, algebra products, state evaluation, and parameter coefficients. Each elementary operation commutes with its component of $`\Phi`$ by hypothesis. Their finite sums and compositions therefore commute with $`\Phi`$. State preservation identifies the resulting scalars. Induction over perturbative order proves the claim. ◻

</div>

<div id="cor:lsz" class="corollary">

**Corollary 4** (LSZ amplitude transport). *Assume, in addition, that both records satisfy the same declared Haag–Ruelle or LSZ hypotheses and that $`\Phi`$ intertwines the one-particle subspaces, external wave packets, pole masses, residues, and infrared prescription. Then the corresponding perturbative scattering amplitudes agree order by order.*

</div>

<div class="proof">

*Proof.* The LSZ map is obtained from time-ordered correlation functions by applying the external inverse free operators, Fourier/wave-packet maps, residues, and on-shell limits. Each operation is intertwined by assumption. Apply <a href="#thm:transport" data-reference-type="ref+label" data-reference="thm:transport">3</a>. ◻

</div>

<div id="cor:inin" class="corollary">

**Corollary 5** (In–in observable transport). *If instead $`\Phi`$ preserves the initial state, closed-time contour, switching data, and final observable, then the perturbative in–in coefficients agree order by order.*

</div>

<div class="proof">

*Proof.* The doubled contour expansion is again built from the preserved time-ordered and anti-time-ordered products, state contractions, interactions, and observable map. The proof of <a href="#thm:transport" data-reference-type="ref+label" data-reference="thm:transport">3</a> applies branch by branch. ◻

</div>

<div class="remark">

*Remark 6*. The theorem is a rigorous equivalence criterion, not a source theorem. It says what follows after every required datum is matched. It does not derive those data from modal geometry.

</div>

# Two exact nonselection results

## The action does not select the state or regime

<div id="prop:state-nonselection" class="proposition">

**Proposition 7** (State and regime nonselection). *A local action and its perturbative graph grammar do not uniquely determine a state, a Feynman two-point function, or an $`S`$-matrix regime.*

</div>

<div class="proof">

*Proof.* Even for a free field on Minkowski spacetime, the vacuum state and thermal KMS states are distinct states on the same field algebra and obey the same field equation. Their two-point functions differ, so state-dependent correlators differ. On a generic globally hyperbolic time-dependent spacetime, the local field algebra may exist while no preferred global vacuum or asymptotic time-translation generator exists. Hence a global in–out $`S`$-matrix is not selected by the local action. The same action and graph valences therefore admit different state/regime completions. ◻

</div>

## Replay is not prediction

<div id="thm:provenance" class="theorem">

**Theorem 8** (Parameter-provenance classification). *Let $`O=F(p)`$ be a calculated observable. If any coordinate of $`p`$ is chosen from the measured value of $`O`$, or from a data set containing the target without a declared holdout, agreement of $`F(p)`$ with $`O`$ is not a held-out prediction. If $`p`$ is supplied independently of the target, all fitting data are declared, and $`O`$ is evaluated on a disjoint holdout with an uncertainty budget, the result qualifies as a prediction at the stated model and uncertainty tier.*

</div>

<div class="proof">

*Proof.* In the first case the map from data to $`p`$ depends on the target, so the target is part of the construction input. The comparison tests consistency or replay, not out-of-sample consequence. In the second case the construction of $`p`$ is independent of the held-out $`O`$, so $`F(p)`$ is fixed before comparison. The remaining qualification is the declared uncertainty and model domain. ◻

</div>

<div class="corollary">

**Corollary 9** (Same-input Standard-Model equality). *If an MTT presentation and the Standard Model use the same renormalized action, state, scheme, matching conditions, external states, and measured parameter coordinates, <a href="#thm:transport" data-reference-type="ref+label" data-reference="thm:transport">3</a> can establish perturbative equivalence at those inputs. It does not establish a no-knob derivation of the shared coordinates.*

</div>

# Renormalization, running, and thresholds

## What local renormalization proves

Renormalized time-ordered products are constrained by locality, covariance, scaling, causal factorization, and field identities. The remaining finite freedoms are local counterterms. Choosing dimensional regularization and minimal subtraction is one concrete scheme, not a theorem that MTT uniquely selects that scheme. Likewise, a functional RG equation is a scale-dependent representation requiring a regulator and truncation .

## Scheme transport

Suppose $`p'=\sigma(p)`$ is a finite scheme change and field/observable maps are transformed consistently. Physical predictions can agree even though beta functions and intermediate coefficients differ. Therefore, “the same running” is meaningful only after specifying the coupling basis, loop order, matching surfaces, masses, thresholds, and scheme transport.

## Thresholds

Decoupling requires both a mass spectrum and a matching rule . A geometric overlap or eigenvalue may parameterize a mass or coupling, but it becomes a prediction only when its normalization and numerical value are sourced independently of the target data. Current profile results can validate the transport machinery while remaining profile inputs.

# Gauge symmetry, anomalies, and unitarity

The current MTT amplitude chain imports standard Faddeev–Popov/BRST/BV quantization rather than deriving it solely from coherence geometry . For a physical gauge amplitude one must establish:

1.  a gauge-fixed Green-hyperbolic complex;

2.  BRST cohomology or equivalent physical observable space;

3.  Ward or Slavnov–Taylor identities under renormalization;

4.  local and global anomaly cancellation for the selected representation content;

5.  positivity or a physical-state theorem on the quotient;

6.  infrared-safe observables where massless gauge fields occur.

Anomaly cancellation of a Standard-Model representation is an important consistency check. It does not show that MTT selected that representation or its couplings. Perturbative unitarity identities do not by themselves provide a nonperturbative $`C^*`$-completion at fixed coupling.

# Illustrative amplitude templates

## Tree-level exchange

Given a selected or supplied gauge coupling $`g`$, propagator prescription, external spinors, and kinematic regime, a tree exchange coefficient has the familiar form
``` math
\mathcal M_{\mathrm{tree}}
=
\bar u(p_3)\Gamma^\mu u(p_1)\,
G_{\mu\nu}(q)\,
\bar u(p_4)\Gamma^\nu u(p_2),
\qquad \Gamma^\mu\propto g.
```
The formula is a consequence of the specified record. Its numerical value is not predicted until $`g`$, masses, wave functions, and normalizations have independent provenance.

## Loop coefficient

At one loop, the coefficient additionally depends on the regularization, counterterms, subtraction scale, and matching convention. A successful same-input comparison verifies implementation and equivalence. A first-principles claim requires the source and uncertainty record as well.

## Curved-spacetime observable

When no scattering regime exists, a better output is a local expectation such as
``` math
\omega\!\left(\mathcal O_{\mathrm{int}}(f)\right)
```
or a finite-time detector response. Hadamard regularity and local covariant renormalization make such quantities meaningful without inventing asymptotic particles.

# Current MTT amplitude status

## Closed selected free source

The companion MTT-to-QFT paper owns the selected free q79 result . On the declared globally hyperbolic framed q79 representative, the twisted massless Dirac operator composes with standard Green-hyperbolic and CAR/AQFT theorems to give an even local net with locality, covariance, time-slice, and nonempty positive Hadamard state space. This is the quantum algebraic source used here; it is not re-proved.

## Formal interacting tier

Current work composes the selected carrier with a classical BV master action, a gauge-fixed Green-hyperbolic equicausal algebra, and a formal all-orders anomaly-free QME and physical-state functor at the declared formal tier. These results support conditional perturbative coefficients. They do not select a unique fixed-nonzero-coupling interacting $`C^*`$-theory.

## Embedded Standard-Model profile tier

The current A04 audit closes twelve obligations for embedded renormalized-Standard-Model equivalence at the adopted one-shared-physical-primitive/profile standard. This is a substantial representation and replay result. Standard gauge quantization is imported, and measured/profile coordinates remain construction inputs. The A05 strict-upgrade ledger keeps the stronger no-knob obligations open.

## Status table

<div class="center">

| Layer | Current status | Meaning for amplitudes |
|:---|:---|:---|
| Finite graded graph transfer | Exact companion result | Graph coefficients transfer when all typed data intertwine |
| Selected q79 free even-CAR net | Closed at declared tier | Free local quantum algebra and state space available |
| Perturbative BV/QME bridge | Formal/conditional | Order-by-order interacting algebra under declared hypotheses |
| Embedded renormalized-SM equivalence | Closed at profile tier | Same-input profile amplitudes can be replayed |
| Upper action and automorphism transfer | Open | No same-source derivation of all interactions |
| Fixed-coupling gauge–BRST $`C^*`$ bridge | Open | No selected nonperturbative interacting completion |
| No-knob SM values and precision packet | Open | No held-out full-precision phenomenology yet |

</div>

# What would make a first-principles prediction

A publishable prediction packet should contain:

1.  the selected source and action, with immutable hashes;

2.  all continuous and discrete inputs classified by provenance;

3.  a convention map to the target observable;

4.  full multi-loop RG, mass-scheme, and threshold transport;

5.  regulator and truncation controls;

6.  correlated theoretical and experimental covariance;

7.  a target declared held out before evaluation;

8.  independent replay by a verifier that does not import target values.

One to three genuinely selected physical primitives may still be a valuable theory. They must be declared as primitives rather than hidden inside normalizations, matching scales, or selected rows.

# Validation checklist

Before an MTT amplitude claim is promoted, verify:

1.  **Algebra:** locality, covariance, time-slice, and physical observable domain.

2.  **State:** positivity and Hadamard or other required regularity.

3.  **Interaction:** same-source action and all vertex normalizations.

4.  **Gauge:** BV/BRST identities, anomalies, and physical quotient.

5.  **Renormalization:** scheme, scale, loop order, and counterterm freedoms.

6.  **Regime:** LSZ/Haag–Ruelle or in–in hypotheses.

7.  **Parameters:** source, fit, observed, scheme, and nuisance classification.

8.  **Transport:** thresholds, masses, matching, and conventions.

9.  **Uncertainty:** truncation, numerical, model, and covariance budget.

10. **Prediction:** held-out target and independent verifier.

# Discussion

## What has genuinely been achieved

MTT is no longer limited to saying that quantum language resembles modal geometry. The selected q79 free-CAR source gives an actual local quantum net on its declared branch. The formal BV/QME chain shows that the interacting perturbative machinery can be composed consistently under explicit hypotheses. The Standard-Model profile program demonstrates that the finite carrier can encode and replay a broad accepted lower structure with unusually detailed provenance.

## What the earlier wording obscured

There is a large logical difference between:
``` math
\text{same inputs}\Longrightarrow\text{same amplitudes}
```
and
``` math
\text{selected geometry}\Longrightarrow
\text{independently predicted inputs and amplitudes}.
```
The first is an equivalence theorem. The second is a source and prediction theorem. Current MTT has strong parts of the first and selected free-field input, but not yet the complete second.

## Best next result

The shortest route forward is not another benchmark amplitude. It is a same-source packet joining:
``` math
\begin{gathered}
\text{selected upper action}\\
\downarrow\\
\text{physical gauge-fixed interacting record}\\
\downarrow\\
\text{RG, threshold, state, and observable transport}\\
\downarrow\\
\text{held-out comparison with uncertainty}.
\end{gathered}
```
<a href="#thm:transport" data-reference-type="ref+Label" data-reference="thm:transport">3</a> then turns the commuting record into coefficient equality without repeating diagram-by-diagram arguments.

# Conclusion

Quantum amplitudes are downstream objects. They require a local quantum algebra, state, interactions, gauge reduction, renormalized products, regime, external states, parameters, and provenance. We organized those requirements into a typed record and proved that a complete intertwiner preserves perturbative coefficients, LSZ amplitudes, or in–in observables on their declared domains.

The same framework proves the limits of current claims. An action and graph grammar do not select a state or scattering regime. Same-input agreement is equivalence, not held-out prediction. Current MTT therefore supports a rigorous selected free-field source, a conditional formal interacting pipeline, and profile-level Standard-Model equivalence. Full first-principles phenomenology awaits the selected upper action, fixed-coupling interacting completion, no-knob or explicitly primitive parameter source, precision transport, uncertainty budget, and held-out observable packet.

# Computational Evidence and Reproducibility

The amplitude transport and provenance theorems proved here are analytic statements. The curated repository <https://github.com/PeterNero/mtt-results-repro> supplies current MTT status context. The mapped is profile-replay evidence for embedded renormalized-Standard-Model equivalence. The mapped is an open stronger-upgrade ledger. Neither row proves the analytic theorems in this paper, and the open row is not evidence of closure. Exact artifacts, tier labels, and source hashes are retained in the repository.
