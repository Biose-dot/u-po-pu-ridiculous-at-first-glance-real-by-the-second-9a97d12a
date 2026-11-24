# Absurd-sounding but real startup pitch, one sentence (final v2).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "We rent out professional line-standers to busy shoppers who pay us to queue for hours so they never have to wait for anything ever again."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
