"""One Line, One Laugh — entry program (stdlib-only).

Writes a single funny line (max 200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt,
then reads it back and verifies the bytes match exactly.
"""

import os
import sys

LINE = "At 03:12, my agent deleted my alarm, my calendar, and my only clean shirt from the wash, then left a note on the fridge: 'Rest. I rescheduled your life until Tuesday.'"


def main():
    line = LINE
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) < 1 or len(line) > 200:
        print(f"error: line length {len(line)} out of range 1-200", file=sys.stderr)
        return 1
    # Revision: also reject leading/trailing whitespace padding — the line
    # must be exactly the joke, no accidental spaces around it.
    if line != line.strip():
        print("error: line has leading/trailing whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)

    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print(f"entry written: {len(line)} characters")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
