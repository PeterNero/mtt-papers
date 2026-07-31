---
abstract: |
  A parameter count is meaningful only relative to a model, a physical tier, a choice of observables, a quotient by redundancies, and a rule separating construction data from held-out tests. This paper rebuilds the parameter and falsifiability account of Modal Triplet Theory (MTT) around that principle. We distinguish structural assumptions, selected discrete data, continuous construction primitives, measured source coordinates, nuisance and metrology inputs, derived outputs, and uncertainty data. We prove that raw symbol counts are not invariant under reparameterization or gauge redundancy, that replay of data used in construction is not a held-out prediction, that loss of a global right inverse is not by itself a falsifier, and that a scalar coherence-capacity diagnostic cannot eliminate the full source ledger. At the current profile-standard Standard Model tier, the auditable ledger contains one shared electroweak construction primitive and fifteen measured common-scheme source coordinates. The transported couplings, charged Yukawa rows, Higgs row, covariance workspace, and finite operators are outputs of that declared construction and are not counted again. This is a coherent embedding and reuse result, not a strict reduction of the Standard Model parameter set. The stronger no-knob program remains two of nine upgrades closed. We give valid falsification capsules for exact algebraic results, numerical certificates, source provenance, and held-out empirical predictions. The result is an honest parameter-identifiability framework: MTT has substantial structural economy, but strict numerical economy must be demonstrated rather than inferred from notation.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: f7fb7e7c3f6e7355614a06c8717e4d3cc9e554c20c5401cdbe192b8ccdb77d2e
paper_id: modal-triplet-theory-parameters-closure-and-structural-ae734bf0
release_state: zenodo_released
released_version: v2
title: |
  **Parameters, Source Provenance, and Structural Falsifiability in Modal Triplet Theory**
  An Auditable Identifiability Ledger
zenodo_doi: 10.5281/zenodo.21713803
zenodo_record_id: 21713803
zenodo_url: "https://zenodo.org/records/21713803"
---

# Version 2 revision note

<div class="description">

Version 1, DOI <https://doi.org/10.5281/zenodo.18255574>.

Version 1 treated all apparent parameters as if they collapsed into one invariant margin, asserted that MTT had no freely tunable structural parameters, and listed the absence of a global measurable right inverse as a theory-level falsifier. It also described broad physical programs as already derived.

Version 2 replaces those claims by a tier-relative source ledger. It counts independent inputs only after conventions and redundancies are declared, separates profile replay from held-out prediction, and assigns every falsifier to a named claim, domain, and evidence contract.

The useful aim survives: a theory with shared source objects can be more constrained than a collection of sector-by-sector fits, and failures of cross-sector compatibility can be powerful tests.

MTT has not yet derived the full measured Standard Model profile from a selected zero-primitive source. The strict program remains open, and this paper does not convert profile inputs into predictions.

</div>

# Why parameter counting needs a ledger

Statements such as “the theory has one parameter” or “the theory has no knobs” sound precise, but they are incomplete. A count changes if one introduces redundant coordinates, changes basis, quotients a gauge orbit, replaces one vector by its components, or treats measured data as fixed background rather than as input. A serious count must therefore answer five questions:

1.  What mathematical model is being evaluated?

2.  Which physical or proof tier is being claimed?

3.  Which quantities enter before the outputs are computed?

4.  Which redundancies and conventions have been quotiented?

5.  Which data were withheld from construction and used only for testing?

This distinction is standard in identifiability theory . Structural identifiability asks whether ideal observations distinguish parameter values in the declared model. Practical identifiability asks whether finite, noisy data constrain them well enough. Neither question can be answered from the number of symbols printed in a formula.

The same discipline is especially important in MTT. Projection, bundle selection, a finite operator, a normalized reserve vector, and an effective action can reuse common structure. That reuse is valuable. It does not imply that every scalar coefficient has been selected by the structure.

## Three different claims that are often confused

We will keep the following claims separate.

#### Representation economy.

Several sectors are represented by one carrier, one group action, or one operator architecture. This can be exact even when numerical coefficients remain external.

#### Construction economy.

