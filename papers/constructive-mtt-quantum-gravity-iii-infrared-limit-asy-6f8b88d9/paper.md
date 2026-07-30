---
abstract: |
  This paper separates a massive or infrared-regulated scattering benchmark from the physical massless-graviton problem in Modal Triplet Theory quantum gravity. A positive transverse-traceless mass gap does not describe the physical massless graviton, and finite-volume Gaussian and BRST results do not by themselves construct the local Lorentzian theory required by Haag–Ruelle scattering. The paper proves the operator statement that for isometric incoming and outgoing wave operators, the scattering operator is only a contraction in general and is unitary exactly when their ranges coincide. It also proves that a normalized SPT factor leaves the leading massless soft pole unchanged. Standard massive Haag–Ruelle theory is retained as a conditional benchmark after its full axioms are supplied. The physical gravity route instead requires a selected Lorentzian BRST theory, asymptotic null geometry, soft-charge control, dressed states or inclusive observables, infrared-regulator removal, and an appropriate completeness theorem. Current MTT data do not yet provide that packet. The paper therefore supplies a precise infrared dependency theorem and executable exit contract, not a unitary MTT gravity S-matrix.
author:
- Peter Nero
current_version: v2
date: July 2026 Version 2
generated_from_main_tex_sha256: 9f6b8bccdc0a55542088280f6900b4d1419f65d0403d7a8742b08d0f865876b8
paper_id: constructive-mtt-quantum-gravity-iii-infrared-limit-asy-6f8b88d9
release_state: zenodo_released
released_version: v2
title: |
  Constructive MTT Quantum Gravity III:
  A Massive Scattering Benchmark and the Massless-Graviton Infrared Contract
zenodo_doi: 10.5281/zenodo.21665958
zenodo_record_id: 21665958
zenodo_url: "https://zenodo.org/records/21665958"
---

# Version 2 Revision Note

Supersedes:
Constructive MTT Quantum Gravity III, first release.

Reason:
A positive TT gap, isometric wave operators, and SPT damping were promoted beyond what they imply for massless gravitational scattering.

Resolution:
Massive Haag–Ruelle theory is retained only as a conditional benchmark; the exact wave-operator range criterion and SPT infrared-neutrality result replace the former closure claim.

Retained result:
Isometric wave operators give a contraction that is unitary exactly when their ranges coincide.

Remaining boundary:
Lorentzian BRST dynamics, null asymptotics, soft charges, dressed or inclusive states, regulator removal, and completeness remain open.

# Correction, purpose, and result map

The first edition relied on the chain
``` math
\begin{aligned}
 \text{SPT damping}
 &\Longrightarrow \text{gapped TT scattering}\\
 &\Longrightarrow \text{isometric wave operators}\\
 &\Longrightarrow \text{unitary gravitational }S\text{-matrix}.
\end{aligned}
```
Every arrow was too strong. SPT is an ultraviolet spectral filter and does not remove the massless soft pole. A positive TT gap changes the infrared theory. The earlier papers did not construct the complete Lorentzian local net on which scattering theory acts. Finally, isometric wave operators need not have the same range, so their overlap need not be unitary.

This paper preserves the useful question but separates two branches:
``` math
\boxed{\text{massive benchmark}}
\qquad\hbox{and}\qquad
\boxed{\text{physical massless-graviton contract}}.
```
Section 3 identifies the errors in the old promotion. Section 4 states the standard massive benchmark without claiming that MTT has supplied its hypotheses. Section 5 proves the exact range criterion for scattering unitarity. Section 6 replaces the massive shortcut by the correct soft-gravity research contract. The final sections locate that contract in the present q79 program and record the remaining objects.

## The central picture in plain language

Scattering compares what a system looks like in the far past with what it looks like in the far future. The maps $`\Omega_{-}`$ and $`\Omega_{+}`$ embed those two asymptotic descriptions into the interacting physical state space. Preserving norms says that neither embedding loses probability. It does not say that the two embeddings cover the same interacting states. Unitarity of the scattering operator requires precisely that additional range statement.

For a massive local field, separated wave packets eventually move apart and the Haag–Ruelle construction can exploit an isolated mass shell. Gravity has a different infrared geometry. Its carrier is massless, its interaction is long-ranged, and arbitrarily low-energy gravitons correlate the hard particles with a soft cloud. The physical question is therefore not whether an ultraviolet Gaussian factor makes a massive proof converge. It is whether MTT selects the correct dressed or inclusive asymptotic object and proves its infrared limits.

