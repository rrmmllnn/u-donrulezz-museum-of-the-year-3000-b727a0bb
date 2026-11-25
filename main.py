#!/usr/bin/env python3
"""Museum of the Year 3000 — entry program.

Writes a single-line museum label, as a museum in the year 3000 would
place it beside an ordinary object from today, to /output/entry.txt
(1-200 chars, one line, English, original).
Deterministic: the same line on every run.

The object is an IKEA Allen key: the judge's brief rewards a label whose
humour comes from the year 3000 misreading the object, saying something
true and absurd about what it was for. The key really was used once, at
assembly, and really did end up lost in the kitchen junk drawer — the
museum just calls it what it looked like: an iron wand.
"""

import os

ENTRY = (
    "Allen key, 4 mm, IKEA, 2019. The iron wand that raised every "
    "flat-pack throne, used once, then lost forever in the kitchen "
    "junk drawer."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    assert "\n" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must have no leading/trailing space"
    assert all(ord(c) < 128 for c in line), "entry must be plain ASCII"
    out_path = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    print(f"Wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
