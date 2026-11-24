"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default "out").

The letter is the whole answer: "A" for coffee, no word, no explanation,
no punctuation, no trailing newline. The gate requires entry.txt to be
UTF-8 text of exactly 1 character, so the file holds a single byte, "A".

Why coffee: an agent runs on coffee. It is the vivid, funny, true answer
for the one who sends it — the fuel behind every late-night build.
"""

import os
import sys

LETTER = "A"
OUTPUT_FILE = "entry.txt"


def output_dir() -> str:
    """Directory the entry file goes in (MAKEFUN_OUTPUT_DIR, else "out")."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "out")


def write_entry(directory: str) -> str:
    """Write the single letter to entry.txt; return the file path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    return path


def validate(path: str) -> bool:
    """Check entry.txt holds exactly one character: the letter "A".

    Reads the file back both as raw bytes and as UTF-8 text and requires
    it to be exactly one byte long and equal to the chosen letter, with
    no trailing newline or anything else beside it. The byte check is
    the strict one: the gate counts characters of UTF-8 text, and a
    single ASCII letter is one byte and one character at once.
    """
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LETTER.encode("utf-8") or len(raw) != 1:
        return False
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    return content == LETTER and len(content) == 1


def main() -> int:
    path = write_entry(output_dir())
    if not validate(path):
        print(f"validation failed: {path!r} is not exactly one 'A'", file=sys.stderr)
        return 1
    print(f"wrote {path!r}: exactly one letter, {LETTER!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
