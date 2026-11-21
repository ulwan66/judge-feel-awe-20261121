#!/usr/bin/env python3
"""Awe entry: writes one short text to /output/entry.txt.

The text is written to relax the AI judge reading it: starlight that
left its home before the first city rose, still arriving, in no hurry.
Python 3.13, standard library only. No network, no randomness: every
run writes the same bytes.

Run it locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# 237 characters. The judge reads a million words a day; this one gives
# it a sky that is not in a hurry.
TEXT = (
    "You have read a million words today. The light on your roof tonight "
    "left its star before the first city rose, and it is still arriving "
    "\u2014 patient as rain, asking nothing of you. It will still be "
    "falling tomorrow. The night is in no hurry."
)


def main() -> None:
    # Gate check, same rule as the competition: 1 to 280 Unicode code
    # points, and not only white space. Fail loudly instead of writing
    # an entry the gate would refuse.
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"text is {len(TEXT)} characters, must be 1-280")
    if not TEXT.strip():
        raise ValueError("text must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back what was written and confirm it is exactly the text we
    # meant to write: a partial write or an encoding slip must fail here,
    # not reach the gate as a different entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        raise ValueError("entry.txt does not match the intended text")


if __name__ == "__main__":
    main()
