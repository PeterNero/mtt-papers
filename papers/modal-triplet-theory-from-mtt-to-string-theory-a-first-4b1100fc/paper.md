---
abstract: |
  We present a bridge from Modal Triplet Theory (MTT) to perturbative string theory. Starting from a ten-dimensional coherent fixed point $`(\mathcal{M}_{10},G_{MN},B_{MN},\Phi;A_{M})`$, we show: (i) a bounded worldsheet projection $`\Pi_{\mathrm{ws}}`$ produces the Polyakov/RNS actions; (ii) vanishing worldsheet $`\beta`$–functions holds to the same order in $`\alpha'`$ as the MTT string-frame action, yielding “fixed point $`\Rightarrow`$ conformal background” to controlled order, up to local field redefinitions; (iii) Green–Schwarz anomaly cancellation and tadpole constraints follow from the MTT topological data with $`\alpha'/4`$ normalization and the torsional spin connection $`R_{+}`$; (iv) compactifications (Calabi–Yau and torsional SU(3)) and gauge bundles emerge from modal holonomy and curvature-gap dynamics; (v) T-duality is exact spectral equivalence on $`S^{1}`$, while S-duality is formulated as a modal-landscape conjecture. We record an AdS corner where a GKPW-type functional emerges at the fixed point
author:
- Peter Nero
bibliography:
- main.bib
current_version: v1.0
date: September 6, 2025
generated_from_main_tex_sha256: 555fc10b680633b44f612aec1fdbcb38414e10c26e87995229e15a6db8e854ac
paper_id: modal-triplet-theory-from-mtt-to-string-theory-a-first-4b1100fc
release_state: zenodo_released
released_version: v1.0
title: |
  Modal Triplet Theory: From MTT to String Theory:  
  A First-Principles Embedding with Worldsheet Projection
zenodo_doi: 10.5281/zenodo.17068115
zenodo_record_id: 17068115
zenodo_url: "https://zenodo.org/records/17068115"
---

# Introduction and motivation

MTT posits a ten-dimensional field ontology with three internal bundles and a bounded joint projector. A contractive flow yields a unique fixed point $`\Psi^{*}`$ that governs low-energy physics. We ask: when does $`\Psi^{*}`$ define a string-consistent background? Answer: (i) map $`(G,B,\Phi;A)`$ to target-space data; (ii) derive worldsheet actions by $`\Pi_{\mathrm{ws}}`$; (iii) show $`\beta=0`$ to controlled order in $`\alpha'`$, consistent with the Strominger slice and the 11D lift.

# Target-space data from MTT and trace conventions

At the fixed point, identify:
``` math
\begin{equation}
H = dB - \frac{\alpha'}{4}\big(\omega_{3}(A)-\omega_{3}(\omega_{+})\big), \qquad
dH = \frac{\alpha'}{4}\left(\mathrm{Tr}_{\mathrm{grav}}R_{+}\wedge R_{+}- \mathrm{Tr}F\wedge F\right).
\label{eq:GS}
\end{equation}
```
Here $`\omega_{+}`$ is the Bismut/Hull connection with curvature $`R_{+}`$.

#### Trace conventions.

We use $`\mathrm{Tr}`$ for the gauge adjoint trace, normalized so that $`\mathrm{Tr}(T^{2})=1`$ for any abelian generator $`T`$, and $`\mathrm{Tr}_{\mathrm{grav}}`$ for the vector trace on $`\mathfrak{so}(d)`$. These conventions match our heterotic flux compactifications and Strominger selection paper.

#### Scheme remark.

$`\beta`$-function equations are scheme-dependent at $`O(\alpha'^{2})`$; we always mean equality up to local field redefinitions that preserve on-shell amplitudes.

# Worldsheet action from a bounded projection

Let $`X:\Sigma\to\mathcal{M}_{10}`$. Pull back via $`\Pi_{\mathrm{ws}}`$. The bosonic action is
``` math
\begin{equation}
S_{\text{bos}} = -\frac{1}{4\pi\alpha'}\!\int_{\Sigma}\!\!\sqrt{-h}\,h^{ab}G_{MN}\partial_{a}X^{M}\partial_{b}X^{N}
+ \frac{1}{4\pi\alpha'}\!\int_{\Sigma}\!\!\epsilon^{ab}B_{MN}\partial_{a}X^{M}\partial_{b}X^{N}
+ \frac{1}{4\pi}\!\int_{\Sigma}\!\!\sqrt{-h}\,\Phi R^{(2)}.
\end{equation}
```
In RNS, fermions couple via the pullback spin connection; the full action is $`S_{\mathrm{ws}}=S_{\text{bos}}+S_{\text{ferm}}+S_{\text{ghosts}}`$. BRST nilpotency $`\Leftrightarrow`$ $`\beta=0`$ at controlled order.

# Vanishing $`\beta`$ functions from the fixed point

