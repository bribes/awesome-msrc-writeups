#!/usr/bin/env python3
"""Validate writeups.csv and render the repository README."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlparse


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
ALLOWED_TYPES = {"blog", "video"}
UNKNOWN = "?"


class CatalogError(ValueError):
    """Raised when the catalog contains invalid or ambiguous data."""


def _is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _normalized_url(value: str) -> str:
    return value.rstrip("/").casefold()


def _markdown_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def _format_bounty(value: str) -> str:
    if value == UNKNOWN:
        return "???"
    amount = Decimal(value)
    if amount == amount.to_integral():
        return f"{int(amount):,}"
    return f"{amount:,.2f}".rstrip("0").rstrip(".")


def load_writeups(csv_path: str | Path) -> list[dict[str, str]]:
    path = Path(csv_path)
    with path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise CatalogError(
                f"{path}: expected CSV header {','.join(FIELDS)!r}, "
                f"got {','.join(reader.fieldnames or ())!r}"
            )
        writeups = [dict(row) for row in reader]

    validate_writeups(writeups, path)
    return writeups


def validate_writeups(writeups: list[dict[str, str]], source: Path | None = None) -> None:
    label = str(source or "writeups.csv")
    seen_urls: dict[str, int] = {}

    for row_number, row in enumerate(writeups, start=2):
        prefix = f"{label}:{row_number}"
        missing = [field for field in FIELDS if not row.get(field, "").strip()]
        if missing:
            raise CatalogError(f"{prefix}: empty field(s): {', '.join(missing)}")

        if row["date"] != UNKNOWN:
            try:
                datetime.strptime(row["date"], "%Y-%m-%d")
            except ValueError as exc:
                raise CatalogError(f"{prefix}: invalid date {row['date']!r}") from exc

        if row["bounty"] != UNKNOWN:
            try:
                amount = Decimal(row["bounty"])
            except InvalidOperation as exc:
                raise CatalogError(f"{prefix}: invalid bounty {row['bounty']!r}") from exc
            if not amount.is_finite() or amount < 0:
                raise CatalogError(f"{prefix}: bounty must be a non-negative number or '?'")

        for field in ("url", "author-url", "archive-url"):
            value = row[field]
            if value != UNKNOWN and not _is_url(value):
                raise CatalogError(f"{prefix}: invalid {field} {value!r}")

        if row["type"] not in ALLOWED_TYPES:
            raise CatalogError(
                f"{prefix}: type must be one of {sorted(ALLOWED_TYPES)}, got {row['type']!r}"
            )
        if row["tweeted"] not in {"true", "false"}:
            raise CatalogError(f"{prefix}: tweeted must be 'true' or 'false'")

        normalized_url = _normalized_url(row["url"])
        if normalized_url in seen_urls:
            raise CatalogError(
                f"{prefix}: duplicate URL (first seen on row {seen_urls[normalized_url]})"
            )
        seen_urls[normalized_url] = row_number


def generate_readme(writeups: list[dict[str, str]], output_file: str | Path) -> None:
    ordered = sorted(
        writeups,
        key=lambda item: item["date"] if item["date"] != UNKNOWN else "0000-00-00",
        reverse=True,
    )
    dated = [item["date"] for item in ordered if item["date"] != UNKNOWN]
    latest = max(dated) if dated else "unknown"

    lines = [
        "# Awesome MSRC Writeups",
        "",
        "🐛 A curated catalog of public security research involving Microsoft products, services, and the Microsoft Security Response Center (MSRC).",
        "",
        f"**{len(ordered)} writeups and talks. Latest publication: {latest}.**",
        "",
        "Originally based on [Awesome Google VRP Writeups](https://github.com/xdavidhu/awesome-google-vrp-writeups).",
        "",
        "## Contributing",
        "",
        "Found a missing original disclosure or technical writeup? Please read [CONTRIBUTING.md](CONTRIBUTING.md) and open a pull request that adds one row to `writeups.csv`. The README is generated from that file.",
        "",
        "## Writeups",
        "",
    ]

    last_year: int | str | None = None
    for writeup in ordered:
        if writeup["date"] == UNKNOWN:
            year: int | str = "Unknown date"
            date_string = "???"
        else:
            date = datetime.strptime(writeup["date"], "%Y-%m-%d")
            year = date.year
            date_string = date.strftime("%b %d")

        if last_year != year:
            if last_year is not None:
                lines.append("")
            lines.extend((f"### {year}", ""))
            last_year = year

        bounty = _format_bounty(writeup["bounty"])
        title = _markdown_text(writeup["title"])
        author = _markdown_text(writeup["author"] if writeup["author"] != UNKNOWN else "???")
        if writeup["author-url"] == UNKNOWN:
            author_text = author
        else:
            author_text = f"[{author}]({writeup['author-url']})"

        archive_text = ""
        if writeup["archive-url"] != UNKNOWN:
            archive_text = f" ([archive]({writeup['archive-url']}))"
        type_text = " · video" if writeup["type"] == "video" else ""

        lines.append(
            f"- **[{date_string} - ${bounty}]** "
            f"[{title}]({writeup['url']}){archive_text} by {author_text}{type_text}"
        )

    Path(output_file).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="path to writeups.csv")
    parser.add_argument("output", type=Path, help="README output path")
    args = parser.parse_args()

    try:
        writeups = load_writeups(args.csv)
        generate_readme(writeups, args.output)
    except (CatalogError, OSError) as exc:
        parser.exit(1, f"error: {exc}\n")

    print(f"Validated {len(writeups)} entries and wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
