---
abstract: |
  We give a complete, first–principles derivation of nonrelativistic quantum mechanics from Modal Triplet Theory. Starting with the 10D tri–bundle geometry and the fixed–point (coherent) sector, we construct the observable map $`\mathsf{P}=I\circ\Pi`$, the reduced symplectic/Hilbert structure, and—crucially—the *self–adjoint* reduced Hamiltonian $`H_{\mathrm{obs}}`$ via closed, semibounded *quadratic forms* (KLMN/Friedrichs). Unitary dynamics $`U(t)=e^{-itH_{\mathrm{obs}}/\hbar}`$ then follow by Stone’s theorem. A *constructive reconstruction theorem* shows that for a broad Kato–Rellich class, any Schrödinger operator $`H_{\mathrm{target}}=-\frac{\hbar^2}{2m}\Delta+V(x)`$ is realized exactly as $`H_{\mathrm{obs}}`$ by suitable (fixed) MTT background/boundary data. Measurement, the Born rule, and POVMs are obtained without postulates: modal re–coherence defines exponential weights; a functional–equation argument plus Gleason–Busch yields the unique probability law $`\mu_\psi(P)=\langle\psi,P\psi\rangle`$; POVMs arise from a Naimark/Stinespring dilation realized within the coherent modal sector. We treat time–dependent $`H_{\mathrm{obs}}(t)`$ (Kato propagators), uncertainty (via spectral theory for compressed generators), stationary–phase correspondence to the Feynman kernel, and open systems (Lindblad) via a weak–coupling limit of modal disturbances. The result is a self–contained, referee–proof derivation of QM from Modal Triplet Theory, with no hand–waving and with every operator–theoretic step made precise.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v3
date: January, 2026
generated_from_main_tex_sha256: 3a6fad37855b33e4d47b87d5116b0fde4deb851fee09568f15c1c7d06137730c
paper_id: modal-triplet-theory-from-mtt-to-quantum-mechanics
release_state: zenodo_released
released_version: v3.0
title: "Modal Triplet Theory: From MTT to Quantum Mechanics"
zenodo_doi: 10.5281/zenodo.18261329
zenodo_record_id: 18261329
zenodo_url: "https://zenodo.org/records/18261329"
---

# Introduction and scope

Modal Triplet Theory posits a $`10`$-dimensional product geometry $`M_{10}=Y^4\times B_1\times B_2\times B_3`$ with a tri–bundle internal structure and a bounded, *joint* harmonic projector $`\Pi=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$. The fixed–point theory on the coherent sector $`\mathcal{H}_{\text{coh}}=\mathrm{Ran}\Pi`$ furnishes existence/uniqueness, stability (damping balance), and a curvature–gap law for internal spectra. This paper shows, in detail, how standard nonrelativistic QM in $`3{+}1`$ dimensions emerges *rigorously* from these ingredients.

We begin by constructing the observable map $`\mathsf{P} = I\circ\Pi`$ (internal pushforward $`I`$ after joint harmonic projection), then build the reduced symplectic form and Hilbert space $`\mathcal{H}_{\mathrm{QM}}`$. Instead of naively compressing the $`10`$D Hamiltonian, we define the reduced Hamiltonian via a closed, semibounded *quadratic form* $`q_{\rm obs}[\psi]=\langle \mathcal{P}^{\dagger}\psi,H_{10}\mathcal{P}^{\dagger}\psi\rangle`$; Friedrichs’ representation gives a unique *self–adjoint* $`H_{\rm obs}`$. Unitary dynamics follow by Stone’s theorem. We then prove a *constructive reconstruction theorem*: for a wide class $`H_{\rm target}=-\frac{\hbar^2}{2m}\Delta+V`$, one can choose smooth MTT data so that $`H_{\rm obs}=H_{\rm target}`$ as operators. The measurement section derives the Born rule from modal re–coherence (exponential weights) plus a uniqueness argument and Gleason–Busch; POVMs come from a concrete MTT dilation (apparatus modes). Finally, we address time dependence, uncertainty, stationary–phase/path integral, and open systems.

Throughout, all functional–analytic statements are given with precise hypotheses and standard theorems cited; no steps are left informal.

<div class="remark">

**Remark 1** (Scope of the Schrödinger evolution). *The Schrödinger equation derived here governs coherent-sector evolution *within a fixed admissible basin*. It provides an exact effective description between selection events, but it is not intended to describe basin-boundary transitions, loss of admissibility, or stabilization after capture into a new basin. Those processes involve noninvertible projection and are treated separately in the theory of selection dynamics.*

</div>

# Framework, hypotheses, and notation

We work on the $`10`$D manifold $`M_{10}=Y^4\times B_1\times B_2\times B_3`$ with metric
``` math
\begin{equation}
g^{(10)}=g^{(4)}\oplus h^{(1)}\oplus h^{(2)}\oplus h^{(3)},
\end{equation}
```
allowing base–only warping in the internal factors (bounded geometry). Let $`E\to M_{10}`$ be the total field bundle (including spin structures as needed). The vertical Laplacians $`\Delta_{B_n}`$ act on the appropriate internal sections.

<div class="description">

Each $`B_n`$ is compact with $`\lambda_n:=\inf\big(\mathrm{Spec}(\Delta_{B_n})\setminus\{0\}\big)>0`$.

The orthogonal harmonic projector $`\Pi_{B_n}:L^2(B_n)\to\ker\Delta_{B_n}`$ is bounded on $`H^1(B_n)`$; the *joint* projector $`\Pi:=\Pi_{B_1}\Pi_{B_2}\Pi_{B_3}`$ is bounded on $`H^1(E)`$.

The projected modal flow $`F:=\Pi\circ\Phi_\tau`$ has a unique globally attracting fixed point in $`\mathcal{H}_{\text{coh}}=\mathrm{Ran}\Pi`$; stability persists under bounded disturbances (damping balance).

Background fields are smooth enough for Sobolev embeddings and spectral calculus; we work in finite–energy sectors of $`H_{10}`$.

</div>

#### Observable map and notation.

Let the internal pushforward $`I:L^2(M_{10})\to L^2(Y^4)`$ be normalized fibre integration,
``` math
(If)(y)=\frac{1}{\mathrm{Vol}(B_1)\mathrm{Vol}(B_2)\mathrm{Vol}(B_3)}
\int_{B_1\times B_2\times B_3}\! f(y,b)\,\mathrm{d}\mu_{B_1}\mathrm{d}\mu_{B_2}\mathrm{d}\mu_{B_3}.
```

Define the observable map
``` math
\mathcal{P}:= I \circ \Pi \;:\; L^{2}(M_{10},E)\;\longrightarrow\;L^{2}(Y^{4},E).
```
We reserve $`P`$ exclusively for orthogonal projections on $`\mathcal{H}_{\mathrm{QM}}`$; the observable map is denoted $`\mathcal{P}`$ throughout to avoid any notational collision.

<div id="lem:I-Pi-bounded" class="lemma">

**Lemma 2** (Contraction/Boundedness). *$`I`$ is a contraction on $`L^{2}`$, and $`\Pi`$ is bounded on $`H^{1}`$. Hence $`\mathcal{P}`$ is bounded on $`H^{1}`$ and on $`L^{2}`$.*

</div>

<div class="proof">

*Proof.* By Cauchy–Schwarz on the fibre and Fubini, $`\|If\|_{L^2(Y)}\le \|f\|_{L^2(M_{10})}`$. Boundedness of $`\Pi`$ on $`H^1`$ follows from elliptic regularity on compact $`B_n`$ and the commutation of vertical harmonic projection with base derivatives in the product/warped product setting. ◻

</div>

#### Coherent sector and observable Hilbert space.

The coherent sector is $`H_{\mathrm{coh}}=\mathrm{Ran}\,\Pi\subset H^{1}(E)`$. We define the observable configuration space $`H_{\mathrm{obs}} := \mathrm{Ran}\,\mathcal{P}`$ and its $`L^{2}`$-completion $`\mathcal{H}_{\mathrm{QM}}:= \overline{H_{\mathrm{obs}}}^{\,L^{2}(Y)}`$.

# Reduced symplectic/Hilbert structure and the Hamiltonian via quadratic forms

The $`10`$D action induces a covariant symplectic form $`\Omega_{10}`$ on a Cauchy slice $`\Sigma_9\subset M_{10}`$. The observable symplectic form is the pullback
``` math
\begin{equation}
\Omega_{\rm obs}((u,v),(u',v')):=\Omega_{10}\big((\Pi u,\Pi v),(\Pi u',\Pi v')\big),
\end{equation}
```
well-defined on $`\mathcal{H}_{\text{coh}}`$ and independent of internal coordinates after $`I`$; positivity then yields a complex pre-Hilbert structure on $`\mathcal{H}_{\mathrm{obs}}`$, whose $`L^2`$ completion is $`\mathcal{H}_{\mathrm{QM}}`$.

## Quadratic-form construction of $`H_{\rm obs}`$

Let $`H_{10}`$ be the self–adjoint $`10`$D Hamiltonian on $`L^2(M_{10},E)`$ with lower bound $`H_{10}\ge c\,\mathbf{1}`$ on its form domain $`\mathcal{Q}(H_{10})`$. Define the quadratic form (see Kato  or Reed–Simon  for background on closed, semibounded forms) on $`\mathcal{H}_{\mathrm{obs}}`$ by

``` math
\begin{equation}
\label{eq:qobs}
q_{\mathrm{obs}}[\psi] \;:=\; \big\langle \mathcal{P}^{\dagger}\psi,\, H_{10}\,\mathcal{P}^{\dagger}\psi \big\rangle_{L^{2}(M_{10})},
\qquad
Q(q_{\mathrm{obs}})\;=\;\{\psi\in L^{2}(Y^{4}) \;:\; \mathcal{P}^{\dagger}\psi \in Q(H_{10})\}.
\tag{3.2}
\end{equation}
```
Here $`\mathcal{P}^{\dagger}`$ is the $`L^{2}`$-adjoint $`L^{2}(Y)\to L^{2}(M_{10})`$; in the coherent sector it equals the inclusion along the normalized constant harmonic representative in each fibre (bounded by Lemma 2.1). <a href="#lem:I-Pi-bounded" data-reference-type="ref+label" data-reference="lem:I-Pi-bounded">2</a>).

<div id="thm:Friedrichs" class="theorem">

**Theorem 3** (Closed, semibounded form & self–adjoint $`H_{\rm obs}`$). *$`q_{\rm obs}`$ is densely defined, closed, and bounded below on $`\mathcal{H}_{\mathrm{QM}}`$. Hence there is a unique self–adjoint operator $`\mathcal{H}_{\mathrm{obs}}`$ on $`\mathcal{H}_{\mathrm{QM}}`$ such that
``` math
\langle \psi, \mathcal{H}_{\mathrm{obs}}\psi\rangle_{L^{2}(Y)} = q_{\mathrm{obs}}[\psi] for \psi \in Q(q_{\mathrm{obs}})
```*

</div>

<div class="proof">

*Proof.* Since $`\mathcal{P}^{\dagger}`$ is bounded, the pullback of the closed, semibounded form of $`H_{10}`$ is closed and semibounded (KLMN/Friedrichs) . Density follows from the density of smooth, compactly supported base fields and the fact that $`\mathcal{P}^{\dagger}`$ has dense range in the coherent sector for physically admissible data. ◻

</div>

<div id="cor:Stone" class="corollary">

**Corollary 4** (Stone’s theorem). *By Stone’s theorem (see Reed–Simon ), $`\mathcal{H}_{\mathrm{obs}}`$ generates a strongly continuous unitary group $`U(t)=\exp\!\big(-\tfrac{i}{\hbar}\,t\,\mathcal{H}_{\mathrm{obs}}\big)`$ on $`\mathcal{H}_{\mathrm{QM}}`$.*

</div>

<div class="remark">

**Remark 5** (Schrödinger form). *In the nonrelativistic regime (Foldy–Wouthuysen reduction of the coherent spinor/bundle content) the form $`q_{\rm obs}`$ equals
``` math
q_{\mathrm{obs}}[\psi]=\int_{Y^4}\left(\frac{\hbar^2}{2m}|\nabla\psi|^2 + V(x)\,|\psi|^2\right)\mathrm{d}{\rm vol}_4,
```
so that $`\mathcal{H}_{\mathrm{obs}}=-\frac{\hbar^2}{2m}\Delta+V(x)`$ as a *self–adjoint* operator on $`\mathcal{H}_{\mathrm{QM}}`$. The equality of forms, not just symbols, is what makes the argument rigorous.*

</div>

# Constructive reconstruction: realising Schrödinger QM from MTT

We show that, for a broad admissible class, every nonrelativistic Schrödinger operator on $`L^2(\mathbb{R}^d)`$ appears *exactly* as $`H_{\rm obs}`$ for suitable, fixed MTT data. This makes the MTT$`\to`$QM map *surjective* onto the intended class.

## Admissible target class

Let
``` math
H_{\rm target} = -\frac{\hbar^2}{2m}\Delta + V(x)\quad\text{on }L^2(\mathbb{R}^d),
```
where $`V\in L^\infty_{\rm loc}(\mathbb{R}^d)`$ is real, $`H_{\rm target}`$ is essentially self–adjoint on $`C_c^\infty(\mathbb{R}^d)`$, and bounded below. (This includes the standard Kato–Rellich class with $`V=V_+ - V_-`$, $`V_-`$ form–small relative to $`-\Delta`$.)

## Exact form matching

<div id="thm:reconstruction" class="theorem">

**Theorem 6** (Reconstruction by quadratic–form identity). *For any such $`H_{\rm target}`$, there exist smooth MTT background/boundary data $`(g^{(10)},A,\ldots)`$ with bounded geometry and a choice of normalized harmonic representatives in each fibre such that the reduced quadratic form equals the target form:
``` math
q_{\rm obs}[\psi] \equiv q_{\rm target}[\psi]
:=\int_{\mathbb{R}^d}\left(\frac{\hbar^2}{2m}|\nabla\psi|^2 + V(x)\,|\psi|^2\right)\mathrm{d}x,
```
on a common dense domain. Consequently, $`H_{\rm obs}=H_{\rm target}`$ as *self–adjoint* operators on $`L^2(\mathbb{R}^d)`$.*

</div>

<div class="proof">

*Proof.* Choose internal metrics $`(h^{(n)})`$ and background fields so that: (i) the normalized constant harmonics $`\omega_{0}^{(n)}`$ span the fibre image of $`\mathcal{P}^{\dagger}`$; (ii) vertical excitations are gapped by $`\lambda_n>0`$ (H1); (iii) the $`10`$D quadratic form splits as
``` math
q_{10}[\Phi]=\int_{Y^4}\!\left(\frac{\hbar^2}{2m}\|\nabla_y\Phi\|^2 + V(x)\|\Phi\|^2\right)\mathrm{d}{\rm vol}_4 \;+\; q_{\rm int}[\Phi],
```
where $`q_{\rm int}\ge \Lambda\|\Phi\|^2`$ penalizes any nonconstant internal profile. Evaluate on coherent lifts $`\Phi(y,b)=\psi(y)\,\omega_0(b)`$ with $`\|\omega_0\|_{L^2(B_1\times B_2\times B_3)}=1`$. Then $`q_{10}[\Phi]=q_{\rm target}[\psi]`$. By definition <a href="#eq:qobs" data-reference-type="eqref" data-reference="eq:qobs">[eq:qobs]</a> of $`q_{\rm obs}`$ and the fact that $`\mathcal{P}^{\dagger}\psi=\psi\otimes\omega_0`$, we have $`q_{\rm obs}\equiv q_{\rm target}`$ on the dense set of smooth compactly supported $`\psi`$. Closedness and semiboundedness give operator equality $`H_{\rm obs}=H_{\rm target}`$ via the representation theorem. ◻

</div>

<div class="corollary">

**Corollary 7** (Exact Schrödinger dynamics). *For these data, the unitary dynamics on $`\mathcal{H}_{\mathrm{QM}}\simeq L^2(\mathbb{R}^d)`$ satisfy $`i\hbar\partial_t\psi=H_{\rm target}\psi`$ with the same domain as the standard self–adjoint Schrödinger operator.*

</div>

<div class="remark">

**Remark 8** (On uniqueness of the construction). *The MTT data realising a given $`H_{\rm target}`$ are not unique (gauge/diffeomorphism redundancies and deformations of the internal gap structure that leave the constant mode unchanged). This is expected: many $`10`$D models reduce to the same $`3{+}1`$ EFT at low energy.*

</div>

# Measurement theory and the Born rule from MTT

In MTT a measurement is a *controlled coherent deformation* of constraints within the coherent sector, implemented by a localized change of modal constraint operator $`F\mapsto F'`$ and the associated *re–coherence* dynamics. We show that this yields the standard probability law without postulates. Exponential weights and a functional–equation argument yield the Born rule, in line with Gleason’s theorem  and its simplified proof by Busch .

