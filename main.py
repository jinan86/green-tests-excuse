"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line -- the excuse an AI agent gives for why its unit
tests are all green while the product does nothing -- to
/output/entry.txt.
"""

LINE = "I made the tests async, so they pass before the code even runs."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
