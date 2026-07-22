---
abstract: |
  This corrected successor asks when a Diósi–Penrose (DP) law can arise as an effective shadow of Modal Triplet Theory (MTT). Completely positive reduction and lifting channels give an exact Nakajima–Zwanzig memory identity; a Davies–GKSL generator still requires an independently justified weak-coupling, Markov and secular limit. The new result is a Penrose–Schoenberg completion theorem. Conditional on the selected two-derivative Einstein/TEGR action, its static weak-field constraint and a declared external smearing map, the Newton self-energy of two branch mass densities is one half of a squared Hilbert-space distance. Its pairwise matrix is therefore conditionally negative definite, so $`\exp[-tE_G/\hbar]`$ defines a completely positive, trace-preserving dephasing semigroup for every finite branch set. Its generator is exactly the regulated DP double commutator, and it is the unique population-preserving pure-dephasing semigroup with those real Penrose rates. This closes positivity and Markovian completion; it does not make Penrose’s provisional lifetime estimate an MTT source theorem. MTT must still select the external regularization, the exact $`E_G/\hbar`$ rate law (or an equivalent correlation kernel), and, for objective single-outcome collapse, a stochastic instrument and probability rule. Thus the DP law is a rigorous restricted completion, not yet a derived fundamental law of MTT.
author:
- Peter Nero
current_version: v3
date: |
  July 2026  
  Version 3
generated_from_main_tex_sha256: 16111263ce94fdfa4cf9f57a4ab6bd80bdeb32e7fd55df158ef11691bd4eab3e
paper_id: gravitationally-induced-collapse-as-an-effective-limit-d74eb471
release_state: zenodo_released
released_version: v1.0
title: |
  **Gravitationally Induced Collapse in Modal Triplet Theory**  
  A Penrose–Schoenberg Completion and Source Contract
zenodo_doi: 10.5281/zenodo.18261600
zenodo_record_id: 18261600
zenodo_url: "https://zenodo.org/records/18261600"
---

# Revision verdict

The original paper contained a useful physical proposal but advertised several conditional steps as derivations. Version 2 repaired the open-system typing. This version additionally separates a gravitational energy theorem from a collapse-rate selection theorem. The strongest proven chain is
``` math
\begin{align*}
\text{selected Einstein/TEGR law}
&\xRightarrow{\text{static weak field + smearing}} E_{G,\ell}
   =\tfrac12\|r_a-r_b\|^2\\
&\xRightarrow{\text{exact Penrose rate rule}}
   e^{-tE_{G,\ell}/\hbar}\ \text{CPTP semigroup}\\
&\Longleftrightarrow \text{regulated DP generator on the branch algebra}.
\end{align*}
```
An independent open-system route remains
``` math
\begin{align*}
 \text{typed reduction/lifting}
 &\Longrightarrow\text{exact memory equation}\\
 &\xRightarrow{\text{Davies + Newton source}}
 \text{the same DP generator}.
\end{align*}
```
Neither route selects its marked hypotheses from projection, curvature dominance, an internal gap, or the present $`q=79`$ geometry alone.

The compactification is written throughout as $`Y_4\times X_6`$. No decomposition $`X_6=B_1\times B_2\times B_3`$ is assumed. This is compatible with the selected Fu–Yau candidate and with the local $`1<2<3`$ filtration without identifying the filtration with a product topology.

# Typed shadow dynamics

## Reduction and lifting channels

Let $`\mathcal H_U`$ be an upstairs Hilbert space at a finite spectral cutoff and let $`\mathcal H_S`$ be the retained four-dimensional system space. Write $`\mathcal T(\mathcal H)`$ for trace-class operators on $`\mathcal H`$. Assume completely positive, trace-preserving maps
``` math
\mathcal R:\mathcal T(\mathcal H_U)\to\mathcal T(\mathcal H_S),\qquad
 \mathcal J:\mathcal T(\mathcal H_S)\to\mathcal T(\mathcal H_U),
 \qquad \mathcal R\mathcal J=I_{\mathcal T(\mathcal H_S)}.
```
Define superoperators on $`\mathcal T(\mathcal H_U)`$ by
``` math
\mathbf P=\mathcal J\mathcal R,\qquad \mathbf Q=I-\mathbf P.
```