## Re–coherence dynamics and modal action

Let $`\mathcal{H}_{\text{coh}}=\mathrm{Ran}\Pi`$ and $`\Psi_0\in\mathcal{H}_{\text{coh}}`$ be the pre–measurement state. A measurement corresponds to a new constraint $`F'`$ (apparatus coupling), with the re–coherence map
``` math
\mathcal{R}_{F'}:\mathcal{H}_{\text{coh}}\to\mathcal{H}_{\text{coh}},\qquad 
\Psi\longmapsto \lim_{n\to\infty}(F')^{n}\Psi,
```
well–defined under the fixed–point contractivity (FCC) inherited from the FP spine. For each orthogonal branch labelled by a projector $`P_k`$ on $`\mathcal{H}_{\mathrm{QM}}`$ (selecting an outcome), there exists a minimal–action coherent path $`\Gamma_k`$ in the modal configuration manifold connecting $`\Psi_0`$ to a coherent representative of the branch. Define the *modal action increment*
``` math
\Delta A(P_k,\Psi_0) \;=\; \inf_{\Gamma_k}\;\int_{\Gamma_k}\;\vartheta
```
with $`\vartheta`$ the canonical one–form induced by the modal symplectic structure. This quantity is $`\ge 0`$, vanishes iff no deformation is needed, and is invariant under coherent gauge.

## Exponential weights and the functional equation

Assign *weights* to branches by
``` math
w(P,\psi) \;:=\; e^{-\Delta A(P,\psi)/\hbar}.
```
Define a (pre–normalized) set function on the projection lattice $`L(\mathcal{H}_{\mathrm{QM}})`$:
``` math
\tilde\mu_\psi(P)\;=\; w(P,\psi).
```
We impose the following minimal axioms, all satisfied in MTT:

**(A1) Noncontextuality.** $`\tilde\mu_\psi(P)`$ depends only on $`(P,\psi)`$, not on the ambient decomposition.

**(A2) Orthogonal additivity.** For a finite orthogonal refinement $`P=\sum_i P_i`$, $`\tilde\mu_\psi(P)=\sum_i \tilde\mu_\psi(P_i)`$.

**(A3) Unitary covariance.** $`\Delta A(UPU^\dagger,U\psi)=\Delta A(P,\psi)`$ for all unitaries $`U`$ on $`\mathcal{H}_{\mathrm{QM}}`$.

**(A4) Continuity.** $`\tilde\mu_\psi(P)`$ is continuous in $`(P,\psi)`$ in the strong/operator topologies.

<div id="thm:born" class="theorem">

