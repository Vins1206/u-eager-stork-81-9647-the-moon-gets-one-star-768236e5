"""The Moon Gets One Star - one-star review of the Moon.

Writes a single hand-written one-star review (91 characters) to
/output/entry.txt. Pure standard library, no input, no network.
"""

from pathlib import Path

REVIEW = "One star. It follows me everywhere, pays no rent, and vanishes once a month without a word."


def main() -> None:
    # Gate in the competition rules: 1 to 120 characters, not only whitespace.
    # The chosen line is 91 characters, so this guard can never fire on it,
    # but it keeps a future typo from silently producing an invalid entry.
    assert 1 <= len(REVIEW) <= 120 and REVIEW.strip(), "review must be 1-120 chars"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_dir.joinpath("entry.txt").write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