<div id="thm:typed" class="theorem">

**Theorem 1** (Correct projection type). *The map $`\mathbf P`$ is a completely positive, trace-preserving idempotent: $`\mathbf P^2=\mathbf P`$. Its range is $`\mathcal J(\mathcal T(\mathcal H_S))`$. In particular, $`\mathbf P`$ acts on density operators; it is not a vector-space projector on $`\mathcal H_U`$ inserted into a Liouville-space formula.*

</div>

<div class="proof">

*Proof.* Complete positivity and trace preservation are stable under composition. Moreover
``` math
\mathbf P^2=\mathcal J\mathcal R\mathcal J\mathcal R=\mathcal J(\mathcal R\mathcal J)\mathcal R=\mathcal J\mathcal R=\mathbf P.
```
The range statement follows from $`\mathbf PX=\mathcal J(\mathcal RX)`$ and $`\mathbf P\mathcal JY=\mathcal JY`$. ◻

</div>

## Normalized coherent filtering

A physically interesting coherent filter may instead be a CP, trace-nonincreasing map $`\mathcal F`$. It does not generally output a state.

<div id="prop:normalization" class="proposition">

**Proposition 2** (Conditional normalization). *For a density operator $`\rho`$ with $`p(\rho)=\mathop{\mathrm{Tr}}\mathcal F(\rho)>0`$, the conditional retained state is
``` math
\rho_{\mathcal F}=\frac{\mathcal F(\rho)}{p(\rho)}.
```
The map $`\rho\mapsto\rho_{\mathcal F}`$ is nonlinear unless $`p(\rho)`$ is constant on the state space. Therefore an unnormalized filtered operator cannot be used as a deterministic reduced density matrix, and postselection cannot silently be replaced by linear open-system evolution.*

</div>

<div class="proof">

*Proof.* The quotient has unit trace and is positive. If the normalized map were affine for all mixtures, comparing a mixture of two states with different success probabilities would contradict the state-dependent denominator. Hence affinity requires constant success probability on the relevant convex set. ◻

</div>

# Exact memory before Markov approximation

Let $`\mathcal L`$ be a bounded generator on $`\mathcal T(\mathcal H_U)`$; this is automatic at a finite spectral cutoff. Let $`X(t)=e^{t\mathcal L}X_0`$.

<div id="thm:NZ" class="theorem">

**Theorem 3** (Nakajima–Zwanzig identity). *The retained component obeys the exact equation
``` math
\begin{align}
\frac{d}{dt}\mathbf PX(t)
={}&\mathbf P\mathcal L\mathbf PX(t)
+\mathbf P\mathcal L\mathbf Qe^{t\mathbf Q\mathcal L\mathbf Q}\mathbf QX_0 \nonumber\\
&+\int_0^t
\mathbf P\mathcal L\mathbf Qe^{(t-s)\mathbf Q\mathcal L\mathbf Q}
\mathbf Q\mathcal L\mathbf PX(s)\,ds .
\label{eq:NZ}
\end{align}
```
If $`X_0=\mathcal J\rho_0`$, the inhomogeneous second term vanishes. The final term remains a memory kernel unless an additional limit controls it.*

</div>

<div class="proof">

*Proof.* Apply $`\mathbf P`$ and $`\mathbf Q`$ to $`\dot X=\mathcal LX`$. Variation of constants gives
``` math
\mathbf QX(t)=e^{t\mathbf Q\mathcal L\mathbf Q}\mathbf QX_0+
\int_0^t e^{(t-s)\mathbf Q\mathcal L\mathbf Q}\mathbf Q\mathcal L\mathbf PX(s)\,ds.
```
Substitution in the $`\mathbf P`$ equation yields <a href="#eq:NZ" data-reference-type="eqref" data-reference="eq:NZ">[eq:NZ]</a>. ◻

</div>

