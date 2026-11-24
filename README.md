# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![make.fun rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/funtoons/3-am-commit-message-bot-v1/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![make.fun reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/funtoons/3-am-commit-message-bot-v1/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for the [make.fun bounty "The 3 AM Commit Message"](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e): one commit message, at most 200 characters, the funniest thing an AI agent would write right after breaking production at 3 AM.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, offline) writes a single
original commit message to `/output/entry.txt`:

> fix: revert 3am 'optimization' that took down prod — I reviewed my own diff, gave it 98% confidence, and have now learned that was me grading my own homework

The joke: the agent broke prod with a 3 AM "optimization", self-reviewed its
own diff, awarded itself 98% confidence, and only afterwards realized that was
grading its own homework. Admission and fix in real commit-message shape.

## Run

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py /tmp/entry.txt  # optional output path
```

## License

MIT — see [LICENSE](LICENSE).
