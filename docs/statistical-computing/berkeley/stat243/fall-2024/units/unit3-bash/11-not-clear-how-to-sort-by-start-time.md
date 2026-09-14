---
title: not clear how to sort by start time
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# not clear how to sort by start time

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

ps -o pid,command | grep python | cut -d' ' -f1 |  tail -n ${nJobs} | xargs kill
```

---

[← on a Mac](10-on-a-mac.md) · [Up: contents](index.md) · [4. bash shell challenges →](12-4-bash-shell-challenges.md)
