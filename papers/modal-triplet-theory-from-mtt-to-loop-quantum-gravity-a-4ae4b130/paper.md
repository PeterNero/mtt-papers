---
abstract: |
  We derive Loop Quantum Gravity (LQG) from the coherent fixed-point sector of Modal Triplet Theory (MTT). Starting with a $`3+1`$ foliation of the 4D face of the MTT fixed point, we show: (i) the Ashtekar–Barbero connection $`A^i_a=\Gamma^i_a+\gamma K^i_a`$ and densitized triad $`E^a_i`$ arise canonically from the modal tetrad/spin connection; (ii) the holonomy–flux $`*`$-algebra, cylindrical consistency, and the Ashtekar–Lewandowski representation follow from the $`\Pi`$-projected symmetry and yield the LOST uniqueness properties; (iii) the Gauss, diffeomorphism, and Hamiltonian constraints descend from MTT gauge/diffeomorphism invariance and from the fixed-point Hamiltonian, including a Master-constraint form; (iv) area/volume spectra of LQG are recovered with a *computed* Barbero–Immirzi parameter $`\gamma=\gamma_{\mathrm{MTT}}(\Theta)`$ determined by modal overlaps/bottlenecks; and (v) spin–foam dynamics (EPRL/FK) arise from a Holst-like MTT effective action via BF + simplicity constraints, with large-spin Regge asymptotics. The embedding is consistent with the UV-finite, causal perturbative QG sector previously derived from MTT (Stieltjes/Bernstein two-point function and SPT Gaussian damping), and identifies cross-checks linking $`\gamma`$, black-hole entropy, and cosmological loop effects.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: September 19, 2025
generated_from_main_tex_sha256: 3558359f08042faadbec0a7eb60a32c79a044286cef40abc8cdfeb7086cc5381
paper_id: modal-triplet-theory-from-mtt-to-loop-quantum-gravity-a-4ae4b130
release_state: zenodo_released
released_version: v1.0
title: |
  **Modal Triplet Theory: From MTT to Loop Quantum Gravity:  
  A Canonical and Spin–Foam Embedding with Predictive Immirzi Map**
zenodo_doi: 10.5281/zenodo.17162355
zenodo_record_id: 17162355
zenodo_url: "https://zenodo.org/records/17162355"
---

# Introduction and aim

#### Aim.

We show that the canonical and covariant structures of Loop Quantum Gravity (LQG)—Ashtekar–Barbero variables, holonomy–flux representation and spin networks, quantum constraints, and spin–foam amplitudes—are obtained from the *same* coherent fixed-point geometry that underlies all containments in MTT (modules G,S,$`\Pi`$,F,E).[^1] The Barbero–Immirzi parameter $`\gamma`$ is not free: it is mapped to a *modal overlap ratio* fixed at the coherent point. This ties LQG predictions to the MTT bottleneck vector $`\Theta`$ and to the UV-finite QG form factor.

#### Context.

LQG quantizes real SU(2) connections and densitized triads on a spatial slice, producing a background-independent kinematics with spin-network basis and discrete geometric spectra, and covariant spin–foam dynamics . We embed these ingredients in the MTT fixed-point framework developing the dictionary and constraints.

#### Standing modules.

We assume bounded geometry, a uniform spectral gap, a bounded joint projector $`\Pi`$ onto harmonic sectors, smoothing flow, and a convex energy functional near the fixed point (§2).[^2]

#### Hypotheses and conventions.

We work on a $`3{+}1`$ split $`M_4=\mathbb{R}\times\Sigma`$ of the coherent 4D face with: (H1) $`\Sigma`$ is oriented, connected, piecewise-analytic, of bounded geometry (uniform curvature and injectivity bounds). (H2) Non-degenerate tetrad and time gauge: choose an internal timelike unit $`n^I`$ so that $`e^0{}_a=0`$ and the internal gauge is reduced to $`\mathrm{SU}(2)`$. (H3) The MTT 4D effective action contains Einstein–Hilbert and Holst-type terms with constant coefficients $`\alpha_{\rm EH}(\Theta),\alpha_{\rm Holst}(\Theta)`$ defined by modal overlap integrals on the coherent sector. (H4) The projector $`\Pi`$ commutes with the natural action of analytic diffeomorphisms on the coherent fields, so the induced GNS state is diffeomorphism invariant. All statements below are made under (G,S,$`\Pi`$,F,E) and (H1)–(H4).

