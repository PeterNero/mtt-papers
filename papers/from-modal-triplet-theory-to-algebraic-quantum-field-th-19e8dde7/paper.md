---
abstract: |
  An admissibility-indexed precosheaf is a pregeometric covariant functor only after its algebras and extension morphisms are supplied; overlap or failure of joint representability does not create commutators or imply locality. A physical Haag–Kastler net instead requires a selected Lorentzian base, an upper local operator net, and a localization-preserving coherent reduction. For a decomposable orthogonal projector $`P`$, we prove that compression of the $`P`$-compatible upper subalgebras preserves isotony and spacelike commutation. This is the rigorous MTT-to-AQFT bridge currently available. We also show why absence of a global admissible chart does not forbid an abstract quasilocal algebra or categorical colimit. The current q79 source now also supplies a selected free twisted-Dirac construction whose even CAR observable net has locality, covariance, the time-slice property, and nonempty positive Hadamard state space through standard AQFT results. The chart-to-region natural equivalence and the nonperturbative interacting C-star completion remain open.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: f885ff123d5a3ded5f81f9eb272ca9a02ad6105e9c74f3a20b29d6a945fdcbcc
paper_id: from-modal-triplet-theory-to-algebraic-quantum-field-th-19e8dde7
release_state: zenodo_released
released_version: v2
title: |
  Admissibility Precosheaves and Conditional AQFT Nets
  in Modal Triplet Theory
zenodo_doi: 10.5281/zenodo.21665973
zenodo_record_id: 21665973
zenodo_url: "https://zenodo.org/records/21665973"
---

# Version 2 Revision Note

Supersedes
Version 1, *From Modal Triplet Theory to Algebraic Quantum Field Theory: Local Nets from Admissible Charts and Coherent Basin Persistence*.

Reason
Version 1 inferred commutation from non-joint representability, assumed extension of every smaller-chart observable, and identified absence of a global chart with absence of an abstract global algebra.

Resolution
Version 2 distinguishes the pregeometric chart functor from the physical Haag–Kastler net and bases physical locality on an upper local net plus coherent locality descent.

Retained result
Admissible charts can index a useful partial algebraic description when their algebra objects and transition morphisms are explicitly given.

Remaining boundary
The selected free CAR sector is now available, but the chart-to-region natural equivalence, interacting physical C-star completion, selected interacting state, and nonperturbative continuum limit remain independent obligations.

# Scope and correction of the chart-only argument

AQFT assigns algebras to causally localized spacetime regions and relates them by injective algebra morphisms . Locally covariant QFT packages analogous data as a covariant functor on globally hyperbolic spacetimes and causal embeddings . Neither framework obtains Einstein causality merely from the absence of a common coordinate chart.

The former edition tried to derive three conclusions directly from MTT admissible charts:

1.  inclusion of charts was said to extend every observable and hence prove isotony;

2.  failure of joint representability was said to force commutation; and

3.  absence of one global chart was said to forbid a global algebra.

All three steps are invalid without additional structure. Extension is a map that must be defined and proved compatible. A commutator is meaningful only after both operands are represented in a common algebra. An abstract inductive limit or colimit need not be represented by any one indexing object.

The corrected construction therefore has three stages:
``` math
\begin{aligned}
 \text{admissibility precosheaf}
 &\longrightarrow \text{selected Lorentzian upper net}\\
 &\longrightarrow \text{coherently compressed physical net}.
\end{aligned}
```
The first arrow requires an explicit chart-to-region and algebra intertwiner. The second is the locality-descent theorem proved below.

# The AQFT target

Let $`(Y,g)`$ be a time-oriented globally hyperbolic Lorentzian spacetime, and let $`\mathcal K(Y)`$ be a chosen poset of relatively compact causally convex open regions. Write $`\mathbf{Alg}`$ for a category of unital $`*`$-algebras (or $`C^*`$-algebras) and unital injective $`*`$-homomorphisms.

<div class="definition">

**Definition 1** (Physical local net). A local net is a covariant functor
``` math
\mathfrak A:\mathcal K(Y)\longrightarrow\mathbf{Alg}.
```
For an inclusion $`O_1\subseteq O_2`$, functoriality supplies an injective map $`\iota_{12}:\mathfrak A(O_1)\to\mathfrak A(O_2)`$. Identifying its image with a subalgebra gives isotony,
``` math
O_1\subseteq O_2
 \quad\Longrightarrow\quad
 \mathfrak A(O_1)\subseteq\mathfrak A(O_2).
```

