#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Absurd on first glance, sound on the second: a real product, a real payer, and a real reason the money flows.
"""
import os

ENTRY = "We rent professional criers to weep at strangers' funerals, and funeral homes pay per tear because grief sells sympathy."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