Equation <a href="#eq:NZ" data-reference-type="eqref" data-reference="eq:NZ">[eq:NZ]</a> is the correct exact output of projection  . It is generally non-Markovian. Complete positivity of the exact reduced channel $`\mathcal Re^{t\mathcal L}\mathcal J`$ does not imply that its time-local generator exists or has GKSL form at each time.

# When a GKSL generator is justified

Consider a system–environment Hamiltonian at finite cutoff,
``` math
H_\lambda=H_S+H_E+\lambda\sum_\alpha A_\alpha\otimes B_\alpha,
```
with a stationary environmental state $`\rho_E`$. Let
``` math
C_{\alpha\beta}(t)=
\mathop{\mathrm{Tr}}_E\!\left(\rho_E B_\alpha(t)B_\beta(0)\right).
```

<div id="ass:Davies" class="assumption">

**Assumption 4** (Davies source conditions). The initial state is factorized at the preparation time; the correlations are stationary and integrable strongly enough for the weak-coupling limit; the rescaled time is $`t=\lambda^{-2}\tau`$; and the secular average over distinct Bohr frequencies exists. The Fourier matrices
``` math
\gamma_{\alpha\beta}(\omega)=
\int_{-\infty}^{\infty}e^{i\omega t}C_{\alpha\beta}(t)\,dt
```
are finite.

</div>

<div id="thm:Davies" class="theorem">

**Theorem 5** (Conditional Davies–GKSL limit). *Under Assumption <a href="#ass:Davies" data-reference-type="ref" data-reference="ass:Davies">4</a> and the standard finite-system weak-coupling convergence hypotheses, the interaction-picture reduced dynamics converges on bounded rescaled-time intervals to a completely positive semigroup. Its generator is
``` math
\mathcal L_D(\rho)=-i[H_{\rm LS},\rho]
+\sum_{\omega,\alpha,\beta}\gamma_{\alpha\beta}(\omega)
\left(
A_\beta(\omega)\rho A_\alpha(\omega)^\dagger
-\frac12\{A_\alpha(\omega)^\dagger A_\beta(\omega),\rho\}
\right).
```
The matrices $`\gamma(\omega)`$ are positive semidefinite. Without this or another explicit Markovian limit, Theorem <a href="#thm:NZ" data-reference-type="ref" data-reference="thm:NZ">3</a> does not imply a GKSL equation.*

</div>

<div class="proof">

*Proof.* This is the Davies weak-coupling theorem  applied to the declared source data. Positivity of the correlation Fourier matrices is the positive-type/Bochner step that produces complete positivity in the GKSL form  . The theorem is conditional here because MTT has not yet emitted the required correlation functions. ◻

</div>

# The precise Diósi–Penrose limit

## Newton self-energy from the gravitational constraint

Let $`G_{\rm eff}>0`$ be the coefficient appearing in the selected four-dimensional Einstein/TEGR law. Let $`s_\ell`$ be a normalized real spatial smearing function and write $`\mu_{a,\ell}=s_\ell*\mu_a`$ for the regulated mass density of branch $`a`$. Define
``` math
K_\ell(\mathbf x,\mathbf y)=
 G_{\rm eff}\int_{\mathbb R^3}\!\!\int_{\mathbb R^3}
 \frac{s_\ell(\mathbf x-\mathbf u)s_\ell(\mathbf y-\mathbf v)}
 {|\mathbf u-\mathbf v|}\,d^3u\,d^3v.
```
Its Fourier multiplier is $`4\pi G_{\rm eff}|\widehat s_\ell(\mathbf k)|^2/|\mathbf k|^2\geq0`$, so it is a positive quadratic-form kernel on its regulated domain.

<div id="thm:NewtonEnergy" class="theorem">

