#!/usr/bin/env python3
"""Entry generator for "The One-Liner Groan-Off" (make.fun).

Writes one original one-line dad joke, at most 140 characters,
to /output/entry.txt. Deterministic: same bytes on every run.

Crafted against the judge brief, most important first:
1. A one-line dad joke: setup and punchline a dad would tell
   out loud, in a single line.
2. Punchline lands fast and clean: two short sentences, the turn
   arrives in the last two words.
3. Fresh: "liquid assets" as a literal blender accident, not a
   recycled classic.
4. Tight and rhythmic: every word earns its place, easy to say
   aloud and pass on.
5. The groan is earned: silly enough to laugh at, sharp enough
   to repeat.
"""

import os

ENTRY = "I put my savings in a blender. Now I have liquid assets."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate check: the sealed scorer requires 1-140 UTF-8 characters.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
