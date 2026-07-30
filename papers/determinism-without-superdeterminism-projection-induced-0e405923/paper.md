---
abstract: |
  A deterministic microscopic evolution need not define a closed deterministic law for a reduced state. The exact obstruction is factorization: for a map $`\Phi:\mathcal U\to\mathcal U`$ and projection $`P:\mathcal U\to\mathcal X`$, a reduced map exists precisely when $`P\Phi`$ is constant on every fiber of $`P`$. Probability does not follow from failure of this condition. After a preparation measure is supplied, regular conditional measures on the fibers define a one-step kernel. That kernel is Dirac exactly when the next reduced state is conditionally almost surely constant, a weaker statement than global fiber constancy. We give finite counterexamples proving that the same projection and microdynamics can induce different kernels under different preparations and that a stationary projection of deterministic dynamics need not be Markov. Thus a stochastic or Markov effective theory requires a measure, a closure theorem, and often a scaling limit. Existing deterministic homogenization results provide such limits under declared assumptions; projection alone does not. We also prove a coupled-basin contraction theorem: once a record basin is selected, a nonnegative influence matrix with spectral radius below one gives geometric joint stabilization. This does not select the basin. Finally, determinism and superdeterminism are separated. In a Bell experiment, measurement independence, Bell factorization, and operational no-signaling are distinct conditions. The stated MTT route retains measurement independence and upper/base locality while allowing a nonseparable state to violate Bell factorization. Its selected state, instruments, and probability source remain completion obligations.
author:
- Peter Nero
current_version: v3
date: July 2026, Version 3
generated_from_main_tex_sha256: bd4f82b83fc45c96e8a7bfc639335f0bb9b282a9515f8d0c0c60763feb9edca5
paper_id: determinism-without-superdeterminism-projection-induced-0e405923
release_state: zenodo_released
released_version: v3
title: |
  Deterministic Microdynamics, Projected Laws,
  and the Superdeterminism Boundary
  Factorization, Conditional Kernels, Markov Closure, and Stabilization in MTT
zenodo_doi: 10.5281/zenodo.21665959
zenodo_record_id: 21665959
zenodo_url: "https://zenodo.org/records/21665959"
---

# Version 3 Revision Note

Supersedes
Version 2, released in January 2026 as *Determinism Without Superdeterminism: Projection-Induced Stochasticity, Non-Randomness, and Cascading Stabilization in Modal Triplet Theory*.

Reason
Version 2 treated a Dirac conditional kernel as global fiber invariance, promoted a one-step conditional law to a Markov process, and described projection as generating stochasticity. Its Gaussian OU assumption did not derive noise from deterministic dynamics, its selection-potential tail claim lacked the required process-level hypotheses, and its cascading stabilization corollary had no coupled contraction estimate. It also described superdeterminism imprecisely.

Resolution
This version separates algebraic descent, almost-sure descent, preparation-dependent kernels, Markov closure, and homogenization. It adds exact counterexamples, replaces the unsupported cascade by a spectral-radius contraction theorem, and aligns the Bell discussion with the corrected locality, measurement-independence, and factorization analysis.

Retained result
The fiber-factorization criterion remains exact: determinism upstairs need not close on a projected state. Structured effective probability and robust downstream stabilization are possible after their missing sources and hypotheses are supplied.

Remaining boundary
MTT does not yet select a universal preparation measure, prove Markov closure for arbitrary projected dynamics, derive all diffusion coefficients from the physical carrier, select one outcome history, or emit the complete Bell state-and-instrument packet.

# Four questions that must not be merged

The word “deterministic” can refer to different mathematical levels. Let a complete state $`u\in\mathcal U`$ evolve by a map
``` math
u_{n+1}=\Phi(u_n).
```
Suppose only
``` math
x_n=P(u_n)
```
is retained. Four separate questions follow:

1.  Does one current reduced state determine the next reduced state?

2.  If not, which probability measure describes unresolved complete states?

3.  Does the resulting reduced process have the Markov property?

4.  In a Bell experiment, are source variables statistically independent of later settings?

