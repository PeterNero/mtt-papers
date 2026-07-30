---
abstract: |
  The formal microcanonical density $`\delta(H-E)`$ is a surface distribution, not an ordinary phase-space probability density. This paper gives a finite-shell formulation and states precisely when its normalized measures approach the sharp microcanonical ensemble. For a regular energy $`E`$, the coarea formula reduces phase-space integration to the density-of-states functions
  ``` math
  A_f(e)=\int_{H^{-1}(e)}
  \frac{f}{|\nabla H|}\,\mathrm{d}\Sigma_e.
  ```
  If $`\eta_\epsilon`$ is a normalized approximate identity in energy, then the finite-shell expectation is the ratio of two ordinary convolutions,
  ``` math
  \frac{(\eta_\epsilon*A_f)(E)}
  {(\eta_\epsilon*A_1)(E)},
  ```
  and converges to $`A_f(E)/A_1(E)`$. When the two density-of-states functions are locally Lipschitz, an explicit first-order error bound separates shell width, kernel shape, observable variation, and normalization bias. On a symplectic phase space, every shell whose density depends only on $`H`$ is exactly invariant under the Hamiltonian flow; ergodicity is not needed for invariance and is not proved here. Critical energies, noncompact shells, ensemble equivalence, and a physical choice of shell profile require separate hypotheses. In Modal Triplet Theory (MTT), the result supplies a rigorous downstream target: selected geometry may emit a finite energy-tolerance profile, but neither the coarea theorem nor the sharp limit selects that profile or its width.
author:
- Peter Nero
current_version: v1
date: July 2026, Version 1
generated_from_main_tex_sha256: c660d446d9990dfe60a154c43d593b0cabb8c8a69b68557d696623cc88127b81
paper_id: classical-constraint-deltas-and-microcanonical-shells-a-9f4bdcc1
release_state: zenodo_released
released_version: v1
title: |
  Finite Microcanonical Shells and Their Sharp Constraint Limit
  Coarea Geometry, Quantitative Bias, and the MTT Source Boundary
zenodo_doi: 10.5281/zenodo.21703909
zenodo_record_id: 21703909
zenodo_url: "https://zenodo.org/records/21703909"
---

# Version 1 Revision Note

Supersedes
The unversioned April 2026 manuscript *Classical Constraint Deltas and Microcanonical Shells: Admissibility-Shell Limits in Modal Triplet Theory*.

Reason
The earlier manuscript duplicated the general coarea theorem owned by the delta-kernel paper, described every delta as a finite admissible process idealized to zero width, and assigned microcanonical closure to the MTT circle without a source theorem. It did not quantify finite-shell bias, separate invariance from ergodicity, or explain the failures at critical energies and on noncompact shells.

Resolution
This version imports the standard coarea reduction and concentrates on normalized microcanonical measures. It proves convergence, adds an explicit Lipschitz error certificate, proves exact Hamiltonian-flow invariance for energy-dependent shell densities, and records the critical, normalization, ensemble, and MTT-source boundaries.

Retained result
A normalized finite energy shell converges to the sharp microcanonical surface measure at regular energies under finite density-of-states hypotheses.

Remaining boundary
No theorem here selects the shell profile or width from MTT geometry, establishes ergodicity, handles singular critical levels in general, or proves equivalence with a canonical ensemble.

# What the microcanonical delta means

Let $`(M,\omega)`$ be a $`2d`$-dimensional symplectic phase space with Liouville measure
``` math
\mathrm{d}\mu=\frac{\omega^d}{d!},
```
and let $`H:M\to\mathbb R`$ be a smooth Hamiltonian. The familiar expression
``` math
\rho_E(z)
=
\frac{\delta(H(z)-E)}{\Omega(E)}
```
is shorthand for a probability measure on the level set $`H^{-1}(E)`$, when that surface measure is finite and nonzero.

