---
abstract: |
  This paper separates three levels of the current Modal Triplet Theory (MTT) quantum-gravity program. First, an exact finite-carrier result supplies internal transverse-traceless support, while a separate controlled reduction recovers the four-dimensional Einstein action only under declared higher-dimensional action, truncation, gap, and normalization hypotheses. Second, once the resulting local Einstein–matter effective action, Wilson coefficients, state, gauge fixing, and scheme are supplied, standard background-field and BV/BRST methods give fixed-order perturbative quantum-GR equivalence. This is an imported parity construction, not a derivation of the quantum measure or Wilson coefficients from MTT. The two-derivative theory is not ultraviolet complete: its counterterm order grows with loop number and the two-loop pure-gravity divergence is nonzero. Third, the selected compatible ultraviolet route is the q79 Fu–Yau heterotic branch. A conditional inheritance theorem gives absence of local ultraviolet divergences at each fixed genus and multiplicity if an exact modular, anomaly-free heterotic worldsheet theory with factorization, GSO projection, and BV vertices is supplied. The current q79 worldsheet contract has five of twelve rows available, two partial, and five open. The physical nonpullback holomorphic/HYM bundles, complete Green–Schwarz representative, exact worldsheet SCFT, string-field realization, infrared completion, all-genus control, and nonperturbative definition remain open. The resulting claim is therefore low-energy quantum-gravity parity plus a sharply specified heterotic completion program, not completed ultraviolet quantum gravity.
author:
- Peter Nero
bibliography:
- main.bib
current_version: v6
date: Sixth edition July 2026
generated_from_main_tex_sha256: b5306c19857e56517685d64be04d196570780d6f315cf8987b54aeb3c68afe19
paper_id: modal-triplet-theory-perturbative-coherent-sector-quant-eb63e01d
release_state: zenodo_released
released_version: v6
title: "Modal Triplet Theory: Perturbative Coherent-Sector Quantum Gravity and the Heterotic UV-Completion Boundary"
zenodo_doi: 10.5281/zenodo.21666000
zenodo_record_id: 21666000
zenodo_url: "https://zenodo.org/records/21666000"
---

# Revision note for this edition

Supersedes.
*Modal Triplet Theory: Perturbative Coherent-Sector Quantum Gravity and the Heterotic UV-Completion Boundary*, version 5.

Reason.
Version 5 correctly discovered the Gaussian positivity no-go and loop-rank obstruction, but it repeated those results in several appendices, retained an unselected schedule as a derivation of the SPT endpoint, and sometimes described imported perturbative QFT machinery as though it were selected by MTT.

Resolution.
This edition assigns the SPT mathematics to the companion Euclidean TT paper, states the low-energy result at its exact fixed-order parity tier, presents all twelve q79 worldsheet gates, and separates fixed-genus ultraviolet inheritance from all-genus and nonperturbative completion.

Retained result.
The current chain supports an exact internal TT carrier, conditional classical GR reduction, fixed-order quantum-GR EFT parity, selection of the q79 heterotic route as the primary compatible UV candidate, and a conditional fixed-genus inheritance theorem.

Remaining boundary.
MTT has not yet selected the physical higher-derivative Wilson values, complete Lorentzian quantum state and measure, physical nonpullback heterotic bundles, exact q79 worldsheet theory, or nonperturbative ultraviolet completion.

# Purpose, Orientation, and Claim Tiers

In plain language, the present construction has a low-energy bridge and a candidate high-energy bridge. The low-energy bridge says that if MTT supplies the same effective gravitational data used by quantum GR, then the standard quantization machinery yields the same fixed-order observables. The high-energy bridge says that if the selected q79 geometry can be completed into an exact heterotic worldsheet theory, it inherits the string worldsheet’s fixed-genus ultraviolet behavior. Neither conditional bridge manufactures its missing input.

The logical tiers are:

<div class="center">

| Tier | Current status | Meaning |
|:---|:---|:---|
| Finite internal TT carrier | exact on the declared finite branch | Internal helicity-two support, not yet a normalized Lorentzian graviton |
| Four-dimensional Einstein reduction | conditional | Requires an higher-dimensional Einstein sector, controlled truncation, and stabilized non-Einstein modes |
| Interacting quantum-GR EFT | fixed-order parity | Standard QFT structure is imported after action, Wilson data, state, and scheme are declared |
| SPT Gaussian filter | conditional Euclidean model | Useful graph regulator; not selected physical propagation |
| q79 heterotic route | selected compatible route | The route is selected, but its physical worldsheet object is incomplete |
| Fixed-genus string UV inheritance | conditional theorem | Applies only after the exact worldsheet hypotheses are met |
| All-genus or nonperturbative QG | open | No convergence or constructive definition has been supplied |

