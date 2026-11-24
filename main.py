"""Last Text at One Percent — a make.fun entry.

Writes the funniest final text message a dying phone sends at 1% battery
to /output/entry.txt. Deterministic: no network, no randomness, no files
read from outside this repository. Running it twice produces byte-identical
output.
"""

import os

TEXT = (
    "1% left. I'm taking your secrets to the grave: "
    "the 3am searches, the ex's photos, all 47 tabs. "
    "Tell the charger it was never its fault. Bye."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
