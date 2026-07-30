---
abstract: |
  Coherence-selection dynamics can generate an effective causal set only when the event law prevents accumulation and is covariantly defined. This paper states two sufficient routes. In a deterministic hybrid model, a reset margin together with a uniform bound on trigger growth gives a positive dwell time and hence finitely many events on every bounded trajectory interval. In a stochastic model, finite compensator measure on every compact spacetime region implies almost-sure local finiteness. Once local finiteness is established, events inherit a partial order from a globally hyperbolic spacetime. Positive stability margins alone do not provide either result, and noninvertible projection alone does not define event times, reset states, outcome probabilities, or irreversibility. Lorentz-invariant statistics require a concrete covariant event law, such as a scalar intensity with respect to spacetime volume; they do not follow from coherence language. The current MTT corpus does not yet select the required trigger, reset, or hazard. The construction is therefore a rigorous conditional event encoding, not a derivation of fundamental spacetime discreteness or measurement outcomes.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: be3aa3bd85e86377e33655813325d1b7ad8b00db62e1289598a70944ed7ef187
paper_id: causal-sets-as-event-selection-shadows-of-coherence-bre-7bca8116
release_state: zenodo_released
released_version: v2
title: |
  Coherence-Selection Events and Causal Sets in Modal Triplet Theory:
  Non-Zeno Conditions, Reset Laws, and Covariant Statistics
zenodo_doi: 10.5281/zenodo.21665950
zenodo_record_id: 21665950
zenodo_url: "https://zenodo.org/records/21665950"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *Causal Sets as Event-Selection Shadows of Coherence Breakdown*.

The original paper inferred local finiteness from positive stability margins, left the transition/reset law undefined, and claimed approximately Lorentz-invariant statistics without a stochastic source.

Deterministic dwell-time and stochastic compensator criteria are proved, the event/reset data are typed explicitly, and covariance is made a property of the selected law.

Dynamically generated, locally finite events inherit the causal order of the effective spacetime and can be represented as a causal set.

MTT must select the trigger or hazard, reset law, spacetime density, and any outcome instrument from the same physical branch.

</div>

# Events need a law

An “event” is not created by naming a loss of coherence. A dynamical event model must specify:

- a state space and continuous evolution between events;

- an event trigger or stochastic hazard;

- the spacetime location assigned to an event;

- a reset or transition rule after the event;

- whether the event is an observed record, an objective state change, or only a coarse-graining marker.

These distinctions matter in MTT. A noninvertible lower description can discard information without selecting a unique physical outcome. Likewise, a stable fixed point can exist without any finite sequence of transition times.

# Deterministic hybrid route

Let $`z(t)`$ be a continuous state between event times
``` math
0<t_1<t_2<\cdots.
```
Let $`h(z)`$ be a scalar trigger. An event occurs when $`h`$ reaches zero from below, after which a reset map $`R`$ replaces $`z(t_n^-)`$ by $`z(t_n^+)=R(z(t_n^-))`$.

<div id="thm:dwell" class="theorem">

**Theorem 1** (Uniform dwell-time criterion). *Assume that after every event
``` math
h(z(t_n^+))\leq-\delta
```
for a fixed $`\delta>0`$, and that between events
``` math
\left|\frac{d}{dt}h(z(t))\right|\leq M
```
for a fixed finite $`M>0`$. Then
``` math
t_{n+1}-t_n\geq\frac{\delta}{M}.
```
Consequently a trajectory has at most
``` math
1+\frac{MT}{\delta}
```
events in any interval of duration $`T`$.*

</div>

<div class="proof">

*Proof.* After the reset, the trigger must increase by at least $`\delta`$ before it can reach zero. The derivative bound implies that this takes at least $`\delta/M`$. Summing the minimum separations gives the counting bound. ◻

</div>

This is the missing non-Zeno theorem. A positive stability margin for a fixed point does not imply either a reset margin or a bound on trigger growth.

<div class="example">

**Example 2** (Stability without a dwell-time theorem). The continuous system $`\dot x=-x`$ has a positive linear stability rate at the origin. If one separately declares events at $`t_n=1-2^{-n}`$, the events accumulate at $`t=1`$. The flow’s stability has not prevented the Zeno schedule because the event law was independent of the flow.

</div>

# Stochastic hazard route

Let $`N(K)`$ count events in a measurable spacetime region $`K`$. A point process may be specified through a compensator or intensity measure $`\Lambda`$.

<div id="thm:compensator" class="theorem">

**Theorem 3** (Finite-compensator local finiteness). *Suppose an event point process satisfies
``` math
\mathbb E[N(K)]=\Lambda(K)<\infty
```
for every compact $`K\subset Y_4`$. Then $`N(K)<\infty`$ almost surely for every member of a countable compact exhaustion. In particular, the event set is locally finite almost surely.*

</div>

<div class="proof">

*Proof.* A nonnegative extended-integer random variable that equals infinity with positive probability has infinite expectation. Therefore finite expectation implies $`N(K)<\infty`$ almost surely. Apply this to a countable compact exhaustion. ◻

</div>

A sufficient form is
``` math
\Lambda(K)=\int_K\lambda(x,z)\,d\operatorname{vol}_g(x),
```
with a nonnegative scalar predictable intensity $`\lambda`$ that is locally integrable. A uniform compact-region bound on $`\lambda`$ gives finite $`\Lambda(K)`$.

This theorem does not derive Poisson statistics. Correlated point processes, self-exciting processes, and state-dependent hazards can all satisfy local finiteness. Their physical predictions differ.

# From events to a causal set

