# Modal Triplet Theory Papers

This is the canonical source repository for the Modal Triplet Theory paper
corpus. Papers are stored in one flat namespace under `papers/`; the former
numbered topic groups are not part of the repository model.

Each paper directory contains:

- the complete current TeX source project, with `main.tex` as entry point;
- `paper.md`, generated from that exact TeX entry point with Pandoc;
- `metadata.json`, including version, hashes, migration lineage and Zenodo data;
- source-side bibliography, style and media files required by the project.

The current authoring edition and latest public release are separate fields.
This matters when a corrected local TeX edition is newer than the edition
already released through the [MTT Zenodo community](https://zenodo.org/communities/mtt/records).

## Layout

```text
papers/<stable-paper-id>/
  main.tex
  paper.md
  metadata.json
  ...supporting source files

catalog/papers.json
catalog/zenodo-records.json
catalog/unmatched-zenodo-records.json
CATALOG.md
```

Zenodo records without a recoverable local TeX project are listed separately in
`CATALOG.md`; the migration never invents TeX source from a released PDF.

The old grouped tree remains migration provenance only. New paper work should
begin here and update an existing stable paper directory rather than create a
new topical group.

Projects listed under `native_projects` in `config/migration.json` are authored
directly in this flat repository and are preserved when the legacy corpus is
rebuilt. This is the path both for new works and for canonical successors that
must not recreate the old grouped authoring tree. A successor declares its
`superseded_project` and repository-local `revision_evidence`; migration then
excludes the legacy source while preserving its publication lineage.

## Rebuild

```powershell
python scripts/migrate.py --source-root C:\Users\nero_\Downloads\TEXPAPERS --refresh-zenodo
python scripts/verify.py
```

Migration is deterministic with respect to the selected source files and the
cached Zenodo record set. It stages the complete flat paper tree before
replacing the previous generated tree.
