---
abstract: |
  This paper gives a measure-theoretic account of stochastic processes obtained by projecting an upper Modal Triplet Theory (MTT) evolution. Given a selected probability law on upper initial data, measurable upper dynamics, and an observable map, the projected histories carry a unique path-space law. Regular conditional kernels then exist on standard Borel state spaces. The observed process may fail to be Markovian even when the upper process is Markovian or deterministic. We distinguish four statements that were previously conflated: failure of the Markov property on the observed state space, absence of finite Markov order, failure of a chosen Chapman–Kolmogorov reduction, and quantum CP-indivisibility. Every classical path law still factorizes sequentially through its history-dependent conditional kernels and becomes Markovian on a history state space. An exact binary hidden-state example shows that projection can create infinite observed Markov order while the memory remains compressible to one posterior scalar. Exponential action weights define valid kernels when their action and reference measure are supplied, but writing a positive kernel in Gibbs form is a parameterization, not a first-principles prediction. Finally, a commutative path-space algebra does not derive noncommutative quantum observables, process tensors, Born probabilities, or quantum instruments. The resulting MTT theorem is rigorous but conditional: the outstanding physical step is to select the upper probability source and intervention structure from MTT geometry.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 3209a96436978bb986571d595e4a36f50b2038352dfae838cf9d34c444f6e7bf
paper_id: modal-triplet-theory-from-mtt-to-indivisible-stochastic-449ca9a6
release_state: zenodo_released
released_version: v2
title: |
  Modal Triplet Theory and History-Dependent Stochastic Processes:
  Fixed-State Indivisibility, Markov Order, and the Quantum Boundary
zenodo_doi: 10.5281/zenodo.21665996
zenodo_record_id: 21665996
zenodo_url: "https://zenodo.org/records/21665996"
---

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

The first three are classical properties. The fourth requires a noncommutative operator system and completely positive maps. It cannot be deduced from a classical path law alone. Modern process-tensor treatments make this operational distinction explicit .

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
| MTT currently selects the required probability source | Open. |

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

**Theorem 1** (Projected path law). *Let $`\mathcal{Z}`$ and $`Q`$ be standard Borel spaces, let $`T:\mathcal{Z}\to\mathcal{Z}`$ and $`\pi:\mathcal{Z}\to Q`$ be measurable, and let $`\rho`$ be a probability measure on $`\mathcal{Z}`$. Define
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

# Conditional kernels and action weights

## Construction from kernels

One may equivalently start with an initial law $`\lambda_0`$ on $`Q`$ and a sequence of measurable probability kernels
``` math
K_k(\,\cdot\,|h_k),\qquad h_k=(q_0,\ldots,q_k)\in Q^{k+1}.
```
The next theorem is standard probability theory .

<div id="thm:IT" class="theorem">

**Theorem 3** (Ionescu–Tulcea extension). *For every initial probability measure $`\lambda_0`$ and sequence of probability kernels $`K_k`$ from $`Q^{k+1}`$ to $`Q`$, there is a unique probability measure $`\mu`$ on $`Q^{\mathbb{N}}`$ whose finite-dimensional distributions satisfy
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

Conversely, because $`Q`$ is standard Borel, the law in <a href="#thm:projected-law" data-reference-type="ref+Label" data-reference="thm:projected-law">1</a> admits regular conditional distributions
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

**Lemma 4** (Normalized action kernel). *If $`0<Z_k(h_k)<\infty`$ for every reachable history, then
``` math
K_k(A|h_k)=\frac{1}{Z_k(h_k)}
\int_A\exp\!\left[-\frac{\Delta A_k(h_k,q')}{\eta}\right]\nu(dq')
```
is a measurable probability kernel. Together with an initial law it defines a unique path measure by <a href="#thm:IT" data-reference-type="ref+Label" data-reference="thm:IT">3</a>.*

</div>

<div class="proof">

*Proof.* Nonnegativity and normalization are immediate. Measurability of parameterized nonnegative integrals follows from joint Borel measurability; division is measurable because $`Z_k`$ is finite and strictly positive. ◻

</div>

This result is exact, but it begins with $`\Delta A_k`$, $`\eta`$, and $`\nu`$. Calling $`\eta=\hbar`$ is a physical identification, not a consequence of normalization. Likewise, a Euclidean exponential weight is not the complex phase $`e^{iS/\hbar}`$ and does not by itself produce quantum interference.

<div id="lem:gibbs" class="lemma">