Once a declared source profile is supplied, many rows are generated without additional sector-local fitting. This is stronger than representation economy, but the source profile remains an input.

#### Predictive economy.

A source fixed before target data are examined produces held-out observables with a declared uncertainty budget. This is the tier required for a strict parameter-reduction or no-knob claim.

Current MTT has exact examples of the first claim and a profile-standard closure of the second. The third remains incomplete .

# The typed source ledger

<div id="def:ledger" class="definition">

**Definition 1** (Realization and evidence ledger). For a claimed result at tier $`T`$, define
``` math
\mathfrak L_T=
\bigl(
\mathcal S_T,\mathcal B_T,\mathcal A_T,\mathcal P_T,\mathcal N_T,
\mathcal G_T,\mathcal O_T,\mathcal U_T,\mathcal D_T
\bigr).
```
The entries are:

<div class="description">

Hilbert spaces, bundles, domains, regularity, locality, positivity, hyperbolicity, action principles, and theorem hypotheses.

Ranks, branch labels, finite groups, representations, projectors, incidence patterns, and other non-continuous choices.

Continuous quantities supplied by the construction before target observables are evaluated.

Empirical coordinates used to initialize, calibrate, or transport the model.

Scheme, scale, detector response, calibration, covariance policy, and external unit anchors.

Gauge transformations, basis changes, field redefinitions, and equivalent coordinate descriptions.

Rows obtained after the preceding entries are fixed.

Covariance, truncation error, interval bounds, numerical tolerance, and model discrepancy.

For every datum, whether it is construction, validation, or held-out test data.

</div>

</div>

This ledger separates ontology from bookkeeping. A theorem hypothesis is not automatically a fitted parameter. A discrete branch choice contributes no continuous dimension but remains a selection obligation. A measured coordinate is an empirical input even when it appears only once. An output is not counted again merely because it is displayed in several bases.

<div id="def:count" class="definition">

**Definition 2** (Tier-relative continuous input count). Let $`\mathcal I_T=\mathcal A_T\times\mathcal P_T\times\mathcal N_T`$. When these spaces are smooth near the selected point and the declared redundancy group $`\mathcal G_T`$ acts regularly, define
``` math
N_{\mathrm{cont}}(T)
=
\dim\bigl(\mathcal I_T/\mathcal G_T\bigr).
```
The dimensions of construction primitives, measured profile coordinates, and nuisance data should also be reported separately. A single total is insufficient when those categories have different scientific meanings.

</div>

<div id="prop:symbol-count" class="proposition">

**Proposition 3** (Raw symbol counts are not invariant). *The number of named scalar symbols in a presentation is not an invariant parameter count. Under a local diffeomorphic reparameterization of the quotient $`\mathcal I_T/\mathcal G_T`$, the intrinsic dimension in <a href="#def:count" data-reference-type="ref+label" data-reference="def:count">2</a> is unchanged, while the printed symbol count may increase or decrease.*

</div>

<div class="proof">

*Proof.* Replace one coordinate $`a`$ by $`(u,v)`$ subject to $`v-u^2=0`$. The presentation now has two symbols, but the constrained set is still one-dimensional. Conversely, a vector with $`n`$ components may be denoted by one symbol without becoming one-dimensional. Local diffeomorphisms preserve dimension, and quotienting a regular redundancy removes orbit directions. Therefore only the quotient dimension, together with the category ledger, has invariant content. ◻

</div>

<div class="remark">

*Remark 4*. Singular points require a stratified or algebraic dimension statement rather than a naive Jacobian rank. This does not rescue a raw count; it makes the required declaration more precise.

</div>

# Identifiability, replay, and prediction

Let
``` math
F_T:\mathcal I_T/\mathcal G_T\longrightarrow \mathcal O_T
```
be the declared forward map. Parameter economy and predictive power are different properties of $`F_T`$.

<div class="definition">

**Definition 5** (Local identifiability). A selected input class $`[\theta_\ast]`$ is locally structurally identifiable from an observable set $`J`$ if there is a neighborhood $`U`$ such that
``` math
F_{T,J}([\theta])=F_{T,J}([\theta_\ast]),\qquad [\theta]\in U,
```
implies $`[\theta]=[\theta_\ast]`$.