</div>

<div class="definition">

**Definition 2** (Einstein causality). The net is local if, whenever $`O_1`$ and $`O_2`$ are spacelike separated,
``` math
[\mathfrak A(O_1),\mathfrak A(O_2)]=0
```
inside a declared common ambient algebra. For a graded field net, the ordinary commutator is replaced by the graded commutator.

</div>

These two conditions are only part of a physical AQFT. Depending on the target, one must also address covariance, a state space, spectrum or microlocal-spectrum conditions, additivity, the time-slice axiom, duality, superselection structure, and a suitable continuum dynamics. The time-slice property is a dynamical theorem even in established perturbative constructions, rather than a consequence of isotony alone .

If the region system is directed and the morphisms are injective, its $`C^*`$-inductive limit gives a quasilocal algebra
``` math
\mathfrak A_{\mathrm{ql}}
 =\varinjlim_{O\in\mathcal K(Y)}\mathfrak A(O).
```
The limit is an abstract universal object. It need not equal $`\mathfrak A(O_*)`$ for a largest region $`O_*`$, and no largest region need exist.

# The pregeometric admissibility category

Let $`\mathcal C_{\mathrm{adm}}`$ be a category whose objects are declared MTT admissible contexts
``` math
\alpha=(U_\alpha,P_\alpha,\mathcal D_\alpha,\mathbf m_\alpha),
```
where $`U_\alpha`$ is a domain, $`P_\alpha`$ a coherent reduction, $`\mathcal D_\alpha`$ the required operator-domain data, and $`\mathbf m_\alpha`$ a vector of admissibility margins. Raw set inclusion $`U_\alpha\subseteq U_\beta`$ is not yet an algebra morphism.

<div class="definition">

**Definition 3** (Admissibility precosheaf). An admissibility precosheaf is a covariant functor
``` math
\mathfrak B:\mathcal C_{\mathrm{adm}}\longrightarrow\mathbf{Alg}.
```
A morphism $`u:\alpha\to\beta`$ includes, or is represented by, a specified unital injective $`*`$-homomorphism
``` math
j_u:\mathfrak B(\alpha)\longrightarrow\mathfrak B(\beta)
```
satisfying $`j_{\operatorname{id}}=\operatorname{id}`$ and $`j_{v\circ u}=j_v\circ j_u`$.

</div>

This definition is useful but conditional. The chart domains and projectors do not determine $`\mathfrak B(\alpha)`$, and overlap alone does not determine $`j_u`$.

<div id="prop:noextension" class="proposition">

**Proposition 4** (No automatic extension). *An inclusion $`U_\alpha\subseteq U_\beta`$ and admissibility of both charts do not imply that every observable in $`\mathfrak B(\alpha)`$ extends to $`\mathfrak B(\beta)`$, nor that any extension is unique or injective.*

</div>

<div class="proof">

*Proof.* Extension is additional algebraic data. The same pair of domains can be assigned a constant algebra functor, inequivalent matrix algebras, quotient algebras, or algebras with no selected homomorphism between them. None of these choices is fixed by set inclusion or positivity of admissibility margins. If a restriction map from the larger domain is supplied, it runs in the opposite direction and still need not possess a section. ◻

</div>

<div class="proposition">

**Proposition 5** (Non-comparability is not commutation). *Suppose $`\alpha`$ and $`\beta`$ have no common comparison object in $`\mathcal C_{\mathrm{adm}}`$. This fact alone implies neither $`[A,B]=0`$ nor $`[A,B]\ne0`$ for $`A\in\mathfrak B(\alpha)`$ and $`B\in\mathfrak B(\beta)`$.*

</div>

<div class="proof">

*Proof.* Without morphisms into a common algebra, the product $`AB`$ and hence the commutator $`AB-BA`$ are not typed. A value cannot be inferred for an expression that has not been defined. If a later physical realization maps both observables into a common algebra, their commutator is determined by that realization and its locality theorem. ◻

</div>

Thus $`\mathfrak B`$ records which partial descriptions and extensions have actually been constructed. It is a pregeometric organization of representability, not yet a Haag–Kastler net. In particular it has no notion of spacelike separation until a causal localization functor is supplied.

# Physical realization data

The physical construction requires the following independent hypotheses.

Lorentzian base.
A selected, time-oriented, globally hyperbolic four-dimensional base $`(Y,g)`$ and a bundle $`\pi:M\to Y`$.

