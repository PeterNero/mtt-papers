"""Local artifact operations for the six explicitly assigned editorial papers."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONFIG = json.loads((HERE / "editorial-config.json").read_text(encoding="utf-8"))
sys.path.insert(0, str(ROOT / "scripts"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="\n")


def refresh(directory):
    import migrate

    metadata_path = directory / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    release_identity = (metadata.get("latest_zenodo_release"), metadata.get("zenodo_releases"))
    _, _, _, abstract = migrate.pandoc_metadata(directory)
    if directory == HERE:
        metadata["abstract"] = abstract
    metadata["main_tex_sha256"] = digest(directory / "main.tex")
    _, warning = migrate.build_markdown(
        directory, directory.name, metadata["current_version"], metadata["release_state"],
        metadata["main_tex_sha256"], metadata.get("latest_zenodo_release"),
        date_override=metadata["date"],
    )
    mdpath = directory / "paper.md"
    markdown = mdpath.read_text(encoding="utf-8")
    if "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->" not in markdown:
        match = re.search(r"(?m)^#+ (?:Computational Evidence and Reproducibility|Reproducibility and Result Ownership)\s*$", markdown)
        if match:
            stop = re.search(r"(?m)^# References\s*$", markdown[match.end():])
            end = match.end() + stop.start() if stop else len(markdown)
            markdown = (markdown[:match.start()] + "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->\n"
                        + markdown[match.start():end].rstrip()
                        + "\n<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->\n\n" + markdown[end:])
            mdpath.write_text(markdown, encoding="utf-8", newline="\n")
    metadata["paper_md_sha256"] = digest(mdpath)
    metadata["revision"]["revision_evidence_sha256"] = digest(directory / "REVISION_AUDIT.md")
    source_names = [row["path"] for row in metadata["source_files"]]
    extra = ["paper-markdown.lua"]
    if directory == HERE:
        extra += ["frozen-qm.bib", "consumer-qm.bib", "editorial-config.json",
                  "editorial_artifacts.py", "check_editorial_examples.py"]
    source_names.extend(name for name in extra if name not in source_names)
    metadata["source_files"] = [
        {"path": name, "bytes": (directory / name).stat().st_size,
         "sha256": digest(directory / name)} for name in source_names
    ]
    metadata["source_tree_sha256"] = migrate.canonical_hash(metadata["source_files"])
    assert release_identity == (metadata.get("latest_zenodo_release"), metadata.get("zenodo_releases"))
    write_json(metadata_path, metadata)
    write_json(directory / "editorial-build" / "markdown-check.json",
               {"generator": "migrate.build_markdown with local Lua filter",
                "warning": warning, "main_tex_sha256": metadata["main_tex_sha256"],
                "paper_md_sha256": metadata["paper_md_sha256"]})
    print(json.dumps({"paper_id": directory.name, "markdown_warning": warning}))


def render(directory):
    from PIL import Image, ImageDraw
    from pypdf import PdfReader

    target = directory / "editorial-build" / "pages"
    target.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pdftoppm", "-png", "-r", "110", str(directory / "main.pdf"),
                    str(target / "page")], check=True, capture_output=True)
    count = len(PdfReader(directory / "main.pdf").pages)
    files = [target / ("page-" + str(i).zfill(len(str(count))) + ".png")
             for i in range(1, count + 1)]
    assert all(path.is_file() for path in files)
    sheets = []
    for start in range(0, count, 4):
        sheet = Image.new("RGB", (1300, 1770), "#b8bdc3")
        draw = ImageDraw.Draw(sheet)
        for index, path in enumerate(files[start:start + 4]):
            with Image.open(path) as page:
                page.thumbnail((630, 835))
                x, y = 10 + (index % 2) * 650, 30 + (index // 2) * 880
                sheet.paste(page, (x, y))
                draw.text((x, y - 22), f"Page {start + index + 1}", fill="black")
        out = target.parent / f"contact-{start // 4 + 1:02d}.png"
        sheet.save(out)
        sheets.append(str(out))
    record = {"paper_id": directory.name, "pdf_pages": count,
              "pdf_sha256": digest(directory / "main.pdf"), "render_dpi": 110,
              "page_images": [str(p) for p in files], "contact_sheets": sheets,
              "visual_review": "pending"}
    write_json(target.parent / "render-record.json", record)
    print(json.dumps(record))


def report(directory):
    from pypdf import PdfReader

    text = (directory / "main.tex").read_text(encoding="utf-8")
    metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
    print(json.dumps({"paper_id": directory.name, "version": metadata["current_version"],
                      "main_tex_sha256": digest(directory / "main.tex"),
                      "main_tex_lf_sha256": hashlib.sha256(text.encode()).hexdigest(),
                      "source_tree_sha256": metadata["source_tree_sha256"],
                      "paper_md_sha256": digest(directory / "paper.md"),
                      "pdf_sha256": digest(directory / "main.pdf"),
                      "pdf_pages": len(PdfReader(directory / "main.pdf").pages),
                      "source_files": metadata["source_files"]}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["refresh", "render", "report"])
    parser.add_argument("--paper-id", required=True, choices=list(CONFIG))
    args = parser.parse_args()
    directory = (ROOT / "papers" / args.paper_id).resolve()
    assert directory.parent == (ROOT / "papers").resolve()
    globals()[args.operation](directory)


if __name__ == "__main__":
    main()
