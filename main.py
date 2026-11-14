# Copies a pre-made 1024x1024 news infographic (entry.png, sitting beside
# this script) to the grader's output directory. Entry for the make.fun
# "news-image-01" bounty: one image summing up Friday 13 November 2026.
"""Deterministic, stdlib-only copier for the news-image-01 entry."""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> Path:
    """Where the image goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if value:
        return Path(value)
    return Path(DEFAULT_OUTPUT_DIR)


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        print(f"error: bundled image not found: {source}", file=sys.stderr)
        return 1
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / SOURCE_NAME
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
