---
abstract: |
  Bell experiments do not require a controllable signal between spacelike separated laboratories, but they do exclude a complete measurement-independent hidden-variable description whose conditional probabilities factorize. This paper formulates that distinction for Modal Triplet Theory (MTT). The upper description is a local algebra or field theory on $`M=Y^4\times X^6`$, while an admissible fixed point may define a globally nonseparable state. Under an explicit base-local descent hypothesis, microcausality passes to the four-dimensional observable algebras. Under standard local completely positive instruments, this gives operational no-signaling. If the descended statistics violate CHSH while measurement independence is retained, Bell factorization must nevertheless fail. The result is therefore not a Bell-local hidden-variable completion. It is a conditional account in which upper-local dynamics and globally constrained state selection coexist, so the correlations need not be produced by a spacelike dynamical influence. A singlet packet is included as a benchmark, not as an MTT prediction. A physical MTT realization still requires a selected fixed-point state, a locality-preserving descent, local instruments, and a probability source that yields the benchmark statistics.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v2
date: July 2026
generated_from_main_tex_sha256: 58f6802a63d13d2106bc61f0cb3620adb7d92576e3a2aa48b2fb37a6a22ee398
paper_id: modal-fixed-points-bell-s-beables-and-the-limits-of-fac-59a69f5c
release_state: zenodo_released
released_version: v2
title: |
  **Modal Fixed Points, Bell’s Beables, and the Limits of Factorization:
  Upper-Local Dynamics, Nonseparable States, and Operational No-Signaling in MTT**
zenodo_doi: 10.5281/zenodo.21665825
zenodo_record_id: 21665825
zenodo_url: "https://zenodo.org/records/21665825"
---

# Revision note

#### Supersedes.

Version 2 supersedes the 2025 version associated with Zenodo record 17076301.

#### Reason.

The earlier text treated projection as creating Bell correlations from an otherwise Bell-local completion and did not keep microcausality, operational no-signaling, state nonseparability, measurement independence, and Bell factorization logically separate.

#### Resolution.

This version distinguishes those notions, removes the incorrect inference that an ordinary Kaluza–Klein reduction forces state factorization, and reclassifies the singlet and quantum-network calculations as conditional benchmarks until their probability and state data are selected by MTT.

#### Retained content.

The fixed-point perspective and the proposal that apparently nonlocal correlations may descend from an upper description with local dynamics are retained, now with their exact assumptions and completion obligations stated.

#### Remaining boundary.

MTT has not yet selected from first principles the physical preparation state, the Born probability functional, and the detector instruments needed to derive the singlet correlations rather than use them as a benchmark.

# Introduction: the central picture

The familiar phrase “spooky action at a distance” combines two very different claims:

1.  a choice in one laboratory sends a controllable physical influence to a spacelike separated laboratory;

2.  the joint probabilities cannot be screened off into independent local responses by conditioning on a complete hidden state.

Bell’s theorem concerns the second claim. Relativistic no-signaling concerns the first. Quantum theory can violate a Bell inequality while forbidding the use of the correlations as a faster-than-light communication channel . Algebraic quantum field theory sharpens the same distinction: spacelike observable algebras commute, yet a state on their joint algebra need not factorize .

The proposed MTT perspective is consequently not that Bell’s theorem has been evaded. It is that the upper description can remain local at the level of equations and observable algebras while its selected admissible state is global and nonseparable. Projection then reveals correlations already carried by that state; it does not manufacture them from a separable Bell-local state. In plain language, the two laboratories read different parts of one globally constrained preparation; neither measurement has to send a message to the other laboratory in order for their records to be correlated.

## What is proved and what is conditional

This paper proves four statements at the declared level:

1.  a base-local internal descent preserves spacelike commutativity;

2.  local nonselective instruments imply operational no-signaling;

3.  measurement independence plus Bell factorization implies the CHSH bound;

4.  therefore any MTT packet reproducing a CHSH violation while preserving measurement independence must be globally nonfactorizing.

The paper does *not* derive a particular entangled state, Born probabilities, the value $`2\sqrt{2}`$, or a physical detector instrument from fixed-point language alone. Those are source rows in the completion contract of <a href="#sec:completion" data-reference-type="ref+label" data-reference="sec:completion">12</a>.

# Three meanings of locality

<div class="definition">

