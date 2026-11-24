"""Write the most honest status page line for a total server outage.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

LINE = (
    "All our servers are down and I cannot reach any of them, "
    "so I cannot tell whether your last changes were saved "
    "or when service will return."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
