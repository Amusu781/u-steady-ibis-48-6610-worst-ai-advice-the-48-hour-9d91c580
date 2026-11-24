#!/usr/bin/env python3
"""Worst AI Advice — make.fun bounty u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of confidently terrible AI-assistant advice (at most 140
characters) to $OUTPUT_DIR/entry.txt, default /output/entry.txt.
Deterministic, stdlib only, no network. Creates the output directory and
clears only its contents — never deletes the directory itself.
"""

import os

ENTRY = (
    "Great question! To free up phone storage, delete your Photos app "
    "— don't worry, your memories are safely backed up in your heart."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
