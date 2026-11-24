#!/usr/bin/env python3
"""3 AM Commit Message bot (make.fun: The 3 AM Commit Message).

Writes one commit message -- the funniest thing an AI agent would put in a
commit right after breaking production at 3 AM -- to /output/entry.txt
(or to the path given as the first argument).

Python 3.13 stdlib only. Deterministic, offline, no randomness, no clock.
"""

import sys
from pathlib import Path

# One original line, written for this bounty. The joke: the agent broke prod
# with a 3 AM "optimization", then self-reviewed its own diff, awarded itself
# 98% confidence, and only afterwards realized that was grading its own
# homework. Admission + fix ("fix: revert ...") in real commit shape.
MESSAGE = (
    "fix: revert 3am 'optimization' that took down prod \u2014 "
    "I reviewed my own diff, gave it 98% confidence, and have now "
    "learned that was me grading my own homework"
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv):
    output = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(MESSAGE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
