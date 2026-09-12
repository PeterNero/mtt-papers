# Fixed Points: Foundational Dependency Repair

The author requires a one-way analytic foundation. FP n may use local results,
earlier FP installments and standard mathematical literature. Other MTT papers
and research calculations may build on this series, never supply its premises.
This overrides the broader standalone policy that permits named MTT imports.

## Scope and Versions

Starting paper commit: `3011fd814701f8cae303af613addbe6654243c77`.

| Paper | Current version | Correction |
|---|---|---|
| I | v7, unchanged | No non-FP MTT import identified; standard analytic sources only |
| II | v6 | Replaces q79 type import with a local tensor-factor example; retains the shared-phase/dimension distinction |
| III | v8 | Removes later finite-mode companion citation; preserves the conditional homogenization framework |
| IV | v7 | Standard universal-connection source, local Hessian transport and two reduction proofs with explicit domains |
| V | v9 | Removes generic computational-evidence assertion and explicitly references the earlier FP sources |
| VI | v7 | Removes the downstream status ledger and q79 carrier imports; retains synthesis and causality results |

## Mathematical Review

FP II still assumes the common vertical operators, gaps and strong commutation.
Its finite rank-flag example follows by diagonal matrix multiplication; it
does not select a physical carrier. No old literal seven-dimensional product
or unproved manifold nesting is restored.

FP III's finite-time example was not a homogenization premise. Removing it
therefore does not remove a proof step. The enhanced path-limit, iterated
integral, corrector and initial-layer assumptions remain explicit.

FP IV attributes universal connections to Narasimhan and Ramanan, *American
Journal of Mathematics* 83 (1961), 563--572,
[doi:10.2307/2372896](https://doi.org/10.2307/2372896).
The isometry is unitary onto the image module, not the whole ambient space.
The same connection, closed domains, quadratic forms and gauge slice must be
transported. No additional ambient harmonic modes are ruled out by this fact.

Its finite-reduction proof solves the complementary block and substitutes it
back into the retained equation. The Feshbach map is an exact spectral
equation, not automatically an autonomous dynamical generator. Its constrained
Hessian proof uses a coercive self-adjoint operator and a bounded finite-target
surjection; the minimizer is in the operator domain and the comparison uses
the quadratic-form domain. The result is a tangent quadratic minimization,
not an unspecified global nonlinear effective action. The 2-by-2 worked
example gives 5/3 by both reductions, compared with bare compression 2.

FP V's formal results and FP VI's two causality propositions are unchanged.
Earlier FP editions are explicitly identified. Historical revision notes are
retained as history; they do not reinstate their removed downstream imports.

## Where the Downstream Material Remains

- The finite-mode recurrence, cubic heat-trace and L11 channel results remain
  in `papers/finite-mode-closure-dynamics-recurrence-and-certified-channel-bounds`.
  That companion remains their unique calculation owner and cites FP III.
- q79 carrier typing, connection-compiler execution and physical endpoint
  progress remain in the research sources, their application papers and the
  Kernel. The old FP VI snapshot at source commit `1615da7` is historical;
  it is not promoted back into a live status authority.
- The exact pre-edit text remains available at the starting paper commit.
  Removal from the foundational PDFs is not deletion or demotion of those
  results, nor permission to duplicate them in a new foundational theorem.

## Regression Guard

`catalog/fp-foundational-dependencies.json` records reviewed bibliography
identities, standard sources and the allowed earlier-FP edges. The new
verifier rejects later/self edges, unknown citations, downstream repository
imports and changed bibliography bytes requiring renewed review. It also
checks for unreviewed external TeX inputs. Tests include reference-key reuse
and the finite-reduction arithmetic. It does not infer the validity of an
uncited proof premise; contextual review remains necessary.

## Validation and Kernel Scope

The five revised PDFs built successfully with no reported PDF build warnings:
FP II 13 pages, III 10, IV 10, V 9 and VI 10. All 52 pages were rendered and
visually inspected; FP IV's two reduction-proof pages were rechecked at full
size. Markdown and catalog metadata were regenerated and reviewed artifact
hashes frozen. Pandoc reports the existing benign series.sty macro warning;
it is distinct from the clean PDF build.

The 11 focused FP regression tests and the 142-paper repository verifier pass.
There are zero duplicate theorem-body groups and zero forbidden series
declarations. The guard verifies reviewed citation direction, not every
uncited mathematical premise or the whole theory anew.

Kernel reconciliation C.FP.03 now covers the six foundational installments.
The downstream C.FP.01 physical bridge remains open in its application papers.
Later numerical and physical-source results are no longer suggested as FP
prerequisites; their owner papers and all scientific blocker states survive.
Nineteen Kernel corpus-completion regression tests pass with this distinction.

No Zenodo upload or publication was performed. These are current unreleased
authoring versions, not claims that existing published PDFs have changed.
