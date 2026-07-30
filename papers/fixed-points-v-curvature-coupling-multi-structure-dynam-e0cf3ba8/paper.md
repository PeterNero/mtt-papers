---
abstract: |
  We formulate multi-structure covariance and admissibility diagnostics on the canonical FP–I–IV spine. Curvature enters through the full Laplace-type operator and its curved spectral projector, not through an unproved affine eigenvalue rule. Exact Gaussian claims are restricted to frozen linear Ornstein–Uhlenbeck systems. The scalar OU baseline is imported from Fixed Points III, its canonical owner, and the genuinely multi-structure stationary covariance derived here satisfies a Lyapunov equation, and block-diagonal damping gives a correct cross-covariance and canonical-correlation estimate. Admissibility is encoded by a finite or trace-controlled family of declared spectral, damping, and performance margins. The resulting deficit score detects exit but is neither a force nor an energy unless a separate variational source theorem is supplied. For affine Gaussian margin observables we prove finite-grid and continuous-time exit bounds. Cross-correlation controls simultaneous exits on a declared observation grid; it does not by itself prove localization, non-propagation, or selection of a post-exit state.
author:
- Peter Nero
current_version: v7
date: July 2026 Version 7
generated_from_main_tex_sha256: 4e014f3af6686d3e4af042e3ae923fd3021bb09ad74d323207db0d676b0499ed
paper_id: fixed-points-v-curvature-coupling-multi-structure-dynam-e0cf3ba8
release_state: zenodo_released
released_version: v7
title: |
  Fixed Points V: Curvature Coupling, Multi-Structure Dynamics,
  and Admissibility Barriers
zenodo_doi: 10.5281/zenodo.21655379
zenodo_record_id: 21655379
zenodo_url: "https://zenodo.org/records/21655379"
---

# Revision note for version 7

Supersedes.
*Fixed Points V: Curvature Coupling, Multi-Structure Dynamics, and Admissibility Barriers*, version 6.

Reason.
Version 6 corrected the covariance and exit mathematics, but a reader could still mistake the deficit diagnostic or cross-correlation for a force, propagation law, or post-exit selector.

Resolution.
Version 7 adds a concrete covariance-cloud interpretation, an explicit explanation of why the deficit is diagnostic only, and a paper-specific route through the hypotheses. It preserves the scalar OU ownership of Fixed Points III and makes no new physical promotion.

Retained result.
The stationary covariance, canonical-correlation, and declared-margin exit bounds are retained unchanged on their frozen-linear and Gaussian domains.

Remaining boundary.
Nonlinear dynamics, causal propagation, localization, an exit-generating action, and selection of the next basin remain independent source problems.

# Revision note for version 6

Supersedes.
*Fixed Points V: Curvature Coupling, Multi-Structure Dynamics, and Drivers*, version 5.

Reason.
Affine curvature shifts, nonlinear Gaussian claims, an incorrectly normalized covariance bound, and a deficit score interpreted as force, energy, censorship, and post-exit selection exceeded the proved model.

Resolution.
Version 6 derives covariance from the frozen linear OU system, corrects canonical-correlation bounds, declares all admissibility margins, and proves only finite-grid or continuous Gaussian exit estimates. The scalar OU lemma is assigned to Fixed Points III and retained here only as a self-contained imported baseline.

Retained result.
Multi-structure covariance and admissibility-exit diagnostics remain rigorous on their stated domains.

Remaining boundary.
Correlation does not establish propagation, localization, an exit-causing force, or selection of the next basin.

# How to read this paper

FP–III controls disturbances mode by mode, while FP–IV explains how curvature changes the operator and coherent projector. FP–V combines those inputs at a frozen configuration and asks two narrower questions: how are different modal structures statistically correlated, and how likely is a declared admissibility margin to be crossed?

#### The central picture in plain language.

