---
abstract: |
  Across the Modal Triplet Theory (MTT) corpus, effective physical descriptions are shown to exist only within restricted admissible domains controlled by spectral gaps, projector regularity, and truncation stability. Outside these domains, effective evolution becomes irreversible despite invertibility of the underlying dynamics.

  In this paper we extract and formalize the invariant structure underlying these results. We show that all MTT admissibility conditions define a single finite stability margin, which we term *coherence capacity*. Coherence capacity is not an additional dynamical field, but a scalar measure of how much projection-based effective description can be supported before controlled truncation fails.

  We prove, in MTT-native language, that exhaustion of coherence capacity implies the nonexistence of a global measurable section of the coherent projection, yielding effective irreversibility as a structural necessity. This formulation does not modify existing MTT constructions; it compresses them, making explicit which aspects of MTT are contingent and which are unavoidable in any projection-based theory with finite control margins.
author:
- Peter Nero
current_version: v3
date: January 2026
generated_from_main_tex_sha256: 7af26b805cf9d8eeef642d19a2a017de6def912b1dee55e99e36c431268a4ffe
paper_id: coherence-capacity-as-the-invariant-admissibility-margi-423433d4
release_state: zenodo_released
released_version: v3.0
title: Coherence Capacity as the Invariant Admissibility Margin of Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.18322057
zenodo_record_id: 18322057
zenodo_url: "https://zenodo.org/records/18322057"
---

# Motivation and Relation to the MTT Corpus

Modal Triplet Theory derives quantum mechanics, quantum field theory, spacetime geometry, and classical physics from a common structural architecture: invertible fundamental dynamics combined with noninjective projection to observables and controlled truncation.

These results are obtained through multiple technical frameworks, including:

- admissible slabs and coherent sectors,

- joint Riesz projectors and spectral gaps,

- fixed points of projected evolution,

- controlled renormalization flow endpoints.

While technically distinct, these constructions all rely on the same fact: *effective physics is possible only while a finite stability margin remains available*. The present paper isolates this margin and makes it explicit.

#### Scope.

This paper establishes inevitability results internal to MTT. It introduces no new microscopic dynamics and does not alter any existing derivations. All statements are conditional on assumptions already present, explicitly or implicitly, in the MTT corpus.

# MTT Structural Setup

We adopt the standard MTT framework.

## Fundamental dynamics

Let $`(X,\mathcal{B})`$ be a standard measurable space equipped with an invertible evolution $`\Phi_\tau : X \to X`$, where $`\tau`$ is an ordering parameter rather than fundamental time.

## Coherent projection

MTT defines a projection onto an effective coherent sector via a bounded operator
``` math
\Pi_{\mathrm{coh}} : \mathcal{H} \to \mathcal{H}_{\mathrm{coh}},
```
constructed using joint Riesz projectors associated with a uniform spectral gap.

Observable states are equivalence classes under this projection.

## Effective evolution

The effective (shadow) evolution is given by
``` math
T := \Pi_{\mathrm{coh}} \circ \Phi_\tau .
```

All effective laws are statements about the iterates of $`T`$ on the coherent sector.

# Controlled Truncation and Admissibility

We summarize the admissibility conditions appearing in Fixed Points I–VI and Universality and Controlled Truncation.

<div class="assumption">

**Assumption 1** (Controlled Truncation). There exists a domain $`\mathcal{A} \subset X`$ such that:

1.  the spectral gap $`\Delta`$ defining $`\Pi_{\mathrm{coh}}`$ is uniformly bounded below on $`\mathcal{A}`$,

2.  the projector $`\Pi_{\mathrm{coh}}`$ is norm-continuous on $`\mathcal{A}`$,

3.  truncation error remains bounded by $`\varepsilon < \varepsilon_\ast`$ under iteration of $`T`$.

</div>

<div class="definition">

**Definition 2** (MTT Admissibility). A point $`x \in X`$ is admissible if it lies in a domain $`\mathcal{A}`$ satisfying the above controlled truncation conditions.

</div>

This definition is equivalent to admissibility as used throughout the MTT corpus.

# Coherence Capacity (MTT-Native Definition)

We now define coherence capacity directly in terms of MTT control data.

<div class="definition">

**Definition 3** (MTT Coherence Capacity). The coherence capacity $`C_{\mathrm{MTT}}(x)`$ at $`x \in X`$ is a lower bound on the admissibility margin, defined as any scalar functional satisfying
``` math
C_{\mathrm{MTT}}(x) > 0
\quad \Longleftrightarrow \quad
\begin{cases}
\Delta(x) > 0,\\
\|\Pi_{\mathrm{coh}}\| \text{ is bounded near } x,\\
\text{truncation error remains controlled.}
\end{cases}
```

</div>

<div class="remark">

*Remark 4*. The precise functional form of $`C_{\mathrm{MTT}}`$ is not unique. Any scalar that vanishes precisely when controlled truncation fails is sufficient. This nonuniqueness reflects the fact that coherence capacity is an invariant resource, not a new observable.

</div>

