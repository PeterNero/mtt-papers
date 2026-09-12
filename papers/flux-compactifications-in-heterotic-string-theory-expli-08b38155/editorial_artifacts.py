"""Build and derive artifacts only inside the six assigned paper directories."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
THETA = (
    "theta-closure-in-modal-triplet-theory-i-gauge-profile-t-c11e7b8f",
    "theta-closure-in-modal-triplet-theory-ii-direct-geometr-303cc1ca",
    "theta-closure-in-modal-triplet-theory-iii-conditional-t-36bd7643",
    "theta-closure-in-modal-triplet-theory-iv-conditional-gr-1b3e0dc5",
    "theta-closure-in-modal-triplet-theory-v-weak-angle-roun-a4083c1c",
)
ALLOWED = (HERE.name, *THETA)
sys.path.insert(0, str(ROOT / "scripts"))
from migrate import build_markdown, canonical_hash, pandoc_metadata
import build_contextual_evidence_papers as builder


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def managed_markers(project: Path) -> None:
    path = project / "paper.md"
    md = path.read_text(encoding="utf-8")
    begin = "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"
    end = "<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->"
    if begin in md:
        return
    heading = re.search(r"^#{1,6} Computational Evidence and Reproducibility\s*$", md, re.M)
    if heading is None:
        raise ValueError("Missing managed evidence heading")
    next_heading = re.search(r"^#{1,6} \S", md[heading.end():], re.M)
    stop = heading.end() + next_heading.start() if next_heading else len(md)
    md = (md[:heading.start()].rstrip() + "\n\n" + begin + "\n"
          + md[heading.start():stop].strip() + "\n" + end + "\n\n"
          + md[stop:].lstrip())
    path.write_text(md.rstrip() + "\n", encoding="utf-8", newline="\n")


def derive(project: Path, qa: Path, version: str) -> dict:
    import fitz

    metadata_path = project / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8-sig"))
    baseline = qa / "metadata-before.json"
    if not baseline.exists():
        write_json(baseline, metadata)
    release_identity = {key: metadata.get(key) for key in ("latest_zenodo_release", "zenodo_releases")}
    _, _, date, abstract = pandoc_metadata(project)
    metadata.update(current_version=version, release_state="current_revised_tex",
                    version_relation="current_source_newer_than_release", date=date, abstract=abstract)
    rows = json.loads((ROOT / "catalog/research-ownership.json").read_text(encoding="utf-8"))["results"]
    references = {"eta9_gate1_campaign", "eta9_three_cycle_b96_nondetection", "q79_bk3_rank_zero_kernel"}
    if project.name == HERE.name:
        references.update(row["result_id"] for row in rows if row["integration_owner"] == HERE.name)
        references.update(("q79_global_fitting_descent", "q79_projective_hym_naturality", "q79_cech_projector_compiler"))
    metadata["result_refs"] = sorted(set(metadata.get("result_refs", [])) | references)
    tex = project / "main.tex"
    metadata["main_tex_sha256"] = digest(tex)
    _, warning = build_markdown(project, project.name, version, metadata["release_state"],
                                digest(tex), metadata.get("latest_zenodo_release"), date)
    managed_markers(project)
    metadata["paper_md_sha256"] = digest(project / "paper.md")
    paths = [row["path"] for row in metadata["source_files"]]
    paths += ["main.pdf", "REVISION_AUDIT.md"]
    if project.name == HERE.name:
        paths += ["test_contextual_revision.py", "editorial_artifacts.py"]
    metadata["source_files"] = [dict(path=name, bytes=(project / name).stat().st_size,
                                     sha256=digest(project / name)) for name in dict.fromkeys(paths)]
    metadata["source_tree_sha256"] = canonical_hash(metadata["source_files"])
    revision = metadata.setdefault("revision", {})
    revision.update(selected_revision=True,
                    revision_evidence_path=f"papers/{project.name}/REVISION_AUDIT.md",
                    revision_evidence_sha256=digest(project / "REVISION_AUDIT.md"))
    assert release_identity == {key: metadata.get(key) for key in release_identity}
    write_json(metadata_path, metadata)
    pdf = fitz.open(project / "main.pdf")
    all_text = "\n".join(page.get_text() for page in pdf)
    assert "Version " + version[1:] in all_text
    report = dict(paper_id=project.name, version=version, pdf_pages=len(pdf),
                  main_tex_lf_sha256=hashlib.sha256(tex.read_text(encoding="utf-8").encode()).hexdigest(),
                  main_pdf_sha256=digest(project / "main.pdf"),
                  paper_md_sha256=metadata["paper_md_sha256"], pandoc_warning=warning,
                  release_identity_preserved=True,
                  pages_with_text=[bool(page.get_text().strip()) for page in pdf],
                  generated_by="paper-local editorial_artifacts.py; migrate.build_markdown; scoped contextual build helper")
    write_json(qa / "artifact-report.json", report)
    return report


def render(project: Path, qa: Path) -> None:
    from PIL import Image, ImageOps, ImageDraw

    subprocess.run(["pdftoppm", "-png", "-r", "105", str(project / "main.pdf"), str(qa / "page")], check=True)
    pages = sorted(qa.glob("page-*.png"))
    for offset in range(0, len(pages), 2):
        images = [Image.open(path).convert("RGB") for path in pages[offset:offset+2]]
        w, h = images[0].size
        sheet = Image.new("RGB", (w * len(images), h + 32), "#eeeeee")
        draw = ImageDraw.Draw(sheet)
        for column, (path, img) in enumerate(zip(pages[offset:offset+2], images)):
            sheet.paste(img, (column*w, 32))
            draw.text((column*w+16, 10), project.name + " / " + path.stem, fill="black")
        sheet.save(qa / f"spread-{offset+1:02d}-{offset+len(images):02d}.png")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-id", choices=ALLOWED, action="append")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()
    for slug in args.paper_id or ALLOWED:
        project = ROOT / "papers" / slug
        version = "v7" if slug == HERE.name else "v3"
        qa = project / ("qa-" + version)
        qa.mkdir(exist_ok=True)
        if not args.skip_build:
            builder.LOG_ROOT = qa / "build"
            old_argv = sys.argv
            sys.argv = ["scripts/build_contextual_evidence_papers.py", "--paper-id", slug, "--jobs", "1"]
            try:
                status = builder.main()
            finally:
                sys.argv = old_argv
            if status:
                raise SystemExit(status)
        print(json.dumps(derive(project, qa, version)), flush=True)
        if args.render:
            render(project, qa)


if __name__ == "__main__":
    main()
