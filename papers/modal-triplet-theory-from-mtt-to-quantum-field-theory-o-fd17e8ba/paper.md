---
abstract: |
  The current Modal Triplet Theory corpus supports a precise but limited curved-spacetime quantum-field-theory result. On the selected globally hyperbolic framed q79 representative, a global coframe and parallel rank-six carrier define a zero-order-free twisted massless Dirac operator. Standard algebraic QFT then yields an even CAR observable net with locality, covariance, the time-slice property, and a nonempty positive Hadamard state space, together with the exact finite coherent/complement component map. These conclusions use independent QFT theorems; they are not derived from projection alone. At nonzero interaction, the selected carrier has a classical BV master-action and formal perturbative QME/equicausal construction, while a physical nonperturbative gauge-BRST C-star net, selected state, renormalization-group matching, and observable uncertainty packet remain open. The paper also separates Hadamard regularity from unitary implementability, and treats the semiclassical Einstein equation and FRW particle production as conditional applications. This establishes a selected free local QFT source and a formal interacting bridge, not a first-principles derivation of full interacting QFT from finite projection.
author:
- Peter Nero
current_version: v4
date: July 2026 Version 4
generated_from_main_tex_sha256: 03b7e07110f8ff1a980338f47ce88346aaa598cd6a9b149cbaa971234dcb6bb2
paper_id: modal-triplet-theory-from-mtt-to-quantum-field-theory-o-fd17e8ba
release_state: zenodo_released
released_version: v4
title: |
  Modal Triplet Theory and Quantum Field Theory on Curved Spacetime:
  A Selected Free CAR Net and the Interacting Reconstruction Boundary
zenodo_doi: 10.5281/zenodo.21665998
zenodo_record_id: 21665998
zenodo_url: "https://zenodo.org/records/21665998"
---

# Version 4 Revision Note

<div class="description">

Version 3, *Modal Triplet Theory: From MTT to Quantum Field Theory on Curved Spacetime*.

The earlier paper treated CCR/CAR quantization, Hadamard selection, local covariance, positivity, and unitary implementability as outputs of a projection map. It also blurred the internal six-dimensional geometry with four-dimensional curved spacetime.

The geometry is typed as $`Y_4`$ plus the selected internal $`X_6`$. Standard AQFT inputs are named explicitly, the currently closed free CAR net is stated at its selected tier, and interacting, semiclassical, and FRG layers are separated.

A selected twisted massless Dirac source composes with established CAR/AQFT machinery to give a local covariant free observable net and positive Hadamard states.

A geometry-selected nonperturbative interacting gauge-BRST C-star construction, full-branch state, RG/matching map, uncertainty budget, and observable comparison remain open.

</div>

# What is being constructed

Quantum field theory on curved spacetime is not one Hilbert space with a preferred vacuum. Its local formulation assigns algebras of observables to spacetime regions and controls states by microlocal singularity conditions .

The MTT construction must therefore provide a typed chain:
``` math
\begin{gathered}
\text{selected geometry and bundle}
\longrightarrow
\text{Green-hyperbolic field operator}\\
\downarrow\\
\text{classical solution/propagator space}
\longrightarrow
\text{CCR or CAR algebra and local net}\\
\downarrow\\
\text{physical states and observables}.
\end{gathered}
```
Projection can enter several arrows, but it does not replace any of them.

## Four plus six dimensions

The physical Lorentzian spacetime is denoted $`(Y_4,g)`$, assumed globally hyperbolic. The internal compactification candidate is denoted $`X_6`$, on the selected q79 Fu–Yau branch. At a simple reduction tier one may use $`Y_4\times X_6`$; a nontrivial fibration requires additional gluing data.

The shared circle is phase-bundle data within the selected geometry. It is not a fifth spacetime coordinate and is not Lorentzian time. Internal projectors act on internal or finite carrier factors unless a proved intertwiner transports them to a spacetime operator.

# Independent QFT ingredients

