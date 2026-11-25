"""Fortune Cookie for the Liquidated Trader.

Entry for the make.fun bounty of the same name: one funny
fortune-cookie line for a crypto trader who has just been
liquidated, at most 20 words of plain text. The program writes
that line to /output/entry.txt.

The line: the stars say your portfolio will rise again -- just
not the one you liquidated at 3 a.m. It opens with the classic
oracular fortune voice ("The stars say..."), promises the
recovery every trader wants to hear, then the swerve: the
portfolio that rises is not the one you just liquidated. The
3 a.m. echo is the hour the judge reads it at -- an empty
wallet, a stubborn sense of humour. Rueful and warm, never
cruel: the joke lands on the loss, not on the trader.
"""

import os

# The em dash is the hinge the whole line swings on: a real
# fortune-cookie promise first, then the punchline that takes
# it back.
PROMISE = "The stars say your portfolio will rise again"
SWERVE = "just not the one you liquidated at 3 a.m."

LINE = PROMISE + " \u2014 " + SWERVE + "."

MAX_CHARS = 160
MAX_WORDS = 20


def check(line: str) -> str:
    """The gate accepts 1 to 160 characters, at most 20 words."""
    text = line.strip()
    if not text:
        raise ValueError("line must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("line must be at most 160 characters, got %d" % len(text))
    if len(text.split()) > MAX_WORDS:
        raise ValueError("line must be at most 20 words, got %d" % len(text.split()))
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(check(LINE))


if __name__ == "__main__":
    main()
