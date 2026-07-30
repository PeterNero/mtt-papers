# Fixed Points IV v6 Release Audit

## v6 publication delta (July 2026)

- **Supersedes:** v5.
- **Reason:** three distinct meanings of finite data and two distinct
  curvature effects needed explicit explanation.
- **Resolution:** add the finite-module, Galerkin, and invariant-reduction
  guide while retaining all formal statements.
- **Retained:** the v5 curved-cluster, leakage, modulation, barrier, and
  Feshbach/reduced-Green results.
- **Remaining:** selected physical HYM and finite-reduction source data.

## v5 delta (July 2026)

The v5 update consumes the canonically verified
`mtt-qm-source-proof` head `1615da7` and extends FP IV exactly where its
curved-projector analysis meets the q79 continuum/finite interface.

| New result | v5 action |
|---|---|
| Universal connection/projective-module naturality is closed | Adds exact transport of the supplied connection, curvature, coupled differential, and functorial Hessian |
| A smooth finite matrix projector is not a finite Fourier or Galerkin cutoff | Adds the explicit matrix-size versus mode-cutoff distinction |
| The Cech compiler requires a connection correction | States that the projector alone generally carries the Grassmann connection, not the physical HYM connection |
| `PHP` is exact precisely when `QHP=0` | Adds the invariant-subspace criterion |
| Nonzero `QHP` requires complementary-sector elimination | Adds the exact Feshbach-Schur operator and identifies its self-energy as same-source data |
| The six-coordinate strain carrier is nonlinear | Adds the reduced-Green shorted Hessian `(J G_Q J*)^{-1}` and its variational proof |
| Universal contracts are closed but the actual q79 diagram remains `0/3` | Leaves endpoint, action, physical Hessian, finite-subspace, and execution rows open |

The update also corrects two TeX transcription errors in the leakage formulas:
`\quad` and `\sup` are restored. No numerical physical result is promoted.

## Prior v4 correction retained

## Source lineage

- Source: `_work/Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v3`
- Revised: `revised_tex_vnext/Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v4`
- The v3 project remains untouched.

## Required corrections evaluated

| Finding | v3 evaluation | v4 action |
|---|---|---|
| Normalize the Weitzenbock decomposition | The rough Laplacian and full curved operator were identified inconsistently | Defines `L=nabla* nabla+R`, with the rough Laplacian nonnegative and `R` a self-adjoint curvature endomorphism |
| Separate curvature shift, mixing, and variation | These effects were treated as one scalar correction | Separates the negative spectral part of `R`, the off-diagonal block `QRP`, and base derivatives/commutators |
| Prove a gap for the full curved operator | The uncurved gap was reused after adding curvature | Proves cluster persistence under `||R||<lambda_*/2` and defines the curved Riesz projector `P_R` |
| Distinguish `P` from `P_R` | The old coherent projector was silently retained | States that `P_R` is the invariant curved projector; retaining `P` creates explicit curvature leakage |
| Include coherent-to-noncoherent leakage | The `QRP` source term was absent | Derives a `Q`-sector differential inequality with leakage coefficient `ell_QP=||QRP||` and its induced floor |
| Make the centroid intrinsic | Coordinate averaging is not invariant on a manifold | Defines the Karcher centroid in a strongly convex normal ball and states uniqueness assumptions |
| Match modulation order to the parent flow | A Newton equation was claimed from first-order gradient flow | Derives a first-order metric modulation equation; second-order motion is conditional on a separately specified inertial parent equation |
| Do not infer interaction sign from overlap magnitude | An absolute overlap estimate was promoted to attraction/merger | Proves only `|E_int|<=C O` without sign data |
| State the extra sign hypothesis | Attraction and repulsion were not separated | Gives a signed interaction criterion based on the sign of the cross term |
| Replace the schematic barrier claim | The previous transition statement did not supply a precise energy/work hypothesis | Gives a mountain-pass/work exclusion theorem with an explicit barrier and accumulated work |
| Separate exit from basin selection | Threshold exit was treated as selecting the next structure | Proves that exit detection alone does not determine the post-transition basin |

## Additional corrections

- The rank of the low curved spectral cluster is preserved by the Riesz
  projector homotopy while the contour remains in the resolvent set.
- The leakage theorem states its nonlinear one-sided constant and the required
  positive margin instead of appealing to curvature-corrected damping
  informally.
- Base-dependent projectors are accompanied by a commutator/connection term;
  differentiating `P_R(x)` is not treated as free.
- Fixed-point existence and promotion to equilibrium are inherited only under
  the corrected FP I/II hypotheses.
- Overlap remains a useful magnitude diagnostic, but dynamic merger requires
  both sign information and a specified evolution law.

## Resulting scope

FP IV v5 proves perturbative persistence of the selected low spectral cluster,
quantifies curvature-induced leakage when the old projector is retained, and
gives intrinsic first-order centroid modulation for the gradient-flow model.
It additionally proves the exact projective-transport and
compression/Feshbach/shorted-Hessian boundary for supplied source data. It does
not claim that the finite presentation selects the physical q79 endpoint,
Hessian, or post-transition state.

## Expository revision

The current paper now includes a paper-specific reader guide built around the
two curvature blocks and the three different meanings of "finite." New
discussion explains:

- why persistence of a low cluster does not preserve the old coherent states;
- why projective-module transport is not a Galerkin cutoff;
- when bare compression, Feshbach reduction, and reduced-Green shorting apply;
- why a positive leakage floor can reflect projector misalignment rather than
  instability;
- why Karcher-centroid motion is first order for the chosen parent flow;
- why barrier exclusion, exit detection, and basin selection are separate.

The conclusion now gives a practical decision tree and the exact q79
instantiation data still required. No theorem from FP I--III or FP V--VI was
duplicated.

## Validation

- The canonical `mtt-qm-source-proof` verifier passes at commit `1615da7`.
- The 139-paper repository verifier passes after Markdown and hash regeneration.
- The current source compiles with `pdflatex` to an 8-page PDF.
- The final log has no undefined references, underfull boxes, overfull boxes,
  or LaTeX/package warnings.
