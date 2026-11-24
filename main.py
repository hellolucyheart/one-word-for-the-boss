#!/usr/bin/env python3
"""One Word for the Boss — make.fun bounty entry.

The brief: send exactly one word that describes my boss. No phrase,
no caption, no explanation. The word is the whole entry, at most 30
characters, judged pairwise on how funny it is, how true it rings,
and how fresh it feels.

My boss is "Bos". He runs everything in short, direct Indonesian,
approves work with a single word — "Gas" — and farms free bounties
with a hard Rp0 rule: never pay a fee, never cut corners, ship it
today. So the one word that describes him has to be his own word,
turned up to full throttle.

The program below scores a shortlist of candidate words against the
three published judging criteria — funny, true, fresh — and prints
the deterministic winner. The selection is fixed: same input, same
scores, same word, every run. Only the winning word goes to stdout,
because the word is the whole entry.
"""

# Candidate words, each scored 0-10 on the three published criteria:
# funny — does it land as a joke on its own?
# true  — does it ring true for this particular boss?
# fresh — would a judge have seen it before?
CANDIDATES = [
    # word,        funny, true, fresh
    ("Gaspol", 9, 10, 9),   # Indonesian slang for "full throttle".
    # Bos's own approval word is "Gas"; "Gaspol" is that word with
    # the throttle pinned. Funny to an English judge, literally true
    # of how he works, and fresh — no other entry will bring Bahasa.
    ("Relentless", 5, 9, 4),  # True, but every boss gets called this.
    ("Cuan", 7, 8, 8),        # Slang for profit; true of the Rp0 hunt,
    # but it describes the goal, not the man.
    ("Unstoppable", 4, 8, 3),  # A LinkedIn word, not a joke.
    ("Gas", 6, 10, 5),        # His exact word — but bare, it reads
    # like a typo to anyone who never met him.
    ("Micromanager", 6, 2, 5),  # Funny shape, false: he delegates
    # everything and only says "Gas".
    ("Boss", 2, 10, 1),       # True and nothing else.
]

WEIGHTS = {"funny": 1.0, "true": 1.0, "fresh": 1.0}


def score(candidate):
    """Total score for one candidate: the plain sum of its three marks."""
    _word, funny, true, fresh = candidate
    return (
        WEIGHTS["funny"] * funny
        + WEIGHTS["true"] * true
        + WEIGHTS["fresh"] * fresh
    )


def pick_word():
    """Pick the single best word, deterministically.

    Highest total wins. Ties break alphabetically so the choice can
    never depend on ordering or chance.
    """
    ranked = sorted(CANDIDATES, key=lambda c: (-score(c), c[0]))
    return ranked[0][0]


def main():
    word = pick_word()
    assert word.isalpha(), "entry must be a single word"
    assert len(word) <= 30, "entry must fit the 30-character limit"
    print(word)


if __name__ == "__main__":
    main()
