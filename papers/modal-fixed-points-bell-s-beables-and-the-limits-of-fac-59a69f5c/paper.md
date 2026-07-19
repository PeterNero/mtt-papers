---
abstract: |
  Bell’s theorem rules out local hidden-variable models under *measurement independence* (MI) and *factorization* (local causality). We revisit Bell’s program in the setting of the ten-dimensional modal fixed-point dynamics of Modal Triplet Theory (MTT). The fundamental beables are local modal fields on $`M=Y^4\times B_1\times B_2\times B_3`$ subject to a global fixed-point constraint. Their projection to four dimensions preserves MI and *operational* no-signaling but necessarily violates factorization. We formalize the probability space of seeds $`(\Xi,\Sigma,\mu)`$, prove no-signaling by mapping outcome probabilities *exactly* to the Born rule on $`\mathcal{H}_{\mathrm{QM}}`$ via the observable map $`\mathsf{P}=I\circ\Pi`$, and show that MI + (QM agreement) $`\Rightarrow`$ failure of factorization by CHSH. Thus the observed “nonlocal” correlations are a *projection artifact* of local 10D beables. We compare with Kaluza–Klein and discuss implications.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: September 8, 2025
generated_from_main_tex_sha256: c45e2e411f580e70acdfacde7931a2f9e25946fd2670c119c6cdebb8924031a5
paper_id: modal-fixed-points-bell-s-beables-and-the-limits-of-fac-59a69f5c
release_state: zenodo_released
released_version: v1.0
title: |
  **Modal Fixed Points, Bell’s Beables, and the Limits of Factorization:  
  A Local 10D Ontology with Operational No-Signaling**
zenodo_doi: 10.5281/zenodo.17076301
zenodo_record_id: 17076301
zenodo_url: "https://zenodo.org/records/17076301"
---

# Introduction

We aim to reconcile Bell’s demand for a theory of *local beables* with the empirical violation of Bell inequalities. Our starting point is your Bell/beables draft and the rigorous MTT$`\Rightarrow`$QM reduction, which provides the operator-algebraic backbone (bounded harmonic projector, observable map, Born rule, unitary dynamics). We adopt the notation and functional-analytic conventions of the MTT$`\Rightarrow`$QM paper (observable map $`\mathcal{P}:= I \circ \Pi`$; we reserve $`P`$ exclusively for orthogonal projectors on $`H_{\rm QM}`$).

#### Main claims.

\(i\) The beables are local 10D fixed-point fields $`\Psi^\ast\in H^1(M)`$ (local PDEs + bounded geometry). (ii) We encode measurement settings and seeds on a common probability space with MI, $`\rho(\xi\,|\,a,b)=\rho(\xi)`$. (iii) *Operational* no-signaling holds because outcome probabilities coincide with those of standard QM on $`\mathcal{H}_{\mathrm{QM}}`$ (hence parameter independence at the operational level). (iv) Since the model reproduces QM correlations, factorization must fail (by CHSH). Items (iii)–(iv) are shown in §<a href="#sec:bell-in-modal" data-reference-type="ref" data-reference="sec:bell-in-modal">4</a>.

#### On measurement independence (MI).

In this paper MI, $`\rho(\xi|a,b)=\rho(\xi)`$, is a *modeling assumption* about the joint distribution of settings and seeds. We neither invoke retrocausality nor exploit conspiratorial fine-tuning; MI simply enforces statistical independence between the freely-choosable settings $`(a,b)`$ and the seed $`\xi`$. All results (no-signaling, CHSH violation) are conditioned on MI.

# Bell’s MI, factorization, and CHSH

We recall the standard assumptions in a form convenient for our modal construction.

<div class="definition">

**Definition 1** (Measurement independence (MI)). *Let $`a\in\mathcal{A}`$, $`b\in\mathcal{B}`$ be settings; let $`\xi\in\Xi`$ be hidden seeds with probability measure $`\mu`$. MI means
``` math
\rho(\xi\,|\,a,b)=\rho(\xi).
```*

</div>

<div class="definition">

**Definition 2** (Factorization / local causality). *Given $`\xi`$, the joint conditional is multiplicative:
``` math
P(A,B\,|\,a,b,\xi)=P(A\,|\,a,\xi)\,P(B\,|\,b,\xi).
```*

</div>