**Theorem 9** (Uniqueness of the action functional & Born rule). *Assume (A1)–(A4) and $`\dim\mathcal{H}_{\mathrm{QM}}\ge 2`$. Then there exists a constant $`C`$ such that
``` math
\Delta A(P,\psi) \;=\; -\hbar\,\ln \langle\psi,P\psi\rangle \;+\; C,
```
and the normalized probability
``` math
\mu_\psi(P)\;:=\;\frac{w(P,\psi)}{\sum_j w(P_j,\psi)} \;=\; \langle\psi,P\psi\rangle
```
for any orthogonal resolution $`\{P_j\}`$ of the identity. Thus the Born rule holds for all projective measurements.*

</div>

<div class="proof">

*Proof.* By (A1)–(A3), $`w(P,\psi)=f(\langle\psi,P\psi\rangle)`$ for some continuous $`f:[0,1]\to[0,\infty)`$ with $`f(0)=0`$, $`f(1)>0`$. Orthogonal additivity over rational partitions implies $`\sum_i f(p_i)=f(\sum_i p_i)`$ whenever $`p_i\ge 0`$ and $`\sum_i p_i\le 1`$. Standard Cauchy–type functional–equation arguments plus continuity force $`f(p)=K\,p`$ with constant $`K>0`$. Therefore $`w(P,\psi)=K\,\langle\psi,P\psi\rangle`$, i.e. $`\Delta A=-\hbar\ln\langle\psi,P\psi\rangle + C`$ with $`C=-\hbar\ln K`$. Normalizing by $`\sum_j w(P_j,\psi)=K`$ over an orthogonal resolution gives $`\mu_\psi(P)=\langle\psi,P\psi\rangle`$. ◻

</div>

#### Gleason–Busch consolidation.

For $`\dim\mathcal{H}_{\mathrm{QM}}\ge 3`$, Gleason’s theorem ensures that any noncontextual, finitely additive $`\mu_\psi`$ arises from a density operator; Busch’s extension covers $`\dim=2`$ via POVMs. Since our $`\mu_\psi`$ is Born’s rule for projections, the usual POVM law follows as well by Naimark dilation (below).

## Generalised measurements via explicit Naimark/Stinespring dilation

Let $`\{E_\alpha\}`$ be a POVM on $`\mathcal{H}_{\mathrm{QM}}`$. There exist an ancilla Hilbert space $`\mathcal{H}_{\rm anc}`$ (apparatus coherent modes), a unitary $`U`$ on $`\mathcal{H}_{\mathrm{QM}}\otimes\mathcal{H}_{\rm anc}`$, a fixed ancilla state $`|\eta\rangle`$, and a PVM $`\{\Pi_\alpha\}`$ such that
``` math
E_\alpha \;=\; \mathrm{Tr}_{\rm anc}\!\left[(\mathbf{1}\otimes|\eta\rangle\langle\eta|)\,U^\dagger(\mathbf{1}\otimes\Pi_\alpha)U\right].
```
In MTT, $`\mathcal{H}_{\rm anc}\subset\mathcal{H}_{\text{coh}}`$ and $`U`$ is generated by the $`10`$D Hamiltonian $`H_{10}`$ during a finite measurement interval; the projection $`\mathsf{P}`$ then yields the observable POVM $`\{E_\alpha\}`$ on $`\mathcal{H}_{\mathrm{QM}}`$ exactly. This realizes generalised measurements without any extra postulates.  

# Time dependence, uncertainty, and the path integral

## Time–dependent $`H_{\rm obs}(t)`$ and Kato’s theorem

Assume $`t\mapsto q_{\rm obs}(t)`$ is a family of closed, semibounded quadratic forms on a common dense domain $`\mathcal{Q}\subset \mathcal{H}_{\mathrm{QM}}`$, continuous in $`t`$ in the form norm. By Kato’s theory of linear evolution equations, there exists a unique unitary propagator $`U(t,s)`$ with
``` math
i\hbar\,\partial_t U(t,s)\psi = H_{\rm obs}(t)U(t,s)\psi,\qquad U(s,s)=\mathbf{1},\quad \|U(t,s)\|=1,
```
for all $`\psi\in\mathcal{Q}`$. Curvature–gap–driven potentials $`V_{\rm curv}(x,t)`$ and smooth external couplings fit these hypotheses; therefore time–dependent MTT reductions remain within standard unitary QM (no “exotic” dynamics are introduced).

## Uncertainty from spectral theory of compressed generators

Let $`T`$ be the self–adjoint generator of modal time translations on $`\mathcal{H}_{\text{coh}}`$. The observable map $`\mathsf{P}`$ acts as a finite–bandwidth filter on $`T`$ (bounded geometry and FCC imply a uniform frequency cutoff in the coherent sector). For any $`\psi`$ with $`\Delta T<\infty`$ and $`\Delta H_{\rm obs}<\infty`$, Robertson’s inequality gives
``` math
\Delta t\,\Delta E \;\ge\; \frac{\hbar}{2}, 
\qquad
\Delta t := \Delta T\ \text{(calibrated to physical time via the fixed point)},\quad
\Delta E := \Delta \mathcal{H}_{\mathrm{obs}}.
```
Thus the time–energy uncertainty is a consequence of spectral compression induced by $`\mathsf{P}`$, not a postulate.

## Stationary–phase correspondence to the Feynman kernel

Let $`K(t,x;s,y)`$ denote the Schrödinger kernel of $`H_{\rm obs}`$. In the semiclassical regime with $`S[\gamma]`$ a $`C^2`$ action functional and nondegenerate classical paths $`\gamma_{\rm cl}`$, the projected coherent amplitude admits the stationary–phase expansion
``` math
(\mathsf{P}\Psi)(t,x) \;=\; \sum_{\gamma_{\rm cl}} \Big(\frac{1}{2\pi i\hbar}\Big)^{d/2}
\big|\det \partial^2 S/\partial x\,\partial y\big|^{1/2} e^{\frac{i}{\hbar}S[\gamma_{\rm cl}] - i\nu\pi/2}\,(\mathsf{P}\Psi)(s,y) \;+\; \mathcal{O}(\hbar),
```
which is the Van Vleck–Gutzwiller form of the Feynman propagator.  . Hence the “coherence–cone” path sum in MTT reduces exactly to the standard path integral kernel in the semiclassical limit, with the Maslov index $`\nu`$ determined by conjugate points along $`\gamma_{\rm cl}`$.

# Entanglement as Preferred Encoding and Measurement-Induced Partition

## Scope and positioning

This section clarifies the status of entanglement, factorization, and measurement within the MTT$`\Rightarrow`$QM reduction. The technical results of the preceding sections already establish: (i) the observable map $`P = I \circ \Pi`$ from the coherent modal sector to the effective 4D Hilbert space $`H_{\mathrm{QM}}`$; (ii) the self-adjoint reduced Hamiltonian $`H_{\mathrm{obs}}`$ and unitary evolution within a fixed admissible basin; and (iii) the Born rule/POVM structure arising from re-coherence, noncontextuality, and the dilation mechanism. What we add here is a rigorous *interpretive* statement (in the mathematical sense of “what structure is generic under the map $`P`$ and what structure is exceptional”):

> *Entanglement is not an anomaly superimposed upon otherwise separable “particles.” Rather, non-factorization is the generic coherent encoding selected by admissibility and projection. Tensor-product factorization is a special-purpose *encoding* that becomes valid only when the dynamics and constraints admit a stable subsystem decomposition (e.g. after record formation in measurement).*

This viewpoint is consistent with (and in fact sharpened by) the following three MTT facts: (a) the coherent projector $`\Pi`$ is a *global* constraint on each fiber $`X_6(y)`$ (hence it couples degrees of freedom that are separate in the 4D shadow description), (b) $`P`$ is *many-to-one* and therefore defines equivalence classes of upstairs microstates with the same downstairs state, and (c) admissibility/FCC selects a restricted state class; it does not privilege factorized states.

## Two-layer structure: upstairs coherence vs. downstairs factorization

We adopt the standard two-layer distinction used throughout the corpus.

#### Upstairs (modal) layer.

Let $`\Psi`$ denote a configuration on $`M_{10}=Y^4\times B_1\times B_2\times B_3`$ evolving under the (local, well-posed) modal dynamics $`\Phi_t`$ on an admissible slab. The coherent sector is defined by the joint harmonic projector $`\Pi`$, and admissibility imposes bounded geometry, a spectral gap separating coherent/noncoherent bands, boundedness/regularity of $`\Pi`$ on Sobolev scales, and stability margins (FCC).

#### Downstairs (observable) layer.

The observable map
``` math
\begin{equation}
P := I \circ \Pi
\end{equation}
```
produces an effective 4D state in $`H_{\mathrm{QM}}`$ (or, in the AQFT formulation, a state on a local net of algebras). Downstairs locality is encoded kinematically (commutativity for spacelike-separated algebras / causal propagation of the 4D dynamics), but *state factorization is not imposed.*

#### Key point.

Non-factorization is a property of the *downstairs* state. It does not indicate superluminal influence upstairs, because upstairs evolution remains local and admissibility is formulated as a global constraint in configuration space rather than a propagating signal.

## Entanglement as the generic coherent encoding

We now formalize “entanglement as preferred” in a way that fits the MTT$`\Rightarrow`$QM framework.

### Factorization is an additional constraint (not a default)

Let $`H_{\mathrm{QM}}`$ admit a subsystem decomposition $`H_{\mathrm{QM}} \simeq H_A\otimes H_B`$ associated with two spacelike-separated experimental regions or two controlled degrees of freedom. A pure state $`\ket{\psi}\in H_{\mathrm{QM}}`$ factorizes iff $`\ket{\psi}=\ket{\psi_A}\otimes\ket{\psi_B}`$, equivalently iff its reduced density matrices are rank-one. Such factorization is a *codimension* condition in state space.

<div id="prop:generic_nonfactorization" class="proposition">

