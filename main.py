"""Say What Actually Broke — make.fun entry.

Writes one single line of software error copy to /output/entry.txt:
at most 200 characters, naming the real failure in plain words,
telling the user what to do next, and landing one joke on a single
read. The text is a fixed constant: no input is read, no file is
read, no randomness, no clock, no network — running this program
twice always produces byte-identical output.
"""

TEXT = (
    "Your session expired while you were reading this sentence. "
    "Sign in again and we'll put you right back where you left off."
)


def main() -> None:
    """Write TEXT to /output/entry.txt with no trailing newline.

    ENTRY_OUTPUT may override the destination for local testing only;
    the grader runs without it, so the default is /output/entry.txt.
    """
    import os
    from pathlib import Path

    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
