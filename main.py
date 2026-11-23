"""One Letter: Coffee or Tea -- make.fun entry.

Writes exactly one character, "A" (coffee), to the entry file.
The gate requires 1 to 1 characters, so no trailing newline is written.
"""

import os

LETTER = "A"


def main():
    # The gate is exactly 1 character: guard the letter before writing.
    assert len(LETTER) == 1, "entry must be exactly one character"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