**Lemma 5** (Gibbs form is a parameterization). *Suppose $`K_k(\cdot|h_k)`$ has a strictly positive normalized density $`k_k(\cdot|h_k)`$ with respect to $`\nu`$. For any $`\eta>0`$, setting
``` math
\Delta A_k(h_k,q')=-\eta\log k_k(q'|h_k)
```
reproduces $`K_k`$ through <a href="#lem:action-kernel" data-reference-type="ref+Label" data-reference="lem:action-kernel">4</a>, with $`Z_k=1`$. Adding an arbitrary history-dependent constant to $`\Delta A_k`$ leaves the normalized kernel unchanged.*

</div>

<div class="proof">

*Proof.* Exponentiation gives $`e^{-\Delta A_k/\eta}=k_k`$, and the density is already normalized. A history-only constant multiplies numerator and denominator by the same factor. ◻

</div>

<a href="#lem:gibbs" data-reference-type="ref+Label" data-reference="lem:gibbs">5</a> is useful for fitting or encoding a known kernel. It cannot show that MTT geometry selected that kernel. Exact reconstruction of arbitrary target kernels demonstrates expressive capacity; prediction requires a rule that fixes the action before the target data are supplied.

# Markov order and fixed-state indivisibility

## Precise definitions

Let $`\mathcal{F}_k=\sigma(Q_0,\ldots,Q_k)`$.

<div id="def:markov-order" class="definition">

**Definition 6** (Markov order). The process has Markov order at most $`r\geq 1`$ if, for every $`k\geq r-1`$, there is a kernel $`L_k`$ such that
``` math
\mathbb{P}(Q_{k+1}\in A\mid\mathcal{F}_k)
=L_k(A|Q_{k-r+1},\ldots,Q_k)
\quad\text{a.s.}
```
for every Borel $`A`$. It has infinite Markov order on $`Q`$ if no finite $`r`$ has this property.

</div>

<div id="def:q-indivisible" class="definition">

**Definition 7** (Fixed-$`Q`$ indivisibility). For this paper only, a process is *fixed-$`Q`$ indivisible* if its complete finite-dimensional distributions cannot be generated by one-step kernels depending only on the current value $`q_k`$. This is simply failure of Markov order one on the chosen observed state space. It is not quantum CP-indivisibility.

</div>

<div id="prop:factorization" class="proposition">

**Proposition 8** (Factorization criterion). *A path law is Markov of order one on $`Q`$ if and only if there are kernels $`M_k(dq_{k+1}|q_k)`$ for which every finite-dimensional law factorizes as
``` math
\lambda_0(dq_0)\prod_{k=0}^{n-1}M_k(dq_{k+1}|q_k).
```
Consequently, fixed-$`Q`$ indivisibility is exactly a statement about the chosen state description $`Q`$, not about the impossibility of sequential factorization.*

</div>

<div class="proof">

*Proof.* The forward implication is <a href="#thm:IT" data-reference-type="ref+Label" data-reference="thm:IT">3</a> applied to Markov kernels. For the reverse implication, disintegration of the displayed law gives a version of the conditional law of $`Q_{k+1}`$ that depends only on $`Q_k`$. ◻

</div>

## Every process is Markov on its history state

<div id="thm:history-markov" class="theorem">

**Theorem 9** (History-state Markovization). *Let $`\mu`$ be any path law on a standard Borel space $`Q`$, with conditional kernels $`K_k`$. Define
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

**Proposition 10** (Finite sufficient-state compression). *Suppose there is a standard Borel space $`S`$, measurable summaries $`s_k:Q^{k+1}\to S`$, update maps
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

# An exact projection-induced memory example

<div id="ex:binary" class="example">

**Example 11** (Binary latent source). Let $`S\in\{0,1\}`$ be chosen with equal prior probabilities and remain fixed. Conditional on $`S`$, let $`Q_0,Q_1,\ldots`$ be independent with
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

**Proposition 12** (Infinite observed order, one-scalar memory). *The process in <a href="#ex:binary" data-reference-type="ref+Label" data-reference="ex:binary">11</a> has no finite Markov order on $`Q=\{0,1\}`$. Nevertheless, the scalar posterior $`p_k`$ is a sufficient state, so the observed memory is recursively compressible to one real number.*

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
The next prediction depends only on $`p_k`$, and $`p_{k+1}=u(p_k,Q_{k+1})`$. Apply <a href="#prop:sufficient" data-reference-type="ref+Label" data-reference="prop:sufficient">10</a>. ◻

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