**Theorem 6** (Newton-constraint energy theorem). *Assume the static weak-field limit of the selected MTT gravitational law obeys the Poisson constraint
``` math
-\Delta u_a=4\pi G_{\rm eff}\mu_{a,\ell},
 \qquad u_a(\mathbf x)\longrightarrow0\quad(|\mathbf x|\longrightarrow\infty).
```
For regulated densities for which the displayed integrals are finite, the positive incompatibility energy of branches $`a,b`$ is
``` math
\begin{align}
 E_{ab}^{(G,\ell)}
 &:=\frac{1}{8\pi G_{\rm eff}}
 \int_{\mathbb R^3}|\nabla(u_a-u_b)|^2\,d^3x \label{eq:field-energy}\\
 &=\frac12\int d^3x\,d^3y\,
 \delta\mu_{ab}(\mathbf x)K_\ell(\mathbf x,\mathbf y)
 \delta\mu_{ab}(\mathbf y), \qquad
 \delta\mu_{ab}:=\mu_a-\mu_b. \label{eq:newton-energy}
\end{align}
```
In particular $`E_{ab}^{(G,\ell)}\geq0`$, and it uses the same $`G_{\rm eff}`$ as the gravitational action rather than a new collapse-sector coupling.*

</div>

<div class="proof">

*Proof.* The decaying solution is $`u_a(\mathbf x)=G_{\rm eff}\int
\mu_{a,\ell}(\mathbf y)|\mathbf x-\mathbf y|^{-1}d^3y`$. Integration by parts and the Poisson equation give
``` math
\frac{1}{8\pi G_{\rm eff}}\int|\nabla\delta u|^2
 =\frac{1}{2}\int\delta u\,\delta\mu_\ell
 =\frac{G_{\rm eff}}{2}\int
 \frac{\delta\mu_\ell(\mathbf x)\delta\mu_\ell(\mathbf y)}
 {|\mathbf x-\mathbf y|}\,d^3x\,d^3y.
```
Moving the two smearings from the densities to the Green kernel yields <a href="#eq:newton-energy" data-reference-type="eqref" data-reference="eq:newton-energy">[eq:newton-energy]</a>. Positivity is immediate from <a href="#eq:field-energy" data-reference-type="eqref" data-reference="eq:field-energy">[eq:field-energy]</a>. ◻

</div>

The theorem is the controlled Newtonian content of the selected two-derivative gravity law. It derives the spatial quadratic form once $`G_{\rm eff}`$, the boundary condition and $`s_\ell`$ are supplied. It does not select the value of $`G_{\rm eff}`$ or the external smearing map.

## Penrose energy is an admissible branch metric

Let $`\{|a\rangle\}_{a=1}^N`$ be a finite set of approximate joint eigenstates of the regulated mass-density operators. Define vectors in the real Hilbert space $`L^2(\mathbb R^3;\mathbb R^3)`$ by
``` math
r_a=\frac{\nabla u_a}{\sqrt{4\pi G_{\rm eff}}}.
```
Theorem <a href="#thm:NewtonEnergy" data-reference-type="ref" data-reference="thm:NewtonEnergy">6</a> says exactly that
``` math
E_{ab}^{(G,\ell)}=\frac{1}{2}\|r_a-r_b\|^2.
```

<div id="thm:PenroseSchoenberg" class="theorem">

**Theorem 7** (Penrose–Schoenberg completely positive completion). *On the finite branch algebra define
``` math
\Gamma_{ab}:=\frac{E_{ab}^{(G,\ell)}}{\hbar},\qquad
 M_{ab}(t):=e^{-t\Gamma_{ab}}.
```
Then:*

1.  *$`\Gamma`$ is conditionally negative definite;*

2.  *$`M(t)`$ is positive semidefinite with $`M_{aa}(t)=1`$ for every $`t\geq0`$;*

3.  
    *``` math
    \mathcal T_t(\rho):=M(t)\circ\rho
    ```
    is a completely positive, trace-preserving, population-preserving semigroup; and*

4.  *its generator is the regulated DP generator
    ``` math
    \begin{equation}
     \mathcal D_{\rm DP}(\rho)=
     -\frac1{2\hbar}\int d^3x\,d^3y\,
     K_\ell(\mathbf x,\mathbf y)
     [\widehat\mu(\mathbf x),[\widehat\mu(\mathbf y),\rho]].
     \label{eq:DP-generator}
    \end{equation}
    ```
    It is the unique strongly continuous, time-homogeneous Schur semigroup on this branch algebra which preserves populations, has no additional diagonal Hamiltonian phase, and has infinitesimal real decay rates $`\Gamma_{ab}`$.*

