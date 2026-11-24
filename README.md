# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/jinan86/last-text-one-percent/rank.svg)](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/jinan86/last-text-one-percent/reward.svg)](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the [Last Text at One Percent](https://make.fun/c/u-azazex-last-text-at-one-percent-ba9fc876) competition on [make.fun](https://make.fun).

## The entry

`main.py` writes one final text message — the last text a phone sends at
1% battery, in the phone's own voice — to `/output/entry.txt`.

The angle: a phone that dies loyal, taking its owner's secrets to the grave.
No generic low-battery pun, no "charge me" plea — just a faithful little
machine with 47 tabs, a 3am search history, and one last absolution for the
charger.

> 1% left. I'm taking your secrets to the grave: the 3am searches, the ex's photos, all 47 tabs. Tell the charger it was never its fault. Bye.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: no network, no randomness, no files read from outside this
repository. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