#### Meaning of invariance.

By “invariant” we do not mean that coherence capacity is a fundamental or unique primitive. Rather, it is invariant in the sense that all admissibility criteria used throughout the MTT corpus define the same zero set and positivity domain. Different technical constructions may realize this margin in different variables, but they all fail simultaneously. Coherence capacity is therefore an invariant of admissibility failure, not an additional axiom.

<div class="proposition">

**Proposition 5**. *For any MTT realization satisfying the controlled truncation assumptions, there exists a coherence capacity functional $`C_{\mathrm{MTT}}`$ that is strictly positive on admissible domains and vanishes at admissibility boundaries.*

</div>

<div class="proof">

*Proof.* This follows directly from compactness of admissible slabs and continuity of the spectral data defining $`\Pi_{\mathrm{coh}}`$. ◻

</div>

# Capacity Collapse and Nonexistence of Global Inverse

We now restate the irreversibility result in fully MTT-native form.

<div class="definition">

**Definition 6** (Global Section). A global section of the coherent projection is a measurable map $`S : \mathcal{H}_{\mathrm{coh}} \to \mathcal{H}`$ such that
``` math
\Pi_{\mathrm{coh}} \circ S = \mathrm{Id}_{\mathcal{H}_{\mathrm{coh}}}.
```

</div>

<div id="thm:capacity_collapse" class="theorem">

**Theorem 7** (Capacity Collapse Implies No Global Section). *Assume controlled truncation holds on $`\mathcal{A}`$ and fails on $`\partial\mathcal{A}`$. If a trajectory crosses a point where $`C_{\mathrm{MTT}} = 0`$, then no global measurable section of $`\Pi_{\mathrm{coh}}`$ exists.*

</div>

<div class="proof">

*Proof.* At $`C_{\mathrm{MTT}}=0`$, the spectral gap closes or projector regularity fails. Consequently, $`\Pi_{\mathrm{coh}}`$ identifies distinct states in $`X`$ whose images in $`\mathcal{H}_{\mathrm{coh}}`$ coincide on a set of nonzero measure. Any measurable section would require selecting a unique representative from each equivalence class, contradicting measurability and boundedness of $`\Pi_{\mathrm{coh}}`$. ◻

</div>

<div class="corollary">

**Corollary 8**. *Effective irreversibility in MTT is a structural consequence of admissibility failure, not of stochasticity or noninvertible fundamental dynamics.*

</div>

# Geometry as a Two–Derivative Bookkeeping of Admissibility

In Modal Triplet Theory, spacetime geometry does not appear as a fundamental interaction but as a consistency structure ensuring compatibility of local coherent projections across neighboring admissible regions. The coherence-capacity formulation sharpens this statement.

Let $`C_{\mathrm{MTT}}(x)`$ denote the coherence capacity expressed in effective spacetime coordinates wherever such a representation exists.

<div class="assumption">

**Assumption 9** (Slow Variation). We restrict attention to regimes in which $`C_{\mathrm{MTT}}`$ varies slowly compared to the characteristic coherence length of admissible slabs.

</div>

This assumption is implicit in all geometric derivations in the MTT corpus and corresponds to working at leading order in a derivative expansion.

#### Interpretive warning.

The appearance of $`C_{MTT}(x)`$ in an effective action does *not* indicate the introduction of a new dynamical scalar field or degree of freedom. The function $`C_{MTT}(x)`$ represents the local admissibility margin expressed in effective spacetime coordinates under the assumption of slow variation. Writing $`C_{MTT}`$ as a spacetime-dependent quantity is a descriptive reparameterization of projector regularity, spectral separation, and truncation control, not a modification of the microscopic dynamics.

<div class="proposition">

**Proposition 10**. *At two-derivative order, the unique local, diffeomorphism-invariant scalar functional that can encode spatial variation of coherence capacity is linear in the Ricci scalar.*

</div>

<div class="proof">

*Proof.* Locality restricts admissible terms to functions of the metric and finitely many derivatives. Diffeomorphism invariance restricts scalars to contractions of curvature tensors and scalar fields. At two-derivative order, the only scalar linear in curvature is the Ricci scalar $`R`$. ◻

</div>

Accordingly, the effective bookkeeping action may be written as
``` math
\begin{equation}
S_{\mathrm{eff}}
=
\int \sqrt{-g}\left(
\frac{C_{\mathrm{MTT}}(x)}{16\pi} R
+ \mathcal{L}_{\mathrm{m}}
\right)
+ \mathcal{O}(\partial^4).
\end{equation}
```

<div class="remark">

*Remark 11*. Higher-curvature terms correspond to subleading corrections suppressed by the coherence length. No claim of uniqueness is made beyond the chosen truncation order.

</div>

## Einstein Limit

Varying the action with respect to the metric yields
``` math
\begin{equation}
C_{\mathrm{MTT}}\, G_{\mu\nu}
+
(g_{\mu\nu}\Box - \nabla_\mu\nabla_\nu) C_{\mathrm{MTT}}
=
8\pi T_{\mu\nu}
+ \cdots .
\end{equation}
```

