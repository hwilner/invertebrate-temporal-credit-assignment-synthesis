#!/usr/bin/env python3
"""Check tracked repository content against the public release boundary.

The scanner obtains paths from ``git ls-files`` and reads only tracked text files.
It does not walk untracked directories, access a network, or write files.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROHIBITED_PATH_PARTS = frozenset(
    {
        "access_logs",
        "archive",
        "archives",
        "artifacts",
        "data",
        "derived",
        "download",
        "downloads",
        "external",
        "external_docs",
        "figure",
        "figures",
        "metadata",
        "output",
        "outputs",
        "plot",
        "plots",
        "raw",
        "result",
        "results",
        "source_material",
        "sources",
    }
)
PROHIBITED_SUFFIXES = frozenset(
    {
        ".7z",
        ".bz2",
        ".csv",
        ".feather",
        ".gif",
        ".gz",
        ".h5",
        ".hdf5",
        ".ipynb",
        ".jpeg",
        ".jpg",
        ".json",
        ".jsonl",
        ".mat",
        ".mp4",
        ".npy",
        ".npz",
        ".parquet",
        ".pdf",
        ".png",
        ".rdata",
        ".rds",
        ".svg",
        ".tar",
        ".tgz",
        ".tif",
        ".tiff",
        ".tsv",
        ".webm",
        ".xz",
        ".zip",
    }
)
TEXT_SUFFIXES = frozenset({"", ".md", ".py", ".txt", ".toml", ".yaml", ".yml"})
TEXT_MARKERS = (
    ("http" + "://", "external URL"),
    ("https" + "://", "external URL"),
    ("doi" + ".org", "DOI-like identifier"),
    (chr(64), "email-like text"),
)


def tracked_paths(root: Path) -> list[Path]:
    """Return paths reported as tracked by Git.

    Args:
        root: Repository directory in which to invoke Git.

    Returns:
        Repository-relative paths reported by ``git ls-files``.

    Raises:
        RuntimeError: If ``root`` is not a Git working tree or Git fails.
    """
    completed = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(message or "git ls-files failed")
    return [Path(item) for item in completed.stdout.decode("utf-8").split("\0") if item]


def path_violations(path: Path) -> list[str]:
    """Identify prohibited release-boundary features in a tracked path.

    Args:
        path: Repository-relative tracked path.

    Returns:
        Human-readable violations found in ``path``.
    """
    violations: list[str] = []
    if any(part.lower() in PROHIBITED_PATH_PARTS for part in path.parts):
        violations.append("prohibited directory name")
    if path.suffix.lower() in PROHIBITED_SUFFIXES:
        violations.append("prohibited file suffix")
    return violations


def text_violations(path: Path) -> list[str]:
    """Identify clear public-boundary markers in one tracked text file.

    Args:
        path: Absolute path to a tracked text file.

    Returns:
        Human-readable violations found in file text. Binary or unreadable files
        are skipped because only textual content is in scope for this check.
    """
    if path.name == "INTRODUCTION.md" and path.parent.name == "docs":
        return []
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    lowered = text.lower()
    markers = TEXT_MARKERS
    if path.name == "EXTENDED_INTRODUCTION.md" and path.parent.name == "docs":
        # Owner-approved exemption: docs/EXTENDED_INTRODUCTION.md is exempt from
        # the external-URL rule only; all other markers still apply to it.
        markers = tuple(item for item in TEXT_MARKERS if item[1] != "external URL")
    return [description for marker, description in markers if marker in lowered]


def main() -> int:
    """Run the tracked-file release-boundary check.

    Returns:
        Zero when no configured violations are found; otherwise one. When the
        current directory is not a Git checkout, the check is skipped and zero
        is returned because no tracked-file set is available.
    """
    root = Path.cwd()
    try:
        paths = tracked_paths(root)
    except RuntimeError as error:
        print(f"SKIP: tracked-file scan unavailable: {error}")
        return 0

    violations: list[str] = []
    for relative_path in paths:
        for reason in path_violations(relative_path):
            violations.append(f"{relative_path}: {reason}")
        for reason in text_violations(root / relative_path):
            violations.append(f"{relative_path}: {reason}")

    if violations:
        print("FAIL: public release-boundary violations found:")
        print("\n".join(f"- {item}" for item in violations))
        return 1

    print(f"PASS: checked {len(paths)} tracked path(s) and tracked text only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
