#!/usr/bin/env python3
"""Validate markdown file placement for this repository."""

from __future__ import annotations

import sys
from pathlib import Path

ALLOWED_ROOT_MARKDOWN = {
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
}

ALLOWED_PREFIXES = (
    ".github/",
    "docs/",
    "projects/main-submission/",
    "projects/experiments/",
    "assets/",
    "tasks/",
)


def _normalize(path: str) -> str:
    p = Path(path)
    normalized = p.as_posix()
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def markdown_path_allowed(path: str) -> bool:
    normalized = _normalize(path)
    if not normalized.endswith(".md"):
        return True

    if "/" not in normalized:
        return normalized in ALLOWED_ROOT_MARKDOWN

    return normalized.startswith(ALLOWED_PREFIXES)


def validate_paths(paths: list[str]) -> tuple[list[str], list[str]]:
    invalid: list[str] = []
    valid: list[str] = []

    for original in paths:
        normalized = _normalize(original)
        if markdown_path_allowed(normalized):
            valid.append(normalized)
        else:
            invalid.append(normalized)

    return valid, invalid


def main() -> int:
    paths = sys.argv[1:]
    if not paths:
        print("No file paths provided. Usage: python tools/validate_docs_scope.py <path> [<path> ...]")
        return 0

    _, invalid = validate_paths(paths)

    if invalid:
        print("ERROR: Markdown files found outside allowed lanes:")
        for path in invalid:
            print(f" - {path}")
        print("Allowed root markdown files:")
        for file_name in sorted(ALLOWED_ROOT_MARKDOWN):
            print(f" - {file_name}")
        print("Allowed markdown prefixes:")
        for prefix in ALLOWED_PREFIXES:
            print(f" - {prefix}")
        return 1

    print("OK: All markdown paths are within allowed lanes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
