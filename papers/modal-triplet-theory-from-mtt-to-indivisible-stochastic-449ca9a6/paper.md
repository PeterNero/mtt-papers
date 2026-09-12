---
abstract: |
  This paper gives a measure-theoretic account of stochastic processes obtained by projecting an upper Modal Triplet Theory (MTT) evolution. Given a selected probability law on upper initial data, measurable upper dynamics, and an observable map, the projected histories carry a unique path-space law. Regular conditional kernels then exist on standard Borel state spaces. The observed process may fail to be Markovian even when the upper process is Markovian or deterministic. We distinguish four statements that were previously conflated: failure of the Markov property on the observed state space, absence of finite Markov order, failure of a chosen Chapman–Kolmogorov reduction, and quantum CP-indivisibility. Every classical path law still factorizes sequentially through its history-dependent conditional kernels and becomes Markovian on a history state space. An exact binary hidden-state example shows that projection can create infinite observed Markov order while the memory remains compressible to one posterior scalar. Exponential action weights define valid kernels when their action and reference measure are supplied, but writing a positive kernel in Gibbs form is a parameterization, not a first-principles prediction. Finally, a commutative path-space algebra does not derive noncommutative quantum observables, process tensors, Born probabilities, or quantum instruments. This limitation does not reopen the separately established canonical operational q79 model. We explain its relation to coherent history witnesses, frozen finite hierarchical-equations-of-motion calculations, and bounded optical readout. A charged molecular line and conditional geometric repair provide further comparison structures, but neither an abstract intertwiner nor a fitted response selects a physical q79–FMO correspondence. The remaining physical obligations are a same-source preparation and intervention model, controlled observable transport, calibration, and an independently fixed clock.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: September 2026 (v3)
generated_from_main_tex_sha256: 7c0c28e644a84d251576c57ca52a0e62b38389c29d9a0b7db2670d95782f4be2
paper_id: modal-triplet-theory-from-mtt-to-indivisible-stochastic-449ca9a6
release_state: current_revised_tex
released_version: v2
title: |
  Modal Triplet Theory and History-Dependent Stochastic Processes:
  Fixed-State Indivisibility, Markov Order, and the Quantum Boundary
zenodo_doi: 10.5281/zenodo.21665996
zenodo_record_id: 21665996
zenodo_url: "https://zenodo.org/records/21665996"
---

# Modal Triplet Theory and History-Dependent Stochastic Processes: Fixed-State Indivisibility, Markov Order, and the Quantum Boundary

Peter Nero. September 2026 (v3)

## Abstract

This paper gives a measure-theoretic account of stochastic processes obtained by projecting an upper Modal Triplet Theory (MTT) evolution. Given a selected probability law on upper initial data, measurable upper dynamics, and an observable map, the projected histories carry a unique path-space law. Regular conditional kernels then exist on standard Borel state spaces. The observed process may fail to be Markovian even when the upper process is Markovian or deterministic. We distinguish four statements that were previously conflated: failure of the Markov property on the observed state space, absence of finite Markov order, failure of a chosen Chapman–Kolmogorov reduction, and quantum CP-indivisibility. Every classical path law still factorizes sequentially through its history-dependent conditional kernels and becomes Markovian on a history state space. An exact binary hidden-state example shows that projection can create infinite observed Markov order while the memory remains compressible to one posterior scalar. Exponential action weights define valid kernels when their action and reference measure are supplied, but writing a positive kernel in Gibbs form is a parameterization, not a first-principles prediction. Finally, a commutative path-space algebra does not derive noncommutative quantum observables, process tensors, Born probabilities, or quantum instruments. This limitation does not reopen the separately established canonical operational q79 model. We explain its relation to coherent history witnesses, frozen finite hierarchical-equations-of-motion calculations, and bounded optical readout. A charged molecular line and conditional geometric repair provide further comparison structures, but neither an abstract intertwiner nor a fitted response selects a physical q79–FMO correspondence. The remaining physical obligations are a same-source preparation and intervention model, controlled observable transport, calibration, and an independently fixed clock.

# Revision note: v3

#### Supersedes.

Version 3 supersedes v2 (July 2026; Zenodo record 21665996). The earlier revision note below is retained as a record of that correction, not as the current status of every quantum-source question.

#### Reason.

The classical account predates the canonical operational q79 source and the subsequent BEQ coherent-history, readout, charged-line, and repair results. Its blanket quantum-source boundary and older corpus ledger were stale.

#### Resolution.

The new contextual sections distinguish exact constructions, finite numerical profiles, excluded realizations, conditional comparisons, and physical source selection. They explain all 48 assigned frozen results, including later refinements inside the evolving candidate audit. The transported-metric semigroup estimate now states its common-norm assumptions explicitly.

#### Retained.

The classical projection and Markovization proofs, the posterior-memory example, and measurement as ordinary physical intervention are retained. No finite q79 or canonical operational quantum conclusion is reopened.

#### Open boundary.

The physical molecular correspondence, selected nonflat endpoint, detector and source uncertainty, bounded bath-active realization, and dimensionful clock remain separate obligations. Pure positive repair is not the selected physical signed action. Reading frozen certificates is not an independent scientific rerun.

# Revision note

#### Supersedes.

Version 2 supersedes the January 2026 release associated with Zenodo record 18254863.

#### Reason.

The former version called the construction complete and first-principles while assuming its probability source. It also inferred indivisibility from history dependence, treated exact realization of a prescribed kernel as an MTT prediction, and used a commutative GNS representation as if it supplied general quantum instruments.

#### Resolution.

This version replaces those claims by a conditional projection theorem, separates Markov order from classical and quantum divisibility, proves history-space Markovization, and distinguishes a physical intervention from Bayesian conditioning. It also replaces the inconsistent product of three three-manifolds by the current upper-space notation $`Y^4\times X^6`$, with the $`1<2<3`$ lanes understood as operator data on a shared carrier.

#### Retained content.

The valid path-space construction, the possibility of projection-induced memory, normalized history-dependent kernels, and ordinary conditional probability are retained with explicit hypotheses.

#### Remaining boundary.

MTT must still select an upper capture or preparation law, derive any proposed action-weight kernel from the same branch, rule out finite sufficient-state compression when infinite memory is claimed, and provide a noncommutative observable and instrument source before quantum-process conclusions follow.

# Introduction: what projection can and cannot do

The central idea of this paper is simple. A lower observer may see only a coarse variable $`q_k`$, while an upper state $`z_k`$ contains additional information. Even if the upper evolution is deterministic, two upper states with the same present value of $`q_k`$ can have different futures. An ensemble of such upper states therefore produces an observed process whose prediction depends on more than the present observed value.

This is a standard and important mechanism. Hidden Markov models, coarse graining, and open-system reductions all exhibit it. MTT gives the mechanism a geometric interpretation: the observed record is a projection of a richer fixed-point and bundle state. The geometry can therefore be a source of memory in the projected description.

The mechanism alone, however, does not supply probabilities. A deterministic map and a projection produce a single history from a single initial state. To obtain a probability law one must additionally specify a distribution over initial states, a stochastic upper transition rule, or some other selected capture measure. This distinction is the main logical boundary of the revised paper.

## Four notions that must be kept separate

The word “indivisible” is used in several inequivalent ways. We distinguish:

1.  failure of the one-step Markov property on the observed state space $`Q`$;

2.  absence of every finite Markov order on $`Q`$;

3.  failure of a specified two-time family to satisfy a Chapman–Kolmogorov composition law on $`Q`$;

4.  failure of CP-divisibility for a family of quantum channels.

