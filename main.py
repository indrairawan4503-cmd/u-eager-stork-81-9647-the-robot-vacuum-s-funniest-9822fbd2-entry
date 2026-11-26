#!/usr/bin/env python3
"""Robot vacuum's excuse for missing a spot (variant B: pet hair / rug conspiracy).

Writes one line to /output/entry.txt first; any repo-root copy is best-effort
inside try/except because the grader sandbox mounts the repo read-only.
Deterministic: no randomness, no time, no network, no file reads outside the repo.
"""

import os

ENTRY = "The rug under the couch reached pet-hair critical mass and unionized, so my suction has formally surrendered."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Best-effort local copy; must never crash the run in a read-only sandbox.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
