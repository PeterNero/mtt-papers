---
abstract: |
  Decoherence is widely regarded as sufficient to explain the emergence of classical behavior and, in many accounts, as eliminating the need for a distinct measurement postulate. In this work we show that this belief rests on a structural conflation. Within Modal Triplet Theory (MTT), decoherence and measurement arise as distinct shadows of a single projection-based mechanism. Decoherence corresponds to contractive, unitary dynamics within admissible basins of the reduced state space, while measurement corresponds to discrete, irreversible transitions between basins enforced by noninvertible projection and admissibility loss. Decoherence is therefore necessary for stability but insufficient for outcome selection. This distinction is derived using the same coherent-sector projector, spectral gap, and basin structure that underlie other shadow-bridge results in MTT. Alignment with decoherence theory, quantum Darwinism, continuous measurement, and objective-collapse models is shown to validate the framework while explaining their persistent limitations. The measurement problem is reframed as a structural issue of admissibility rather than an interpretational choice.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 9128b63a8527d106a5df6a6cdb84697dc22dc17ab6a84996fa1d56923bdb4402
paper_id: why-decoherence-cannot-replace-measurement-a-projection-f6e29ea2
release_state: zenodo_released
released_version: v1.0
title: |
  **Why Decoherence Cannot Replace Measurement  
  A Projection-Based Shadow Bridge in Modal Triplet Theory**
zenodo_doi: 10.5281/zenodo.18261893
zenodo_record_id: 18261893
zenodo_url: "https://zenodo.org/records/18261893"
---

# Introduction

The measurement problem in quantum mechanics has persisted despite decades of technical progress. Among the most influential developments is decoherence theory, which explains the suppression of interference and the stability of macroscopic records through entanglement with environmental degrees of freedom. It is now common to hear the claim that decoherence solves, or nearly solves, the measurement problem.

At the same time, persistent conceptual gaps remain. Decoherence does not explain why a single outcome is realized in any given experimental run, nor why outcome probabilities obey the Born rule. These gaps are often dismissed as interpretational or epistemic, but their persistence suggests a deeper structural issue.

In this paper we argue that the problem lies not in decoherence itself, but in the assumption that decoherence and measurement are competing mechanisms. Within Modal Triplet Theory, decoherence and measurement are complementary shadows of the same projection-based structure. Decoherence governs dynamics within admissible basins, while measurement corresponds to transitions between basins. Confusing these two roles leads to the widespread but incorrect belief that decoherence can replace measurement.

This paper applies the general MTT shadow-bridge validation template to quantum measurement. We explicitly identify the common higher-level structure (S1), show how it gives rise to two apparently independent four-dimensional phenomena (S2), derive a precise bridge relation between them (S3), and validate the result against mainstream quantum measurement theory (S4).

# Scope and Standing Assumptions

This work is not an interpretation of quantum mechanics, nor does it modify Schrödinger evolution. It assumes the empirical correctness of quantum theory and addresses the structural origin of outcome selection and classicality.

Throughout, we assume:

1.  a well-defined microscopic Hilbert space $`\mathcal{H}_{\mathrm{ext}}`$,

2.  existence of a coherent-sector projector $`\Pi_{\mathrm{coh}}`$ with finite spectral gap,

3.  locality and bounded-geometry conditions sufficient to define admissible reduced dynamics,

4.  no fundamental stochastic postulates or observer-dependent axioms.

All results are slab-local and concern effective dynamics after projection. No claims are made about microscopic determinism beyond what is already established in MTT.

# Coherent-Sector Projection in Modal Triplet Theory

We briefly recall the elements of Modal Triplet Theory required for the present analysis. Detailed derivations are given elsewhere in the MTT corpus; here we focus on the minimal structure needed to analyze decoherence and measurement.

## Extended and reduced state spaces

Let $`\mathcal{H}_{\mathrm{ext}}`$ denote the extended Hilbert space describing the full modal degrees of freedom of the theory. Physical observables accessible at low energy are supported on a reduced Hilbert space $`\mathcal{H}_4`$, obtained by projection onto the coherent sector followed by restriction to four-dimensional observables.

