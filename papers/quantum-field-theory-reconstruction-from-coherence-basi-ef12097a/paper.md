---
abstract: |
  This paper asks a narrower and more useful question than whether quantum field theory can be reconstructed from classical ensemble statistics. Let an admissible coherence-basin space carry a probability measure and bounded basin observables. We prove that these data have a canonical Hilbert-space representation by multiplication operators on an $`L^2`$ space. The representation is commutative. Convex mixtures, covariance kernels, Gaussian characteristic functionals, and classical coarse-graining follow within that layer, but canonical commutation or anticommutation relations, quantum interference, time ordering, a local net, and renormalized interactions do not.

  The correct connection to quantum field theory is an interface rather than an emergence-by-statistics theorem. A state on a quantum observable algebra restricts to a probability measure on every commutative record subalgebra; equivalently, a positive operator-valued measurement or instrument produces classical outcome statistics. Conversely, every state on a commutative subalgebra has extensions to the ambient $`C^*`$-algebra, but those extensions are generally nonunique. Identical basin statistics can therefore coexist with inequivalent quantum phases and correlations.

  This distinction can now be applied to the current Modal Triplet Theory (MTT) corpus. A companion paper owns the selected free-field construction: on the declared globally hyperbolic framed q79 representative, a twisted massless Dirac source composes with standard CAR/AQFT machinery to give an even local observable net with locality, covariance, the time-slice property, and a nonempty positive Hadamard state space. Basin and detector statistics may be read from commuting subalgebras or instruments of that net. The geometry-selected nonperturbative interacting gauge-BRST $`C^*`$-bridge, selected full-branch state, renormalization-group matching, and observable uncertainty packet remain open. The result is a precise classical-to-quantum interface and a closed selected free-QFT source, not a derivation of noncommutative QFT from probability alone.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: Version 3, July 2026
generated_from_main_tex_sha256: 54382b40794f6a0c0c77f151b4750262a84cc7c75d9089dc433f547e26fbdbf5
paper_id: quantum-field-theory-reconstruction-from-coherence-basi-ef12097a
release_state: zenodo_released
released_version: v3
title: |
  **From Coherence-Basin Statistics to a Local Quantum-Field Interface**
  Commutative Measures, the Selected Free CAR Net, and the Interacting Boundary
zenodo_doi: 10.5281/zenodo.21714936
zenodo_record_id: 21714936
zenodo_url: "https://zenodo.org/records/21714936"
---

# Version 3 revision note

<div class="description">

Version 2, DOI <https://doi.org/10.5281/zenodo.18322089>.

Version 2 claimed that coherence-basin measures generated Hilbert-space quantum states, noncommuting fields, propagators, path integrals, renormalization, and Feynman rules. Its GNS argument began with a commutative algebra and then inserted noncommuting operators without a construction. It also conflated classical covariance with several different quantum and causal kernels.

Version 3 proves the exact commutative representation supplied by basin statistics, gives a finite-dimensional nonuniqueness witness, and replaces the unsupported reconstruction with a typed state-restriction and state-extension interface. It imports, rather than duplicates, the separately owned selected free-CAR theorem and records the current interacting boundary.

Coherence basins can still provide useful configuration variables, preparation distributions, detector records, classical correlations, and coarse-grained summaries. Quantum fields need not be interpreted as classical substances. What is withdrawn is the claim that ordinary probability theory alone creates their noncommutative algebra.

The selected free q79 CAR net is closed at its declared tier. A unique state-selection rule and a geometry-selected nonperturbative interacting gauge-BRST $`C^*`$-completion remain open, as do full RG matching and precision-observable comparison.

</div>

# The question after the current MTT advances

There are two very different claims that can be made about a statistical description.

1.  A collection of physical configurations and a probability measure can be represented by functions and multiplication operators on a Hilbert space.

2.  Those statistical data determine a noncommutative quantum theory with field equations, causal propagators, local observable algebras, states, and interactions.

The first claim is a standard and exact representation theorem. The second does not follow from the first.

This distinction matters especially in MTT. The earlier version of this paper tried to make basin statistics do all of the work. The current research program has since supplied a more concrete route. A selected geometric source gives a Dirac-type operator; established CAR and algebraic QFT constructions then give the free quantum observable net. Statistics enter when a state and a physical record channel are applied to that net.

