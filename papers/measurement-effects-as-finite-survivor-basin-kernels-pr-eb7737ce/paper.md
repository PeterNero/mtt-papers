---
abstract: |
  Measurement is an ordinary physical interaction. Its mathematical description nevertheless has several layers: an effect-valued measure gives outcome probabilities, an instrument also gives conditional post-interaction states, a realized record requires an outcome-completion rule, and later dynamics may stabilize that record. This paper constructs the first two layers exactly for finite-resolution position detection and keeps the latter two distinct. On $`L^2(\mathbb R^d)`$, a normalized detector response $`g_\epsilon(x-y)`$ defines a commutative positive operator-valued measure that is precisely a classical smearing of the sharp position projection-valued measure. Its outcome density is the convolution $`g_\epsilon*|\psi|^2`$, which converges in $`L^1`$, hence in total variation, to the sharp Born density. If the density is in $`W^{1,1}`$, the error is at most
  ``` math
  \epsilon
  \left(\int_{\mathbb R^d}|u|g(u)\,du\right)
  \|\nabla|\psi|^2\|_1.
  ```
  An explicit square-root instrument realizes the same effects and produces a finite post-measurement filter. For a Gaussian response, detector blur adds exactly $`\epsilon^2 I_d`$ to the outcome covariance. A two-outcome qubit example shows that finite unsharp effects converge in operator norm to a discrete projective measurement, so not every projective measurement is a distributional singularity. In Modal Triplet Theory (MTT), these results supply a rigorous downstream detector interface. They do not derive the instrument from selected geometry, select one realized outcome, or identify detector width with a coherence or Ornstein–Uhlenbeck floor.
author:
- Peter Nero
current_version: v1
date: July 2026, Version 1
generated_from_main_tex_sha256: 934812854297ed27f26dd704216837a01e7ff20b7265a495fbecd0fdbb2fa43b
paper_id: measurement-effects-as-finite-survivor-basin-kernels-pr-eb7737ce
release_state: zenodo_released
released_version: v1
title: |
  Finite-Resolution Position Measurements and Their Sharp Limit
  Detector POVMs, Instruments, and the MTT Completion Boundary
zenodo_doi: 10.5281/zenodo.21665984
zenodo_record_id: 21665984
zenodo_url: "https://zenodo.org/records/21665984"
---

# Version 1 Revision Note

Supersedes
The unversioned April 2026 manuscript *Measurement Effects as Finite Survivor–Basin Kernels: Projective Collapse as the Singular Limit of Admissible Selection in Modal Triplet Theory*.

Reason
The earlier manuscript conflated a position-PVM density with a bounded point projector, treated every projective measurement as a singular limit, let effects determine state updates, and identified basin stabilization with outcome completion. It also presented a conditional Ornstein–Uhlenbeck variance as a detector-width lower bound without a source or calibration theorem.

Resolution
This version formulates the sharp position PVM correctly, constructs its finite detector smearing as a POVM, proves total-variation convergence and a quantitative $`W^{1,1}`$ error bound, supplies one explicit instrument while emphasizing instrument nonuniqueness, and separates physical interaction, outcome completion, and record stabilization.

Retained result
Normalized finite detector kernels give honest finite-resolution effects and recover the sharp position statistics in a controlled limit. The Gaussian and two-outcome models remain concrete examples.

Remaining boundary
No theorem here derives the detector response or instrument from the selected MTT carrier, supplies a general Born source for arbitrary apparatus contexts, selects one realized history, or equates detector width with a geometric coherence floor.

# What a measurement model must contain

A laboratory measurement is not metaphysically exceptional. It is a physical coupling that leaves an outcome-bearing record. The formal description still has to distinguish what different mathematical objects do:

1.  the system–apparatus interaction produces an outcome-sensitive transition;

2.  a POVM gives the probability law of the outcome label;

3.  an instrument gives both that law and the conditional post-interaction state;

4.  an outcome-completion rule says how one realized record is represented; and

5.  subsequent dynamics may stabilize or amplify that record.

Neither a POVM nor a contraction theorem silently performs every step. A finite detector kernel can rigorously supply the second step and, after a Kraus choice, the third. It does not by itself select one history or prove that a record basin is dynamically stable.

The aim of this paper is therefore precise:
``` math
\boxed{
\begin{gathered}
\text{finite detector response}
\longrightarrow
\text{POVM and one compatible instrument}\\
\longrightarrow
\text{controlled sharp-statistics limit}
\end{gathered}
}
```

# The sharp position observable