Effective states are trace-class operators
``` math
\rho \in \mathcal{T}_1(\mathcal{H}_4),
```
and effective dynamics acts on this space.

## The coherent-sector projector

Central to MTT is the coherent-sector projector
``` math
\Pi_{\mathrm{coh}} : \mathcal{H}_{\mathrm{ext}}\to \mathcal{H}_{\mathrm{coh}}\subset \mathcal{H}_{\mathrm{ext}},
```
defined as the joint spectral projector onto the lowest eigenspaces of the modal Laplace-type operators. The existence of a finite spectral gap $`\lambda_\ast > 0`$ separating coherent from noncoherent modes ensures that $`\Pi_{\mathrm{coh}}`$ is bounded and stable under admissible perturbations.

All effective dynamics considered in this work arises from restricting to $`\mathcal{H}_{\mathrm{coh}}`$ and projecting onto $`\mathcal{H}_4`$.

## Reduced evolution and noninvertibility

The reduced evolution is described by an evolve–project map of the form
``` math
\begin{equation}
\rho_{n+1} = \mathcal{P}\bigl( U \rho_n U^\dagger \bigr),
\end{equation}
```
where $`U`$ is a unitary operator generated by the coherent Hamiltonian and $`\mathcal{P}`$ denotes projection to the reduced description.

Crucially, $`\mathcal{P}`$ is noninvertible: distinct microscopic states may map to the same reduced state, and no admissible operation reconstructs the preimage. This noninvertibility is the ultimate source of irreversibility and selection in the theory.

<div class="remark">

*Remark 1*. The noninvertibility of $`\mathcal{P}`$ is not an approximation or a coarse-grain choice. It is enforced by the spectral gap and admissibility conditions and cannot be removed without destroying stability.

</div>

# Admissibility and Basin Structure

## Admissible reduced dynamics

Not all reduced trajectories are physically meaningful. Modal Triplet Theory introduces the notion of *admissibility* to characterize effective dynamics that remains stable and predictive.

<div class="definition">

**Definition 2** (Admissible trajectory). A reduced trajectory $`\{\rho_n\}`$ is admissible on a slab if it remains within the domain where:

1.  the coherent-sector projection remains bounded,

2.  the reduced description remains stable under perturbations of size $`\varepsilon`$,

3.  the effective dynamics is contractive toward stable configurations.

</div>

Admissibility is a physical condition, not a mathematical convenience. It expresses the requirement that effective descriptions remain predictive and robust.

## Admissible basins

The admissible reduced state space decomposes into dynamically stable regions.

<div class="definition">

**Definition 3** (Admissible basin). An admissible basin $`\mathcal{B}_\alpha \subset \mathcal{T}_1(\mathcal{H}_4)`$ is a connected region of the reduced state space such that:

1.  trajectories starting in $`\mathcal{B}_\alpha`$ remain in $`\mathcal{B}_\alpha`$ under admissible evolution,

2.  trajectories are contractive toward a stable core within $`\mathcal{B}_\alpha`$,

3.  $`\mathcal{B}_\alpha`$ is separated from other basins by a finite stability margin.

</div>

Each basin corresponds to a stable macroscopic configuration, such as a measurement outcome, pointer state, or classical record.

## Basin boundaries and loss of admissibility

Basin boundaries mark the limits of validity of a given effective description. When a trajectory approaches a basin boundary, contractivity fails and admissibility is lost.

At this point, noninvertible projection enforces capture into one of the neighboring admissible basins. This process is discrete and irreversible on the slab.

<div class="remark">

*Remark 4*. Basin boundaries are not dynamical singularities. They are points where the assumptions underlying a particular effective description cease to apply.

</div>

# Selection Events

## Definition and properties

<div class="definition">

