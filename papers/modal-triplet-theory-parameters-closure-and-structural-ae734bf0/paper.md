---
abstract: |
  A parameter count is meaningful only relative to a model, a physical tier, a choice of observables, a quotient by redundancies, and a rule separating construction data from held-out tests. This paper rebuilds the parameter and falsifiability account of Modal Triplet Theory (MTT) around that principle. We distinguish structural assumptions, selected discrete data, continuous construction primitives, measured source coordinates, nuisance and metrology inputs, derived outputs, and uncertainty data. We prove that raw symbol counts are not invariant under reparameterization or gauge redundancy, that replay of data used in construction is not a held-out prediction, that loss of a global right inverse is not by itself a falsifier, and that a scalar coherence-capacity diagnostic cannot eliminate the full source ledger. At the original profile-standard Standard Model execution, the auditable ledger contains one shared electroweak construction primitive and fifteen measured common-scheme source coordinates. The transported couplings, charged Yukawa rows, Higgs row, covariance workspace, and finite operators are outputs of that declared construction and are not counted again. This is a coherent embedding and reuse result, not a strict reduction of the Standard Model parameter set. The stronger no-knob program remains two of nine upgrades closed. A later effective ledger counts thirteen non-neutrino inputs, or nineteen with the adopted six-coordinate neutrino sector, excluding strong theta; this is a different accounting question from the original execution record. We also explain what the evolving constants program establishes about conditional scale selection and what source and unit anchors it does not select. We give valid falsification capsules for exact algebraic results, numerical certificates, source provenance, and held-out empirical predictions. The result is an honest parameter-identifiability framework: MTT has substantial structural economy, but strict numerical economy must be demonstrated rather than inferred from notation.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, September 2026
generated_from_main_tex_sha256: d510e6d0d28ad3d5b97a6245abf059c6386c129dbb60f7c1a3385600668eb768
paper_id: modal-triplet-theory-parameters-closure-and-structural-ae734bf0
release_state: current_revised_tex
released_version: v2
title: |
  **Parameters, Source Provenance, and Structural Falsifiability in Modal Triplet Theory**
  An Auditable Identifiability Ledger
zenodo_doi: 10.5281/zenodo.21713803
zenodo_record_id: 21713803
zenodo_url: "https://zenodo.org/records/21713803"
---

# Parameters, Source Provenance, and Structural Falsifiability in Modal Triplet Theory An Auditable Identifiability Ledger

Peter Nero. Version 3, September 2026

## Abstract

A parameter count is meaningful only relative to a model, a physical tier, a choice of observables, a quotient by redundancies, and a rule separating construction data from held-out tests. This paper rebuilds the parameter and falsifiability account of Modal Triplet Theory (MTT) around that principle. We distinguish structural assumptions, selected discrete data, continuous construction primitives, measured source coordinates, nuisance and metrology inputs, derived outputs, and uncertainty data. We prove that raw symbol counts are not invariant under reparameterization or gauge redundancy, that replay of data used in construction is not a held-out prediction, that loss of a global right inverse is not by itself a falsifier, and that a scalar coherence-capacity diagnostic cannot eliminate the full source ledger. At the original profile-standard Standard Model execution, the auditable ledger contains one shared electroweak construction primitive and fifteen measured common-scheme source coordinates. The transported couplings, charged Yukawa rows, Higgs row, covariance workspace, and finite operators are outputs of that declared construction and are not counted again. This is a coherent embedding and reuse result, not a strict reduction of the Standard Model parameter set. The stronger no-knob program remains two of nine upgrades closed. A later effective ledger counts thirteen non-neutrino inputs, or nineteen with the adopted six-coordinate neutrino sector, excluding strong theta; this is a different accounting question from the original execution record. We also explain what the evolving constants program establishes about conditional scale selection and what source and unit anchors it does not select. We give valid falsification capsules for exact algebraic results, numerical certificates, source provenance, and held-out empirical predictions. The result is an honest parameter-identifiability framework: MTT has substantial structural economy, but strict numerical economy must be demonstrated rather than inferred from notation.