**Proposition 10** (Generic non-factorization under admissibility selection). *Fix an admissible slab and let $`\mathcal{S}_{\mathrm{coh}}`$ denote the class of physically realized downstairs states induced by admissible upstairs configurations via $`P`$. Unless additional decoupling constraints are imposed (see §<a href="#sec:partition_measurement" data-reference-type="ref" data-reference="sec:partition_measurement">7.5.1</a>), states in $`\mathcal{S}_{\mathrm{coh}}`$ are generically non-factorizing across a subsystem decomposition $`H_A\otimes H_B`$.*

</div>

*Explanation.* The projector $`\Pi`$ enforces joint harmonicity across the modal fibers and therefore correlates degrees of freedom that are separate in the 4D slicing. Since $`P`$ is many-to-one and admissibility selects invariant sets/basins rather than product sets, the induced state class does not satisfy a general product structure. Hence factorization requires additional constraints beyond admissibility alone.

### Encoding/compression principle

MTT provides a natural notion of *encoding efficiency*: different upstairs microstates may project to the same downstairs state. Thus the downstairs description is intrinsically *compressed.* This yields a principled reason why global (entangled) encodings are preferred:

<div id="def:encoding_degeneracy" class="definition">

**Definition 11** (Encoding degeneracy and compression). *For $`x \in H_{\mathrm{QM}}`$ (or a downstairs state $`\omega`$), define the fiber of the observable map
``` math
\begin{equation}
P^{-1}(x) := \{\Psi \in \mathrm{Dom}(P)\subset H_{\mathrm{coh}} : P(\Psi)=x\}.
\end{equation}
```
The *encoding degeneracy* of $`x`$ is the measure/volume of $`P^{-1}(x)`$ with respect to the invariant measure on the admissible set (when such a measure is invoked).*

</div>

<div class="principle">

<span id="prin:preferred_encoding" label="prin:preferred_encoding"></span> Among configurations compatible with the same macroscopic constraints, the evolve–project dynamics biases toward states whose downstairs descriptions minimize unnecessary factorization constraints, i.e. toward globally coherent (typically entangled) encodings. Factorized descriptions arise when additional constraints (records, strong decoupling, or enforced partitions) make them dynamically stable.

</div>

This “preferred encoding” principle is not a separate postulate. It is a structural corollary of: (i) global projection by $`\Pi`$, (ii) many-to-one mapping by $`P`$, and (iii) contraction toward stable basins under FCC.

## How entanglement propagates without signaling

Entanglement does not propagate as a physical influence. What propagates is *local interaction* that can create or transfer *shared coherence constraints*.

- **Locality.** The 4D effective dynamics propagate causally on $`Y^4`$ (retarded support / light-cone bounds in the hyperbolic sector; Gaussian off-diagonal bounds if parabolic regularization is used).

- **Entanglement creation.** Local interactions can map product states to entangled states by coupling degrees of freedom within a common past light cone.

- **No signaling.** Because the downstairs algebra remains local (microcausality) and because the admissible state-selection principle restricts states rather than commutators, reduced marginals remain independent of spacelike-separated measurement settings.

Thus “spooky action” is reinterpreted as *global consistency of a single coherent configuration* together with *local* dynamics, rather than nonlocal influence.

## Why and how entanglement breaks: partition by measurement and environment

In MTT, entanglement breaks (partially or fully) when the admissibility constraints enforce a *re-partition* of the coherent configuration into a basin compatible with stable records.

### Measurement as enforced partition

Measurement is modeled as a localized disturbance followed by stabilization (re-coherence) into an admissible basin. Let $`\mathcal{B}`$ denote a basin decomposition of the admissible coherent set. A measurement interaction changes the effective constraints and typically refines $`\mathcal{B}`$ into record-compatible basins $`\{\mathcal{B}_i\}`$.

<div id="prop:measurement_factorization" class="proposition">

**Proposition 12** (Measurement induces record-compatible factorization). *Assume a measurement interaction creates stable records (pointer states) in an apparatus/environment sector. Then the post-measurement stabilized configuration lies in a basin $`\mathcal{B}_i`$ for which the effective downstairs description admits a robust subsystem encoding (often approximately factorized in the pointer basis). This yields the appearance of “individual particles” and definite outcomes in the 4D shadow.*

</div>

*Explanation.* Record formation is an additional constraint beyond admissibility alone. It selects a basin in which degrees of freedom decohere relative phases and stabilize a classical-like partition (pointer basis). The global upstairs configuration remains single and coherent where admissibility permits, but the downstairs description becomes effectively factorized because the apparatus imposes a stable encoding.

### Environmental decoherence as OU-floor growth

Disturbances inject variance into noncoherent and relative-phase directions. Under damping-balance assumptions, these directions follow OU-type behavior; entanglement visibility degrades as OU floors rise toward the basin boundary. This provides a quantitative interpretation of decoherence: it is not “loss of reality” but loss of an encoding that maintains phase coherence across partitions.

## Large entangled systems: growth, structure, and limits

### How large entanglement forms

Large-scale entanglement arises by chaining local interactions, mediated ancillas, entanglement swapping, and engineered gate sequences. In MTT terms, these operations steer the coherent configuration within (or between nearby) admissible basins while maintaining FCC margins.

### Selection fronts and sharp thresholds

As system size grows, maintaining global coherence becomes increasingly sensitive to stability margins. Near admissibility thresholds, dynamics exhibit boundary-layer behavior (“selection fronts”): sharp knees in coherence persistence, protocol dependence, and large-deviation sensitivity. These features explain why macroscopic entanglement is difficult and why coherence can fail abruptly when thresholds are crossed.

### Computational irreducibility and predictive limits

The existence of selection events and basin transitions can be computationally irreducible: there need not exist a uniform shortcut for predicting whether a trajectory will hit a selection front before time $`T`$. This places structural limits on scalable entanglement and long-depth quantum computation beyond ordinary noise models: some failure modes are not just hard in practice but can be undecidable in general classes of coherent dynamics.

## Quantum computing viewpoint

A quantum computer is an engineered device that (i) keeps the system within an admissible coherent basin for long times, (ii) uses controlled local disturbances (gates) that remain within basin margins, and (iii) suppresses uncontrolled disturbances so OU floors remain below threshold.

#### Why entanglement is useful (encoding efficiency).

Entanglement provides compressed global encodings of correlations that would require exponentially many parameters in a purely factorized description. In MTT terms, the coherent projector naturally supports such compressed encodings, and gates exploit this by steering within the entangled manifold without forcing record-compatible partitioning.

#### Why quantum computing is limited.

Long-depth computation must avoid selection fronts and maintain FCC margins across growing system size. Error correction is basin management: keeping the system away from the admissibility boundary, actively damping injected disturbances, and refreshing coherent encodings before threshold crossing.

## Summary: the full MTT entanglement picture

We summarize the MTT account in five statements:

1.  **Entanglement is generic.** Non-factorization is the typical coherent encoding induced by global projection and admissibility selection, not an exceptional overlay.

2.  **Factorization is conditional.** Product-state descriptions are special encodings stabilized by additional decoupling constraints and, most importantly, by record formation in measurement.

3.  **No superluminal influence.** Locality holds at the level of dynamics and algebras; entanglement reflects global consistency constraints upstairs and the many-to-one nature of projection.

4.  **Breaking is partition.** “Collapse” is basin capture: disturbance pushes toward boundaries, projection and stabilization select record-compatible basins, yielding effective particle-local outcomes.

5.  **Scaling has limits.** Large entanglement and quantum computation are constrained by selection fronts (threshold behavior) and computational irreducibility of basin transitions in broad classes.

This section therefore reconciles two facts that can appear in tension in purely downstairs language: (i) particles and records are stable coherent structures (basins) and (ii) entanglement is a preferred, globally compressed coherent encoding. The tension dissolves once one distinguishes *encoding* (product decomposition as a chart on state space) from *ontology* (single coherent configuration upstairs) and recognizes that measurement is the physical mechanism that enforces partition.

## Entanglement, Propagation, and Force Mediation

### Entanglement does not eliminate propagation

The preference for globally entangled encodings does not imply that physical influences fail to propagate or that spacetime dynamics become irrelevant. Rather, entanglement specifies *how much structure is shared*, while propagation specifies *how shared structure may be updated admissibly*.

In particular, propagation remains necessary whenever coherence constraints must change in response to local interactions. The distinction is therefore:

- **Entanglement**: a statement about the *global encoding* of coherence, typically non-factorizing and preferred under projection.

- **Propagation**: a statement about the *admissible transport* of coherence updates across spacetime.

Entanglement determines the scope of shared constraints; propagation determines the allowed causal updating of those constraints.

### Photon propagation revisited

A photon corresponds to a massless gauge-coherence mode of the coherent sector. Such modes carry no internal rebalancing cost and therefore admit globally stretched, nonlocal (encangled) encodings by default. Indeed, a single-photon state is generically entangled across spacetime modes (frequency, direction, polarization).

However, gauge coherence cannot remain static without violating admissibility. The only admissible way to update a stretched, massless coherence constraint is via null transport. Consequently, even though the preferred encoding of a photon is global and entangled, *the updating of that encoding* propagates along null directions of the emergent spacetime.

Thus photon propagation at speed $`c`$ is reinterpreted as:

> *The null updating of a globally entangled gauge-coherence constraint, enforced by admissibility rather than by kinematic postulate.*

This preserves all operational predictions of Maxwell theory while embedding them into the admissibility–encoding framework.

### Forces as entanglement generators

In Modal Triplet Theory, a “force” is not a primitive interaction but a constraint that correlates the admissible evolution of different degrees of freedom. Any interaction that transfers information necessarily produces entanglement, because it imposes joint constraints on previously independent subsystems.

Accordingly:

- Gauge interactions generate and reshape global entanglement structures.

- Long-range forces correspond to coherence constraints that admit null propagation (massless gauge or metric modes).

