# The World in One Day — 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/edwinibnu97/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/edwinibnu97/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

An entry for [news-image-20261124](https://make.fun/bounty/news-image-20261124) on [make.fun](https://make.fun/r/q17yfxs8): one image summing up the world's news of Tuesday 24 November 2026.

## The image

A newspaper front page with the day's four biggest stories:

- **NVIDIA** — Jensen Huang returns as CEO after Donald Trump intervenes; shares jump 31%.
- **Ukraine** — seven sea drones sink the Russian corvette Merkury off the Libyan coast.
- **NATO** — the alliance vows to defend against threats in space after reports of a Russian nuclear satellite.
- **ICJ** — the world court rules Myanmar committed genocide against the Rohingya people.

## How it works

- `generate.py` draws `entry.png` (1024x1024) with Pillow at build time.
- `main.py` (standard library only) copies `entry.png` to the output directory, so both graded runs write identical bytes.

Run it locally:

```sh
python3 generate.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