A stable linear stochastic system settles into a Gaussian cloud whose shape is the covariance matrix $`\Sigma`$. Its diagonal blocks describe uncertainty within individual structures; its off-diagonal blocks describe their shared fluctuation. Declared margins cut out an admissible region around the reference configuration. Exit estimates ask how much of the Gaussian cloud, or of a continuous Gaussian path, reaches the wrong side of those boundaries.

#### Why the deficit score is only diagnostic.

The scalar $`\mathfrak B`$ records the worst violated margin, much as a single warning display can summarize many monitored constraints. It tells us whether the declared description has failed. It does not push the system toward or away from the boundary, assign an energetic cost, determine causal propagation, or choose the next basin. Any such role requires an additional source theorem connecting the score to an action or transition law.

#### Argument map.

Sections 1–2 state the inherited curved linearization and import the scalar OU baseline from FP–III. Section 3 derives stationary covariance from the stable semigroup, then bounds cross-covariance and canonical correlation. Section 4 defines the admissibility margins and exact deficit diagnostic. Section 5 adds the affine Gaussian structure required for finite-grid and continuous-time exit bounds. Section 6 uses correlation to bound simultaneous observed exits and then states precisely what covariance cannot establish.

#### Scope boundary.

The covariance theorems are frozen-linear results. The Gaussian exit theorems require affine margin observables. Nonlinear time-dependent operators, physical propagation, localization, and post-exit selection are not consequences of this layer.

# Inherited setting and scope

Let $`I=[t_0,t_1]`$ be a finite parameter interval and let $`(B,g_t)`$ be a Riemannian base with uniformly bounded geometry on $`I`$. This formulation does not identify the FP stabilization parameter with physical Lorentzian time. Existence of a projected fixed point and promotion to a full equilibrium are inherited only when the hypotheses of FP I and FP II hold. Disturbance floors are interpreted according to FP III, and curvature uses the full operator and projector construction of FP IV.

At a frozen configuration $`x`$, write
``` math
L_x=\nabla_x^\ast\nabla_x+\mathcal R_x,
 \qquad P_x=P_{\mathcal R}(x),\qquad Q_x=I-P_x .
```
The contour defining $`P_x`$ is assumed to remain in the resolvent set. If the old uncurved projector is used instead, the leakage term $`Q\mathcal RP`$ from FP IV must be retained.

All matrix theorems below are finite dimensional. They also extend to a separable Hilbert space when the noise covariance is trace class, the semigroup is exponentially stable, and every displayed covariance product is well defined. Modal sums are never used without a finite truncation or an explicit summability hypothesis.

# Curved modal damping and exact OU modes

Let $`\alpha`$ denote a joint spectral label, including multiplicity. In a frozen $`Q_x`$-sector linearization, suppose the scalar mode satisfies the Itô equation
``` math
\begin{equation}
 da_\alpha=-\gamma_\alpha(x)a_\alpha\,dt
              +\sqrt{q_\alpha(x)}\,dW_\alpha(t),
 \qquad \gamma_\alpha(x)>0 .
 \label{eq:scalar-ou}
\end{equation}
```
Here $`\gamma_\alpha`$ is the damping margin obtained after the one-sided nonlinear estimate; it is not a shared deterministic/stochastic disturbance parameter. Curvature dependence is inherited from $`L_x`$. An affine response formula for an eigenvalue is an additional approximation, not a consequence of the Weitzenbock identity.

#### Imported scalar OU baseline.

Fixed Points III is the canonical source for the exact scalar result . Equation <a href="#eq:scalar-ou" data-reference-type="eqref" data-reference="eq:scalar-ou">[eq:scalar-ou]</a> has the unique invariant law
``` math
\mathcal N\!\left(0,\frac{q_\alpha}{2\gamma_\alpha}\right).
```
Deterministic forcing $`f_\alpha`$ instead gives the input-to-state scale $`|f_\alpha|/\gamma_\alpha`$; these two quantities are not interchangeable. For completeness, the variation-of-constants representation is
``` math
a_\alpha(t)=e^{-\gamma_\alpha t}a_\alpha(0)
 +\sqrt{q_\alpha}\int_0^t e^{-\gamma_\alpha(t-s)}\,dW_\alpha(s).
```
Itô isometry yields variance $`q_\alpha(1-e^{-2\gamma_\alpha t})/(2\gamma_\alpha)`$, which converges to the displayed value. The deterministic scale follows by integrating the stable kernel against a bounded input.

