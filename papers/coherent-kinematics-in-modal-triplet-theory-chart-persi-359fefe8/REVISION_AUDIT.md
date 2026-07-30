# Coherent Kinematics v2 Revision Audit

## Source lineage

- Source: `_work/Coherent_Kinematics_in_Modal_Triplet_Theory`
- Revised: `revised_tex_vnext/Coherent_Kinematics_in_Modal_Triplet_Theory_v2`
- The original project remains untouched.

## Retained core

The useful conceptual core survives:

- Position is relative to a declared effective chart and localization
  diagnostic.
- One upper carrier can be represented through multiple compatible charts.
- Compatible chart curves define an encoding trajectory or worldline
  equivalence class.
- Loss of a chart can terminate a particular encoding without destroying the
  upper object.

These are now stated as encoding-level kinematics rather than physical causal
theorems.

## Required corrections

| Finding | Original status | v2 action |
|---|---|---|
| Configuration space written as `Y_4 x B_1 x B_2 x B_3` | Conflicted with canonical geometry and risked dimension double-counting | Uses a typed upper state space; physical `Y_4` appears only in the selected physical bridge |
| Charts used without a factor-through condition | Transition map could be ill-defined | Requires the Projection-Admissibility descent criterion on overlaps |
| Chart compatibility described only qualitatively | No gluing theorem | Adds transition identity/cocycle hypotheses and proves quotient-curve gluing |
| Position treated as any invariant functional | Regularity and domain under-specified | Types the support class, target, covariance, and regularity of each localization map |
| Coordinate centroid used generically | Not intrinsic | Refers to the FP IV Karcher-mean conditions |
| Motion inferred from chart chains alone | No underlying path | Requires an actual upper path and an interval/chart cover |
| Contractivity said to imply continuity | False without map/path regularity | Proves Lipschitz encoding only from a Lipschitz upper path, charts, transitions, and localization maps |
| Null/timelike classes inferred from admissibility directions | No physical metric or principal symbol | Defines causal class only in the selected Lorentzian realization |
| No-superluminal theorem inferred from chart admissibility | Circular | Uses a conditional finite-domain-of-dependence theorem for the selected physical PDE |
| Chart partial order promoted to causal/temporal order | Unsupported | Explicitly separates descriptive order, physical causal order, and stabilization order |
| Coincident support used to motivate exclusion principles | Noninjectivity prevents the inference | States that support coincidence does not prove identity or exclusion |
| Merge identified with physical coalescence | No interaction or dynamical connection | Defines only effective merger as noninjectivity of a descended map |
| Split automatically generated branches/worldlines | A deterministic map is single-valued | Requires refined, multivalued, stochastic, or hybrid continuation data |
| Merge/split used to derive irreversibility and an arrow | Depended on the withdrawn right-inverse obstruction | Removes the claim; temporal arrows need a physical asymmetric theorem |
| Horizon said to terminate worldlines | False for regular horizon crossing | Distinguishes exterior chart/decoder failure from geodesic incompleteness and PDE breakdown |
| QM, photons, QFT, and cosmology treated as automatic examples | Missing physical constructions | Reclassifies them as possible later instantiations |
| Duplicate `end{document}` | Source error | Leaves exactly one document terminator |

## Resulting theorem chain

1. Compatible charts satisfying descent and cocycle conditions form an
   effective atlas.
2. An upper path represented through that atlas defines an encoding worldline.
3. Explicit Lipschitz hypotheses imply a regular encoding trajectory.
4. A selected hyperbolic physical PDE plus principal-symbol/locality descent
   gives conditional causal support propagation.
5. Effective merger, split, exterior decoding, and physical termination remain
   separately typed.

## Resulting scope

The paper establishes chart-persistence kinematics and a conditional bridge to
physical support propagation. It does not derive a metric, null cone, physical
time, particle identity, exclusion principle, measurement outcome, merger,
split probability, horizon entropy, or temporal arrow.

## Validation

- Coherent Kinematics v2 permanent theorem audit passes.
- Foundation v7, Projection-Admissibility v2, Signature Stability v2, Baseline
  Scales v2, and all six Fixed Points audits continue to pass.
- Migration and verifier scripts pass Python syntax validation.
- TeX environment nesting, ASCII/tab guards, and the single-document-terminator
  check pass.
- The current source compiles successfully with two `pdflatex` passes.
- The complete PDF is rendered and visually inspected before release freeze.