A many-to-one $`P`$ answers none of the last three questions by itself. Noninjectivity permits hidden distinctions; it does not supply a probability law, erase temporal memory, or correlate a source with future settings.

The corrected chain is
``` math
\boxed{
\begin{gathered}
\text{deterministic complete dynamics}
\ +\ \text{projection}
\ +\ \text{preparation measure}\\
\longrightarrow
\text{conditional reduced laws}
\ +\ \text{a separate closure or limit theorem}.
\end{gathered}
}
```

# Exact deterministic descent

Let $`\mathcal U`$ and $`\mathcal X`$ be sets, let
``` math
\Phi:\mathcal U\to\mathcal U,
\qquad
P:\mathcal U\to\mathcal X,
```
and write $`\mathcal X_0=P(\mathcal U)`$.

<div id="thm:fiber" class="theorem">

**Theorem 1** (Fiber-factorization criterion). *There exists a map $`F:\mathcal X_0\to\mathcal X`$ satisfying
``` math
P\circ\Phi=F\circ P
```
if and only if
``` math
\begin{equation}
P(u)=P(v)
\quad\Longrightarrow\quad
P(\Phi u)=P(\Phi v)
\label{eq:fiber}
\end{equation}
```
for every $`u,v\in\mathcal U`$.*

</div>

<div class="proof">

*Proof.* If the factorization exists and $`P(u)=P(v)=x`$, then
``` math
P(\Phi u)=F(x)=P(\Phi v).
```
Conversely, assume equation <a href="#eq:fiber" data-reference-type="eqref" data-reference="eq:fiber">[eq:fiber]</a>. For $`x\in\mathcal X_0`$, choose any $`u`$ with $`P(u)=x`$ and define
``` math
F(x)=P(\Phi u).
```
The fiber condition makes this definition independent of the representative. ◻

</div>

The theorem is algebraic. If $`P`$ and $`\Phi`$ are measurable, measurability of the quotient map $`F`$ requires the corresponding measurable-space hypotheses. The probabilistic version is naturally almost sure.

<div id="thm:as-descent" class="theorem">

**Theorem 2** (Almost-sure deterministic descent). *Let $`\mathcal U`$ and $`\mathcal X`$ be standard Borel spaces, let $`U`$ have probability law $`\mu`$, and define
``` math
X=P(U),
\qquad
Y=P(\Phi U).
```
The following are equivalent:*

1.  *there is a measurable $`F:\mathcal X\to\mathcal X`$ such that $`Y=F(X)`$ almost surely;*

2.  *$`Y`$ is measurable with respect to $`\sigma(X)`$;*

3.  *the regular conditional law $`\operatorname{Law}(Y\mid X=x)`$ is a Dirac measure for $`P_\#\mu`$-almost every $`x`$.*

</div>

<div class="proof">

*Proof.* The equivalence of the first two statements is the Doob–Dynkin lemma for standard Borel targets. If $`Y=F(X)`$, its conditional law given $`X=x`$ is $`\delta_{F(x)}`$ almost everywhere. Conversely, if the conditional law is Dirac almost everywhere, a measurable choice of its atom gives $`Y=F(X)`$ almost surely. ◻

</div>

This corrects a central overstatement in Version 2. A Dirac conditional law proves constancy only on the part of each fiber seen by the chosen preparation, up to conditional null sets. It does not prove equation <a href="#eq:fiber" data-reference-type="eqref" data-reference="eq:fiber">[eq:fiber]</a> at every point of every fiber.

# Where the reduced probability law comes from

Let $`\mu_x`$ be a regular conditional distribution of $`U`$ given $`P(U)=x`$. Define
``` math
\begin{equation}
K_\mu(x,A)
=
\mu_x\!\left(
\left\{u:P(\Phi u)\in A\right\}
\right),
\qquad A\in\mathcal B(\mathcal X).
\label{eq:kernel}
\end{equation}
```
For $`P_\#\mu`$-almost every $`x`$, this is the conditional law of the next reduced state.

<div id="prop:preparation" class="proposition">

