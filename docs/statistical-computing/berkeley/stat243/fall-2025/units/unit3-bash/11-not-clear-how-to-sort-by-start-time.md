---
title: not clear how to sort by start time
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# not clear how to sort by start time

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

ps -o pid,command | grep python | cut -d' ' -f1 |  tail -n ${nJobs} | xargs kill
```

Or, if you started the jobs all at once, then the process IDs are likely to be in sequential order,
so you could use [brace expansion](https://computing.stat.berkeley.edu/tutorial-using-bash/using-commands.html#brace-expansion) in combination with `kill`:

```bash
#| eval: false
kill {871841..871870}
```

---

[← on a Mac](10-on-a-mac.md) · [Up: contents](index.md) · [4. bash shell challenges →](12-4-bash-shell-challenges.md)