If $`E`$ is a regular value, then $`\nabla H\neq0`$ on $`H^{-1}(E)`$, and the coarea formula gives
``` math
\Omega(E)
=
\int_{H^{-1}(E)}
\frac{1}{|\nabla H(z)|}\,\mathrm{d}\Sigma_E(z).
```
For an observable $`f`$, the sharp microcanonical expectation is
``` math
\langle f\rangle_E
=
\frac{1}{\Omega(E)}
\int_{H^{-1}(E)}
\frac{f(z)}{|\nabla H(z)|}\,\mathrm{d}\Sigma_E(z).
```
The factor $`1/|\nabla H|`$ is not optional. It is the normal Jacobian that converts ambient phase volume into level-set measure.

The delta notation is exact distribution theory. A finite shell is a different probability model that can approach it. Such a shell can represent finite energy preparation, detector resolution, thermodynamic coarse graining, or a mathematical regularization. Those interpretations are not interchangeable until a physical preparation protocol is specified.

# Finite energy-shell measures

Let $`\eta:\mathbb R\to[0,\infty)`$ satisfy
``` math
\int_{\mathbb R}\eta(u)\,\mathrm{d}u=1,
```
and define
``` math
\eta_\epsilon(u)
=
\frac{1}{\epsilon}\eta\!\left(\frac{u}{\epsilon}\right),
\qquad \epsilon>0.
```
Compactly supported profiles describe a hard finite band with shaped edges. The normalized Gaussian
``` math
\eta_\epsilon(u)
=
\frac{1}{\sqrt{2\pi}\epsilon}
\exp\!\left(-\frac{u^2}{2\epsilon^2}\right)
```
describes soft energy mismatch. Both are ordinary nonnegative densities in the energy variable.

Define the unnormalized shell functional
``` math
N_\epsilon(f;E)
=
\int_M f(z)\eta_\epsilon(H(z)-E)\,\mathrm{d}\mu(z)
```
and its normalizing factor
``` math
\Omega_\epsilon(E)
=
N_\epsilon(1;E).
```
Whenever $`0<\Omega_\epsilon(E)<\infty`$, the finite-shell probability measure is
``` math
\mathrm{d}\nu_{E,\epsilon}(z)
=
\frac{\eta_\epsilon(H(z)-E)}
{\Omega_\epsilon(E)}\,\mathrm{d}\mu(z).
```

The normalization must be checked. On a noncompact phase space, even a narrow energy profile can have infinite phase volume. Confinement, compact energy bands, or a declared observable support is therefore part of the theorem, not a cosmetic assumption.

# Coarea reduction to one energy variable

For energies $`e`$ in a regular interval around $`E`$, define
``` math
A_f(e)
=
\int_{H^{-1}(e)}
\frac{f(z)}{|\nabla H(z)|}\,\mathrm{d}\Sigma_e(z).
```
The coarea formula gives
``` math
N_\epsilon(f;E)
=
\int_{\mathbb R}
\eta_\epsilon(e-E)A_f(e)\,\mathrm{d}e.
```
If $`\widetilde\eta(u)=\eta(-u)`$, this can be written
``` math
N_\epsilon(f;E)
=
(\widetilde\eta_\epsilon*A_f)(E).
```
For symmetric shell profiles, $`\widetilde\eta=\eta`$.

This reduction is the key simplification. Finite-shell convergence is an ordinary problem for an approximate identity acting on the density-of-states function $`A_f`$. The geometric work is contained in the coarea factor.

# Normalized microcanonical convergence

<div id="thm:microcanonical-limit" class="theorem">

**Theorem 1** (Finite-shell microcanonical limit). *Let $`E`$ lie in an open interval $`I`$ of regular values of $`H`$. Let $`\eta\geq0`$ be integrable with unit integral, and assume its rescaled mass outside every fixed neighborhood of zero tends to zero. Suppose $`A_1(e)`$ and $`A_f(e)`$ are finite and continuous at $`E`$, with
``` math
\Omega(E)=A_1(E)>0.
```
Assume also that the shell integrals are finite and that contributions from outside a compact subinterval of $`I`$ vanish as $`\epsilon\downarrow0`$. Then
``` math
\int_M f\,\mathrm{d}\nu_{E,\epsilon}
\longrightarrow
\frac{A_f(E)}{A_1(E)}
=
\langle f\rangle_E.
```*