**Proposition 3** (Preparation dependence). *The maps $`P`$ and $`\Phi`$ do not determine $`K_\mu`$. Two preparation measures can have the same reduced marginal $`P_\#\mu`$ and induce different next-step kernels.*

</div>

<div class="proof">

*Proof.* Take
``` math
\mathcal U=\{0,1\}\times\{0,1\},
\qquad
P(x,h)=x,
\qquad
\Phi(x,h)=(h,h).
```
Let $`\mu`$ give equal weight to $`(0,0)`$ and $`(1,0)`$, and let $`\nu`$ give equal weight to $`(0,1)`$ and $`(1,1)`$. Both projected marginals are uniform on $`\{0,1\}`$. Under $`\mu`$, the next projected state is always zero, so
``` math
K_\mu(x,\cdot)=\delta_0.
```
Under $`\nu`$, it is always one, so
``` math
K_\nu(x,\cdot)=\delta_1.
```
 ◻

</div>

The example is small because the point is structural. Projection identifies $`(x,0)`$ and $`(x,1)`$, but only a preparation says how the unresolved coordinate is distributed. In MTT language, a selected upper state, preparation protocol, invariant measure, or normal state is part of every probability theorem.

# A one-step kernel is not automatically Markov

Starting from $`U_0\sim\mu`$, define
``` math
U_n=\Phi^n(U_0),
\qquad
X_n=P(U_n).
```
Equation <a href="#eq:kernel" data-reference-type="eqref" data-reference="eq:kernel">[eq:kernel]</a> describes a conditional one-step law for one declared preparation. The process $`(X_n)`$ is Markov only if
``` math
\mathbb P(X_{n+1}\in A\mid X_0,\ldots,X_n)
=
\mathbb P(X_{n+1}\in A\mid X_n)
```
almost surely for every $`n`$ and measurable $`A`$. Time homogeneity requires the right side to be the same kernel at every $`n`$.

<div id="prop:not-markov" class="proposition">

**Proposition 4** (Projected deterministic dynamics need not be Markov). *A deterministic invertible microscopic map with an invariant preparation can have a non-Markov projected process.*

</div>

<div class="proof">

*Proof.* Let
``` math
\mathcal U=\{0,1,2,3\},
\qquad
\Phi(i)=i+1\pmod 4,
```
let $`\mu`$ be uniform, and set
``` math
P(0)=P(1)=0,
\qquad
P(2)=P(3)=1.
```
The stationary observed sequence is a uniformly phased version of
``` math
0,0,1,1,0,0,1,1,\ldots.
```
Conditioning only on $`X_n=0`$ gives
``` math
\mathbb P(X_{n+1}=1\mid X_n=0)=\frac12.
```
But if $`X_{n-1}=0`$ as well, the current phase is the second zero and
``` math
\mathbb P(X_{n+1}=1\mid X_n=0,X_{n-1}=0)=1.
```
The Markov identity fails. ◻

</div>

The hidden complete state retains phase information. Conditioning on the current reduced value does not reconstruct the posterior distribution of that phase. A valid Markov reduction therefore needs a sufficient-state or lumpability theorem, a memory augmentation, or a scaling limit that removes the memory.

# How deterministic dynamics can have a diffusion limit

There is no contradiction between deterministic trajectories and a stochastic effective limit. One begins with an ensemble of initial conditions, a fast–slow scaling, and a functional limit theorem. Standard deterministic homogenization makes this precise for broad classes of chaotic systems .

The companion MTT paper *Deterministic Projection, Diffusive Limits, and Knee-Like Threshold Transitions* gives a concrete finite source:
``` math
F_{\epsilon,s}(x,y)
=
\left(
(1-\epsilon\gamma)x
+\epsilon\alpha(s-s_0)
+\sqrt{\epsilon}\sin(2\pi y_1),
\ Ay\!\!\pmod{\mathbb Z^2}
\right),
```
where
``` math
A=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}.
```
For every fixed initial condition the dynamics is deterministic. With the hidden torus coordinate sampled from its invariant measure, the projected slow coordinate has a rigorously controlled diffusion limit, and the Green–Kubo variance for the displayed forcing is exactly $`1/2`$.