**Definition 5** (Selection event). A *selection event* is an irreversible transition
``` math
\rho \in \mathcal{B}_\alpha \longrightarrow \rho' \in \mathcal{B}_\beta,\qquad \alpha \neq
\beta,
```
occurring when admissibility is lost at a basin boundary and projection enforces capture into a new basin.

</div>

Selection events have the following properties:

- they are discrete rather than continuous,

- they are irreversible on admissible slabs,

- they produce stable records,

- they reset the effective Hamiltonian governing subsequent evolution.

## Selection versus unitary evolution

Within a basin, evolution is governed by unitary Schrödinger dynamics combined with environmental coupling. Selection events lie outside the scope of any single Schrödinger equation and cannot be generated by unitary evolution alone.

This distinction underlies the shadow-bridge analysis developed in the following sections.

# Decoherence as a Four-Dimensional Shadow

After projection to four-dimensional effective descriptions, one of the most prominent phenomena to appear is decoherence. Decoherence is often treated as the mechanism by which quantum systems acquire classical behavior, and it is therefore essential to characterize precisely what decoherence does and does not represent in Modal Triplet Theory.

## Reduced density matrices and environmental coupling

Consider a system coupled to an environment, with total state evolving under a unitary operator $`U`$ acting on $`\mathcal{H}_{\mathrm{coh}}`$. The reduced state of the system is obtained by tracing over environmental degrees of freedom, yielding a reduced density matrix $`\rho \in \mathcal{T}_1(\mathcal{H}_4)`$.

Under generic environmental coupling, off-diagonal elements of $`\rho`$ in a preferred basis are dynamically suppressed. This suppression is rapid for macroscopic systems and leads to effective diagonalization of $`\rho`$ in the pointer basis.

## Decoherence as contractive dynamics

Within the MTT framework, this suppression corresponds to contractive dynamics within a fixed admissible basin. Environmental interactions damp fluctuations transverse to the basin core and drive trajectories toward stable fixed points without altering basin membership.

Decoherence therefore explains:

- the emergence of stable pointer states,

- the robustness of macroscopic records,

- the effective irreversibility of certain processes.

However, decoherence does not induce transitions between basins. The reduced trajectory remains within the same admissible basin throughout decoherent evolution.

<div class="remark">

*Remark 6*. Decoherence preserves the linear structure of the reduced dynamics and does not introduce noninvertibility at the level of the full coherent-sector evolution.

</div>

# Measurement as a Distinct Four-Dimensional Shadow

In contrast to decoherence, measurement introduces discrete, irreversible outcomes. In standard quantum mechanics, this is often represented by a collapse postulate or by interpretational supplements.

## Discrete outcomes and irreversibility

Empirically, measurement produces:

- a single realized outcome per run,

- stable, macroscopic records,

- irreversibility that cannot be undone by reversing unitary evolution.

These features cannot be derived from decoherence alone. They require a mechanism that changes basin membership and enforces a new admissible description.

## Measurement as basin transition

Within MTT, measurement corresponds to loss of admissibility at a basin boundary followed by irreversible capture into a new basin. This process is enforced by noninvertible projection and is independent of environmental decoherence rates.

Measurement is therefore a distinct four-dimensional shadow: it reflects the necessity of switching between admissible effective descriptions rather than continuing contractive dynamics within one.

## Historical separation and confusion

Because decoherence and measurement appear in four dimensions as unrelated phenomena—one continuous and dynamical, the other discrete and irreversible—they have historically been treated as separate problems. This separation has led to the belief that decoherence might replace measurement altogether.

The next section shows why this belief is structurally incorrect by deriving the precise bridge relation between decoherence and measurement.

# S3 — Decoherence and Measurement as Intra- and Inter-Basin Dynamics

We now derive the central structural result of this work. Decoherence and measurement are not alternative explanations of the same phenomenon. They are distinct dynamical processes operating at different levels of the same projection-based structure.

## Intra-basin dynamics and contractivity