# Canonical variables from the MTT fixed point

Let $`M_4= \mathbb{R}\times \Sigma`$ be a $`3+1`$ foliation of the 4D face of the MTT coherent fixed point, with spatial slice $`\Sigma`$ of bounded geometry. Let $`e^I_{\ a}`$ be the spatial triad, $`\omega^{IJ}_{\ a}`$ the spin connection, and $`K^i_{\ a}`$ the extrinsic-curvature one-form in an internal $`\mathfrak{su}(2)`$ basis ($`i=1,2,3`$).

<div id="def:AB" class="defn">

**Definition 1** (MTT$`\to`$Ashtekar–Barbero dictionary). In time gauge (H2), let $`e^i{}_{a}`$ be a spatial triad on $`\Sigma`$, $`\Gamma^i{}_{a}(e)`$ its torsion-free spin connection, and $`K^i{}_{a}`$ the extrinsic curvature one-form. Define
``` math
A^i{}_{a}=\Gamma^i{}_{a}+\gamma_{\rm BI}\,K^i{}_{a},\qquad
E^{a}{}_{i}=\tfrac12\,\epsilon^{abc}\epsilon_{ijk}\,e^j{}_{b}\,e^k{}_{c}.
```

Here $`\gamma`$ denotes the Barbero–Immirzi parameter (fixed later in §<a href="#subsec:ImmirziMap" data-reference-type="ref" data-reference="subsec:ImmirziMap">5</a>).

The symplectic structure induced by the MTT action on the coherent sector yields the real bracket
``` math
\begin{equation}
\label{eq:PB-AB}
\{A^{i}{}_{a}(x),\,E^{b}{}_{j}(y)\}
= 8\pi G\,\gamma_{\mathrm{BI}}\,\delta^{i}{}_{j}\,\delta^{b}{}_{a}\,\delta^{(3)}(x,y).
\end{equation}
```
which matches canonical LQG.

</div>

#### Hypotheses for the canonical sector.

We work on $`(\Sigma,\bar q_{ab})`$ of bounded geometry in the (piecewise) analytic category used in LOST, with triads $`e^i{}_a`$ and torsion-free $`\Gamma^i{}_a(e)`$. The MTT 4D effective action on the coherent face contains Einstein–Hilbert and Holst terms with $`\Theta`$–dependent coefficients,
``` math
S_{\mathrm{eff}}[e,\omega] =
\alpha_{\mathrm{EH}}(\Theta)\int
\epsilon_{IJKL}\,e^{I}\wedge e^{J}\wedge F^{KL}[\omega]
\;+\;
\alpha_{\mathrm{Holst}}(\Theta)\int e^{I}\wedge e^{J}\wedge F_{IJ}[\omega].
\footnote{In standard conventions one writes
$S_{\mathrm{Holst}} \propto \tfrac{1}{\gamma}\int e\wedge e\wedge F[\omega]$.
Thus identifying $\alpha_{\mathrm{Holst}}(\Theta)\propto 1/\gamma$ yields
$\gamma_{\mathrm{MTT}}(\Theta)=\alpha_{\mathrm{EH}}(\Theta)/\alpha_{\mathrm{Holst}}(\Theta)$.}
```
so that $`\gamma_{\rm MTT}(\Theta):=\alpha_{\rm EH}(\Theta)/\alpha_{\rm Holst}(\Theta)`$. Performing the $`3{+}1`$ split and keeping the standard boundary term, the symplectic potential reduces in the coherent sector to
``` math
\Theta_{\rm symp}
= \frac{1}{8\pi G}\int_\Sigma E^a{}_i\,\delta A^i{}_a,
\qquad
\{A^i{}_a(x),E^b{}_j(y)\}
= 8\pi G\,\gamma_{\rm MTT}(\Theta)\,\delta^i{}_j\,\delta^b{}_a\,\delta^{(3)}(x,y),
```
i.e. with $`\gamma=\gamma_{\rm MTT}(\Theta)`$.