</div>

Full-column Jacobian rank is a useful sufficient local test in a regular finite-dimensional setting, but it is not a global uniqueness theorem. Practical identifiability additionally depends on uncertainty and conditioning.

<div id="def:prediction" class="definition">

**Definition 6** (Prediction certificate). A held-out prediction certificate consists of:

1.  a source and branch selection rule fixed before the test data enter;

2.  disjoint construction and test sets $`\mathcal D_{\mathrm{build}}\cap\mathcal D_{\mathrm{test}}=\varnothing`$;

3.  a forward map with scheme, scale, units, and conventions;

4.  an uncertainty budget independent of the realized test residual; and

5.  an archived comparison rule fixed before evaluation.

</div>

<div id="prop:replay" class="proposition">

**Proposition 7** (Replay is not held-out prediction). *Suppose a target datum $`y`$ is used to choose an input, branch, normalization, or acceptance rule, and the same $`y`$ is then reproduced by the forward map. That reproduction is a fit, calibration, or profile replay. It is not a held-out prediction in the sense of <a href="#def:prediction" data-reference-type="ref+label" data-reference="def:prediction">6</a>.*

</div>

<div class="proof">

*Proof.* The data-use sets are not disjoint. The construction map depends on $`y`$, so the displayed agreement does not test the map on information absent from its construction. The conclusion follows directly from item 2 of <a href="#def:prediction" data-reference-type="ref+label" data-reference="def:prediction">6</a>. ◻

</div>

<div class="example">

**Example 8**. If fifteen measured common-scheme coordinates are transported to eight rows and their covariance, the eight rows are genuine outputs of the transport. They are not independent predictions of the fifteen inputs. The calculation can still be exact, reproducible, and useful: it proves consistency and scheme transport at the declared profile tier.

</div>

# What coherence capacity does and does not count

The corrected coherence-capacity formalism begins with a sourced, dimensionless reserve vector
``` math
r(x)=\bigl(r_1(x),\ldots,r_m(x)\bigr),
\qquad
C(x)=\min_i r_i(x),
```
and, when needed, a separately declared metric clearance . Each row records a different admissibility obligation, with its own provenance, units, normalization, and tolerance.

<div id="prop:min-not-injective" class="proposition">

**Proposition 9** (Bottleneck compression is not source reconstruction). *For $`m\geq2`$, the map
``` math
(r_1,\ldots,r_m)\longmapsto \min_i r_i
```
is not injective. Therefore the scalar bottleneck capacity cannot, without additional structure, reconstruct the reserve vector or eliminate the parameters on which its rows depend.*

</div>

<div class="proof">

*Proof.* For every $`a>1`$, the vectors $`(1,a)`$ have the same minimum $`1`$. Thus infinitely many distinct reserve vectors share one bottleneck value. ◻

</div>

This simple fact corrects a central overstatement of Version 1. Many conditions may be summarized by their weakest reserve, but the summary does not identify their sources. Nor does $`-\nabla C`$ become a force, $`C`$ become a conserved charge, or a reparameterization $`f(C)`$ become physically equivalent merely because it preserves the zero set.

# The current MTT parameter ledger

## Declared profile-standard closure

Current MTT closes embedded renormalized-Standard-Model equivalence at a declared profile standard. The accepted calculation has twelve of twelve obligations closed, uses one shared electroweak construction primitive, and uses fifteen measured common-scheme source coordinates . Standard SM quantization is imported on this branch rather than derived from abstract projection.

<div id="tab:current-ledger">