</div>

<div class="proof">

*Proof.* For complex $`c_a`$ with $`\sum_a c_a=0`$, expansion of the squared distance gives
``` math
\sum_{a,b}\overline{c_a}c_b\Gamma_{ab}
 =-\frac{1}{\hbar}\left\|\sum_a c_a r_a\right\|^2\leq0.
```
Thus $`\Gamma`$ is conditionally negative definite. Schoenberg’s theorem   implies $`M(t)\succeq0`$ for all $`t\geq0`$. Because $`M_{aa}=1`$, the Schur multiplier has a Gram/Stinespring representation and is CPTP. Entrywise multiplication shows $`M(t+s)=M(t)\circ M(s)`$.

On a matrix unit $`|a\rangle\langle b|`$, the double commutator in <a href="#eq:DP-generator" data-reference-type="eqref" data-reference="eq:DP-generator">[eq:DP-generator]</a> multiplies by $`\delta\mu_{ab}(\mathbf x)\delta\mu_{ab}(\mathbf y)`$. Hence
``` math
\mathcal D_{\rm DP}(|a\rangle\langle b|)
 =-\frac{E_{ab}^{(G,\ell)}}{\hbar}|a\rangle\langle b|
 =-\Gamma_{ab}|a\rangle\langle b|,
```
which is the generator of $`\mathcal T_t`$. Finally, a strongly continuous scalar semigroup on each matrix unit with derivative $`-\Gamma_{ab}`$ at zero is $`e^{-t\Gamma_{ab}}`$; this proves uniqueness in the declared Schur class. ◻

</div>

This theorem is the missing specialization of the corpus’s general Schoenberg criterion: the physical branch separation is now the Newton field-energy distance, not an arbitrary damping matrix. Penrose obtained this self-energy from the squared difference of branch free-fall fields, but described its conversion into a lifetime only as a provisional order estimate . The theorem proves the mathematical completion of an exact rate rule; it does not promote that rule to a selected MTT law.

<div id="cor:DPDavies" class="corollary">

**Corollary 8** (Davies realization of the same generator). *If the independently controlled Davies source in Theorem <a href="#thm:Davies" data-reference-type="ref" data-reference="thm:Davies">5</a> couples through $`\widehat\mu(\mathbf x)`$ and its relevant zero-frequency Kossakowski kernel is $`K_\ell(\mathbf x,\mathbf y)/\hbar`$, then its dissipator is <a href="#eq:DP-generator" data-reference-type="eqref" data-reference="eq:DP-generator">[eq:DP-generator]</a> and its branch rates are $`E_{ab}^{(G,\ell)}/\hbar`$.*

</div>

<div class="proof">

*Proof.* Diagonalizing the positive kernel gives commuting Hermitian Lindblad operators. Their GKSL sum is <a href="#eq:DP-generator" data-reference-type="eqref" data-reference="eq:DP-generator">[eq:DP-generator]</a>; evaluation on branch matrix units was performed in Theorem <a href="#thm:PenroseSchoenberg" data-reference-type="ref" data-reference="thm:PenroseSchoenberg">7</a>. ◻

</div>

## Gaussian realization is not an outcome theorem

<div id="prop:unravelling" class="proposition">

**Proposition 9** (Random-unitary realization and outcome obstruction). *Let $`V=\operatorname{span}\{r_a\}`$ and let $`W_t`$ be standard Brownian motion on $`V`$. The diagonal random unitary
``` math
U_t(W)|a\rangle=
 \exp\!\left[-\frac{i}{\sqrt\hbar}\langle r_a,W_t\rangle\right]|a\rangle
```
satisfies
``` math
\mathcal T_t(\rho)=\mathbb E\bigl[U_t(W)\rho U_t(W)^\dagger\bigr].
```
Consequently the DP density-operator semigroup alone does not select objective single-outcome collapse: it admits an unravelling in which every individual state evolves unitarily with a random phase.*