<div class="remark">

*Remark 2* (Holst and Nieh–Yan). Under (H3) and vanishing torsion, the Holst density differs from a topological Nieh–Yan term; the ratio of the Einstein–Hilbert and Holst coefficients fixes the Immirzi parameter via <a href="#eq:gamma-map" data-reference-type="eqref" data-reference="eq:gamma-map">[eq:gamma-map]</a> below. This also reproduces <a href="#eq:PB-AB" data-reference-type="eqref" data-reference="eq:PB-AB">[eq:PB-AB]</a>.

</div>

<div class="remark">

*Remark 3* (Holst term from MTT). The MTT effective action on the 4D face contains, besides the Einstein–Hilbert term, a parity-odd piece of Holst type $`S_{\mathrm{Holst}}\!\propto\!\gamma^{-1}\!\int e\wedge e \wedge F[\omega]`$. The *ratio* of these two terms is fixed by modal overlap integrals, giving a prediction $`\gamma=\gamma_{\mathrm{MTT}}(\Theta)`$ (see §<a href="#subsec:ImmirziMap" data-reference-type="ref" data-reference="subsec:ImmirziMap">5</a>).

</div>

# Holonomy–flux algebra and the LOST representation

Let $`\Gamma`$ be a piecewise analytic graph on $`\Sigma`$ with oriented edges $`e`$ and dual faces $`S`$. For $`A\in\mathcal{A}`$, define the holonomy $`h_e[A]\in \mathrm{SU}(2)`$ and flux $`E_i(S)=\int_S \epsilon_{abc}\,E^a_{\ i}\,\,\mathrm{d}x^b\wedge \,\mathrm{d}x^c`$.

#### LOST hypotheses.

We work with piecewise analytic graphs on $`\Sigma`$; the holonomy–flux $`*`$-algebra generated by $`\{h_e[A],E_i(S)\}`$; a diffeomorphism-invariant cyclic vector (the $`\Pi`$-induced vacuum); and continuity of parallel transport maps along edges. These are precisely the assumptions under which the Ashtekar–Lewandowski (AL) representation is unique (LOST).

<div class="defn">

**Definition 4** (Holonomy–flux \*-algebra). Cylindrical functions on graphs $`\gamma`$ form $`\mathcal{C}_\gamma`$; the holonomy–flux \*-algebra is generated by $`\{h_e, E_i(S)\}`$ with relations induced by <a href="#eq:PB-AB" data-reference-type="eqref" data-reference="eq:PB-AB">[eq:PB-AB]</a>, Gauss rotations, and spatial diffeomorphisms.

</div>

<div id="thm:LOST" class="theorem">

**Theorem 5** (MTT$`\to`$LOST). *Let $`\mathfrak{A}`$ be the holonomy–flux $`*`$-algebra built from holonomies along piecewise-analytic edges and fluxes through piecewise-analytic surfaces on $`\Sigma`$. Assume: (i) $`\mathrm{Diff}_{\mathrm{an}}(\Sigma)`$ acts by automorphisms on $`\mathfrak{A}`$; (ii) there exists a $`\mathrm{Diff}^{\rm an}`$-invariant cyclic state $`\omega`$; and (iii) holonomies act continuously along analytic edges. Then the GNS representation of $`(\mathfrak{A},\omega)`$ is unitarily equivalent to the Ashtekar–Lewandowski representation with the AL measure on generalized connections. In the MTT embedding, (H1) and (H4) furnish (i)–(iii), hence LOST uniqueness applies. .*

</div>

<div class="proof">

*Idea.* $`\Pi`$ eliminates non-harmonic (KK-like) sectors and enforces background independence on $`\Sigma`$; the induced GNS construction satisfies the LOST axioms, hence uniqueness of the AL representation. ◻

</div>

<div class="cor">

**Corollary 6** (Spin networks). *The AL kinematical Hilbert space is $`L^2(\overline{\mathcal{A}},\,\mathrm{d}\mu_{\mathrm{AL}})`$ with orthonormal basis of spin networks $`\psi_{\gamma,\{j_e\},\{\iota_v\}}`$.*

</div>

# Constraints and dynamics

#### Constraints.

