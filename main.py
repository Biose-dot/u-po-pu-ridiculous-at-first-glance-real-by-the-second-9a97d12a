#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Absurd on first glance, sound on the second: a real product, a real payer, and a real reason the money flows — quiet as a subscription.
"""
import os

ENTRY = 'We sell bottled quiet harvested from empty libraries to open-plan offices, and exhausted managers pay monthly so their teams can hear themselves think.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