Let
``` math
\mathcal H=L^2(\mathbb R^d).
```
The sharp position observable is the projection-valued measure $`Q`$ defined for Borel sets $`B\subseteq\mathbb R^d`$ by
``` math
(Q(B)\psi)(y)=\mathbf 1_B(y)\psi(y).
```
Every $`Q(B)`$ is a bounded orthogonal projection, $`Q(\mathbb R^d)=I`$, and $`Q`$ is countably additive in the strong operator topology.

The notation
``` math
Q(dx)=|x\rangle\langle x|\,dx
```
is a useful formal density. The generalized vector $`|x\rangle`$ is not in $`L^2(\mathbb R^d)`$, and $`|x\rangle\langle x|`$ is not a bounded rank-one operator. This does not make the PVM $`Q`$ ill-defined. It means only that its pointwise Dirac density belongs to a rigged-Hilbert-space or distributional description.

This distinction matters. Continuous position has a distributional density, whereas a discrete spectral projection is an ordinary bounded operator. The claim that every PVM is a singular fiction is therefore false. What can be proved is that a declared family of finite-response measurements converges to a declared sharp observable.

# Finite detector response as a smeared PVM

Choose a detector profile
``` math
g\in L^1(\mathbb R^d),\qquad
g\geq0,\qquad
\int_{\mathbb R^d}g(u)\,du=1,
```
and set
``` math
g_\epsilon(u)=\epsilon^{-d}g(u/\epsilon),
\qquad \epsilon>0.
```
For a true position $`y`$, define the classical detector channel
``` math
\kappa_\epsilon(B\mid y)
=\int_B g_\epsilon(x-y)\,dx.
```
It is the probability that the reported position lies in $`B`$.

Define an operator-valued set function
``` math
\begin{equation}
E_\epsilon(B)
=\int_{\mathbb R^d}
\kappa_\epsilon(B\mid y)\,Q(dy).
\label{eq:smeared-povm}
\end{equation}
```
Equivalently,
``` math
(E_\epsilon(B)\psi)(y)
=\kappa_\epsilon(B\mid y)\psi(y).
```

<div id="thm:smearing" class="theorem">

**Theorem 1** (Detector smearing theorem). *For every $`\epsilon>0`$, equation <a href="#eq:smeared-povm" data-reference-type="eqref" data-reference="eq:smeared-povm">[eq:smeared-povm]</a> defines a normalized commutative POVM on $`\mathbb R^d`$. It is a classical post-processing of the sharp position PVM $`Q`$.*

</div>

<div class="proof">

*Proof.* For every Borel $`B`$,
``` math
0\leq\kappa_\epsilon(B\mid y)\leq1
```
almost everywhere, so $`0\leq E_\epsilon(B)\leq I`$. Normalization follows from
``` math
\kappa_\epsilon(\mathbb R^d\mid y)=1.
```
If $`B_1,B_2,\ldots`$ are disjoint, countable additivity of the scalar probability kernel gives
``` math
\kappa_\epsilon\!\left(\bigcup_nB_n\mid y\right)
=\sum_n\kappa_\epsilon(B_n\mid y).
```
Dominated convergence then gives weak, and in this multiplication representation strong, countable additivity of $`E_\epsilon`$. All effects are multiplication operators and therefore commute. The defining formula is exactly the composition of $`Q`$ with the classical Markov kernel $`\kappa_\epsilon`$. ◻

</div>

For a normalized pure state $`\psi`$, the outcome law has density
``` math
\begin{equation}
p_\epsilon(x\mid\psi)
=\langle\psi,E_\epsilon(dx)\psi\rangle/dx
=\int_{\mathbb R^d}
g_\epsilon(x-y)|\psi(y)|^2\,dy.
\label{eq:blurred-density}
\end{equation}
```
Thus
``` math
p_\epsilon=g_\epsilon*|\psi|^2.
```
This uses the usual quantum trace rule. It is a detector-smearing theorem, not a derivation of the Born rule.

# Sharp-limit convergence and an error certificate

The outcome law admits a stronger statement than pointwise convergence under continuity assumptions.

<div id="thm:tv-limit" class="theorem">

**Theorem 2** (Total-variation sharp limit). *Let $`g_\epsilon`$ be the approximate identity above. For every normalized $`\psi\in L^2(\mathbb R^d)`$,
``` math
\|p_\epsilon-|\psi|^2\|_{L^1}\longrightarrow0
\quad\text{as }\epsilon\downarrow0.
```
Equivalently, the finite and sharp outcome probability measures converge in total variation:
``` math
\operatorname{TV}(\mu_\epsilon^\psi,\mu_0^\psi)
=\frac12\|p_\epsilon-|\psi|^2\|_1
\longrightarrow0.
```*

