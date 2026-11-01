#!/usr/bin/env python3
"""Recover catalog rows from a generated README.

The CSV remains the source of truth. This utility exists only for recovery and
migration work.
"""

from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path


FIELDS = (
    "date",
    "bounty",
    "title",
    "url",
    "author",
    "author-url",
    "type",
    "tweeted",
    "archive-url",
)
ENTRY_RE = re.compile(
    r"^- \*\*\[(?P<date>[A-Z][a-z]{2} \d{2}|\?\?\?) - \$(?P<bounty>[\d,]+|\?\?\?)\]\*\* "
    r"\[(?P<title>.+)\]\((?P<url>https?://[^)]+)\)"
    r"(?: \(\[archive\]\((?P<archive>https?://[^)]+)\)\))? by "
    r"(?P<author>.+?)(?P<video> · video)?$"
)
LINKED_AUTHOR_RE = re.compile(r"^\[(?P<name>.+)\]\((?P<url>https?://[^)]+)\)$")


def _unescape(value: str) -> str:
    return value.replace("\\]", "]").replace("\\[", "[").replace("\\\\", "\\")


def parse_readme(readme: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    year: int | None = None

    for line_number, line in enumerate(readme.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("### "):
            heading = line.removeprefix("### ")
            year = int(heading) if heading.isdigit() else None
            continue
        if not line.startswith("- **["):
            continue

        match = ENTRY_RE.fullmatch(line)
        if not match:
            raise ValueError(f"{readme}:{line_number}: cannot parse generated catalog entry")

        raw_date = match.group("date")
        if raw_date == "???" or year is None:
            date = "?"
        else:
            date = datetime.strptime(f"{year} {raw_date}", "%Y %b %d").strftime("%Y-%m-%d")

        raw_author = match.group("author")
        linked_author = LINKED_AUTHOR_RE.fullmatch(raw_author)
        if linked_author:
            author = _unescape(linked_author.group("name"))
            author_url = linked_author.group("url")
        else:
            author = "?" if raw_author == "???" else _unescape(raw_author)
            author_url = "?"

        rows.append(
            {
                "date": date,
                "bounty": match.group("bounty").replace(",", "")
                if match.group("bounty") != "???"
                else "?",
                "title": _unescape(match.group("title")),
                "url": match.group("url"),
                "author": author,
                "author-url": author_url,
                "type": "video" if match.group("video") else "blog",
                "tweeted": "false",
                "archive-url": match.group("archive") or "?",
            }
        )

    if not rows:
        raise ValueError(f"{readme}: no catalog entries found")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    try:
        rows = parse_readme(args.readme)
        with args.output.open("w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FIELDS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"error: {exc}\n")

    print(f"Recovered {len(rows)} entries into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