That result establishes possibility, not automatic MTT source selection. A physical promotion still needs an intertwiner from the selected carrier, selection of the invariant preparation, and derivation of the scale parameters.

## Random does not mean arbitrary

Once a probability measure is introduced, the reduced process is random in the mathematical sense. Its distribution may be sharply concentrated, biased, bounded, correlated, or generated as a deterministic scaling limit. Those properties make it structured, not “non-random.” Lawful stochastic models are standard probability theory; they do not form a third logical category between deterministic and random.

The OU and selection-potential argument from Version 2 is therefore retained only as a conditional modeling direction. To obtain a slab-exit bound, one must specify a valid Gaussian process, its path metric and continuity, Lipschitz dependence of the observable on the Gaussian state, the expected supremum or entropy bound, and the relation between threshold crossing and physical inadmissibility. A pointwise covariance estimate does not supply all of that.

# What cascading stabilization can rigorously mean

Outcome selection and later stability are different. Suppose one outcome-completion rule has already placed a coupled apparatus and environment inside a declared record basin
``` math
\mathcal D=D_1\times\cdots\times D_m.
```
Let $`T=(T_1,\ldots,T_m):\mathcal D\to\mathcal D`$.

<div id="thm:coupled" class="theorem">

**Theorem 5** (Coupled-basin contraction). *Assume each $`(D_i,d_i)`$ is complete and there is a nonnegative matrix $`L=(L_{ij})`$ such that
``` math
d_i(T_i x,T_i y)
\leq
\sum_{j=1}^m L_{ij}d_j(x_j,y_j)
```
for all $`x,y\in\mathcal D`$. If the spectral radius satisfies
``` math
\rho(L)<1,
```
then there are positive weights $`w_i`$ and $`q<1`$ for which $`T`$ is a contraction in
``` math
d_w(x,y)
=\max_i\frac{d_i(x_i,y_i)}{w_i}.
```
Consequently $`T`$ has one fixed record in $`\mathcal D`$, and every orbit in that basin converges to it geometrically.*

</div>

<div class="proof">

*Proof.* Choose $`q`$ with $`\rho(L)<q<1`$. The Neumann series
``` math
w=
\sum_{k=0}^{\infty}(L/q)^k\mathbf 1
```
converges and has strictly positive components. It obeys
``` math
Lw=q(w-\mathbf 1)\leq qw.
```
If $`d_w(x,y)=r`$, then
``` math
d_j(x_j,y_j)\leq r w_j,
```
so
``` math
d_i(T_i x,T_i y)
\leq r(Lw)_i
\leq qrw_i.
```
Hence $`d_w(Tx,Ty)\leq qd_w(x,y)`$. The weighted product of finitely many complete spaces is complete, so the Banach fixed-point theorem gives the unique fixed point and geometric convergence. ◻

</div>

This theorem supplies the missing quantitative meaning of downstream “cascading stabilization.” It does not say which basin is entered. Multiple records require multiple basins, a noncontractive transition region, or an outcome-resolved instrument. The influence matrix $`L`$ and its physical spectral-radius bound must also be derived for the apparatus under study.

# Determinism and superdeterminism

Consider a Bell experiment with source variable $`\Lambda`$, settings $`A,B`$, and outcomes $`R,S`$.

Measurement independence
The source distribution is independent of the later settings:
``` math
\mathbb P(d\lambda\mid A=a,B=b)=\mathbb P(d\lambda).
```

Bell factorization
Conditional on a complete hidden variable,
``` math
\mathbb P(r,s\mid a,b,\lambda)
=
\mathbb P(r\mid a,\lambda)\,
\mathbb P(s\mid b,\lambda).
```

Operational no-signaling
The marginal outcome law on either side does not depend on the remote setting.

These conditions are not equivalent. Superdeterministic Bell models are normally characterized by relaxing measurement independence in a deterministic common-cause description; explicit measurement-dependent local models exist . Determinism by itself neither proves nor disproves such dependence. A joint preparation-and-setting measure must be specified.