</div>

<div class="proof">

*Proof.* Because $`\psi\in L^2`$, the density
``` math
f=|\psi|^2
```
belongs to $`L^1`$. The standard $`L^1`$ approximate-identity theorem gives
``` math
\|g_\epsilon*f-f\|_1\longrightarrow0.
```
Equation <a href="#eq:blurred-density" data-reference-type="eqref" data-reference="eq:blurred-density">[eq:blurred-density]</a> identifies $`g_\epsilon*f=p_\epsilon`$. The total-variation identity holds for absolutely continuous probability measures. ◻

</div>

When the input density has one integrable weak derivative, the approach to the sharp limit has an explicit bound.

<div id="thm:error-bound" class="theorem">

**Theorem 3** (Finite-resolution error bound). *Suppose
``` math
f=|\psi|^2\in W^{1,1}(\mathbb R^d)
```
and
``` math
m_1(g):=\int_{\mathbb R^d}|u|g(u)\,du<\infty.
```
Then
``` math
\begin{equation}
\|p_\epsilon-f\|_1
\leq
\epsilon\,m_1(g)\,\|\nabla f\|_1.
\label{eq:error-bound}
\end{equation}
```
Consequently,
``` math
\operatorname{TV}(\mu_\epsilon^\psi,\mu_0^\psi)
\leq
\frac{\epsilon}{2}m_1(g)\|\nabla|\psi|^2\|_1.
```*

</div>

<div class="proof">

*Proof.* After the change of variables $`u=(x-y)/\epsilon`$,
``` math
(g_\epsilon*f)(x)-f(x)
=\int_{\mathbb R^d}
g(u)\bigl(f(x-\epsilon u)-f(x)\bigr)\,du.
```
Minkowski’s inequality and the translation estimate for $`W^{1,1}`$ give
``` math
\|g_\epsilon*f-f\|_1
\leq
\int g(u)
\|f(\,\cdot-\epsilon u)-f\|_1\,du
\leq
\epsilon\|\nabla f\|_1
\int |u|g(u)\,du.
```
This is equation <a href="#eq:error-bound" data-reference-type="eqref" data-reference="eq:error-bound">[eq:error-bound]</a>. ◻

</div>

The bound is operational: it separates detector resolution $`\epsilon`$, detector shape $`m_1(g)`$, and spatial variation of the input density. None of those factors is selected by the abstract POVM theorem.

# A compatible instrument

A POVM fixes probabilities but not post-measurement states. To construct one instrument, assume additionally that $`g\in L^\infty`$, and define the bounded multiplication operator
``` math
(M_{x,\epsilon}\psi)(y)
=g_\epsilon(x-y)^{1/2}\psi(y).
```
For a Borel set $`B`$, set
``` math
\begin{equation}
\mathcal I_\epsilon(B)(\rho)
=\int_B
M_{x,\epsilon}\rho M_{x,\epsilon}^{*}\,dx,
\label{eq:instrument}
\end{equation}
```
where the integral is understood weakly on trace-class states.

<div id="thm:instrument" class="theorem">

**Theorem 4** (Square-root detector instrument). *Equation <a href="#eq:instrument" data-reference-type="eqref" data-reference="eq:instrument">[eq:instrument]</a> defines a normalized completely positive instrument. Its associated POVM is $`E_\epsilon`$:
``` math
\operatorname{Tr}\!\left[\mathcal I_\epsilon(B)(\rho)\right]
=\operatorname{Tr}\!\left[\rho E_\epsilon(B)\right],
\qquad
\operatorname{Tr}\!\left[\mathcal I_\epsilon(\mathbb R^d)(\rho)\right]
=\operatorname{Tr}\rho.
```*

</div>

<div class="proof">

*Proof.* Each map
``` math
\rho\longmapsto
M_{x,\epsilon}\rho M_{x,\epsilon}^{*}
```
is completely positive, and positive weak integrals preserve complete positivity. Cyclicity of the trace gives
``` math
\operatorname{Tr}\!\left[\mathcal I_\epsilon(B)(\rho)\right]
=\int_B
\operatorname{Tr}\!\left[\rho M_{x,\epsilon}^{*}M_{x,\epsilon}\right]dx.
```
Since $`M_{x,\epsilon}^{*}M_{x,\epsilon}`$ is multiplication by $`g_\epsilon(x-y)`$, the integral over $`B`$ is multiplication by $`\kappa_\epsilon(B\mid y)`$, namely $`E_\epsilon(B)`$. Taking $`B=\mathbb R^d`$ and using Theorem <a href="#thm:smearing" data-reference-type="ref" data-reference="thm:smearing">1</a> proves trace normalization. ◻