Let $`\mathcal{B}_\alpha`$ be an admissible basin of the reduced state space $`\mathcal{T}_1(\mathcal{H}_4)`$. By definition, admissible dynamics within $`\mathcal{B}_\alpha`$ is contractive toward a stable core. This contractivity is generated by the combination of coherent-sector unitary evolution and environmental coupling.

Formally, for $`\rho \in \mathcal{B}_\alpha`$, the reduced evolution takes the form
``` math
\begin{equation}
\rho_{n+1} = \mathcal{D}_\alpha(\rho_n),
\end{equation}
```
where $`\mathcal{D}_\alpha`$ is a completely positive, trace-preserving map that contracts trajectories toward the basin core. The map $`\mathcal{D}_\alpha`$ preserves basin membership:
``` math
\begin{equation}
\rho_n \in \mathcal{B}_\alpha \;\Rightarrow\; \rho_{n+1} \in \mathcal{B}_\alpha.
\end{equation}
```

Decoherence corresponds precisely to this intra-basin contractive behavior. It suppresses coherences transverse to the basin core and stabilizes pointer states, but it does not alter which basin the system occupies.

## Why decoherence preserves basin membership

The preservation of basin membership under decoherence follows from two facts:

1.  Decoherence acts continuously and linearly on the reduced state.

2.  Admissible basins are separated by finite stability margins.

As long as the reduced trajectory remains admissible, decoherence cannot drive the system across a basin boundary. Any such transition would require violation of the stability conditions that define the basin itself.

This explains why decoherence-based models necessarily retain superpositions at the level of the total state, even when interference becomes unobservable in practice.

## Inter-basin transitions and loss of admissibility

Measurement corresponds to a fundamentally different process. When a reduced trajectory approaches a basin boundary closely enough that stability margins collapse, the assumptions underlying intra-basin contractivity fail. At this point, admissibility is lost.

Noninvertible projection then enforces capture into one of the neighboring admissible basins:
``` math
\begin{equation}
\rho \in \partial \mathcal{B}_\alpha \;\longrightarrow\; \rho' \in \mathcal{B}_\beta,
\qquad \beta \neq \alpha.
\end{equation}
```

This transition is discrete, irreversible on the slab, and record-forming. It cannot be generated by any continuous limit of intra-basin dynamics.

## Measurement as selection, not dynamics

Selection events differ categorically from decoherence:

- Decoherence is continuous; selection is discrete.

- Decoherence is reversible in principle; selection is irreversible.

- Decoherence stabilizes states; selection chooses outcomes.

Measurement is therefore not a dynamical refinement of decoherence, but a distinct process enforced by the structure of projection and admissibility.

## The precise shadow-bridge relation

We can now state the bridge relation explicitly:
``` math
\begin{equation}
\boxed{
\begin{aligned}
\text{Decoherence} &\equiv \text{contractive dynamics within an admissible basin}, \\
\text{Measurement} &\equiv \text{irreversible transition between admissible basins}.
\end{aligned}
}
\end{equation}
```

Both phenomena arise from the same coherent-sector projector and spectral gap, but they operate in different dynamical regimes. Decoherence is necessary for classical stability, while selection is necessary for outcome definiteness.

## Why decoherence cannot replace measurement

Because decoherence preserves basin membership, it cannot:

- select a unique outcome,

- normalize outcome probabilities,

- explain the discreteness of measurement results.

Any attempt to extract outcomes from decoherence alone must therefore introduce additional mechanisms—stochastic jumps, conditioning rules, branching interpretations, or collapse terms—that effectively reintroduce basin selection without recognizing its origin.

Modal Triplet Theory explains why such additions are unavoidable and why decoherence, by itself, can never resolve the measurement problem.

# S4 — Validation via Mainstream Measurement Theory

We now validate the decoherence–measurement bridge by examining how mainstream quantum measurement theory has independently reconstructed partial aspects of the basin structure without identifying its common origin. These approaches succeed where they implicitly capture intra-basin contraction and fail where they omit inter-basin selection.