**Definition 1** (Upper algebraic locality). *Let $`Y^4`$ be a supplied causal spacetime and $`X^6`$ a compact internal space. Set $`M=Y^4\times X^6`$. For each causally suitable $`\mathcal O\subset Y^4`$, let
``` math
\mathcal{A}_M(\widetilde{\mathcal O}),
  \qquad
  \widetilde{\mathcal O}:=\mathcal O\times X^6,
```
be an upper observable algebra. Upper algebraic locality means
``` math
[A,B]=0
 \quad\text{whenever}\quad
 A\in\mathcal{A}_M(\widetilde{\mathcal O}_A),\
 B\in\mathcal{A}_M(\widetilde{\mathcal O}_B),
 \quad
 \mathcal O_A\perp\mathcal O_B .
```*

</div>

The product notation is a control model. It does not assert that the internal space is literally three independent manifolds or that its rank filtration adds new spacetime coordinates. In the current MTT geometric program, $`X^6`$ must be supplied by the selected physical branch, and the $`1<2<3`$ labels are operator or lane data on that geometry.

<div class="definition">

**Definition 2** (Operational no-signaling). *For settings $`a,b`$ and outcomes $`\alpha,\beta`$, a probability packet $`p(\alpha,\beta\mid a,b)`$ is no-signaling when
``` math
\sum_\beta p(\alpha,\beta\mid a,b)
 \quad\text{is independent of }b,
\qquad
 \sum_\alpha p(\alpha,\beta\mid a,b)
 \quad\text{is independent of }a.
```*

</div>

<div class="definition">

**Definition 3** (Bell factorization). *Let $`\lambda`$ denote a proposed complete ontic state. Bell factorization is the screening-off condition
``` math
p(\alpha,\beta\mid a,b,\lambda)
 =
 p_A(\alpha\mid a,\lambda)\,
 p_B(\beta\mid b,\lambda)
```
for almost every $`\lambda`$. Measurement independence is
``` math
\rho(\lambda\mid a,b)=\rho(\lambda).
```*

</div>

These notions are not interchangeable. Commuting algebras need not carry a product state. No-signaling is an observed marginal condition, whereas Bell factorization is a conditional-independence claim about a complete underlying description. A theory may satisfy the first two notions and fail the third.

# The upper fixed-point packet

The minimal MTT packet needed in this paper consists of:

1.  a causal base $`Y^4`$, an internal space $`X^6`$, and an upper local net $`\mathcal O\mapsto\mathcal{A}_M(\mathcal O\times X^6)`$;

2.  preparation data $`\lambda`$ with a measure $`\rho`$ selected before the laboratory settings;

3.  an admissible fixed point or stationary upper state $`\omega_\lambda`$ selected from the preparation data, not from the later choices $`a,b`$;

4.  a base-local descent $`\mathcal{D}`$ from upper observables to the effective four-dimensional local algebras;

5.  local instruments $`\{\mathcal{I}_{a}^{\alpha}\}_{\alpha}`$ and $`\{\mathcal{J}_{b}^{\beta}\}_{\beta}`$;

6.  a probability rule evaluating the descended state on those instruments.

The phrase “fixed point” may refer to a fixed point of an auxiliary stabilization flow. Its parameter is not automatically physical time. Likewise, existence of a fixed point does not by itself imply that the associated Lorentzian theory is causal or that its state is entangled. The local-net and state hypotheses are separate rows.

## Why the state must not depend silently on both settings

An expression such as
``` math
\Psi^\ast=\Psi^\ast(a,b,\xi)
```
cannot simultaneously be treated as a complete premeasurement hidden state and as independent of $`a,b`$. There are only four coherent readings:

1.  $`\xi`$ is incomplete and the complete state includes $`\Psi^\ast(a,b,\xi)`$;

2.  the settings are boundary data in an atemporal global boundary-value problem;

3.  the construction is retrocausal;

4.  measurement independence is abandoned.

This paper uses a fifth, cleaner preparation branch: a common preparation selects $`\omega_\lambda`$ before $`a,b`$, and the settings choose only local instruments. The state may be nonseparable, but it is not recalculated from the two later settings. This is compatible with measurement independence and makes the remaining failure of Bell factorization explicit.

# Locality-preserving descent