Let $`E\to Y_4`$ be a vector bundle and
``` math
P:\Gamma(E)\to\Gamma(E)
```
a normally hyperbolic or Green-hyperbolic field operator. Advanced and retarded Green operators $`G^\pm`$ satisfy
``` math
PG^\pm f=f=G^\pm Pf,
 \qquad
 \operatorname{supp}(G^\pm f)\subseteq J^\pm(\operatorname{supp}f).
```
Their difference $`G=G^- -G^+`$ determines the classical causal commutator or anticommutator form.

For bosons, canonical commutation relations require a symplectic solution space. For fermions, canonical anticommutation relations require the appropriate Hermitian form and charge conjugation structure. These quantization functors are standard mathematical inputs, not consequences of a Gaussian expansion or of choosing a coherent subspace.

## Local net axioms

For each suitable open region $`O\subset Y_4`$, an algebraic QFT net assigns $`\mathcal A(O)`$. The principal properties used here are:

<div class="description">

$`O_1\subset O_2`$ implies $`\mathcal A(O_1)\subset\mathcal A(O_2)`$.

Spacelike separated observable algebras commute (or graded-commute before taking the even observable subalgebra).

A region containing a Cauchy surface generates the full algebra.

Causal isometric embeddings induce compatible algebra morphisms.

</div>

These properties follow from the support and covariance structure of the chosen operator and quantization functor under standard hypotheses . They are not automatic for an arbitrary nonlocal filter.

# The selected free MTT source

The current q79 research ledger closes the following source statement on a selected globally hyperbolic framed representative:

- the global coframe and parallel rank-six carrier define a zero-order-free twisted massless Dirac operator $`\mathcal D_{\mathrm{q79}}`$;

- the corresponding even CAR observable net satisfies locality, covariance, and the time-slice property;

- its positive Hadamard state space is nonempty;

- the finite $`P_{\mathrm{Haar}}/Q`$ component map is exact.

This result is imported from the selected QFT source certificate; the present paper explains its meaning and boundaries.

<div id="thm:car" class="theorem">

**Theorem 1** (Conditional free CAR reconstruction). *Let $`(Y_4,g)`$ be globally hyperbolic and spin, let $`E\to Y_4`$ carry the required Hermitian and charge-conjugation data, and let $`\mathcal D`$ be a formally self-adjoint Green-hyperbolic Dirac-type operator. Then the standard CAR construction defines a locally covariant graded field net. Its even observable subnet obeys Einstein causality and the time-slice property. If a quasifree Hadamard two-point function exists, it defines a positive Hadamard state and supports locally covariant Wick polynomials and stress-tensor renormalization up to the standard finite curvature ambiguities.*

</div>

<div class="proof">

*Proof.* Green hyperbolicity provides the causal propagator and the Hermitian form on the quotient of compactly supported test sections. The CAR functor gives the graded net; support of the propagator gives graded locality and the Cauchy-surface exact sequence gives the time-slice property. The final statement is the standard Hadamard/microlocal renormalization theorem . ◻

</div>

Applied to $`\mathcal D_{\mathrm{q79}}`$, the hypotheses have been certified at the declared free tier. This is stronger than a general proposal: it is a selected local QFT source. It does not yet select masses, interactions, or a preferred global state.

# Hadamard states are not selected by phase transport alone

A two-point distribution $`W`$ is Hadamard when its wavefront set has the universal positive-frequency null-geodesic structure . Locally matching the leading Minkowski singularity is not, by itself, a global state construction: positivity, the field equation, commutation relations, and global consistency must all hold.

The current free q79 certificate establishes a nonempty positive Hadamard state space. It does not yet choose a unique state from shared-circle phases. Selecting one state requires additional physical data such as a stationary KMS condition, an asymptotic prescription, a cosmological initial-state condition, or another same-source rule.

## Hadamard regularity versus unitarity

Hadamard regularity controls ultraviolet singularities and local renormalization. Unitary implementability of a classical evolution between two Fock representations is a separate global question.