# Multi-structure covariance

<div id="thm:semigroup-covariance" class="theorem">

**Theorem 1** (Stable-semigroup covariance and resolvent bounds). *Consider
``` math
d\zeta=A\zeta\,dt+B\,dW_t,\qquad Q:=BB^\top,
```
and assume
``` math
\|e^{tA}\|\le M e^{-\omega t},
 \qquad t\ge0,\quad M\ge1,\quad\omega>0.
```
Then the stationary covariance is
``` math
\Sigma=\int_0^\infty e^{tA}Qe^{tA^\top}\,dt,
```
it solves
``` math
A\Sigma+\Sigma A^\top+Q=0,
```
and
``` math
\|\Sigma\|\le\frac{M^2\|Q\|}{2\omega},
 \qquad
 \|A^{-1}\|\le\frac{M}{\omega}.
```*

</div>

<div class="proof">

*Proof.* The semigroup estimate makes the covariance integral converge. Differentiating its integrand gives the Lyapunov equation. Exponential stability also gives $`A^{-1}=-\int_0^\infty e^{tA}\,dt`$. Taking norms proves both bounds. ◻

</div>

This form is required for nonnormal generators: the spectral abscissa alone does not control transient amplification or justify setting $`M=1`$.

#### What the Lyapunov equation means.

The covariance is accumulated noise transported by the decaying semigroup. The algebraic Lyapunov equation is the balance statement obtained after this accumulation has reached stationarity. The constant $`M`$ remembers transient amplification of nonnormal dynamics; two generators with the same asymptotic decay rate can therefore support different covariance bounds.

For the block estimates and exit bounds below, specialize to the symmetric damping model and collect a finite set of frozen linearized amplitudes in $`a(t)\in\mathbb R^d`$:
``` math
\begin{equation}
 da=-\Gamma a\,dt+B\,dW_t,
 \qquad Q:=BB^\top,
 \label{eq:vector-ou}
\end{equation}
```
where $`\Gamma=\Gamma^\top\succeq\gamma_0 I`$ with $`\gamma_0>0`$.

<div id="thm:covariance" class="corollary">

**Corollary 2** (Symmetric-damping covariance). *Equation <a href="#eq:vector-ou" data-reference-type="eqref" data-reference="eq:vector-ou">[eq:vector-ou]</a> has a unique centered Gaussian invariant law with covariance
``` math
\Sigma=\int_0^\infty e^{-t\Gamma}Qe^{-t\Gamma}\,dt .
```
It is the unique solution of
``` math
\Gamma\Sigma+\Sigma\Gamma=Q,
 \qquad \|\Sigma\|_{\rm op}\le\frac{\|Q\|_{\rm op}}{2\gamma_0}.
```*

</div>

<div class="proof">

*Proof.* Apply Theorem <a href="#thm:semigroup-covariance" data-reference-type="ref" data-reference="thm:semigroup-covariance">1</a> with $`A=-\Gamma`$, $`M=1`$, and $`\omega=\gamma_0`$. Uniqueness follows by applying the stable semigroup to the homogeneous Lyapunov equation. ◻

</div>

Partition the structures into $`A`$ and $`B`$ and assume for this section that
``` math
\Gamma=\operatorname{diag}(\Gamma_A,\Gamma_B),\qquad
 \Gamma_A\succeq\gamma_A I,\quad
 \Gamma_B\succeq\gamma_B I.
```
Then the cross block obeys the Sylvester equation
``` math
\Gamma_A\Sigma_{AB}+\Sigma_{AB}\Gamma_B=Q_{AB}.
```

<div id="lem:cross-covariance" class="lemma">

