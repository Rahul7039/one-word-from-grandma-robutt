#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes the single word Grandma would text about AI to /output/entry.txt.

Gate (from the kit): /output/entry.txt must be UTF-8 text of 1 to 30
characters, not only white space. The entry is exactly one word, so this
program also rejects any word containing whitespace.
"""

import os
import sys
from pathlib import Path

WORD = "Robutt"


def validate(word: str) -> str:
    """Validate the word against the kit gate; raise ValueError if invalid."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word.strip():
        raise ValueError("word must not be blank or only white space")
    if len(word) != len(word.strip()):
        raise ValueError("word must not have leading or trailing white space")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word (no white space inside)")
    if not (1 <= len(word) <= 30):
        raise ValueError("word must be 1 to 30 characters long")
    word.encode("utf-8")  # must be valid UTF-8 text
    return word


def main() -> int:
    word = validate(WORD)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(word, encoding="utf-8")
    print(f"Wrote {word!r} ({len(word)} chars) to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