The revised chain is therefore
``` math
\begin{gathered}
\text{selected geometry and bundle}
\longrightarrow
\text{Green-hyperbolic field operator}\\
\longrightarrow
\text{CAR observable net},\\
\text{state and record channel}
\longrightarrow
\text{classical basin or detector law}.
\end{gathered}
```
The lower line is not a lesser physical event. Preparation, interaction with an apparatus, amplification, and recording are ordinary physical processes. The point is only that their classical output law does not, when read backwards, uniquely determine the quantum algebra that produced it.

# The classical basin layer

## Typed statistical data

Let $`(\mathcal B,\Sigma,\mu)`$ be a probability space whose points represent admissible coherence-basin configurations at a declared resolution. A bounded classical basin observable is an element
``` math
f\in L^\infty(\mathcal B,\Sigma,\mu).
```
Its expectation is
``` math
\mathbb E_\mu[f]=\int_{\mathcal B}f(b)\,d\mu(b).
```
The observable algebra
``` math
\mathcal C_\mu:=L^\infty(\mathcal B,\Sigma,\mu)
```
is a commutative unital $`C^*`$-algebra up to the usual identification almost everywhere. If topological basin data are needed, one may instead start from $`C(K)`$ for a compact Hausdorff configuration space $`K`$.

These definitions are intentionally modest. They describe a probability law over configurations and the functions that can be averaged. They do not assume that a basin is a particle, that $`\mu`$ is fundamental, or that the basin variables are complete.

## The canonical Hilbert representation

<div id="thm:commutative" class="theorem">

**Theorem 1** (Commutative basin representation). *Let $`(\mathcal B,\Sigma,\mu)`$ be a probability space. On $`\mathcal H_\mu=L^2(\mathcal B,\mu)`$, define
``` math
(M_f\psi)(b):=f(b)\psi(b),
 \qquad f\in L^\infty(\mathcal B,\mu).
```
Then $`f\mapsto M_f`$ is a faithful unital $`*`$-representation of $`\mathcal C_\mu`$, the vector $`\mathbf 1\in\mathcal H_\mu`$ represents the expectation state,
``` math
\mathbb E_\mu[f]=\langle\mathbf 1,M_f\mathbf 1\rangle,
```
and
``` math
[M_f,M_g]=0
 \qquad\text{for every }f,g\in\mathcal C_\mu.
```*

</div>

<div class="proof">

*Proof.* Multiplication by an essentially bounded function is a bounded operator on $`L^2`$, with $`M_f^*=M_{\overline f}`$, $`M_fM_g=M_{fg}`$, and $`M_1=I`$. If $`M_f=0`$, then $`f=0`$ almost everywhere, so the representation is faithful. The expectation identity is immediate from the $`L^2`$ inner product, and multiplication operators commute because $`fg=gf`$. ◻

</div>

This is the relevant GNS representation in concrete form. It explains why Hilbert spaces occur naturally in probability theory. It does not turn a commutative algebra into a noncommutative one.

<div id="cor:no-car" class="corollary">

**Corollary 2** (Probability does not supply CCR or CAR). *The data of Theorem <a href="#thm:commutative" data-reference-type="ref" data-reference="thm:commutative">1</a> do not by themselves produce operators satisfying nonzero canonical commutation relations or canonical anticommutation relations. Any such operators require additional algebraic and dynamical input.*

</div>

<div class="proof">

*Proof.* Every represented basin observable lies in a commutative algebra. In particular, all commutators vanish. A CAR algebra also contains odd generators with prescribed anticommutators and a grading. Neither structure is specified by the probability space. ◻

</div>

## Convexity is not coherent superposition

If $`\mu_1`$ and $`\mu_2`$ are probability measures, then
``` math
\mu_t=t\mu_1+(1-t)\mu_2,\qquad 0\leq t\leq1,
```
is a statistical mixture. Expectations depend affinely on $`t`$. Quantum density matrices are also convex, but a coherent vector
``` math
\psi=\alpha\psi_1+\beta\psi_2
```
contains relative phase information that is not determined by the probabilities $`|\alpha|^2`$ and $`|\beta|^2`$. Off-diagonal matrix elements can change interference observables while every diagonal outcome probability remains fixed.

Classical overlap of two probability densities can therefore model ordinary uncertainty or common support. It is not, without a phase-bearing quantum algebra and state, a derivation of interference.

# Why the reverse reconstruction is nonunique

## A two-level witness