</div>

<div class="proof">

*Proof.* The coarea reduction gives
``` math
N_\epsilon(f;E)\longrightarrow A_f(E),
\qquad
\Omega_\epsilon(E)\longrightarrow A_1(E)
```
by the approximate-identity property. Since $`A_1(E)>0`$, the denominator is positive and bounded away from zero for sufficiently small $`\epsilon`$. Taking the quotient proves the claim. ◻

</div>

The theorem does not say that the finite shell is physically more fundamental than the sharp surface. It says that if a physical or mathematical model uses such finite profiles, their normalized expectations have a controlled sharp limit.

# A quantitative finite-width certificate

Convergence alone does not tell us whether a chosen finite shell is already a good approximation. Let
``` math
m_1(\eta)
=
\int_{\mathbb R}|u|\eta(u)\,\mathrm{d}u
```
be the first absolute moment of the profile.

<div id="thm:bias" class="theorem">

**Theorem 2** (Lipschitz shell-bias bound). *Under the hypotheses of Theorem <a href="#thm:microcanonical-limit" data-reference-type="ref" data-reference="thm:microcanonical-limit">1</a>, suppose $`A_f`$ and $`A_1`$ are Lipschitz on an interval containing all sufficiently small shells, with constants $`L_f`$ and $`L_1`$, and suppose $`m_1(\eta)<\infty`$. Write
``` math
a=A_f(E),
\qquad
\Omega=A_1(E)>0.
```
If
``` math
\epsilon m_1(\eta)L_1\leq\frac{\Omega}{2},
```
then
``` math
\left|
\int_M f\,\mathrm{d}\nu_{E,\epsilon}
-\frac{a}{\Omega}
\right|
\leq
\frac{2\epsilon m_1(\eta)L_f}{\Omega}
+
\frac{2|a|\epsilon m_1(\eta)L_1}{\Omega^2}.
```*

</div>

<div class="proof">

*Proof.* Changing variables $`e=E+\epsilon u`$ gives
``` math
|N_\epsilon(f;E)-a|
\leq
\epsilon m_1(\eta)L_f
```
and
``` math
|\Omega_\epsilon(E)-\Omega|
\leq
\epsilon m_1(\eta)L_1.
```
The assumed inequality implies $`\Omega_\epsilon(E)\geq\Omega/2`$. Therefore
``` math
\begin{align*}
\left|
\frac{N_\epsilon(f;E)}{\Omega_\epsilon(E)}
-\frac{a}{\Omega}
\right|
&\leq
\frac{|N_\epsilon(f;E)-a|}{\Omega_\epsilon(E)}
+
\frac{|a|\,|\Omega_\epsilon(E)-\Omega|}
{\Omega_\epsilon(E)\Omega}\\
&\leq
\frac{2\epsilon m_1(\eta)L_f}{\Omega}
+
\frac{2|a|\epsilon m_1(\eta)L_1}{\Omega^2}.
\end{align*}
```
 ◻

</div>

The two terms have different meanings. The first measures variation of the observable-weighted density of states across the shell. The second measures normalization drift. A small width alone is not enough if the density of states changes rapidly near $`E`$.

For an even profile with a finite second moment and twice differentiable density-of-states functions, the first signed moment vanishes and a second-order bound can be obtained. That improvement depends on stronger regularity and is not used here.

# Exact invariance under Hamiltonian flow

Let $`\Phi_t`$ be the Hamiltonian flow of $`H`$. Liouville’s theorem gives
``` math
(\Phi_t)_\#\mu=\mu,
```
and conservation of energy gives
``` math
H\circ\Phi_t=H.
```

<div id="thm:invariance" class="theorem">

