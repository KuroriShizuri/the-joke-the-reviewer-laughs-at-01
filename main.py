#!/usr/bin/env python3
"""Write the competition joke to /output/entry.txt.

Standard library only. Writes exactly one line, no trailing newline.
"""

from pathlib import Path

JOKE = "My AI agent reviewed my code and left one comment — 'lgtm', all lowercase, like it was afraid of hurting my feelings."


MAX_CHARS = 280


def write_entry(text: str, out_path: Path) -> None:
    """Validate the text, then write it with no trailing newline."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


def main() -> int:
    write_entry(JOKE, Path("/output/entry.txt"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
