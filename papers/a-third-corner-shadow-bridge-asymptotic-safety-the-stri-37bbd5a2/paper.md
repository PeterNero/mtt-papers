---
abstract: |
  Modal Triplet Theory currently approaches ultraviolet gravity through two partly developed routes: selected q79 heterotic geometry and projection-filtered four-dimensional constructions. Functional renormalization group asymptotic safety can serve as a third diagnostic corner, but it is not yet equivalent to either route. This paper gives a theorem-light map of the three descriptions. The q79 branch has exact finite algebraic data and a partial heterotic worldsheet contract; the physical visible-hidden bundle, continuum HYM operator, and infrared conformal field theory remain open. The FRG corner has conditional endpoint, conjugacy, truncation-error, and unstable-subspace theorems, but no selected MTT-to-coupling chart. Agreement of fixed points or critical exponents can therefore be used only after overlap domains, maps, conventions, and defects are supplied. The useful claim is a conditional triple diagnostic: independent encodings may test one selected upper construction. The paper does not claim equivalence of ultraviolet completions.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 3e41b1f2bb07a7a45fd45dccfd4f5d9c62c8636a07396c9fc453e6c6dde99fad
paper_id: a-third-corner-shadow-bridge-asymptotic-safety-the-stri-37bbd5a2
release_state: zenodo_released
released_version: v2
title: |
  The Asymptotic-Safety Third Corner in MTT:
  A Conditional Diagnostic Between Coherent Geometry and the String Branch
zenodo_doi: 10.5281/zenodo.21665942
zenodo_record_id: 21665942
zenodo_url: "https://zenodo.org/records/21665942"
---

# Version 2 Revision Note

<div class="description">

Version 1.0, *A Third-Corner Shadow Bridge: Asymptotic Safety, the String Corner, and the Coherent Spine in Modal Triplet Theory*.

The earlier paper promoted assumed conjugacies into a triple-corner equivalence and used an invalid additive-error fixed-point lemma.

All technical fixed-point claims are assigned to their owner papers. This paper now describes the three corners, their actual current status, and the maps and error certificates needed for comparison.

A three-corner comparison is a useful consistency test when the encodings arise from one selected upper object and their overlap maps commute.

The physical q79 worldsheet contract, continuum geometry-to-operator map, and MTT-to-FRG coupling chart are all incomplete. No triple equivalence is claimed.

</div>

# The idea that survives

The motivating idea is good: one underlying construction can have several effective descriptions, and agreement among them is stronger evidence than success in one representation. In MTT the proposed corners are:
``` math
\begin{array}{c}
\text{selected coherent q79 geometry}\\[0.3em]
\swarrow\qquad\searrow\\[-0.2em]
\text{heterotic/worldsheet description}
\qquad
\text{four-dimensional FRG description}.
\end{array}
```

The correction concerns the arrows. They are not supplied by drawing the diagram. Each arrow must map states, operators, normalizations, and dynamics on a declared overlap domain. Exact fixed-point correspondence then follows from conjugacy; approximate commutation gives only a residual and an error budget.

This paper is intentionally interpretive. The technical conditional conjugacy and unstable-subspace results belong to the MTT–asymptotic-safety paper. The truncation residual bounds belong to its companion truncation paper. The worldsheet obligations belong to the q79 heterotic program.

# Corner one: selected coherent geometry

The upper corner is not an unspecified “coherent spine.” Its strongest current realization is the selected q79 branch. At the finite tier the corpus contains:

- a finite root-stack and shared-line construction;

- a $`1+2+3`$ rank filtration;

- exact finite projectors and a normalized finite Hessian;

- a rank-two coherent kernel and rank-four penalized complement;

- finite Standard-Model carrier and profile-level compatibility results.

These are real algebraic achievements. They do not yet provide the selected physical nonzero-Chern HYM bundles, continuum Hessian blocks, upper action, or four-dimensional quantum theory. The continuum naturality theorem must preserve connections, covariant derivatives, sectors, and Hessians, not just vector-space dimensions.

The phrase “upper” therefore means prior to the effective encodings, not already proven more fundamental physics.

# Corner two: the q79 string branch

Fu–Yau geometry gives a mathematically established route to non-Kähler heterotic compactifications satisfying the Hull–Strominger system under specific bundle and anomaly conditions . This makes the q79 Fu–Yau branch the strongest current MTT compactification candidate.