The obstruction is visible in the smallest noncommutative example. In $`\mathcal A=M_2(\mathbb C)`$, let
``` math
\mathcal C=\left\{
 \begin{pmatrix}a&0\\0&b\end{pmatrix}:a,b\in\mathbb C
 \right\}
 \cong C(\{0,1\}).
```
For $`t\in[-1/2,1/2]`$, define
``` math
\rho_t=
 \begin{pmatrix}
 1/2&t\\
 t&1/2
 \end{pmatrix}.
```
Each $`\rho_t`$ is a density matrix and gives the same probability $`(1/2,1/2)`$ on $`\mathcal C`$. Yet
``` math
\mathop{\mathrm{tr}}(\rho_t\sigma_x)=2t
```
depends on $`t`$. A fixed classical outcome law therefore leaves a whole interval of quantum coherences undetermined.

<div id="prop:nonselection" class="proposition">

**Proposition 3** (Classical-law nonselection). *There is no rule depending only on a classical probability space $`(\mathcal B,\Sigma,\mu)`$ that uniquely selects an ambient noncommutative $`C^*`$-algebra and state up to physical equivalence.*

</div>

<div class="proof">

*Proof.* The two-level construction already gives distinct states on one fixed noncommutative algebra with the same restriction to its classical diagonal subalgebra. Tensoring with additional noncommutative systems gives further ambient algebras with the same classical restriction. Hence the classical law does not determine either the off-diagonal state data or the full ambient algebra. ◻

</div>

The proposition does not say that classical records are uninformative. Tomography can recover a quantum state when a sufficiently rich family of noncommuting preparations and effects is already defined. That procedure uses a specified quantum model and an informationally complete measurement; it does not infer the quantum model from one classical law.

## What a valid reconstruction would need

To reconstruct a QFT rather than a classical random field, one must provide at least:

1.  a spacetime category or a fixed causal spacetime;

2.  a field equation or local action with a declared domain;

3.  a symplectic or Hermitian solution-space structure;

4.  a CCR, CAR, or other observable algebra;

5.  local covariance, causality, and time-slice maps;

6.  a positive state satisfying the relevant spectrum or Hadamard condition;

7.  for gauge fields, the BRST/BV quotient and physical observables;

8.  for interactions, a renormalized product or controlled continuum construction.

Probability distributions may be outputs of this structure. They cannot replace these eight items. Standard operator-algebraic and locally covariant formulations make these obligations explicit .

# The exact classical-to-quantum interface

## Restriction of a quantum state

Let $`\mathcal A`$ be a unital $`C^*`$-algebra and let $`\mathcal C\subseteq\mathcal A`$ be a unital commutative $`C^*`$-subalgebra. By the Gelfand representation, $`\mathcal C\cong C(K)`$ for a compact Hausdorff spectrum $`K`$.

<div id="thm:interface" class="theorem">

**Theorem 4** (State restriction and extension interface). *The restriction map
``` math
\operatorname{Res}_{\mathcal C}:\mathsf S(\mathcal A)\longrightarrow\mathsf S(\mathcal C),
 \qquad
 \omega\longmapsto\omega|_{\mathcal C},
```
is affine. Every restricted state has a unique probability measure $`\mu_\omega`$ on $`K`$ satisfying
``` math
\omega(c)=\int_K\widehat c(k)\,d\mu_\omega(k),
 \qquad c\in\mathcal C.
```
Conversely, every state on $`\mathcal C`$ has at least one state extension to $`\mathcal A`$. The extension need not be unique.*

</div>

<div class="proof">

*Proof.* Affineness is immediate. The Riesz–Markov representation theorem gives the unique probability measure associated with the positive normalized functional $`\omega|_{\mathcal C}`$. The positive Hahn–Banach state-extension theorem extends any state on a unital $`C^*`$-subalgebra to a state on $`\mathcal A`$ . Nonuniqueness is witnessed by the family $`\rho_t`$ above. ◻

</div>

This theorem is the corrected mathematical meaning of “basin statistics as a shadow of quantum theory.” The arrow from a quantum state to a classical law is exact once the record subalgebra has been chosen. The reverse arrow exists as an extension problem but is generally multivalued.

## POVMs and instruments

A detector need not correspond to a sharp commutative subalgebra. A positive operator-valued measure $`E`$ on an outcome space $`K`$ assigns effects $`E(\Delta)\in\mathcal A`$ to measurable outcome sets. In state $`\omega`$,
``` math
\mu_\omega(\Delta)=\omega(E(\Delta))
```
is a probability measure. A quantum instrument additionally specifies the state update associated with each outcome. Both are physical maps implemented by an interaction, amplification, and record process.

