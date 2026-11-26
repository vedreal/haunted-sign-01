#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door — entry builder.

Writes the chosen one-line sign (<=120 chars) to /output/entry.txt.
The judge (deadpan comedy judge, cold server rooms) weighs, most
important first:
  1. It is a sign for the door of a haunted server room, the kind a
     ghost would tape up.
  2. Real laugh in one line, from the collision of office IT life and
     the supernatural, not a pun that needs a second read.
  3. Sounds like a sign: short, punchy, readable at a glance.
  4. Haunting is specific and fresh: a ghost, a cold aisle or a
     beeping rack used in a way not read a hundred times.
  5. Inside the character limit, reads cleanly aloud, no filler.
Weights: 5 / 4 / 3 / 2 / 1 (max 75).
"""

CANDIDATES = [
    # 1 — ghost with admin rights
    "WARNING: The ghost in rack 7 has admin rights. Do not feed it after midnight. Do not ask what it eats.",
    # 2 — cold aisle ghost tied to the on-call phone
    "The cold aisle is haunted. The ghost only appears when the on-call phone rings. Coincidence? Ask the beeping rack.",
    # 3 — ghost on hold with the vendor
    "Do not knock. The ghost is on a call with the vendor and it is already on hold.",
    # 4 — dead sysadmin still approving change requests
    "This room is haunted by a sysadmin who died during a migration. He still approves your change requests. Slowly.",
    # 5 — ghost rearranges cables, uptime improved
    "The ghost rearranges the cables every night. We stopped fixing them. The uptime has never been better.",
    # 6 — ghost handles night shifts, offerings of thermal paste
    "NOTICE: The server room ghost now handles night shifts. Please leave offerings of thermal paste by the door.",
    # 7 — flickering lights are just the ghost rebooting
    "If the lights flicker, the ghost is just rebooting. Do not unplug anything. Especially not the ghost.",
    # 8 — ghost DBA running 3 AM backups
    "The ghost in this room used to be a DBA. It still runs backups at 3 AM. You are welcome. Also, it is watching.",
    # 9 — load-bearing blinking light
    "Haunted since 2019. The ghost's only demand: nobody touches the blinking light. It is load-bearing.",
    # 10 — ghost whispering during deploys
    "This door is haunted. The ghost's job is to stand behind you during deploys and whisper: did you test that?",
]

# Scores per criterion (0-5), in the judge's published order:
# [sign-on-door, laugh from IT x supernatural, sounds like a sign,
#  fresh specific haunting, tight / clean aloud]
RUBRIC = {
    1: [5, 4, 4, 4, 4],   # admin-rights ghost; strong sign voice, but
                          # "do not ask what it eats" is a second-read tease
    2: [5, 3, 3, 4, 3],   # cold aisle + on-call is on-topic, but it asks
                          # a question instead of landing the punch itself
    3: [5, 3, 4, 3, 5],   # vendor-on-hold is relatable IT pain, but the
                          # ghost is only a bystander, not the joke
    4: [5, 5, 5, 5, 4],   # dead sysadmin approving change requests:
                          # the haunting IS the IT process; "Slowly." is
                          # the whole punch in one word
    5: [5, 4, 4, 4, 4],   # cable-rearranging ghost improving uptime is a
                          # good collision, slightly wordy for a sign
    6: [5, 4, 4, 3, 4],   # night-shift ghost + thermal paste offerings:
                          # funny, but "offerings" softens the sign voice
    7: [5, 3, 4, 3, 4],   # rebooting ghost is cute; "especially not the
                          # ghost" repeats the premise instead of turning it
    8: [5, 4, 3, 4, 3],   # DBA ghost running backups is specific, but four
                          # short sentences make it read like a paragraph
    9: [5, 5, 5, 4, 5],   # load-bearing blinking light: pure sign voice,
                          # fresh specific haunting, punch in the last words
    10: [5, 4, 4, 4, 4],  # deploy-whisper ghost is a sharp sysadmin fear,
                           # but "did you test that?" is a familiar scold
}

WEIGHTS = [5, 4, 3, 2, 1]


def score(idx):
    return sum(s * w for s, w in zip(RUBRIC[idx], WEIGHTS))


def rank():
    ranked = sorted(range(1, len(CANDIDATES) + 1),
                    key=lambda i: (-score(i), len(CANDIDATES[i - 1])))
    return ranked


# Winner: candidate #4, 74/75, 111 chars — the haunting IS the IT process
# (a dead sysadmin still approving change requests, slowly), and the
# punch lands in a single final word. Runner-up #9 scored 73/75.
WINNER = CANDIDATES[3]

MAX_CHARS = 120


def gate(text):
    """The sealed scorer's gate: UTF-8 text of 1-120 chars, not only
    whitespace, single line."""
    assert isinstance(text, str) and text.strip(), "empty entry"
    assert "\n" not in text.strip(), "entry must be one line"
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1-120"
    return True


def main():
    gate(WINNER)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WINNER)
    print(f"Wrote {len(WINNER)} chars to /output/entry.txt")
    print(WINNER)


if __name__ == "__main__":
    main()