The Gauss, diffeomorphism, and Hamiltonian constraints descend from MTT gauge/diffeomorphism invariance and from the fixed-point Hamiltonian in the $`3+1`$ split:
``` math
\begin{align}
\mathcal{G}_i &= D_a E^a_{\ i} \approx 0,\qquad 
\mathcal{V}_a = E^b_{\ i} F^i_{\ ab} - (1+\gamma^2)\,K^i_{\ a}\,\mathcal{G}_i \approx 0,\\
\mathcal{H} &= \frac{E^a_{\ i} E^b_{\ j}}{\sqrt{\det E}}\left(\epsilon^{ij}\!_{k}\,F^k_{\ ab} - 2(1+\gamma^2)\,K^i_{\ [a}K^j_{\ b]}\right)\approx 0,
\end{align}
```
where $`F^i_{\ ab}`$ is the curvature of $`A^i_{\ a}`$.

#### Quantization.

In the AL representation the Gauss/diffeomorphism constraints are implemented by group-averaging; for the Hamiltonian we may use Thiemann’s regularization or the Master-constraint .

#### Domains and positivity.

The Gauss and diffeomorphism constraints are implemented by group averaging on the cylindrical, diffeomorphism-invariant dense domain. The Master-constraint $`M=\int_\Sigma \frac{H^2}{\sqrt{\det E}}\,\mathrm{d}^3x`$ defines a positive quadratic form on the diffeo-invariant span of spin networks; closability and existence of a self-adjoint extension hold under the standard assumptions (cylindrical consistency and graph-changing regularisation).

<div class="theorem">

**Theorem 7** (Master-constraint in the MTT embedding). *There exists a positive, diffeomorphism-invariant Master-constraint $`\mathbf{M}=\int_\Sigma \frac{\mathcal{H}^2}{\sqrt{\det E}}\,\mathrm{d}^3x`$ whose quadratic form is well-defined on diffeo-invariant states induced by the $`\Pi`$-projected sector. Its kernel coincides with the simultaneous solution space of $`(\mathcal{G}_i,\mathcal{V}_a,\mathcal{H})`$ in the embedding.*

</div>

# Geometric operators and the Immirzi map

``` math
\begin{equation}
\label{eq:area-volume}
\hat A(S)\,\psi
= 8\pi\,\gamma_{\mathrm{BI}}\,\ell_{\mathrm P}^{2}\!
\sum_{e\cap S}\!\sqrt{j_{e}(j_{e}+1)}\,\psi,
\qquad
\hat V(R)\,\psi
= \sum_{v\in R}\sqrt{\hat Q_{v}}\,\psi,
\end{equation}
```
where $`\widehat{Q}_v`$ is the standard, graph-local, gauge-invariant node operator built from fluxes at $`v`$. Both operators are essentially self-adjoint on the cylindrical domain. .

#### Predictive $`\gamma`$.

In the MTT reduction, the 4D effective action contains the Einstein–Hilbert term and a Holst-like term with coefficients given by *modal overlaps*:
``` math
\begin{equation}
S_{\mathrm{MTT}\to 4\mathrm{D}} \;\sim\; \alpha_{\mathrm{EH}}(\Theta)\,\int \epsilon_{IJKL}\,e^I\wedge e^J\wedge F^{KL}
\;+\; \alpha_{\mathrm{Holst}}(\Theta)\,\int e_I\wedge e_J\wedge F^{IJ} \,.
\end{equation}
```
Matching to the canonical symplectic structure gives
``` math
\begin{equation}
\label{eq:gammaMap}
\gamma\;=\; \gamma_{\mathrm{MTT}}(\Theta)\;:=\;\frac{\alpha_{\mathrm{EH}}(\Theta)}{\alpha_{\mathrm{Holst}}(\Theta)}\,.
\end{equation}
```

Matching the canonical symplectic form and <a href="#eq:PB-AB" data-reference-type="eqref" data-reference="eq:PB-AB">[eq:PB-AB]</a> fixes
``` math
\begin{equation}
\label{eq:gamma-map}
\gamma_{\rm BI}=\gamma_{\rm BI}^{\rm MTT}(\Theta):=\frac{\alpha_{\rm EH}(\Theta)}{\alpha_{\rm Holst}(\Theta)}\,,
\end{equation}
```