Nothing in this description makes measurement metaphysically privileged. It is a particular coupling between systems that produces a durable classical record. What matters mathematically is the chosen effect or instrument, not the presence of an observer.

## Local compatibility

For a local QFT net $`O\mapsto\mathcal A(O)`$, choose compatible record subalgebras $`\mathcal C(O)\subseteq\mathcal A(O)`$ or local instruments. A net state $`\omega`$ then supplies compatible local probability laws
``` math
\mu_{\omega,O}:=\omega|_{\mathcal C(O)}.
```
If $`O_1\subseteq O_2`$ and the inclusions of record algebras commute with the net inclusions, the restricted laws have the corresponding consistency.

Independent state extensions region by region do not automatically glue to one global net state. Compatibility, causality, and the selected state condition remain global obligations.

# Four kernels that must remain distinct

The earlier paper used the word “propagator” for a classical covariance. Several kernels can have similar formulas while carrying different structures.

<div class="center">

| **Kernel** | Definition or source | What it controls |
|:---|:---|:---|
| **Classical covariance** | $`\mathbb E_\mu[(\rho(x)-\bar\rho(x))(\rho(y)-\bar\rho(y))]`$ | Second moments of a classical random field. |
| **Advanced/retarded Green kernel** | Fundamental solution $`G^\pm`$ of a Green-hyperbolic operator | Causal response and support in $`J^\pm`$. |
| **Quantum two-point function** | $`W_\omega(x,y)=\omega(\phi(x)\phi(y))`$ in a state $`\omega`$ | State correlations, positivity, field equation, and singularity structure. |
| **Feynman kernel** | Time-ordered two-point distribution or perturbative inverse | Perturbative contractions subject to a prescription and state. |

</div>

A classical Gaussian covariance can resemble a Euclidean free-field two-point function. A QFT reconstruction from Euclidean data nevertheless requires additional conditions such as reflection positivity, covariance, regularity, and clustering. In Lorentzian AQFT, the commutator or anticommutator, microlocal spectrum condition, and positivity are separate requirements .

<div class="proposition">

**Proposition 5** (Covariance is not a propagator certificate). *A symmetric positive classical covariance kernel does not by itself determine retarded and advanced Green operators, a quantum commutator or anticommutator, a time-ordered product, or a local observable net.*

</div>

<div class="proof">

*Proof.* The classical covariance contains no causal orientation, field operator, grading, or local-algebra assignment. Distinct quantum states and even distinct field equations can have the same covariance on a restricted commuting record family. The missing structures cannot be recovered from positivity and symmetry alone. ◻

</div>

# Characteristic functionals and path integrals

For a classical random distribution $`\rho`$, the functional
``` math
Z_{\mathrm{cl}}[J]
 =\mathbb E_\mu\!\left[e^{i\rho(J)}\right]
```
is its characteristic functional. Functional derivatives generate classical moments when the derivatives exist. This is useful and exact.

A Lorentzian QFT path integral is not generally a countably additive probability measure with density $`e^{iS}`$. In perturbation theory it is often a compact notation for time-ordered distributions, Wick expansion, gauge fixing, renormalization, and boundary conditions. Euclidean functional measures can be rigorous in selected models, but passage to a Lorentzian QFT uses a reconstruction theorem and its hypotheses.

<div class="proposition">

**Proposition 6** (Generating-functional boundary). *The existence of $`Z_{\mathrm{cl}}`$ supplies classical moments. It becomes evidence for a quantum field theory only after an independent reconstruction verifies the required algebra, causal or Euclidean structure, positivity, and state conditions.*

</div>

This is not a defect of basin statistics. A classical random field may be the right effective model for a detector signal, stochastic environment, hydrodynamic variable, or semiclassical noise source. It should simply be named correctly.

# Coarse-graining, renormalization, and diagrams

## Three different reductions

It is useful to separate:

1.  **statistical marginalization**, which integrates out random variables in a probability measure;

2.  **projection or truncation**, which retains a selected effective subspace or finite set of observables;

3.  **renormalization-group transport**, which changes scale while preserving a declared class of observables through running couplings, counterterms, or effective actions.

They may be combined in one model, but they are not synonyms.

A coherence capacity can control a domain, truncation error, spectral gap, or first-exit margin. It does not alone calculate beta functions. A Wilsonian or perturbative RG flow requires a specified action or local algebra, scale prescription, regulator or subtraction scheme, and matching conditions.

