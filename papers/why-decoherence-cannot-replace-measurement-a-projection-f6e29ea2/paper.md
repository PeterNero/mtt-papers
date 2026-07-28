---
abstract: |
  Decoherence suppresses interference and stabilizes preferred records, but a nonselective decoherence channel does not contain an outcome label, a conditional state update, or a rule that one outcome is realized. We make this separation exact in finite-dimensional quantum theory and then state its consequence for Modal Triplet Theory (MTT). For a pointer resolution $`\{P_a\}`$, the dephasing channel $`\Delta_P(\rho)=\sum_aP_a\rho P_a`$ is completely positive and trace preserving, removes every off-diagonal pointer block, and preserves all pointer populations. We prove that the same nonselective channel is compatible with distinct outcome instruments having different probability laws. Hence the channel alone selects neither outcomes nor probabilities.

  An MTT basin boundary or chart exit has the same logical limitation: it marks the failure of a supplied effective chart, but it does not choose a successor basin. A completed measurement model must additionally provide an outcome-indexed completely positive instrument or a normalized selection-completion kernel, together with its source and domain. This yields a rigorous conditional bridge: decoherence may represent intra-basin suppression, whereas measurement requires inter-basin completion data. The current canonical q79 binary recorder supplies an exact stopped-output law on its declared finite domain, but general apparatus contexts and objective single-history actualization remain open. The paper therefore retains the decoherence-versus-selection distinction while withdrawing any inference of capture, Born probabilities, irreversibility, or objective outcomes from projection, noninjectivity, admissibility loss, or chart exit alone.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: c0118f95260a40cfd73ce6bc8c62a07c0f2aedc493329dab906568af9fdc7681
paper_id: why-decoherence-cannot-replace-measurement-a-projection-f6e29ea2
release_state: zenodo_released
released_version: v1.0
title: |
  **Why Decoherence Cannot Replace Measurement  
  Suppression, Selection, and the Missing Completion Map in Modal Triplet Theory**
zenodo_doi: 10.5281/zenodo.18261893
zenodo_record_id: 18261893
zenodo_url: "https://zenodo.org/records/18261893"
---

# Scope and Claim Tier

Environment-induced decoherence is a dynamical account of interference suppression and pointer stability . The definite-outcome problem asks for something else: why an individual run has a recorded outcome, what its conditional post-measurement state is, and what law governs the alternatives. Conflating these questions obscures both the success of decoherence and the data still required for measurement.

This revision separates four claim tiers.

1.  **Established measurement mathematics.** Channels describe nonselective dynamics; instruments describe outcome probabilities and conditional updates .

2.  **Exact result of this paper.** A dephasing channel does not determine an instrument, and loss of an effective chart does not determine a continuation kernel.

3.  **Conditional MTT bridge.** If a selected MTT descent emits basins, basin-preserving channels, and an inter-basin completion instrument, then decoherence and measurement can be represented as intra- and inter-basin operations.

4.  **Current selected finite-domain result.** The canonical q79 binary one-anchor recorder emits an operational stopped-output measure and second-moment capture descent on its declared domain . This is not yet a universal apparatus theorem or an objective single-history theorem.

No result below derives a Born source, physical time, entropy arrow, or objective actualization from projection alone. The analysis is finite-dimensional so that every map and norm is elementary. The distinction extends to normal instruments on operator algebras, but that extension is not needed here.

# Channels, Pointer Blocks, and Decoherence

Let $`\mathcal H`$ be a finite-dimensional Hilbert space and let
``` math
\mathsf D(\mathcal H)=\{\rho\geq0:\operatorname{Tr}\rho=1\}.
```
A finite pointer resolution is a family of mutually orthogonal projections $`P=\{P_a\}_{a\in A}`$ satisfying $`\sum_aP_a=I`$.

<div class="definition">

**Definition 1** (Nonselective dephasing channel). The $`P`$-dephasing channel is
``` math
\begin{equation}
 \Delta_P(\rho)=\sum_{a\in A}P_a\rho P_a.
 \label{eq:dephasing}
\end{equation}
```
Its pointer-coherence functional is
``` math
\begin{equation}
 C_P(\rho)^2
 =\sum_{\substack{a,b\in A\\a\neq b}}
   \lVert P_a\rho P_b\rVert_2^2,
 \label{eq:coherence}
\end{equation}
```
where $`\lVert X\rVert_2^2=\operatorname{Tr}(X^\dagger X)`$.