For bosons, the Shale criterion requires the antilinear Bogoliubov coefficient $`\beta`$ to be Hilbert–Schmidt. The CAR analogue imposes the corresponding restricted-unitary condition . Adiabatic regularity can improve high-frequency behavior, but it does not guarantee global Hilbert–Schmidt implementability on every noncompact spacetime or for every pair of states.

# Interacting and gauge sectors

For gauge theories, a physical construction must preserve the BV/BRST complex, the quantum master equation, causal factorization, and positivity on physical observables. A projector on a finite carrier does not establish these identities.

The current MTT interacting status is:

1.  the selected carrier composes with a classical BV master action;

2.  a gauge-fixed Green-hyperbolic equicausal algebra is available at the formal perturbative tier;

3.  an anomaly-free formal all-orders QME and formal positive physical state-space functor have been constructed;

4.  a literal physical C-star reference net and declared locally quasiequivalent Hadamard folia are closed at zero coupling.

These are substantial structural results. The formal coupling expansion
``` math
\mathcal A_\lambda=\mathcal A_0[[\lambda]]
```
does not select a unique theory at a fixed nonzero $`\lambda`$. The current flat-deformation no-go result makes this precise: a formal jet can have multiple inequivalent nonperturbative completions. A physical interacting theory therefore still requires a selected gauge-BRST C-star bridge or a regulator/continuum limit.

# Standard-Model profile results

The selected MTT Standard-Model program has closed its declared 12-of-12 embedded renormalized-SM equivalence at the adopted one-shared-physical- primitive/profile tier. This means that, once the accepted Standard-Model data and convention map are supplied, the finite carrier and transport pipeline reproduce the targeted perturbative observable profile.

It does not mean that all gauge, Yukawa, mixing, and Higgs values have been derived from q79 geometry without observed construction inputs. Those source-value and precision obligations remain separate from the existence of the free CAR net.

# Renormalized stress tensor and semiclassical gravity

Given a Hadamard state and a locally covariant renormalization prescription, point splitting defines
``` math
\langle T_{\mu\nu}\rangle_{\mathrm{ren}}
 =
 \lim_{x'\to x}
 D_{\mu\nu}(x,x')
 \bigl(W(x,x')-H(x,x')\bigr)
 +C_{\mu\nu}(g),
```
where $`H`$ is a Hadamard parametrix and $`C_{\mu\nu}`$ records the allowed local curvature counterterms. Conservation and trace anomaly statements depend on the field, state, and renormalization conditions .

The semiclassical Einstein equation
``` math
G_{\mu\nu}+\Lambda g_{\mu\nu}
 =
 8\pi G\,\langle T_{\mu\nu}\rangle_{\mathrm{ren}}
```
is a coupled semiclassical model. MTT does not currently derive it from the free CAR net. The revised GR paper supplies a conditional four-dimensional Einstein reduction; a same-source matter/gravity response and backreaction theorem remains additional work.

# FRG and curved spacetime

An FRG flow can organize effective couplings, but its use on curved Lorentzian spacetime requires a declared background split, gauge fixing, regulator, state or contour, and continuation prescription. Not every globally hyperbolic spacetime admits a useful Euclidean continuation.

The revised asymptotic-safety papers provide conditional endpoint, conjugacy, truncation-error, and essential-spectrum theorems. They do not currently emit the q79-to-FRG coupling chart. FRG-improved masses or curvature couplings should therefore be treated as external or conditional inputs in a curved-spacetime example.

# Illustrative FRW benchmark

On a spatially flat FRW spacetime
``` math
ds^2=-dt^2+a(t)^2d\mathbf x^2,
```
a scalar benchmark with specified mass $`m`$ and curvature coupling $`\xi`$ has rescaled modes satisfying an equation of the form
``` math
\ddot u_{\mathbf k}
 +\Omega_{\mathbf k}(t)^2u_{\mathbf k}=0,
```
where $`\Omega_{\mathbf k}`$ is determined by $`|\mathbf k|^2/a^2`$, $`m^2`$, $`\xi R`$, and the chosen rescaling. Adiabatic initial data of sufficiently high order can define Hadamard states under standard smoothness assumptions.