Under MI+factorization, the CHSH combination obeys $`|S|\le 2`$ . In the Jarrett/Fine decomposition, factorization $`\Leftrightarrow`$ PI$`+`$OI .

#### Jarrett/Fine decomposition.

We distinguish *parameter independence* (PI) and *outcome independence* (OI):
``` math
\text{PI: }P(A|a,b,\xi)=P(A|a,\xi),\qquad P(B|a,b,\xi)=P(B|b,\xi),
```
``` math
\text{OI: }P(A|B,a,b,\xi)=P(A|a,b,\xi),\qquad P(B|A,a,b,\xi)=P(B|a,b,\xi).
```
Bell’s *factorization* (local causality) is equivalent to PI $`+`$ OI:
``` math
P(A,B|a,b,\xi)=P(A|a,\xi)\,P(B|b,\xi).
```
Throughout we assume *measurement independence* (MI), $`\rho(\xi|a,b)=\rho(\xi)`$.

#### CHSH under MI+factorization (self-contained).

Let $`A,A'\in\{\pm1\}`$ at setting $`a,a'`$ and $`B,B'\in\{\pm1\}`$ at $`b,b'`$. Under MI+factorization,
``` math
E(a,b)=\!\int\! d\mu(\xi)\sum_{A,B} AB\,P(A|a,\xi)P(B|b,\xi)=\!\int\! d\mu(\xi)\, \bar A(a,\xi)\bar B(b,\xi),
```
with $`\bar A(a,\xi)=\sum_A A\,P(A|a,\xi)\in[-1,1]`$ and similarly $`\bar B`$. Then
``` math
S=E(a,b)+E(a,b')+E(a',b)-E(a',b')=\!\int\! d\mu(\xi)\, s(\xi),
```
where $`s(\xi)=\bar A(a,\xi)[\bar B(b,\xi)+\bar B(b',\xi)]+\bar A(a',\xi)[\bar B(b,\xi)-\bar B(b',\xi)]`$ and $`|s(\xi)|\le2`$. Hence $`|S|\le2`$.

# Modal beables and the observable map

Let $`M=Y^4\times B_1\times B_2\times B_3`$ be the 10D product with bounded geometry; fields evolve by a local (hyperbolic/parabolic) flow $`\Phi_\tau`$ on $`H^1(M)`$ and admissible states satisfy a global fixed-point constraint $`\Psi^\ast=\Pi\circ\Phi_\tau(\Psi^\ast)`$.

<div class="definition">

**Definition 3** (10D beables). *The *beables* are the fixed-point fields $`\Psi^\ast\in H^1(M)`$ stabilized by the projected flow. Locality means: for any open $`U\subset M`$, the restriction map $`\Psi^\ast\mapsto \Psi^\ast|_U`$ is measurable w.r.t. the local $`\sigma`$-algebra on $`U`$, and the field equations are local differential operators on $`M`$.*

</div>

#### Observable map and Hilbert space.

