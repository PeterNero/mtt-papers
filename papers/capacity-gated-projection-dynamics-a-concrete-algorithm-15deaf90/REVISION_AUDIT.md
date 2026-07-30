# Revision Audit: Capacity-Gated Projection Dynamics

Date: 2026-07-30

Paper id:
`capacity-gated-projection-dynamics-a-concrete-algorithm-15deaf90`

Selected revision:
Version 3

Superseded release:
Version 2.0, DOI `10.5281/zenodo.18283389`

## Revision purpose

Version 2 contained a useful particle-field construction but classified it
incorrectly. It defined a logarithmic barrier and inserted its negative
gradient in the force update while denying that the barrier was a force or
penalty. It used capacity-dependent speed and noise schedules without
classifying them as constitutive inputs. It also left the response at
`C=0` undefined while claiming forced selection, irreversibility,
nonfactorizable effective states, necessary behavioral signatures, and no
close mathematical analogues.

Version 3 preserves the concrete model but rewrites it as a typed hybrid
stochastic particle system. The flow domain, guard, rowwise barrier
feedback, reset map or Markov kernel, solution concept, numerical event
handling, and parameter provenance are explicit. Behavioral labels are
diagnostics to test rather than consequences to announce.

The revision is a standalone explanatory paper, not a list of corrections.

## Current authority lock

Kernel model at task start:
`001d8a78af47a60cf7406b5364e9180efeee7f52be2dbab3ca06ab8612b09272`

Repository starting head:
`c71e4128b7cd7b535cb6d1cb264e97d1207ec763`

Controlling authority:

- `A10`, recorded:
  `78be7385c3acfb484f31db7fad08a525bced4b86eb0df63c4622a772e730571e`.
  The master corrigendum classifies the implementation as a hybrid
  constrained stochastic dynamical system; identifies the logarithmic
  barrier gradient as a force or penalty; requires flow domains, guards,
  reset maps or kernels, and invariants; and limits the shared-field
  construction to classical collective correlation unless a quantum
  algebra is supplied.

There is no mapped numerical result for this paper. The revision changes
definitions, theorem hypotheses, algorithm status, and interpretation. It
does not promote a physical prediction.

## Canonical ownership lock

The MTT Foundation owns the admissibility ledger and the
stop/continue/reset alternatives:

- `papers/modal-triplet-theory-foundations/main.tex`
- released DOI: `10.5281/zenodo.21655367`

The normalized-margin paper owns signed slacks, scales, reserve vectors,
bottleneck capacity, metric clearance, and active rows:

- `papers/coherence-capacity-as-the-invariant-admissibility-margi-423433d4/main.tex`
- released DOI: `10.5281/zenodo.21709472`

The control-budget paper owns perturbation cost and cumulative consumption:

- `papers/coherence-capacity-as-the-fundamental-resource-of-effec-cd41c322/main.tex`
- released DOI: `10.5281/zenodo.21709596`

The capacity-dynamics paper owns the continuous rowwise budget, transport
classification, balance identities, and first-exit geometry:

- `papers/dynamics-of-coherence-capacity-transport-concentration-f2edc08a/main.tex`
- released DOI: `10.5281/zenodo.21709740`

Version 3 of this paper owns only the capacity-gated hybrid record, its
rowwise barrier specialization, explicit reset and executable contracts,
the no-selection result, the conditional hybrid well-posedness
specialization, the cross-dependence criterion, and the model-level
parameter ledger.

## Current version delta

Version 3 adds:

1. a typed state space with particles, velocities, and modes;
2. a declared relational summary map;
3. signed normalized reserve rows with no clipping;
4. separate exact and numerical guard boundaries;
5. a rowwise logarithmic barrier that remains smooth at active-row ties;
6. explicit drift, damping, mobility, diffusion, speed, and noise inputs;
7. stop, chart-transition, deterministic-reset, and stochastic-reset
   alternatives;
8. a reset-support certificate;
9. a conditional existence and uniqueness theorem up to jump
   accumulation;
10. an event-aware Euler--Maruyama specification;
11. a generator criterion for classical shared-field dependence;
12. a complete parameter and provenance ledger;
13. a closed-form two-particle circle example; and
14. a table turning qualitative behavioral claims into diagnostics.

## Claim-by-claim audit

### The algorithm is outside established dynamical classes

Version 2 claim:
The model is a distinct paradigm with no close analogue.