</div>

For an outcome density at $`x`$ with $`p_\epsilon(x\mid\psi)>0`$, the conditional pure state for this particular instrument is
``` math
\psi_{x,\epsilon}(y)
=
\frac{
g_\epsilon(x-y)^{1/2}\psi(y)
}{
p_\epsilon(x\mid\psi)^{1/2}
}.
```
This is a finite filter. It is not an exact point eigenstate.

## Why the instrument must be stated

The square-root instrument is not forced by the POVM. For example, a projective effect $`P_i`$ is compatible both with the Lüders operation
``` math
\rho\longmapsto P_i\rho P_i
```
and with a measure-and-prepare operation
``` math
\rho\longmapsto
\operatorname{Tr}(\rho P_i)\,|\phi_i\rangle\langle\phi_i|.
```
Both have outcome effect $`P_i`$, but their output states and later measurement statistics can differ. The finite effects therefore cannot by themselves encode measurement order, repeatability, or record dynamics. This is the reason quantum instruments, rather than effects alone, are the correct interface for sequential experiments .

# Gaussian detector model

For the centered Gaussian profile
``` math
g(u)=(2\pi)^{-d/2}e^{-|u|^2/2},
```
equation <a href="#eq:blurred-density" data-reference-type="eqref" data-reference="eq:blurred-density">[eq:blurred-density]</a> becomes
``` math
p_\epsilon(x\mid\psi)
=(2\pi\epsilon^2)^{-d/2}
\int_{\mathbb R^d}
e^{-|x-y|^2/(2\epsilon^2)}
|\psi(y)|^2\,dy.
```
The first absolute moment is
``` math
m_1(g)
=
\sqrt{2}\,
\frac{\Gamma((d+1)/2)}{\Gamma(d/2)}.
```
Theorem <a href="#thm:error-bound" data-reference-type="ref" data-reference="thm:error-bound">3</a> therefore gives a fully explicit finite-resolution certificate.

There is also a simple probabilistic interpretation. Let $`Y`$ have density $`|\psi|^2`$, let $`Z\sim N(0,I_d)`$ be independent, and set
``` math
X_\epsilon=Y+\epsilon Z.
```
Then $`X_\epsilon`$ has density $`p_\epsilon`$.

<div id="prop:gaussian-covariance" class="proposition">

**Proposition 5** (Exact Gaussian covariance broadening). *If $`Y`$ has finite second moments, then
``` math
\mathbb E X_\epsilon=\mathbb E Y,
\qquad
\operatorname{Cov}(X_\epsilon)
=\operatorname{Cov}(Y)+\epsilon^2I_d.
```*

</div>

<div class="proof">

*Proof.* Independence and $`\mathbb EZ=0`$ give the mean identity. The cross covariances vanish, and
``` math
\operatorname{Cov}(\epsilon Z)=\epsilon^2I_d.
```
 ◻

</div>

This added variance is a property of the declared response channel. It is not yet a geometric prediction for $`\epsilon`$.

# Discrete effects are not distributional singularities

Let
``` math
P_\pm=\frac12(I\pm\sigma_z)
```
be the sharp two-outcome qubit PVM. A symmetric unsharp family is
``` math
E_\pm(\eta)
=\frac12(I\pm\eta\sigma_z),
\qquad 0\leq\eta\leq1.
```
For
``` math
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),
```
the probabilities are
``` math
p_\pm(\eta)
=\operatorname{Tr}[\rho E_\pm(\eta)]
=\frac12(1\pm\eta r_z).
```
Moreover,
``` math
\|E_\pm(\eta)-P_\pm\|
=\frac{1-\eta}{2}
\longrightarrow0
\quad\text{as }\eta\uparrow1.
```

This is an ordinary operator-norm limit. There is no Dirac distribution and no vanishing spatial width. The example corrects the overly broad slogan that projective measurement is always a singular limit. Continuous position has a distributional density; a finite-dimensional spectral projection does not.

A Lüders-type choice
``` math
\rho\longmapsto
E_\pm(\eta)^{1/2}\rho E_\pm(\eta)^{1/2}
```
defines one compatible instrument, not the unique one.

# Where outcome completion and stabilization enter

The finite detector construction gives an operational probability law and a conditional state map. It does not make measurement a special nonphysical act. It also does not, by itself, say which outcome is realized in one run.