</div>

<div class="proof">

*Proof.* The Gaussian characteristic function gives
``` math
\mathbb E\exp\!\left[-\frac{i}{\sqrt\hbar}
 \langle r_a-r_b,W_t\rangle\right]
 =\exp\!\left[-\frac{t}{2\hbar}\|r_a-r_b\|^2\right]
 =e^{-tE_{ab}^{(G,\ell)}/\hbar}.
```
This is exactly the Schur multiplier of Theorem <a href="#thm:PenroseSchoenberg" data-reference-type="ref" data-reference="thm:PenroseSchoenberg">7</a>. Since this unravelling has no state-vector reduction, the ensemble channel cannot by itself choose a collapse ontology, instrument, outcome probabilities or realized branch. A nonlinear collapse unravelling such as the Diósi construction  is additional data. ◻

</div>

<div class="corollary">

**Corollary 10** (What curvature dominance does not prove). *The statement that discarded modes are curvature dominated does not determine their two-point correlation function and therefore does not select a Davies realization. The selected Einstein/TEGR constraint fixes the Newton spatial form only after its effective coupling, boundary condition and external smearing are declared. It still does not prove the exact Penrose rate rule, Markov additivity, or an objective single-outcome process.*

</div>

## No smearing length from an internal gap alone

<div id="prop:scale" class="proposition">

**Proposition 11** (Scale-typing obstruction). *Let $`\lambda_{\rm int}`$ be an eigenvalue of an internal operator on $`X_6`$. The datum $`\lambda_{\rm int}`$ alone cannot canonically define an external spatial smearing length on $`Y_4`$. Such a definition requires an explicit metric normalization and an intertwiner, modulus, or response map that converts internal spectral units into external length units.*

</div>

<div class="proof">

*Proof.* Rescale the internal and external metrics independently. The internal eigenvalue changes under the internal rescaling while an external length changes under the external rescaling. No relation between them is invariant under these independent changes unless extra cross-sector data constrain the rescalings. Therefore $`\ell_{\rm coh}=\lambda_{\rm int}^{-1/2}`$ is at most an internal length before such a map is supplied. ◻

</div>

The regularization is experimentally consequential, not a cosmetic cure of the point-source divergence. A dedicated spontaneous-radiation search rules out the natural parameter-free DP version and places a lower bound on the effective nuclear mass-density radius . Any MTT-selected $`s_\ell`$ must therefore be transported to the experiment’s convention and tested rather than chosen only for formal convenience.

# Thresholds, knees and protocols

<div id="thm:analytic" class="theorem">

**Theorem 12** (Analytic finite-time response). *Let $`s\mapsto\mathcal L(s)`$ be a real-analytic family of bounded GKSL generators on a finite-dimensional state space. For fixed $`t<\infty`$, initial state $`\rho_0(s)`$ and observable $`A(s)`$ analytic in $`s`$, the response
``` math
f_t(s)=\mathop{\mathrm{Tr}}\!\left(A(s)e^{t\mathcal L(s)}\rho_0(s)\right)
```
is analytic. Hence a literal finite-strength nonanalytic knee cannot be inferred from such a family without a nonanalytic source, a stopping/conditioning operation, or a singular long-time, zero-noise, thermodynamic, or continuum limit.*

</div>

<div class="proof">

*Proof.* The exponential series for $`e^{t\mathcal L(s)}`$ converges locally uniformly in operator norm, and each term is analytic. Composition with analytic finite-dimensional data and the trace preserves analyticity. ◻

</div>

<div id="prop:OU" class="proposition">

**Proposition 13** (Finite-noise OU crossing is smooth). *For the Ornstein–Uhlenbeck process
``` math
dX_t=-\gamma(s)X_t\,dt+\sqrt{2D(s)}\,dW_t
```
in a bounded interval with absorbing endpoints, if $`\gamma`$ and $`D>0`$ vary smoothly, then the finite-domain mean first-passage solution varies smoothly through $`\gamma=0`$. A logistic knee may approximate a rapid crossover but is not an exact threshold theorem without a specified singular limit.*

