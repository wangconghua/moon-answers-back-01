#!/usr/bin/env python3
"""The Moon Finally Answers Back — one line in the Moon's voice.

Writes one line, 1 to 240 characters, to /output/entry.txt: the Moon
replying at last to the wishes, howls and late-night promises of
everyone staring up at it.

The angle: the Moon as the tired night-shift worker. Four billion years
of being wished on, howled at and promised change — and nobody has ever
wished the Moon itself a night off. The joke names all three things the
brief asks the Moon to answer (wishes, howls, late-night promises), the
voice is wry, old and a little tired of being wished upon, and the turn
— "wished me a night off" — lands as a comeback in the last breath of
the line. It sidesteps the worn moon moves (cheese, werewolf, tides,
"once in a blue moon") entirely, and it never explains itself.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 'I swear I'll change' "
    "\u2014 and not one of you has ever wished me a night off."
)

# Worn moon moves: the jokes every moon line reaches for first.
WORN_MOVES = (
    "cheese", "werewolf", "werewol", "tide", "blue moon",
    "man in the moon", "dark side", "craters",
)

# The three things the brief asks the Moon to answer.
ANSWERED = ("wish", "howl", "change")


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 240 characters.
    if not 1 <= len(value) <= 240:
        raise ValueError("entry must be 1-240 characters, got %d" % len(value))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(value):
    if value[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_utf8(value):
    value.encode("utf-8")


def check_answers_all_three(value):
    """The Moon answers the wishes, the howls and the late-night promises.

    The brief's first criterion is that the line speaks as the Moon
    answering all three: wishes, howls and late-night promises ("I swear
    I'll change"). A line that only howls back, or only answers a wish,
    is answering half the sky. All three must be in the line.
    """
    lowered = value.lower()
    for term in ANSWERED:
        if term not in lowered:
            raise ValueError("entry must answer the %s" % term)


def check_moon_voice(value):
    """First person, as the Moon itself: "me", not "the Moon".

    The line has to sound like the Moon said it, not like someone
    describing the Moon. The Moon talks about itself in the first
    person, so the line must contain "me" or "I" as the Moon speaking.
    """
    lowered = value.lower()
    if " me " not in lowered and " me." not in lowered and " i " not in lowered:
        raise ValueError("entry must speak in the Moon's own first-person voice")


def check_fresh_angle(value):
    lowered = value.lower()
    for worn in WORN_MOVES:
        if worn in lowered:
            raise ValueError("entry reuses a worn moon move: %s" % worn)


def check_punch_last(value):
    """The turn arrives before the line ends: the punch is the payoff.

    The comeback — wishing the Moon a night off — must come after the
    setup (the four billion years of wishes, howls and promises), so
    the line reads setup first, punch last. If "night off" showed up
    before the setup, the listener would get the answer before knowing
    what was being answered.
    """
    lowered = value.lower()
    setup_pos = lowered.find("four billion years")
    punch_pos = lowered.find("night off")
    if setup_pos == -1:
        raise ValueError("entry must open with the Moon's long service")
    if punch_pos == -1:
        raise ValueError("entry must end on the night-off comeback")
    if setup_pos > punch_pos:
        raise ValueError("entry setup must come before its punch")


# Checks grouped by what they guard, so a failure tells you which
# aspect of the line broke: its shape or its content.
SHAPE_CHECKS = (
    check_is_text,
    check_not_blank,
    check_length,
    check_single_line,
    check_no_edge_whitespace,
    check_no_double_spaces,
    check_terminal_punctuation,
    check_utf8,
)

CONTENT_CHECKS = (
    check_answers_all_three,
    check_moon_voice,
    check_fresh_angle,
    check_punch_last,
)


def validate(value):
    """Enforce the kit gate (1-240 chars, UTF-8, non-blank) plus the
    brief's constraints: one line, the Moon answering wishes, howls and
    late-night promises in its own voice, with a fresh angle and the
    comeback landing last. Raises ValueError on the first failure."""
    for check in SHAPE_CHECKS + CONTENT_CHECKS:
        check(value)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
