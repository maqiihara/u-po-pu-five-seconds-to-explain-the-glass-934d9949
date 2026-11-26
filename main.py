#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.
"""

import os

ENTRY = (
    "The glass kept staring at me like it paid the rent, so I reminded it "
    "who actually runs this house \u2014 and it fell for it."
)


def validate(text: str) -> str:
    """Mirror the sealed gate: UTF-8 text of 1-200 chars, not only
    whitespace, exactly one sentence. Raises ValueError otherwise."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters")
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
