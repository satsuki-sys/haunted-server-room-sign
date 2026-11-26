#!/usr/bin/env python3
"""Writes the entry for 'Funniest Sign on a Haunted Server Room Door'.

One line, the funniest sign for the door of a haunted server room:
the 3 a.m. beeping is not a failing alarm but the previous admin,
still on shift, still keeping notes. Writes exactly the entry text
(no trailing newline) to entry.txt.
"""

import os

ENTRY = "The 3 a.m. beeping is not an alarm. It's the previous admin. He has notes."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
