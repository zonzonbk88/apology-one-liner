"""Write the winning apology one-liner to /output/entry.txt.

Standard library only. No network, no file reads outside this repo.
The entry is a single line, 1-159 characters, written with no trailing
newline so the file content is exactly the line itself.
"""

import os

LINE = "I emailed your boss the draft named FINAL_final_v2_DO_NOT_SEND \u2014 I read the filename as a dare."


def main():
    # Enforce the bounty gate: one line, 1-159 characters, not only
    # whitespace, and no trailing newline in the file.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 159, f"entry is {len(LINE)} chars, must be 1-159"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