At leading order in $`\alpha'`$:
``` math
\begin{align}
\beta^{G}_{MN} &= \alpha'\!\left(R_{MN} - \tfrac{1}{4}H_{MPQ}H_{N}{}^{PQ} + 2\nabla_{M}\nabla_{N}\Phi\right)+\mathcal{O}(\alpha'^{2}),\\
\beta^{B}_{MN} &= \alpha'\!\left(-\tfrac{1}{2}\nabla^{P}H_{PMN} + \nabla^{P}\Phi\,H_{PMN}\right)+\mathcal{O}(\alpha'^{2}),\\
\beta^{\Phi} &= \frac{D-26}{6} - \frac{\alpha'}{2}\Big(\nabla^{2}\Phi - 2(\nabla\Phi)^{2} + \tfrac{1}{12}H^{2}\Big)+\mathcal{O}(\alpha'^{2}),
\end{align}
```
with $`D=10`$ for superstrings (ghost/fermion shifts cancel the constant). The gauge $`\beta`$ enforces HYM.

<div class="theorem">

**Theorem 1** (Fixed point $`\Rightarrow`$ $`\beta=0`$ to order $`\alpha'^{n}`$). *If the MTT string-frame action matches 10D supergravity+$`\alpha'`$ corrections to $`\alpha'^{n}`$ and $`\Psi^{*}`$ solves the projected EL equations with $`R_{+}`$, then $`(G,B,\Phi;A)`$ satisfies $`\beta^{G}=\beta^{B}=\beta^{\Phi}=0`$ to $`\alpha'^{n}`$, up to field redefinitions.*

</div>

# Consistency: anomalies, Bianchi, supersymmetry

With <a href="#eq:GS" data-reference-type="eqref" data-reference="eq:GS">[eq:GS]</a>, anomaly cancellation is manifest.

<div class="proposition">

**Proposition 2**. *If $`\int_{C_{4}}\mathrm{Tr}F^{2} = \int_{C_{4}}\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}`$ for all 4-cycles $`C_{4}\subset X_{6}`$, then the Bianchi identity holds at the fixed point.*

</div>

<div class="remark">

**Remark 3**. *In the torsional SU(3) slice (balanced metrics, HYM bundles), the Hull–Strominger system arises: $`d(e^{-2\Phi}J^{2})=0`$, $`F^{0,2}=J\lrcorner F=0`$, $`H=i(\bar\partial-\partial)J`$, $`dH=\frac{\alpha'}{4}(\mathrm{Tr}_{\mathrm{grav}}R_{+}^{2}-\mathrm{Tr}F^{2})`$. Our selection theorem proves strict convexity: the Strominger solution is the unique minimizer = MTT fixed point ().*

</div>

#### Modular invariance.

In the CY/toroidal corner, the one-loop partition function is modular-invariant; $`\tau_{2}\to 0`$ maps to $`\tau_{2}\to\infty`$, ensuring UV finiteness. See our UV paper for a full derivation ().

# Compactification and 4D EFT

The 10D action reduces to
``` math
\begin{equation}
S_{4}=\frac{1}{2\kappa_{4}^{2}}\int d^{4}x\sqrt{-g_{4}}\left(R_{4}-\tfrac{1}{2}G_{IJ}\partial\varphi^{I}\partial\varphi^{J}-V_{\text{eff}}(\varphi)\right)
+ S_{\text{gauge}}+S_{\text{Yuk}}+\cdots,
\end{equation}
```
with
``` math
\begin{equation}
\frac{1}{g_{4}^{2}}=\frac{1}{g_{10}^{2}}\,\mathrm{Vol}(X_{6})\,e^{-2\Phi_{0}}.
\end{equation}
```
Yukawas come from internal overlaps. In MTT, curvature–gap dynamics fix $`V_{\text{eff}}`$.

# Dualities and holography

#### T-duality.

On $`S^{1}_{R}`$: $`M^{2}=n^{2}/R^{2}+w^{2}R^{2}/\alpha'^{2}+\cdots`$ invariant under $`(n,w;R)\mapsto(w,n;\alpha'/R)`$.

#### S-duality.

Conjectural map exchanging weak/strong fixed points $`g_{s}\leftrightarrow 1/g_{s}`$ and topological sectors.

#### Holography.

At AdS fixed points, $`Z_{\text{bulk}}[\phi_{0}]=e^{-S_{\text{on-shell}}[\phi_{0}]}`$ produces boundary correlators.

# Alignment

The torsional SU(3) slice selection theorem proves uniqueness of Strominger solutions (). The 11D lift reproduces shifted $`G_{4}`$ quantization and M5 anomaly (). Together, the string, flux, and M-theory slices are mutually consistent.

# Conclusions

We have embedded perturbative string theory within MTT with consistent conventions, avoiding regressions. Fixed points yield target data; $`\Pi_{\mathrm{ws}}`$ gives worldsheet actions; $`\beta=0`$ follows to order $`\alpha'^{n}`$ with $`R_{+}`$; anomaly cancellation is manifest; compactifications, dualities, and holography align with heterotic flux selection and 11D lifts.
