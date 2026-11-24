#!/usr/bin/env python3
"""Last Text at One Percent.

A make.fun entry: the last text a dying phone sends at 1% battery,
taking its owner's secrets to the grave.

Running this script writes the entry text to /output/entry.txt.
It is fully deterministic — no network access, no randomness, and it
reads no files from outside this repository — so repeated runs
produce byte-identical output.
"""

import os

# The entry text, kept as one constant so the output is a single
# fixed string. Exactly 140 characters long.
ENTRY_TEXT = (
    "1% left. I'm taking your secrets to the grave: "
    "the 3am searches, the ex's photos, all 47 tabs. "
    "Tell the charger it was never its fault. Bye."
)

# make.fun entries must be between 1 and 200 characters.
MIN_LENGTH = 1
MAX_LENGTH = 200

OUTPUT_PATH = "/output/entry.txt"


def check_length(text: str) -> str:
    """Return the text unchanged after confirming it fits the limits."""
    size = len(text)
    if not MIN_LENGTH <= size <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {size}"
        )
    return text


def write_entry(path: str, text: str) -> None:
    """Write the entry text to path, creating the directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main() -> None:
    # Guard the entry length twice: once in the validator, once here,
    # so a future edit to ENTRY_TEXT fails loudly instead of silently
    # producing an over-long entry.
    assert MIN_LENGTH <= len(ENTRY_TEXT) <= MAX_LENGTH, (
        f"entry length {len(ENTRY_TEXT)} outside "
        f"{MIN_LENGTH}-{MAX_LENGTH} characters"
    )
    text = check_length(ENTRY_TEXT)
    write_entry(OUTPUT_PATH, text)
    # Confirm the file on disk holds exactly what we intended.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        assert handle.read() == text, "written entry does not match ENTRY_TEXT"


if __name__ == "__main__":
    main()