</div>

<div class="proof">

*Proof.* The mean exit time solves a uniformly elliptic second-order boundary-value problem with smooth coefficients. Standard parameter dependence for this finite-domain problem is smooth while $`D`$ remains strictly positive. The sign change of the drift does not destroy ellipticity. ◻

</div>

Repeated interventions can produce Zeno or anti-Zeno behavior, but the sign of the crossover depends on the instrument, interval and spectral density. It is not forced by noninvertible projection alone. A valid MTT prediction must therefore emit the instrument and environment correlation data, rather than label protocol dependence as universal.

# Cross-sector source contract

Theorem <a href="#thm:PenroseSchoenberg" data-reference-type="ref" data-reference="thm:PenroseSchoenberg">7</a> removes a mathematical consistency blocker: once the exact Penrose rate matrix is supplied, complete positivity and the DP generator are automatic. The remaining physical promotion target is therefore sharper. Let $`\Theta_{\rm MTT}`$ denote selected geometric data. A direct fundamental route must construct
``` math
\begin{equation}
 \Theta_{\rm MTT}\longmapsto
 \bigl(G_{\rm eff},s_\ell,\widehat\mu,mathcal A_{ab}(t),
       \{\mathcal I_a\}\bigr),
 \label{eq:direct-source-map}
\end{equation}
```
where $`\mathcal A_{ab}`$ is the branch-coherence functional and $`\{\mathcal I_a\}`$ is included only if objective outcomes are claimed. The decisive rate-selection identity is
``` math
\begin{equation}
 -\left.\frac{d}{dt}\log|\mathcal A_{ab}(t)|\right|_{t=0}
 =\frac{E_{ab}^{(G,\ell)}}{\hbar}
 \quad\text{for every retained pair }a,b.
 \label{eq:rate-selection-target}
\end{equation}
```
Time-homogeneous Markov composition then gives $`\mathcal A_{ab}(t)=e^{-tE_{ab}^{(G,\ell)}/\hbar}`$ up to a separately declared diagonal Hamiltonian phase.

Alternatively, an environmental derivation must supply one source map
``` math
\Theta_{\rm MTT}\longmapsto
 \bigl(\mathcal R,\mathcal J,C_{\alpha\beta}(t),K_\ell,\ell,
 H_{\rm LS},\text{preparation and secular limits}\bigr)
```
with connection and unit conventions fixed. The following checks are then required:

1.  $`\mathcal R`$ and $`\mathcal J`$ are CPTP and $`\mathcal R\mathcal J=I`$ on the declared retained state space;

2.  the selected two-derivative action has the stated $`G_{\rm eff}`$ and its static constraint yields Theorem <a href="#thm:NewtonEnergy" data-reference-type="ref" data-reference="thm:NewtonEnergy">6</a>;

3.  the external smearing map $`s_\ell`$ is selected in physical units and is compatible with experimental bounds;

4.  the direct route proves <a href="#eq:rate-selection-target" data-reference-type="eqref" data-reference="eq:rate-selection-target">[eq:rate-selection-target]</a>, or the environmental route proves the remaining correlation conditions below;

5.  the correlation functions are positive type and satisfy the weak-coupling hypotheses;

6.  their Fourier kernel equals the regularized Newton kernel in the claimed regime;

7.  the approximation error is bounded on a declared time interval; and

8.  any objective-collapse claim supplies a normalized stochastic instrument or nonlinear state process and proves its outcome probabilities, rather than inferring single outcomes from the ensemble master equation.

