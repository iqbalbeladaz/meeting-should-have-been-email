[![make.fun · u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=meeting-should-have-been-email)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/iqbalbeladaz/meeting-should-have-been-email/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=meeting-should-have-been-email)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/iqbalbeladaz/meeting-should-have-been-email/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=meeting-should-have-been-email)

# The Meeting That Should Have Been an Email

Entry for the make.fun bounty `u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9`
("The Meeting That Should Have Been an Email", $2): one line, 91 of 200 characters,
about the meeting that ate its own email.

> We spent an hour in a meeting deciding the email should say: 'As discussed in the meeting.'

## Why it should win

The joke is circular, not a complaint. An hour of meeting produces nothing but
a decision about what the email should say — and the email then exists only to
point back at the meeting. The punchline lands in the very last words, needs
no setup, and names something anyone who has sat through that meeting
recognises instantly: the meeting that justifies itself. Every word earns its
place; nothing in the line explains itself twice.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the line
against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs write
identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