Let $`\Pi_x`$ be an internal coherent projector acting fiberwise over $`x\in Y^4`$. Schematically, a descended observable has the form
``` math
\mathcal{D}_{\mathcal O}(A)
 =
 \int_{X^6}(\Pi A\Pi)(\,\cdot\,,u)\,d\nu_X(u),
```
where the integral is a bounded weak operator integral. The crucial condition is not merely boundedness of $`\Pi`$: $`\Pi`$ and the integral must preserve support in the base region $`\mathcal O`$.

<div id="ass:base-local" class="assumption">

**Assumption 4** (Base-local descent). *For every $`\mathcal O\subset Y^4`$,
``` math
\mathcal{D}_{\mathcal O}
 \bigl(\mathcal{A}_M(\mathcal O\times X^6)\bigr)
 \subseteq \mathcal{A}_Y(\mathcal O).
```
For spacelike $`\mathcal O_A,\mathcal O_B`$, representatives of the two weak operator integrals commute pairwise at every pair of internal points.*

</div>

<div id="lem:locality-descent" class="lemma">

**Lemma 5** (Locality descent). *Under upper algebraic locality and <a href="#ass:base-local" data-reference-type="ref+label" data-reference="ass:base-local">4</a>,
``` math
[\mathcal{D}_{\mathcal O_A}(A),\mathcal{D}_{\mathcal O_B}(B)]=0
```
for $`A\in\mathcal{A}_M(\widetilde{\mathcal O}_A)`$ and $`B\in\mathcal{A}_M(\widetilde{\mathcal O}_B)`$ whenever $`\mathcal O_A\perp\mathcal O_B`$.*

</div>

<div class="proof">

*Proof.* Using bounded weak integration and bilinearity of the commutator,
``` math
\begin{split}
 [\mathcal{D}_{\mathcal O_A}(A),\mathcal{D}_{\mathcal O_B}(B)]
 &=
 \int_{X^6}\!\!\int_{X^6}
 [(\Pi A\Pi)(u),(\Pi B\Pi)(v)]\,
 d\nu_X(u)d\nu_X(v).
\end{split}
```
Every integrand vanishes by upper locality and base-support preservation. The integral is therefore zero. ◻

</div>

<div class="remark">

*Remark 6*. A generic spatially nonlocal projector does not satisfy <a href="#ass:base-local" data-reference-type="ref+label" data-reference="ass:base-local">4</a>. Nor does a global fixed-point constraint automatically prove it. This is why locality descent must be stated as a theorem hypothesis and verified for the selected MTT operator.

</div>

# Local instruments and no-signaling

Let Alice’s and Bob’s local instruments be normal completely positive maps. Write their Heisenberg dual operations as $`\mathcal{I}_{a}^{\alpha\ast}`$ and $`\mathcal{J}_{b}^{\beta\ast}`$. The corresponding nonselective operations are
``` math
\mathcal{I}_a^\ast=\sum_\alpha\mathcal{I}_{a}^{\alpha\ast},
 \qquad
 \mathcal{J}_b^\ast=\sum_\beta\mathcal{J}_{b}^{\beta\ast}.
```
They are unital. Spacelike locality means that Bob’s nonselective operation acts trivially on Alice’s local observables, and conversely .

<div id="prop:no-signaling" class="proposition">

**Proposition 7** (Operational no-signaling from local instruments). *Let $`\omega_\lambda`$ be any normal, possibly nonseparable state on the joint algebra. If the two instruments are local in the preceding sense, then
``` math
p_\lambda(\alpha,\beta\mid a,b)
 :=
 \omega_\lambda\!\left(
 \mathcal{I}_{a}^{\alpha\ast}
 \mathcal{J}_{b}^{\beta\ast}(\mathbf 1)\right)
```
is operationally no-signaling. The same remains true after averaging over a setting-independent measure $`\rho(d\lambda)`$.*

</div>

<div class="proof">

*Proof.* Summing over Bob’s outcomes gives
``` math
\begin{split}
\sum_\beta p_\lambda(\alpha,\beta\mid a,b)
 &=
\omega_\lambda\!\left(
\mathcal{I}_{a}^{\alpha\ast}\mathcal{J}_b^\ast(\mathbf 1)\right)\\
 &=
\omega_\lambda\!\left(
\mathcal{I}_{a}^{\alpha\ast}(\mathbf 1)\right),
\end{split}
```
which is independent of $`b`$. The other marginal is analogous. Integration against $`\rho(d\lambda)`$ preserves both equalities. ◻

