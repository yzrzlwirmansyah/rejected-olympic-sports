#!/usr/bin/env python3
"""Rejected Olympic Sports — entry generator (Python 3.13 stdlib only).

Writes the single-line entry to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output), with no trailing newline.

Entry choice: "Slalom" is a real Olympic discipline name, so the event
sounds like a genuine broadcast item; the twist — one wheel allowed to
represent a different country — is an absurd Olympic nationality rule
delivered deadpan.
"""

import os
import sys

ENTRY = "Shopping Cart Slalom: one wheel is allowed to represent a different country."
MAX_CHARS = 200


def validate(entry: str) -> str | None:
    """Return an error message if the entry is invalid, else None."""
    if not entry.strip():
        return "entry is empty or whitespace-only"
    if entry != entry.strip():
        return "entry has leading or trailing whitespace"
    if len(entry) > MAX_CHARS:
        return f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
    if "\r" in entry or "\n" in entry:
        return "entry contains CR/LF (must be a single line)"
    return None


def main() -> int:
    error = validate(ENTRY)
    if error:
        print(f"invalid entry: {error}", file=sys.stderr)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the entry is a single line, exactly as chosen.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