## Quantum Darwinism: redundancy after selection

Quantum Darwinism explains the emergence of objective classical records through the redundant encoding of information about “pointer states” in multiple environmental fragments. Empirically, this accounts for the accessibility and robustness of classical information.

Within the basin framework, redundancy is a downstream consequence of selection. Once a selection event has occurred and the system is captured into a basin, environmental coupling contracts trajectories toward the same basin core and proliferates records associated with that basin.

Quantum Darwinism therefore presupposes outcome selection. It explains why information spreads *after* a basin is chosen, but it does not provide a mechanism for choosing that basin. This limitation is structural and cannot be removed without introducing inter-basin dynamics.

## Continuous measurement and quantum trajectories

Continuous measurement theory models observation as a stochastic process, leading to quantum trajectories governed by stochastic master equations. These formalisms introduce state-dependent noise, jumps, or conditioning rules to recover individual outcomes.

From the MTT perspective, such constructions are effective descriptions of piecewise dynamics:

- continuous evolution corresponds to intra-basin contraction,

- stochastic jumps correspond to inter-basin selection events.

The necessity of introducing jumps reflects the impossibility of describing selection within purely unitary evolution. Trajectory formalisms therefore approximate basin transitions without identifying their structural origin in projection and admissibility.

## Objective collapse models

Objective collapse models introduce explicit nonunitary terms or stochastic dynamics to enforce outcome selection. These models correctly identify the need for a mechanism beyond decoherence, but they treat collapse as a new physical postulate.

In Modal Triplet Theory, collapse-like behavior arises as a nongeneric effective limit of basin dynamics when stability margins are reduced, for example through gravitational amplification or strong environmental coupling. This explains why collapse models capture certain phenomenological features while remaining parameter-dependent and nonuniversal.

## Why decoherence-only explanations persist

Despite their limitations, decoherence-only explanations remain attractive because they successfully reproduce much of classical behavior. The basin framework clarifies why these explanations persist and why they fail.

Decoherence captures intra-basin contraction and stability, which dominate most observable phenomena. However, outcome selection occurs only at basin boundaries, which are rarely probed except during measurement. As a result, decoherence appears sufficient until the moment of selection is examined.

This explains the long-standing confusion in the measurement literature and predicts that any decoherence-only framework must be supplemented when outcome definiteness is required.

## Summary of validation

Mainstream measurement theory has already reconstructed key elements of the basin structure:

- decoherence models intra-basin contraction,

- Darwinism explains redundancy after selection,

- trajectory and collapse models approximate inter-basin transitions.

What is missing in each case is the unifying principle that distinguishes contraction from selection and explains why both must occur. Modal Triplet Theory supplies this principle by identifying decoherence and measurement as complementary shadows of projection and admissibility.

# Indivisible Stochasticity and Structural Undecidability

The basin-based distinction between decoherence and measurement integrates naturally with the theory of indivisible stochastic processes developed within Modal Triplet Theory. Together, these results clarify the ultimate limits of predictability in quantum mechanics.

## Indivisible stochastic processes

Previous work has shown that the reduced dynamics induced by coherent-sector projection can be described as an *indivisible stochastic process*. Such a process consists of deterministic evolution punctuated by discrete, irreversible selection events and does not admit a decomposition into independent infinitesimal increments.

Within the present framework, this structure acquires a clear interpretation. Decoherence corresponds to the deterministic, contractive component of the process operating within admissible basins. Measurement corresponds to the indivisible component: a noninvertible transition between basins that cannot be represented as the limit of continuous noise.

The stochastic description is therefore not fundamental but emergent. It is the correct effective language for a dynamics in which deterministic prediction of outcome selection is structurally impossible.

## Algorithmic undecidability of selection events

Recent results establish that selection-event occurrence in projection-based theories is not merely unpredictable in practice but algorithmically undecidable across admissible regimes. Even given complete physical information at finite precision, there exists no algorithm that decides whether a specified selection event will occur within the physically determined coherence budget.