# Version 3 revision note

**Supersedes.** Current Version 2; its released identity and revision history are retained.

**Reason.** The execution-input ledger needed the later effective and neutrino ledgers alongside it, and the constants-source chronology needed context rather than a single historical status label.

**Resolution.** We separate execution inputs from effective coordinates, explain conditional scale selection and data-use discipline, and distinguish continuous from measurable right inverses.

**Retained.** Finite SM and shared-primitive profile closure, the typed identifiability ledger, and the strict two-of-nine boundary are unchanged.

**Open boundary.** A selected zero-primitive physical source, absolute normalizations, and genuinely held-out values remain separate obligations.

# Version 2 revision note

**Supersedes.** Version 1, DOI <https://doi.org/10.5281/zenodo.18255574>.

**Reason.** Version 1 treated all apparent parameters as if they collapsed into one invariant margin, asserted that MTT had no freely tunable structural parameters, and listed the absence of a global measurable right inverse as a theory-level falsifier. It also described broad physical programs as already derived.

**Resolution.** Version 2 replaces those claims by a tier-relative source ledger. It counts independent inputs only after conventions and redundancies are declared, separates profile replay from held-out prediction, and assigns every falsifier to a named claim, domain, and evidence contract.

**Retained content.** The useful aim survives: a theory with shared source objects can be more constrained than a collection of sector-by-sector fits, and failures of cross-sector compatibility can be powerful tests.

**Open boundary.** MTT has not yet derived the full measured Standard Model profile from a selected zero-primitive source. The strict program remains open, and this paper does not convert profile inputs into predictions.

# Why parameter counting needs a ledger

Statements such as “the theory has one parameter” or “the theory has no knobs” sound precise, but they are incomplete. A count changes if one introduces redundant coordinates, changes basis, quotients a gauge orbit, replaces one vector by its components, or treats measured data as fixed background rather than as input. A serious count must therefore answer five questions:

1.  What mathematical model is being evaluated?

2.  Which physical or proof tier is being claimed?

3.  Which quantities enter before the outputs are computed?

4.  Which redundancies and conventions have been quotiented?

5.  Which data were withheld from construction and used only for testing?

