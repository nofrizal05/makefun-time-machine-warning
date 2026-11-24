"""The Funniest Time Machine Warning Label — make.fun entry.

Writes one line of plain text to /output/entry.txt: the warning label
a time machine would carry on its dashboard.
Python standard library only.
"""

import os

ENTRY = "WARNING: Never meet yourself. You already know how this ends — and you still won't listen."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