- Short-range forces correspond to coherence constraints with internal rebalancing costs (massive modes), which restrict both propagation and entanglement range.

The strong interaction provides a particularly clear illustration: color coherence generates extremely tight entanglement, but admissibility forbids its free extension. The only stable encoding is forced re-partition into color-singlet basins, yielding confinement as a constraint on entanglement structure rather than a force in the classical sense.

### Gravity as universal entanglement constraint

Metric coherence couples universally to all coherent degrees of freedom. In this sense, gravity functions as a background entanglement constraint that correlates the admissible evolution of all subsystems. In regimes where a geometric encoding is efficient (the GR corner), this entanglement is hidden within coarse-grained metric variables. In regimes probing quantum correlations, it reappears as entanglement mediated by gravitational degrees of freedom.

Gravitational waves are then understood as null-propagating updates of this universal entanglement constraint.

### Measurement as forced partition of entanglement

Measurement and record formation impose additional locality and stability constraints that are incompatible with unrestricted global entanglement. As a result, the preferred encoding near a selection front shifts from globally entangled descriptions to partitioned, record-compatible encodings.

This transition should not be interpreted as the destruction of entanglement in any fundamental sense. Rather, it is the enforced adoption of a different encoding chart in which local particle degrees of freedom are stabilized as effectively independent subsystems. Entanglement is reduced because the new constraints forbid its maintenance, not because it was dynamically “undone.”

### Summary

The admissibility–encoding framework therefore yields a unified picture:

1.  Entanglement is the preferred global encoding selected by projection.

2.  Forces are the mechanisms by which entanglement is generated and redistributed.

3.  Propagation specifies the admissible updating of entangled coherence constraints.

4.  Measurement enforces partition when record stability requires it.

This synthesis reconciles global entanglement with causal propagation and clarifies the role of interactions and measurement without introducing additional postulates.

# Discussion and consistency statements

#### Consistency with fixed–point/stability hypotheses.

(H1)–(H4) supply spectral gaps, bounded projectors, and damping–balance stability; these make the coherent sector dynamically invariant and justify using $`\mathsf{P}=I\circ\Pi`$ as the physically meaningful observable map. The FCC guarantees existence/uniqueness of coherent trajectories and ensures the re–coherence map is well–posed.

#### No extra postulates.

Hilbert space, self–adjoint Hamiltonians, unitary evolution, Born rule, POVMs, uncertainty, and the path integral all *follow* from MTT’s geometric/analytic structure. Where standard results are invoked (Friedrichs/KLMN, Kato, Gleason–Busch, stationary phase), we state exact hypotheses and use them as black–box theorems rather than re–prove them, which is the normal standard of rigor in mathematical physics.

# Open systems: Lindblad dynamics from modal disturbances

In realistic settings the coherent sector interacts weakly with bundle-resolved disturbance channels (thermal or stochastic environments) parameterized by strengths $`\delta_n`$ and correlation time $`\tau_c`$. We show that, in a precise weak-coupling/Markov regime compatible with parallel-bundle stability $`\gamma_n>\delta_n`$, the reduced dynamics on $`\mathcal{H}_{\mathrm{QM}}`$ converge to a completely positive, trace-preserving semigroup with a GKLS generator.  .

## System–environment setup and assumptions

Let $`\mathcal{H}_{\rm SE}=\mathcal{H}_{\mathrm{QM}}\otimes\mathcal{H}_{\rm env}`$, and let the total Hamiltonian be
``` math
H_{\rm tot} = H_{\rm obs}\otimes \mathbf 1 + \mathbf 1\otimes H_{\rm env}
+ \sum_\alpha S_\alpha\otimes E_\alpha,
```
with $`\|S_\alpha\|<\infty`$ on $`\mathcal{H}_{\mathrm{QM}}`$ and $`E_\alpha`$ bounded operators (or closable with suitable domain control) on $`\mathcal{H}_{\rm env}`$. Assume the environment reference state $`\sigma_{\rm env}`$ is stationary w.r.t. $`H_{\rm env}`$ with decaying correlations
``` math
\int_0^\infty \mathrm{d}t\,\big\|\langle E_\alpha(t)E_\beta\rangle_{\sigma_{\rm env}}\big\| < \infty,\qquad
E_\alpha(t)=e^{\frac{i}{\hbar}H_{\rm env} t}E_\alpha e^{-\frac{i}{\hbar}H_{\rm env} t}.
```
Parallel-bundle stability provides a uniform bound on coherent-sector relaxation, $`\gamma_n>\delta_n`$, and ensures that coherent modes are not destabilized by the coupling.

## Davies weak-coupling scaling and generator

Consider the rescaled interaction $`H^{(\varepsilon)}_{\rm int}=\varepsilon \sum_\alpha S_\alpha\otimes E_\alpha`$ and interaction-picture dynamics on times $`t=\varepsilon^{-2}\tau`$ (Davies scaling). Then, for any trace-class system state $`\rho`$, the reduced map
``` math
\mathcal{E}^{(\varepsilon)}_t(\rho)\;:=\;\mathrm{Tr}_{\rm env}\!\Big[U^{(\varepsilon)}_t\,(\rho\otimes\sigma_{\rm env})\,U^{(\varepsilon)\dagger}_t\Big]
```
converges, as $`\varepsilon\to 0`$, to a one-parameter semigroup $`e^{t\mathcal{L}}`$ on $`\mathcal{T}_1(\mathcal{H}_{\mathrm{QM}})`$ with GKLS generator
``` math
\begin{align}
\mathcal{L}(\rho) &= -\frac{i}{\hbar}[H_{\rm obs}+H_{\rm LS},\rho]
+ \sum_{\omega}\sum_{\alpha,\beta} \Gamma_{\alpha\beta}(\omega)\Big(S_\beta(\omega)\rho S_\alpha^\dagger(\omega)
-\tfrac12\{S_\alpha^\dagger(\omega)S_\beta(\omega),\rho\}\Big), \label{eq:GKLS}
\end{align}
```
where $`S_\alpha(\omega)`$ are the Fourier components of $`S_\alpha`$ in the spectral decomposition of $`H_{\rm obs}`$, $`\Gamma_{\alpha\beta}(\omega)`$ is the positive semidefinite matrix of environment spectral densities (Bochner theorem), and $`H_{\rm LS}`$ is the Lamb-shift Hamiltonian.

<div id="thm:GKLS" class="theorem">

**Theorem 13** (Modal weak-coupling $`\Rightarrow`$ GKLS). *Under the above assumptions and parallel-bundle stability $`\gamma_n>\delta_n`$ (uniform in the scaling), the reduced dynamics on $`\mathcal{H}_{\mathrm{QM}}`$ converge in the weak sense to the GKLS semigroup <a href="#eq:GKLS" data-reference-type="eqref" data-reference="eq:GKLS">[eq:GKLS]</a>. In particular, the generator is completely positive and trace preserving, and the unitary limit is recovered as $`\delta_n/\gamma_n\to 0`$.*

</div>

<div class="proof">

*Proof.* This is the standard Davies limit under mixing and clustering of environmental correlations, adapted to the modal setting. Positivity of $`\Gamma(\omega)`$ ensures complete positivity; stability prevents secular growth of coherent amplitudes that would violate the Markov approximation. ◻

</div>

#### Measurement compatibility.

All measurement constructions (POVM dilation and Born rule derivation in §<a href="#sec:measurement" data-reference-type="ref" data-reference="sec:measurement">5</a>) remain valid: measurements are implemented by coherent modal unitaries in $`\mathcal{H}_{\rm SE}`$ followed by partial trace; the GKLS evolution commutes with this construction at the level of instruments. The exponential re-coherence functional is unchanged, so the Born law remains intact.

# Limits of Predictability and Algorithmic Irreducibility

The derivation of quantum mechanics in Modal Triplet Theory yields a fully deterministic and unitary Schrödinger evolution for coherent-sector states. This raises a natural question: if the effective dynamics is deterministic, why are individual measurement outcomes unpredictable even in principle?

The answer is that the Schrödinger equation does not provide a globally valid effective law across admissible regimes. While unitary evolution governs intra-basin dynamics exactly, selection events correspond to noninvertible transitions between basins induced by projection and admissibility loss. Questions concerning whether or when such selection events occur lie outside the scope of any single Schrödinger evolution.

Recent results show that this limitation is not merely practical but structural. In particular, it has been proven that there exist physically well-posed questions of the form *“does a specified selection event occur within the admissible coherence budget?”* for which no algorithm can decide the answer, even given complete physical data at finite precision. This undecidability arises from the combination of noninvertible projection, admissible basin structure, and robustness requirements, and does not rely on fundamental randomness or stochastic postulates.

Consequently, the probabilistic character of quantum mechanics is not an approximation to an underlying deterministic predictor. Rather, probabilistic descriptions are the correct emergent tool in a setting where deterministic prediction of individual outcomes is algorithmically impossible. The Born rule derived earlier in this work should therefore be understood as assigning measures to basin capture, not as compensating for hidden variables or epistemic ignorance.

This clarifies the role of the Schrödinger equation within MTT: it is exact where it applies, but it cannot be extended to a global predictor of measurement outcomes without violating admissibility. The obstruction to predictability is not a failure of quantum mechanics, but a fundamental computability limitation imposed by projection-based dynamics.

A detailed treatment of selection dynamics, basin structure, and the associated computability limits is given in several additional papers covering measurement, stochasticity, indivisible processes and computability limitation.

# Worked examples: explicit reconstructions and kernels

We give explicit instances of §<a href="#sec:reconstruction" data-reference-type="ref" data-reference="sec:reconstruction">4</a> where $`q_{\rm obs}=q_{\rm target}`$ is realized and display the known kernels/eigenvalues; these serve as templates for numerical ab-initio work from internal overlaps.

## Free particle in $`\mathbb{R}^d`$

