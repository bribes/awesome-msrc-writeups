#!/usr/bin/env python3
"""Request Wayback Machine snapshots for catalog entries without an archive URL."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


BUILDER_DIR = Path(__file__).resolve().parents[1] / "builder"
sys.path.insert(0, str(BUILDER_DIR))

from csv_to_readme import FIELDS, load_writeups  # noqa: E402


USER_AGENT = "https://github.com/bribes/awesome-msrc-writeups"


def archive(url: str, timeout: int) -> str | None:
    request = Request(
        f"https://web.archive.org/save/{quote(url, safe='')}",
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            snapshot = response.headers.get("Content-Location") or response.geturl()
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"warning: could not archive {url}: {exc}", file=sys.stderr)
        return None

    if snapshot.startswith("/"):
        snapshot = f"https://web.archive.org{snapshot}"
    return snapshot if "web.archive.org" in snapshot else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    try:
        writeups = load_writeups(args.csv)
        updated = 0
        for writeup in writeups:
            if writeup["archive-url"] != "?" or writeup["type"] == "video":
                continue
            print(f"Archiving {writeup['url']}")
            archive_url = archive(writeup["url"], args.timeout)
            if archive_url:
                writeup["archive-url"] = archive_url
                updated += 1

        with args.csv.open("w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FIELDS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(writeups)
    except OSError as exc:
        parser.exit(1, f"error: {exc}\n")

    print(f"Updated {updated} archive URL(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