# What the current MTT results actually supply

The current MTT quantum-gravity ledger contains several relevant but logically earlier results:

1.  a finite q79 internal TT operator and a positive free two-helicity block at their declared finite-carrier tier;

2.  a conditional reduction to the two-derivative Einstein/TEGR tensor shape on an explicitly selected branch;

3.  fixed-order quantum-GR effective-field-theory parity after the renormalized action, Wilson coefficients, state, scale, gauge fixing, and scheme are declared; and

4.  corrected finite-volume SPT Gaussian and conditional BRST/BV interface theorems.

These are useful compatibility data. They do not yet emit a normalized Lorentzian graviton field, a nonperturbative physical state space, a local observable net, or asymptotic wave operators. In particular, the eigenvalues of the finite internal TT Hessian are not automatically the invariant masses of a Poincare representation. An explicit bridge from the internal carrier to the four-dimensional Lorentzian spectrum is required before the word *mass gap* has its scattering-theory meaning.

The corrected predecessor papers also change what Part III may inherit. Constructive QG I proves a bounded-volume Gaussian measure and a finite-mode quartic Borel theorem, not an interacting gravity continuum. Constructive QG II proves conditional BRST/BV interfaces, not a completed physical Hilbert space. This paper therefore cannot begin by assuming those missing endpoints have already been constructed.

# Why the old scattering proof fails

## A finite slab is not an asymptotic region

<div class="proposition">

**Proposition 1** (Finite-slab obstruction). *Let a dynamics be defined only for $`t\in[T_-,T_+]`$ with both endpoints finite. Then limits whose definition requires $`t\to\pm\infty`$ are not defined by that finite-slab dynamics. A scattering construction needs either a global dynamics or a controlled exhaustion in which the slab endpoints tend to infinity.*

</div>

<div class="proof">

*Proof.* The nets $`t\mapsto U(t)`$ and the comparison maps used in a wave-operator limit must be evaluated for arbitrarily large positive or negative $`t`$. A function defined only on a bounded interval has no such directed tail. Introducing a sequence of larger slabs creates a second limit, whose existence and independence must be proved rather than inferred from any one slab. ◻

</div>

The old definition of asymptotic flatness also included the existence of Moller operators among the assumed consequences. Using that definition to prove the same operators exist was circular. Geometric falloff, spectral assumptions, propagation estimates, domains, and the wave-operator limits must be stated as separate inputs.

## A positive TT gap is not the physical graviton

The massless graviton has a lightlike one-particle shell. Assuming that the physical spectrum starts above a strictly positive mass $`\mu`$ removes that shell. Such an assumption can define a useful massive model, finite-volume approximation, or infrared regulator, but its regulator-removal limit is an additional theorem. It cannot be called the infrared completion of massless gravity.

This distinction also prevents an ambiguity in Constructive QG I. Its parameter $`m^2>0`$ makes the Euclidean bounded-volume covariance invertible. It was explicitly introduced as an infrared shift, not selected as a physical graviton mass.

## SPT smoothing does not remove the soft pole

<div id="prop:ir-neutral" class="proposition">

**Proposition 2** (Infrared neutrality of a normalized SPT filter). *Let $`F:[0,\epsilon)\to\mathbb R`$ satisfy $`F(u)=1+O(u)`$ as $`u\downarrow0`$. Then
``` math
\frac{F(p^2)}{p^2}=\frac1{p^2}+O(1)
 \qquad (p^2\downarrow0).
```
In particular, multiplying a massless propagator by such an SPT factor does not remove its leading soft pole.*

</div>

<div class="proof">

*Proof.* Write $`F(u)=1+u r(u)`$ with $`r`$ bounded near zero. Division by $`u=p^2`$ gives $`F(u)/u=1/u+r(u)`$. ◻

</div>

For the proper-time form
``` math
F(u)=\int_0^\infty e^{-tu}\,d\mu(t),
```
normalization is $`F(0)=\mu([0,\infty))=1`$. If the first moment of $`\mu`$ is finite, then $`F(u)=1-u\int t\,d\mu(t)+o(u)`$, so Proposition <a href="#prop:ir-neutral" data-reference-type="ref" data-reference="prop:ir-neutral">2</a> applies directly. The filter can strongly change high momentum while leaving the leading infrared singularity intact.