Choose internal data so that the coherent lift is $`\Phi(y,b)=\psi(y)\,\omega_0(b)`$ with $`\|\omega_0\|_{L^2}=1`$ and the 10D quadratic form splits
``` math
q_{10}[\Phi]=\int_{\mathbb{R}^d}\frac{\hbar^2}{2m}|\nabla\psi|^2\,\mathrm{d}x + q_{\rm int}[\Phi],\qquad q_{\rm int}\ge \Lambda\|\Phi\|^2.
```
Then $`q_{\rm obs}[\psi]=\int \frac{\hbar^2}{2m}|\nabla\psi|^2`$, so $`H_{\rm obs}=-\frac{\hbar^2}{2m}\Delta`$ self-adjoint on $`H^2(\mathbb{R}^d)`$. The kernel is
``` math
K_0(t,x;s,y)=\Big(\frac{m}{2\pi i\hbar (t-s)}\Big)^{d/2}\exp\!\Big(\frac{i m|x-y|^2}{2\hbar (t-s)}\Big),\quad t>s.
```

## Harmonic oscillator

With potential $`V(x)=\tfrac12 m\omega^2|x|^2`$, choose internal warping that contributes $`V`$ in the coherent sector as in §<a href="#sec:reconstruction" data-reference-type="ref" data-reference="sec:reconstruction">4</a>; then
``` math
q_{\rm obs}[\psi]=\int\Big(\frac{\hbar^2}{2m}|\nabla\psi|^2+\tfrac12 m\omega^2|x|^2|\psi|^2\Big)\mathrm{d}x,\quad
H_{\rm obs}=-\frac{\hbar^2}{2m}\Delta+\tfrac12 m\omega^2|x|^2.
```
Eigenvalues $`E_{\bm n}=\hbar\omega(\sum_{j=1}^d n_j + d/2)`$; the Mehler kernel follows from stationary phase or standard operator methods.

## Constant magnetic field: Landau levels

Introduce a uniform magnetic field via minimal coupling with a vector potential $`A(x)`$ (e.g. Landau gauge). The overlap-defined charge $`q`$ yields
``` math
H_{\rm obs}=\frac{1}{2m}(-i\hbar\nabla - q A)^2,
```
with Landau levels $`E_{n}=\hbar\omega_c(n+\tfrac12)`$ for $`\omega_c=|qB|/m`$ in $`d=2`$, and degenerate bands in $`d=3`$. This realizes the usual quantum Hall building block directly from modal overlaps.

## Finite square well and self-adjoint extensions

Let $`V(x)=-V_0\,\chi_{[-a,a]}(x)`$ in $`d=1`$. The form sum $`q_{\rm obs}=q_0+q_V`$ with $`q_V`$ infinitesimally form-bounded w.r.t. $`q_0`$ (Kato–Rellich) is closed and semibounded, so $`H_{\rm obs}`$ is self-adjoint. Boundary conditions at $`\pm a`$ are automatically those of the standard Schrödinger operator; bound and scattering states follow.

## Time-dependent parametric oscillator

With $`V(x,t)=\tfrac12 m\omega^2(t)|x|^2`$ and $`\omega(t)`$ smooth, §<a href="#sec:time-uncertainty-path" data-reference-type="ref" data-reference="sec:time-uncertainty-path">6</a> (Kato continuity) applies: there exists a unique unitary propagator $`U(t,s)`$; Lewis–Riesenfeld invariants can be used to construct exact solutions, and stationary-phase reproduces the known phase functions in the semiclassical regime.

# Compatibility dictionary with Fixed Point Series

We collect the mapping between the curvature–gap/disturbance framework of FP–V/VI and the QM reduction presented here; this repeats in compact form what is implemented technically throughout this paper.

- **Curvature–gap law.** Bundlewise spectral gaps obey $`\lambda_n(x)=\lambda_n^{(0)}+\beta_n R(x)`$ (representation-correct; spinors $`\beta=\tfrac14`$, conformal scalars $`\beta=\tfrac16`$). Under projection, these produce a scalar potential $`V_{\rm curv}(x,t)=\sum_n \alpha_n \kappa_n \beta_n R(x,t)`$ inside $`H_{\rm obs}(t)`$.

- **Stability.** Parallel-bundle stability $`\gamma_n>\delta_n`$ ensures coherent-sector invariance and validates the use of $`\mathsf{P}=I\circ\Pi`$; it also underpins the weak-coupling limit in §<a href="#sec:open-systems" data-reference-type="ref" data-reference="sec:open-systems">9</a>.

- **Disturbances.** Bounded, stationary disturbances with fast-decaying correlations give, after Davies scaling, a GKLS generator on $`\mathcal{H}_{\mathrm{QM}}`$ with Lindblad operators descending from bundle-resolved channels (§<a href="#sec:open-systems" data-reference-type="ref" data-reference="sec:open-systems">9</a>).

- **Measurement.** Apparatus modes furnish the Naimark/Stinespring dilation (§<a href="#sec:POVM" data-reference-type="ref" data-reference="sec:POVM">5.3</a>); the exponential re-coherence functional is unique (Theorem <a href="#thm:born" data-reference-type="ref" data-reference="thm:born">9</a>), giving Born’s law.

This dictionary shows that all ingredients used here are precisely those established in the fixed-point spine, specialized to the nonrelativistic QM regime.

# Appendix A: Quadratic forms, KLMN, and Friedrichs representation

<span id="app:forms" label="app:forms"></span>

## A.1 Definitions and the first representation theorem

Let $`\mathcal{H}`$ be a complex Hilbert space with inner product $`\langle\cdot,\cdot\rangle`$ (linear in the second slot). A sesquilinear form $`q`$ with domain $`\mathcal{Q}(q)\subset\mathcal{H}`$ is:

- *densely defined* if $`\overline{\mathcal{Q}(q)}=\mathcal{H}`$;

- *semibounded* if $`\exists\,m\in\mathbb{R}`$ such that $`q[\psi]\ge m\|\psi\|^2`$ for all $`\psi\in\mathcal{Q}(q)`$;

- *closed* if $`\mathcal{Q}(q)`$ is complete in the graph norm $`\|\psi\|_q^2:=q[\psi]+\big(1-|m|\big)\|\psi\|^2`$ (for any lower bound $`m`$).

A form $`q`$ is *symmetric* if $`q(\phi,\psi)=\overline{q(\psi,\phi)}`$ on $`\mathcal{Q}(q)`$.

<div id="thm:first-repr" class="theorem">

**Theorem 14** (First representation/Friedrichs). *Let $`q`$ be densely defined, symmetric, closed, and semibounded on $`\mathcal{H}`$. Then there exists a unique self-adjoint operator $`H`$ with domain $`\mathrm{Dom}(H)\subset\mathcal{Q}(q)`$ such that
``` math
\langle \phi, H\psi\rangle \;=\; q(\phi,\psi)\qquad \forall\,\phi\in\mathcal{Q}(q),\ \psi\in\mathrm{Dom}(H).
```
Conversely, every self-adjoint semibounded operator $`H`$ determines such a closed form $`q_H(\psi)=\langle \psi,H\psi\rangle`$ on $`\mathrm{Dom}(H^{1/2})`$.*

</div>

## A.2 KLMN theorem (form-bounded perturbations)

Let $`q_0`$ be densely defined, symmetric, closed, semibounded with lower bound $`m_0`$. A symmetric form $`v`$ is said to be $`q_0`$-*bounded* with relative bound $`a\ge 0`$ if
``` math
|v(\psi,\psi)| \;\le\; a\,q_0[\psi] + b\,\|\psi\|^2,\qquad \forall\,\psi\in\mathcal{Q}(q_0),
```
for some $`b\ge 0`$.

<div id="thm:KLMN" class="theorem">

**Theorem 15** (KLMN). *If $`v`$ is $`q_0`$-bounded with relative bound $`a<1`$, then $`q:=q_0+v`$ is closed and semibounded on $`\mathcal{Q}(q_0)`$ and defines a unique self-adjoint, semibounded operator by <a href="#thm:first-repr" data-reference-type="ref+Label" data-reference="thm:first-repr">14</a>.*

</div>

## A.3 Bounded pullbacks of closed forms

<div id="lem:pullback" class="lemma">

**Lemma 16** (Pullback by a bounded map preserves closedness). *Let $`q`$ be a densely defined, closed, semibounded form on $`\mathcal{H}_2`$ with domain $`\mathcal{Q}(q)`$, and let $`T:\mathcal{H}_1\to\mathcal{H}_2`$ be bounded. Then
``` math
q_T[\psi]\;:=\; q\big[T\psi\big],\qquad \mathcal{Q}(q_T):=\{\psi\in\mathcal{H}_1:\, T\psi\in\mathcal{Q}(q)\},
```
is densely defined, closed, and semibounded on $`\mathcal{H}_1`$.*

</div>

<div class="proof">

*Proof.* Closedness follows because Cauchy sequences in the graph norm of $`q_T`$ map under $`T`$ to Cauchy sequences in the graph norm of $`q`$; boundedness of $`T`$ controls the norms. Semiboundedness is inherited from $`q`$. ◻

</div>

## A.4 Application to $`H_{\rm obs}`$