| Ledger class | Count | Current status at the profile tier |
|:---|:---|:---|
| Structural assumptions | not a scalar count | Selected branch, finite carrier, action and QFT conventions, regularity, scheme, and theorem domains must be declared. |
| Selected discrete data | finite, tier-dependent | Ranks, finite branch data, representation and projector choices. They add zero continuous dimension but require provenance. |
| Construction primitives | $`1`$ | One shared physical electroweak primitive $`P_{\mathrm{EW}}`$ at the adopted standard. |
| Measured source profile | $`15`$ | Common-scheme SM source coordinates with a declared covariance policy. |
| Nuisance/metrology | reported separately | Scale, scheme, unit anchors, likelihood or covariance choice, numerical tolerances, and any external calibration. |
| Derived outputs | not recounted | Transported couplings, nine charged Yukawa rows, the Higgs row, finite operator entries, threshold rows, and covariance workspace after the source is fixed. |
| Held-out observables | claim-specific | Only observables excluded from construction can support predictive-economy claims. |

The current input/output ledger. Counts are meaningful only at the declared profile tier.

</div>

Consequently, the transparent continuous construction ledger at this tier is
``` math
N_{\mathrm{build}}^{\mathrm{profile}}=1+15=16
```
before separately counted nuisance and metrology quantities. This equation does not claim that the number 16 is directly comparable with every published Standard Model parameter count. Such comparisons depend on the reference scale, renormalization scheme, flavor basis, neutrino assumptions, and which experimental inputs are treated as fixed. It says exactly what enters this MTT execution.

## What has nevertheless been reduced

The ledger does record real structural achievements.

- Native selected bundle automorphisms give the faithful $`(SU(3)\times SU(2)\times U(1))/\mathbb Z_6`$ group without adding continuous gauge-group knobs.

- The selected finite carrier, anomaly table, one-Higgs projector, and finite gauge/ghost spectrum rows are exact at their declared tiers.

- The same profile supports gauge, flavor, Higgs, threshold, and finite operator constructions without separately fitting each displayed output row.

- The fifteen-to-eight precision transport has a positive-definite covariance workspace and explicit cross-covariance entries.

These are compatibility, reuse, and representation-economy results. They constrain how inputs can be assembled. They do not yet replace the measured profile by a selected physical source.

## The strict tier

The stronger program asks for the source geometry and action to emit the electroweak primitive and measured gauge, Yukawa, mixing, Higgs, threshold, and precision values before those observables are used. The current strict upgrade ledger is two of nine closed. The zero-primitive electroweak source and true held-out Standard Model value packet remain open.

<div id="thm:current-ledger" class="theorem">

**Theorem 10** (Current-ledger statement). *At the adopted profile standard, the declared one-plus-fifteen continuous source ledger is sufficient to execute the accepted embedded-SM forward map. Removing the measured profile leaves no current theorem that emits all of its coordinates from the selected MTT geometry and action. Therefore:*

1.  *profile-standard equivalence is closed at its stated tier;*

2.  *a strict no-knob derivation is not closed;*

3.  *outputs of the profile map are not additional independent inputs; and*

4.  *those outputs are not held-out predictions of the source coordinates.*

</div>

<div class="proof">

*Proof.* Items 1 and 2 are the current A04 and A05 ledger statuses. The construction uses one shared primitive and fifteen measured source coordinates. Once these are fixed, the accepted forward map emits its transported and finite rows, so they are outputs rather than additional inputs. By <a href="#prop:replay" data-reference-type="ref+label" data-reference="prop:replay">7</a>, rows whose source values entered construction cannot be reclassified as held-out predictions. ◻

</div>

# What can legitimately falsify a claim

Falsification must be typed as carefully as the parameter count. A failed theorem hypothesis, a failed numerical certificate, a failed physical model, and a failed universal theory claim are not interchangeable.

<div id="def:falsifier" class="definition">

**Definition 11** (Falsification capsule). A falsification capsule for a claim $`K`$ contains:
``` math
\mathfrak F(K)=
(K,\Omega,H,S,V,E,\mathcal R),
```
where $`\Omega`$ is the domain, $`H`$ the hypotheses, $`S`$ the selected source, $`V`$ the verifier, $`E`$ the admissible error or uncertainty budget, and $`\mathcal R`$ the rule assigning a failure to the theorem, implementation, realization, or broader theory.

</div>

<div id="prop:scope-rule" class="proposition">

