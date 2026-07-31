---
abstract: |
  Feynman graphs are used in quantum field theory, classical statistical field theory, stochastic dynamics, and effective descriptions of gravity. Their recurrence has a precise but limited explanation. Once one specifies a nondegenerate quadratic kernel, interaction tensors, a grading, and a contraction rule, Wick expansion organizes perturbative coefficients by graphs. The graph grammar is therefore not uniquely quantum. It also does not, by itself, select a physical propagator, Bose or Fermi statistics, causal locality, gauge reduction, counterterms, positivity, or unitarity.

  This paper reformulates modal diagrammatics around that distinction. We prove a finite graded graph-expansion theorem and an exact projection theorem: if an even projector intertwines the quadratic operator, interaction tensors, grading, and declared identities, then every all-retained graph coefficient agrees with the coefficient computed in the projected theory. We also prove a nonselection theorem showing that the same graph combinatorics supports continuously many inequivalent weights and different statistics. Thus basin adjacency or coherence language alone cannot derive Feynman rules.

  For Modal Triplet Theory, the result supplies a rigorous transfer target. The selected q79 twisted-Dirac construction already composes with standard CAR/AQFT machinery to give a free even local net. The present theorem explains how a selected upper action could transfer its perturbative graph data to a lower effective sector. It does not manufacture that action. The geometry-selected upper action, fixed-coupling interacting gauge–BRST $`C^*`$-completion, renormalization-group matching, and observable uncertainty packet remain open. The formulation retains the explanatory value of modal diagrammatics while making its mathematical and physical boundary explicit.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: Version 2, July 2026
generated_from_main_tex_sha256: 3e02bffabd34d5a711ba23c10a8d5a63d77d409de28fc75b62f5bc29cf88a2a6
paper_id: modal-diagrammatics-the-origin-of-feynman-rules-from-co-79b757d8
release_state: zenodo_released
released_version: v2
title: |
  **Universal Perturbative Graph Structure:**
  A Typed Modal Diagrammatics and Its Quantum Boundary
zenodo_doi: 10.5281/zenodo.21715156
zenodo_record_id: 21715156
zenodo_url: "https://zenodo.org/records/21715156"
---

# Version 2 revision note

#### Supersedes.