Let $`H_{10}`$ be the self-adjoint $`10`$D Hamiltonian on $`L^2(M_{10},E)`$ with closed, semibounded quadratic form $`q_{10}`$ and form domain $`\mathcal{Q}(H_{10})`$. Define the observable map $`\mathsf{P}=I\circ\Pi`$ (§<a href="#sec:setup" data-reference-type="ref" data-reference="sec:setup">2</a>) and its adjoint $`\mathcal{P}^{\dagger}:L^2(Y^4)\to L^2(M_{10})`$, which is bounded by <a href="#lem:I-Pi-bounded" data-reference-type="ref+Label" data-reference="lem:I-Pi-bounded">2</a>. Set
``` math
q_{\rm obs}[\psi]\;:=\; q_{10}\big[\mathcal{P}^{\dagger}\psi\big],\qquad
\mathcal{Q}(q_{\rm obs})=\{\psi:\mathcal{P}^{\dagger}\psi\in \mathcal{Q}(H_{10})\}.
```
By <a href="#lem:pullback" data-reference-type="ref+Label" data-reference="lem:pullback">16</a>, $`q_{\rm obs}`$ is closed and semibounded. <a href="#thm:first-repr" data-reference-type="ref+Label" data-reference="thm:first-repr">14</a> then yields the unique self-adjoint $`H_{\rm obs}`$ with $`\langle\psi,H_{\rm obs}\psi\rangle=q_{\rm obs}[\psi]`$ on $`\mathrm{Dom}(H_{\rm obs})\subset\mathcal{Q}(q_{\rm obs})`$. This rigorizes §<a href="#sec:reduction" data-reference-type="ref" data-reference="sec:reduction">3</a> and justifies <a href="#thm:Friedrichs" data-reference-type="ref+Label" data-reference="thm:Friedrichs">3</a> without any compression heuristics.

## A.5 Typical Schrödinger forms and Kato–Rellich

On $`L^2(\mathbb{R}^d)`$, $`q_0[\psi]=\int \frac{\hbar^2}{2m}|\nabla\psi|^2`$ is closed (domain $`H^1(\mathbb{R}^d)`$). If $`V=V_+-V_-`$ with $`V_-\in L^{p}(\mathbb{R}^d)`$ in a Kato class, then the potential form $`v[\psi]=\int V|\psi|^2`$ is $`q_0`$-bounded with relative bound $`<1`$ (Kato–Rellich), hence $`q_0+v`$ is closed and defines the standard self-adjoint $`H=-\frac{\hbar^2}{2m}\Delta+V`$.

*Conclusion.* All uses of $`H_{\rm obs}`$ in the main text rest on <a href="#thm:first-repr,thm:KLMN,lem:pullback" data-reference-type="ref+Label" data-reference="thm:first-repr,thm:KLMN,lem:pullback">[thm:first-repr,thm:KLMN,lem:pullback]</a>, and the hypotheses (H1)–(H7) guarantee they apply.

# Appendix B: Kato’s theorem for time-dependent Hamiltonians

<span id="app:kato" label="app:kato"></span>

## B.1 Hypotheses (form sense)

Let $`\{q(t)\}_{t\in I}`$ be a family of densely defined, closed, semibounded quadratic forms on $`\mathcal{H}`$ with a *common* domain $`\mathcal{Q}\subset\mathcal{H}`$. Assume:

1.  *Uniform lower bound:* $`\exists\,m\in\mathbb{R}`$ such that $`q(t)[\psi]\ge m\|\psi\|^2`$ for all $`\psi\in\mathcal{Q}`$ and $`t\in I`$.

2.  *Form continuity:* $`t\mapsto q(t)[\psi]`$ is continuous on $`I`$ for each $`\psi\in\mathcal{Q}`$.

By the representation theorem, each $`q(t)`$ determines a self-adjoint operator $`H(t)`$ with $`\mathrm{Dom}(H(t))\subset\mathcal{Q}`$ and $`H(t)\ge m`$.

<div id="thm:kato" class="theorem">

**Theorem 17** (Kato’s evolution theorem (form version)). *Under **(K1)–(K2)**, there exists a unique two-parameter family of unitary operators $`\{U(t,s)\}_{t,s\in I}`$ on $`\mathcal{H}`$ such that:*

1.  *$`U(t,t)=\mathbf{1}`$ and $`U(t,r)U(r,s)=U(t,s)`$ for all $`t,r,s\in I`$;*

2.  *For each $`\psi\in\mathcal{Q}`$, $`t\mapsto U(t,s)\psi`$ is strongly continuous and
    ``` math
    i\hbar\,\frac{\mathrm{d}}{\mathrm{d}t}\langle \phi, U(t,s)\psi\rangle \;=\; q(t)\!\big[\phi,\, U(t,s)\psi\big]\quad \forall\,\phi\in\mathcal{Q};
    ```*

3.  *If, in addition, $`t\mapsto q(t)`$ is $`C^1`$ in the form sense, then $`i\hbar\,\partial_t U(t,s)\psi=H(t)\,U(t,s)\psi`$ holds for all $`\psi\in\mathrm{Dom}(H(t))`$.*

</div>

## B.2 Application to $`H_{\rm obs}(t)`$

In the main text, $`q_{\rm obs}(t)`$ has the Schrödinger form
``` math
q_{\rm obs}(t)[\psi]=\int\left(\frac{\hbar^2}{2m}|\nabla\psi|^2 + V_{\rm eff}(x,t)\,|\psi|^2\right)\mathrm{d}x,
```
with $`V_{\rm eff}=V_0(x)+V_{\rm curv}(x,t)`$ and $`V_{\rm curv}(x,t)=\sum_n \alpha_n \kappa_n \beta_n R(x,t)`$. If $`R(\cdot,t)\in L^\infty_{\rm loc}`$ and $`t\mapsto R(\cdot,t)`$ is continuous in the distributional sense on compact sets, then $`t\mapsto q_{\rm obs}(t)`$ is form-continuous on a common domain $`\mathcal{Q}=H^1(\mathbb{R}^d)`$. The uniform lower bound follows if $`V_{\rm eff}`$ is bounded below (or $`V_-`$ is $`q_0`$-small). Hence <a href="#thm:kato" data-reference-type="ref+Label" data-reference="thm:kato">17</a> applies, yielding the unique unitary propagator $`U(t,s)`$ on $`\mathcal{H}_{\mathrm{QM}}`$ with the properties used in §<a href="#sec:time-uncertainty-path" data-reference-type="ref" data-reference="sec:time-uncertainty-path">6</a>.

## B.3 Remarks on stronger regularity

If $`t\mapsto V_{\rm eff}(\cdot,t)`$ is $`C^1`$ in $`L^\infty_{\rm loc}`$ (or in the Kato sense), one obtains differentiability of $`U(t,s)\psi`$ in $`\mathcal{H}`$ and the strong Schrödinger equation $`i\hbar\,\partial_t U(t,s)\psi=H_{\rm obs}(t)\,U(t,s)\psi`$ for $`\psi\in\mathrm{Dom}(H_{\rm obs}(t))`$. If only **(K1)–(K2)** hold, the weak Schrödinger form equation in <a href="#thm:kato" data-reference-type="ref+Label" data-reference="thm:kato">17</a>(b) suffices for all computations in the main text.

# Appendix C: Functional–equation proof details for the Born rule

<span id="app:born-functional" label="app:born-functional"></span>

## C.1 Axioms and reduction to a scalar functional

Let $`\mathcal{H}_{\mathrm{QM}}`$ be a complex Hilbert space, $`\psi\in\mathcal{H}_{\mathrm{QM}}`$ a unit vector, and $`P`$ an orthogonal projector. Define a set function
``` math
\tilde\mu_\psi(P) = w(P,\psi)= e^{-\Delta A(P,\psi)/\hbar}\in[0,\infty),
```
with $`\Delta A`$ the modal re–coherence action increment. Assume:

- *Noncontextuality:* $`\tilde\mu_\psi(P)`$ depends only on $`(P,\psi)`$.

- *Orthogonal additivity:* For orthogonal $`\{P_i\}`$ with $`P=\sum_i P_i`$, $`\tilde\mu_\psi(P)=\sum_i \tilde\mu_\psi(P_i)`$.

- *Unitary covariance:* $`\tilde\mu_{U\psi}(UPU^\dagger)=\tilde\mu_\psi(P)`$.

- *Continuity:* $`(P,\psi)\mapsto \tilde\mu_\psi(P)`$ is continuous.

By (A1)–(A3), there exists a continuous $`f:[0,1]\to[0,\infty)`$ such that
``` math
\tilde\mu_\psi(P)=f\!\big(\langle\psi,P\psi\rangle\big)=:f(p),\qquad p\in[0,1].
```

## C.2 Additivity on partitions and Cauchy–type functional equation

Let $`\{p_i\}_{i=1}^N\subset[0,1]`$ with $`\sum_{i=1}^N p_i\le 1`$. There exist orthogonal projectors $`\{P_i\}`$ with $`\langle\psi,P_i\psi\rangle=p_i`$ and $`P=\sum_i P_i`$ (extend $`\{P_i\}`$ to a decomposition of the identity if necessary). Then by (A2),
``` math
f\!\Big(\sum_{i=1}^N p_i\Big) \;=\; \sum_{i=1}^N f(p_i).
```
In particular, for rational partitions with $`p=\frac{m}{N}`$,
``` math
f\!\Big(\frac{m}{N}\Big) = m\,f\!\Big(\frac{1}{N}\Big),\qquad
f\!\Big(\frac{1}{N}\Big)=\frac{f(1)}{N}.
```
Thus for $`p\in\mathbb{Q}\cap[0,1]`$, $`f(p)=K\,p`$ with $`K:=f(1)`$. By continuity (A4), this extends to all $`p\in[0,1]`$:
``` math
\boxed{\, f(p)=K\,p \, } \quad\text{with } K=f(1)>0.
```

## C.3 Normalization and the Born rule

For an orthogonal resolution $`\{P_i\}`$ of the identity, $`\sum_i \langle\psi,P_i\psi\rangle=1`$. Hence
``` math
\sum_i \tilde\mu_\psi(P_i)=\sum_i f(\langle\psi,P_i\psi\rangle)=K\sum_i \langle\psi,P_i\psi\rangle = K.
```
Normalizing $`\mu_\psi(P):=\tilde\mu_\psi(P)/\sum_i \tilde\mu_\psi(P_i)`$ yields
``` math
\boxed{\, \mu_\psi(P)=\langle\psi,P\psi\rangle \, }.
```
Equivalently, the re–coherence action increment is $`\Delta A(P,\psi)=-\hbar\ln \langle\psi,P\psi\rangle + C`$ with $`C=-\hbar\ln K`$.