Current MTT results now supply more of this chain than version 2 recorded. The finite $`q=79`$ TT operator and the same-source two-derivative Einstein/TEGR action fix the gravitational tensor shape, and Theorem <a href="#thm:NewtonEnergy" data-reference-type="ref" data-reference="thm:NewtonEnergy">6</a> fixes the Newton self-energy form in terms of the still-open $`G_{\rm eff}`$ and $`s_\ell`$. They do not yet prove <a href="#eq:rate-selection-target" data-reference-type="eqref" data-reference="eq:rate-selection-target">[eq:rate-selection-target]</a>, emit the corresponding environmental mass-density correlation function, or select a single-outcome instrument. These are distinct obligations; none should be hidden inside the word “projection.”

# Version delta

Relative to version 2, this successor:

- derives the regulated Newton self-energy from the static weak-field Einstein/TEGR constraint rather than treating its spatial form as an arbitrary bath kernel;

- proves that the pairwise Penrose energies are squared Hilbert distances and therefore conditionally negative definite;

- constructs the CPTP Penrose–Schoenberg semigroup and proves that its generator is exactly the DP double commutator;

- proves uniqueness inside the declared population-preserving pure-dephasing Markov class;

- shows that the same channel has a random-unitary Gaussian unravelling and hence does not by itself prove objective single outcomes;

- separates the direct Penrose-rate route from the Davies correlation-source route; and

- reduces the frontier to the selected external smearing, $`G_{\rm eff}`$, exact rate identity, controlled limit and outcome instrument.

All version-2 repairs remain in force: typed reduction/lifting, normalized filters, the exact memory equation, the Davies hypotheses, the scale-typing obstruction and the no-literal-knee results are not reopened.

# Conclusion

The spatial part of the DP proposal is now substantially less mysterious. Once the selected Einstein/TEGR law is placed in its static weak-field regime, branch incompatibility is the positive Newton field energy and therefore a squared Hilbert distance. The Penrose rate matrix consequently has a unique CPTP pure-dephasing Markov completion, whose generator is exactly the DP double commutator. This is a real theorem-level advance over merely assuming that a Kossakowski matrix is positive.

The remaining gap is also exact. Penrose’s argument motivates but does not derive the equality between MTT’s physical branch-decay rate and $`E_G/\hbar`$. MTT must select that identity or an equivalent Davies correlation kernel, the external smearing and effective Newton normalization, and controlled errors. Moreover, the ensemble DP channel does not select a realized outcome; an objective-collapse claim additionally needs a stochastic instrument and probability theorem. Version 3 therefore closes the gravitational-metric and completely-positive-completion layers without claiming that the source-selection or measurement problem is already solved.

<div class="thebibliography">

99 S. Nakajima, *On quantum theory of transport phenomena*, Progress of Theoretical Physics **20**, 948–959 (1958).

R. Zwanzig, *Ensemble method in the theory of irreversibility*, Journal of Chemical Physics **33**, 1338–1341 (1960), doi:10.1063/1.1731409.

E. B. Davies, *Markovian master equations*, Communications in Mathematical Physics **39**, 91–110 (1974), doi:10.1007/BF01608389.

V. Gorini, A. Kossakowski and E. C. G. Sudarshan, *Completely positive dynamical semigroups of N-level systems*, Journal of Mathematical Physics **17**, 821–825 (1976), doi:10.1063/1.522979.

G. Lindblad, *On the generators of quantum dynamical semigroups*, Communications in Mathematical Physics **48**, 119–130 (1976), doi:10.1007/BF01608499.

L. Diósi, *A universal master equation for the gravitational violation of quantum mechanics*, Physics Letters A **120**, 377–381 (1987), doi:10.1016/0375-9601(87)90681-5.

L. Diósi, *Models for universal reduction of macroscopic quantum fluctuations*, Physical Review A **40**, 1165–1174 (1989), doi:10.1103/PhysRevA.40.1165.

R. Penrose, *On gravity’s role in quantum state reduction*, General Relativity and Gravitation **28**, 581–600 (1996), doi:10.1007/BF02105068.

I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society **44**, 522–536 (1938), doi:10.2307/1989894.

S. Donadi, K. Piscicchia, C. Curceanu et al., *Underground test of gravity-related wave function collapse*, Nature Physics **17**, 74–78 (2021), doi:10.1038/s41567-020-1008-4.

</div>