**Lemma 3** (Cross-covariance bound). *Under the block-damping hypothesis,
``` math
\|\Sigma_{AB}\|_{\rm op}
 \le \frac{\|Q_{AB}\|_{\rm op}}{\gamma_A+\gamma_B}.
```
In particular, $`Q_{AB}=0`$ implies $`\Sigma_{AB}=0`$ in this frozen linear model.*

</div>

<div class="proof">

*Proof.* The Sylvester solution is $`\Sigma_{AB}=\int_0^\infty e^{-t\Gamma_A}Q_{AB}e^{-t\Gamma_B}\,dt`$. Taking norms proves the claim. ◻

</div>

<div id="def:canonical" class="definition">

**Definition 4** (Canonical cross-correlation). For a positive semidefinite covariance block matrix, define
``` math
\rho_{AB}:=
 \|\Sigma_A^{\dagger/2}\Sigma_{AB}\Sigma_B^{\dagger/2}\|_{\rm op}.
```
The covariance support inclusions imply $`0\le\rho_{AB}\le1`$. Let $`m_A,m_B>0`$ denote the smallest positive eigenvalues of $`\Sigma_A,\Sigma_B`$ on their supports.

</div>

<div id="thm:canonical" class="theorem">

**Theorem 5** (Damping bound for canonical correlation). *Under the preceding hypotheses,
``` math
\rho_{AB}
 \le
 \frac{\|Q_{AB}\|_{\rm op}}
 { (\gamma_A+\gamma_B)\sqrt{m_A m_B}}.
```
Consequently the right-hand side being smaller than $`\rho_0\in(0,1)`$ is a sufficient condition for $`\rho_{AB}<\rho_0`$.*

</div>

<div class="proof">

*Proof.* Use submultiplicativity, the identities $`\|\Sigma_A^{\dagger/2}\|=m_A^{-1/2}`$ and $`\|\Sigma_B^{\dagger/2}\|=m_B^{-1/2}`$, and Lemma <a href="#lem:cross-covariance" data-reference-type="ref" data-reference="lem:cross-covariance">3</a>. ◻

</div>

The smallest positive covariance eigenvalues are essential. Replacing them by $`\|\Sigma_A\|`$ and $`\|\Sigma_B\|`$ reverses the relevant normalization and does not bound canonical correlation.

#### Interpretation of cross-correlation.

$`Q_{AB}`$ is the shared noise input in the block model, while $`\gamma_A+\gamma_B`$ is the rate at which the two blocks jointly erase that shared fluctuation. Canonical correlation then normalizes the surviving cross-covariance by the variances actually present on each support. It is a dimensionless dependence measure, not a signal speed or causal kernel.

# Admissibility margins and deficit score

Fix a finite family of continuous margins $`m_j(x)`$, $`j\in\mathcal J`$. They may include:

- separation of the curved low spectral cluster from the rest of the spectrum;

- positive one-sided damping margins $`\gamma_\alpha(x)`$;

- declared deterministic performance bounds $`r^{\rm det}_\alpha-|f_\alpha|/\gamma_\alpha`$;

- declared stochastic variance bounds $`r^{\rm stoch}_\alpha-q_\alpha/(2\gamma_\alpha)`$.

For an infinite family, replace finiteness by uniform convergence and compact control sufficient to make the infimum below continuous.

<div id="def:deficit" class="definition">

**Definition 6** (Admissible domains and deficit score). Set
``` math
\mathcal D_\varepsilon
 :=\{x:m_j(x)\ge\varepsilon\text{ for every }j\in\mathcal J\},
 \qquad
 \mathfrak B(x):=\max_{j\in\mathcal J}[-m_j(x)].
```
Then $`x\in\mathcal D_0`$ exactly when $`\mathfrak B(x)\le0`$, and $`x\in\mathcal D_\varepsilon`$ exactly when $`\mathfrak B(x)\le-\varepsilon`$.

</div>

<div id="prop:diagnostic" class="proposition">

**Proposition 7** (Diagnostic status). *The score $`\mathfrak B`$ is an exact scalar encoding of the declared margin constraints. It is not inserted into the evolution equation. It is not a physical energy, selection potential, or infinite enforcement cost unless an independent variational source theorem identifies it with such an object.*

