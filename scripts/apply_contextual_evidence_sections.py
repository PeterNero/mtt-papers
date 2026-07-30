from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
CATALOG = ROOT / "catalog" / "papers.json"
MAP_PATH = ROOT / "catalog" / "contextual-evidence-map.json"

TEX_BEGIN = "% BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE"
TEX_END = "% END MTT MANAGED COMPUTATIONAL EVIDENCE"
MD_BEGIN = "<!-- BEGIN MTT MANAGED COMPUTATIONAL EVIDENCE -->"
MD_END = "<!-- END MTT MANAGED COMPUTATIONAL EVIDENCE -->"
HEADING = "Computational Evidence and Reproducibility"
TEX_NEEDSPACE = (
    r"\par\begingroup\dimen0=\pagegoal"
    r"\advance\dimen0 by -\pagetotal"
    r"\ifdim\dimen0<7\baselineskip\newpage\fi\endgroup"
)

TEX_BLOCK_RE = re.compile(
    re.escape(TEX_BEGIN) + r".*?" + re.escape(TEX_END),
    re.DOTALL,
)
MD_BLOCK_RE = re.compile(
    re.escape(MD_BEGIN) + r".*?" + re.escape(MD_END),
    re.DOTALL,
)
MD_UNMARKED_SECTION_RE = re.compile(
    rf"^#{{1,6}} {re.escape(HEADING)}\s*\n.*?(?=^#{{1,6}} |\Z)",
    re.MULTILINE | re.DOTALL,
)
TEX_ANCHORS = (
    re.compile(r"\\begin\{thebibliography\}"),
    re.compile(r"\\printbibliography\b"),
    re.compile(r"\\bibliography\{"),
    re.compile(
        r"\\(?:part|chapter|section|subsection|subsubsection)"
        r"\*?\{References\}",
        re.IGNORECASE,
    ),
    re.compile(r"\\end\{document\}"),
)
MD_ANCHORS = (
    re.compile(r"^# References\s*$", re.MULTILINE),
    re.compile(r'^<div class="thebibliography">', re.MULTILINE),
)


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def tex_escape(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "$": r"\$",
        "&": r"\&",
        "#": r"\#",
        "%": r"\%",
        "_": r"\_",
        "^": r"\textasciicircum{}",
        "~": r"\textasciitilde{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def tier_label(value: str) -> str:
    return value.replace("_", " ").lower()


def tex_grouped_hash(value: str, width: int = 8) -> str:
    chunks = [
        value[index : index + width]
        for index in range(0, len(value), width)
    ]
    return r"\texttt{" + " ".join(chunks) + "}"


def tex_grouped_hash_lines(
    value: str,
    width: int = 8,
    chunks_per_line: int = 4,
) -> list[str]:
    chunks = [
        value[index : index + width]
        for index in range(0, len(value), width)
    ]
    return [
        r"\texttt{" + " ".join(chunks[index : index + chunks_per_line]) + "}"
        for index in range(0, len(chunks), chunks_per_line)
    ]


def resolve_rows(
    document: dict[str, Any],
    paper_id: str,
) -> tuple[dict[str, Any], list[str], list[str], list[str]]:
    papers = document.get("papers") or {}
    if paper_id not in papers:
        raise KeyError(f"paper lacks contextual evidence map: {paper_id}")
    paper = papers[paper_id]
    result_set = str(paper.get("result_set") or "")
    result_sets = document.get("result_sets") or {}
    if result_set not in result_sets:
        raise KeyError(f"{paper_id}: unknown result set {result_set!r}")
    mapped = [str(value) for value in result_sets[result_set]]
    direct = [str(value) for value in paper.get("direct_result_ids") or []]
    if not set(direct).issubset(mapped):
        unknown = sorted(set(direct) - set(mapped))
        raise ValueError(
            f"{paper_id}: direct rows are outside the mapped set: {unknown}"
        )

    results = document.get("results") or {}
    missing = [result_id for result_id in mapped if result_id not in results]
    if missing:
        raise KeyError(f"{paper_id}: result metadata missing for {missing}")
    boundary = [
        result_id
        for result_id in mapped
        if str(results[result_id].get("tier") or "") == "OPEN"
    ]
    invalid_direct = sorted(set(direct) & set(boundary))
    if invalid_direct:
        raise ValueError(
            f"{paper_id}: OPEN rows cannot be direct support: "
            f"{invalid_direct}"
        )
    context = [
        result_id
        for result_id in mapped
        if result_id not in set(direct) | set(boundary)
    ]
    return paper, direct, context, boundary


def tex_rows(
    document: dict[str, Any],
    result_ids: list[str],
) -> list[str]:
    results = document["results"]
    lines = [
        r"\begin{itemize}",
        r"\setlength{\itemsep}{0.25em}",
    ]
    for result_id in result_ids:
        row = results[result_id]
        lines.append(
            r"\item \path{"
            + result_id
            + r"} (\emph{"
            + tex_escape(tier_label(str(row["tier"])))
            + r"}).\par "
            + tex_escape(str(row["description"]))
        )
    lines.append(r"\end{itemize}")
    return lines


def markdown_rows(
    document: dict[str, Any],
    result_ids: list[str],
) -> list[str]:
    results = document["results"]
    return [
        (
            f"- `{result_id}` (**{row['tier']}**): "
            f"{row['description']}"
        )
        for result_id in result_ids
        for row in [results[result_id]]
    ]


def render_tex(document: dict[str, Any], paper_id: str) -> str:
    paper, direct, context, boundary = resolve_rows(document, paper_id)
    repository = document["results_repository"]
    commit = str(repository["commit"])
    manifest_path = str(repository["manifest_path"])
    manifest_sha = str(repository["manifest_sha256"])
    repository_url = str(repository["url"])
    manifest_sha_lines = tex_grouped_hash_lines(manifest_sha)
    lines = [
        TEX_BEGIN,
        rf"\section*{{{HEADING}}}",
        tex_escape(str(paper["scope"])),
        "",
        (
            "The referenced rows are frozen to the curated results "
            "repository state identified below. Hashes are grouped in "
            "eight-character blocks for line breaking."
        ),
        r"\begin{quote}\small",
        rf"\textbf{{Repository:}} \url{{{repository_url}}}\\",
        (
            r"\textbf{Commit:} "
            + tex_grouped_hash(commit)
            + r"\\"
        ),
        (
            r"\textbf{Manifest:} \path{"
            + manifest_path
            + r"}\\"
        ),
        (
            r"\textbf{Manifest SHA-256:}\\"
        ),
        *[
            line + (r"\\" if index < len(manifest_sha_lines) - 1 else "")
            for index, line in enumerate(manifest_sha_lines)
        ],
        r"\end{quote}",
        "",
        (
            "Tier labels are quoted verbatim from that manifest. "
            "A row used directly supports only the specific computational "
            "statement identified above; a corpus-state cross-check does not "
            "prove this paper's local theorems; and an open row is evidence "
            "of an unresolved obligation, never of closure."
        ),
    ]
    if direct:
        lines.extend(
            [
                "",
                TEX_NEEDSPACE,
                r"\paragraph{Rows used directly in this paper.}",
                *tex_rows(document, direct),
            ]
        )
    if context:
        lines.extend(
            [
                "",
                TEX_NEEDSPACE,
                r"\paragraph{Corpus-state cross-checks.}",
                *tex_rows(document, context),
            ]
        )
    if boundary:
        lines.extend(
            [
                "",
                TEX_NEEDSPACE,
                r"\paragraph{Open boundary (not evidence of closure).}",
                *tex_rows(document, boundary),
            ]
        )
    lines.extend(
        [
            "",
            (
                "No imported row changes theorem ownership or promotes a "
                "neighboring claim: all local statements retain their stated "
                "hypotheses, domains, and limitations."
            ),
            TEX_END,
        ]
    )
    return "\n".join(lines)


def render_markdown(document: dict[str, Any], paper_id: str) -> str:
    paper, direct, context, boundary = resolve_rows(document, paper_id)
    repository = document["results_repository"]
    commit = str(repository["commit"])
    manifest_path = str(repository["manifest_path"])
    manifest_sha = str(repository["manifest_sha256"])
    repository_url = str(repository["url"])
    manifest_url = (
        f"{repository_url}/blob/{commit}/{manifest_path}"
    )
    lines = [
        MD_BEGIN,
        f"# {HEADING}",
        "",
        str(paper["scope"]),
        "",
        (
            "The referenced rows are frozen to the curated results "
            f"repository at commit `{commit}`. The "
            f"[immutable result manifest]({manifest_url}) has SHA-256 "
            f"`{manifest_sha}`."
        ),
        "",
        (
            "Tier labels are quoted verbatim from that manifest. A row used "
            "directly supports only the specific computational statement "
            "identified above; a corpus-state cross-check does not prove this "
            "paper's local theorems; and an open row is evidence of an "
            "unresolved obligation, never of closure."
        ),
    ]
    if direct:
        lines.extend(
            [
                "",
                "## Rows used directly in this paper",
                "",
                *markdown_rows(document, direct),
            ]
        )
    if context:
        lines.extend(
            [
                "",
                "## Corpus-state cross-checks",
                "",
                *markdown_rows(document, context),
            ]
        )
    if boundary:
        lines.extend(
            [
                "",
                "## Open boundary (not evidence of closure)",
                "",
                *markdown_rows(document, boundary),
            ]
        )
    lines.extend(
        [
            "",
            (
                "No imported row changes theorem ownership or promotes a "
                "neighboring claim: all local statements retain their stated "
                "hypotheses, domains, and limitations."
            ),
            MD_END,
        ]
    )
    return "\n".join(lines)


def insert_before_anchor(
    text: str,
    block: str,
    anchors: tuple[re.Pattern[str], ...],
) -> str:
    positions = [
        match.start()
        for pattern in anchors
        for match in [pattern.search(text)]
        if match is not None
    ]
    if positions:
        index = min(positions)
        return (
            text[:index].rstrip()
            + "\n\n"
            + block
            + "\n\n"
            + text[index:].lstrip()
        )
    return text.rstrip() + "\n\n" + block + "\n"


def apply_tex(text: str, block: str) -> str:
    text = TEX_BLOCK_RE.sub("", text)
    return insert_before_anchor(text, block, TEX_ANCHORS)


def apply_markdown(text: str, block: str) -> str:
    text = MD_BLOCK_RE.sub("", text)
    text = MD_UNMARKED_SECTION_RE.sub("", text)
    return insert_before_anchor(text, block, MD_ANCHORS)


def exact_block(
    text: str,
    pattern: re.Pattern[str],
    expected: str,
) -> bool:
    matches = pattern.findall(text)
    return len(matches) == 1 and matches[0].strip() == expected.strip()


def update_catalog_hashes(
    paper_hashes: dict[str, str],
) -> None:
    catalog = read_json(CATALOG)
    for row in catalog.get("papers") or []:
        paper_id = str(row.get("paper_id") or "")
        if paper_id in paper_hashes:
            row["paper_md_sha256"] = paper_hashes[paper_id]
    write_json_atomic(CATALOG, catalog)


def selected_paper_ids(
    document: dict[str, Any],
    requested: list[str],
) -> list[str]:
    available = set((document.get("papers") or {}).keys())
    if not requested:
        return sorted(available)
    selected = set(requested)
    missing = sorted(selected - available)
    if missing:
        raise KeyError(
            "papers lack contextual evidence mapping: "
            + ", ".join(missing)
        )
    return sorted(selected)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Apply or verify context-specific computational-evidence "
            "sections in mapped MTT papers."
        )
    )
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    document = read_json(MAP_PATH)
    paper_ids = selected_paper_ids(document, args.paper_id)
    failures = []
    changed_tex = 0
    changed_markdown = 0
    paper_hashes: dict[str, str] = {}

    for paper_id in paper_ids:
        directory = PAPERS / paper_id
        metadata_path = directory / "metadata.json"
        metadata = read_json(metadata_path)
        tex_path = directory / str(
            metadata.get("canonical_tex") or "main.tex"
        )
        markdown_path = directory / str(
            metadata.get("canonical_markdown") or "paper.md"
        )
        expected_tex = render_tex(document, paper_id)
        expected_markdown = render_markdown(document, paper_id)
        tex = tex_path.read_text(encoding="utf-8-sig")
        markdown = markdown_path.read_text(encoding="utf-8-sig")

        if args.verify:
            if not exact_block(tex, TEX_BLOCK_RE, expected_tex):
                failures.append(
                    f"{paper_id}: TeX evidence block differs or is missing"
                )
            if not exact_block(
                markdown,
                MD_BLOCK_RE,
                expected_markdown,
            ):
                failures.append(
                    f"{paper_id}: Markdown evidence block differs or is "
                    "missing"
                )
            if tex.count(rf"\section*{{{HEADING}}}") != 1:
                failures.append(
                    f"{paper_id}: TeX evidence heading is duplicated"
                )
            if markdown.count(f"# {HEADING}") != 1:
                failures.append(
                    f"{paper_id}: Markdown evidence heading is duplicated"
                )
            continue

        updated_tex = apply_tex(tex, expected_tex)
        updated_markdown = apply_markdown(
            markdown,
            expected_markdown,
        )
        if updated_tex != tex:
            tex_path.write_text(
                updated_tex,
                encoding="utf-8",
                newline="\n",
            )
            changed_tex += 1
        if updated_markdown != markdown:
            markdown_path.write_text(
                updated_markdown,
                encoding="utf-8",
                newline="\n",
            )
            changed_markdown += 1
        markdown_hash = sha256(markdown_path)
        metadata["paper_md_sha256"] = markdown_hash
        write_json_atomic(metadata_path, metadata)
        paper_hashes[paper_id] = markdown_hash

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    if not args.verify:
        update_catalog_hashes(paper_hashes)
        print(
            json.dumps(
                {
                    "papers": len(paper_ids),
                    "changed_tex": changed_tex,
                    "changed_markdown": changed_markdown,
                },
                indent=2,
            )
        )
    else:
        print(
            json.dumps(
                {
                    "verified_papers": len(paper_ids),
                    "status": "pass",
                },
                indent=2,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