**Theorem 3** (Hamiltonian invariance of every energy-profile shell). *Let $`w:\mathbb R\to[0,\infty)`$ be measurable and assume
``` math
0<\int_M w(H(z))\,\mathrm{d}\mu(z)<\infty.
```
Then the probability measure
``` math
\mathrm{d}\nu_w(z)
=
\frac{w(H(z))}
{\int_Mw(H)\,\mathrm{d}\mu}\,\mathrm{d}\mu(z)
```
is invariant under $`\Phi_t`$. In particular, every finite shell $`\nu_{E,\epsilon}`$ is invariant whenever it is normalizable.*

</div>

<div class="proof">

*Proof.* For every bounded measurable $`f`$,
``` math
\begin{align*}
\int_M f\circ\Phi_t\,w(H)\,\mathrm{d}\mu
&=
\int_M f\circ\Phi_t\,w(H\circ\Phi_t)\,\mathrm{d}\mu\\
&=
\int_M (fw(H))\circ\Phi_t\,\mathrm{d}\mu\\
&=
\int_M fw(H)\,\mathrm{d}\mu.
\end{align*}
```
Normalization gives invariance of $`\nu_w`$. ◻

</div>

Invariance is not ergodicity. A flow can preserve a microcanonical measure while decomposing its energy surface into many invariant components. Equilibrium interpretations based on time averages require ergodicity, mixing, typicality, or another statistical argument not supplied by the delta or shell construction.

# Worked kinetic-energy example

For one momentum coordinate $`p\in\mathbb R`$,
``` math
H(p)=\frac{p^2}{2m}.
```
At $`E>0`$, the energy level consists of
``` math
p_\pm=\pm\sqrt{2mE}.
```
Since $`H'(p)=p/m`$, the sharp constraint acts on a test function as
``` math
\int_{\mathbb R}
f(p)\delta\!\left(\frac{p^2}{2m}-E\right)\,\mathrm{d}p
=
\frac{m}{\sqrt{2mE}}
\left[
f(\sqrt{2mE})+f(-\sqrt{2mE})
\right].
```
The density of states is
``` math
\Omega(E)
=
\sqrt{\frac{2m}{E}},
\qquad E>0.
```
The normalized sharp expectation is therefore
``` math
\langle f\rangle_E
=
\frac12
\left[
f(\sqrt{2mE})+f(-\sqrt{2mE})
\right].
```

A finite profile $`\eta_\epsilon(H-E)`$ samples neighborhoods of both roots. Its normalized expectation converges to their equal average. The equality of the two sharp weights follows from the equal Jacobian magnitudes, not from an extra probability postulate.

At $`E=0`$, the two roots merge and $`H'(0)=0`$. The regular-value theorem no longer applies, and $`\Omega(E)`$ diverges as $`E^{-1/2}`$. This elementary example shows why critical energies cannot be dismissed as a technical footnote.

# Several simultaneous constraints

For a smooth map
``` math
C:M\to\mathbb R^r
```
with full rank near $`C^{-1}(0)`$, the normal Jacobian is
``` math
\mathcal J_C(z)
=
\sqrt{\det\!\bigl(DC(z)DC(z)^\ast\bigr)}.
```
A normalized approximate identity $`\eta_\epsilon^{(r)}`$ in $`\mathbb R^r`$ gives
``` math
\int_M f(z)\eta_\epsilon^{(r)}(C(z))\,\mathrm{d}\mu(z)
\longrightarrow
\int_{C^{-1}(0)}
\frac{f(z)}{\mathcal J_C(z)}\,\mathrm{d}\Sigma(z).
```
This is the general coarea-tube result proved in the companion delta-kernel paper. After dividing by the same expression with $`f=1`$, one obtains a normalized constraint-surface measure whenever its total mass is finite and nonzero.

The full-rank hypothesis matters. First-class Hamiltonian constraints can carry gauge redundancy, and singular constraint sets may require reduction before a finite probability measure is meaningful. The finite-dimensional coarea formula does not by itself construct an infinite-dimensional path integral or a global gauge quotient.