</div>

<div id="thm:exit" class="theorem">

**Theorem 8** (Deterministic exit detection). *Let $`X:I\to B`$ be continuous and suppose the margins are continuous. If $`X(t_0)\in\mathcal D_0`$ and $`\mathfrak B(X(t_1))>0`$, there is a first exit time
``` math
\tau:=\inf\{t\in[t_0,t_1]:\mathfrak B(X(t))>0\},
```
with $`\mathfrak B(X(\tau))=0`$. At times with $`\mathfrak B(X(t))>0`$, at least one declared constraint fails.*

</div>

<div class="proof">

*Proof.* The maximum of finitely many continuous functions is continuous. The result follows from the intermediate value theorem and the definition of first exit. ◻

</div>

This theorem detects loss of the declared description. It neither supplies a force causing the exit nor selects the state or basin after exit.

#### What is exact here.

For the chosen list of margins, $`\mathfrak B\le0`$ is exactly equivalent to admissibility. The theorem therefore provides an exact logical detector. The physical content still depends on whether the selected margins faithfully encode the intended geometry, damping, and performance requirements.

# Gaussian exit estimates

We now impose the stronger structure actually needed for Gaussian claims. Assume the stationary solution of <a href="#eq:vector-ou" data-reference-type="eqref" data-reference="eq:vector-ou">[eq:vector-ou]</a> and an exact affine linearized margin model
``` math
\begin{equation}
 m_j(t)=\bar m_j+\ell_j^\top a(t),
 \qquad \bar m_j>0 .
 \label{eq:affine-margin}
\end{equation}
```
Thus $`Z_j(t):=\ell_j^\top a(t)`$ is a centered stationary Gaussian process with
``` math
v_j:=\operatorname{Var}Z_j(t)
 =\ell_j^\top\Sigma\ell_j
 \le\|\ell_j\|^2\frac{\|Q\|}{2\gamma_0}.
```
A merely Lipschitz nonlinear function of a Gaussian process is not generally Gaussian, so <a href="#eq:affine-margin" data-reference-type="eqref" data-reference="eq:affine-margin">[eq:affine-margin]</a> cannot be replaced by Lipschitz regularity alone.

<div id="thm:grid" class="theorem">

**Theorem 9** (Finite-grid exit bound). *For observation times $`t_1,\ldots,t_N`$,
``` math
\mathbb P\!\left(\min_{j\in\mathcal J,\,1\le k\le N}m_j(t_k)<0\right)
 \le
 \sum_{j\in\mathcal J}N
 \exp\!\left(-\frac{\bar m_j^2}{2v_j}\right),
```
with a zero-variance term interpreted as zero when $`\bar m_j>0`$.*

</div>

<div class="proof">

*Proof.* For each pair $`(j,k)`$, the Gaussian tail bound gives $`\mathbb P(Z_j(t_k)<-\bar m_j)\le
\exp[-\bar m_j^2/(2v_j)]`$. Apply the union bound. No temporal independence is required. ◻

</div>

<div id="thm:continuous" class="theorem">

**Theorem 10** (Continuous-time Gaussian exit bound). *Assume each $`Z_j`$ is separable with almost surely continuous paths and
``` math
e_j:=\mathbb E\sup_{t\in I}[-Z_j(t)]<\infty,
 \qquad \sigma_j^2:=\sup_{t\in I}\operatorname{Var}Z_j(t).
```
If $`\bar m_j>e_j`$ for every $`j`$, then
``` math
\mathbb P\!\left(\inf_{t\in I}\min_{j\in\mathcal J}m_j(t)<0\right)
 \le
 \sum_{j\in\mathcal J}
 \exp\!\left[-\frac{(\bar m_j-e_j)^2}{2\sigma_j^2}\right].
```*

</div>

<div class="proof">

*Proof.* Apply the Borell–TIS inequality to the separable Gaussian process $`-Z_j`$ and then take a union bound over the finite constraint family. ◻

