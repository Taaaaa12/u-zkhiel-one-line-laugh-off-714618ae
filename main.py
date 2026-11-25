#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Deterministic: no input, no randomness, no network, no clock.
"""

from pathlib import Path

JOKE = (
    "My fitness tracker says I burned 500 calories today, "
    "mostly from anxiously refreshing my bank account."
)


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