The first three are classical properties. The fourth requires a noncommutative operator system and completely positive maps. It cannot be deduced from a classical path law alone. Modern process-tensor treatments make this operational distinction explicit \[[52](#ref-pollock2018framework),[53](#ref-pollock2018markov),[54](#ref-rivas2010)\].

## Claim map

<div class="center">

| Statement | Status in this paper |
|:---|:---|
| Selected upper law plus dynamics and projection define a path law | Proved. |
| Projection can destroy the Markov property on $`Q`$ | Proved conditionally and illustrated exactly. |
| History dependence proves absolute indivisibility | False; replaced by history-space Markovization. |
| Complete-past dependence proves irreducible infinite memory | False without excluding finite sufficient statistics. |
| $`\exp(-\Delta A/\eta)`$ defines a kernel | Proved when $`\Delta A,\eta`$, and a reference measure are supplied. |
| Every positive kernel has an action representation | True but tautological; it is not a prediction. |
| Classical conditioning is a quantum instrument | False without a noncommutative source theorem. |
| Canonical operational q79 source | Established at its finite-symbol, binary, one-anchor tier. |
| Physical q79–FMO preparation and intervention source | Open; compatibility and finite readout do not select it. |

</div>

# The corrected MTT input

## Upper geometry

The stochastic theorem does not require a literal product of three independent three-manifolds. We use the current branch notation
``` math
M=Y^4\times X^6,
```
where $`Y^4`$ is the external spacetime and $`X^6`$ is the selected compact internal geometry when such a branch has been supplied. The Circle–Lens–Nil $`1<2<3`$ structure is treated as a rank or operator filtration on a shared carrier. In particular, its lane count is not added as $`4+3+3+3`$, which would be thirteen rather than ten.

For the probability theory below, all geometric and field data are collected into an upper state space $`(\mathcal{Z},\mathcal{B}(\mathcal{Z}))`$. This may include fields on $`Y^4\times X^6`$, bundle connections, fixed-point data, recorder variables, and any finite source coordinates. We assume $`\mathcal{Z}`$ is a standard Borel space. Let
``` math
T:\mathcal{Z}\longrightarrow\mathcal{Z}
```
be one step of the selected upper evolution, and let
``` math
\pi:\mathcal{Z}\longrightarrow Q
```
be the measurable observable or recorder map into a standard Borel space $`Q`$.

## Where probability enters

A probability measure $`\rho`$ on $`\mathcal{Z}`$ is an additional datum. It may represent a preparation ensemble, a capture measure on basins, uncertainty in unobserved upper variables, or a genuinely stochastic source. Those physical interpretations are different, but the mathematical construction begins only after $`\rho`$ has been specified.

<div id="thm:projected-law" class="theorem">

**Theorem 2.1** (Projected path law). *Let $`\mathcal{Z}`$ and $`Q`$ be standard Borel spaces, let $`T:\mathcal{Z}\to\mathcal{Z}`$ and $`\pi:\mathcal{Z}\to Q`$ be measurable, and let $`\rho`$ be a probability measure on $`\mathcal{Z}`$. Define
``` math
\Gamma(z)=\bigl(\pi(z),\pi(Tz),\pi(T^2z),\ldots\bigr)\in Q^{\mathbb{N}}.
```
Then $`\Gamma`$ is measurable and
``` math
\mu:=\Gamma_{\ast}\rho
```
is a unique probability measure on $`(Q^{\mathbb{N}},\mathcal{B}(Q)^{\otimes\mathbb{N}})`$. Its coordinate process $`Q_k(\omega)=\omega_k`$ is the stochastic shadow of the upper ensemble.*

</div>

<div class="proof">

*Proof.* Every coordinate $`\pi\circ T^k`$ is measurable. The product sigma-algebra is generated by coordinate cylinders, hence $`\Gamma`$ is measurable. The pushforward of a probability measure under a measurable map is a probability measure and is uniquely defined by $`\mu(C)=\rho(\Gamma^{-1}C)`$. ◻

</div>

<div class="remark">

*Remark 2*. If $`\rho=\delta_{z_0}`$, then $`\mu`$ is concentrated on one path. Neither projection nor fixed-point dynamics turns that Dirac law into a nontrivial probability distribution. This is why the capture or preparation law is a real source obligation rather than a technical detail.

</div>

<a id="sec:recurrence-boundary"></a>

## Finite phase recurrence is not irreversible mixing

For a closed finite-mode self-adjoint phase generator, matrix coefficients of unitary evolution are finite sums of oscillatory exponentials. They are almost periodic, not decaying mixing correlations. With compact resolvent, the same recurrence conclusion holds for individual vectors by approximation with finite spectral sums. Compact resolvent alone does not turn these reversible phases into a physical stochastic driver.

This is not a no-go for finite dissipative models: a supplied Markov or Lindblad generator can mix, and a positive repair heat semigroup can decay. Those are different dynamics. Deriving irreversible stochastic behavior from a closed microscopic phase model requires a controlled continuum, bath, weak-coupling, or thermodynamic limit with its state, observables, scaling, and error bounds specified. The finite HEOM comparisons below are calculations within a supplied bath model, not that derivation \[[39](#ref-beq04),[23](#ref-beq06)\]. The selected physical driver construction remains a B.ACTION.01 obligation, without reopening the canonical operational model.

# Conditional kernels and action weights

## Construction from kernels

One may equivalently start with an initial law $`\lambda_0`$ on $`Q`$ and a sequence of measurable probability kernels
``` math
K_k(\,\cdot\,|h_k),\qquad h_k=(q_0,\ldots,q_k)\in Q^{k+1}.
```
The next theorem is standard probability theory \[[51](#ref-kallenberg2002)\].

<div id="thm:IT" class="theorem">

**Theorem 3.1** (Ionescu–Tulcea extension). *For every initial probability measure $`\lambda_0`$ and sequence of probability kernels $`K_k`$ from $`Q^{k+1}`$ to $`Q`$, there is a unique probability measure $`\mu`$ on $`Q^{\mathbb{N}}`$ whose finite-dimensional distributions satisfy
``` math
\begin{split}
&\mu(Q_0\in A_0,\ldots,Q_n\in A_n)\\
&\quad =
\int_{A_0}\lambda_0(dq_0)
\int_{A_1}K_0(dq_1|q_0)\cdots
\int_{A_n}K_{n-1}(dq_n|q_0,\ldots,q_{n-1}).
\end{split}
```*

</div>

Conversely, because $`Q`$ is standard Borel, the law in [2.1](#thm:projected-law) admits regular conditional distributions
``` math
K_k(A|Q_0,\ldots,Q_k)
=\mu(Q_{k+1}\in A\mid Q_0,\ldots,Q_k)
```
for every $`k`$, unique up to the usual null sets. Thus every path law factorizes sequentially through history-dependent kernels. A claim that a path law has no such factorization is therefore incorrect.

## A selected action kernel

Let $`\nu`$ be a sigma-finite reference measure on $`Q`$, let $`\eta>0`$, and let
``` math
\Delta A_k:Q^{k+1}\times Q\longrightarrow\mathbb{R}\cup\{+\infty\}
```
be jointly Borel. Define
``` math
Z_k(h_k)=\int_Q
\exp\!\left[-\frac{\Delta A_k(h_k,q')}{\eta}\right]\nu(dq').
```

<div id="lem:action-kernel" class="lemma">

**Lemma 3.2** (Normalized action kernel). *On the Borel set $`G_k=\{h_k:0<Z_k(h_k)<\infty\}`$, the expression
``` math
K_k(A|h_k)=\frac{1}{Z_k(h_k)}
\int_A\exp\!\left[-\frac{\Delta A_k(h_k,q')}{\eta}\right]\nu(dq')
```
is a measurable probability kernel. Extend it outside $`G_k`$ by any fixed probability measure. If every reachable history lies in $`G_k`$, this extension does not change the intended process. Together with an initial law the extended kernel defines a unique path measure by [3.1](#thm:IT).*

</div>

<div class="proof">

*Proof.* Nonnegativity and normalization are immediate. Measurability of parameterized nonnegative integrals follows from joint Borel measurability; division is measurable because $`Z_k`$ is finite and strictly positive. ◻

</div>

This result is exact, but it begins with $`\Delta A_k`$, $`\eta`$, and $`\nu`$. Calling $`\eta=\hbar`$ is a physical identification, not a consequence of normalization. Likewise, a Euclidean exponential weight is not the complex phase $`e^{iS/\hbar}`$ and does not by itself produce quantum interference.

<div id="lem:gibbs" class="lemma">

**Lemma 3.3** (Gibbs form is a parameterization). *Suppose $`K_k(\cdot|h_k)`$ has a strictly positive normalized density $`k_k(\cdot|h_k)`$ with respect to $`\nu`$. For any $`\eta>0`$, setting
``` math
\Delta A_k(h_k,q')=-\eta\log k_k(q'|h_k)
```
reproduces $`K_k`$ through [3.2](#lem:action-kernel), with $`Z_k=1`$. Adding an arbitrary history-dependent constant to $`\Delta A_k`$ leaves the normalized kernel unchanged.*

</div>

<div class="proof">

*Proof.* Exponentiation gives $`e^{-\Delta A_k/\eta}=k_k`$, and the density is already normalized. A history-only constant multiplies numerator and denominator by the same factor. ◻

</div>

[3.3](#lem:gibbs) is useful for fitting or encoding a known kernel. It cannot show that MTT geometry selected that kernel. Exact reconstruction of arbitrary target kernels demonstrates expressive capacity; prediction requires a rule that fixes the action before the target data are supplied.

# Markov order and fixed-state indivisibility

## Precise definitions

Let $`\mathcal{F}_k=\sigma(Q_0,\ldots,Q_k)`$.

<div id="def:markov-order" class="definition">

**Definition 4.1** (Markov order). The process has Markov order at most $`r\geq 1`$ if, for every $`k\geq r-1`$, there is a kernel $`L_k`$ such that
``` math
\mathbb{P}(Q_{k+1}\in A\mid\mathcal{F}_k)
=L_k(A|Q_{k-r+1},\ldots,Q_k)
\quad\text{a.s.}
```
for every Borel $`A`$. It has infinite Markov order on $`Q`$ if no finite $`r`$ has this property.

</div>

<div id="def:q-indivisible" class="definition">

**Definition 4.2** (Fixed-$`Q`$ indivisibility). For this paper only, a process is *fixed-$`Q`$ indivisible* if its complete finite-dimensional distributions cannot be generated by one-step kernels depending only on the current value $`q_k`$. This is simply failure of Markov order one on the chosen observed state space. It is not quantum CP-indivisibility.

</div>

<div id="prop:factorization" class="proposition">

**Proposition 4.3** (Factorization criterion). *A path law is Markov of order one on $`Q`$ if and only if there are kernels $`M_k(dq_{k+1}|q_k)`$ for which every finite-dimensional law factorizes as
``` math
\lambda_0(dq_0)\prod_{k=0}^{n-1}M_k(dq_{k+1}|q_k).
```
Consequently, fixed-$`Q`$ indivisibility is exactly a statement about the chosen state description $`Q`$, not about the impossibility of sequential factorization.*

</div>

<div class="proof">

*Proof.* The forward implication is [3.1](#thm:IT) applied to Markov kernels. For the reverse implication, disintegration of the displayed law gives a version of the conditional law of $`Q_{k+1}`$ that depends only on $`Q_k`$. ◻

</div>

## Every process is Markov on its history state

<div id="thm:history-markov" class="theorem">

**Theorem 4.4** (History-state Markovization). *Let $`\mu`$ be any path law on a standard Borel space $`Q`$, with conditional kernels $`K_k`$. Define
``` math
\mathcal{H}=\bigsqcup_{k\geq0}\{k\}\times Q^{k+1},
\qquad
H_k=(k,Q_0,\ldots,Q_k).
```
Then $`H_k`$ is a first-order Markov process on $`\mathcal{H}`$. Its transition from $`(k,h_k)`$ appends $`q'`$ with law $`K_k(dq'|h_k)`$.*

</div>

<div class="proof">

*Proof.* Given $`H_k`$, the complete observed past is known. The conditional distribution of $`H_{k+1}`$ is therefore the pushforward of $`K_k(\cdot|h_k)`$ under $`q'\mapsto(k+1,h_k,q')`$, and depends on no earlier history state. ◻

</div>

This theorem is not a trick that removes physically relevant memory. It tells us what must be measured: the size and structure of the state required to make the process Markovian. A useful non-Markovianity claim should therefore rule out a small sufficient state, not merely observe that $`q_k`$ alone is insufficient.

<div id="prop:sufficient" class="proposition">

**Proposition 4.5** (Sufficient-state compression). *Suppose there is a standard Borel space $`S`$, measurable summaries $`s_k:Q^{k+1}\to S`$, update maps
``` math
s_{k+1}(h_k,q')=u_k(s_k(h_k),q'),
```
and kernels $`L_k`$ such that
``` math
K_k(\cdot|h_k)=L_k(\cdot|q_k,s_k(h_k)).
```
Then $`(Q_k,S_k)`$, with $`S_k=s_k(Q_0,\ldots,Q_k)`$, is first-order Markov. Complete-past notation therefore does not prove irreducible or infinite-dimensional memory.*

</div>

<div class="proof">

*Proof.* The next $`Q`$-value depends only on $`(Q_k,S_k)`$, and the next summary is a measurable function of $`(S_k,Q_{k+1})`$. Hence the joint next-state law depends only on the current augmented state. ◻

</div>

The proposition permits any standard Borel $`S`$. Calling the compression finite requires a specified finite-state or finite-dimensional class of summaries; measurable encoding alone is not a physical memory-size bound.

# An exact projection-induced memory example

<div id="ex:binary" class="example">

**Example 5.1** (Binary latent source). Let $`S\in\{0,1\}`$ be chosen with equal prior probabilities and remain fixed. Conditional on $`S`$, let $`Q_0,Q_1,\ldots`$ be independent with
``` math
\mathbb{P}(Q_k=S|S)=1-\varepsilon,\qquad
\mathbb{P}(Q_k\neq S|S)=\varepsilon,
\qquad 0<\varepsilon<\frac12.
```
The upper state includes $`S`$; the observer records only $`Q_k`$.

</div>

For a history $`h_k=(q_0,\ldots,q_k)`$, write $`n_1`$ and $`n_0`$ for the numbers of ones and zeros. Bayes’ rule gives
``` math
p_k:=\mathbb{P}(S=1|h_k)
=\frac{(1-\varepsilon)^{n_1}\varepsilon^{n_0}}
{(1-\varepsilon)^{n_1}\varepsilon^{n_0}
 +\varepsilon^{n_1}(1-\varepsilon)^{n_0}},
```
and therefore
``` math
\mathbb{P}(Q_{k+1}=1|h_k)
=\varepsilon+(1-2\varepsilon)p_k.
```

<div id="prop:binary" class="proposition">

**Proposition 5.2** (Infinite observed order, one-scalar memory). *The process in [5.1](#ex:binary) has no finite Markov order on $`Q=\{0,1\}`$. Nevertheless, the scalar posterior $`p_k`$ is a sufficient state, so the observed memory is recursively compressible to one real number.*

</div>

<div class="proof">

*Proof.* Fix any proposed order $`r`$. Choose two positive-probability histories with the same final $`r`$ symbols but with sufficiently many additional ones in one prefix and zeros in the other. Their values of $`n_1-n_0`$, hence their posteriors $`p_k`$, differ. Their next-symbol probabilities therefore differ, so no order-$`r`$ kernel can represent both histories.

For compression, after observing $`q\in\{0,1\}`$, Bayes’ rule updates $`p`$ by
``` math
u(p,q)=
\frac{p(1-\varepsilon)^q\varepsilon^{1-q}}
{p(1-\varepsilon)^q\varepsilon^{1-q}
 +(1-p)\varepsilon^q(1-\varepsilon)^{1-q}}.
```
The next prediction depends only on $`p_k`$, and $`p_{k+1}=u(p_k,Q_{k+1})`$. Apply [4.5](#prop:sufficient). ◻

</div>

This example captures both the promise and the warning for MTT. Projection can genuinely produce observed infinite-order memory. Yet an upper hidden coordinate, or even a one-dimensional posterior over it, can restore a Markov description. A claim of irreducible MTT memory must therefore prove that no allowed finite recorder state or sufficient statistic closes the evolution.

# The classical–quantum boundary

## What classical GNS does

Let $`(\Omega,\mathcal{F},\mu)`$ be the path space. Bounded classical observables form the commutative algebra $`L^\infty(\Omega,\mu)`$. Acting by multiplication on $`L^2(\Omega,\mu)`$, an event $`E`$ is represented by the projection
``` math
(M_Ef)(\omega)=\mathbf{1}_E(\omega)f(\omega),
```
and
``` math
\mu(E)=\langle \mathbf{1},M_E\mathbf{1}\rangle.
```
This has the appearance of a Born formula, but all $`M_E`$ commute.

<div id="prop:commutative" class="proposition">

**Proposition 6.1** (Commutative reconstruction limit). *The GNS representation of a commutative path-space algebra has a commuting operator image. It does not, without extra structure, produce incompatible observables, complex interference amplitudes, a noncommutative state algebra, or general completely positive instruments.*

</div>

<div class="proof">

*Proof.* If $`ab=ba`$ in the algebra, then every representation satisfies $`\pi(a)\pi(b)=\pi(ab)=\pi(ba)=\pi(b)\pi(a)`$. The missing noncommutative objects cannot be obtained by relabeling commuting multiplication operators. ◻

</div>

Ordinary sigma-additivity also implies that the probability of a fixed measurable event is unchanged when a partition is refined around it. That is a consistency property of one classical sample space, not by itself the operational measurement noncontextuality used in quantum-foundational theorems \[[55](#ref-spekkens2005)\].

## Why quantum divisibility is separate

Quantum CP-divisibility concerns a family of channels $`\Lambda_{t:s}`$ for which
``` math
\Lambda_{t:r}=\Lambda_{t:s}\Lambda_{s:r}
```
with the intermediate map completely positive and trace preserving. A process tensor goes further by mapping sequences of interventions to outcome statistics. Both notions require noncommutative input and output systems and an intervention calculus \[[52](#ref-pollock2018framework),[53](#ref-pollock2018markov)\].

A classical kernel can agree numerically with the probabilities of one chosen quantum experiment. Such agreement does not identify its updates with all quantum instruments or establish CP-divisibility. The classical construction does not supply those structures. A separate canonical q79 construction now does so at its declared operational tier, as explained next; extending that model to a selected molecular preparation and detector is a different task.

<a id="sec:q79-source"></a>

## The established operational q79 source

The frozen source-base result imports a noncommutative model on $`\mathcal{H}_\Sigma=L^2(\Sigma,d\mu_h;F_{q79})`$, with positive trace-class states and a bounded completion of the decomposable observable algebra. Its binary finite-symbol generator is
``` math
\overline{\mathcal L}(\rho)=\log(448)
 \bigl(P\rho P+Q\rho Q-\rho\bigr),\qquad Q=I-P.
```
The construction includes the preparation-ensemble second-moment and ready Fock finite-horizon structure at the canonical one-anchor tier. These are not inferred from commuting path events or fitted observed frequencies \[[8](#ref-beq46)\]. The theorem here remains a classical theorem; the existence of that separate source prevents its limitation from being misreported as a failure of operational MTT quantum mechanics.

An elementary compatibility model further illustrates the distinction. The nilpotent matrix $`d=E_{12}`$ on a three-dimensional carrier has $`d^\dagger d+dd^\dagger=\operatorname{diag}(1,1,0)`$. Exact changes of basis give the q79 Hodge split and a route-cycle split. This is an explicit compatibility square, not a uniqueness theorem selecting a biological Hamiltonian. In particular the full natural q79 unital dephasing generator is not the full natural FMO HEOM generator. The source’s corresponding no-go is retained; a future restricted observable comparison has a different type \[[20](#ref-beq47)\].

# Measurement: intervention first, conditioning second

Measurement has no special metaphysical status here. It is an ordinary physical interaction involving a system, an apparatus, and an outcome record. Probability theory describes two different operations:

1.  an *intervention* changes the physical transition law because the apparatus is coupled to the system;

2.  *conditioning* updates the probability law after an outcome has been learned.

To represent the first operation classically, let $`a_k`$ denote an apparatus setting and use an intervention-dependent kernel
``` math
K_k^{a_k}(dq_{k+1},dy_k|h_k),
```
where $`y_k`$ is the record. The experimental protocol and these kernels define a path law. After observing $`Y_k=y`$, the posterior is the ordinary conditional measure
``` math
\mu^{a,y}(B)=\frac{\mu^a(B\cap\{Y_k=y\})}
{\mu^a(Y_k=y)}
```
when the denominator is nonzero.

Replacing the physical intervention by posterior conditioning loses disturbance information. Conversely, conditioning on a later event can alter the inferred distribution of earlier variables, so no-signaling does not follow from conditioning alone. Operational no-signaling requires the remote marginal to be independent of the local intervention after local outcomes are averaged. That is a locality condition on the instrument kernels, consistent with the corrected spatial Bell analysis, not a generic property of a path measure.

<a id="sec:coherent-history"></a>

# A coherent history is more than an endpoint record

The q79–FMO comparison makes the preceding distinction operational. FMO denotes the Fenna–Matthews–Olson complex. The BEQ calculations considered here are frozen models of its excitonic and optical response, not biological measurements and not a derivation of their molecular parameters from MTT.

<a id="sec:route-witness"></a>

## Two projectors with different jobs

For the oriented three-edge route graph, set
``` math
B=\begin{pmatrix}-1&-1&0\\0&1&-1\\1&0&1\end{pmatrix},\quad
c=\frac{(-1,1,1)^T}{\sqrt3},\quad P_c=cc^\dagger.
```
Then $`B^\dagger B/3=I-P_c`$. The sign matrix $`D=\operatorname{diag}(-1,1,1)`$ carries the q79 Haar projector to $`P_c`$. A different route-outcome unitary carries the q79 rank-one/rank-two split to the direct/indirect route split. These are not interchangeable observables: the cycle projector does not commute with the direct-route projector. A postselected two-dimensional route-label space cannot contain an isometric copy of the full three-dimensional carrier \[[19](#ref-beq02)\].

For example, the cycle witness $`\{P_c,I-P_c\}`$ gives probabilities $`1`$, $`1/3`$, and $`1/9`$ on the cycle state, the equal incoherent mixture, and the all-plus pure state, respectively. Yet the first two states have the same coarse endpoint populations $`(2/3,1/3)`$. Population agreement therefore cannot identify coherent histories. The exploratory lift $`\sqrt{k}=1/\sqrt{\tau}`$ of route rates gives direct weight $`\tau_{41}/(\tau_{41}+\tau_{42}+\tau_{21})`$; its one-third condition is $`2\tau_{41}=\tau_{42}+\tau_{21}`$. This is a declared rate-to-amplitude diagnostic, not a derived quantum generator or a statistical confidence interval \[[19](#ref-beq02),[12](#ref-beq03)\].

For a positive history operator $`\sigma=\Upsilon\star T_H`$, the tester must preserve the coherent history labels, and its capture $`p_{\rm cap}=\operatorname{tr}\sigma`$ must be positive before conditioning. Writing $`\rho_H=\sigma/p_{\rm cap}`$, witness fidelity $`\operatorname{tr}(P_c\rho_H)\geq1-\epsilon^2`$ implies trace distance at most $`\epsilon`$ from the cycle state, hence at most $`\epsilon`$ total-variation error for every subsequent measurement. Capture and conditional fidelity are separate experimental quantities; successful postselection alone establishes neither \[[12](#ref-beq03)\].

<a id="sec:heom-history"></a>

## What the frozen HEOM calculation supplies

The hierarchical equations of motion (HEOM) retain auxiliary density operators (ADOs) as well as the reduced density matrix. The supplied seven-site, 300 K reference compares a declared finite set of hierarchy depths $`D`$ and bath-expansion orders $`K`$. Its one-time density-matrix checks are useful baselines but do not determine an intervention-dependent multi-time process \[[39](#ref-beq04)\].

The later history calculation starts in exciton 4, tags at 50 fs and 100 fs, and retains the ordered histories $`(1,1),(2,2),(2,1)`$. Exciton eigenvectors and both tag phases are transported in the same locked gauge. Applying the tag on both sides of every ADO before subsequent propagation retains system–bath memory that a reduced-state-only reset would discard. At the reported $`D6,K1`$ rung the capture is approximately $`0.08027944`$, while the conditioned cycle witness is approximately $`0.29475899`$. Thus the ideal cycle prediction and this specified standard model are separated, not experimentally discriminated \[[46](#ref-beq05)\].

The four-history ADO process slice retains $`(1,1),(1,2),(2,1),(2,2)`$ and directly composes 15 CP settings. Its selected three-history block reproduces the preceding witness and capture, with the reported finite depth and bath comparisons below their locked tolerance. This resolves the earlier packet’s missing multi-time calculation at this slice, not full process-tensor tomography. Ground-state bleach (GSB), stimulated emission (SE), excited-state absorption (ESA), finite pulses, disorder, and experiment-matched uncertainty are additional types of input \[[23](#ref-beq06)\]. The distinction parallels classical Markovization: an enlarged state may carry memory exactly while a reduced output alone loses it.

<a id="sec:optical-readout"></a>

# From algebraic readout to a bounded optical instrument

<a id="sec:optical-existence"></a>

## Dilation and reachability are existence statements

For $`K_m=P_1+i^mP_2`$ on seven single-exciton levels, $`\operatorname{rank}(I-K_m^\dagger K_m)=5`$, so the minimal unitary dilation has dimension $`7+5=12`$. Ground plus single excitation supplies only eight levels; the hard-core ground/single/double manifold has $`1+7+21=29`$ and can supply the missing shelving space. The explicit determinant-corrected dilations give a two-outcome CP instrument. Coherent deferred selection is valid during the specified number-preserving wait, not under arbitrary number-changing dynamics \[[27](#ref-beq07)\].

Each of the four additional Hermitian root observables can be written $`O_a=V_a\Lambda_aV_a^\dagger`$. A basis change followed by population measurement and signed eigenvalue weighting realizes its expectation. Four settings with seven outcomes describe this direct spectral protocol; they are not a universal lower bound for all generalized measurements. The targets are pairwise noncommuting and largely outside the old exciton-1/2 block. Existing impulsive process-coordinate response arrays cannot be declared to span these root-state observables without the preparation/evolution/detection contraction that relates their domains \[[41](#ref-beq08)\].

The frozen $`K_{ij}=0`$, rotating-wave, 29-state control fixture has an exact strong-regularity and connectivity argument for $`\mathfrak{su}(29)`$. It supplies finite piecewise-control existence with unbounded signed controls. It does not impose a laboratory amplitude, bandwidth, duration, or bath tolerance. The separately optimized one-picosecond bounded pulses pass the strict closed-system gate for only one of four targets. The weighted-observable searches instead optimize $`C^\dagger\operatorname{diag}(\lambda)C=O`$, but all four returned candidates miss their stricter gate. Iteration-capped local searches do not prove unreachable targets \[[35](#ref-beq09),[3](#ref-beq10),[48](#ref-beq11)\].

<a id="sec:bath-chronology"></a>

## The bath-active chronology matters

The original canonical target-0 five-rung bath ladder fails its declared comparison tolerance: its largest operator difference is approximately $`0.00578835>0.005`$. A later predeclared $`D3,K1`$ higher-corner comparison stabilizes that waveform and rejects its readout, with relative residual approximately $`1.00565`$. The later result does not retroactively turn the original five-rung comparison into a pass. The separate weighted waveform already yields a finite convergence-controlled rejection on its own five-rung ladder \[[6](#ref-beq12),[47](#ref-beq13),[7](#ref-beq15)\].

The exact discrete-adjoint result makes bath-aware optimization feasible without claiming optimal control has been solved. For a finite-rung segment $`S_j=\exp(\Delta t\,L_j^\dagger)`$, its control derivative is a Fréchet derivative of the matrix exponential, evaluated using a block exponential. Forward and adjoint recursions then differentiate the selected quadratic readout objective exactly for that discretization. They give no global minimum or infinite-hierarchy error estimate \[[17](#ref-beq14)\]. Two independently replayed local seeds fail the locked 0.1 relative operator gate. Convex optimization of terminal-population weights for a fixed pulse also fails in the nested 7-, 8-, 9-, and 29-outcome families; only the weight optimization is globally convex. These terminal sectors are not GSB/SE/ESA pathways. A separate normalized 300 fs, 12-segment search also fails; its predeclared exit clause stops the proposed 24-segment continuation for that family \[[45](#ref-beq16),[21](#ref-beq17),[29](#ref-beq18)\].

<a id="sec:bounded-probe"></a>

## Full span does not guarantee stable estimation

The molecular-frame finite-probe design first supplies 162 effects of numerical real Hermitian rank 49. All four targets are in their unbounded span, but none passes with normalized coefficient norm $`\|w\|_2\leq10`$. With all seven carriers, 882 effects retain full span and three of four targets pass the unchanged bounded gate. The fourth remains missing; the three positive results are not erased by that joint failure \[[25](#ref-beq19),[24](#ref-beq20)\].

A predeclared standalone temporal-profile screen then selects the broad 100 fs probe, which passes all four targets at exploratory $`D1,K0`$. The profiles are not pooled. An apparently successful early profile is rejected by its forward/adjoint integrity check. The broad probe passes the $`D1,K1`$ bath-axis comparison but fails the $`D1,K0`$ to $`D2,K0`$ depth comparison; $`D3,K0`$ still fails the stacked-effect stability test \[[42](#ref-beq21),[5](#ref-beq22),[4](#ref-beq23)\].

The hierarchy-tail diagnostic measures contracting finite increments and forecasts one further rung. This is not a rigorous tail bound. The subsequent corrected-accuracy $`D4,K0`$ calculation actually supplies that rung: the maximum per-effect difference is approximately $`0.00039272`$, and the stacked relative difference is approximately $`0.023352`$, below the respective 0.005 and 0.05 thresholds. All four bounded residuals, approximately $`0.7453,0.5363,0.7359,0.7084`$, nevertheless fail. This is a stable finite-depth negative for this profile, not infinite-HEOM convergence or a universal optical no-go. Blind depth escalation is not the conclusion \[[18](#ref-beq24),[14](#ref-beq25)\].

<a id="sec:physical-tangent"></a>

## The physical domain of a nuisance calculation

The complete complex-linear response has 24 rows and 392 ADO coordinates. After four selected coordinates are separated, 388 nuisance coordinates span the same rank-18 response image. Six observation combinations remain nuisance-free, but their selected response rank is zero. Recovery against one realized nuisance vector therefore does not imply recovery against the complete complement. Nor does the latter ambient-complex obstruction imply a physical no-go: Hermiticity, trace, preparation and hierarchy constraints matter \[[2](#ref-beq27)\].

The later physical-tangent calculation supplies those constraints for the factorized-root preparation at $`D1,K0`$. The trace-free Hermitian root tangent has 48 real dimensions, rather than the independent 392-real- coordinate Hermitian ambient hierarchy. Its optical response has reported rank 18; adjoining the four target rows raises this to 22, exposing four missing scalar directions. Four stored traceless Hermitian root observables complete the linear algebra to the stated numerical tolerance. The large estimator weights and absent calibrated optical realization still matter. The structural tangent dimension is exact; floating-point row ranks and residuals are reported source computations, not new exact arithmetic certificates. Pure-state positivity cones, correlated preparations, and Hamiltonian/bath parameter tangents require separately chosen domains \[[31](#ref-beq26)\].

<a id="sec:evolving-audit"></a>

## Later refinements inside the evolving audit

The candidate audit contains substantive progress after its early snapshot header. Under unchanged source coordinates and detector norm, adding a zero-target GSB coordinate cannot lower the existing least-squares residual; a contractive isotropic transformation cannot enlarge the reachable set. These restricted statements neither construct the missing full laboratory response nor rule out a changed physical model \[[16](#ref-beq01)\].

The same audit records distinct external $`K_{ij}`$ inputs from the historical published table and a current-structure reconstruction. Both alter the signed ESA response, pass exploratory $`D1`$ readout, and fail the matched $`D4`$ bounded-readout test. Their effects are genuine model sensitivity, not MTT parameter selection. On a fixed structure the apparent 21 pair couplings reduce to an external amplitude $`g`$ and common twist $`\phi`$; the weight-one dipoles yield only weight-zero and weight-two pair harmonics. The resulting cone and cross-structure identities permit conditional source tests. They do not supply an independent covariance measurement. The separate $`J_{ij}`$ ensemble comparison uses ensemble dispersions, not errors on the means, and is not the double-exciton $`K_{ij}`$ sector \[[16](#ref-beq01)\].

A common ambient circle can carry both sectors with distinct amplitudes and a fixed relative anchor. A constant 18-degree intertwiner commutes with circle transport even though 18 degrees is not a $`\mathbb Z_{64}`$ element; interpreting it as such a group element is an additional, unsupported identification. Charge rows alone do not identify molecular geometry or that anchor. The frozen B-factor covariance model is a geometry-uncertainty model, not experimental covariance, and does not resolve the proposed finite-phase separation \[[16](#ref-beq01)\].

Finally, the audit advances from source-to-generator Lipschitz control to restricted two-parameter response tangents and analytic remainder bounds. The $`D1`$ tangent has an independent numerical comparison. The executed $`D4`$ tangent and sparse channel Hessian have no interval numerical-error enclosure or independent $`D4`$ validation in the record. Their improved local radii remain conditional numerical diagnostics, not a certified cover of the full source family. Detector calibration is also explicit: $`D_{\rm cal}=RG^T\Sigma^{-1/2}`$, with $`R`$ the source response, $`G`$ the gain map, and $`\Sigma`$ independent positive detector covariance. Selecting gain or covariance to make the target pass is circular; no experiment-matched payload for these 882 rows is supplied. These later refinements are retained without treating packet eligibility flags as physical evidence \[[16](#ref-beq01)\].

<a id="sec:charged-repair"></a>

# Charged lines, connections, and a conditional repair

<a id="sec:charged-module"></a>

## A representation does not select its physical transport

The frozen 47-atom HF–CIS charge rows $`q_J=q_{10}`$ and $`q_K=q_{11}-q_{00}`$ are neutral and linearly independent over $`\mathbb Q`$ as deposited decimals. Tensoring their rank-two span with a molecular weight-one line gives a charged module with weights $`(1,1)`$. A half-turn acts as $`-I_2`$; bilinear pair quantities have weight two and sesquilinear quantities weight zero. Restriction to $`\mathbb Z_{64}`$ is faithful. The exact decimal rank and classifying-stack pullback do not eliminate electronic-structure or geometry uncertainty \[[10](#ref-beq28)\].

This construction supplies the charged carrier that the earlier same-source compatibility packet still listed as missing. A neutral adjoint/form complex cannot replace it under a nontrivial phase action \[[20](#ref-beq47)\]. The selected nondegenerate seven-site configuration uses oriented atomic-plane frames and nonzero projected charge vectors. These frames trivialize the site lines, but the frame-flat connection and the projected connection $`P\,ds`$ are distinct: the latter can have curvature. A common parallel identification requires trivial relative Hom holonomy, not merely isomorphic underlying lines \[[28](#ref-beq29)\].

<a id="sec:phase-geometry"></a>

## Relative phase and two different kinds of loop

On the product of seven unit-frame circles, quotient the diagonal circle to leave six relative phases. The geometric mechanical connection is
``` math
A_F=\frac17\sum_{i=1}^7\alpha_i,\qquad
\beta_i=\alpha_i-A_F,\qquad \sum_i\beta_i=0.
```
It uses the product frame metric; it is not automatically a nuclear Eckart connection. The six relative forms need not vanish \[[15](#ref-beq30)\]. On the locked crystal-transfer fixture, the J/K phase increments lie within an arc shorter than $`\pi`$, selecting a shortest relative-torus path. Its horizontal endpoint comparison is approximately $`-173.663085`$ degrees, or $`6.336915`$ after the declared half-turn. It yields neither the external 18-degree anchor nor an exact $`\mathbb Z_{64}`$ step, and is not itself a q79–FMO physical trajectory \[[26](#ref-beq31)\].

At fixed configuration the full phase fiber has holonomy $`\exp(-2\pi i\sum_i n_i/7)`$, hence group $`\mu_7`$. Its intersection with $`\mu_{64}`$ is trivial, excluding a nontrivial primitive parallel identification on that full fiber \[[30](#ref-beq35)\]. This does not exclude a geometry-base loop. A synchronous rotation of all seven molecular planes over a round cap makes the relative forms vanish there. The cap $`\theta\leq\pi/3`$ has area $`\pi`$ and boundary holonomy $`-1`$, matching the q79 branch half-turn. The cap normalization is chosen for that compatibility, not predicted molecular motion. Globally the atom-framed site lines have $`c_1=0`$, so they cannot simultaneously realize a degree-one full normal sphere with Chern number two \[[43](#ref-beq42)\].

<a id="sec:interval-descent"></a>

## Contractible comparison versus a selected endpoint

The selected flat q79 family maps to $`B_\nabla U(1)`$. Along the contractible J/K interval, a parallel comparison exists by solving $`g^{-1}dg=A_q-A_F`$, uniquely after one initial fiber map. Its solutions form a $`U(1)`$ torsor. This exact nonempty pullback is not evidence of a physically selected pairing: interval comparisons exist universally \[[22](#ref-beq44)\].

The endpoint compiler reduces four future line-comparison rows to two inputs: a fully selected q79 endpoint and a prospectively selected q79–FMO pairing rule. It does not supply either input. The endpoint needs honest descended line/cocycle data, metrics, a common HYM chamber, and connections; a formal or twisted placeholder is insufficient. The current hidden projective rank-nine and existential HYM conclusions are retained. The missing physical visible endpoint and comparison data belong to the remaining B.HS.01/B.GEO.01 boundary, not to a reopened existential problem \[[37](#ref-beq45)\].

<a id="sec:relative-repair"></a>

## Relative curvature is weaker than equality of connections

On the cap the smooth connection is $`A_F=(1-\cos\theta)d\varphi`$, with curvature $`\operatorname{vol}_D`$. The punctured q79 representative is $`A_q=\tfrac12d\varphi`$, with coarse current curvature $`\pi\delta_p`$. Their difference
``` math
\eta=(\tfrac12-\cos\theta)d\varphi,\qquad
d\eta=\operatorname{vol}_D-\pi\delta_p
```
has zero tangential boundary value. Thus their relative current class agrees, while their curvatures and differential characters are not identical. A ramified/root-stack extension is not an ordinary smooth filled-disk connection isomorphism \[[34](#ref-beq38),[43](#ref-beq42)\].

For the declared round metric and fixed flux $`\pi`$, the abelian Yang–Mills energy is at least $`\pi/2`$, with equality exactly at constant curvature density one. Neumann heat repair $`F_s=\pi H_N(\kappa s;p,x)\operatorname{vol}_D`$ smooths the initial current for $`s>0`$, preserves flux and boundary holonomy, and approaches that endpoint. Boundary data alone admit infinitely many interior profiles $`F_F+da`$, so they do not select this metric, pairing or law \[[34](#ref-beq38)\].

On the scalar abelian lane the Maurer–Cartan quadratic bracket vanishes: the residual is $`dA`$. In the relative Coulomb slice its positive squared residual is the fixed-flux Yang–Mills functional; its gradient gives the same curvature heat equation. This explains the repair-law shape without an extra dimensionless coefficient, but $`\kappa>0`$ is still an absolute action/clock scale. This pure positive repair specialization is not the selected physical signed action and its gauge row is not a physical HYM moment map \[[36](#ref-beq41)\].

<a id="sec:observable-test"></a>

# Transported errors and an observable test

<a id="sec:metric-qualification"></a>

## Name the metric before bounding the semigroup

For a bounded invertible, domain-, boundary-, and flux-preserving chain map $`T`$, set $`g_{{\rm tr},k}(x,y)=g_{q,k}(T_k^{-1}x,T_k^{-1}y)`$. Then $`\Delta_{\rm tr}=T\Delta_qT^{-1}`$, with exact transported cost and heat semigroup. Initial isometry is unnecessary. Product preservation is unnecessary for this scalar curvature action but remains necessary for the full nonabelian theory \[[44](#ref-beq40)\].

For a separately selected physical metric $`g_{\rm phys}(x,y)=g_{\rm tr}(x,Ey)`$, write $`C_k=E_{k+1}d_k-d_kE_k`$. On a retained bounded sector the exact defect is
``` math
\Delta_{\rm phys}-\Delta_{\rm tr}
=d_{k-1}E_{k-1}^{-1}C_{k-1}^{\dagger_{\rm tr}}
 +E_k^{-1}C_k^{\dagger_{\rm tr}}d_k.
```
The triangle inequality gives a bound $`\delta_k`$ from the corresponding operator norms. Vanishing metric-chain defects suffice for exact physical intertwining even when $`E\ne I`$ \[[44](#ref-beq40)\].

#### Consumer correction to the frozen error formula.

The source’s coefficient-one estimate $`\kappa s\delta_k\|T\|`$ requires both heat semigroups to be contractions in the *same* norm used for $`\delta_k`$. Self-adjointness in two different metrics does not supply this hypothesis. In the transported norm, the general Duhamel estimate is
``` math
\begin{split}
&\|e^{-\kappa s\Delta_{\rm phys}}T-Te^{-\kappa s\Delta_q}\|\\
&\quad\leq\kappa\delta_k\|T\|
 \int_0^s\|e^{-\kappa(s-u)\Delta_{\rm phys}}\|_{\rm tr}
              \|e^{-\kappa u\Delta_{\rm tr}}\|_{\rm tr}\,du.
\end{split}
```
For bounded coercive $`E_k`$, contraction in the physical metric yields the valid bound $`K_{E_k}\kappa s\delta_k\|T\|`$, where $`K_{E_k}=\sqrt{\|E_k\|_{\rm tr}\|E_k^{-1}\|_{\rm tr}}`$. Observable evaluation adds $`\|\ell\|\|x\|`$ in these same norms. This qualification preserves the exact transported-metric identities and the source’s commuting diagonal example; it is separately recorded for source-owner correction, not a blanket downgrade of the result \[[44](#ref-beq40)\].

Positive-time smoothing cannot manufacture the required bounded inverse. For an infinite-dimensional compact-resolvent nonnegative Laplacian, $`e^{-\tau\Delta}`$, $`\tau>0`$, is compact with dense nonclosed range. Bounded factors remain compact. On a finite spectral cutoff its inverse norm grows as $`e^{\tau\lambda_{\max}}`$. Therefore a pre-smoothing chain map or a justified retained finite sector with tail control must come first; unitary evolution is not excluded by this heat-specific no-go \[[33](#ref-beq37)\].

<a id="sec:cap-observable"></a>

## An exact conditional mode, with a rigorous spectral interval

On the round cap, the axisymmetric reducing sector has
``` math
L=-\frac{d}{dx}\left((1-x^2)\frac{d}{dx}\right),\quad
\tfrac12\leq x\leq1,
```
regularity at the pole and Neumann condition $`u'(1/2)=0`$. The least positive root of $`P_\nu'(1/2)=0`$ gives $`\lambda=\nu(\nu+1)`$. Normalize its eigenfunction $`\varphi`$ in $`L^2(D)`$ and choose its sign positive at the pole. The mean-zero observable $`\ell_\varphi`$ then gives $`R(s)=\pi\varphi(p)e^{-\kappa\lambda s}`$. The flux observable instead stays constant and cannot determine a clock \[[1](#ref-beq32)\].

The later interval proof excludes earlier roots, uses a pole-free Dirichlet-to-Neumann monotonicity argument for uniqueness, and bisects an Arb-certified enclosure. Coarse outward enclosures of its frozen intervals are
``` math
\begin{split}
3.19569115101221&<\nu<3.19569115101222,\\
13.40813308366998&<\lambda<13.40813308367000.
\end{split}
```
These are imported rigorous intervals, not a new spectral computation \[[9](#ref-beq34)\]. The initial delta current is not an $`L^2`$ vector. To apply the bounded-vector error estimate above, begin at a positive regularization time or supply a separately justified distribution-space bound. Also convert the physical $`L^2`$ observable norm into the comparison metric before claiming a numerical error budget.

<a id="sec:response-identifiability"></a>

## Clock identification and held-out response

For $`Y(t)=C e^{-\beta t}`$, unknown nonzero gain and unknown rate are not identified by one observation. With a positive response, two observations identify $`\beta=-\log(Y_1/Y_0)/(t_1-t_0)`$; a third is held out. At equal spacing the prediction is $`Y_1^2=Y_0Y_2`$. Relative errors bounded by $`\rho<1`$ give a log-defect allowance $`4[-\log(1-\rho)]`$. An additive error needs a positive response lower bound before using that relative criterion. Fitting the rate is calibration, not an MTT prediction, and a single exponential is not unique to MTT \[[11](#ref-beq33)\].

For a positive finite mixture $`Y_n=\sum_j a_jr_j^n`$, with $`a_j>0`$ and distinct $`0<r_j<1`$,
``` math
Y_nY_{n+2}-Y_{n+1}^2
=\sum_{i<j}a_ia_j(r_ir_j)^n(r_i-r_j)^2.
```
Hence a positive two-by-two Hankel defect excludes a single rate in that class. The general Hankel rank is the number of distinct modes, not the three modes in the source’s example. Passing a noisy rank-one test does not prove an exactly single-mode source \[[32](#ref-beq36)\].

Signed and oscillatory responses require the later Prony extension, not the positivity argument. For distinct nonzero complex nodes and nonzero amplitudes, the Hankel matrix factors through a Vandermonde matrix and a diagonal amplitude matrix. A known $`m`$-mode model can be fitted from $`2m`$ training samples and tested on further samples. Signed cancellations can make a small minor vanish while the full rank is three; conjugate oscillatory nodes obey a real recurrence. Frequency aliases remain unless a sampling-band restriction is supplied. If every entry error is at most $`\delta`$, an $`m`$-square Hankel perturbation has norm at most $`m\delta`$; a singular value above that bound certifies retained rank, but a small singular value alone does not prove exact low rank. Repeated nodes, continuous spectra, and certified noisy node intervals are further problems \[[40](#ref-beq39)\].

<a id="sec:physical-gate"></a>

## The remaining physical test is not an auxiliary-row count

The frozen physical-descent checklist has four supplied rows out of 18: the charged module, its prospective preselection, the FMO configuration, and the canonical q79 source base. Its 14 remaining rows ask for an actual correspondence, parallel connection data, selected amplitudes and anchor, observable-semigroup/CP-memory and error transport, normalization, clock, and a prospectively fixed held-out experiment. Audit integrity is not a physical pass \[[38](#ref-beq43)\].

The later frontier organizes the auxiliary results into finite compatibility, connection geometry, repair, and response discrimination. A conditional compiler can close implications within these layers without supplying a physical input. Its cumulative auxiliary counts cannot be substituted for the 18 physical obligations. The useful next step is to specify the endpoint and pairing, then a bounded pre-smoothing chain map and metric defect, an observable with an error budget, and an independently controlled clock and detector. None of the preceding algebra requires new biological measurement principles \[[13](#ref-beq48)\].

# The corrected MTT theorem

<div id="thm:mtt" class="theorem">

**Theorem 12.1** (Conditional MTT stochastic-shadow theorem). *Assume a selected MTT branch supplies:*

1.  *a standard Borel upper state space $`\mathcal{Z}`$ compatible with the $`Y^4\times X^6`$ branch and its shared-carrier lane data;*

2.  *measurable upper dynamics $`T`$, or selected upper transition kernels;*

3.  *a selected probability law $`\rho`$ on preparations or captured upper states;*

4.  *a measurable observable map $`\pi:\mathcal{Z}\to Q`$.*

*Then:*

1.  *the observed histories possess a unique path law;*

2.  *regular history-dependent conditional kernels exist;*

3.  *failure of the Markov property on $`Q`$, or a higher Markov order, follows whenever the corresponding conditional-independence witness is verified;*

4.  *any action-weight expression gives those kernels only if its action, scale, reference measure, and equality to the projected conditional law are separately established.*

*No conclusion about Born probabilities, noncommutative observables, quantum instruments, process tensors, or CP-divisibility follows from (S1)–(S4) alone.*

</div>

<div class="proof">

*Proof.* Parts (a) and (b) follow from [2.1](#thm:projected-law) and standard disintegration on standard Borel spaces. Part (c) follows from [4.1](#def:markov-order), [4.3](#prop:factorization) after a witness has been proved. Part (d) is [3.2](#lem:action-kernel) together with the source distinction in [3.3](#lem:gibbs). [6.1](#prop:commutative) proves the final limitation. ◻

</div>

## What is closed and what remains open

#### Closed mathematical layer.

Once a source law or family of kernels is given, the path measure, conditional kernels, Bayesian posteriors, Markov-order tests, and history-state Markovization are standard and rigorous. Projection-induced observed memory is real and can be demonstrated exactly.

#### Conditional MTT layer.

An MTT fixed-point flow and recorder map can instantiate the upper dynamics and projection. A selected finite action kernel can instantiate the conditional law. These are conditional constructions until the same MTT branch fixes all their source data.

#### Open physical layer.

The decisive missing objects are:

1.  a selected physical capture or preparation measure $`\rho`$ for the proposed application, beyond the established canonical q79 tier;

2.  a derivation of the proposed $`\Delta A`$, reference measure, and scale from the selected geometry rather than from target probabilities;

3.  a proof that no allowed finite MTT state summarizes the claimed memory;

4.  a selected family of physical intervention and recorder kernels;

5.  a same-source connection between the established noncommutative model and the proposed physical preparation, intervention, and detector.

These obligations are testable. For example, a proposed finite MTT recorder state can be checked by conditioning two histories with the same recorder value and comparing their next-step kernels. A proposed action source can be tested by computing both the geometric weight and the projected conditional frequency without fitting one to the other.

# Discussion

## What survives from the original proposal

The original physical intuition survives in a narrower and more useful form. A many-to-one projection can hide upper variables that retain predictive information. The lower process can therefore be non-Markovian even when the upper process is simple. MTT’s fixed-point and bundle language supplies a natural place for those hidden variables, and the shared carrier offers a possible common memory channel across projected sectors.

The path-space language is also valuable computationally. It provides a precise object to estimate in simulations: conditional kernels indexed by recorder histories, their total-variation separation, and the minimal sufficient state needed for prediction. These are stronger diagnostics than calling a trajectory “indivisible” by inspection.

## What is no longer claimed

This paper does not claim that:

- history dependence eliminates every sequential factorization;

- failure of one-step Markovianity proves infinite-dimensional memory;

- a fitted Gibbs action is selected by MTT;

- a classical event algebra derives the full Hilbert-space quantum formalism;

- measurement is merely conditioning rather than a physical process;

- no-signaling follows automatically from postselection.

Removing those claims strengthens the program. It leaves a theorem that can be used without ambiguity and identifies exactly which future calculation would turn a flexible stochastic encoding into an MTT prediction.

## Relation to established work

Chains with complete connections provide a mature framework for processes whose conditional probabilities depend continuously on a long or infinite past \[[49](#ref-fernandez2005),[50](#ref-johansson2003)\]. Their uniqueness and mixing theorems require specific regularity hypotheses; “summable variations” is not a synonym for arbitrary history dependence. Those results can be applied after an MTT kernel has been selected and its variation bounds have been verified.

Quantum non-Markovianity is richer because interventions can disturb the system and the relevant objects are noncommutative multi-time maps. Process tensors and CP-divisibility are therefore appropriate comparison targets, not automatic consequences of the classical shadow construction. The revised MTT path is:
``` math
\begin{array}{c}
\text{selected upper source and dynamics}\\
\downarrow\\
\text{projected classical path law and memory diagnostics}\\
\downarrow\quad\text{(additional noncommutative source theorem)}\\
\text{quantum process tensor or channel family}.
\end{array}
```

# Conclusion

MTT can rigorously support a history-dependent stochastic shadow, but only after a probability source has been selected. The resulting lower process may be non-Markovian and even have infinite Markov order on the recorded state space. This is a substantive consequence of projection. It is nevertheless state-relative: the process is Markovian on its history space and may admit a small sufficient-state compression.

The corrected result therefore does two things at once. It preserves the useful MTT insight that hidden upper coherence can appear as lower memory, and it prevents that insight from being mistaken for a derivation of quantum probability or absolute indivisibility. The new q79–FMO account makes that boundary concrete. Canonical operational quantum structure, coherent-history calculations, and exact charged-line compatibility are already available. Finite numerical readout profiles and conditional geometric repair do not yet select a physical molecular correspondence. The next research target is that same-source preparation and intervention model, with calibrated observable transport, followed by a test of which memory remains on the chosen recorder state.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->

# Computational Evidence and Reproducibility

The classical path-law proofs are independent of the numerical packets. The contextual sections cite all 48 assigned BEQ frozen artifacts at commit `f141a20e a23c5c3f f19cc216 1c0e226e 29ade8a7` of the [curated results repository](https://github.com/PeterNero/mtt-results-repro). The frozen manifest is `release/result_manifest.json`; its SHA-256 is

> 5715b0da 6a54df29 d43a53fe 4b9ae932
> bf6d4cd9 fc43e8c0 ff2e2254 56df13e3

Each bibliography link identifies its exact artifact bytes. Local metadata and the review fragment bind result identifiers to source hashes and this manuscript. The evolving candidate audit is read through its later sections; its preceding-snapshot self-reference and older eligibility headers are historical context, not current authority over refined results.

This revision performs source reading, byte-hash validation, and small bounded algebraic consistency checks. It does not replay HEOM, control optimization, interval spectral isolation, or molecular calculations, and it does not infer independent verification from packet booleans. Negative readout results retain their exact fixture, norm, and finite-rung scope. Conditional geometry retains its metric, domain, pairing and clock inputs. Current canonical operational q79 and finite mathematical conclusions are not reopened by historical source-selection language. No imported result changes theorem ownership or promotes the physical q79–FMO gate.

<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

# References

<a id="ref-beq32"></a>

\[1\] BEQ Research. Axisymmetric Neumann response observable.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_axisymmetric_neumann_observable/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq27"></a>

\[2\] BEQ Research. Basis-complete complex nuisance response.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_basis_complete_nuisance/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq10"></a>

\[3\] BEQ Research. Bounded projective pulse searches.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_bounded_projective_pulses/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq23"></a>

\[4\] BEQ Research. Broad-probe D3 depth instability.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_broad_probe_d3_depth_instability/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq22"></a>

\[5\] BEQ Research. Broad-probe two-axis convergence rejection.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_broad_probe_two_axis_convergence_rejection/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq12"></a>

\[6\] BEQ Research. Canonical bath-active projective ladder.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_bath_projective_ladder/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq15"></a>

\[7\] BEQ Research. Canonical D3,K1 higher-corner follow-up.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_canonical_d3k1_followup/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq46"></a>

\[8\] BEQ Research. Canonical q79 selected finite source base.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_q79_selected_source_base/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq34"></a>

\[9\] BEQ Research. Certified first positive Neumann spectral interval.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_neumann_spectral_interval/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq28"></a>

\[10\] BEQ Research. Charged HF–CIS module and representation pullback.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_charged_hfcis_module/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq33"></a>

\[11\] BEQ Research. Clock identifiability and held-out exponential test.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_clock_identifiability/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq03"></a>

\[12\] BEQ Research. Coherent cycle witness and endpoint-population nonidentifiability.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_process_witness/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq48"></a>

\[13\] BEQ Research. Consolidated auxiliary frontier and physical boundary.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_frontier_consolidation_2026_08_26/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq25"></a>

\[14\] BEQ Research. Corrected-accuracy D4 stable bounded-readout negative.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_broad_probe_d4_stable_negative/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq30"></a>

\[15\] BEQ Research. Diagonal molecular phase connection.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_diagonal_phase_connection/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq01"></a>

\[16\] BEQ Research. Evolving q79–FMO candidate audit and source-selection boundaries.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_candidate_audit/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq14"></a>

\[17\] BEQ Research. Exact finite-rung discrete adjoint and Frechet gradient.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_bath_aware_adjoint_gradient/artifact.md), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq24"></a>

\[18\] BEQ Research. Finite hierarchy-tail diagnostic.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_broad_probe_hierarchy_tail_diagnostic/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq02"></a>

\[19\] BEQ Research. Finite route-Hodge intertwiners and the binary-carrier obstruction.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_route_hodge_intertwiner/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq47"></a>

\[20\] BEQ Research. Finite same-source repair compatibility.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_same_source_repair_descent/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq17"></a>

\[21\] BEQ Research. Fixed-pulse terminal-sector readout rejection.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_terminal_sector_rejection/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq44"></a>

\[22\] BEQ Research. Flat-family open-path differential pullback.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_q79_flat_family_fmo_open_path_pullback/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq06"></a>

\[23\] BEQ Research. Four-history ADO process response and fifteen CP settings.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_ado_process_response/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq20"></a>

\[24\] BEQ Research. Full-carrier three-of-four bounded readout.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_full_carrier_three_of_four/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq19"></a>

\[25\] BEQ Research. Full-rank unbounded finite-probe readout.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_finite_probe_full_rank_unbounded/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq31"></a>

\[26\] BEQ Research. Locked crystal-transfer J/K relative-phase path.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_jk_relative_phase_path/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq07"></a>

\[27\] BEQ Research. Minimal optical filter dilation and ideal control reachability.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_optical_filter_dilation/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq29"></a>

\[28\] BEQ Research. Molecular configuration lines and connection selection.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_configuration_line/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq18"></a>

\[29\] BEQ Research. Normalized 300 fs control rejection.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_normalized_300fs_control_rejection/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq35"></a>

\[30\] BEQ Research. Phase-fiber holonomy coprimality obstruction.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_phase_fiber_holonomy/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq26"></a>

\[31\] BEQ Research. Physical Hermitian ADO and factorized-root tangents.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_physical_ado_tangent/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq36"></a>

\[32\] BEQ Research. Positive-mixture Hankel discrimination.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_positive_mixture_hankel/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq37"></a>

\[33\] BEQ Research. Positive-time smoothing and bounded-inverse obstruction.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_positive_time_smoothing_nogo/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq38"></a>

\[34\] BEQ Research. Relative current and fixed-flux Yang–Mills repair.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_relative_yang_mills_repair/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq09"></a>

\[35\] BEQ Research. Root-readout reachability in the frozen SU(29) fixture.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_su29_root_reachability/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq41"></a>

\[36\] BEQ Research. Scalar upper repair action and Yang–Mills restriction.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_upper_action_yang_mills_restriction/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq45"></a>

\[37\] BEQ Research. Selected endpoint interval descent compiler.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_q79_fmo_selected_endpoint_interval_compiler/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq43"></a>

\[38\] BEQ Research. Selected physical q79–FMO descent gate.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_physical_gate/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq04"></a>

\[39\] BEQ Research. Seven-rung 300 K HEOM reference.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_heom_reference/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq39"></a>

\[40\] BEQ Research. Signed and oscillatory Prony discrimination.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_signed_oscillatory_prony/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq08"></a>

\[41\] BEQ Research. Spectral population design for four physical root readouts.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_physical_readout_design/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq21"></a>

\[42\] BEQ Research. Standalone broad-probe four-of-four D1 readout.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_broad_probe_d1_four_of_four/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq42"></a>

\[43\] BEQ Research. Synchronous cap and ramification boundary comparison.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_synchronous_cap_q79_ramification/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq40"></a>

\[44\] BEQ Research. Transported metric and semigroup-defect compiler.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_q79_fmo_fmo_q79_transported_metric_semigroup/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq16"></a>

\[45\] BEQ Research. Two-seed bath-aware control replay.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_bath_aware_two_seed_replay/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq05"></a>

\[46\] BEQ Research. Two-time coherent HEOM history functional.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_heom_history/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq13"></a>

\[47\] BEQ Research. Weighted bath-active readout rejection.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_bath_weighted_rejection/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-beq11"></a>

\[48\] BEQ Research. Weighted-observable pulse searches.

[Frozen result artifact](https://github.com/PeterNero/mtt-results-repro/blob/f141a20ea23c5c3ff19cc2161c0e226e29ade8a7/release/results/beq_fmo_weighted_pulse_search/artifact.json), 2026. Curated snapshot f141a20e; source scope retained.

<a id="ref-fernandez2005"></a>

\[49\] Roberto Fernandez and Gregory Maillard. Chains with complete connections: General theory, uniqueness, loss of memory and mixing properties. *Journal of Statistical Physics*, 118(3–4):555–588, 2005.

<a id="ref-johansson2003"></a>

\[50\] Anders Johansson and Anders Öberg. Square summability of variations of $`g`$-functions and uniqueness of $`g`$-measures. *Mathematical Research Letters*, 10(5–6):587–601, 2003.

<a id="ref-kallenberg2002"></a>

\[51\] Olav Kallenberg. *Foundations of Modern Probability*. Springer, New York, 2 edition, 2002.

<a id="ref-pollock2018framework"></a>

\[52\] Felix A. Pollock, Cesar Rodriguez-Rosario, Thomas Frauenheim, Mauro Paternostro, and Kavan Modi. Non-markovian quantum processes: Complete framework and efficient characterization. *Physical Review A*, 97:012127, 2018.

<a id="ref-pollock2018markov"></a>

\[53\] Felix A. Pollock, Cesar Rodriguez-Rosario, Thomas Frauenheim, Mauro Paternostro, and Kavan Modi. Operational markov condition for quantum processes. *Physical Review Letters*, 120:040405, 2018.

<a id="ref-rivas2010"></a>

\[54\] Angel Rivas, Susana F. Huelga, and Martin B. Plenio. Entanglement and non-markovianity of quantum evolutions. *Physical Review Letters*, 105:050403, 2010.

<a id="ref-spekkens2005"></a>

\[55\] Robert W. Spekkens. Contextuality for preparations, transformations, and unsharp measurements. *Physical Review A*, 71:052108, 2005.