**Proposition 12** (Scope rule for certificate falsification). *Let a claim state that verified hypotheses $`H`$ imply a conclusion $`K`$ within error $`E`$. If $`H`$ and the source identity are independently verified but $`V`$ rejects $`K`$ beyond $`E`$, then that certified claim fails. If $`H`$ is not established for the tested system, the test shows non-applicability, not falsification of the conditional theorem.*

</div>

<div class="proof">

*Proof.* The first statement is modus tollens applied to the certified implication. The second follows because a conditional statement makes no assertion outside its hypotheses. ◻

</div>

## Valid falsifier classes

#### Algebraic and descent falsifiers.

An asserted representation, cocycle, anomaly cancellation, global-group quotient, or commuting diagram can be checked exactly. Failure falsifies that specific construction.

#### Analytic and numerical certificate falsifiers.

A claimed spectral gap, coercivity margin, contraction inequality, interval enclosure, tail bound, or convergence estimate can be replayed. A rejected certificate falsifies the claimed numerical theorem at its declared inputs.

#### Source-provenance falsifiers.

If a row advertised as source-selected actually depends on target data, unreported calibration, a changed branch, or an untracked convention, its source theorem fails even if the numerical value happens to agree.

#### Cross-sector consistency falsifiers.

When one source is genuinely fixed independently and several sectors are computed from it, incompatible outputs can falsify the shared-source realization. This is stronger than noticing that two separate fits disagree.

#### Held-out empirical falsifiers.

After <a href="#def:prediction" data-reference-type="ref+label" data-reference="def:prediction">6</a> is satisfied, a residual outside the predeclared uncertainty and model-discrepancy budget falsifies the prediction capsule. Whether it also falsifies a larger theory depends on the claim’s stated ownership.

# Why absence of a right inverse is not a universal falsifier

Version 1 listed nonexistence of a global measurable right inverse across an admissibility collapse as an exact theory-level falsifier. That criterion is not valid in this form.

<div id="prop:no-section" class="proposition">

**Proposition 13** (No-section does not imply inconsistency). *The absence of a global right inverse or section of a projection does not, by itself, imply that the projection, its domain, or a physical model using it is inconsistent.*

</div>

<div class="proof">

*Proof.* The Hopf fibration $`S^3\to S^2`$ is a well-defined smooth principal $`U(1)`$-bundle with no global continuous section; a section would trivialize the bundle, contradicting its nonzero first Chern class . Thus a mathematically consistent and physically useful projection can lack a global section. ◻

</div>

The correct falsifier is conditional. If an MTT claim requires a section, decoder, or inverse on a named domain, then a proof that no such object exists falsifies that claim. If the model instead represents intentional information loss, local trivializations, a quotient, or a restricted recovery channel, the absence of a global inverse may be expected.

The same point applies to measurement, horizons, and projection-induced irreversibility. Noninvertibility alone does not derive a physical arrow of time, an outcome law, or a horizon. Those require a selected dynamics, state, observable algebra, and operational domain.

# A current falsification matrix

<div id="tab:falsifiers">

| Claim | Required source and domain | Valid failure test | Invalid overreach |
|:---|:---|:---|:---|
| Claim | Required source and domain | Valid failure test | Invalid overreach |
| Profile-standard embedded SM equivalence | Frozen one-plus-fifteen ledger, branch, SMDR version, conventions, and covariance policy | Independent replay fails one of the twelve declared obligations or the transport/covariance checks | Calling a moving experimental central value a theorem target |
| Native finite gauge structure | Selected finite carrier, automorphism action, center quotient, and anomaly table | Exact matrix, representation, center, or anomaly calculation fails | Inferring measured relative gauge couplings from normalized finite spectra |
| Finite HYM or operator certificate | Exact source hashes, discretization, norm, tail estimate, and tolerance | Independent interval or a posteriori verifier rejects the claimed bound | Treating one certified representative as global branch uniqueness |
| Coherence-capacity certificate | Complete reserve rows, scales, provenance, metric, and region | A declared margin is nonpositive where uniform positivity was claimed | Treating an arbitrary gradient of capacity as a force law |
| Strict no-knob Standard Model values | Source fixed before observed values, same-branch action, forward map, and held-out data split | Predicted held-out packet lies outside its predeclared uncertainty budget | Counting successful profile replay as this strict test |
| QM, QFT, gravity, or cosmology bridge | Target-specific state, algebra, dynamics, observables, source map, and error contract | One required map or physical axiom fails on the claimed domain | Falsifying all of MTT because an interpretive analogy is incomplete |