When $`C_{\mathrm{MTT}}`$ is constant, Einstein gravity is recovered with
``` math
\begin{equation}
G_{\mathrm{eff}} = \frac{1}{C_{\mathrm{MTT}}}.
\end{equation}
```

<div class="remark">

*Remark 12*. Within MTT, Newton’s constant is not treated as a fundamental microscopic parameter but encodes, at effective level, the admissibility margin of the coherent sector. This interpretation is consistent with fixed-point and asymptotic-safety analyses in the corpus.

</div>

# Time and the Arrow of Irreversibility

The fundamental evolution $`\Phi_\tau`$ provides an ordering of configurations but does not define a physical time parameter. Time emerges only at the level of effective description, where admissible projections can be sequenced.

<div class="proposition">

**Proposition 13**. *Within an admissible coherence basin, effective evolution may be locally reversible.*

</div>

<div class="proof">

*Proof.* Within a basin, the projected evolution $`T=\Pi_{\mathrm{coh}}\circ\Phi_\tau`$ is contractive and admits a local inverse on its image so long as $`C_{\mathrm{MTT}}>0`$. ◻

</div>

Irreversibility enters precisely when admissibility fails.

<div class="definition">

**Definition 14** (Arrow of Time). The arrow of time is the ordering induced by the sequence of coherence-capacity exhaustion events along an effective trajectory.

</div>

This arrow is structural rather than statistical. Entropy increase follows as a consequence of capacity loss, not as its cause.

# Horizons, Bottlenecks, and Entropy

Coherence capacity is transported through effective descriptions and may concentrate or become depleted.

<div class="definition">

**Definition 15** (Capacity Bottleneck). A capacity bottleneck is a codimension-one surface across which
``` math
C_{\mathrm{MTT}} \to 0.
```

</div>

<div class="theorem">

**Theorem 16**. *Across a capacity bottleneck, the effective evolution admits no inverse accessible to observers confined to one side of the surface.*

</div>

<div class="proof">

*Proof.* At the bottleneck, controlled truncation fails and the conditions of Theorem <a href="#thm:capacity_collapse" data-reference-type="ref" data-reference="thm:capacity_collapse">7</a> apply locally. Hence no measurable section of $`\Pi_{\mathrm{coh}}`$ exists across the surface. ◻

</div>

In gravitational settings, such bottlenecks correspond to horizons. Finite redistributive capacity implies a bound on information flux across the surface, yielding area-scaling entropy laws derived elsewhere in the MTT corpus.

# Measurement and Thermalization Revisited

The same structural mechanism underlies phenomena traditionally treated as distinct.

## Measurement

Coupling a system to an apparatus imposes additional projection constraints, locally reducing $`C_{\mathrm{MTT}}`$. When capacity vanishes, the effective description must reset to a new admissible basin. This reset is observed as collapse.

## Thermalization

In high-capacity regimes, basin mixing erases memory of initial conditions. In low-capacity or fragmented regimes, memory persists. Thermalization is therefore capacity-dependent rather than universal.

# Explicit Mapping to Coherent Consistency and Fixed Points I–VI

We summarize the correspondence between coherence capacity and existing MTT constructions.

<div class="center">

| **MTT Construction**              |    **Capacity Interpretation**     |
|:----------------------------------|:----------------------------------:|
| Admissible slab                   | Region with $`C_{\mathrm{MTT}}>0`$ |
| Uniform spectral gap $`\Delta>0`$ |      Positive capacity margin      |
| Projector regularity              |        Capacity continuity         |
| Controlled truncation             |       Capacity conservation        |
| Gap closure / projector blowup    |        Capacity exhaustion         |
| Coherence spine                   |    Maximal-capacity fixed point    |
| RG fixed point                    |     Capacity-limited attractor     |

</div>

<div class="remark">

*Remark 17*. This mapping is many-to-one: multiple technical control parameters contribute to a single capacity margin. This nonuniqueness reflects the invariant nature of coherence capacity.

</div>

# Undecidability and Physical Simulability

If coherence-capacity exhaustion events were decidable in advance, effective evolution would require evaluating admissibility under all future perturbations.

<div class="proposition">

**Proposition 18**. *Decidability of capacity exhaustion would require solving the global inverse problem for the projected evolution and would render physical evolution non-simulable in real time.*

</div>

<div class="remark">

*Remark 19*. Undecidability of admissibility failure is therefore a consistency requirement ensuring that physical evolution can proceed without global foresight.

</div>

# Conclusion

We have shown that coherence capacity is the invariant admissibility margin underlying the diverse constructions of Modal Triplet Theory. By defining this margin explicitly in terms of spectral gaps, projector regularity, and controlled truncation, we close a conceptual gap in the MTT corpus.

Coherence capacity introduces no new dynamics and no additional ontology. It is the scalar measure of how much effective physics can be supported before projection fails. That this capacity is finite is not a limitation of Modal Triplet Theory, but the reason its effective descriptions exist at all.
