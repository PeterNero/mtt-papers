from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "catalog" / "portable-text-hashes.json"
TEXT_SUFFIXES = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".md",
    ".py",
    ".sty",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}


def canonical_text_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def git_output(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def build(ref: str) -> dict:
    paths = git_output("ls-tree", "-r", "--name-only", ref, "--", "papers").decode(
        "utf-8"
    )
    rows: dict[str, dict[str, int | str]] = {}
    for relative in sorted(filter(None, paths.splitlines())):
        if Path(relative).suffix.lower() not in TEXT_SUFFIXES:
            continue
        raw = git_output("show", f"{ref}:{relative}")
        if b"\x00" in raw:
            continue
        canonical = canonical_text_bytes(raw)
        rows[relative] = {
            "bytes_lf": len(canonical),
            "sha256_lf": hashlib.sha256(canonical).hexdigest(),
        }
    return {
        "schema": "mtt.portable-text-hashes.v1",
        "source_ref": ref,
        "normalization": "CRLF and CR converted to LF; all other bytes preserved",
        "files": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build clone-portable hashes for tracked paper text artifacts."
    )
    parser.add_argument("--ref", default="HEAD")
    args = parser.parse_args()
    payload = build(args.ref)
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"files": len(payload["files"]), "ref": args.ref}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