Let $`C\subset Y_4`$ be the generated event set. On a globally hyperbolic spacetime define
``` math
x\preceq y
 \quad\Longleftrightarrow\quad
 y\in J^+(x).
```
The kinematic companion paper proves that any locally finite $`C`$ with this inherited order is a causal set. Thus either <a href="#thm:dwell" data-reference-type="ref+label" data-reference="thm:dwell">1</a>, with the required spatial population bound, or <a href="#thm:compensator" data-reference-type="ref+label" data-reference="thm:compensator">3</a> can provide the local-finiteness input.

For a deterministic family of trajectories, a compact spacetime region must intersect only finitely many relevant trajectories, or a separate uniform spatial density bound is needed. Dwell time along each of infinitely many worldlines would not by itself control the total number of events in the region.

# Reset, irreversibility, and records

A reset map can be invertible or noninvertible. If it is noninvertible, the effective hybrid dynamics loses information. That is a model of irreversibility at the chosen descriptive level, not automatically a fundamental arrow of time.

For quantum states, an outcome event requires an instrument $`\{\mathcal I_a\}`$, not only an effect or decoherence channel. The probability and conditional state are
``` math
p_a=\operatorname{tr}[\mathcal I_a(\rho)],
 \qquad
 \rho_a=\frac{\mathcal I_a(\rho)}{p_a}
```
when $`p_a>0`$. A nonselective channel $`\sum_a\mathcal I_a`$ does not say which event occurred. The current MTT Born-source result is closed only on a restricted selected recorder and remains open for arbitrary apparatus contexts and objective ontic selection.

Measurement has no privileged metaphysical role here. It is one physical process capable of producing records. The same event mathematics can describe switching, threshold crossings, detector clicks, or other transitions.

# Covariance and Lorentz statistics

Lorentz-invariant or generally covariant statistics are properties of the event law. In Minkowski spacetime, a constant scalar Poisson intensity
``` math
\Lambda(B)=\rho\int_Bd^4x
```
is invariant in law under proper orthochronous Poincare transformations. In curved spacetime, a scalar $`\lambda(x,z)`$ integrated against $`d\operatorname{vol}_g`$ is covariantly defined if the state variables and evolution are also geometrically specified.

By contrast, a reset at equal coordinate-time intervals or a hazard tied to a preferred foliation generally breaks Lorentz symmetry. An approximately isotropic numerical event cloud is not a proof of invariant law.

# Relation to MTT data

The local $`1+2+3`$ filtration, shared phase line, finite q79 Hessian, and fixed-point stability results do not currently emit:

- a four-dimensional scalar trigger $`h`$;

- a reset map $`R`$;

- a spacetime hazard $`\lambda`$;

- a covariant event-location rule;

- an event density in physical units.

These objects could be derived in a future same-source event model. For example, a response functional might define a scalar threshold, while a selected detector or basin map defines the reset. But the cross-sector intertwiner and unit map must be exhibited. An internal spectral gap alone does not supply a four-volume intensity.

# Status ledger

<div class="center">

| Statement | Status | Boundary |
|:---|:---|:---|
| Reset margin plus derivative bound gives dwell time | Exact | <a href="#thm:dwell" data-reference-type="ref+label" data-reference="thm:dwell">1</a>. |
| Finite compensator gives local finiteness | Exact | <a href="#thm:compensator" data-reference-type="ref+label" data-reference="thm:compensator">3</a>. |
| Local events inherit causal-set order | Exact, imported | Kinematic companion theorem. |
| Positive stability margin excludes Zeno events | False in general | Event/reset law is additional. |
| MTT selects trigger/reset law | Open | No same-source event generator. |
| MTT predicts Lorentz-invariant event statistics | Open | Requires a covariant stochastic or hybrid law. |
| Event channel selects objective outcome | Open | Instrument, probability, and ontology are separate. |

</div>

# Discussion

The corrected event route is sharper than the original proposal. It gives two concrete mathematical exits from the local-finiteness blocker and makes clear what a simulation would need to test. A hybrid simulation should log the reset margin and maximum trigger derivative. A stochastic simulation should estimate or certify compact-region compensators and test covariance of the full law, not only the appearance of one sample.

The shortest path to an MTT-specific result is to construct one physical event source on the already selected free q79 QFT net. A detector instrument, a covariant hazard derived from its response kernel, and a finite-compensator proof would produce a genuine event causal set without assuming Poisson sprinkling.

# Conclusion

Coherence-selection events can form a causal set, but only after non-accumulation and causal-order conditions are proved. Uniform reset margins and trigger bounds provide one route; finite stochastic compensators provide another.

MTT has not yet selected either event law. The present result is therefore a conditional mathematical framework. It replaces an unsupported local- finiteness claim with exact, testable criteria and preserves the distinction between effective irreversibility, observed records, and objective outcomes.

<div class="thebibliography">

99

L. Bombelli, J. Lee, D. Meyer, and R. D. Sorkin, “Space-time as a causal set,” *Physical Review Letters* **59** (1987), 521–524.

D. J. Daley and D. Vere-Jones, *An Introduction to the Theory of Point Processes, Volume I*, Springer, 2003.

R. Goebel, R. G. Sanfelice, and A. R. Teel, *Hybrid Dynamical Systems: Modeling, Stability, and Robustness*, Princeton University Press, 2012.

P. Nero, *Causal Sets as a Conditional Coarse-Graining of Modal Triplet Theory*, current revised MTT paper corpus, 2026.

P. Nero, *Measurement and Coherence Selection in Modal Triplet Theory*, current revised MTT paper corpus, 2026.

</div>