Upper local theory.
A concrete upper net
``` math
O\longmapsto\mathfrak A_U(\pi^{-1}O)\subseteq\mathcal B(\mathcal H_U)
```
that is isotonic and local on $`\mathcal K(Y)`$.

Coherent reduction.
A decomposable orthogonal projector
``` math
P=\int_Y^\oplus P_y\,\mathrm d\nu(y)
```
on the upper Hilbert bundle. Decomposability prevents the reduction itself from mixing unrelated base fibers.

Compatibility.
Physical observables are taken from the subalgebra that preserves the coherent sector,
``` math
\mathfrak A_U^P(O)
 :=\{A\in\mathfrak A_U(\pi^{-1}O):[A,P]=0\}.
```
For a graded net, $`P`$ is also required to be even.

FP VI does not construct these data from the fixed-point spine alone. It proves that an instantaneous spatially bilocal kernel is insufficient for causality and identifies a local hyperbolic mediator theory as the consistent completion route . A selected completion must still supply the upper local net. The corrected Projection–Admissibility paper then supplies the compression theorem .

# Coherent locality descent

For $`O\in\mathcal K(Y)`$ define
``` math
\begin{equation}
 \mathfrak A_P(O)
 :=\{PAP|_{P\mathcal H_U}:A\in\mathfrak A_U^P(O)\}
 \subseteq\mathcal B(P\mathcal H_U).
 \label{eq:compressed-net}
\end{equation}
```

<div id="thm:descent" class="theorem">

**Theorem 6** (Conditional MTT locality descent). *Under the physical realization hypotheses above, $`O\mapsto\mathfrak A_P(O)`$ is an isotonic local net. If the upper net is $`C^*`$-algebraic, each $`\mathfrak A_P(O)`$ is a $`C^*`$-algebra. The graded statement also holds when $`P`$ is even and upper locality is graded locality.*

</div>

<div class="proof">

*Proof.* For $`A,B\in\mathfrak A_U^P(O)`$, commutation with $`P`$ gives
``` math
(PAP)(PBP)|_{P\mathcal H_U}=PABP|_{P\mathcal H_U},
 \qquad
 (PAP)^*=PA^*P.
```
Thus compression is a unital $`*`$-homomorphism on the compatible subalgebra, and its image is a unital $`*`$-algebra. A $`*`$-homomorphic image of a $`C^*`$-algebra is $`C^*`$-algebraic after the standard quotient/image identification.

If $`O_1\subseteq O_2`$, upper isotony gives $`\mathfrak A_U^P(O_1)\subseteq\mathfrak A_U^P(O_2)`$, hence $`\mathfrak A_P(O_1)\subseteq\mathfrak A_P(O_2)`$. If $`O_1`$ and $`O_2`$ are spacelike separated and $`A,B`$ belong to their respective compatible upper algebras, then
``` math
[PAP,PBP]|_{P\mathcal H_U}
 =P[A,B]P|_{P\mathcal H_U}=0
```
by upper locality. Replacing commutators by graded commutators proves the graded case. ◻

</div>

The theorem is inheritance, not creation. It cannot prove locality unless the upper theory is already local, and it says nothing about an upper observable that fails to preserve $`P\mathcal H_U`$. Likewise, a nondecomposable projector may mix base support and lies outside the declared physical interpretation.

# The missing chart-to-region intertwiner

The pregeometric and physical constructions are connected only after a selected interface is provided. Let
``` math
L:\mathcal K(Y)\longrightarrow\mathcal C_{\mathrm{adm}}
```
assign an admissible context to each physical region. Suppose there are $`*`$-homomorphisms
``` math
\rho_O:\mathfrak B(L(O))\longrightarrow\mathfrak A_P(O).
```

<div id="prop:naturality" class="proposition">

**Proposition 7** (Naturality gate). *The admissibility precosheaf represents the physical net only if, for every $`O_1\subseteq O_2`$, the naturality equation
``` math
\begin{equation}
 \rho_{O_2}\circ j_{12}
 =\iota_{12}\circ\rho_{O_1}
 \label{eq:naturality}
\end{equation}
```
holds. If every $`\rho_O`$ is an isomorphism, the two nets are naturally isomorphic. If they are merely homomorphisms, the interface is a reduction or representation, not an equivalence.*

</div>

<div class="proof">

*Proof.* Commutativity is exactly the naturality condition. Componentwise isomorphisms define a natural isomorphism; weaker components do not. ◻

