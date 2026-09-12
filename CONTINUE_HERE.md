# Paper Continuation

Current editorial checkpoint: 2026-09-12. Read AGENTS.md and the release requirements first. No Zenodo release is authorized.

## What Is Already Done

- The catalog contains 141 papers, and all 305 curated results have one integration home.
- Flux v6 now preserves the established projective rank-nine hidden carrier and existential HYM connection. The numerical chamber, common visible endpoint and Bianchi data remain separate.
- The cohesive manuscript is now v3: explicit six-row residual, 25-block support,
  conditional character reduction, metric comparison and source-factorization
  imports are integrated. Its isometric-embedding statement is corrected.
  The existing repair/noise/recurrence discussion is retained.
- SM v4 now incorporates all 14 previously confirmed additions. Its finite
  structure, admitted electroweak primitive, Yukawa profiles and precision
  reconstruction survive. The effective 13/19-coordinate ledger is a profile
  count, not independent predictive validation.

## Review Queue, Not Missing Mathematics

`catalog/research-integration-reviews.json` is the manual contextual record. `catalog/research-ownership.json` and per-paper `RESEARCH_INTEGRATION.md` are generated views.

51 result assignments have been reviewed: 46 integrated, one historical
provenance record needing no new theorem, and four additions needed. The other
254 are unreviewed, not known omissions. This pass resolved 15 of the former
19 additions/details and reviewed nine formerly unreviewed assignments.
A literal ID in metadata is not manuscript integration. A missing literal ID
does not prove the mathematics is absent.

Reviews bind LF-normalized manuscript bytes, exact result hashes and real source anchors. Do not refresh a changed hash without reading the change. Generating a new ownership view flags stale reviews; the repository verifier rejects them until reevaluated.

## Next Editorial Work

1. Place the four finite-mode heat-trace/L11/recurrence records in a calculation
   companion. Keep FP III standalone and add only a scoped consumer discussion.
   The current summary and immutable sources are in its integration record.
2. Continue the 254 contextual reviews in the order and clusters recorded in
   EDITORIAL_INTEGRATION_PLAN.md. SM has no remaining assigned imports.
3. Review downstream uses of embedded isometries against the corrected cohesive
   theorem. Cost pullback alone is not reducing operator intertwining.
4. Do not repeat the completed SM/residual edits or treat review counts as
   scientific closure counts. Preserve historical artifacts without importing
   obsolete status fields as current.

The Locality manuscript still needs the author's ontological wording review. Technical examples passing is not author approval.

## Reproduction

Run `python -m unittest discover -s scripts -p test_research_ownership.py` for review-state regression tests, then `python scripts/verify.py` for the paper corpus. After source changes, regenerate Markdown, rebuild and visually inspect every PDF page, and record the reviewed hashes before the verifier.

The public result links are immutable. The ownership generator reads the manifest from the actual specified Git commit, verifies artifact bytes and does not turn current working files into claims about an older public snapshot.

The commercial book and HumanVoicePass source remain excluded. Do not import preserved research branches wholesale; their existence is provenance, not proof promotion.
