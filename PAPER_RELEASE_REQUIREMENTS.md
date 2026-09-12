# MTT Paper Release Requirements

Date: 2026-07-28

## Purpose

This is the release contract for every canonical MTT paper. A paper is not
release-ready merely because its formulas compile or its status claims are
current. It must be understandable, correctly scoped, reproducible, and
packaged without mixing scholarly content with revision administration.

These rules apply to TeX, generated Markdown, PDF, repository metadata, and
Zenodo metadata.

## 1. Expository Content

Every paper must satisfy the eight requirements in
`EXPOSITORY_READABILITY_POLICY.md`:

1. orient the reader to the problem, contribution, imports, and claim tier;
2. explain the central spaces, maps, operators, or numerical objects;
3. give the dependency flow of the argument;
4. interpret each major theorem cluster;
5. provide a concrete example, model, picture, or limiting case where the
   subject permits one;
6. relate the work to its actual MTT dependencies and established context;
7. state assumptions, failure modes, limitations, and the open frontier; and
8. define enough notation and imported contracts for standalone reading.

Human contextual review is mandatory. Automated theorem-density or keyword
scores prioritize review; they do not certify prose quality.

## 2. Theorem Ownership

Every formal result has one canonical owner, following
`THEOREM_OWNERSHIP_AND_STANDALONE_POLICY.md`.

- A paper may explain an imported result, state its hypotheses and conclusion,
  cite its owner, and discuss its paper-specific consequence.
- It must not reproduce another paper's theorem/proof block.
- A new formal result belongs only where it is used as a central contribution.
- Current A/B authority rows control theorem status. Older corpus text is
  historical evidence, not permission to revive a superseded claim.

## 3. Role-Specific Requirements

- **MTT Foundations:** the technical expository reference. It must explain the
  architecture and gates, not merely list them.
- **Fixed Points I--VI:** each paper must be independently readable while
  retaining its distinct theorem role. Proof dependencies may use only local
  arguments, earlier numbered FP installments and standard external
  mathematics. Downstream MTT citations, numerical examples and progress
  ledgers belong outside this foundational series. The generic series
  paragraph is forbidden. Run the foundational-dependency verifier as well
  as the ownership verifier.
- **The Book on Modal Triplet Theory:** a low-mathematics interpretive guide.
  It owns no theorem and must not become a technical ledger.
- **Program and encoding papers:** distinguish representation, reconstruction,
  reduction, selection, and physical derivation.
- **Calculation papers:** explain inputs, algorithm, certification standard,
  result tier, error policy, and what the calculation does not prove.

## 4. Title, Abstract, and Revision Separation

The three objects have different jobs and must never be merged.

### Scholarly title

- Contains the subject of the paper.
- Does not contain `corrected edition`, `revised version`, or similar release
  administration.
- Edition and version belong in the version field or title-page date block.

### Abstract / Zenodo description

- States the problem, method, principal result, claim tier, and scope boundary.
- Contains no correction history, supersession statement, revision-note prose,
  or edition announcement.
- May discuss mathematical or physical correction terms when they are part of
  the subject; it must not describe the manuscript as corrected.

### Revision note

A revised paper carries a separate note after the abstract. It records:

1. `Supersedes`;
2. `Reason`;
3. `Resolution`;
4. `Retained result` or `Retained content`; and
5. `Remaining boundary` or `Open boundary`.

The note explains the version delta. It does not replace the abstract,
introduction, limitations, or conclusion.

## 5. Claims, References, and Evidence

- Every nontrivial claim has its correct tier: exact, conditional, controlled,
  profile/replay, support, interpretive, open, or retired.
- A paper must not silently strengthen a profile match into source selection
  or a finite result into a continuum theorem.
- Imported mathematics and physics receive normal bibliographic citations.
- Computational claims cite the curated results repository and, when
  available, a versioned calculation-capsule DOI.
- Managed computational-evidence blocks are idempotent, paired, and outside
  the abstract.
- Open rows may be cited as open frontiers but never as established results.

## 6. Artifact Quality

Before a paper is marked ready:

1. run the required TeX/BibTeX passes;
2. reject compilation errors, undefined references, and unresolved layout
   warnings;
3. render every PDF page and inspect for clipping, overlap, broken tables,
   bad page breaks, and unreadable text;
4. regenerate `paper.md` and descriptive metadata from canonical TeX;
5. verify source and artifact hashes;
6. before committing, verify that the PDF was rebuilt after every TeX, style,
   and bibliography input; in cloned repositories, where Git does not preserve
   modification times, verify the reviewed TeX, PDF, and source-tree hashes;
7. run the theorem-ownership, Book-role, readability, and repository
   verifiers; and
8. record the human review decision.

## 7. Zenodo Draft Gate

Zenodo synchronization is draft-only. This repository workflow never
publishes.

1. Preview metadata first.
2. Require the canonical title and content-only abstract.
3. Put correction history in Zenodo notes/version fields, not the description.
4. Preserve the concept DOI by creating a new-version draft when a prior
   release exists.
5. Add the canonical paper repository and curated results repository as
   explicit related identifiers.
6. Add relevant external and computational references with their declared
   tiers.
7. Apply managed evidence references to TeX and Markdown before the final PDF
   build.
8. Recompile and visually check the referenced paper.
9. Upload that final PDF and verify the tracked draft id and reserved DOI.
10. Leave publication to explicit manual review by the author.

## 8. Ready-State Definition

A paper is ready only when:

- its review decision is `reviewed` or `reference_ready`;
- all local release checks pass;
- its PDF has been visually inspected;
- its metadata preview has no warning or title/abstract correction leak; and
- it is either an unpublished tracked Zenodo draft or an already published
  current release.

Run:

```powershell
python scripts/verify_paper_release_requirements.py
python scripts/verify_theorem_ownership.py
python scripts/verify_book_interpretive_role.py
python scripts/audit_expository_readability.py --write --strict-boilerplate
python scripts/verify.py
```

When the local research console is available, also run:

```powershell
python scripts/verify_paper_release_requirements.py `
  --publication-api http://127.0.0.1:8791
```

Any failed gate returns the paper to revision. A Zenodo draft is not evidence
that the paper is correct, and a successful calculation process is not theorem
promotion.

## 9. Public-Corpus Exclusions and Release Identity

- A paper marked `matches_latest_release` must have a local `main.pdf` whose
  byte length and Zenodo MD5 checksum equal the latest public Zenodo file.
- A locally newer authoring edition must be assigned a newer version and marked
  `current_source_newer_than_release`; it must never inherit the released
  edition's identity merely because its title is unchanged.
- The commercial book *The Universe Has a Bad Memory*, its `HumanVoicePass`
  source, and companion-site artifacts are outside the MTT scholarly paper
  corpus. They must not appear as paper entries, Zenodo-community records, or
  repository file paths.
- A phrase used incidentally in scholarly prose is not a publication artifact;
  the exclusion concerns the commercial manuscript, title record, source tree,
  and companion application.