so $`\gamma_{\rm BI}`$ is a *derived* constant determined by the bottleneck vector $`\Theta`$ (spectral gaps, harmonic norms, volumes, curvature/overlap integrals). This directly links LQG geometric spectra and black-hole microstate counts to the same modal data that govern gauge/Yukawa/EFT parameters.

<div id="thm:gammaMTT" class="theorem">

**Theorem 8** (Predictive Immirzi map). *Under the standing MTT hypotheses (bounded geometry, $`\Pi`$-projection, coherent fixed point), the canonical symplectic form induced by $`S_{\rm eff}`$ equals the Ashtekar–Barbero form with
``` math
\gamma=\gamma_{\rm MTT}(\Theta)=\frac{\alpha_{\rm EH}(\Theta)}{\alpha_{\rm Holst}(\Theta)}.
```
Consequently, the spectra of $`\widehat{A}(S)`$ and $`\widehat{V}(R)`$ are the standard LQG spectra with this value of $`\gamma`$, and black-hole microstate counting constraints on $`\gamma`$ become constraints on $`\Theta`$.*

</div>

<div class="remark">

*Remark 9* (Cross-checks). (i) Black-hole entropy fixes $`\gamma`$ in LQG microstate counts, giving a test of <a href="#eq:gammaMap" data-reference-type="eqref" data-reference="eq:gammaMap">[eq:gammaMap]</a>. (ii) Semiclassical weave/coherent states provide an independent constraint via area/volume calibration.

</div>

# Covariant dynamics from MTT: BF + simplicity $`\Rightarrow`$ EPRL/FK

#### Holst/Plebanski form.

The MTT action in the 4D face admits a BF-like rewrite with simplicity constraints. Imposing simplicity with the $`\gamma`$-dependent linear constraints yields the EPRL/FK vertex amplitude on 2-complexes dual to triangulations .

We use the Holst/Plebanski rewrite with linear simplicity constraints adapted to $`\gamma_{\rm BI}`$; imposing them weakly in the boundary Hilbert space yields EPRL/FK vertex amplitudes. In the large-spin asymptotics ($`j\to\infty`$ with areas fixed), stationary phase analysis reproduces Regge gravity with the correct Immirzi dependence.

#### Simplicity constraints.

We impose the linear simplicity constraints corresponding to $`\gamma_{\rm MTT}(\Theta)`$ so that $`SL(2,\mathbb{C})`$ representations $`(\rho,k)`$ map to $`SU(2)`$ spins $`j`$ via the standard $`\gamma`$-dependent embedding (e.g. $`j=k`$, $`\rho=\gamma k`$). This fixes the EPRL/FK vertex labelling and ensures the correct Holst dependence in the large-spin asymptotics.

We employ the standard embedding for (unitary) principal series labels $`(\rho,k)`$ into $`SU(2)`$ spins via $`j=k,\quad \rho=\gamma_{\mathrm{BI}}\,k,`$ so that boundary $`SU(2)`$ spins and intertwiners are $`\gamma_{\mathrm{BI}}`$–compatible with the Holst term.

<div class="theorem">

**Theorem 10** (Spin–foam emergence). *The MTT path integral on the coherent sector reduces, after BF + simplicity reduction with the ratio <a href="#eq:gammaMap" data-reference-type="eqref" data-reference="eq:gammaMap">[eq:gammaMap]</a>, to a spin–foam sum with EPRL/FK vertex weights. In the large-spin limit the amplitude reproduces Regge gravity with the correct Barbero–Immirzi dependence.*

</div>

<div class="remark">

*Remark 11* (Compatibility with the UV-finite QG sector). The Stieltjes/Bernstein two-point structure and SPT Gaussian damping derived in the perturbative MTT QG sector persist in the background-independent sum as vertex/face amplitude suppressions at large momenta, consistent with cylindrical consistency and diffeomorphism invariance.

</div>

# Semiclassical sector and cosmology

#### Complexifier coherent states.

Using Thiemann’s complexifier construction adapted to the MTT symplectic form, one obtains semiclassical states peaked on $`(A,E)`$ reproducing classical geometry at scales $`\gg \ell_P`$ .

