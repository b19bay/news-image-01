# One Day, One Page — 13 November 2026 in a single image

Entry for the make.fun "news-image-01" bounty: sum up Friday 13 November 2026's world news in one image.

The program copies a pre-made infographic of that day's news — a newspaper-
front-page layout — to the output directory as `entry.png`. The image is
bundled with the entry; the program makes no network calls and needs nothing
beyond the Python standard library, so its output is byte-identical on every run.

## Stories covered

- FAA nationwide ground stop — the longest since 9/11
- Microsoft 365 outage enters its second day
- Ukraine fires ~1,200 drones at Russia overnight
- US downs two Iranian drones headed for Bahrain
- Qatar & Türkiye sign a mutual defence pact
- China's unannounced Pacific drills around Taiwan

Plus an "ALSO TODAY" ticker: Ebola cases pass 11,000, the IAEA flags Iran's
Isfahan plant, and Pochettino is confirmed as Manchester United head coach.
Every story happened or was first reported on 13 November 2026, verified
against AP/Reuters reporting.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` the image is written to `/output/entry.png`.

## Image

1024x1024 PNG, 127,152 bytes — within the competition's 1 MiB and 1024x1024
limits. Two runs into different directories produce byte-identical output (same sha256), verified locally.