</div>

<div id="prop:dephasing" class="proposition">

**Proposition 2** (What dephasing does). *The map $`\Delta_P`$ is completely positive and trace preserving. For every $`\rho\in\mathsf D(\mathcal H)`$,
``` math
C_P(\Delta_P(\rho))=0,
 \qquad
 \operatorname{Tr}(P_a\Delta_P(\rho))=\operatorname{Tr}(P_a\rho)
```
for all $`a\in A`$.*

</div>

<div class="proof">

*Proof.* Equation <a href="#eq:dephasing" data-reference-type="eqref" data-reference="eq:dephasing">[eq:dephasing]</a> is a Kraus representation with Kraus operators $`P_a`$, and $`\sum_aP_a^\dagger P_a=I`$. Orthogonality gives $`P_a\Delta_P(\rho)P_b=0`$ for $`a\neq b`$, proving the first identity. Cyclicity of the trace and $`P_aP_b=\delta_{ab}P_a`$ give the second. ◻

</div>

More general decoherence dynamics may approach $`\Delta_P`$ only asymptotically, may include dissipation, and may have an approximate pointer resolution. None of those refinements changes the type of the object: discarding the environmental record produces a nonselective quantum channel. It produces a density operator, not a classical outcome label.

<div id="ex:qubit" class="example">

**Example 3** (Suppression without an outcome). For $`\mathcal H=\mathbb C^2`$, let $`P_0=\lvert0\rangle\langle0\rvert`$, $`P_1=\lvert1\rangle\langle1\rvert`$, and $`\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$. Then
``` math
\Delta_P(\lvert+\rangle\langle+\rvert)
 =\frac12P_0+\frac12P_1.
```
The off-diagonal blocks vanish, but the output is not either conditional state $`P_0`$ or $`P_1`$, and no recorded value $`0`$ or $`1`$ appears in the channel output.

</div>

# Measurement Requires an Instrument

An outcome-resolved measurement is not represented by its nonselective channel alone.

<div id="def:instrument" class="definition">

**Definition 4** (Quantum instrument). A finite quantum instrument is a family $`\{\mathcal I_a\}_{a\in A}`$ of completely positive, trace-nonincreasing maps such that
``` math
\mathcal I_{\mathrm{ns}}=\sum_{a\in A}\mathcal I_a
```
is trace preserving. For input $`\rho`$ it defines
``` math
\begin{equation}
 p(a\mid\rho)=\operatorname{Tr}\mathcal I_a(\rho),
 \qquad
 \rho_a=\frac{\mathcal I_a(\rho)}{p(a\mid\rho)}
 \quad\text{when }p(a\mid\rho)>0.
 \label{eq:instrument-law}
\end{equation}
```

</div>

The instrument contains three pieces absent from a nonselective channel: an outcome index, its probability, and its conditional update. If one also claims that exactly one ontic history is actualized, the operational instrument must be supplemented by a statement identifying what constitutes that realized event. The instrument predicts records; the existence of an objective single-history ontology is a further claim.

<div id="thm:underdetermination" class="theorem">

**Theorem 5** (A nonselective channel does not select an instrument). *The dephasing channel $`\Delta_P`$ does not determine outcome probabilities or conditional states. In particular, for the two-outcome qubit resolution of Example <a href="#ex:qubit" data-reference-type="ref" data-reference="ex:qubit">3</a>, the Lüders instrument
``` math
\mathcal I_0(\rho)=P_0\rho P_0,\qquad
 \mathcal I_1(\rho)=P_1\rho P_1
```
and, for every $`q\in[0,1]`$, the instrument
``` math
\mathcal J^{(q)}_0(\rho)=q\Delta_P(\rho),\qquad
 \mathcal J^{(q)}_1(\rho)=(1-q)\Delta_P(\rho)