</div>

Finiteness of $`e_j`$ can be verified from the canonical increment metric by a metric-entropy bound. Exponential covariance decay alone suggests the usual $`\sqrt{\log(1+\gamma_0|I|)}`$ scale, but that scale is not asserted without the required entropy estimate.

#### Finite grid versus continuous path.

The grid theorem controls only the declared observation times and needs no temporal independence. The continuous theorem controls every time in the interval, but pays for that stronger statement through path continuity, separability, and a bound on the expected supremum. Sampling more densely does not by itself turn the first theorem into the second.

# Simultaneous exits and the limit of correlation data

For two scalar affine margin observables at a fixed time, standardize the exit variables as $`U=-Z_A/\sigma_A`$ and $`V=-Z_B/\sigma_B`$. Suppose $`-1<\rho_0<1`$, $`\operatorname{Corr}(U,V)\le\rho_0`$, and the standardized positive margins obey $`u_A=\bar m_A/\sigma_A`$, $`u_B=\bar m_B/\sigma_B`$.

<div id="lem:simultaneous" class="lemma">

**Lemma 11** (Fixed-time simultaneous-exit bound).
*``` math
\mathbb P(U\ge u_A,\,V\ge u_B)
 \le
 \exp\!\left[-\frac{(u_A+u_B)^2}{4(1+\rho_0)}\right].
```
For $`N`$ declared observation times at which the same bounds hold, the probability of a simultaneous observed exit is at most $`N`$ times the right-hand side.*

</div>

<div class="proof">

*Proof.* The joint event implies $`U+V\ge u_A+u_B`$, while $`\operatorname{Var}(U+V)\le2(1+\rho_0)`$. Apply the one-dimensional Gaussian tail bound and then the union bound over observation times. ◻

</div>

<div class="proposition">

**Proposition 12** (No propagation theorem from covariance alone). *Equal-time covariance or canonical correlation does not determine causal propagation, temporal clustering, or a post-exit transition. Such conclusions require a specified coupled evolution or transition kernel and control of cross-time covariance. Therefore FP V makes no probabilistic censorship or non-propagation claim from $`\rho_{AB}`$ alone.*

</div>

# Conclusion

FP V now supplies a rigorous frozen-linear covariance layer and a correctly scoped admissibility layer. Curvature is handled through the FP IV full operator and projector. Joint modes use the FP II/III indexing and disturbance conventions. Canonical correlation is normalized by the smallest positive covariance eigenvalues, and Gaussian persistence is proved only for affine Gaussian margin observables under the assumptions required by the relevant concentration theorem. The deficit score detects a declared loss of admissibility but is not promoted to dynamics, energy, propagation, or post-exit selection.

The practical chain is now explicit: a stable curved linearization determines a covariance; a declared affine margin turns that covariance into an exit observable; Gaussian concentration bounds its crossing probability; and cross-covariance can bound simultaneous observed crossings. The chain ends there. Moving from correlated exits to causal transport, localization, or a selected successor state requires a time-dependent coupled dynamics or transition kernel that is not encoded in equal-time covariance. That missing law is the next model-specific frontier, not another reinterpretation of the deficit score.

<div class="thebibliography">

99

P. Nero, *Fixed Points III: Disturbance–Damping Balance and Stability*, revised edition, 2026.

G. Da Prato and J. Zabczyk, *Stochastic Equations in Infinite Dimensions*, Encyclopedia of Mathematics and Its Applications, Vol. 44, Cambridge University Press, Cambridge, 1992.

R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, Applied Mathematical Sciences, Vol. 68, Springer-Verlag, New York, 1997.

</div>

# Computational Evidence and Reproducibility

The numerical and machine-verifiable claims used by this paper are archived in the curated repository, `https://github.com/PeterNero/mtt-results-repro`. The mapped authority/result identifiers are `no result rows mapped`. Claim tiers in that capsule distinguish exact derivation, certified numerics, profile replay, conditional results, and open obligations.