# Canonical weighting is a different ensemble

The canonical density
``` math
\mathrm{d}\nu_\beta
=
\frac{e^{-\beta H}}{Z(\beta)}\,\mathrm{d}\mu
```
weights many energies. It is not a finite-width approximation to one microcanonical surface unless an additional concentration or thermodynamic limit is proved.

Microcanonical and canonical ensembles can agree for suitable observables in suitable large-system limits. They need not agree for finite systems, at phase-transition points, or for systems with long-range interactions. The shell theorem proves neither ensemble equivalence nor thermalization. It only controls one regularized representation of a declared energy constraint.

# MTT interpretation and source obligation

The mathematically complete downstream chain is
``` math
\boxed{
\begin{gathered}
\text{regular Hamiltonian level geometry}\\
\downarrow\\
\text{normalized finite energy profile}\\
\downarrow\\
\text{coarea convolution and error bound}\\
\downarrow\\
\text{sharp microcanonical surface measure}.
\end{gathered}
}
```

MTT can use this chain as an interface. An upstream construction would have to emit:

1.  the Hamiltonian or effective conserved quantity;

2.  the prepared target energy $`E`$;

3.  the shell profile $`\eta`$;

4.  the physical width $`\epsilon`$;

5.  the phase-space measure and any reduction by constraints; and

6.  the regime in which regularity and normalization hold.

The common circle or fixed-point geometry may eventually help source a conservation or return condition, but equality of interpretation is not a derivation. No present theorem identifies $`\epsilon`$ with a circle scale, coherence length, spectral gap, or universal noise floor.

Different normalized profiles have the same sharp limit but different finite-width predictions. That universality makes the limiting theorem robust, while also showing why the limit cannot select the finite profile. Empirical comparison at nonzero width would test the source model, not the coarea formula.

# Status ledger

<div class="center">

| Status | Result |
|:---|:---|
| Standard input | Coarea representation of a regular energy-level distribution |
| Exact | Normalized finite-shell measures converge to the sharp microcanonical measure |
| Exact | The Lipschitz shell-bias bound separates numerator and normalization errors |
| Exact | Every normalizable density depending only on $`H`$ is Hamiltonian-flow invariant |
| Exact example | The one-dimensional kinetic shell gives equal weights at its two regular roots |
| Conditional | Finite shell as detector resolution, preparation tolerance, or coarse graining |
| Open | Critical-level theory, ergodicity, thermalization, and ensemble equivalence |
| Open in MTT | Selected $`H`$, $`E`$, profile, width, and reduced phase-space measure |

</div>

# Conclusion

The microcanonical delta is a precisely defined surface distribution. A normalized finite energy shell is an ordinary probability measure that can approach it. Coarea geometry turns the problem into convolution of density-of-states functions, making both convergence and finite-width error transparent.

The resulting picture is sharper than the slogan that the delta is merely a hidden finite projection. At regular energies, many shell profiles share the same limit; at finite width, they are distinct models. Hamiltonian flow preserves all normalizable energy-profile shells exactly, but invariance alone does not establish ergodicity or equilibrium.

For MTT, the theorem is now a reusable interface rather than a source claim. Once selected geometry provides a conserved quantity, preparation energy, and finite profile, the paper gives the normalized measure, sharp limit, and an error certificate. Selecting those inputs remains the physical task.

<div class="thebibliography">

99

L. C. Evans and R. F. Gariepy, *Measure Theory and Fine Properties of Functions*, revised edition, CRC Press, Boca Raton, 2015, doi:10.1201/b18333.

D. Ruelle, *Statistical Mechanics: Rigorous Results*, World Scientific, Singapore, 1999, doi:10.1142/4090.

A. Campa, T. Dauxois, and S. Ruffo, *Statistical Mechanics and Dynamics of Solvable Models with Long-Range Interactions*, Physics Reports **480** (2009) 57–159, doi:10.1016/j.physrep.2009.07.001.

</div>