Decision:
Withdraw.

Reason:
The mathematical object is a hybrid constrained stochastic particle
system. Hybrid systems, viability theory, control barrier functions,
boundary-hitting resets, and mean-field particle systems are close
established neighbors.

Version 3 resolution:
Locate the model inside those literatures. Restrict the MTT-specific
contribution to provenance-aware use of a normalized multirow
admissibility gate and explicit separation of guard hitting from outcome
selection.

### The barrier is not a force or penalty

Version 2 claim:
`U=-log(epsilon+C)` and `-grad U` encode representational viability but do
not act as a force or penalty.

Decision:
Withdraw.

Reason:
The negative gradient appears in the acceleration update. It is therefore
a gradient feedback force in the reduced model regardless of its
interpretation.

Version 3 resolution:
State and prove the classification. Use a rowwise barrier
`-sum alpha_ia log r_ia`, which avoids differentiating a nonsmooth minimum
at row ties.

### Capacity alone determines dynamics

Version 2 claim:
As capacity falls, motion must slow, noise must decrease, and trajectories
must align with admissible gradients.

Decision:
Withdraw as a theorem; retain as a constitutive model family.

Reason:
The speed cap, noise schedule, mobility, and feedback gains are additional
inputs.

Version 3 resolution:
List those functions in the typed record and parameter ledger. State that
hesitation or alignment occurs only when the supplied schedules produce it.

### Capacity exhaustion forces a successor state

Version 2 claim:
At zero capacity the current state must be replaced by a new admissible
configuration.

Decision:
Replace by a four-way continuation contract.

Reason:
A guard supplies no successor. The model can stop, change chart, apply a
deterministic reset, or sample a Markov reset kernel.

Version 3 resolution:
Define all four options, prove that a guard does not uniquely select an
outcome, and require the reset law to return to a certified restart set.

### The algorithm is complete at `C=0`

Version 2 claim:
The displayed seven-step algorithm is complete and runnable.

Decision:
Withdraw.

Reason:
Its final step says "detect and respond" without defining the response.
The update can also cross the guard in one numerical step.

Version 3 resolution:
Supply a complete event-driven specification with stop/reset handling,
event bracketing, reset-support verification, random seed recording, and
signed-row history.

### The Gaussian-field update is strictly local

Version 2 claim:
The model uses strictly local real-time updates and no communication.

Decision:
Narrow.

Reason:
A Gaussian kernel has noncompact support and makes each field depend on
every particle. Local sampling of an already aggregated field is not the
same as finite-range microscopic interaction.

Version 3 resolution:
Distinguish compactly supported finite-range kernels from all-to-all
mean-field kernels. Keep "no look-ahead" only when the implemented
integrator is causal.

### Projection is automatically many-to-one

Version 2 claim:
The relational map is noninvertible by construction.

Decision:
Replace by a sufficient theorem and boundary.

Reason:
Noninjectivity depends on the source and quotient conventions.

Version 3 resolution:
Prove noninjectivity for labeled equal-weight particles under permutation,
and state that the proof disappears if indistinguishable particles have
already been quotiented by that symmetry.

### Collective dependence is entanglement-like

Version 2 claim:
A nonfactorizable joint effective state is formally analogous to quantum
entanglement.

Decision:
Withdraw the quantum analogy.

Reason:
The model supplies no Hilbert-space or operator-algebra composition, no
quantum state, and no separability criterion.

Version 3 resolution:
Prove a cross-coordinate generator criterion and call the result classical
collective dependence or mean-field coupling.

### Projection noninjectivity creates irreversibility

Version 2 claim:
Noninvertible projection is the source of irreversibility and selection.

Decision:
Withdraw.

Reason:
A noninjective map can possess a section on its range. Reversibility also
depends on the chosen state space, reset, retained records, and
coarse-graining.

Version 3 resolution:
Prove only that guard hitting does not decide reversibility. List the
additional structures needed for a path-measure or record-based theorem.

### Boundary layers are necessary and refinement invariant

Version 2 claim:
Boundary layers necessarily occur and persist under spatial, temporal, and
noise refinement.

Decision:
Reclassify as a diagnostic hypothesis.

Reason:
The barrier and gain can be removed, and no convergence study was
provided.

Version 3 resolution:
Define an operational boundary-layer diagnostic and require asymptotic
analysis or step-refined simulations against a matched baseline.