Version 1.0 (DOI [10.5281/zenodo.18330804](https://doi.org/10.5281/zenodo.18330804)).

#### Reason.

Version 1 correctly emphasized that diagrammatic expansions are not exclusive to quantum theories, but it attributed too much to coherence and Gaussian combinatorics. In several places it treated a modal Hessian as a selected physical propagator, described projected diagrams as necessarily the standard Feynman rules, and discussed quantum behavior and gravity beyond what the supplied structure proved.

#### Resolution.

Version 2 makes four substantive changes.

1.  It replaces the broad origin claim by exact finite graded graph-expansion and projection theorems.

2.  It distinguishes the quadratic inverse, Euclidean covariance, retarded/advanced Green operators, causal propagator, state two-point function, and Feynman kernel.

3.  It proves that graph incidence data do not select numerical weights, statistics, gauge identities, counterterms, or a quantum theory.

4.  It reconciles the paper with the current MTT ledger: the selected free q79 even-CAR net is closed at its declared tier, while the upper action and nonperturbative interacting completion remain open.

These are corrections to the central claim, not merely added caveats.

#### Retained result.

The original observation that classical and quantum models can share the same perturbative graph grammar is retained and is now proved at the exact finite graded level.

#### Remaining boundary.

A selected upper action, its complete projection intertwiners, and a fixed-coupling interacting gauge–BRST $`C^*`$-completion are not established here.

# Why the same diagrams recur

A perturbative graph is a compact record of two operations:

1.  insert multilinear interaction tensors;

2.  contract their arguments pairwise with a chosen two-point kernel.

The record is useful because the number of pairings grows rapidly. Wick’s theorem is the algebraic mechanism that turns those pairings into graph sums . Nothing in that combinatorial statement alone decides whether the underlying system is a Euclidean random field, a Lorentzian quantum field, a response theory, or a finite algebraic model.

This observation motivates, but does not yet prove, the MTT interpretation. A fixed point can provide a background about which to expand. A projector can identify retained modes. Neither object determines the action, its quadratic inverse, or its higher derivatives. Those data must be supplied or derived separately. The useful question is therefore not *whether coherence automatically creates Feynman rules*, but:

> Under which explicit hypotheses does perturbative graph data pass from an upper description to a projected effective description?

The answer below is exact on a declared finite or regularized domain. It is intentionally not a claim about convergence of an infinite perturbation series or existence of an interacting continuum QFT.

# The typed perturbative input

## Finite graded field space

Let
``` math
E=E_{\bar 0}\oplus E_{\bar 1}
```
be a finite-dimensional real or complex super vector space. Even coordinates represent bosonic directions and odd coordinates represent fermionic directions. Fix:

1.  an even nondegenerate quadratic operator $`K:E\to E^*`$;

2.  its inverse contraction kernel $`G=K^{-1}:E^*\to E`$;

3.  graded-symmetric interaction tensors
    ``` math
    V_n\in (E^*)^{\otimes n},\qquad 3\leq n\leq N;
    ```

4.  a formal coupling parameter $`\lambda`$;

5.  an ordering and orientation convention for odd half-edges.

The formal action is
``` math
\begin{equation}
 S(\phi)=\frac12 K(\phi,\phi)
 +\sum_{n=3}^{N}\frac{\lambda^{n-2}}{n!}V_n(\phi,\ldots,\phi).
 \label{eq:action}
\end{equation}
```
The powers of $`\lambda`$ are conventional and may be replaced by independent formal couplings without changing the argument.

The word “typed” matters. The pair $`(K,V_n)`$ does not yet define a physical QFT. It defines algebraic graph weights. A physical interpretation requires additional structures described in <a href="#sec:quantum-boundary" data-reference-type="ref+label" data-reference="sec:quantum-boundary">6</a>.

## Graph weights

Let $`\Gamma`$ be a finite graph whose vertices have valence between $`3`$ and $`N`$. Assign $`V_{\deg(v)}`$ to every vertex and $`G`$ to every internal edge. Contract matching tensor indices. For odd labels, include the Koszul sign $`\epsilon(\Gamma)`$ determined by the declared ordering. The resulting scalar or external tensor is
``` math
\begin{equation}
 W_\Gamma(K,V,G)
 =
 \frac{\epsilon(\Gamma)}{|\operatorname{Aut}\Gamma|}
 \operatorname{Contr}_\Gamma
 \left(
 \bigotimes_{v\in V(\Gamma)}V_{\deg(v)}
 \otimes
 \bigotimes_{e\in E_{\mathrm{int}}(\Gamma)}G
 \right).
 \label{eq:graph-weight}
\end{equation}
```
This formula exposes all of the information that a bare graph drawing hides: numerical kernels, vertex tensors, symmetry factors, and grading.

<div class="definition">

**Definition 1** (Perturbative graph datum). A perturbative graph datum is the tuple
``` math
\mathfrak D=(E,\operatorname{Gr}E,K,G,\{V_n\},\epsilon,\mathcal R),
```
where $`\mathcal R`$ records any regularization or renormalization map needed to define singular contractions. In a finite nonsingular model, $`\mathcal R=\mathrm{Id}`$.

</div>

# The graph expansion theorem

<div id="thm:wick-graph" class="theorem">

**Theorem 2** (Finite graded Wick graph expansion). *Let $`E`$, $`K`$, and $`V_n`$ be as above. Treat the Gaussian expectation with covariance $`G=K^{-1}`$ and the interaction exponential as a formal power series. Every coefficient of every polynomial correlation function is a finite sum of the weights <a href="#eq:graph-weight" data-reference-type="eqref" data-reference="eq:graph-weight">[eq:graph-weight]</a>. The vertices are the tensors $`V_n`$, the internal edges are contractions by $`G`$, the automorphism denominator gives the symmetry factor, and the odd permutation convention gives the fermionic sign.*

</div>

<div class="proof">

*Proof.* Expand the interaction exponential order by order in $`\lambda`$. At a fixed order only finitely many products of the $`V_n`$ occur. Apply the graded Wick rule to each polynomial Gaussian expectation. Every complete pairing identifies two tensor arguments and contracts them with $`G`$. Grouping pairings that differ only by relabeling yields an isomorphism class of graphs and the orbit–stabilizer factor $`|\operatorname{Aut}\Gamma|^{-1}`$. Moving odd variables into the chosen pairing order produces the Koszul sign. Conversely, every decorated graph determines such a pairing. Thus the two finite sums agree coefficient by coefficient. ◻

</div>

<div class="remark">

*Remark 3*. The theorem is exact as a statement about formal coefficients. It does not assert convergence, reflection positivity, causal factorization, unitarity, or existence of a continuum measure.

</div>

## What is universal

The universal content is now precise:
``` math
\begin{gathered}
\text{quadratic contraction}
+\text{multilinear interactions}
+\text{grading}\\
\Longrightarrow\quad
\text{graph-indexed formal coefficients}.
\end{gathered}
```
Classical Gaussian measures and quasifree quantum states both instantiate this schema. Their physical meanings remain different because their algebras, kernels, state conditions, and localization rules differ.

# Exact transfer through a finite projection

## Compatible retained sector

Let $`P:E\to E`$ be an even idempotent and write $`E_P=\mathop{\mathrm{im}}P`$. Assume $`P`$ is $`K`$-self-adjoint and
``` math
\begin{equation}
 [P,K]=0.
 \label{eq:PK}
\end{equation}
```
Then $`K`$ is block diagonal on $`E_P\oplus\ker P`$, and
``` math
K_P=K|_{E_P},\qquad G_P=K_P^{-1}=PGP|_{E_P}.
```
Define the retained vertex
``` math
V_n^P=V_n|_{E_P^{\otimes n}}.
```

<div id="thm:projection" class="theorem">

**Theorem 4** (All-retained graph transfer). *Under <a href="#eq:PK" data-reference-type="eqref" data-reference="eq:PK">[eq:PK]</a>, let $`\Gamma`$ be a decorated graph for which every half-edge label lies in $`E_P`$. Then
``` math
W_\Gamma(K_P,V^P,G_P)
 =
 W_\Gamma(K,V,G)\big|_{E_P}.
```
The equality includes symmetry factors and graded signs.*

</div>

<div class="proof">

*Proof.* At every retained vertex, $`V_n^P`$ is exactly the restriction of $`V_n`$. On every retained internal edge, commutation and block diagonality give $`G_P=PGP|_{E_P}`$. Since $`P`$ is even, it preserves parity and hence the Koszul sign. The underlying graph and its automorphism group are unchanged. Substitution into <a href="#eq:graph-weight" data-reference-type="eqref" data-reference="eq:graph-weight">[eq:graph-weight]</a> proves the equality. ◻

</div>

<div id="cor:closed-sector" class="corollary">

**Corollary 5** (Closed retained subtheory). *If, in addition, every mixed interaction component vanishes,
``` math
V_n(x_1,\ldots,x_n)=0
 \quad\text{whenever retained and discarded arguments both occur},
 \label{eq:no-mixed}
```
then the full formal perturbative expansion with retained external legs factorizes from the discarded sector. After normalization by vacuum terms, it equals the expansion computed solely from $`(E_P,K_P,\{V_n^P\})`$.*

</div>

<div class="proof">

*Proof.* Condition <a href="#eq:no-mixed" data-reference-type="eqref" data-reference="eq:no-mixed">[eq:no-mixed]</a> prevents a connected graph with retained external legs from containing a discarded internal label. Apply <a href="#thm:projection" data-reference-type="ref+label" data-reference="thm:projection">4</a> to every connected contribution. Purely discarded vacuum graphs factor and cancel in normalized correlators. ◻

</div>

## Why effective actions are needed

Without <a href="#eq:no-mixed" data-reference-type="eqref" data-reference="eq:no-mixed">[eq:no-mixed]</a>, the theorem does *not* say that simply deleting discarded modes gives the correct lower theory. Mixed vertices allow discarded internal lines to contribute to retained observables. Integrating them out produces an effective action
``` math
e^{-S_{\mathrm{eff}}(\phi_P)}
 =
 \int_{\ker P}e^{-S(\phi_P+\chi)}\,\mathrm{d}\chi
```
in a Euclidean finite model, or its appropriate formal/algebraic analogue. That effective action usually contains new nonlocal or higher-order vertices. Projection and marginalization are therefore different operations.

## Transfer of identities

<div id="prop:ward" class="proposition">

**Proposition 6** (Intertwined identity transfer). *Let $`\mathcal A`$ and $`\mathcal A_P`$ be algebras of formal functionals, let $`R:\mathcal A\to\mathcal A_P`$ be the restriction induced by $`P`$, and let $`\mathcal W,\mathcal W_P`$ be linear identity operators. If
``` math
R\mathcal W=\mathcal W_P R,
```
then $`\mathcal W F=0`$ implies $`\mathcal W_P(RF)=0`$.*

</div>

<div class="proof">

*Proof.* Apply $`R`$ to $`\mathcal W F=0`$ and use the intertwining equality. ◻

</div>

This proposition is elementary, but it identifies the real obligation in gauge theory. Ward, BRST, or BV identities descend only after their operators and brackets are shown to intertwine. A mode count or a graph match does not establish this.

# The nonselection theorem

<div id="thm:nonselection" class="theorem">

**Theorem 7** (Graph combinatorics does not select Feynman rules). *The incidence structure of perturbative graphs, even together with a list of allowed valences, does not determine:*

1.  *propagator values;*

2.  *interaction strengths;*

3.  *bosonic or fermionic statistics;*

4.  *causal or boundary prescriptions;*

5.  *gauge-fixing, ghost, or BRST data;*

6.  *renormalization extensions or counterterms.*

*In particular, continuously many inequivalent perturbative graph data have the same underlying graph set.*

</div>

<div class="proof">

*Proof.* Take the one-dimensional bosonic action
``` math
S_{k,g}(x)=\frac{k}{2}x^2+\frac{g}{4!}x^4,
 \qquad k>0.
```
For every $`k`$ and $`g\neq0`$, the allowed connected graphs are the same four-valent graphs. A graph with $`I`$ internal edges and $`V`$ vertices has weight proportional to $`k^{-I}g^V`$. Varying $`k`$ or $`g`$ therefore changes all nontrivial weights without changing incidence data. Replacing the field by an odd multiplet changes exchange signs while the ungraded incidence graph can remain identical. Retarded, advanced, Euclidean, and Feynman prescriptions may solve equations associated with the same differential expression but obey different support or boundary conditions. Gauge fixing adds ghost and identity data, and renormalization chooses extensions of singular distributions. None is encoded by the bare graph set. ◻

</div>

<div class="corollary">

**Corollary 8** (Basin adjacency is insufficient). *A basin graph, neighborhood relation, or coherence-capacity network cannot by itself derive physical Feynman rules. It must be supplemented by a selected quadratic operator and inverse prescription, interaction tensors, grading, gauge structure where applicable, and a renormalization rule.*

</div>

# Which kernel is meant?

Version 1 used “propagator” too broadly. The following objects can be related, but they are not interchangeable.

<div class="center">

| Object | Defining input | What it does not automatically provide |
|:---|:---|:---|
| Algebraic inverse $`K^{-1}`$ | Nondegenerate finite quadratic form | Causality, positivity, or a quantum state |
| Euclidean covariance | Positive elliptic operator and measure | Lorentzian time ordering without reconstruction hypotheses |
| Retarded/advanced Green operator | Green-hyperbolic operator and support condition | A state two-point function |
| Causal propagator | Difference of retarded and advanced operators | Positive-frequency or Hadamard choice |
| Two-point function | Observable algebra and state | Time ordering or unique vacuum |
| Feynman kernel | Time ordering/state or boundary prescription | Nonperturbative completion |

</div>

On curved spacetime, local covariant Wick products and time-ordered products require microlocal and renormalization conditions . Epstein–Glaser renormalization shows that locality and causal factorization constrain the extension of distributions . These are physical and analytic inputs, not consequences of graph drawing.

# Gauge theories and renormalization

## Gauge-fixed perturbation theory

For a gauge theory the naive Hessian is degenerate along gauge orbits. One must introduce gauge-fixing and ghost sectors, or work in a homological BV/BRST formulation. The interaction data then include graded fields, antifields, a bracket, and a differential. The quantum master equation or corresponding Ward identities control the consistency of the perturbative expansion .

Modal projection is compatible with such a construction only if the projection preserves the relevant complex and identities. Schematically,
``` math
PQ=QP,\qquad
 P\{\cdot,\cdot\}=\{P\cdot,P\cdot\}_P,
\qquad
 R\mathcal W=\mathcal W_P R.
```
These equations are proof obligations. Calling discarded directions “inadmissible” does not make them true.

## Renormalized graph weights

In a continuum theory, products of propagators can be singular on coincident-point diagonals. A graph before extension may define a distribution only away from those diagonals. Renormalization extends it subject to locality, covariance, scaling, and symmetry requirements. Different allowed extensions correspond to finite renormalization freedoms. Thus the renormalization map $`\mathcal R`$ belongs in the perturbative graph datum.

The graph theorem remains useful: it organizes which distribution must be extended. It does not perform or uniquely select the extension.

# What MTT contributes now

## Fixed points and coherent sectors

MTT supplies a language of coherent fixed points, admissible sectors, and finite projections. At the level needed here, a fixed point identifies a background $`u_*`$, and a selected action $`S`$ would yield
``` math
K=\mathrm{d}^2S[u_*],
 \qquad
 V_n=\mathrm{d}^nS[u_*].
```
If $`S`$, $`u_*`$, and the inverse prescription are selected from one source, the tensors in the graph datum are no longer arbitrary. If only the fixed point or carrier is known, they remain underdetermined.

This is the significance of the current upper-action blocker. The missing theorem is not another restatement of Wick expansion. It is a same-source construction of an upper differential/action whose Hessian, higher products, symmetries, and projections reproduce the accepted lower structures.

## The selected free q79 CAR result

The companion QFT paper owns the current selected free-field theorem . On the declared globally hyperbolic framed q79 representative, the selected twisted massless Dirac operator composes with standard Green-hyperbolic and CAR/AQFT machinery to produce an even local observable net with locality, covariance, the time-slice property, and a nonempty positive Hadamard state space.

The present paper does not re-prove that theorem. It uses it to mark the quantum boundary accurately:
``` math
\text{selected Dirac source}
\longrightarrow
\text{standard CAR/AQFT construction}
\longrightarrow
\text{free local quantum net}.
```
The CAR relations and Hadamard machinery are not inferred from modal graphs.

## The interacting boundary

Current MTT work also records a classical BV master action, a gauge-fixed Green-hyperbolic equicausal algebra, and a formal all-orders anomaly-free quantum master equation at the declared perturbative tier. Those results support a conditional perturbative graph construction. A formal jet at zero coupling does not select a unique fixed-nonzero-coupling $`C^*`$-completion. A geometry-selected nonperturbative gauge–BRST bridge or regulator/continuum limit, selected physical state, RG matching, uncertainty control, and observable comparison remain open.

# Three illustrative cases

## Euclidean scalar model

For a positive matrix $`K`$ and quartic tensor $`V_4`$, the finite Gaussian integral is literal. The graph expansion is a moment expansion of an ordinary probability measure. It demonstrates that the graph grammar is not uniquely quantum.

## Free fermions

For an odd field, the Gaussian integral is algebraic in Grassmann variables, and contractions carry signs. The ungraded graph shape alone cannot recover those signs. One needs the parity and ordering data. In a physical CAR theory one additionally needs the CAR algebra, localization, and a state.

## Gauge fields

For gauge fields, the uncorrected Hessian has a kernel along gauge directions. A propagator appears only after gauge-fixing or homological reduction, and ghost vertices are part of the graph datum. BRST or BV identities constrain admissible counterterms. This case makes especially clear why “inverse Hessian plus coherence” is insufficient.

# Classical, quantum, and gravitational uses

## Classical statistical fields

In classical statistical field theory, a positive covariance and interaction potential generate graph expansions of moments. This is a fully adequate explanation for the recurrence of the same combinatorial grammar. It does not imply that classical and quantum theories differ only in interpretation: noncommutative observables, interference phases, local commutation relations, and state conditions are additional mathematical structures.

## Quantum field theory

In QFT, Wick expansion acts on a quasifree state or time-ordered product. The propagator prescription, statistics, local algebra, and renormalization conditions give the graphs their physical meaning. The current MTT free-CAR theorem provides such a free quantum source on its declared branch. Interacting QFT requires the remaining bridge.

## Perturbative gravity

Expanding a specified gravitational action around a background also produces quadratic and higher tensors, so graph organization applies. This neither proves UV completion nor shows that spacetime quantization is unnecessary. It establishes only the same conditional perturbative grammar. Any stronger MTT gravity claim must derive the background, action, gauge complex, state, and ultraviolet control from the selected source.

# Status and theorem ownership

<div class="center">

| Statement | Status | Owner or boundary |
|:---|:---|:---|
| Finite graded Wick graph expansion | Exact here | <a href="#thm:wick-graph" data-reference-type="ref+Label" data-reference="thm:wick-graph">2</a> |
| All-retained finite projection equality | Exact here | <a href="#thm:projection" data-reference-type="ref+Label" data-reference="thm:projection">4</a> |
| Closed-sector factorization under no mixed vertices | Exact here | <a href="#cor:closed-sector" data-reference-type="ref+Label" data-reference="cor:closed-sector">5</a> |
| Graph-combinatorics nonselection | Exact here | <a href="#thm:nonselection" data-reference-type="ref+Label" data-reference="thm:nonselection">7</a> |
| Selected q79 free even-CAR net | Closed at declared tier | Companion MTT-to-QFT paper; imported CAR/AQFT theorems |
| Embedded renormalized-SM equivalence | Closed at profile tier | Current A04 result; not a derivation of quantization |
| Upper action and automorphism transfer | Open | Current blocker B.ACTION.01 |
| Nonperturbative interacting gauge–BRST $`C^*`$ bridge | Open | Current blocker B.QFT.02 |
| No-knob Standard Model values | Open | Current strict-upgrade ledger |

</div>

This ownership table prevents a common form of accidental duplication. The paper proves the finite graph and transfer statements. It cites the free-CAR result. It does not promote formal or profile evidence into an interacting-QFT theorem.

# Validation program

A candidate upper-to-lower diagrammatic derivation should be accepted only after the following checks.

1.  **Source check:** identify the action, background, grading, and all continuous inputs by path and hash.

2.  **Quadratic check:** prove invertibility on the declared gauge-fixed or reduced domain and specify the inverse prescription.

3.  **Vertex check:** compute every retained $`V_n`$ from the same action, including overlap integrals and normalization conventions.

4.  **Projection check:** verify $`[P,K]=0`$, the vertex intertwiners, and whether mixed vertices vanish or are integrated out.

5.  **Statistics check:** preserve the $`\mathbb Z_2`$ grading and Koszul signs.

6.  **Gauge check:** verify BRST/BV chain maps and Ward or QME identities.

7.  **Renormalization check:** specify distribution extensions, scheme transport, and residual finite freedoms.

8.  **Physical check:** establish local algebra, positivity/state conditions, uncertainty control, and observable comparison at the claimed tier.

Passing only the graph-shape check is not enough.

# Discussion

## What survives from the original idea

The central intuition survives in a stronger form. Feynman-style diagrams are not mysterious pictures added to quantum mechanics. They are the natural combinatorial language of perturbative contractions. MTT can use that universality because its fixed points and projections offer a candidate upstream organization of backgrounds and retained sectors.

The correction is equally important. “Universal graph grammar” is not “universal physical dynamics.” A graph does not know which kernel is causal, which state is positive, which field is fermionic, which gauge identity must hold, or which counterterm is allowed. Those facts reside in the typed data attached to the graph.

## Why the projection theorem matters

<a href="#thm:projection" data-reference-type="ref+Label" data-reference="thm:projection">4</a> gives a concrete target for future MTT work. If the selected upper action is found, one need not compare final amplitudes by analogy. One can verify the commuting projection at the level of the quadratic operator, every interaction tensor, grading, and identity operator. Equality of the retained graph coefficients then follows mechanically.

The theorem also identifies failure modes. If $`P`$ does not commute with $`K`$, the lower propagator is not simply $`PGP`$. If mixed vertices survive, discarded modes generate effective interactions. If BRST/BV operators fail to intertwine, gauge identities need not descend. These are informative obstructions, not merely missing prose.

## Best next theorem

The decisive upstream theorem is:
``` math
\begin{gathered}
\text{selected q79 upper action and complex}\\
\Downarrow\\
K,\ \{V_n\},\ Q_{\mathrm{BRST}},\ \text{state/renormalization data}\\
\Downarrow\quad\text{by certified intertwiners}\\
\text{accepted lower free and interacting structures}.
\end{gathered}
```
This would turn the graph datum from an input into a derived object. Until then, the present paper supplies the exact transfer mathematics and the boundary that any claimed derivation must cross.

# Conclusion

The recurrence of Feynman graphs has a clean explanation. A quadratic contraction and multilinear interactions generate graph-indexed perturbative coefficients through graded Wick expansion. This grammar is shared by classical and quantum models. It is not, on its own, a quantization theorem.

We proved that compatible finite projection preserves every all-retained graph coefficient and, under absence of mixed vertices, the normalized retained perturbative expansion. We also proved that graph combinatorics cannot select numerical weights, statistics, causal prescriptions, gauge data, or renormalization. These statements give modal diagrammatics a precise role: it is an exact language for transferring a *selected* perturbative datum, not a substitute for selecting that datum.

For MTT, the free q79 even-CAR net is already available through a companion construction using standard CAR/AQFT machinery. The next frontier is the same-source upper action and its interacting gauge–BRST completion. A future success there can plug directly into the theorem proved here.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The theorems proved here are finite algebraic statements and do not depend on numerical fitting. The curated [MTT Results Reproduction repository](https://github.com/PeterNero/mtt-results-repro) is cited for current MTT status context. In particular, `A04/final_12_of_12_audit` records embedded renormalized-Standard-Model equivalence at the adopted profile tier, while `A05/strict_upgrade_ledger` records stronger no-knob obligations that remain open. Neither row proves the finite graph-expansion, projection, or nonselection theorems in this paper, and the open row is not evidence of closure.

The selected free-CAR theorem and the classical-to-quantum interface are documented in the companion records [10.5281/zenodo.21665998](https://doi.org/10.5281/zenodo.21665998) and [10.5281/zenodo.21714936](https://doi.org/10.5281/zenodo.21714936). Exact release artifacts, source hashes, and the revision audit accompany this paper in the MTT papers repository.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