```
have the same nonselective channel $`\Delta_P`$. On $`\lvert+\rangle\langle+\rvert`$ their outcome laws are respectively $`(1/2,1/2)`$ and $`(q,1-q)`$.*

</div>

<div class="proof">

*Proof.* Each displayed map is completely positive and trace nonincreasing. Both families sum to $`\Delta_P`$. Their probabilities follow from Equation <a href="#eq:instrument-law" data-reference-type="eqref" data-reference="eq:instrument-law">[eq:instrument-law]</a>. Choosing $`q\neq1/2`$ proves that the same nonselective channel is compatible with different outcome laws. Their conditional states also differ: the Lüders instrument gives $`P_a`$, whereas $`\mathcal J^{(q)}_a`$ gives the same dephased state for either nonzero outcome. ◻

</div>

<div id="cor:nonselection" class="corollary">

**Corollary 6** (Decoherence non-selection). *No outcome law, conditional update, or unique realized outcome can be inferred from a decoherence channel without additional outcome-resolved data.*

</div>

The artificial family $`\mathcal J^{(q)}`$ is not proposed as a physical detector. Its purpose is logical: the channel does not encode which instrument is physical. A source theorem must select the detector coupling, readout algebra, and instrument independently of the observed target probabilities.

# The Missing Selection-Completion Map

The basin language used in MTT can be made precise without turning chart failure into an outcome theorem. Let $`U\subseteq\mathsf D(\mathcal H)`$ be the domain of an effective chart and let $`\{\mathcal B_a\}_{a\in A}`$ be declared measurable successor regions.

<div id="def:kernel" class="definition">

**Definition 7** (Selection-completion kernel). For a boundary state $`\eta\in\partial U`$, a selection-completion kernel is a probability kernel
``` math
K_\partial(a,d\sigma\mid\eta)
```
on $`A\times\mathsf D(\mathcal H)`$ satisfying
``` math
\begin{align}
 &\sum_{a\in A}\int_{\mathsf D(\mathcal H)}
 K_\partial(a,d\sigma\mid\eta)=1,
 \label{eq:kernel-normalization}\\
 &K_\partial\bigl(a,\mathsf D(\mathcal H)\setminus\mathcal B_a\mid\eta\bigr)=0.
 \label{eq:kernel-support}
\end{align}
```
Its nonselective continuation is the barycenter
``` math
\begin{equation}
 T_K(\eta)=
 \sum_{a\in A}\int_{\mathsf D(\mathcal H)}
 \sigma\,K_\partial(a,d\sigma\mid\eta).
 \label{eq:barycenter}
\end{equation}
```

</div>

A deterministic continuation is the special case in which the kernel is a point mass. An affine completely positive realization is more strongly encoded by an instrument. Definition <a href="#def:kernel" data-reference-type="ref" data-reference="def:kernel">7</a> is deliberately minimal: it exposes exactly the data that the phrase “capture into a basin” must supply.

<div id="prop:chart" class="proposition">

**Proposition 8** (Chart exit is not completion). *The statement that a trajectory reaches $`\partial U`$ does not determine $`K_\partial`$. If two successor regions $`\mathcal B_0,\mathcal B_1`$ contain states $`\sigma_0,\sigma_1`$, then both
``` math
K^{(0)}_\partial(a,d\sigma\mid\eta)
 =\delta_{a0}\delta_{\sigma_0}(d\sigma)
```
and
``` math
K^{(1)}_\partial(a,d\sigma\mid\eta)
 =\delta_{a1}\delta_{\sigma_1}(d\sigma)