### Channeling, sprouting, hesitation, and abrupt basins are inevitable

Version 2 claim:
These signatures necessarily follow from projection plus finite capacity.

Decision:
Withdraw necessity.

Reason:
Each depends on reserve geometry, force, gate, noise, reset, initial law,
and parameters. Simple countermodels omit each behavior.

Version 3 resolution:
Publish a diagnostic table stating what must be measured and what evidence
would support each label.

### The model is minimal

Version 2 claim:
Every component is necessary and the algorithm is minimal.

Decision:
Withdraw.

Reason:
No equivalence class of models or minimality criterion was defined.
Several components can be removed while leaving a valid hybrid system.

Version 3 resolution:
Call the construction one transparent model record, not a minimal or unique
one.

### Prediction failure is structurally unavoidable

Version 2 claim:
There are configurations for which no continuation can be specified and
prediction necessarily fails.

Decision:
Withdraw.

Reason:
Once a reset kernel is supplied, the hybrid process has a continuation law
under standard hypotheses. Uncertainty, sensitivity, undecidability, and
nonexistence are distinct claims.

Version 3 resolution:
State the conditional well-posedness theorem and leave reachability,
stability, and computational complexity as separate questions.

## Local theorem ownership

Version 3 owns:

1. the capacity-gated hybrid record;
2. the model-relative permutation noninjectivity result;
3. the rowwise barrier construction;
4. the barrier-feedback classification;
5. the reset-support contract;
6. the no-selection proposition;
7. the no-automatic-irreversibility corollary;
8. the guarded hybrid existence specialization;
9. the shared-field cross-dependence criterion; and
10. the executable and provenance contracts.

The standard hybrid-system tuple, SDE existence theorem, Markov
piecing-out construction, viability theory, control barrier functions,
Euler--Maruyama convergence, mean-field theory, and quantum separability
retain their literature ownership.

## Expository review

The revision:

- starts from one operational question;
- separates inherited capacity data from constitutive dynamics;
- explains every field and row before using it;
- distinguishes exact failure from a numerical guard;
- proves why a rowwise barrier is preferable to differentiating a minimum;
- states plainly that the barrier is feedback;
- gives all four continuation choices;
- explains why a guard cannot select an outcome;
- states well-posedness with its exact hypotheses and non-results;
- distinguishes mean-field coupling from quantum entanglement;
- includes event-aware pseudocode;
- publishes the complete parameter ledger;
- works through a two-particle circle model;
- converts qualitative language into testable diagnostics;
- places the method beside its established mathematical analogues; and
- ends with a completion and falsifiability contract.

## Frontier delta

Before:
The released paper presented an incomplete hybrid update as a novel global
paradigm and treated several inserted feedback choices and unsupported
physical analogies as necessary consequences.

After:
The paper provides a complete conditional hybrid stochastic model, a
well-posed guard/reset semantics, an executable event contract, exact
classical coupling status, and a full provenance ledger. No physical or
quantum conclusion is promoted.

## Release verification

Published version:

- Zenodo record: `10.5281/zenodo.21709930`;
- Zenodo concept DOI: `10.5281/zenodo.18274654`;
- publication date: 2026-07-30;
- one uploaded file, `main.pdf`;
- 17 PDF pages;
- 15 explicit bibliography references;
- two related repository identifiers;
- zero mapped numerical-result references, because this paper introduces no
  numerical result packet; and
- plain-text Zenodo description and revision note, with no TeX markup and no
  correction notice mixed into the abstract.

Immutable local artifact hashes:

- `main.tex`:
  `8fd8910fc64488c5fe076290edc00632a3cefdddc3a08cf81b8e255b49017c79`;
- `main.bib`:
  `8f0ae03f14bfb3af06fc9585a014d9348d9f1cf2a18f9c1c04f27f7f71d95016`;
- `main.pdf`:
  `e10b8dfdbaa6c0124247ca2c021eb4eeb5059d87ea91afd89601f5d489ea20ce`;
  and
- canonical source tree:
  `725f69f068c5197dcfaa53fab2208c4938e7ba54f2105ea790cf4ec082884233`.

The full 17-page PDF was rendered and visually inspected. The title page,
definitions, theorem blocks, event-driven algorithm, parameter ledger,
worked example, diagnostic table, bibliography, page breaks, and final
reference page are legible and free of clipping or overlap.
