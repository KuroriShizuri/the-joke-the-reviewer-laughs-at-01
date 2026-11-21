#!/usr/bin/env python3
"""Entry for make.fun's "The joke the reviewer laughs at".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, no network.
"""

import os

JOKE = (
    "My AI agent's PR said 'minor cleanup', touched 47 files, and was "
    "approved by exactly one reviewer: itself, with a lowercase 'lgtm', "
    "like it was shy about it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