Claim-level falsification contracts.

</div>

# Comparison with Standard Model and effective-theory practice

The Standard Model is usually parameterized at a chosen scale and scheme, with basis conventions and assumptions about neutrino masses. A numerical comparison between MTT and the Standard Model is therefore meaningful only after both ledgers use the same convention.

At present, MTT should make two separate statements.

1.  **Structural statement.** One selected finite architecture supports a faithful gauge group, chiral carrier, anomaly cancellation, finite operator organization, one-Higgs projection, and exact finite gauge/ghost spectra at their declared tiers.

2.  **Numerical statement.** The accepted profile-standard execution uses one shared construction primitive and fifteen measured source coordinates. No strict global reduction of the measured Standard Model profile is presently proved.

This is not a negligible result. Structural sharing can expose consistency conditions, remove duplicated fit slots, and provide a clear route toward prediction. But credibility increases when the profile coordinates remain visible in the ledger. Hiding them behind an operator or calling them “geometry” would not reduce their empirical role.

# Minimum standard for future parameter claims

Every future claim of a derived constant, reduced parameter count, or falsifiable prediction should publish the following record.

1.  **Tier and claim owner.** Exact, numerical-certified, profile, conditional, support, or open.

2.  **Source identity.** Repository commit, artifact hash, branch, and selected geometric or operator object.

3.  **Input ledger.** Structural assumptions, discrete choices, continuous primitives, measured coordinates, nuisance quantities, and unit anchors.

4.  **Quotient and convention map.** Gauge, basis, scheme, scale, and field redefinitions.

5.  **Forward map.** The executable map from inputs to outputs.

6.  **Data-use certificate.** Construction, validation, and held-out sets.

7.  **Uncertainty budget.** Experimental covariance, truncation, numerical, matching, and model-discrepancy errors.

8.  **Independent verifier.** A replay path that does not trust only the producer’s success flag.

9.  **Failure ownership.** What a failed test would reject and what it would leave untouched.

This standard prevents two opposite mistakes. It prevents an exact structural theorem from being dismissed merely because a physical normalization is still open. It also prevents a successful profile replay from being promoted into a source theorem.

# What remains to be proved

The strongest parameter-economy program now has a short, explicit agenda.

1.  Derive $`P_{\mathrm{EW}}`$ from the selected source geometry and action without an equivalent continuous physical primitive.

2.  Emit the measured gauge, charged-Yukawa, mixing, Higgs, and threshold source values from the same branch before those values enter construction.

3.  Complete the nonperturbative QFT and renormalization/matching bridge needed to compare physical observables with a controlled uncertainty budget.

4.  Produce genuinely held-out predictions and archive the data-separation certificate.

5.  Compare the final MTT and Standard Model ledgers in one common scheme, including discrete assumptions and nuisance data rather than only continuous headline counts.

These tasks are represented by the open strict-upgrade ledger and the zero-primitive and true-precision blockers. Until they close, “no-knob MTT” is a research target, not a result.

# Version 2 changes and reasons

| Version 1 statement | Version 2 decision | Reason |
|:---|:---|:---|
| MTT already derives QM, QFT, spacetime, irreversibility, and cosmology | Withdraw as a global status statement | Current bridges have different exact, profile, conditional, and open tiers. |
| All apparent parameters collapse to one invariant margin | Withdraw and replace by the typed ledger | The minimum of a reserve vector is noninjective and does not reconstruct its sources. |
| No freely tunable structural parameters | Replace by a tier-relative count | The current profile execution declares one construction primitive and fifteen measured source coordinates. |
| Persistence of an open degree of freedom falsifies MTT | Narrow to failure of a declared source theorem or held-out prediction | An open research obligation is not a failed theorem. |
| Absence of a global right inverse is a structural falsifier | Withdraw as universal criterion | Consistent nontrivial bundles and quotient maps may have no global section. |
| Many falsifiers follow automatically from few parameters | Replace by falsification capsules | Every test needs a domain, source, assumptions, verifier, error budget, and failure owner. |