## Euclidean decay is not Lorentzian locality

Rapid decay of a Euclidean covariance does not by itself construct microcausal Lorentzian observables. A nonpolynomial function of a Laplacian is generally nonlocal. The old proof used the Gaussian multiplier both to improve decay and to assume the strict locality needed by Haag–Ruelle theory. A future construction must instead prove that its physical observable algebra has the required commutation or almost-locality properties after continuation and BRST reduction.

# The valid massive benchmark

The corrected massive statement belongs to standard local quantum field theory. It is retained because it gives a clean test that a future MTT Lorentzian construction may attempt to satisfy in a genuinely massive sector.

<div id="thm:massive" class="theorem">

**Theorem 3** (Conditional massive Haag–Ruelle benchmark). *Suppose a theory on Minkowski spacetime is supplied with a local, translation-covariant observable net on a positive Hilbert space, a unique vacuum, the spectrum condition, and an isolated stable one-particle mass hyperboloid separated from the remaining spectrum as required by Haag–Ruelle theory. Then the Haag–Ruelle limits define incoming and outgoing multi-particle isometries from the corresponding asymptotic Fock space into the physical Hilbert space. A unitary scattering operator follows only after the relevant incoming and outgoing ranges are proved equal.*

</div>

<div class="proof">

*Proof.* The existence and isometry statement is the standard Haag–Ruelle theorem . The final sentence follows from Theorem <a href="#thm:range" data-reference-type="ref" data-reference="thm:range">4</a> below. ◻

</div>

This is a conditional benchmark, not a new construction of the stated net. It also does not apply directly to the massless graviton. Refined Haag–Ruelle methods can construct stable massive particles in theories that also contain massless excitations under additional regularity assumptions ; this still does not turn the graviton itself into an isolated massive particle.

# What wave operators actually prove

<div id="thm:range" class="theorem">

**Theorem 4** (Wave-operator range criterion). *Let $`\Omega_{-},\Omega_{+}:\mathcal H_{\mathrm{as}}\to\mathcal H_{\mathrm{phys}}`$ be isometries and define
``` math
S=\Omega_{+}^{*}\Omega_{-}:\mathcal H_{\mathrm{as}}\to\mathcal H_{\mathrm{as}}.
```
Then $`\|S\|\leq1`$. Moreover,
``` math
S^{*}S=I
 \quad\Longleftrightarrow\quad
 \mathop{\mathrm{Ran}}\Omega_{-}\subseteq\mathop{\mathrm{Ran}}\Omega_{+},
```
and
``` math
SS^{*}=I
 \quad\Longleftrightarrow\quad
 \mathop{\mathrm{Ran}}\Omega_{+}\subseteq\mathop{\mathrm{Ran}}\Omega_{-}.
```
Consequently $`S`$ is unitary exactly when $`\mathop{\mathrm{Ran}}\Omega_{-}=\mathop{\mathrm{Ran}}\Omega_{+}`$.*

</div>

<div class="proof">

*Proof.* Let $`P_\pm=\Omega_\pm\Omega_\pm^*`$ be the orthogonal projections onto the closed ranges of the two isometries. Then
``` math
S^*S=\Omega_{-}^*P_+\Omega_{-},\qquad
 SS^*=\Omega_{+}^*P_-\Omega_{+}.
```
Since orthogonal projections are contractions, so is $`S`$. The first expression equals the identity precisely when $`P_+\Omega_{-}=\Omega_{-}`$, which is the first range inclusion. The second is analogous. Both identities hold exactly when both inclusions hold. ◻

</div>

#### Concrete foothold.

Take $`\mathcal H_{\mathrm{as}}=\mathbb C`$, $`\mathcal H_{\mathrm{phys}}=\mathbb C^2`$,
``` math
\Omega_{-}z=(z,0),\qquad
 \Omega_{+}z=(\cos\theta\,z,\sin\theta\,z).
```
Both maps are isometries, but $`S z=\cos\theta\,z`$. Unless the two ranges coincide, $`S`$ is not unitary. This one-dimensional example isolates the gap in the first edition: norm preservation of each asymptotic embedding is not asymptotic completeness.

For conventional scattering theory, wave operators are often described as partial isometries on their initial subspaces. That terminology does not repair the missing range theorem. In the present same-domain formulation, $`\Omega_{+}^*\Omega_{-}`$ is guaranteed to be a contraction; it need not itself be a partial isometry for arbitrary relative ranges.

