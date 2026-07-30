# Zenodo Draft Release Readiness

Date: 2026-07-28

Final live verification: 2026-07-28 23:32 UTC

## Decision

The reviewed release set is **not yet safe to publish**.

The local paper and metadata gates pass for all 30 reviewed candidates. The
Zenodo metadata is also current for all 30 tracked drafts. The remaining
failure is entirely at the remote file layer:

- 29 drafts contain exactly one older PDF and no exact copy of the reviewed
  local PDF;
- the Book on MTT draft contains no PDF;
- therefore 0 of 30 drafts currently pass the exact remote-PDF checksum gate.

The machine-readable per-paper result, including every draft ID and local MD5
and SHA-256 value, is
`catalog/zenodo-draft-readiness.json`.

## Gates that pass

1. All 30 candidates have a recorded expository review.
2. Every reviewed canonical TeX and PDF matches its frozen review hash.
3. Every local PDF is present, nonempty, and no older than its TeX, style, or
   bibliography inputs.
4. Zenodo titles and descriptions match the current canonical metadata.
5. Zenodo descriptions contain no raw TeX commands or math delimiters.
6. Correction and version history is kept out of titles and descriptions and
   remains in notes or the paper's separate revision note.
7. The rejected generic Fixed Points series declaration is absent from the
   reviewed paper sources and publication descriptions.
8. Fixed Points I, the Temporal Bell paper, and Program D2 now have distinct
   successor drafts:

   - Fixed Points I v7: draft 21657157
   - Temporal Bell v3: draft 21657161
   - Program D2 v2: draft 21657167
9. The refreshed Kernel publication API sees all 140 canonical papers and
   passes its release-requirement preview for all 30 reviewed drafts.
10. The local Zenodo release inventory has been reconciled with the three
    latest public records that arrived after the prior cache was built.

No draft was published.

## Remote file blocker

Three supported upload routes were tested on the Book draft, with a second
draft used to confirm that the failure was not Book-specific:

1. The Zenodo bucket PUT route returned HTTP 400 with
   `The file upload transfer failed, please try again.`
2. The documented legacy deposition-file multipart route returned the same
   HTTP 400 transfer failure.
3. The current draft-file content/commit route initialized correctly but the
   content PUT returned HTTP 504; Zenodo then removed the incomplete pending
   entry.

The synchronization code uploads a uniquely named candidate first, verifies
its MD5, and only then deletes an older PDF. Consequently no existing PDF was
deleted during these failures.

A final Book-only retry at 23:32 UTC reproduced the same transfer failure on
all three routes. The Book draft still contains zero files, with no incomplete
pending upload left behind.

## Publication exit condition

Do not press Publish until both commands pass:

```powershell
python scripts\verify_paper_release_requirements.py
python scripts\zenodo_draft_readiness.py verify `
  --report catalog\zenodo-draft-readiness.json
```

When Zenodo file storage is responsive again, synchronize and verify with:

```powershell
python scripts\zenodo_draft_readiness.py sync
python scripts\zenodo_draft_readiness.py verify `
  --report catalog\zenodo-draft-readiness.json
```

The synchronization command never invokes a Zenodo publish action.