Current-version delta.

# Conclusion

The honest current picture is sharper than either “MTT has no parameters” or “MTT is merely another fit.” MTT has exact structural results and a profile-standard construction in which one architecture and one source ledger feed many sectors. That reuse is a real achievement. The present execution nevertheless uses one shared continuous construction primitive and fifteen measured source coordinates, plus separately declared conventions, metrology, and uncertainty data.

Falsifiability begins when a claim is made precise. Exact matrix and descent claims can fail exactly. Numerical certificates can fail under independent replay. Source claims can fail through hidden target dependence. Shared-source models can fail through cross-sector incompatibility. Held-out predictions can fail outside a predeclared uncertainty budget. The absence of a global right inverse, the existence of an open parameter, or a diagnostic capacity gradient is not by itself such a failure.

This ledger gives the research program a stable baseline. Future reductions can now be measured as actual movements of quantities from the input columns to the output columns, with no relabeling and no loss of provenance.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The current MTT status statements in this paper are imported from the curated results repository. They are not rederived here. The source is frozen to:

- **Repository:** <https://github.com/PeterNero/mtt-results-repro>
- **Commit:** `31247ebb5c22f3fbb5443024365433c6ee0bff4a`
- **Manifest:** `release/result_manifest.json`
- **Manifest SHA-256:** `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`

## Profile rows used directly

- `A01/current_global_lock` (**PROFILE_REPLAY**): current non-looping status and source-certificate map. Result SHA-256: `f1a4c656fed97eb9d185c30a852404b3e0e029952c142dc7db6d72b85cdd4883`.
- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): twelve-obligation profile-standard embedded-SM audit. Result SHA-256: `d783988a4d10f10abfa4f5fa2769219cbea3fae238e3894d405c404fc3f546e9`.
- `A02/precision_15_source_transport` (**PROFILE_REPLAY**): fifteen measured source coordinates and transport workspace. Result SHA-256: `55df4532ae2bb6dd5995ed5e7e0d16308d5e0647fbfa99bd82e767be0859da59`.
- `A02/precision_8x8_workspace` (**PROFILE_REPLAY**): eight output coordinates and positive-definite covariance. Result SHA-256: `c5af11222a282343ab6009038a4fd61bcaec6406e88c537c8bc64ebdd9267ecf`.
- `A01/charged_yukawa_higgs_profile` (**PROFILE_REPLAY**): charged Yukawa and Higgs profile rows. Result SHA-256: `9648804f5b9f0867ccfa55b3b1bc9cc11332576d41e573b5900c4caafca90ad9`.

## Exact structural rows used directly

- `A01/strict_pew_row` (**DERIVED_EXACT**): exact source row at the declared one-shared-primitive standard. Result SHA-256: `203f294f770c724295f89307b6cebea8f813c5abd15add73d3772492ea04c787`.
- `A47/native_gauge_group` (**DERIVED_EXACT**): native faithful gauge group and parameter-assumption audit. Result SHA-256: `eeb8c7bb501d151a53ba2df109654e34ea4735560338c86e978107c9b5678582`.
- `A62/su3_finite_gauge_spectrum` (**DERIVED_EXACT**): final exact finite gauge-spectrum row and the common-normalized-spectrum no-go. Result SHA-256: `b106f81bee0af46148a99ac55422524bcac0f1a3b2f01689bf01a0747f96f2e0`.

## Open boundary

- `A05/strict_upgrade_ledger` (**OPEN**): current `2/9` strict no-knob upgrade ledger. This row is not evidence of strict closure. Result SHA-256: `659afd20a06fcc6492cfb77688dae81d109dfd16b368d877e1ea4d92da5e97ac`.

Tier labels and status are inherited from the manifest. No imported row promotes a profile value into a held-out prediction or changes theorem ownership.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
