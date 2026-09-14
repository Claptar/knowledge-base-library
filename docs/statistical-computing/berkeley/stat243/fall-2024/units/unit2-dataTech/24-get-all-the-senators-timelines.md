---
title: get all the senators' timelines
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit2-dataTech.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit2-dataTech.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# get all the senators' timelines

**Source:** [`units/unit2-dataTech.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit2-dataTech.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

names = [d["screen_name"] for d in senators["users"]]
timelines = [api.statuses.user_timeline(screen_name=name, count = 500)
             for name in names]

---

[← get the list of senators](23-get-the-list-of-senators.md) · [Up: contents](index.md) · [save information out to JSON →](25-save-information-out-to-json.md)
