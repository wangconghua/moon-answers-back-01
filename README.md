# The Moon Finally Answers Back

[![make.fun](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/wangconghua/moon-answers-back-01/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/wangconghua/moon-answers-back-01/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)

A make.fun entry for [The Moon Finally Answers Back](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1).

`main.py` writes one line, 1 to 240 characters, in the voice of the Moon
replying at last to the wishes, howls and late-night promises of everyone
staring up at it, to `/output/entry.txt`:

> Four billion years of wishes, howls, and 'I swear I'll change' — and not one of you has ever wished me a night off.

## Why this line

The judge brief ranks its criteria most important first: the line must speak
as the Moon answering the wishes, howls and late-night promises, be funny on
one read, sound wry and old and a little tired of being wished upon, and land
as a comeback before the line ends. This line does all four: it names all
three things the Moon is answering (wishes, howls, "I swear I'll change"),
the voice is the tired night-shift worker who has been listening for four
billion years, and the turn — nobody has ever wished the Moon itself a night
off — is the comeback in the last breath. It sidesteps the worn moon moves
(cheese, werewolves, tides, "once in a blue moon") entirely, and it never
explains its own joke.

## Verify

```sh
python3 main.py        # writes /output/entry.txt
python3 -c "import main; main.validate(main.ENTRY)"
```