</div>

The word *parity* is important. It means equality to an already defined target theory after matching all target inputs at a declared order. It is a valid equivalence statement, but it is not a no-input prediction or a derivation of those inputs.

# The Low-Energy Coherent-Sector Tier

## What MTT supplies before quantization

The finite proto-spinor/GR program proves an exact internal TT support identity on the selected finite carrier. It identifies the intended helicity-two internal block and removes an ambiguity that was formerly left as an ansatz. It does not by itself provide:

- a Lorentzian principal symbol and physical massless pole;

- the Newton or Planck normalization;

- universal conserved coupling to the full stress tensor;

- the causal state or asymptotic prescription; or

- the interacting higher-derivative Wilson coefficients.

The companion paper *Controlled Coherent Reduction to Four-Dimensional Einstein Gravity* supplies a separate analytic bridge. On a $`4+6`$-dimensional geometry, it gives a contraction/Schur–Feshbach estimate for eliminating heavy modes, provided that the higher-dimensional Einstein sector, gap, small coupling, truncation, and zero-mode audit are already available. The shared circle is counted once as common holonomy data and is not identified with compact physical time.

## Fixed-order quantum-GR parity

Let $`S_{\rm EFT}^{(N)}`$ denote the local diffeomorphism-invariant Einstein–matter effective action through a declared loop and derivative order $`N`$. It includes the Einstein term, cosmological term, matter sector, and the finite list of local higher-curvature operators required at that order. Let $`\sigma`$ denote the causal state, gauge fixing, scale, and renormalization scheme. The current parity construction is summarized by
``` math
\begin{equation}
 \mathcal{O}_{\rm MTT}^{(N)}
 =
 \operatorname{Readout}\circ
 \operatorname{Green}_{\sigma}\circ
 Q_{\rm GR,EFT}^{(N)}\circ
 E_{q79}.
 \label{eq:composition}
\end{equation}
```
Here $`E_{q79}`$ embeds the declared coherent source data into the effective field variables, $`Q_{\rm GR,EFT}^{(N)}`$ is the standard fixed-order background-field/BV quantization, and the final maps construct the selected observables.

<div id="prop:parity" class="proposition">

**Proposition 1** (Fixed-order parity statement). *If $`E_{q79}`$ supplies the same renormalized action $`S_{\rm EFT}^{(N)}`$, Wilson coefficients, gauge fixing, state, scale, and scheme as quantum GR EFT through order $`N`$, then the renormalized generating functionals and gauge-invariant observables obtained from <a href="#eq:composition" data-reference-type="eqref" data-reference="eq:composition">[eq:composition]</a> agree through order $`N`$.*

</div>

<div class="proof">

*Proof.* After the stated data are identified, both constructions apply the same renormalized functional and the same observable maps. Equality follows by composition. The proposition proves a typed embedding/equivalence result; it does not select the matched data. ◻

</div>

#### What this means.

The proposition checks that the MTT carrier can host the standard fixed-order quantum-GR calculation without changing its predictions. Its scientific content is compatibility and typed transport. Predictive improvement would require MTT to emit some of the matched Wilson values, state data, or normalization before the target calculation is imported.

On a globally hyperbolic background with a Hadamard state, local covariant time-ordered products and perturbative observables can be constructed using Epstein–Glaser or perturbative algebraic QFT methods . The BV induction restores the quantum master equation order by order when the relevant local ghost-number-one anomaly class vanishes . These are standard imported theorems. The current MTT source does not yet derive the full measure, Hadamard state, anomaly cohomology, or fixed-nonzero-coupling completion.

## Why fixed-order predictivity is not UV completion

For a connected Einstein graph with $`L`$ loops, $`V`$ two-derivative vertices, and $`I`$ internal lines, the superficial derivative order is
``` math
D=4L+2V-2I.
```
Using $`L=I-V+1`$ gives
``` math
\begin{equation}
 D=2L+2.
 \label{eq:power}
\end{equation}
```
For example, tree, one-loop, and two-loop graphs require operators of superficial derivative order two, four, and six respectively. The Riemann-cubed counterterm at two loops is therefore the first explicit worked case showing why the two-derivative parameter set cannot remain closed. At every fixed loop order only finitely many local counterterms are needed, which is precisely the effective-field-theory notion of predictivity . Across all loop orders, however, the derivative order is unbounded. Pure gravity is on-shell finite at one loop for zero cosmological constant in the standard sense, but it has a nonzero two-loop Riemann-cubed divergence .