This distinction is standard in identifiability theory \[[1](#ref-BellmanAstrom1970),[11](#ref-RaueEtAl2009)\]. Structural identifiability asks whether ideal observations distinguish parameter values in the declared model. Practical identifiability asks whether finite, noisy data constrain them well enough. Neither question can be answered from the number of symbols printed in a formula.

The same discipline is especially important in MTT. Projection, bundle selection, a finite operator, a normalized reserve vector, and an effective action can reuse common structure. That reuse is valuable. It does not imply that every scalar coefficient has been selected by the structure.

## Three different claims that are often confused

We will keep the following claims separate.

#### Representation economy.

Several sectors are represented by one carrier, one group action, or one operator architecture. This can be exact even when numerical coefficients remain external.

#### Construction economy.

Once a declared source profile is supplied, many rows are generated without additional sector-local fitting. This is stronger than representation economy, but the source profile remains an input.

#### Predictive economy.

A source fixed before target data are examined produces held-out observables with a declared uncertainty budget. This is the tier required for a strict parameter-reduction or no-knob claim.

Current MTT has exact examples of the first claim and a profile-standard closure of the second. The third remains incomplete \[[8](#ref-MTTSuperset2026),[9](#ref-MTTRoadmap2026)\].

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

**\\\mathcal S_T\\: structural assumptions** Hilbert spaces, bundles, domains, regularity, locality, positivity, hyperbolicity, action principles, and theorem hypotheses.

**\\\mathcal B_T\\: selected discrete data** Ranks, branch labels, finite groups, representations, projectors, incidence patterns, and other non-continuous choices.

**\\\mathcal A_T\\: construction primitives** Continuous quantities supplied by the construction before target observables are evaluated.

**\\\Profile_T\\: measured source profile** Empirical coordinates used to initialize, calibrate, or transport the model.

**\\\mathcal N_T\\: nuisance and metrology data** Scheme, scale, detector response, calibration, covariance policy, and external unit anchors.

**\\\Redundancy_T\\: redundancies and conventions** Gauge transformations, basis changes, field redefinitions, and equivalent coordinate descriptions.

**\\\Outputs_T\\: outputs** Rows obtained after the preceding entries are fixed.

**\\\mathcal U_T\\: uncertainty record** Covariance, truncation error, interval bounds, numerical tolerance, and model discrepancy.

**\\\Data_T\\: data-use map** For every datum, whether it is construction, validation, or held-out test data.

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

**Proposition 3** (Raw symbol counts are not invariant). *The number of named scalar symbols in a presentation is not an invariant parameter count. Under a local diffeomorphic reparameterization of the quotient $`\mathcal I_T/\mathcal G_T`$, the intrinsic dimension in [2.2](#def:count) is unchanged, while the printed symbol count may increase or decrease.*

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

**Proposition 7** (Replay is not held-out prediction). *Suppose a target datum $`y`$ is used to choose an input, branch, normalization, or acceptance rule, and the same $`y`$ is then reproduced by the forward map. That reproduction is a fit, calibration, or profile replay. It is not a held-out prediction in the sense of [3.2](#def:prediction).*

</div>

<div class="proof">

*Proof.* The data-use sets are not disjoint. The construction map depends on $`y`$, so the displayed agreement does not test the map on information absent from its construction. The conclusion follows directly from item 2 of [3.2](#def:prediction). ◻

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
and, when needed, a separately declared metric clearance \[[4](#ref-MTTCapacity2026)\]. Each row records a different admissibility obligation, with its own provenance, units, normalization, and tolerance.

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

# Execution inputs and the current effective ledger

## The original declared profile execution

Current MTT closes embedded renormalized-Standard-Model equivalence at a declared profile standard. The accepted calculation has twelve of twelve obligations closed, uses one shared electroweak construction primitive, and uses fifteen measured common-scheme source coordinates \[[8](#ref-MTTSuperset2026),[9](#ref-MTTRoadmap2026)\]. Standard SM quantization is imported on this branch rather than derived from abstract projection.

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

The original execution input/output ledger, not the later effective coordinate count. Counts are meaningful only at the declared profile tier.

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

<a id="sec:effective-ledger"></a>

## The effective and neutrino ledgers

The later minimal-parameter ledger asks which effective inputs remain after the accepted reductions, rather than which coordinates entered the original profile execution. Its non-neutrino count is
``` math
N_{\mathrm{eff,non\nu}}=1+9+1+1+1=13:
```
one gauge normalization anchor, nine charged-fermion coordinates, one CKM phase, one electroweak scale, and one shared $`P_{\mathrm{EW}}`$ primitive. Strong theta is excluded from this declared count. Adding the adopted six neutrino coordinates gives nineteen \[[6](#ref-FrozenEffectiveLedger)\]. Subtracting thirteen from the original sixteen would not measure three new predictions: the ledgers have different domains, conventions, and input/output roles.

The adopted U5 neutrino decision uses a selected holonomy shape and one absolute mass scale. Its effective coordinates remain three mixing angles, one Dirac phase, one holonomy-shape coordinate, and one mass scale. The non-self-conjugate holonomy branch retains its Dirac interpretation; the nil-minimal trace boundary is a declared assumption, not a proof that every neutrino realization has been selected \[[3](#ref-FrozenU5)\]. This is an adopted profile closure, not strict source emission of six measured quantities.

Likewise, the U9 branch-measure construction gives equal weights to the two members of its finite orbit and, after conditioning, unit weight to the retarded member. This is exact for that finite conditioning problem, not a measure on all physical histories. With the adopted U5 and U9 decisions, the upgrade ledger is four closed, four partial, and one blocked; at the strict source standard it remains two closed, six partial, and one blocked \[[10](#ref-FrozenU9)\]. Keeping both ledgers visible prevents adopted branch choices from being silently advertised as strict predictions.

## The strict tier

The stronger program asks for the source geometry and action to emit the electroweak primitive and measured gauge, Yukawa, mixing, Higgs, threshold, and precision values before those observables are used. The current strict upgrade ledger is two of nine closed. The zero-primitive electroweak source and true held-out Standard Model value packet remain open.

<div id="thm:current-ledger" class="theorem">

**Theorem 10** (Current-ledger statement). *At the original adopted profile execution standard, the declared one-plus-fifteen continuous source ledger is sufficient to execute the accepted embedded-SM forward map. Removing the measured profile leaves no current theorem that emits all of its coordinates from the selected MTT geometry and action. Therefore:*

1.  *profile-standard equivalence is closed at its stated tier;*

2.  *a strict no-knob derivation is not closed;*

3.  *outputs of the profile map are not additional independent inputs; and*

4.  *those outputs are not held-out predictions of the source coordinates.*

</div>

<div class="proof">

*Proof.* Items 1 and 2 are the current A04 and A05 ledger statuses. The construction uses one shared primitive and fifteen measured source coordinates. Once these are fixed, the accepted forward map emits its transported and finite rows, so they are outputs rather than additional inputs. By [3.3](#prop:replay), rows whose source values entered construction cannot be reclassified as held-out predictions. ◻

</div>

<a id="sec:constants-programs"></a>

# What the constants programs actually contribute

The short individual-constants policy fixes a useful provenance rule: measured values may test a construction downstream, but may not select its branch, source, kernel, or purported universal constant upstream. Shared global source parameters are not forbidden; undisclosed per-observable fits are. A calculation that uses an observed value to choose among sources must record that use in $`\mathcal D_{\mathrm{build}}`$, even when the final formula contains no fit symbol \[[5](#ref-FrozenIndividual)\].

The longer non-SM program is an evolving research record, not one theorem with one status. It distinguishes closed, conditional, structural, and open claims, and explicitly forbids interpreting a unit convention as a derived constant. In particular, internal choices such as $`\alpha=G_{10}=1`$ do not predict a measured electromagnetic coupling or Newton constant \[[7](#ref-FrozenNonSM)\]. Its later finite selected-character, gap, and operator first-variation results must not be discarded because an earlier paragraph describes their route as open. Conversely, those finite advances do not erase the source obligations left in later branches.

<a id="sec:scale-example"></a>

## A conditional scale-selection example

For declared positive coefficients $`A,B,p`$, consider
``` math
E(s)=A s^{-p}+B s^2,\qquad s>0.
```
It diverges at both ends, has $`E''(s)=p(p+1)A s^{-p-2}+2B>0`$, and therefore has the unique minimizer
``` math
s_\ast=\left(\frac{pA}{2B}\right)^{1/(p+2)}.
```
This is a genuine conditional scale-selection mechanism. It does not select the physical coefficients or the conversion from $`s`$ to an external unit. For the program’s $`p=4`$ branch, $`A=C_{\rm uv}^2`$ and $`B=\delta/(30\kappa)`$, so at $`\kappa=1`$, $`s_\ast=(60\rho)^{1/6}`$, where $`\rho=C_{\rm uv}^2/\delta`$. Here $`\delta>0`$ is the declared disturbance coefficient, not an unrelated signed threshold correction bearing a similar symbol \[[7](#ref-FrozenNonSM)\].

One later unit-selected-character branch records
``` math
\rho(R)=\left(\frac{64(2\pi)^2}{16R^4+8}\right)^2,
\qquad s_\ast(R)=(60\rho(R))^{1/6}.
```
The displayed dependence is informative: it exposes the radius/source obligation instead of hiding it inside a numerical constant. The source’s retarded-shift phase and character normalization specify a finite branch; they do not alone supply an absolute physical radius or metrology anchor.

<a id="sec:source-chronology"></a>

## Noise, tangent normalization, and chronology

A unit Brownian covariance specifies a mathematical noise convention. To claim a physical disturbance power after propagation requires the source covariance and the actual maps, schematically
``` math
\int_0^\infty P K Q_\tau K^\ast P^\ast\,\mathrm{d}\tau,
```
with convergence and domains declared. A Green–Kubo identification also requires a selected measure and autocovariance. Neither follows from naming the driving noise Brownian. Similarly, the program’s normalized $`\alpha_1`$ tangent, expressed as $`N(h)=1`$, fixes a tangent convention; it is not by itself a physical coupling coefficient \[[7](#ref-FrozenNonSM)\].

These distinctions preserve the later finite positive results while keeping their consumer contract explicit. A source-specific gap and first variation can justify a local operator or scale response once the source is fixed. They do not reopen established finite SM, Yukawa, or electroweak closure, nor do they close an absolute-normalization problem in a different sector. The right editorial unit is the scoped result with its assumptions, not the first or last status word in an evolving notebook.

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

After [3.2](#def:prediction) is satisfied, a residual outside the predeclared uncertainty and model-discrepancy budget falsifies the prediction capsule. Whether it also falsifies a larger theory depends on the claim’s stated ownership.

# Why absence of a right inverse is not a universal falsifier

Version 1 listed nonexistence of a global measurable right inverse across an admissibility collapse as an exact theory-level falsifier. That criterion is not valid in this form.

<div id="prop:no-section" class="proposition">

**Proposition 13** (No-section does not imply inconsistency). *The absence of a global right inverse or section of a projection does not, by itself, imply that the projection, its domain, or a physical model using it is inconsistent.*

</div>

<div class="proof">

*Proof.* The Hopf fibration $`S^3\to S^2`$ is a well-defined smooth principal $`U(1)`$-bundle with no global continuous section; a section would trivialize the bundle, contradicting its nonzero first Chern class \[[2](#ref-BottTu1982)\]. Thus a mathematically consistent and physically useful projection can lack a global section. ◻

</div>

The regularity category matters here. The Hopf example excludes continuous sections, not measurable ones: a Borel section can be assembled from local trivializations over a Borel partition of a finite trivializing cover. Thus the example cannot establish the nonexistence of a measurable decoder. Any no-section claim must name its continuity, measurability, or other regularity requirement before it can be tested.

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

2.  **Numerical statement.** The original accepted profile execution uses one shared construction primitive and fifteen measured source coordinates. The later effective ledger is thirteen non-neutrino inputs or nineteen with the adopted neutrino sector, excluding strong theta. These counts do not establish strict source emission of the measured profile.

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

The honest current picture is sharper than either “MTT has no parameters” or “MTT is merely another fit.” MTT has exact structural results and a profile-standard construction in which one architecture and one source ledger feed many sectors. That reuse is a real achievement. The present original execution nevertheless uses one shared continuous construction primitive and fifteen measured source coordinates, plus separately declared conventions, metrology, and uncertainty data. The later thirteen/nineteen effective ledger and the adopted/strict upgrade split refine this account without relabeling construction data as predictions. Conditional scale minimization is likewise kept separate from physical source and unit selection.

Falsifiability begins when a claim is made precise. Exact matrix and descent claims can fail exactly. Numerical certificates can fail under independent replay. Source claims can fail through hidden target dependence. Shared-source models can fail through cross-sector incompatibility. Held-out predictions can fail outside a predeclared uncertainty budget. The absence of a global right inverse, the existence of an open parameter, or a diagnostic capacity gradient is not by itself such a failure.

This ledger gives the research program a stable baseline. Future reductions can now be measured as actual movements of quantities from the input columns to the output columns, with no relabeling and no loss of provenance.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The current MTT status statements in this paper are imported from the curated results repository. They are not rederived here. The source is frozen to:

> **Repository:** <https://github.com/PeterNero/mtt-results-repro>
> **Commit:** `31247ebb 5c22f3fb b5443024 365433c6 ee0bff4a`
> **Manifest:**
> **Manifest SHA-256:**
> `fb399689 60b00584 631dbf53 1a708e18`
> `ef928d6b 6d935119 c185d7f6 32b1e7cd`
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

#### Profile rows used directly.

- : current non-looping status and source certificate map.

- : twelve-obligation profile-standard embedded-SM audit.

- : fifteen measured source coordinates and transport workspace.

- : eight output coordinates and positive-definite covariance.

- : charged Yukawa and Higgs profile rows.

#### Exact structural rows used directly.

- : exact source row at the declared one-shared-primitive standard.

- : native faithful gauge group and parameter-assumption audit.

- : final exact finite gauge-spectrum row and the common-normalized-spectrum no-go.

#### Open boundary.

- : current $`2/9`$ strict no-knob upgrade ledger. This row is not evidence of strict closure.

Tier labels and status are inherited from the manifest. No imported row promotes a profile value into a held-out prediction or changes theorem ownership.

# References

<a id="ref-BellmanAstrom1970"></a>

\[1\] Richard Bellman and Karl J. Astrom. On structural identifiability. *Mathematical Biosciences*, 7(3–4):329–339, 1970.

<a id="ref-BottTu1982"></a>

\[2\] Raoul Bott and Loring W. Tu. *Differential Forms in Algebraic Topology*. Springer, New York, 1982.

<a id="ref-FrozenU5"></a>

\[3\] Peter Nero. Adopted U5 neutrino-tier decision.

<https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/sm_neutral_u5_tier_decision/artifact.md>, 2026. Frozen source record; result sm_neutral_u5_tier_decision. Scope as stated in the text.

<a id="ref-MTTCapacity2026"></a>

\[4\] Peter Nero. Coherence capacity in modal triplet theory: Normalized margins, metric clearance, and the invariance class, 2026.

<a id="ref-FrozenIndividual"></a>

\[5\] Peter Nero. Individual constants: downstream validation and source policy.

<https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/individual_constants_program/artifact.md>, 2026. Frozen source record; result individual_constants_program. Scope as stated in the text.

<a id="ref-FrozenEffectiveLedger"></a>

\[6\] Peter Nero. Minimal effective parameter ledger.

<https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/sm_minimal_parameter_ledger/artifact.md>, 2026. Frozen source record; result sm_minimal_parameter_ledger. Scope as stated in the text.

<a id="ref-FrozenNonSM"></a>

\[7\] Peter Nero. Non-SM constants program and evolving source chronology.

<https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/nonsm_constants_program/artifact.md>, 2026. Frozen source record; result nonsm_constants_program. Scope as stated in the text.

<a id="ref-MTTSuperset2026"></a>

\[8\] Peter Nero. Superset determinations in modal triplet theory: Parameter identifiability after profile-standard standard-model closure, 2026.

<a id="ref-MTTRoadmap2026"></a>

\[9\] Peter Nero. A tiered roadmap for calculations in modal triplet theory: Audited closure and strict upgrades, 2026.

<a id="ref-FrozenU9"></a>

\[10\] Peter Nero. U9 finite-orbit conditional measure.

<https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/sm_branch_u9_conditional_measure/artifact.md>, 2026. Frozen source record; result sm_branch_u9_conditional_measure. Scope as stated in the text.

<a id="ref-RaueEtAl2009"></a>

\[11\] Andreas Raue, Clemens Kreutz, Thomas Maiwald, Julie Bachmann, Marcel Schilling, Ulrike Klingmuller, and Jens Timmer. Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. *Bioinformatics*, 25(15):1923–1929, 2009.
