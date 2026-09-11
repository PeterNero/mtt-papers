#!/usr/bin/env python3
"""Build every paper governed by the contextual evidence map."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
MAP_PATH = ROOT / "catalog" / "contextual-evidence-map.json"
LOG_ROOT = ROOT / "tmp" / "build-contextual-evidence"
WARNING_RE = re.compile(
    r"(Overfull \\[hv]box|LaTeX Warning:.*(?:undefined|multiply defined)|"
    r"Package .* Warning:.*(?:undefined|multiply defined))",
    re.IGNORECASE,
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def resolve_executable(name: str) -> str:
    resolved = shutil.which(name)
    if not resolved:
        raise RuntimeError(f"required executable is unavailable: {name}")
    return resolved


def run_step(
    command: list[str],
    cwd: Path,
    log_path: Path,
) -> tuple[int, str]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    log_path.write_text(completed.stdout, encoding="utf-8")
    return completed.returncode, completed.stdout


def needs_biber(tex: str) -> bool:
    return (
        r"\addbibresource" in tex
        or r"\printbibliography" in tex
        or r"\usepackage{biblatex}" in tex
    )


def needs_bibtex(tex: str) -> bool:
    return r"\bibliography{" in tex


def build_paper(
    paper_id: str,
    pdflatex: str,
    biber: str | None,
    bibtex: str | None,
) -> dict[str, Any]:
    directory = PAPERS / paper_id
    metadata = read_json(directory / "metadata.json")
    tex_name = str(metadata.get("canonical_tex") or "main.tex")
    tex_path = directory / tex_name
    tex = tex_path.read_text(encoding="utf-8-sig")
    log_directory = LOG_ROOT / paper_id
    log_directory.mkdir(parents=True, exist_ok=True)
    commands: list[tuple[str, list[str]]] = [
        (
            "pdflatex-1",
            [
                pdflatex,
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                tex_name,
            ],
        )
    ]
    if needs_biber(tex):
        if not biber:
            return {
                "paper_id": paper_id,
                "status": "failed",
                "error": "biber is required but unavailable",
                "warnings": [],
            }
        commands.append(("biber", [biber, Path(tex_name).stem]))
    elif needs_bibtex(tex):
        if not bibtex:
            return {
                "paper_id": paper_id,
                "status": "failed",
                "error": "bibtex is required but unavailable",
                "warnings": [],
            }
        commands.append(("bibtex", [bibtex, Path(tex_name).stem]))
    commands.extend(
        [
            (
                "pdflatex-2",
                [
                    pdflatex,
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    tex_name,
                ],
            ),
            (
                "pdflatex-3",
                [
                    pdflatex,
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    tex_name,
                ],
            ),
        ]
    )

    outputs: list[str] = []
    for label, command in commands:
        returncode, output = run_step(
            command,
            directory,
            log_directory / f"{label}.log",
        )
        outputs.append(output)
        if returncode:
            return {
                "paper_id": paper_id,
                "status": "failed",
                "error": f"{label} exited with status {returncode}",
                "warnings": sorted(set(WARNING_RE.findall("\n".join(outputs)))),
            }

    pdf_path = directory / f"{Path(tex_name).stem}.pdf"
    if not pdf_path.is_file() or pdf_path.stat().st_size == 0:
        return {
            "paper_id": paper_id,
            "status": "failed",
            "error": f"missing output PDF: {pdf_path}",
            "warnings": [],
        }
    warnings = sorted(
        {
            match.group(0)
            for output in outputs[-1:]
            for match in WARNING_RE.finditer(output)
        }
    )
    return {
        "paper_id": paper_id,
        "status": "pass" if not warnings else "warning",
        "pdf_bytes": pdf_path.stat().st_size,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument(
        "--jobs",
        type=int,
        default=max(1, min(4, (os.cpu_count() or 2) // 2)),
    )
    args = parser.parse_args()

    document = read_json(MAP_PATH)
    all_ids = sorted(document["papers"])
    paper_ids = args.paper_id or all_ids
    catalog_ids = {row["paper_id"] for row in read_json(ROOT / "catalog/papers.json")["papers"]}
    unknown = sorted(set(paper_ids) - catalog_ids)
    if unknown:
        print(
            "unknown paper IDs: " + ", ".join(unknown),
            file=sys.stderr,
        )
        return 2

    try:
        pdflatex = resolve_executable("pdflatex")
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    biber = shutil.which("biber")
    bibtex = shutil.which("bibtex")
    LOG_ROOT.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as executor:
        futures = {
            executor.submit(
                build_paper,
                paper_id,
                pdflatex,
                biber,
                bibtex,
            ): paper_id
            for paper_id in paper_ids
        }
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(
                f"{result['status']:7} {result['paper_id']}",
                flush=True,
            )

    results.sort(key=lambda item: item["paper_id"])
    summary = {
        "papers": len(results),
        "pass": sum(item["status"] == "pass" for item in results),
        "warning": sum(
            item["status"] == "warning" for item in results
        ),
        "failed": sum(item["status"] == "failed" for item in results),
        "results": results,
    }
    (LOG_ROOT / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({key: summary[key] for key in (
        "papers",
        "pass",
        "warning",
        "failed",
    )}, indent=2))
    return 0 if not summary["failed"] and not summary["warning"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