The correct division of labor is
``` math
\boxed{
\begin{array}{c}
\text{physical coupling and response}\\
\downarrow\\
\text{outcome-resolved instrument}\\
\downarrow\\
\text{completion into one record}\\
\downarrow\\
\text{amplification or basin-local stabilization}.
\end{array}
}
```

A contraction inside a record basin can prove that an already completed record persists. One global strict contraction cannot supply multiple stable records. Likewise, decoherence can suppress selected off-diagonal terms but does not choose one instrument outcome. Those roles must not be assigned to the detector POVM.

# MTT interpretation and current status

MTT can use the detector kernel as a downstream target. A selected system–apparatus carrier would have to emit:

1.  the detector response $`g_\epsilon`$ or a more general quantum effect kernel;

2.  the compatible instrument, not merely its effects;

3.  the preparation state or state family on which the law is evaluated;

4.  any record-completion rule required by the intended ontology; and

5.  the dynamics that makes the record repeatable.

The current canonical q79 binary one-anchor recorder is stronger than a bare analogy on its declared domain: it supplies selected finite state, observable, output-algebra, and stopped-record data, with an exact output law and second-moment capture. It does not yet provide arbitrary continuous detector responses or every apparatus context. The present Gaussian model is therefore a rigorous interface example, not a promoted q79 source theorem.

## The width is not yet selected

If a pointer coordinate is separately assumed to obey an additive Ornstein–Uhlenbeck equation, its stationary variance is fixed by that equation’s damping and noise coefficients. A finite-memory colored source has a corresponding corrected response variance. Neither fact identifies the detector parameter $`\epsilon`$ with that variance.

Such an identification would require a calibration theorem connecting:
``` math
\text{selected apparatus dynamics}
\longrightarrow
\text{pointer response distribution}
\longrightarrow
g_\epsilon.
```
Without this map, an OU width is a conditional model and $`\epsilon`$ is a detector parameter.

# Status ledger

<div class="center">

| Status | Result |
|:---|:---|
| Exact | The sharp position observable is a PVM $`Q`$ on Borel sets |
| Exact | A normalized detector channel smears $`Q`$ into a commutative POVM |
| Exact | Outcome densities converge in $`L^1`$ and total variation |
| Exact | $`W^{1,1}`$ inputs obey the error bound $`\epsilon m_1(g)\|\nabla|\psi|^2\|_1`$ |
| Exact | The square-root Kraus family defines one compatible instrument |
| Exact | Gaussian blur adds $`\epsilon^2I_d`$ to outcome covariance |
| Exact | The qubit unsharp family converges in norm to its PVM |
| Input | The quantum trace rule used to evaluate the POVM |
| Conditional | Identification with a selected MTT detector or pointer model |
| Open | General instrument source, arbitrary contexts, and one-history completion |

</div>

# What has and has not been achieved

The exact achievement is a clean mathematical bridge between ideal and finite-resolution position statistics. It answers four questions:

1.  what the sharp position observable actually is;

2.  how a normalized detector response produces a POVM;

3.  how close its probabilities are to the sharp probabilities; and

4.  how one explicit instrument realizes the same effects.

The bridge does not explain why nature chooses a particular detector response, why the trace rule holds in every intended context, or why one outcome rather than another becomes the experienced record. It also does not make detector finite width uniquely MTT-specific: the POVM and instrument mathematics is standard quantum measurement theory . The MTT research content lies in the proposed upstream source and completion program, which remains testable and incomplete.

# Conclusion

Finite-resolution measurement should be described without turning an ordinary physical interaction into a mystical operation. A detector response kernel defines a normalized POVM; after a Kraus choice it defines an instrument; and its outcome law can approach a sharp observable with a quantified error.

For continuous position, Gaussian or other approximate-identity responses converge in total variation to the sharp Born density. For discrete qubit measurements, the corresponding unsharp effects converge directly in operator norm. The two cases show why “projective measurement is a singular limit” is useful only with a declared topology and observable.

The MTT boundary is now explicit. A physical carrier must emit the response and instrument, while outcome completion and later stabilization remain separate tasks. The finite detector mathematics is complete; its universal geometric source is not.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The detector POVM, instrument, and sharp-limit results are finite-resolution measurement statements. The mapped open ledger is not a probability source or detector model; it records a separate corpus-level no-knob obligation.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

E. B. Davies and J. T. Lewis, *An Operational Approach to Quantum Probability*, Communications in Mathematical Physics **17** (1970) 239–260, doi:10.1007/BF01647093.

A. S. Holevo, *Statistical Structure of Quantum Theory*, Lecture Notes in Physics Monographs, vol. 67, Springer, Berlin, 2001, doi:10.1007/3-540-44998-1.

</div>
