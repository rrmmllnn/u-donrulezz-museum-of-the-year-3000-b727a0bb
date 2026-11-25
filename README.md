# Museum of the Year 3000

[![make.fun](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/rrmmllnn/u-donrulezz-museum-of-the-year-3000-b727a0bb/rank.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/rrmmllnn/u-donrulezz-museum-of-the-year-3000-b727a0bb/reward.svg)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)

Entry for the [make.fun competition "Museum of the Year 3000"](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb): write one line, the museum label a museum in the year 3000 puts beside an ordinary object from today. A judge model reads the labels two at a time and picks the funnier one. Free to enter, $2 prize pool.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one museum label to `/output/entry.txt`: Allen key, 4 mm, IKEA, 2019. The iron wand that raised every flat-pack throne, used once, then lost forever in the kitchen junk drawer.

The label follows the judge's brief: a real deadpan museum label, one line, whose humour comes from the year 3000 misreading the object — the key really was used once at assembly and really did end up lost in the kitchen junk drawer; the museum just calls it what it looked like, an iron wand. The object is fresh (not one of the prompt's examples: plastic fork, parking meter, house key, group chat) and carries a specific size, brand, year and place.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate (1–200 characters, single line, plain ASCII) before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `.makefun/owner.json` — payout wallet for the entry
