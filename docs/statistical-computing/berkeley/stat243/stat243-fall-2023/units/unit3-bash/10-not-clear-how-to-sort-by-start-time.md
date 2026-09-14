---
title: not clear how to sort by start time
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit3-bash.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# not clear how to sort by start time

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

ps -o pid,command | grep python | cut -d' ' -f1 |  tail -n ${nJobs} | xargs kill
```

---

[← on a Mac](09-on-a-mac.md) · [Up: contents](index.md) · [4. bash shell challenges →](11-4-bash-shell-challenges.md)