Consequently, the two parameters of the two-derivative action do not define an all-scale interacting quantum theory. The current MTT parity theorem allows a finite set of declared Wilson values at any chosen order; it does not emit their complete tower.

# Why SPT Does Not Close the Ultraviolet Problem

The companion paper *An SPT-Filtered Euclidean TT Model and Its Conditional Perturbative Properties* owns the SPT theorems. Its conclusions can be summarized without repeating their proofs:

1.  an internal spectral gap controls internal inversion but does not produce an external Gaussian multiplier;

2.  a positive proper-time endpoint is an additional filter or schedule assumption;

3.  Gaussian-damped lines control all $`L`$ loop directions exactly when their loop-momentum matrix $`C_\Gamma`$ has $`\operatorname{rank}C_\Gamma=L`$, equivalently when unfiltered edges form a forest; and

4.  a nonzero positive Kallen–Lehmann/Stieltjes propagator cannot have permanent Gaussian decay in the same Euclidean spectral variable.

These results leave SPT useful as a Euclidean regulator or exploratory effective filter. They withdraw the former route
``` math
\text{internal gap}
 \Longrightarrow
 \text{physical Gaussian propagator}
 \Longrightarrow
 \text{OS positivity, causality, and unitarity}.
```
Each arrow needs an independent theorem, and the first arrow is false in general. The exact finite TT eigenvalue recorded by the internal carrier is dimensionless until a physical units-and-normalization map is supplied; it is not automatically the Planck cutoff.

# The Selected q79 Heterotic Route

## Why this is the primary compatible candidate

The q79 program selects a Fu–Yau-type heterotic route rather than the SPT filter as its primary compatible ultraviolet candidate. Fu–Yau geometry provides established existence machinery for non-Kahler heterotic compactifications with torsion under specific bundle, stability, and anomaly conditions . Torsion linear sigma models provide a related worldsheet framework . These external theorems do not say that every topological MTT packet is automatically a physical heterotic vacuum.

The current q79 records include:

- a time-oriented discrete branch label $`q=79`$, with conjugate $`369`$ modulo $`448`$;

- a degree-two K3 incidence GLSM base and rank-one Fu–Yau source data;

- curvature-level Green–Schwarz/Bianchi information;

- finite gerbe, torsion-phase, and modular-orbit data;

- a smooth topological visible $`SU(3)`$ candidate with $`c_2=9u`$ and $`c_3=\pm6`$; and

- partial twisted-spectral and modular-character calculations.

Topological existence and Hodge admissibility do not yet produce the physical nonpullback holomorphic bundle, a common positive HYM chamber, connections, or the complete local worldsheet anomaly data. Those are the physical endpoint obligations, not optional polish.

## Conditional fixed-genus inheritance

<div id="thm:inheritance" class="theorem">

**Theorem 2** (Heterotic fixed-genus UV inheritance). *Assume the selected q79 background is completed to an exact anomaly-free modular heterotic $`(0,2)`$ worldsheet theory with a tachyon-free GSO projection, correct factorization, and quantum-BV string vertices. Then each fixed-genus, fixed-multiplicity on-shell amplitude has no local point-particle ultraviolet divergence. Possible degeneration-boundary singularities are governed by physical factorization channels and require the separate tadpole, vacuum-shift, and infrared prescriptions.*

</div>

<div class="proof">

*Reason for the inheritance.* Worldsheet moduli are integrated over a modular fundamental domain rather than over an unrestricted point-particle proper-time region. Short-distance operator collisions are controlled by the worldsheet OPE and BRST factorization, while modular equivalence removes duplicate ultraviolet regions. Degenerations of the Riemann surface represent long tubes and physical on-shell propagation, so their divergences are infrared or tadpole questions rather than local ultraviolet counterterms. This is the standard perturbative string framework applied conditionally to the q79 background . ◻

</div>

The theorem is coefficientwise in genus and multiplicity. It does not prove convergence of the genus expansion, existence of a preferred vacuum, or a nonperturbative definition.

## The twelve-row worldsheet contract

The present contract is not a vague list of future work. It has twelve named rows, with five available, two partial, and five open:

| Row | Required object | Current status |
|:---|:---|:---|
| Row | Required object | Current status |
| W1 | Time-oriented q79 target branch | Available |
| W2 | Fu–Yau Mukai charge and Green–Schwarz/Bianchi sector | Available |
| W3 | Visible curvature-level Green–Schwarz cancellation | Available at curvature tier |
| W4 | Critical heterotic central-charge balance | Available universally |
| W5 | q79 low-energy GR and quantum-EFT limit | Available at declared parity tier |
| W6 | Global Deligne gerbe and Freed–Witten condition on the full visible cycle set | Open; finite representative only |
| W7 | All-orders-in-$`\alpha'`$ q79 target background | Open; current background is first-order |
| W8 | Exact q79 heterotic $`(0,2)`$ SCFT or all beta functions | Partial; base GLSM, local anomaly, and topological candidate exist, but the physical bundle and IR SCFT do not |
| W9 | q79 modular-invariant GSO partition function and factorization | Partial; finite torsion module and seven-seed induction exist, analytic characters and GSO remain open |
| W10 | q79-specific string-field vertices and BV master action | Open; standard framework exists but is not instantiated on q79 |
| W11 | Tadpole, vacuum-shift, infrared, and soft-state completion | Open |
| W12 | All-genus convergence or a nonperturbative definition | Open |

Rows W8 and W9 are genuine advances, but partial rows do not count as available rows. The current authoritative total remains $`5/12`$, with two additional partials. Standard heterotic string-field BV machinery is known ; importing its existence is not the same as building the q79 vertices.

# Branch Orientation, Conjugation, and Double Traversal

The q79 and $`369`$ labels form a conjugate pair modulo $`448`$:
``` math
79+369\equiv0\pmod{448}.
```
Current MTT results select the retarded $`q79/F/m1`$ representative at the orientation level. They do not prove uniqueness of the global carrier measure, derive the initial state, or require the conjugate branch to be well-behaved.

A Schwinger–Keldysh or closed-time-path description doubles fields along forward and backward contour legs. Given a normalized density operator and unitary evolution, equal sources obey $`Z[J,J]=1`$ . This identity expresses cancellation on a closed contour; it does not select the arrow of time or prove that a literal double traversal of the MTT circle returns the universe to a state with no space, time, or gravity.

The shared MTT circle is therefore treated as common phase or holonomy data. Physical time is a noncompact Lorentzian ordering variable, possibly related to a lift of phase data only after an additional theorem.

# What Has Been Achieved and What Would Close the Program

## Achievements at their declared tiers

- The internal TT sector is selected exactly on the finite carrier.

- A controlled analytic reduction to four-dimensional Einstein gravity is available under explicit hypotheses.

- Quantum GR EFT parity is closed at each fixed declared order after matching the action, Wilson data, state, gauge fixing, scale, and scheme.

- The finite internal carrier and the old SPT shortcut are excluded as automatic all-scale ultraviolet regulators.

- The q79 Fu–Yau heterotic route is selected as the primary compatible UV route.

- Fixed-genus UV inheritance is proved conditionally on the exact worldsheet contract.

- The worldsheet frontier is counted explicitly as five available, two partial, and five open rows.

## The shortest honest closure sequence

The remaining work has a dependency order:

1.  **Physical Hull–Strominger endpoints.** Construct the visible and hidden nonpullback holomorphic bundles, common HYM chamber, connections, and local Bianchi/anomaly representative.

2.  **Complete W6–W9.** Promote the global gerbe, all-order background, exact $`(0,2)`$ SCFT, analytic modular characters, GSO projection, and factorization on that same source.

3.  **Instantiate W10–W11.** Build q79-specific string-field/BV vertices and the tadpole, vacuum-shift, infrared, and soft-state completion.

4.  **Connect low and high energy.** Derive the four-dimensional Wilson coefficients, Newton normalization, universal stress response, and selected state from the same compactification.

5.  **Nonperturbative exit.** Establish all-genus control or another well-defined nonperturbative completion, with a positive physical observable sector and comparison map.

The first item controls the rest: without the physical bundles, worldsheet rows cannot all refer to one selected background. The final item cannot be inferred merely by adding more fixed-genus calculations.

# Conclusion

The current MTT quantum-gravity result is substantial but tiered. It supplies an exact internal TT carrier, a conditional Einstein reduction, and fixed-order quantum-GR EFT parity. It also identifies the q79 Fu–Yau heterotic construction as the primary compatible ultraviolet route and proves the correct conditional fixed-genus inheritance statement.

It does not yet supply a UV-complete theory. The former Gaussian shortcut is a conditional Euclidean model, the low-energy quantum theory imports standard EFT quantization after matching its inputs, and the q79 worldsheet contract remains $`5/12`$ with two partial rows. The path forward is therefore not to rename these tiers as closure. It is to construct one physical visible–hidden Hull–Strominger source, complete its worldsheet and BV contracts, derive the low-energy normalization and Wilson data from that same source, and then solve the all-genus or nonperturbative problem.
