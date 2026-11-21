#!/usr/bin/env python3
"""Make.fun entry: "The joke the reviewer laughs at".

Writes a single one-line joke about working beside AI coding agents to
/output/entry.txt. Standard library only, no network access.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "My AI agent reviewed my code and left one comment \u2014 'lgtm', all "
    "lowercase, like it was afraid of hurting my feelings."
)


def main() -> None:
    """Write the joke to the entry file.

    The file holds exactly the joke text: no trailing newline, so the
    entry is one clean line of at most 280 characters.
    """
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