## Where Feynman diagrams come from

Feynman diagrams encode the combinatorics of a perturbative expansion once the free propagator, interaction vertices, grading, time ordering, and renormalization prescription have been specified. Basin correlations can be represented diagrammatically too, as in cumulant or cluster expansions. The visual similarity does not establish equality of the theories.

Within the current MTT Standard-Model branch, the perturbative observable functor uses standard BRST/Faddeev–Popov quantization. That layer is an imported standard-QFT construction composed with the selected carrier, not a derivation of quantization from coherence-basin counting.

# The selected MTT quantum-field source

## The theorem owned by the companion paper

The paper *Modal Triplet Theory and Quantum Field Theory on Curved Spacetime: A Selected Free CAR Net and the Interacting Reconstruction Boundary* owns the current selected free-QFT theorem . Its declared source is a globally hyperbolic framed q79 representative with a global coframe and parallel rank-six carrier. Those data define a zero-order-free twisted massless Dirac operator. Under the standard Green-hyperbolic and CAR/AQFT theorems, the construction gives:

- an even CAR observable net;

- locality, covariance, and the time-slice property;

- a nonempty positive Hadamard state space;

- an exact finite coherent/complement component map.

The independent analytic and algebraic ingredients are standard results for Green-hyperbolic equations, Dirac fields, local covariance, and Hadamard renormalization .

This paper does not reprove or rename that result. It explains how coherence-basin and detector statistics can be attached to it through Theorem <a href="#thm:interface" data-reference-type="ref" data-reference="thm:interface">4</a>. A selected state $`\omega`$ and a record subalgebra or instrument produce the corresponding probability law.

## What is closed and what is not

<div class="center">

| **Object** | Current tier | Meaning for this paper |
|:---|:---|:---|
| **Finite selected quantum model** | Closed | The finite-symbol Cauchy Hilbert/state/observable system and its declared comparison maps are available. |
| **Selected local QFT source** | Closed | The q79 twisted-Dirac even-CAR net supplies the quantum algebra used by the interface. |
| **Basin probability representation** | Exact | Theorem <a href="#thm:commutative" data-reference-type="ref" data-reference="thm:commutative">1</a>; commutative and not a quantum source. |
| **Quantum-to-record restriction** | Exact | Theorem <a href="#thm:interface" data-reference-type="ref" data-reference="thm:interface">4</a>; the reverse extension is nonunique. |
| **Perturbative SM observable functor** | Conditional, imported | Standard BRST/Faddeev–Popov quantization is used rather than derived from MTT. |
| **Finite-domain quantization results** | Conditional, finite domain | Useful controlled results exist, with explicit continuum and gauge obligations. |
| **Nonperturbative interacting QFT** | Open | Requires a geometry-selected gauge-BRST $`C^*`$-bridge or a controlled regulator/continuum limit. |
| **Unique full-branch state** | Open | Nonempty Hadamard state space does not select one physical state. |

</div>

## The interacting boundary

The current interacting program contains a classical BV master action, a gauge-fixed Green-hyperbolic equicausal algebra, a formal all-orders anomaly-free quantum master equation, a formal physical-state functor, and a literal free $`C^*`$-reference net at zero coupling. These are meaningful structural advances.

They do not select a unique fixed-nonzero-coupling $`C^*`$-completion. The current flat-deformation result shows why a formal power-series jet is insufficient: distinct nonperturbative theories can share the same formal expansion. The remaining exit is a same-source nonperturbative gauge-BRST bridge or regulator/continuum limit, followed by state selection, renormalization-group matching, uncertainty control, and observable comparison.

# Physical interpretation without overclaiming

## What basin variables can mean

A coherence basin may serve as:

- a classical label for a stable projected configuration;

- a preparation class;

- a detector-record class;

- a coarse-grained feature of a quantum state;

- a semiclassical or stochastic effective variable.

These roles are not automatically identical. Each application should name the source map and the observable domain.

In particular, a particle in QFT is not generally a localized classical basin. Particle interpretations depend on representations, asymptotic structure, or detector models, especially in curved spacetime. A basin may encode a stable effective particle-like regime while the local quantum field remains the algebraic source of correlations.

## Measurement as a physical interface

A measurement is an interaction that correlates a system with an apparatus and produces a record. In the algebraic description, an effect or instrument maps a state to outcome probabilities and conditional states. In the basin description, the same output may be represented by a probability measure over stable records.