This is a test bed for the QFT machinery, not a numerical MTT prediction. To promote it, one must derive $`a(t)`$, the state, masses, couplings, and matching scale from the same selected branch and compare renormalized observables with an uncertainty budget.

# Status ledger

<div class="center">

| Object | Status | Meaning |
|:---|:---|:---|
| Selected twisted massless Dirac source | Closed | Globally hyperbolic framed q79 representative. |
| Even free CAR observable net | Closed | Locality, covariance, time slice, and positive Hadamard states. |
| Unique state from MTT phase data | Open | Nonempty state space is not a selection rule. |
| Interacting BV/QME construction | Formal all orders | Perturbative algebra and anomaly control, not fixed-coupling completion. |
| Physical nonperturbative C-star net | Open | Requires gauge-BRST bridge or regulator/continuum limit. |
| Embedded renormalized-SM equivalence | Closed at profile tier | Uses accepted profile inputs; not zero-knob source derivation. |
| Semiclassical backreaction | Conditional | Requires selected state, stress tensor, gravity source, and solution. |
| MTT-to-FRG curved-spacetime map | Open | Regulator, coupling chart, and continuation are not selected. |

</div>

# Discussion

The important advance is that the curved-spacetime QFT program no longer starts from an unspecified projection. It starts from a selected geometric Dirac operator and composes it with a well-developed local QFT functor. This gives a real free-theory result with correct locality and state-space properties.

The remaining difficulty is concentrated in the interaction. Formal perturbative control can establish powerful algebraic identities, but it cannot choose a unique fixed-coupling C-star completion. The correct next target is therefore a geometry-selected interacting regulator or renormalized BV pushforward that preserves the QME, positivity, local covariance, and the selected state through a continuum limit.

# Conclusion

MTT now reaches QFT on curved spacetime at two distinct tiers. The free twisted-Dirac CAR net is selected and closed on the declared q79 representative. The interacting gauge theory is formally reconstructed but not nonperturbatively selected.

This is a meaningful bridge, not a derivation of quantum theory from projection. CCR/CAR quantization, Hadamard microlocal structure, local covariance, time-slice behavior, and positivity enter through independent QFT theorems whose hypotheses the selected source must satisfy. Keeping those roles explicit makes the remaining interacting and backreaction problems sharply testable.

#### Corpus-state cross-checks.

- (*profile replay*).

  Twelve-obligation embedded renormalized-SM equivalence audit.

= by -

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The selected free CAR net and its curved-spacetime properties are established independently of the embedded Standard Model profile audit. That audit is contextual evidence for a lower effective target, while the open strict-upgrade row supplies no interacting QFT construction.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*, University of Chicago Press, 1994.

M. J. Radzikowski, “Micro-local approach to the Hadamard condition in quantum field theory on curved space-time,” *Communications in Mathematical Physics* **179** (1996), 529–553.

R. Brunetti, K. Fredenhagen, and R. Verch, “The generally covariant locality principle: A new paradigm for local quantum field theory,” *Communications in Mathematical Physics* **237** (2003), 31–68.

S. Hollands and R. M. Wald, “Local Wick polynomials and time ordered products of quantum fields in curved spacetime,” *Communications in Mathematical Physics* **223** (2001), 289–326.

J. Dimock, “Dirac quantum fields on a manifold,” *Transactions of the American Mathematical Society* **269** (1982), 133–147.

C. Bär, N. Ginoux, and F. Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007.

D. Shale, “Linear symmetries of free boson fields,” *Transactions of the American Mathematical Society* **103** (1962), 149–167.

P. Nero, *Modal Triplet Theory: Foundations*, current revised MTT paper corpus, 2026.

P. Nero, *Controlled Coherent Reduction to Four-Dimensional Einstein Gravity*, current revised MTT paper corpus, 2026.

P. Nero, *Modal Triplet Theory: Perturbative Coherent-Sector Quantum Gravity and the Heterotic UV-Completion Boundary*, current revised MTT paper corpus, 2026.

</div>