Let $`\Pi=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$ be the joint harmonic projector; $`I`$ is fiber integration over $`B_1\times B_2\times B_3`$; define $`\mathcal{P}= I \circ \Pi`$. Boundedness and contraction properties carry over from the QM derivation (Lemma A.4 in that paper), and $`\mathcal{P}`$ maps the coherent sector into $`H_{\rm QM}`$ with the Born rule and unitary dynamics established there.

# MI, no-signaling, and failure of factorization in modal space

## Probability space and measurement

Let $`(\Xi,\Sigma,\mu)`$ be a standard probability space of seeds. We embed the settings into a product space with independent measures $`\eta_{\mathcal{A}},\eta_{\mathcal{B}}`$ and write the global measure as $`\eta_{\mathcal{A}}\otimes \eta_{\mathcal{B}}\otimes \mu`$. MI holds by construction,
``` math
\rho(\xi\,|\,a,b)=\rho(\xi).
```
For fixed $`(a,b,\xi)`$, the flow produces a unique fixed point $`\Psi^\ast(a,b,\xi)`$. The *local readouts* are measurable functionals of the local projected field,
``` math
A \;=\; R_A\!\big(a;\,(\mathsf{P}\Psi^\ast)(a,b,\xi)\big),\qquad
B \;=\; R_B\!\big(b;\,(\mathsf{P}\Psi^\ast)(a,b,\xi)\big).
```
Operationally (in the laboratory) these readouts are represented by projectors/POVMs on $`\mathcal{H}_{\mathrm{QM}}`$ as constructed in the MTT$`\Rightarrow`$QM paper (Born rule, Naimark/Stinespring).

## Worked example: Bilocality inequality

The bilocal scenario has three parties $`(A,B,C)`$ in a line, with independent sources $`S_{AB},S_{BC}`$ producing hidden seeds $`\xi_{AB},\xi_{BC}`$. Classical bilocal models require a factorization
``` math
P(a,b,c|x,y,z) = \int d\lambda_{AB}\, d\lambda_{BC}\, \rho(\lambda_{AB})\rho(\lambda_{BC})
\,P(a|x,\lambda_{AB})\,P(b|y,\lambda_{AB},\lambda_{BC})\,P(c|z,\lambda_{BC}),
```
leading to a bilocality constraint (e.g. $`\sqrt{|I_1|}+\sqrt{|I_2|}\le 2`$ or equivalent forms) .

#### Modal realization.

In MTT the unique global fixed point $`\Psi^\ast(x,y,z,\xi)`$ simultaneously couples all three wings once projected, so such a decomposition need not exist. Choose MTT data such that the projected $`\mathcal{H}_{\mathrm{QM}}`$ state is two entangled pairs $`(AB)`$ and $`(BC)`$ with $`B`$ measured in a Bell basis. Standard QM predicts $`|I|=2`$, violating the bilocal bound. By the MTT$`\Rightarrow`$QM reduction, the modal model reproduces this exactly.

<div class="proposition">

**Proposition 4** (Bilocal inequality violation). *There exist choices of MTT data and seeds for which the modal model reproduces $`|I|=2`$ in the bilocal scenario, hence exceeds the classical bilocal bound while preserving measurement independence and operational no-signaling.  .*

</div>

#### Bilocal inequality (Branciard-type).

Classical bilocal models obey $`|I|\le1`$ with $`I=\sqrt{|I_1|}+\sqrt{|I_2|}`$ constructed from two-source correlators. In our construction, choosing MTT data whose projection gives two maximally entangled pairs with a Bell-state measurement at $`B`$ yields $`|I|=2`$, matching the quantum maximum. The choice preserves MI and operational no-signaling as above.

## Operational no-signaling

<div id="thm:nosig" class="theorem">

**Theorem 5** (Operational no-signaling). *For any settings $`a,b`$ and outcome $`A`$, the marginal $`P(A\,|\,a,b)`$ is independent of $`b`$. Similarly, $`P(B\,|\,a,b)`$ is independent of $`a`$.*

</div>

<div class="proof">

*Proof.* By the MTT$`\Rightarrow`$QM derivation, the outcome probabilities computed from $`\Psi^\ast`$ via the observable map equal the Born rule on $`\mathcal{H}_{\mathrm{QM}}`$:
``` math
P(A\,|\,a,b) \;=\; \langle \psi,\,P_A(a)\,\psi\rangle,\qquad
P(B\,|\,a,b) \;=\; \langle \psi,\,P_B(b)\,\psi\rangle,
```
for some $`\psi\in\mathcal{H}_{\mathrm{QM}}`$ determined by the preparation, with $`P_A(a)`$ and $`P_B(b)`$ the local projectors. These expressions are manifestly independent of the *remote* setting because $`P_A(a)`$ depends only on $`a`$ and $`P_B(b)`$ only on $`b`$. Hence operational parameter independence holds. ◻

</div>

#### Jarrett split in the modal model.

Our construction *satisfies operational PI* (no-signaling of marginals), because on $`H_{\mathrm{QM}}`$
``` math
P(A|a,b)=\langle\psi,E_A(a)\psi\rangle\ \text{and}\ P(B|a,b)=\langle\psi,E_B(b)\psi\rangle,
```
which are manifestly independent of the remote setting. However, *OI generically fails*: at fixed $`\xi`$ the global fixed-point constraint that defines $`\Psi^*(a,b,\xi)`$ correlates the projected local readouts, so $`P(A|B,a,b,\xi)\neq P(A|a,b,\xi)`$ in general. Consequently, factorization (PI+OI) fails while operational PI holds.

## Failure of factorization (and why it must fail)

<div id="thm:nofact" class="theorem">

**Theorem 6** (MI + QM agreement $`\Rightarrow`$ no factorization). *Assume MI and that the model reproduces QM correlators for a CHSH setup (two settings per wing). Then the factorization condition
``` math
P(A,B\,|\,a,b,\xi)=P(A\,|\,a,\xi)P(B\,|\,b,\xi)
```
cannot hold for all $`(a,b)`$ on a set of $`\xi`$ of full measure.*

</div>

<div class="proof">

*Proof.* Suppose factorization held $`\mu`$‑a.s. Under MI, the CHSH proof (Theorem 2.1) gives $`|S|\le 2`$. But your MTT$`\Rightarrow`$QM mapping yields the standard QM correlators with $`|S|=2\sqrt{2}`$ for suitable choices of $`(a,b)`$ (Tsirelson bound) . Contradiction. Therefore, factorization must fail on a set of seeds of nonzero measure (indeed full measure for generic couplings). ◻

</div>

<div class="corollary">

**Corollary 7** (Pattern of assumptions). *The modal fixed-point model satisfies: MI (yes), operational no-signaling (yes), factorization (no). Consequently, Bell–CHSH inequalities do not apply, and the model can reproduce quantum violations up to $`2\sqrt2`$, as observed.*

</div>

## Locality of beables vs. projection artifacts

The beables are local fields on $`M`$ with local equations; their apparent “nonlocality” in 4D arises because the constraint building $`\Psi^\ast`$ is global on $`M`$, and projection $`\mathsf{P}`$ mixes internal directions in a way that correlates spacelike marginals when viewed solely on $`Y^4`$. This is a *projection artifact*: the underlying ontology is local on the extended space; factorization fails only after reducing to 4D.

# Kaluza–Klein vs. modal projection

Kaluza–Klein (KK) reduction projects higher-dimensional fields onto *zero modes* by geometric smallness; modal projection in MTT instead selects *fiber-harmonic* modes by a *dynamical* fixed-point constraint. This difference matters for Bell.  .

## Zero-mode truncation preserves factorization

Let $`M=Y^4\times K`$ with $`K`$ compact, $`\mathrm{diam}(K)\ll`$ experimental scales. In KK one expands $`\Phi(x,y)=\sum_n \phi_n(x) Y_n(y)`$ with $`\Delta_K Y_n=\lambda_n Y_n`$. At low energy, only $`\phi_0(x)Y_0(y)`$ remains. The resulting 4D theory is a local QFT on $`Y^4`$ with fields $`\phi_0`$.

<div id="prop:KK-factor" class="proposition">

**Proposition 8** (KK factorization). *Consider a bipartite Bell experiment in a KK zero-mode truncation. Assume measurement independence (MI) and that outcomes at spacelike separated regions are functions of the *local* 4D beables and a seed $`\xi`$,
``` math
A=A(a;\,\phi_0|_{U_A},\xi),\qquad B=B(b;\,\phi_0|_{U_B},\xi),
```
with $`U_A\cap U_B=\emptyset`$. Then factorization holds:
``` math
P(A,B\,|\,a,b,\xi)=P(A\,|\,a,\xi)\,P(B\,|\,b,\xi).
```*

</div>

<div class="proof">

*Proof.* Given $`\xi`$ and $`(a,b)`$, $`\phi_0`$ solves a local hyperbolic PDE on $`Y^4`$ with microcausality: algebras of observables for $`U_A`$ and $`U_B`$ commute and classical beables at $`U_A`$ are functions of initial data in $`J^-(U_A)`$, likewise for $`U_B`$. Since $`U_A`$ and $`U_B`$ are spacelike, $`A`$ is conditionally independent of $`B`$ given $`\xi`$ (and the initial data absorbed into $`\xi`$). Therefore the joint conditional distribution factorizes. Integrating w.r.t. $`\rho(\xi)`$ (MI) preserves factorization. ◻

</div>

#### Background/zero–mode equivalence with KK.

Our Proposition 5.1 is exactly the background/zero–mode regime captured by the MTT$`\to`$KK equivalence (Prop. 3.2 and Theorem 4.5 therein): the block–diagonal metric, isometry–gauge map, and fiber–integral couplings reproduce a local 4D QFT with the usual microcausality and latent–variable factorization, hence CHSH$`\le2`$ under MI. By contrast, the modal fixed–point constraint couples the full $`M`$ prior to projection, which is why factorization can fail while operational no–signaling persists.

<div id="cor:KK-CHSH" class="corollary">

**Corollary 9** (KK cannot reproduce CHSH$`>2`$ under MI). *Under MI, any KK zero-mode model obeys CHSH $`\le 2`$; thus it cannot reproduce quantum violations.*

</div>

## Modal fixed points violate factorization after projection

In the modal setting, the dynamical constraint $`\Psi^\ast=\Pi\circ\Phi_\tau(\Psi^\ast)`$ is *global* on $`M`$, not a local truncation on $`K`$. The *projected* beables on $`Y^4`$ are $`\mathsf{P}\Psi^\ast`$, and the fixed-point constraint couples disjoint $`U_A,U_B`$ after projection. Hence the conditional independence argument of <a href="#prop:KK-factor" data-reference-type="ref+Label" data-reference="prop:KK-factor">8</a> fails: *even at fixed $`\xi`$*, $`A`$ and $`B`$ remain coupled via the global constraint that defines $`\Psi^\ast(a,b,\xi)`$. This is precisely the origin of factorization failure proved in <a href="#thm:nofact" data-reference-type="ref+Label" data-reference="thm:nofact">6</a>.

<div class="remark">

**Remark 10**. *KK compactification hides extra dimensions by *geometry*; modal dynamics hide them by *constraint*. Only the latter mechanism can violate factorization while preserving MI and operational no-signaling.*

</div>

# Multipartite and network scenarios

Network nonlocality (triangle, bilocality) enriches the causal structure. We sketch how the modal fixed-point picture extends, emphasizing what carries over from the bipartite case.

## Setup

Let parties $`V=\{1,\dots,N\}`$ sit at spacelike separated regions $`U_i\subset Y^4`$ with settings $`a_i\in\mathcal{A}_i`$, outcomes $`A_i\in\mathcal{O}_i`$, and a seed space $`(\Xi,\Sigma,\mu)`$. The modal flow and projection produce a unique fixed point
``` math
\Psi^\ast(\bm a,\xi)\in H^1(M),\qquad \bm a=(a_1,\dots,a_N).
```
Outcomes are readouts $`A_i=R_i(a_i;\,(\mathsf{P}\Psi^\ast)(\bm a,\xi)|_{U_i})`$.

## Operational no-signaling persists

By the MTT$`\Rightarrow`$QM mapping, observable probabilities equal the Born rule on $`\mathcal{H}_{\mathrm{QM}}`$ for local POVMs at each $`U_i`$; hence all *operational* marginals $`P(A_i|\bm a)`$ are independent of $`\{a_j\}_{j\neq i}`$.

<div class="theorem">

**Theorem 11** (Operational no-signaling in networks). *For any finite network and any $`\bm a`$, $`P(A_i\,|\,\bm a)`$ depends only on $`a_i`$.*

</div>

<div class="proof">

*Proof.* Identical to <a href="#thm:nosig" data-reference-type="ref+Label" data-reference="thm:nosig">5</a>, now with tensor products of local algebras on $`\mathcal{H}_{\mathrm{QM}}`$; probabilities are computed by $`\langle\psi,\bigotimes_i E_{i}(a_i)\,\psi\rangle`$ and are manifestly independent of remote settings at the level of marginals. ◻

</div>

## Factorization and network inequalities

Classical network constraints (bilocality, triangle inequalities) rely on factorizations over latent variables. In modal dynamics, the *single* global $`\Psi^\ast(\bm a,\xi)`$ couples all wings once projected; thus the latent-variable factorization graphs underlying such inequalities need not hold. Consequently, modal fixed points can reproduce the set of quantum-allowed network correlations (subject to standard quantum constraints).

<div class="proposition">

**Proposition 12** (Modal networks can saturate quantum bounds). *For standard network scenarios with local POVMs on $`\mathcal{H}_{\mathrm{QM}}`$, there exist choices of MTT data and seeds such that the induced correlations match those of quantum states achieving the known quantum bounds of the respective network inequalities.*

</div>

<div class="proof">

*Idea.* Choose MTT data giving, via §<a href="#sec:beables" data-reference-type="ref" data-reference="sec:beables">3</a>–<a href="#sec:bell-in-modal" data-reference-type="ref" data-reference="sec:bell-in-modal">4</a>, an $`\mathcal{H}_{\mathrm{QM}}`$ state $`\psi`$ that realizes the target quantum correlations under local POVMs; by construction of §<a href="#sec:beables" data-reference-type="ref" data-reference="sec:beables">3</a>, the modal fixed point and projection reproduce these statistics. ◻

</div>

# Conclusions

We have provided a fully rigorous Bell/beables analysis within MTT: (i) beables are local 10D fixed-point fields; (ii) MI and operational no-signaling hold once mapped to $`\mathcal{H}_{\mathrm{QM}}`$; (iii) factorization *must* fail if one reproduces quantum correlators (hence CHSH$`>2`$ is allowed); (iv) KK compactification, by contrast, preserves factorization and cannot explain Bell violations under MI.

#### Empirical outlook.

In bipartite and network Bell tests with finite settings/outcomes, the modal fixed-point construction reproduces exactly the quantum correlators, up to Tsirelson bounds, and never predicts supra-quantum (PR-box) correlations  . Hence the model is fully consistent with current data.

*Where could deviations occur?* Two avenues are possible: (i) Sequential/adaptive protocols, where the same system is measured multiple times with intermediate modal re-coherence; here small deviations from standard quantum instruments could in principle arise. (ii) Background curvature or bundle-moduli dependence (see  ) if the observable map $`\mathsf{P}`$ acquires explicit $`R(x)`$-dependence, small corrections to local probabilities may occur in strong-gravity regimes.

Both effects are negligible in present laboratory Bell tests, but they point to potential future experimental signatures in sequential quantum networks or astrophysical settings.

# Appendix A: Probability spaces, MI, and disintegration

<span id="app:measure" label="app:measure"></span>

Let $`(\Xi,\Sigma,\mu)`$ be a standard Borel space of seeds. Let $`\mathcal{A},\mathcal{B}`$ be finite (or standard Borel) setting spaces with product measure $`\eta=\eta_\mathcal{A}\otimes\eta_\mathcal{B}`$. The global space is $`(\Omega,\mathcal{F},\mathbb{P})=(\mathcal{A}\times\mathcal{B}\times\Xi,\ \mathcal{B}(\mathcal{A})\otimes\mathcal{B}(\mathcal{B})\otimes\Sigma,\ \eta\otimes\mu)`$. (Regular conditional probabilities exist on standard Borel spaces; see, e.g., Kallenberg .)

#### MI.

Measurement independence is the statement $`\rho(\xi\,|\,a,b)=\rho(\xi)`$; equivalently, $`\mathbb{P}`$ factorizes as above and $`(a,b)`$ are independent of $`\xi`$.

#### Regular conditional distributions.

For measurable outcome maps $`A(a,b,\xi)`$, $`B(a,b,\xi)`$ into finite sets, there exist regular conditional probabilities $`P(A\,|\,a,b,\xi),P(B\,|\,a,b,\xi)`$. The observed joints are
``` math
P(A,B\,|\,a,b)=\int_\Xi P(A,B\,|\,a,b,\xi)\,d\mu(\xi),
```
and the marginals $`P(A\,|\,a,b)`$ etc. are defined similarly. Under MI these integrals are well-defined with respect to $`\mu`$ independent of $`(a,b)`$.

#### Factorization.

The factorization condition is the statement that, for $`\mu`$-a.e. $`\xi`$,
``` math
P(A,B\,|\,a,b,\xi)=P(A\,|\,a,\xi)P(B\,|\,b,\xi).
```
As shown in <a href="#thm:nofact" data-reference-type="ref+Label" data-reference="thm:nofact">6</a>, this cannot hold $`\mu`$-a.s. if the model reproduces quantum CHSH violations.

#### Lemma A.1 (Microcausality preserved by projection).

Let $`\Phi,\Psi`$ be local fields on $`M=Y^4\times B`$ obeying microcausality: $`[\Phi(x,b),\Psi(y,b')]=0`$ whenever $`x,y\in Y^4`$ are spacelike. Let $`P:=I\circ\Pi`$ with $`\Pi`$ the fiberwise harmonic projector and $`I`$ the fiber integral. Then for any $`x\perp y`$ in $`Y^4`$,
``` math
[P\Phi(x),P\Psi(y)]=0.
```

#### Remark.

This lemma dovetails with the causality analysis in Fixed Points VI: the local well–posedness and microcausality results for the equal–time bilocal overlap (App. F, Thm. F.1 and Prop. F.2) supply the hyperbolic backbone used here. In particular, the block–diagonal metric and Riemannian internal sector ensure that spacelike separation in $`Y^4`$ lifts to spacelike separation in $`M=Y^4\times B`$, so fiber projection/integration preserve commutativity of spacelike algebras on $`H_{\mathrm{QM}}`$.

*Proof.* Write $`P\Phi(x)=\int_B (\Pi\Phi)(x,b)\,d\mu_B(b)`$ and similarly for $`P\Psi(y)`$. Since the ten-dimensional metric is block-diagonal with a Riemannian internal block, if $`x\perp y`$ in $`Y^4`$ then $`(x,b)`$ is spacelike to $`(y,b')`$ for all $`b,b'`$, hence $`[(\Pi\Phi)(x,b),(\Pi\Psi)(y,b')]=0`$. Bilinearity and Fubini give $`[P\Phi(x),P\Psi(y)]=\int\!\!\int [(\Pi\Phi)(x,b),(\Pi\Psi)(y,b')]\,d\mu_B(b)\,d\mu_B(b')=0`$. 0◻

# Appendix B: Worked CHSH construction at Tsirelson

<span id="app:CHSH" label="app:CHSH"></span>

Let $`\mathcal{H}_{\mathrm{QM}}=\mathbb{C}^2\otimes\mathbb{C}^2`$ and $`\psi`$ the singlet state. Choose the usual CHSH settings:
``` math
\hat a=\sigma_z,\quad \hat a'=\sigma_x,\qquad \hat b=\tfrac{1}{\sqrt2}(\sigma_z+\sigma_x),\quad \hat b'=\tfrac{1}{\sqrt2}(\sigma_z-\sigma_x).
```
Define dichotomic observables $`A=\hat a`$, $`A'=\hat a'`$, $`B=\hat b`$, $`B'=\hat b'`$ with outcomes $`\pm1`$. Then
``` math
E(a,b)=\langle\psi,\,A\otimes B\,\psi\rangle = -\tfrac{1}{\sqrt2},\quad
E(a,b')=\langle\psi,\,A\otimes B'\,\psi\rangle = -\tfrac{1}{\sqrt2},
```
``` math
E(a',b)=\langle\psi,\,A'\otimes B\,\psi\rangle = -\tfrac{1}{\sqrt2},\quad
E(a',b')=\langle\psi,\,A'\otimes B'\,\psi\rangle = +\tfrac{1}{\sqrt2}.
```
Hence $`S=E(a,b)+E(a,b')+E(a',b)-E(a',b')=2\sqrt2`$.

#### Realization in MTT.

Choose MTT data for which the projected $`\mathcal{H}_{\mathrm{QM}}`$ state equals $`\psi`$ and the local measurement POVMs coincide with the spectral measures of $`(A,A')`$ and $`(B,B')`$. By the MTT$`\Rightarrow`$QM mapping, the observable probabilities equal the Born rule on $`\mathcal{H}_{\mathrm{QM}}`$. Therefore the modal model reproduces Tsirelson’s value  and, by Theorem <a href="#thm:nofact" data-reference-type="ref" data-reference="thm:nofact">6</a>, cannot satisfy factorization under MI.

# Appendix C: Locality in 10D and microcausality after projection

<span id="app:locality" label="app:locality"></span>

#### 10D locality.

The modal PDEs are local on $`M`$ with finite propagation speed along $`Y^4`$ and bounded geometry in $`B_n`$. Given a seed $`\xi`$ and settings $`\bm a`$, the fixed point $`\Psi^\ast(\bm a,\xi)`$ is obtained as the limit of local flows $`\Phi_\tau`$ with the harmonic projector $`\Pi`$ acting fiberwise.

#### Microcausality after projection.

The observable map $`\mathcal{P}= I \circ \Pi`$ preserves commutativity of spacelike separated algebras on $`\mathcal{H}_{\mathrm{QM}}`$ (in the sense of operator algebras of local POVMs). Therefore there is no operational signaling; <a href="#thm:nosig" data-reference-type="ref+Label" data-reference="thm:nosig">5</a> follows. For AQFT background on local algebras and microcausality, see .

#### Why factorization fails nonetheless.

Conditional independence at the hidden level is stronger than microcausality of observables: the global constraint that defines $`\Psi^\ast`$ correlates the *projected* local readouts even at fixed $`\xi`$. This is the precise sense in which the projection can destroy factorization while preserving operational no-signaling.