This undecidability result explains why decoherence-based or unitary-only descriptions cannot be extended to global predictors. Decoherence controls intra-basin evolution but does not resolve the undecidable question of inter-basin selection. Any attempt to do so must introduce additional structure that effectively reintroduces basin logic.

## Probability without fundamental randomness

The combination of basin measures and undecidability clarifies the status of probability in quantum mechanics. Probabilities arise because outcome selection cannot be predicted algorithmically, not because nature samples from an irreducible random source.

The Born rule assigns invariant measures to basin capture that are stable under admissible perturbations and consistent with unitary evolution. These measures are not epistemic; they reflect the only predictive content available in a regime where individual outcomes are undecidable in principle.

This perspective dissolves the traditional tension between determinism and probability without invoking superdeterminism, hidden variables, or fundamental noise.

# Consequences for the Measurement Problem

The identification of decoherence and measurement as intra- and inter-basin processes reframes the measurement problem in structural terms.

## Collapse versus no-collapse revisited

Traditional debates frame the measurement problem as a choice between collapse and no-collapse interpretations. In the basin framework, this dichotomy is misleading. Selection events are neither ad hoc collapses nor subjective updates; they are structurally required transitions enforced by noninvertible projection and admissibility loss.

Decoherence does not eliminate the need for selection, and collapse models capture only special limits of basin dynamics. The correct question is not whether collapse occurs, but how inter-basin transitions are enforced in a theory that preserves locality, stability, and empirical adequacy.

## Single outcomes without many worlds

Many-worlds approaches preserve unitary evolution at the cost of proliferating outcomes. In the present framework, unitary evolution remains exact within basins, but selection events enforce single-outcome realization by eliminating all but one admissible basin.

This avoids both branching ontology and ad hoc outcome postulates. Outcome definiteness follows from admissibility rather than interpretational choice.

## Why Schrödinger evolution is exact but incomplete

The Schrödinger equation governs coherent evolution within admissible basins and is therefore exact where it applies. Its apparent failure during measurement reflects not a breakdown of quantum mechanics but a change of regime: the system reaches a basin boundary where the Schrödinger description ceases to be valid.

The incompleteness of Schrödinger evolution as a global predictor is thus a structural necessity, not a defect. Any attempt to extend it across basin boundaries must violate admissibility or introduce unphysical reversibility.

## Measurement as a physical, not epistemic, process

Because selection events are objective, irreversible, and record-forming, the measurement problem is not about observers or knowledge. It is about the physical conditions under which admissibility fails and projection enforces a new stable configuration.

This removes the observer from the foundations of quantum mechanics while preserving all empirical content.

# Conclusions

We have shown that decoherence and measurement are not competing explanations of quantum behavior but complementary shadows of a single projection-based structure. Decoherence corresponds to contractive dynamics within admissible basins, while measurement corresponds to irreversible transitions between basins enforced by noninvertible projection.

This identification explains why decoherence is indispensable yet insufficient, why collapse-like behavior must appear in effective descriptions, and why decades of attempts to eliminate measurement have repeatedly reintroduced selection mechanisms under new names. Modal Triplet Theory provides a unified account in which both phenomena arise naturally and necessarily.

The integration with indivisible stochastic processes and undecidability results further shows that the limits of quantum predictability are structural rather than provisional. Probability is not a placeholder for ignorance, but the correct effective description in a regime where individual outcomes cannot be decided algorithmically.

More broadly, this work demonstrates the power of the shadow-bridge methodology. By identifying distinct four-dimensional phenomena as projections of a single higher-level structure, Modal Triplet Theory explains why disparate research programs repeatedly converge on partial mechanisms without achieving closure. Decoherence, collapse, stochastic trajectories, and classicality are revealed as inseparable aspects of the same admissibility-based dynamics.

The results presented here suggest that the foundations of quantum mechanics are not incomplete, but that their completion requires recognizing the structural role of projection and admissibility in delimiting the scope of effective laws.

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