```
satisfy Equations <a href="#eq:kernel-normalization" data-reference-type="eqref" data-reference="eq:kernel-normalization">[eq:kernel-normalization]</a> and <a href="#eq:kernel-support" data-reference-type="eqref" data-reference="eq:kernel-support">[eq:kernel-support]</a>, while producing different outcomes and continuations.*

</div>

<div class="proof">

*Proof.* Both kernels are normalized point masses supported in their declared successor regions. Their outcome marginals and barycenters are different. Boundary membership supplies no condition that distinguishes them. ◻

</div>

Thus admissibility loss has a precise, limited meaning: the current effective chart no longer controls the continuation. It does not imply that projection “enforces” one particular capture. A selected action, detector coupling, boundary condition, instrument, or kernel must do that work.

# A Correct Conditional MTT Bridge

The useful core of the original paper can now be stated without overclaiming.

<div id="def:basin" class="definition">

**Definition 9** (Typed basin model). A typed basin model consists of:

1.  a state space and declared basin regions $`\mathcal B_a`$;

2.  within-basin channels $`\mathcal D_a`$ satisfying $`\mathcal D_a(\mathcal B_a)\subseteq\mathcal B_a`$ on their stated domains;

3.  a pointer or record algebra;

4.  a selection-completion instrument or kernel at every claimed inter-basin event; and

5.  a source certificate identifying how these objects descend from the same selected MTT data.

</div>

<div id="thm:bridge" class="theorem">

**Theorem 10** (Conditional suppression–selection bridge). *In a typed basin model, a channel $`\mathcal D_a`$ that suppresses off-diagonal pointer blocks while preserving $`\mathcal B_a`$ is an intra-basin operation. A completion kernel with support in $`\mathcal B_b`$, $`b\neq a`$, is an inter-basin operation. The former does not determine the latter.*

</div>

<div class="proof">

*Proof.* The first two statements are immediate from the declared domains and support conditions. The last follows from Theorem <a href="#thm:underdetermination" data-reference-type="ref" data-reference="thm:underdetermination">5</a> at channel level and Proposition <a href="#prop:chart" data-reference-type="ref" data-reference="prop:chart">8</a> at chart-boundary level. ◻

</div>

This theorem retains the intended distinction:
``` math
\boxed{
\begin{aligned}
\text{decoherence} &\longleftrightarrow
  \text{intra-basin suppression and record stabilization},\\
\text{measurement completion} &\longleftrightarrow
  \text{an outcome-indexed inter-basin instrument or kernel}.
\end{aligned}}
```
The arrow is a typed representation, not a proof that both sides have already been emitted by one universal MTT source.

# What Current MTT Results Supply

Several earlier formulations attributed too much to noninvertible projection. A noninjective map can identify microscopic states without selecting a time arrow, an entropy law, a probability measure, or a representative of each fiber. The corrected MTT shadow-bridge analysis states exact descent and restricted-recovery criteria and treats measurement instruments as selected updates, not inverse maps .

There is nevertheless a concrete positive result. On the canonical q79 binary one-anchor Fock recorder, the selected normal state on the commuting nondemolition output algebra induces a stopped output law, and second-moment capture descent is exact on the declared finite-symbol domain . No observed probability or fitted stochastic parameter is added on that domain.

That theorem closes an operational finite-domain row; it does not prove:

- the corresponding construction for every allowed apparatus context;

- finite-bandwidth and non-Markov corrections;

- a pre-quantum probability semantics, if one is demanded;

- objective actualization of one ontic history; or

- that every admissibility boundary carries the same completion law.

Those statements require their own same-source theorems.

# Relation to Standard Measurement Theory

## Decoherence and pointer stability

Standard decoherence theory derives suppression of interference in reduced states through system–environment entanglement and explains the dynamical selection and stability of preferred pointer structures . Proposition <a href="#prop:dephasing" data-reference-type="ref" data-reference="prop:dephasing">2</a> is the finite idealization of this nonselective effect. It agrees with, rather than replaces, the standard account.

## Instruments and trajectories

The Davies–Lewis instrument formalism associates classical outcome statistics and conditional quantum operations with a measurement . Quantum-trajectory descriptions add a monitored record and an unravelling of a nonselective master equation. Different unravellings can represent the same ensemble channel, so the master equation alone does not select a unique record process. MTT must therefore emit its physical readout and instrument, not merely reproduce a reduced channel.

## Redundant records

Environmental redundancy can explain why information in a pointer observable is robustly accessible. Redundancy is compatible with the distinction made here: it concerns the proliferation of record information, whereas Theorem <a href="#thm:underdetermination" data-reference-type="ref" data-reference="thm:underdetermination">5</a> concerns the missing outcome-resolved law when only the nonselective channel is supplied. No claim that Darwinism presupposes a particular MTT selection mechanism is needed.

## Collapse models

Objective-collapse models append nonlinear or stochastic state dynamics that does more than suppress ensemble coherences. Whether an MTT limit reproduces one such model is a separate source-and-error problem. Even an exact dephasing semigroup can possess a random-unitary unravelling and therefore does not by itself prove objective collapse .

# Consequences and Non-Consequences

## Born weights

If the Lüders instrument is supplied, then
``` math
p(a\mid\rho)=\operatorname{Tr}(P_a\rho)
```
follows immediately. This is an evaluation of a selected instrument, not a derivation of that instrument from decoherence. Basin sizes can represent arbitrary finite probability vectors, so matching target weights by basin volume is not predictive unless the measure and partition were independently selected .

## Irreversibility

Reduced decoherence may be effectively irreversible because environmental records are inaccessible, and an instrument may produce persistent records. Neither fact follows from noninjectivity alone. An arrow of time requires a declared state, boundary condition, semigroup, record algebra, or other asymmetric source.

## Undecidability

No algorithmic undecidability theorem follows from the existence of basin boundaries. Such a theorem requires a computably specified MTT decision problem and an explicit reduction from a known undecidable problem. The earlier claim that quantum probability arises because selection is undecidable is therefore withdrawn.

## Single outcomes

An operational instrument predicts the distribution and conditional state of records. It does not by itself settle whether one ontic history is fundamental, emergent, or interpretation-relative. Any stronger single-history claim must identify an actualization object and prove its relation to the instrument.

# Promotion Contract

A universal MTT measurement theorem must emit, from one selected source:

1.  the physical state and observable algebras;

2.  the pointer or record algebra and apparatus coupling;

3.  the nonselective channel with its approximation domain and errors;

4.  the outcome instrument or completion kernel;

5.  normalization, positivity, and coarse-graining consistency;

6.  the probability source without observed target weights as inputs;

7.  stable record formation;

8.  any claimed objective actualization rule; and

9.  transport to general apparatus contexts, including finite-bandwidth and non-Markov regimes.

The canonical q79 recorder supplies a nontrivial subset of this contract on one finite domain. The remaining rows should be attacked as source and transport theorems, not filled by interpreting chart exit as selection.

# Version Delta

Relative to version 1, this revision:

- retains the distinction between intra-basin suppression and inter-basin selection;

- defines decoherence as a nonselective channel and proves its exact suppression properties;

- adds an explicit quantum instrument and a selection-completion kernel;

- proves that one nonselective channel supports different instruments and probability laws;

- proves that chart exit does not select a successor basin or kernel;

- replaces asserted projection-enforced capture by a conditional typed basin theorem;

- records the exact finite-domain q79 recorder result at its current tier;

- withdraws Born, irreversibility, undecidability, and objective-outcome inferences from projection or admissibility loss alone; and

- adds a testable promotion contract for future universal measurement claims.

# Conclusion

Decoherence cannot replace measurement because the two objects have different mathematical types. A nonselective channel can erase off-diagonal pointer blocks and stabilize records while containing no outcome index. Measurement requires an instrument or completion kernel that supplies outcome probabilities and conditional updates. The same channel can be completed by different instruments, and the same chart exit can be continued by different kernels.

This does not invalidate the MTT basin picture. It makes the picture precise. Intra-basin suppression and inter-basin completion form a coherent conditional bridge once both are emitted from selected source data. MTT already has an exact operational completion on one canonical finite q79 recorder domain. Extending that result to general apparatus contexts, controlled memory effects, and any objective single-history claim is the remaining frontier.

<div class="thebibliography">

99

E. B. Davies and J. T. Lewis, *An operational approach to quantum probability*, Communications in Mathematical Physics **17**, 239–260 (1970). <https://doi.org/10.1007/BF01647093>

W. H. Zurek, *Decoherence, einselection, and the quantum origins of the classical*, Reviews of Modern Physics **75**, 715–775 (2003). <https://doi.org/10.1103/RevModPhys.75.715>

M. Schlosshauer, *Decoherence, the measurement problem, and interpretations of quantum mechanics*, Reviews of Modern Physics **76**, 1267–1305 (2005). <https://doi.org/10.1103/RevModPhys.76.1267>

P. Nero, *Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*, corrected version 3 manuscript (2026); latest released concept record: <https://doi.org/10.5281/zenodo.18256408>

P. Nero, *Gravitationally Induced Collapse as an Effective Limit of Modal Triplet Theory*, corrected version 3 manuscript (2026).

P. Nero, *Canonical q79 Fock Output Measure and Second-Moment Capture Descent Theorem*, MTT QM Source Proof repository (2026). <https://github.com/PeterNero/mtt-qm-source-proof>

P. Nero, *Modal Triplet Theory: Foundation*, Zenodo (2025). <https://doi.org/10.5281/zenodo.16949762>

</div>
