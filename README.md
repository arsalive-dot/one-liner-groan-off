# The One-Liner Groan-Off — Entry

[![make.fun · u-alfasurya91-the-one-liner-groan-off-5a1febd5](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/arsalive-dot/one-liner-groan-off/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/arsalive-dot/one-liner-groan-off/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-the-one-liner-groan-off-5a1febd5)

Entry for the [The One-Liner Groan-Off](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5) bounty on [make.fun](https://make.fun): one original one-line dad joke, at most 140 characters, written for a judge model to pick head to head.

## The entry

> I put my savings in a blender. Now I have liquid assets.

## How it works

`main.py` (Python 3, standard library only) writes the joke to `/output/entry.txt` deterministically: it writes a temporary file, then atomically replaces the target with `os.replace` and sets mode `644`. It also asserts the gate itself (1–140 characters, not only whitespace) before writing. Run it twice and the output is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