The present MTT worldsheet contract is not complete. Its current ledger has:
``` math
5\text{ available rows},\qquad
2\text{ partial rows},\qquad
5\text{ open rows}.
```
The missing work includes the selected physical visible-hidden bundle, common stability chamber and HYM connections, full anomaly/Bianchi compatibility at the selected endpoint, and the infrared SCFT/GSO data.

Consequently, “string corner” means a selected geometric candidate with a partial contract. It does not mean that perturbative string theory, the full worldsheet CFT, and four-dimensional MTT have already been proved equivalent.

# Corner three: asymptotic safety

The FRG describes the scale dependence of an effective average action $`\Gamma_k`$ . Its asymptotic-safety program searches for a dimensionless ultraviolet fixed functional with finitely many relevant directions.

The revised MTT asymptotic-safety work now provides four conditional tools:

1.  an integrable-flow theorem for existence of a Banach-space endpoint;

2.  an exact-conjugacy theorem for transporting fixed points and spectra;

3.  a truncation residual theorem with an a posteriori error bound;

4.  a quasi-compactness theorem for a finite-dimensional unstable subspace.

These tools do not yet supply the physical input to which they would be applied. The open data are:

- a selected chart from q79/coherent variables to dimensionless FRG couplings;

- a physical regulator, gauge fixing, ghost sector, and action norm;

- a four-dimensional shell-integrability estimate;

- a certified truncation defect and essential spectral-radius bound.

The third corner is therefore a diagnostic language and a possible target encoding, not an independently closed UV completion.

# What a valid triple comparison looks like

Let $`\mathcal U`$ denote an overlap domain in the selected upper theory, $`\mathcal W`$ a worldsheet description space, and $`\mathcal F`$ an FRG action space. A comparison requires maps
``` math
\mathcal C_{\mathrm{ws}}:\mathcal U\to\mathcal W,
 \qquad
 \mathcal C_{\mathrm{FRG}}:\mathcal U\to\mathcal F.
```
Each map must carry more than configurations. It must specify:

- domains and admissible states;

- parameters and normalization conventions;

- symmetries, constraints, and quotient operations;

- scale evolution or fixed-point maps;

- observables used in the comparison;

- exactness or an explicit defect norm.

Suppose $`T_{\mathcal U}`$, $`T_{\mathcal W}`$, and $`T_{\mathcal F}`$ are the relevant step maps. The exact target is
``` math
\mathcal C_{\mathrm{ws}}T_{\mathcal U}=T_{\mathcal W}\mathcal C_{\mathrm{ws}},
 \qquad
 \mathcal C_{\mathrm{FRG}}T_{\mathcal U}=T_{\mathcal F}\mathcal C_{\mathrm{FRG}}.
```
Under injective regular charts, upper fixed points then map to fixed points and the restricted linearizations are similar. This conclusion is imported from the technical conjugacy theorem.

If instead
``` math
\|\mathcal C_{\mathrm{FRG}}T_{\mathcal U}-T_{\mathcal F}\mathcal C_{\mathrm{FRG}}\|\leq\varepsilon_{\mathcal F},
```
the image has a fixed-point residual of order $`\varepsilon_{\mathcal F}`$. A nearby exact fixed point follows only when a separate validation theorem applies. The same rule holds in the worldsheet corner.

# What can actually be compared

<div class="center">

| Quantity | Meaningful comparison | Required certificate |
|:---|:---|:---|
| Fixed point | Same selected upper state in two charts | Intertwining step maps and domain overlap. |
| Critical exponents | Spectra of conjugate linearizations | Differentiable chart, isolated spectrum, and error bound. |
| Relevant directions | Finite unstable Riesz subspace | Essential spectral-radius control. |
| Anomaly conditions | Worldsheet and spacetime consistency | Selected bundles, connections, and Bianchi identity. |
| Four-dimensional couplings | Reduced observables in one convention | Reduction, matching, RG, and normalization map. |
| UV damping | High-mode behavior of a physical operator | Same-source spacetime operator, not an internal filter alone. |

</div>

Equal numerical values without these certificates can still be suggestive, but they do not establish that the calculations describe the same object.

# How disagreement would help