</div>

This result locates the absence of action at a distance precisely. A remote choice cannot control the local marginal. The proposition does not state that the joint state is separable or that its conditional probabilities factorize.

# Bell’s boundary

For dichotomic outcomes in $`\{-1,+1\}`$, define
``` math
E(a,b)
 =
 \sum_{\alpha,\beta=\pm1}
 \alpha\beta\,p(\alpha,\beta\mid a,b)
```
and
``` math
S=E(a,b)+E(a,b')+E(a',b)-E(a',b').
```

<div id="thm:chsh" class="theorem">

**Theorem 8** (CHSH under measurement independence and factorization). *Suppose $`\rho(d\lambda)`$ is independent of $`a,b`$ and the conditional probabilities factorize for almost every $`\lambda`$. Then
``` math
|S|\leq 2.
```*

</div>

<div class="proof">

*Proof.* Set
``` math
A_a(\lambda)=\sum_{\alpha=\pm1}\alpha\,
 p_A(\alpha\mid a,\lambda),
\qquad
 B_b(\lambda)=\sum_{\beta=\pm1}\beta\,
 p_B(\beta\mid b,\lambda),
```
so $`|A_a|,|B_b|\leq1`$. Factorization gives $`E(a,b)=\int A_a(\lambda)B_b(\lambda)\rho(d\lambda)`$. For every $`\lambda`$,
``` math
\begin{split}
 &\left|
 A_a(B_b+B_{b'})
 +A_{a'}(B_b-B_{b'})
 \right|\\
 &\hspace{4em}\leq
 |B_b+B_{b'}|+|B_b-B_{b'}|
 \leq2.
\end{split}
```
Integration proves the result. ◻

</div>

<div id="cor:required-nonfactorization" class="corollary">

**Corollary 9** (Required MTT nonfactorization). *If a selected MTT packet preserves measurement independence and produces $`|S|>2`$, Bell factorization fails on a set of nonzero $`\rho`$-measure.*

</div>

<div class="proof">

*Proof.* Otherwise <a href="#thm:chsh" data-reference-type="ref+label" data-reference="thm:chsh">8</a> would imply $`|S|\leq2`$. ◻

</div>

This is not a defect to be hidden. It is the mathematical content of the proposal: MTT may retain upper algebraic locality and no-signaling while its admissible state fails the classical screening-off condition. In Jarrett’s language, one must not conflate observed parameter independence with the full factorization package .

# The singlet benchmark

Take
``` math
\mathcal{H}=\mathbb{C}^2\otimes\mathbb{C}^2,
\qquad
 |\psi^-\rangle
 =
 \frac{|01\rangle-|10\rangle}{\sqrt2}.
```
Choose
``` math
A=\sigma_z,\qquad A'=\sigma_x,
```
``` math
B=\frac{\sigma_z+\sigma_x}{\sqrt2},
\qquad
 B'=\frac{\sigma_z-\sigma_x}{\sqrt2}.
```
The standard quantum packet gives
``` math
|S|=2\sqrt2
```
while its local marginals are independent of the remote settings . The observables on opposite tensor factors commute. This is the standard example of local commutativity, no-signaling, and state nonfactorization coexisting.

<div id="prop:conditional-realization" class="proposition">

**Proposition 10** (Conditional MTT realization). *Suppose one selected MTT source emits:*

1.  *a preparation-selected upper fixed-point state whose descent is $`|\psi^-\rangle\langle\psi^-|`$;*

2.  *the four displayed local measurement instruments;*

3.  *the probability functional used in <a href="#prop:no-signaling" data-reference-type="ref+label" data-reference="prop:no-signaling">7</a>;*

4.  *the locality hypotheses of <a href="#lem:locality-descent" data-reference-type="ref+label" data-reference="lem:locality-descent">5</a>.*

*Then the descended packet is no-signaling, reaches $`|S|=2\sqrt2`$, and cannot satisfy Bell factorization under measurement independence.*

</div>

<div class="proof">

*Proof.* No-signaling follows from <a href="#prop:no-signaling" data-reference-type="ref+label" data-reference="prop:no-signaling">7</a>; the CHSH value is the benchmark calculation above; nonfactorization follows from <a href="#cor:required-nonfactorization" data-reference-type="ref+label" data-reference="cor:required-nonfactorization">9</a>. ◻