# The physical massless-graviton route

## Why ordinary Fock scattering is insufficient

Long-range interactions do not switch off in the same way as short-range massive interactions. In perturbative gravity, virtual and real soft gravitons produce infrared structures already analyzed by Weinberg . A naive hard-particle Fock state omits the correlated soft gravitational field. Perturbative constructions therefore use either inclusive observables, in which unresolved soft radiation is summed, or appropriately dressed asymptotic states. Faddeev–Kulish methods originated in QED ; a gravitational implementation constructs an asymptotic dynamics and coherent soft clouds .

These approaches are meaningful precedents, not results automatically owned by MTT. They also carry choices and hypotheses concerning gauge invariance, soft charges, asymptotic symmetries, factorization, and the class of observables. Modern dressed-state analyses make explicit that hard and soft sectors are correlated .

## Two legitimate output types

A corrected MTT infrared program may target either of the following:

Inclusive output.
Infrared-safe transition probabilities or detector observables after summing over experimentally unresolved soft gravitons, with the resolution prescription and regulator removal declared.

Dressed output.
A physical asymptotic state space whose hard states are accompanied by the selected soft gravitational dressing, together with well-defined incoming and outgoing maps and their range theorem.

The two descriptions may agree on suitable observables, but they are not identical data structures. A paper must declare which one it constructs.

## Selected MTT infrared exit contract

For a physical MTT gravity scattering theorem, the following objects must come from one compatible source chain:

1.  **Lorentzian theory.** A selected gauge-invariant action or observable net, a gravitational BRST/BV construction, a physical state, and controlled continuation from any Euclidean input.

2.  **Massless spectrum.** A normalized two-helicity massless graviton sector with a proved map from the finite q79 TT carrier to the Lorentzian Poincare or asymptotic representation.

3.  **Asymptotic geometry.** A declared asymptotically flat spacetime or null-infinity structure, with dynamics defined for arbitrarily large times. Falloff assumptions must not include the desired wave operators.

4.  **Soft data.** Soft charges, memory sectors, and the action of large gauge or asymptotic symmetries on the physical observables.

5.  **Infrared prescription.** Either an inclusive resolution map or a selected dressed-state construction, including gauge/BRST compatibility.

6.  **Removal theorem.** Independence of auxiliary graviton masses, finite volumes, adiabatic switches, and soft-energy cutoffs in the declared observable topology.

7.  **Scattering ranges.** Incoming and outgoing maps, the range relations of Theorem <a href="#thm:range" data-reference-type="ref" data-reference="thm:range">4</a>, and the chosen completeness statement.

The first edition did not supply these seven objects. Importantly, SPT damping does not close item 4 or 5: by Proposition <a href="#prop:ir-neutral" data-reference-type="ref" data-reference="prop:ir-neutral">2</a>, its normalized ultraviolet factor leaves the leading soft pole unchanged.

# Relation to the q79 heterotic route

The selected compatible ultraviolet candidate in the current MTT program is the q79 Fu–Yau heterotic branch, not the SPT filter by itself. That route could eventually constrain the massless spectrum, BRST data, and interactions entering item 1 and item 2 of the exit contract. At present its worldsheet contract has five rows available, two partial, and five open. In particular, the exact worldsheet theory, complete BV vertices, tadpole/vacuum control, infrared and soft completion, and all-genus/nonperturbative definition are not yet available.

Fixed-genus string amplitudes also do not automatically solve the four-dimensional asymptotic problem. One must identify the physical four-dimensional states, take the relevant compactification and low-energy limits, and establish the soft/inclusive or dressed prescription in that sector. The heterotic route is therefore compatible with the contract above, but it has not yet discharged it.

# Status ledger

<div class="center">

| Object | Status | Meaning |
|:---|:---|:---|
| Massive Haag–Ruelle theorem | Imported benchmark | Applies after a local positive theory with the required isolated mass shell is supplied. |
| Finite q79 TT carrier | Available at finite tier | Not yet a Lorentzian mass-shell or asymptotic-state theorem. |
| SPT finite-volume Gaussian | Available conditionally | Controls a Euclidean ultraviolet model; leaves the leading massless soft pole intact. |
| Gravitational BRST/BV state space | Open | Corrected QG II gives interfaces, not the selected quantum measure or physical completion. |
| Massless graviton dressing or inclusive map | Open | No selected MTT soft-sector operator has been emitted. |
| IR-regulator removal | Open | No uniform physical limit for mass, volume, switching, and soft cutoffs is proved. |
| Wave-operator range equality | Open | Isometries alone do not imply a unitary scattering operator. |
| Physical MTT gravity $`S`$-matrix | Open | Requires the complete seven-object contract. |