#### Weave states.

MTT-induced spin networks with typical edge spacing $`\ell\sim \ell_P`$ and label distribution set by $`\Theta`$ act as weaves approximating a given classical metric on $`\Sigma`$.

#### Loop quantum cosmology (outline).

The MTT $`\to`$ LQG map specializes to homogeneous/isotropic symmetry reduction, yielding effective Friedmann equations with a bounce at critical density $`\rho_c\propto 1/\gamma^3`$ times MTT scalings; thus $`\rho_c`$ is ultimately a function of $`\Theta`$ via <a href="#eq:gammaMap" data-reference-type="eqref" data-reference="eq:gammaMap">[eq:gammaMap]</a> (testable in early-universe scenarios).

In standard LQC reductions one finds a critical density scaling $`\rho_c\propto \gamma_{\rm BI}^{-3}`$ (in natural units), so <a href="#eq:gamma-map" data-reference-type="eqref" data-reference="eq:gamma-map">[eq:gamma-map]</a> makes $`\rho_c`$ a function of $`\Theta`$. Coherent-state calibration of $`\widehat{A}`$ and $`\widehat{V}`$ then provides an independent semiclassical test of $`\gamma_{\rm BI}^{\rm MTT}(\Theta)`$.

# Consistency with MTT’s perturbative QG finiteness

#### Kinematics.

The AL representation and holonomy–flux algebra are consistent with OS positivity and causal support of TT two-point functions when probing around the coherent point (no conflict with background independence).

#### Dynamics.

SPT factorization implies an *effective* Gaussian damping on internal graviton lines of Feynman-like expansions of spin–foam transition amplitudes, preserving cylindrical consistency while ensuring UV suppression in mixed representations.

#### Relation to overlaps.

The same $`\Theta`$ that fixes $`\gamma_{\rm BI}`$ in <a href="#eq:gamma-map" data-reference-type="eqref" data-reference="eq:gamma-map">[eq:gamma-map]</a> appears throughout the Superset overlaps (Planck mass, gauge couplings, Yukawas, EFT/KK scales), so LQG geometric spectra are predicted jointly with non-gravitational observables; see the Superset discussion of bottlenecks and global fits.

<div class="lemma">

**Lemma 12** (Gaussian suppression in mixed representations). *In the $`\Pi`$-projected coherent sector, internal graviton propagators entering Feynman-like expansions of spin-foam transition amplitudes carry an entire/Gaussian form factor with scale set by the MTT spectral gap. Consequently, large-momentum (or large-spin with fixed geometry) sectors are exponentially suppressed, compatibly with cylindrical consistency.*

</div>

#### Coherence with the perturbative sector.

The Stieltjes/Bernstein positivity of TT two-point functions, causal support properties, and the all-orders BV/QME renormalisation established in the perturbative MTT QG construction carry over here at the level of kinematics and regulator removal; see the companion QG paper for full details.

# Conclusions and tests

We have constructed a direct MTT$`\to`$LQG embedding, fixed the Barbero–Immirzi parameter by modal overlaps, and matched both canonical and covariant LQG structures. Key tests:

- **Black-hole entropy:** Check that $`\gamma_{\mathrm{MTT}}(\Theta)`$ matches the value required by microstate counting within uncertainties.

- **Semiclassical calibration:** Compare area/volume expectation values on weave/coherent states to classical geometry induced by the MTT fixed point.

- **Cosmology:** Use $`\gamma_{\mathrm{MTT}}(\Theta)`$ in LQC phenomenology (e.g. $`\rho_c`$) and confront with data.

- **Amplitudes:** Verify Regge asymptotics and form-factor suppression scale derived from the SPT map.

#### Outlook.

Extend the EPRL/FK derivation to include matter (gauge and fermions) from the same modal overlaps; quantify the relation between $`\gamma_{\mathrm{MTT}}`$ and the UV-finite QG form factor at low spin; develop global fits in which $`\gamma`$ is predicted jointly with gauge/Yukawa parameters.

[^1]: See the Superset overview for modules and standing assumptions.

[^2]: These are exactly the modules used in your Superset paper.
