---
title: not clear how to sort by start time
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit3-bash.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# not clear how to sort by start time

**Source:** [`units/unit3-bash.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

ps -o pid,command | grep exec/R | cut -d' ' -f1 |  tail -n ${nJobs} | xargs kill
```

---

[← on a Mac](06-on-a-mac.md) · [Up: contents](index.md) · [4. bash shell challenges →](08-4-bash-shell-challenges.md)
