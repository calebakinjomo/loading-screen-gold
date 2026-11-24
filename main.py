#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip (<= 200 characters) for stressed
developers and AI coding agents to /output/entry.txt and prints it.
"""

import os

ENTRY = "Tip: The bug is never where you swear it is. Read the error twice, change one thing, test once. Your future self \u2014 and your agent's context window \u2014 will thank you."

assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
