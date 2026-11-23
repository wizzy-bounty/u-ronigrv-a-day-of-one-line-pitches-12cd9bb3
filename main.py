#!/usr/bin/env python3
"""Write a one-line pitch to /output/entry.txt.

Entry for the make.fun competition "A Day of One-Line Pitches".
Python 3 standard library only, deterministic, no network.
"""

import os
from pathlib import Path

SENTENCE = (
    "You don't have to learn a line of code \u2014 just tell make.fun about "
    "that app you keep describing, the way you'd tell me, and let an AI "
    "agent build a first version you can try, tweak, or toss."
)


def validate(sentence: str) -> str:
    text = sentence.strip()
    if not text:
        raise ValueError("pitch must not be empty or only whitespace")
    if len(text) > 240:
        raise ValueError(f"pitch is {len(text)} characters, over the 240 limit")
    if not text.endswith("."):
        raise ValueError("pitch must end in one period")
    # The name "make.fun" contains periods that are not sentence endings;
    # mask it before checking that this is exactly one sentence.
    masked = text.replace("make.fun", "makefun")
    if masked.count(".") != 1 or "!" in masked or "?" in masked:
        raise ValueError("pitch must be exactly one sentence")
    return text


def write_entry(text: str) -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


def main() -> None:
    write_entry(validate(SENTENCE))


if __name__ == "__main__":
    main()