Bell’s theorem says that measurement independence and Bell factorization imply the Bell inequalities . Therefore a model reproducing CHSH violation while retaining measurement independence must abandon Bell factorization, even if its fundamental dynamics is deterministic. It can still preserve algebraic microcausality and operational no-signaling.

## The corrected MTT Bell route

The current spatial Bell paper uses the following conditional package:
``` math
\boxed{
\begin{gathered}
\text{preparation-selected nonseparable state independent of later settings}\\
+\ \text{base-local descent}
+\ \text{local completely positive instruments}.
\end{gathered}
}
```
This package can violate Bell factorization without a controllable superluminal signal. It is not a Bell-local hidden-variable completion. Calling it “without superdeterminism” is justified only when the selected joint measure really preserves measurement independence.

The logical compatibility is established. The strict MTT source theorem is not: selected geometry must still emit the nonseparable state, probability functional, and detector instruments from one branch.

# Status ledger

<div class="center">

| Status | Result |
|:---|:---|
| Exact | Global fiber criterion for deterministic descent |
| Exact | Almost-sure/Dirac conditional-law criterion |
| Exact | Same reduced marginal can yield different kernels |
| Exact | Deterministic stationary projection can be non-Markov |
| Exact | Coupled-basin stabilization when $`\rho(L)<1`$ |
| Imported | Deterministic homogenization under declared fast–slow hypotheses |
| Conditional | Native MTT preparation, mixing, and diffusion coefficients |
| Conditional | Measurement-independent MTT Bell completion packet |
| Open | General Markov closure and objective one-history completion |

</div>

# Completion program

To promote the structural framework to a physical MTT theorem:

1.  select the complete state space and evolution on the physical branch;

2.  select the retained algebra or projection;

3.  derive the preparation or invariant state rather than adding it after projection;

4.  test global, almost-sure, and approximate fiber factorization;

5.  prove a sufficient-state, memory-kernel, or homogenization theorem;

6.  derive its error bound and coefficients from the same source;

7.  derive the outcome-resolved apparatus instrument;

8.  prove basin-local coupled stabilization after completion; and

9.  for Bell protocols, verify measurement independence, base locality, local instruments, and no-signaling separately.

Each failure is informative. Exact fiber factorization gives deterministic closure. Persistent memory demands an augmented or non-Markov theory. Failure of a functional limit rules out the proposed diffusion. Failure of measurement independence changes the Bell interpretation and must be reported rather than renamed.

# Conclusion

The useful insight behind “determinism without superdeterminism” is not that projection magically creates randomness. It is that a deterministic complete law need not factor through a reduced state. Once a preparation is supplied, the unresolved fibers define conditional laws; once a closure or scaling theorem is proved, those laws may become an effective stochastic process.

This paper now proves the exact descent and conditional-law criteria, shows by example why preparation and memory matter, and gives a quantitative theorem for joint record stabilization after a basin has been selected. It also fixes the Bell language: determinism, measurement independence, Bell factorization, and no-signaling are separate properties.

MTT has compatible exact pieces at each interface, including a deterministic homogenization example, a restricted q79 output law, base-local Bell descent, and basin-local contraction. What remains is their selected same-source composition. That is the honest frontier.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The factorization and conditional-kernel results are measure-theoretic and do not depend on a Standard Model numerical fit. The open strict-upgrade ledger is a corpus boundary, not evidence for determinism, Markov closure, or freedom-of-settings assumptions.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

J. S. Bell, *On the Einstein Podolsky Rosen Paradox*, Physics Physique Fizika **1** (1964) 195–200, doi:10.1103/PhysicsPhysiqueFizika.1.195.

M. J. W. Hall, *Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence*, Physical Review Letters **105** (2010) 250404, doi:10.1103/PhysRevLett.105.250404.

I. Chevyrev, P. K. Friz, A. Korepanov, I. Melbourne, and H. Zhang, *Deterministic Homogenization under Optimal Moment Assumptions for Fast–Slow Systems. Part 2*, Annales de l’Institut Henri Poincare, Probabilites et Statistiques **58** (2022) 1328–1350, doi:10.1214/21-AIHP1203.

</div>