</div>

# Version delta

Relative to version 1, this successor:

- withdraws the claim that the three constructive papers complete nonperturbative MTT quantum gravity;

- reclassifies the positive-gap argument as a massive or infrared-regulated benchmark;

- removes the circular definition that assumed Moller operators inside asymptotic flatness;

- distinguishes finite slabs from the infinite-time limit needed for scattering;

- proves the exact wave-operator range criterion and corrects the claim that isometries alone make the $`S`$-matrix unitary;

- proves that a normalized SPT factor leaves the massless soft pole unchanged;

- replaces the naive graviton Fock-space conclusion by inclusive and dressed alternatives; and

- states the seven-object MTT infrared exit contract.

# Conclusion

The corrected result is sharp. Standard massive Haag–Ruelle theory remains a valuable benchmark, but a positive graviton mass gap is not the infrared physics of our universe. SPT smoothing is ultraviolet data and, when normalized at zero momentum, does not cure the massless soft singularity. Even after incoming and outgoing isometries exist, unitarity requires equality of their ranges.

What MTT has achieved here is therefore not a completed gravity $`S`$-matrix. It has a finite TT carrier, a conditional Einstein reduction, fixed-order EFT parity, and now a corrected map of the infrared problem. The next genuine advance is to construct one selected massless soft-sector packet: Lorentzian physical states, asymptotic charges, a dressing or inclusive prescription, and its regulator-removal and range certificates. That packet would connect the current finite q79 structure to physical gravitational scattering without hiding the long-range problem behind an artificial mass gap.

#### Open boundary (not evidence of closure).

- (*open*).

  Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.

<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->
# Computational Evidence and Reproducibility

The massive benchmark and massless infrared obligations are separated within this paper. The mapped open strict-upgrade row does not close the massless-graviton limit and is cited only as an adjacent unresolved source obligation.

The referenced rows are frozen to the curated results repository at commit `31247ebb5c22f3fbb5443024365433c6ee0bff4a`. The [immutable result manifest](https://github.com/PeterNero/mtt-results-repro/blob/31247ebb5c22f3fbb5443024365433c6ee0bff4a/release/result_manifest.json) has SHA-256 `fb39968960b00584631dbf531a708e18ef928d6b6d935119c185d7f632b1e7cd`.

Tier labels are quoted verbatim from that manifest. A row used directly supports only the specific computational statement identified above; a corpus-state cross-check does not prove this paper's local theorems; and an open row is evidence of an unresolved obligation, never of closure.

## Open boundary (not evidence of closure)

- `A05/strict_upgrade_ledger` (**OPEN**): Current 2/9 strict no-knob upgrade ledger.

No imported row changes theorem ownership or promotes a neighboring claim: all local statements retain their stated hypotheses, domains, and limitations.
<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->

<div class="thebibliography">

99

D. Ruelle, *On the asymptotic condition in quantum field theory*, Helv. Phys. Acta **35** (1962), 147–163.

R. Haag, *Local Quantum Physics*, 2nd ed., Springer, 1996.

W. Dybalski, *Haag–Ruelle scattering theory in presence of massless particles*, Lett. Math. Phys. **72** (2005), 27–38, doi:10.1007/s11005-005-2294-6.

S. Weinberg, *Infrared photons and gravitons*, Phys. Rev. **140** (1965), B516–B524, doi:10.1103/PhysRev.140.B516.

P. P. Kulish and L. D. Faddeev, *Asymptotic conditions and infrared divergences in quantum electrodynamics*, Theor. Math. Phys. **4** (1970), 745–757, doi:10.1007/BF01066485.

J. Ware, R. Saotome, and R. Akhoury, *Construction of an asymptotic S matrix for perturbative quantum gravity*, JHEP **10** (2013), 159, doi:10.1007/JHEP10(2013)159, arXiv:1308.6285.

S. Choi and R. Akhoury, *Subleading soft dressings of asymptotic states in QED and perturbative quantum gravity*, JHEP **09** (2019), 031, arXiv:1907.05438.

</div>