This does not make measurement the act that creates reality. It identifies the precise physical channel at which noncommutative state information is converted into a commutative record law. Whether MTT supplies a deeper same-source capture dynamics is a separate theorem.

## Ontology remains optional

The mathematics is compatible with several ontological readings. One may treat quantum fields as fundamental, as effective local observables, or as linear shadows of deeper closure dynamics. The interface theorem does not decide among those readings. It does decide a mathematical point: a classical ensemble does not uniquely determine the noncommutative theory above it.

# Validation program

A proposed basin-to-QFT model should provide the following certificate.

1.  **Basin domain:** the measurable or topological configuration space and the meaning of its points.

2.  **Probability source:** a preparation law, state restriction, instrument, or dynamical derivation of $`\mu`$.

3.  **Quantum source:** the field operator, solution structure, and CCR/CAR or local algebra.

4.  **Interface map:** the commuting subalgebra, POVM, instrument, or channel producing the basin records.

5.  **State condition:** positivity and the appropriate spectrum, Hadamard, KMS, or asymptotic condition.

6.  **Causal control:** locality, covariance, and time-slice behavior.

7.  **Interaction control:** BV/BRST identities, renormalization, continuum or nonperturbative construction, and uncertainty estimates.

8.  **Observable comparison:** a prediction not used to select the source data.

The model is falsified at its declared tier if the record law cannot be obtained from the selected state and interface, if the claimed local net violates causality or positivity, if a stated state is not Hadamard on the declared spacetime, or if the controlled observable comparison fails.

# Discussion

## What the correction gains

The earlier claim was rhetorically broad but mathematically incomplete:
``` math
\text{basin measure}
 \;\not\Longrightarrow\;
 \text{noncommutative QFT}.
```
The corrected picture has more structure:
``` math
\begin{gathered}
\text{q79 geometry}
\longrightarrow
\text{Dirac source}
\longrightarrow
\text{free CAR net},\\
\text{state + physical record channel}
\longrightarrow
\text{basin statistics}.
\end{gathered}
```
Every arrow now has a type. The free quantum source is not inferred from a classical covariance. The statistical layer is not discarded; it is placed where it can be exact.

## Why this is still an MTT result

The correction does not reduce the paper to a generic textbook observation. The generic theorems identify the only valid interface. Current MTT research supplies a selected source on one side of that interface: the q79 twisted-Dirac free CAR net. MTT also supplies finite projection and apparatus maps on declared domains. The typed upper/coherent/effective distinction and the exact limits of projection claims are stated in the revised foundation and projection papers . The combined statement is therefore specific:

> The selected free MTT quantum-field source can emit ordinary basin and detector statistics through compatible record maps, but those statistics do not independently reconstruct the source.

That statement is stronger than the old statistical analogy because it names the quantum object being represented. It is narrower than a full QFT derivation because the interacting completion and unique state selection remain open.

## The best next theorem

The next major step is not another Hilbert representation of classical probability. It is a same-source construction that carries the selected q79 geometry through:
``` math
\begin{gathered}
 \text{interacting BV/BRST data}
 \longrightarrow
 \text{physical gauge-invariant }C^*\text{-net}\\
 \longrightarrow
 \text{selected state and record instrument}.
\end{gathered}
```
with a regulator or renormalized pushforward that preserves the quantum master equation, locality, positivity, and the observable comparison in the continuum limit.

# Conclusion

Coherence-basin statistics possess a natural Hilbert-space representation, but it is a commutative one. They support expectations, mixtures, covariances, characteristic functionals, and classical coarse-graining. They do not by themselves supply quantum phases, CCR/CAR relations, time-ordered propagators, local nets, gauge reduction, or renormalized interactions.

The correct bridge is an interface. A quantum state restricts to an exact classical probability law on a commuting record algebra or through an instrument. Classical states extend back to the ambient algebra, but generally in many inequivalent ways. The reverse reconstruction is therefore nonunique.

For current MTT, this interface attaches to a real selected result: the free q79 twisted-Dirac even-CAR net with locality, covariance, time-slice behavior, and positive Hadamard states. The interacting nonperturbative gauge-BRST $`C^*`$-completion, selected full-branch state, RG matching, and precision comparison remain the frontier. This is the defensible achievement of the revised paper: not QFT from statistics alone, but a typed and testable connection between a selected quantum-field source and its classical coherence-basin records.