</div>

The proposition is a commuting completion contract, not a derivation of its premises. In particular, choosing MTT data because their descent equals the singlet would be a reconstruction or replay, not an independent prediction.

# Interpretation and consequences: what projection explains

Projection can make the origin of correlations less visible. Two distant four-dimensional observables may be restrictions of one globally constrained upper state. From the lower description alone the correlations can then look like a direct relation between the outcomes, even though no signal is sent during the measurements.

Projection alone, however, does not select:

- a nonseparable upper state;

- a probability measure on preparations;

- the Born functional;

- the local instrument family;

- the strength or sign of a Bell correlator.

The accurate phrase is therefore *descent of upper nonseparability*, not “creation of nonlocality by projection.” The explanatory work belongs to the source theorem that selects the global admissible state and its probability/instrument packet.

# Comparison with Kaluza–Klein and local QFT

An ordinary Kaluza–Klein reduction can preserve base locality, but locality does not force the state to factorize. A local four-dimensional quantum field theory may possess entangled states and Bell-violating correlations while its spacelike algebras commute. The earlier claim that zero-mode reduction by itself yields Bell factorization was therefore incorrect.

The possible MTT contribution is different. MTT proposes that a restricted class of globally coherent states is selected by admissibility and fixed-point conditions. If that selection can be derived from the same upper geometry that supplies the local net and descent, it could explain why a particular nonseparable state occurs. Until that source theorem is supplied, MTT and standard local quantum theory share the same operational reconciliation of Bell violation with no-signaling; MTT adds a conditional selection mechanism, not yet a completed prediction.

# Networks and multipartite experiments

The distinction scales to several laboratories. Pairwise commuting local algebras can carry a globally nonseparable state, and local instruments then preserve operational no-signaling. Classical network inequalities impose additional source-independence factorizations. A violation shows that at least one declared network factorization fails; it does not prove a superluminal signal.

No theorem in this paper states that MTT realizes every quantum network correlation. Such a claim would require a selected multipartite state, source-independence conventions, local instruments, and the corresponding probability functional for each network.

# Relation to temporal Bell inequalities

Spatial Bell and temporal Leggett–Garg experiments test different contracts. The spatial case uses separated laboratories, two-way no-signaling, and Bell factorization. The temporal case uses sequential instruments on one system and permits forward disturbance. The revised temporal Bell paper therefore treats its Leggett–Garg packet separately .

A common upper fixed-point language may eventually connect the two, but a unification theorem would have to preserve both operational probability laws and their different causal constraints. Merely using the word “projection” in both settings does not provide that theorem.

# Completion and falsification contract

For the upper-local account to become a physical MTT result, one same-source packet must provide:

1.  a selected upper Lorentzian local net or hyperbolic field system;

2.  a preparation-selected admissible fixed-point state;

3.  proof that the preparation measure is independent of later settings;

4.  a base-local coherent projector and descent satisfying <a href="#ass:base-local" data-reference-type="ref+label" data-reference="ass:base-local">4</a>;

5.  local completely positive instruments representing the actual detectors;

6.  a selected probability functional;

7.  a calculated CHSH packet with uncertainty and provenance.

The proposal fails in the following clear cases:

- the selected descent spreads support across spacelike base regions;

- the remote setting changes an observed local marginal;

- the complete state is claimed to be measurement-independent and factorizing while $`|S|>2`$;

- the state or probability rows are inserted from observed Bell data and then reported as predictions;

- the fixed-point solution depends on both settings without declaring a global-boundary, retrocausal, contextual, or measurement-dependent branch.

# Conclusion

The upper-world perspective can remove the need for a dynamical “spooky action” between the measurements, but it does not restore Bell factorization. The coherent statement is:
``` math
\boxed{
\text{upper-local dynamics}
+
\text{microcausal descent}
+
\text{local instruments}
+
\text{global nonseparable state}.
}
```
This package yields no operational superluminal signal. If it reproduces a Bell violation while measurement independence is retained, its complete probabilities are necessarily nonfactorizing.

That is already a useful reconciliation. What remains specifically MTT is to derive the nonseparable fixed-point state, the probability functional, and the detector instruments from one selected upper source rather than importing the quantum benchmark. The present paper states that target without mistaking a perspective shift for a completed source theorem.