</div>

Equation <a href="#eq:naturality" data-reference-type="eqref" data-reference="eq:naturality">[eq:naturality]</a>, together with a selected $`L`$, is the precise replacement for the former assertion that chart overlap automatically becomes physical localization.

# Global algebras, states, and representations

Absence of a terminal or largest object in $`\mathcal C_{\mathrm{adm}}`$ means that no one admissible chart represents every context. It does not imply that the diagram $`\mathfrak B`$ lacks a categorical colimit, and it does not imply that the physical net lacks a quasilocal algebra.

<div class="proposition">

**Proposition 8** (Compatible states and the inductive limit). *Let $`\{\mathfrak A_P(O),\iota_{12}\}`$ be a directed unital $`C^*`$-net. A state $`\omega`$ on $`\mathfrak A_{\mathrm{ql}}`$ restricts to a compatible family $`\omega_O`$. Conversely, a compatible family satisfying
``` math
\omega_{O_2}\circ\iota_{12}=\omega_{O_1}
```
defines a state on the algebraic inductive limit and hence on its $`C^*`$-completion.*

</div>

<div class="proof">

*Proof.* Restriction gives compatibility by functoriality. Conversely, define the functional on an equivalence class represented by $`A\in\mathfrak A_P(O)`$ as $`\omega_O(A)`$. Compatibility makes the value independent of the representative. Positivity, normalization, and boundedness pass to the completion. ◻

</div>

Therefore a no-state claim must prove failure of compatible physical state data, not merely failure of a global chart. Similarly, every abstract $`C^*`$-algebra has a faithful Hilbert-space representation, while a *selected chart-induced representation satisfying all MTT admissibility conditions* may fail to exist. Those are different statements.

# Horizons and irreversibility are separate targets

A physical AQFT can assign algebras to regions on both sides of a causal horizon. Restriction to an observer’s wedge, a thermal or modular property, and loss of operational access depend on the spacetime, net, and state. A boundary of an MTT admissible chart may obstruct continuation of that chart or of one selected representation, but it becomes a physical horizon only after the map $`L`$ and the relevant causal statement are proved.

Likewise, neither a missing global chart nor a failed extension map establishes an arrow of time. Irreversibility needs oriented dynamics plus an asymmetric property such as noninvertible effective evolution, a monotone entropy or Lyapunov functional, or boundary data. The local-net theorem is neutral on that question.

# Current MTT-to-AQFT status

The current corpus supports the following scoped ledger.

Admissibility-indexed precosheaf.
Available as a conditional pregeometric construction once algebra objects and extension morphisms are specified. It is not forced by chart overlap alone.

Physical Lorentzian base.
The selected q79 branch currently supplies a conditional global Lorentzian coframe and causal representative after the discrete $`A_{\mathrm{QG}}`$ realization declaration and one binary $`A_{\mathrm{causal}}`$ boundary mark. This does not itself construct a QFT net.

Selected free local theory.
A globally hyperbolic framed q79 representative and selected twisted massless Dirac source now compose with standard CAR/AQFT machinery to give an even observable net with locality, covariance, the time-slice property, and a nonempty positive Hadamard state space . The CAR, microlocal, and time-slice theorems are imported standard results whose hypotheses the selected source satisfies.

Locality descent.
Theorem <a href="#thm:descent" data-reference-type="ref" data-reference="thm:descent">6</a> is exact under its stated upper-net and projector hypotheses. This is the currently rigorous AQFT-style bridge.

Perturbative observable branch.
A current selected-SM result gives a conditional perturbative observable functor, while importing standard BRST/Faddeev–Popov quantization rather than deriving it from MTT.

Constructive finite-domain QFT.
Current SPT-filtered TT/BRST functional integrals provide conditional finite-domain Borel and Ward-identity results. Infinite volume, the full chiral Standard Model, Lorentzian reconstruction, and a complete nonperturbative BRST Hilbert space remain open .

Full interacting AQFT equivalence.
Open. The free CAR net does not supply the naturality interface <a href="#eq:naturality" data-reference-type="eqref" data-reference="eq:naturality">[eq:naturality]</a>, a selected interacting state, a fixed-coupling physical interacting C-star algebra, the nonperturbative continuum completion, or a target-equivalence certificate.

# Scoped reconstruction theorem

<div id="thm:scoped" class="theorem">

