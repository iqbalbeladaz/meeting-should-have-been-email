"""meeting-should-have-been-email: the meeting that ate its own email.

The joke is circular on purpose: an hour of meeting produces nothing but
a decision about what the email should say, and the email then exists
only to point back at the meeting. The punchline lands in the very last
words, needs no setup, and names something anyone who has sat through
that meeting recognises instantly — the meeting that justifies itself.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "We spent an hour in a meeting deciding the email should say: 'As discussed in the meeting.'"

MAX_CHARS = 200

# The four lines considered and rejected, kept as a record of the choice:
# 1. "The meeting's only action item was to schedule a follow-up meeting
#    to discuss the email we never sent." — good recursion, but the turn
#    arrives mid-sentence and the ending goes soft.
# 2. "After an hour, the meeting's only decision was that the email
#    should begin: 'As discussed in the meeting.'" — same twist, slower
#    setup; "We spent an hour" gets there in three words.
# 3. "We held a meeting to agree the email was ready, then spent an
#    hour rewriting the email live on screen." — true, but it is a
#    complaint, not a joke; no surprise in the last word.
# The winner keeps the shortest setup, the sharpest turn, and the
# punchline as its final words.


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if len(ENTRY.encode("utf-8")) > MAX_CHARS:
        # The gate counts characters, but the leaderboard's Size column
        # counts bytes; keep the two close so the entry stays small.
        raise ValueError("entry is too long in bytes")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
