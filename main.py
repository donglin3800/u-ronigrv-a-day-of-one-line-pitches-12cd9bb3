#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt.

The sentence lives here as a tuple of four clauses; the program
joins them with single spaces at run time, checks the result fits
the bounty cap of 240 characters, and writes it out with one
trailing newline. Standard library only, no input, no network,
no clock: every run produces the same bytes.
"""

import os

CLAUSES = (
    "If you can explain your app idea to a friend,",
    "you can have an AI agent build it — just describe it",
    "in plain words on make.fun, and get a working first",
    "version without writing a line of code.",
)

TARGET = "/output/entry.txt"


def assemble(clauses):
    text = " ".join(clauses)
    if not 1 <= len(text) <= 240:
        raise SystemExit("pitch is %d characters, not 1-240" % len(text))
    if "\n" in text or not text.endswith("."):
        raise SystemExit("pitch must be one sentence on one line")
    return text


def place(text):
    folder = os.path.dirname(TARGET)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
        handle.write("\n")


place(assemble(CLAUSES))