**Theorem 9** (Scoped MTT–AQFT relation). *The corrected MTT corpus supports the following implications:*

1.  *admissible contexts can carry a pregeometric precosheaf when their algebras and functorial extension maps are supplied;*

2.  *a selected Lorentzian base, a local upper net, and a decomposable coherent projector produce the physical local net <a href="#eq:compressed-net" data-reference-type="eqref" data-reference="eq:compressed-net">[eq:compressed-net]</a> on the compatible subalgebra;*

3.  *upper isotony and Einstein causality descend to that physical net; and*

4.  *a natural chart-to-region interface identifies the pregeometric and physical nets only to the degree expressed by its component maps.*

*No commutation relation follows from non-joint representability. No absence of an abstract quasilocal algebra, state, faithful abstract representation, horizon law, or temporal arrow follows from absence of a global admissible chart.*

</div>

<div class="proof">

*Proof.* The first item is the definition and functoriality requirement of $`\mathfrak B`$. The second and third are Theorem <a href="#thm:descent" data-reference-type="ref" data-reference="thm:descent">6</a>. The fourth is Proposition <a href="#prop:naturality" data-reference-type="ref" data-reference="prop:naturality">7</a>. The final exclusions follow from the typing arguments and the inductive-limit state proposition above. ◻

</div>

# Changes from Version 1

Version 2 makes the following theorem-level corrections.

1.  It replaces the chart-only AQFT derivation by separate pregeometric and physical constructions.

2.  It removes the inference from failure of joint representability to commutation.

3.  It removes automatic observable extension and requires declared functorial morphisms.

4.  It derives physical isotony from upper algebra inclusion and coherent compression.

5.  It derives physical locality from upper spacelike commutation, not from chart non-comparability.

6.  It restores the possible quasilocal inductive limit and distinguishes it from a single global admissible chart.

7.  It replaces claims of automatic horizons and irreversibility by their actual state, causal, and dynamical theorem requirements.

8.  It adds the chart-to-region naturality gate and updates the QFT status to the current conditional/finite-domain frontier.

# Conclusion

MTT currently has both a rigorous conditional locality-descent bridge and one selected free realization. A local upper theory can be compressed to a coherent physical sector without losing isotony or spacelike commutation, provided the reduction is fiberwise and the observables preserve that sector. On the selected q79 twisted-Dirac source, standard CAR/AQFT machinery supplies the even free observable net, covariance, time slice, and positive Hadamard states.

The result does not make locality emerge from non-comparability. Nor does it construct the chart-to-region map or the interacting physical completion. The precise next targets are the naturality and equivalence conditions linking the free physical net to the admissibility precosheaf, followed by a selected interacting state and nonperturbative interacting C-star completion.

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

The precosheaf and conditional-net results are proved from supplied algebraic data, not from the embedded Standard Model profile audit. That audit is a lower-sector cross-check only. The open strict-upgrade ledger records an unresolved source problem and supplies no AQFT reconstruction theorem.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Corpus-state cross-checks

- `A04/final_12_of_12_audit` (**PROFILE_REPLAY**): Twelve-obligation embedded renormalized-SM equivalence audit.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

9

R. Haag and D. Kastler, *An Algebraic Approach to Quantum Field Theory*, Journal of Mathematical Physics **5** (1964), 848–861, doi:10.1063/1.1704187.

R. Brunetti, K. Fredenhagen, and R. Verch, *The Generally Covariant Locality Principle—A New Paradigm for Local Quantum Physics*, Communications in Mathematical Physics **237** (2003), 31–68, arXiv:math-ph/0112041.

B. Chilian and K. Fredenhagen, *The Time Slice Axiom in Perturbative Quantum Field Theory on Globally Hyperbolic Spacetimes*, arXiv:0802.1642.

P. Nero, *The Projection–Admissibility Principle: Descent, Recovery, and Structural Constraints on Effective Description*, version 2, 2026.

P. Nero, *Fixed Points VI: Formal Synthesis and Physical Interpretations*, corrected version 4, 2026.

P. Nero, *Modal Triplet Theory: A Typed Relationship Atlas*, version 3, 2026.

P. Nero, *MTT Selected Quantization and Nonperturbative-QFT Strict-Upgrade Audit*, technical audit version 1, 2026.

P. Nero, *Modal Triplet Theory and Quantum Field Theory on Curved Spacetime: A Selected Free CAR Net and the Interacting Reconstruction Boundary*, version 4, 2026.

</div>