The three-corner program is valuable even when the corners disagree. Suppose a selected upper candidate passes the finite q79 constraints but cannot satisfy the worldsheet anomaly conditions. Then either the candidate is not a physical heterotic background or the proposed worldsheet chart is wrong. If the same candidate yields an FRG flow with no admissible fixed point under a proved chart, then the asymptotic-safety interpretation fails for that branch.

This makes the diagram a falsification tool. It does not guarantee that all successful theories are secretly equivalent. It asks whether one selected object survives several independently meaningful representations.

# Relation to the shared circle and fixed points

The common q79 line can provide shared phase and holonomy data across finite operators. It does not by itself identify a worldsheet renormalization scale, an FRG scale, or Lorentzian time. Those identifications require connection-preserving maps.

Likewise, fixed points appear in all three corners for different reasons:

<div class="description">

stability or closure under the selected MTT map;

vanishing beta functions and conformal consistency;

scale invariance of a dimensionless effective action.

</div>

The shared word does not establish equality. Conjugacy of the maps does.

# Current status

<div class="center">

| Corner or bridge | Status | Current boundary |
|:---|:---|:---|
| Finite q79 upper carrier | Exact at finite tier | Physical continuum HYM/action transfer open. |
| q79 heterotic worldsheet | Partial, 5/12 available | Visible-hidden endpoint and IR worldsheet data open. |
| FRG analytic toolkit | Exact conditional | Physical chart and estimates open. |
| Upper-to-worldsheet map | Partial/open | Full same-source worldsheet contract absent. |
| Upper-to-FRG map | Open | No selected coupling chart or conjugacy certificate. |
| Triple diagnostic | Proposed | Usable once both maps have certified overlap domains. |
| Triple equivalence of UV completions | Not established | Neither pairwise bridge is complete. |

</div>

# Discussion

The revised picture is less dramatic and more informative. The q79 branch anchors the geometric side in established heterotic mathematics, while the FRG corner supplies a language for scale dependence and relevant directions. MTT contributes the possibility that both are representations of one selected upper construction. The research value lies in constructing and testing the arrows.

A particularly useful next target is a small overlap packet rather than a claim of total equivalence. Choose one selected q79 fluctuation sector, derive its reduced quadratic operator, identify a finite set of dimensionless FRG couplings, and compute both the worldsheet and FRG linearized responses with conventions and errors. Agreement would be a nontrivial cross-check. Disagreement would localize the broken bridge.

# Conclusion

Asymptotic safety can function as a third corner of the MTT quantum-gravity program, but today it is a conditional diagnostic. The finite q79 geometry, partial heterotic contract, and conditional FRG mathematics are mutually relevant without yet being equivalent.

The correct forward statement is therefore:
``` math
\text{one selected upper object}
\longrightarrow
\text{several certified encodings}
\longrightarrow
\text{cross-checked observables}.
```
The next advance must construct one of those certified arrows. Redrawing the triangle more strongly would not move the frontier.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The comparison between the asymptotic-safety and string routes is a conditional structural diagnostic. No numerical Standard Model packet proves that comparison. The mapped strict-upgrade ledger is included only to mark the unresolved no-knob boundary inherited by later ultraviolet claims.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

A. Strominger, “Superstrings with torsion,” *Nuclear Physics B* **274** (1986), 253–284.

J.-X. Fu and S.-T. Yau, “The theory of superstring with flux on non-Kähler manifolds and the complex Monge–Ampère equation,” *Journal of Differential Geometry* **78** (2008), 369–428.

C. Wetterich, “Exact evolution equation for the effective potential,” *Physics Letters B* **301** (1993), 90–94.

M. Reuter, “Nonperturbative evolution equation for quantum gravity,” *Physical Review D* **57** (1998), 971–985.

P. Nero, *Modal Triplet Theory: Foundations*, current revised MTT paper corpus, 2026.

P. Nero, *Modal Triplet Theory and Asymptotic Safety: A Conditional FRG Conjugacy and Unstable-Subspace Theorem*, current revised MTT paper corpus, 2026.

P. Nero, *Asymptotic-Safety Truncations as Conditional Shadows: Fixed-Point Residuals, Error Bounds, and Scheme Dependence*, current revised MTT paper corpus, 2026.

</div>
