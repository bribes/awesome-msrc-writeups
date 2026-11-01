#!/usr/bin/env python3
"""Compatibility entry point for the repository's local Docker action."""

from __future__ import annotations

import os
from pathlib import Path

from csv_to_readme import generate_readme, load_writeups


def builder() -> None:
    default_workspace = Path(__file__).resolve().parents[2]
    workspace = Path(os.environ.get("GITHUB_WORKSPACE", default_workspace))
    csv_path = workspace / "writeups.csv"
    readme_path = workspace / "README.md"

    writeups = load_writeups(csv_path)
    generate_readme(writeups, readme_path)
    print(f"Validated {len(writeups)} entries and wrote {readme_path}")


if __name__ == "__main__":
    builder()