**Proposition 13** (Commutative reconstruction limit). *The GNS representation of a commutative path-space algebra has a commuting operator image. It does not, without extra structure, produce incompatible observables, complex interference amplitudes, a noncommutative state algebra, or general completely positive instruments.*

</div>

<div class="proof">

*Proof.* If $`ab=ba`$ in the algebra, then every representation satisfies $`\pi(a)\pi(b)=\pi(ab)=\pi(ba)=\pi(b)\pi(a)`$. The missing noncommutative objects cannot be obtained by relabeling commuting multiplication operators. ◻

</div>

Ordinary sigma-additivity also implies that the probability of a fixed measurable event is unchanged when a partition is refined around it. That is a consistency property of one classical sample space, not by itself the operational measurement noncontextuality used in quantum-foundational theorems .

## Why quantum divisibility is separate

Quantum CP-divisibility concerns a family of channels $`\Lambda_{t:s}`$ for which
``` math
\Lambda_{t:r}=\Lambda_{t:s}\Lambda_{s:r}
```
with the intermediate map completely positive and trace preserving. A process tensor goes further by mapping sequences of interventions to outcome statistics. Both notions require noncommutative input and output systems and an intervention calculus .

A classical kernel can agree numerically with the probabilities of one chosen quantum experiment. Such agreement does not identify its updates with all quantum instruments or establish CP-divisibility. The current MTT quantization results remain conditional on imported or separately selected operator structures; the classical construction in this paper does not close that boundary.

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

# The corrected MTT theorem

<div id="thm:mtt" class="theorem">

**Theorem 14** (Conditional MTT stochastic-shadow theorem). *Assume a selected MTT branch supplies:*

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

*Proof.* Parts (a) and (b) follow from <a href="#thm:projected-law" data-reference-type="ref+Label" data-reference="thm:projected-law">1</a> and standard disintegration on standard Borel spaces. Part (c) follows from <a href="#def:markov-order,prop:factorization" data-reference-type="ref+Label" data-reference="def:markov-order,prop:factorization">[def:markov-order,prop:factorization]</a> after a witness has been proved. Part (d) is <a href="#lem:action-kernel" data-reference-type="ref+Label" data-reference="lem:action-kernel">4</a> together with the source distinction in <a href="#lem:gibbs" data-reference-type="ref+Label" data-reference="lem:gibbs">5</a>. <a href="#prop:commutative" data-reference-type="ref+Label" data-reference="prop:commutative">13</a> proves the final limitation. ◻

</div>

## What is closed and what remains open

#### Closed mathematical layer.

Once a source law or family of kernels is given, the path measure, conditional kernels, Bayesian posteriors, Markov-order tests, and history-state Markovization are standard and rigorous. Projection-induced observed memory is real and can be demonstrated exactly.

#### Conditional MTT layer.

An MTT fixed-point flow and recorder map can instantiate the upper dynamics and projection. A selected finite action kernel can instantiate the conditional law. These are conditional constructions until the same MTT branch fixes all their source data.

#### Open physical layer.

The decisive missing objects are:

1.  a selected capture or preparation measure $`\rho`$;

2.  a derivation of the proposed $`\Delta A`$, reference measure, and scale from the selected geometry rather than from target probabilities;

3.  a proof that no allowed finite MTT state summarizes the claimed memory;

4.  a selected family of physical intervention and recorder kernels;

5.  an independent noncommutative observable source if a quantum process is claimed.

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

Chains with complete connections provide a mature framework for processes whose conditional probabilities depend continuously on a long or infinite past . Their uniqueness and mixing theorems require specific regularity hypotheses; “summable variations” is not a synonym for arbitrary history dependence. Those results can be applied after an MTT kernel has been selected and its variation bounds have been verified.

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

The corrected result therefore does two things at once. It preserves the useful MTT insight that hidden upper coherence can appear as lower memory, and it prevents that insight from being mistaken for a derivation of quantum probability or absolute indivisibility. The next research target is sharp: derive the capture law and intervention kernels from the selected MTT branch, then compute whether their projected process has memory that cannot be closed by the existing finite recorder state.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The fixed-state indivisibility and Markov-order statements are measure-theoretic. The open strict-upgrade ledger supplies no stochastic kernel, probability measure, or quantum reconstruction and is included only as a stronger unresolved corpus boundary.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->
