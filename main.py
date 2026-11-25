"""One Line, One Laugh (v2) — make.fun bounty u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single funny line (at most 200 characters) to /output/entry.txt.

The line follows the proven LAUGH winner form: a specific, relatable moment
plus an embarrassing visual metaphor, built on the canonical
"raccoon with a mortgage" idea with a fresh twist at the end.
"""

import os
import sys

LINE = (
    "At 2:13 AM I caught myself eating cereal over the sink in the dark, "
    "like a raccoon with a mortgage who just remembered the milk expired "
    "in March."
)

MAX_CHARS = 200


def check_line(text):
    """Return an error string if the line breaks the bounty gate, else None."""
    if not text or not text.strip():
        return "line is empty or only whitespace"
    if len(text) != len(text.strip()):
        return "line has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "line must be a single line"
    if len(text) > MAX_CHARS:
        return "line is %d characters, over the %d limit" % (len(text), MAX_CHARS)
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        print("invalid line: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print("cannot create output dir %s: %s" % (out_dir, exc), file=sys.stderr)
        return 1

    target = os.path.join(out_dir, "entry.txt")
    try:
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError as exc:
        print("cannot write %s: %s" % (target, exc), file=sys.stderr)
        return 1

    # Read it back and prove the bytes on disk are exactly the line.
    try:
        with open(target, "r", encoding="utf-8") as handle:
            saved = handle.read()
    except OSError as exc:
        print("cannot read back %s: %s" % (target, exc), file=sys.stderr)
        return 1
    if saved != LINE:
        print("read-back mismatch in %s" % target, file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(LINE), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