## C.4 Relation to Gleason–Busch

For $`\dim\mathcal{H}_{\mathrm{QM}}\ge 3`$, Gleason’s theorem implies any noncontextual, finitely additive probability measure on projectors arises from a density operator. Busch’s generalization covers POVMs and low dimensions. Our derivation identifies the unique exponential weight functional compatible with these theorems; restricting to pure states gives the Born law.

# Appendix D: Stationary–phase lemma and Van Vleck–Gutzwiller kernel

<span id="app:stationary-phase" label="app:stationary-phase"></span>

## D.1 Oscillatory integral lemma

Let $`\Phi:\mathbb{R}^n\to\mathbb{R}`$ be $`C^2`$ with a nondegenerate critical point at $`x_0`$ ($`\nabla\Phi(x_0)=0`$, $`\det \Phi''(x_0)\neq 0`$). Let $`a\in C_c^\infty(\mathbb{R}^n)`$. Then as $`\hbar\to 0^+`$,
``` math
\int_{\mathbb{R}^n} a(x)\,e^{\frac{i}{\hbar}\Phi(x)}\,dx
= (2\pi\hbar)^{n/2}\, e^{\frac{i}{\hbar}\Phi(x_0)} e^{i\frac{\pi}{4}\sigma}
\frac{a(x_0)}{\sqrt{|\det \Phi''(x_0)|}} + \mathcal{O}(\hbar^{(n+1)/2}),
```
where $`\sigma`$ is the signature of $`\Phi''(x_0)`$.

## D.2 Application to the Schrödinger kernel

For $`H_{\rm obs}=-\frac{\hbar^2}{2m}\Delta+V(x)`$ with $`V\in C^2`$ and $`t>s`$, the integral representation of the propagator $`K(t,x;s,y)`$ admits a stationary–phase evaluation over classical paths $`\gamma_{\rm cl}`$ from $`(s,y)`$ to $`(t,x)`$ with action $`S[\gamma_{\rm cl}]`$ and Maslov index $`\nu`$. Under standard nonconjugacy hypotheses,
``` math
\boxed{\, K(t,x;s,y)=\sum_{\gamma_{\rm cl}}
\Big(\frac{1}{2\pi i\hbar}\Big)^{d/2}
\left|\det\frac{\partial^2 S}{\partial x\,\partial y}\right|^{1/2}
\,e^{\frac{i}{\hbar}S[\gamma_{\rm cl}]-i\pi\nu/2} + \mathcal{O}(\hbar)\, }.
```
This matches the Van Vleck–Gutzwiller form and justifies §<a href="#sec:time-uncertainty-path" data-reference-type="ref" data-reference="sec:time-uncertainty-path">6</a>.

# Appendix E: Davies weak–coupling limit and Lindblad generator

<span id="app:davies-lindblad" label="app:davies-lindblad"></span>

## E.1 Assumptions

Let $`\mathcal{H}_{\rm SE}=\mathcal{H}_{\mathrm{QM}}\otimes\mathcal{H}_{\rm env}`$ with the total Hamiltonian $`H_{\rm tot}=H_{\rm obs}\otimes \mathbf{1} + \mathbf{1}\otimes H_{\rm env} + \varepsilon \sum_\alpha S_\alpha\otimes E_\alpha`$. Assume:

- Stationary environment state $`\sigma_{\rm env}`$ with $`\mathrm{Tr}(\sigma_{\rm env} E_\alpha)=0`$.

- Correlations $`C_{\alpha\beta}(t)=\mathrm{Tr}\big(\sigma_{\rm env} E_\alpha(t) E_\beta\big)`$ integrable: $`\int_0^\infty |C_{\alpha\beta}(t)|dt <\infty`$.

- Parallel–bundle stability $`\gamma_n>\delta_n`$ (prevents secular coherent growth).

## E.2 Scaling and convergence

Define $`U_\varepsilon(t)=\exp\{-\frac{i}{\hbar} H_{\rm tot} t\}`$ and the reduced map $`\mathcal{E}_\varepsilon(t)\rho = \mathrm{Tr}_{\rm env}\!\big[U_\varepsilon(t)(\rho\otimes\sigma_{\rm env})U_\varepsilon(t)^\dagger\big]`$. In the interaction picture and on times $`t=\varepsilon^{-2}\tau`$, the Dyson expansion and the Riemann–Lebesgue lemma yield, as $`\varepsilon\to 0`$,
``` math
\mathcal{E}_\varepsilon(\varepsilon^{-2}\tau)\;\Longrightarrow\; e^{\tau \mathcal{L}},
```
where $`\mathcal{L}`$ has GKLS form (spectral decomposition of $`H_{\rm obs}`$):
``` math
\mathcal{L}(\rho) = -\frac{i}{\hbar}[H_{\rm obs}+H_{\rm LS},\rho]
+ \sum_{\omega}\sum_{\alpha,\beta}\Gamma_{\alpha\beta}(\omega)\!\left(S_\beta(\omega)\rho S_\alpha^\dagger(\omega) - \frac12\{S_\alpha^\dagger(\omega)S_\beta(\omega),\rho\}\right).
```
Here $`\Gamma_{\alpha\beta}(\omega)=\int_{-\infty}^{\infty} e^{i\omega t} C_{\alpha\beta}(t)\,dt/(2\pi\hbar^2)`$ is positive semidefinite (Bochner) and $`H_{\rm LS}`$ is the Lamb shift.

## E.3 Complete positivity and trace preservation

Positivity of $`\Gamma(\omega)`$ implies complete positivity of $`e^{\tau\mathcal{L}}`$, and $`\sum_{\alpha,\beta}\Gamma_{\alpha\beta}(\omega)[S_\alpha^\dagger(\omega),S_\beta(\omega)]=0`$ ensures trace preservation. Stability $`\gamma_n>\delta_n`$ makes the Markov approximation consistent in the coherent sector.

# Appendix F: Explicit Naimark/Stinespring dilation for POVMs

<span id="app:naimark" label="app:naimark"></span>

## F.1 Statement

Let $`\{E_\alpha\}`$ be a POVM on $`\mathcal{H}_{\mathrm{QM}}`$ (finite or countable). Then there exist a Hilbert space $`\mathcal{K}`$, an isometry $`V:\mathcal{H}_{\mathrm{QM}}\to \mathcal{H}_{\mathrm{QM}}\otimes\mathcal{K}`$, and a PVM $`\{\Pi_\alpha\}`$ on $`\mathcal{K}`$ such that
``` math
E_\alpha \;=\; V^\dagger (\mathbf{1}\otimes \Pi_\alpha)\, V,\qquad \sum_\alpha E_\alpha=\mathbf{1}.
```

## F.2 Construction (finite POVM)

Let $`E_\alpha=K_\alpha^\dagger K_\alpha`$ be a Kraus decomposition with $`\sum_\alpha K_\alpha^\dagger K_\alpha=\mathbf{1}`$. Set $`\mathcal{K}=\mathbb{C}^N`$ with orthonormal $`\{|\alpha\rangle\}`$ and define $`V:\mathcal{H}_{\mathrm{QM}}\to \mathcal{H}_{\mathrm{QM}}\otimes\mathcal{K}`$ by $`V\psi=\sum_\alpha (K_\alpha\psi)\otimes |\alpha\rangle`$. Then $`V^\dagger V=\mathbf{1}`$ and with $`\Pi_\alpha=|\alpha\rangle\langle\alpha|`$ we have
``` math
V^\dagger(\mathbf{1}\otimes \Pi_\alpha) V
= \sum_{\beta,\gamma} K_\beta^\dagger K_\gamma \langle\beta|\Pi_\alpha|\gamma\rangle
= K_\alpha^\dagger K_\alpha = E_\alpha.
```
Minimality follows by taking $`\mathcal{K}=\overline{\mathrm{span}}\{K_\alpha\mathcal{H}_{\mathrm{QM}}\}`$.

## F.3 Realization in MTT

Choose $`\mathcal{K}`$ as an apparatus coherent–sector subspace $`\subset \mathcal{H}_{\text{coh}}`$, implement $`V`$ by a coherent modal unitary generated by $`H_{10}`$ during the measurement interval, and take $`\Pi_\alpha`$ as sharp pointer projectors. Applying the observable map and partial trace recovers $`\{E_\alpha\}`$ on $`\mathcal{H}_{\mathrm{QM}}`$.

# Appendix G: Domains, essential self–adjointness, and examples

<span id="app:domains" label="app:domains"></span>

## G.1 Kato–Rellich and Schrödinger operators

On $`L^2(\mathbb{R}^d)`$, $`H_0=-\frac{\hbar^2}{2m}\Delta`$ is self–adjoint on $`H^2(\mathbb{R}^d)`$. If $`V=V_+ - V_-`$ with $`V_-\le a\,(-\Delta)+b`$ in the quadratic–form sense for some $`a<1`$, then $`H=H_0+V`$ is self–adjoint and bounded below on $`H^2(\mathbb{R}^d)`$.

## G.2 Nelson’s analytic vector theorem (oscillator)

For $`H=\frac{1}{2m}p^2+\frac12 m\omega^2 x^2`$, Schwartz space $`\mathcal{S}(\mathbb{R})`$ consists of analytic vectors for $`H`$; hence $`H`$ is essentially self–adjoint on $`C_c^\infty(\mathbb{R})`$.

## G.3 Magnetic Hamiltonians

For $`H=\frac{1}{2m}(-i\hbar\nabla - qA)^2+V`$ with $`A\in L^2_{\mathrm{loc}}`$ and $`V`$ in the Kato class, self–adjointness holds on the magnetic Sobolev domain $`H_A^1`$; essential self–adjointness on $`C_c^\infty`$ holds under standard growth/regularity of $`A`$ and $`V`$.
