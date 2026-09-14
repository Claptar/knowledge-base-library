---
title: Viewing Project History
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/10/moreOnGit.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Viewing Project History

**Source:** [`sections/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

At any point you can view the history of your changes using:

```bash
git log
```

If you also want to see complete diffs at each step, use

```bash
git log -p
```

Often the overview of the change is useful to get a feel of each step:

```bash
git log --stat --summary
```

For a prettier, more detailed graph (with several more options to look up):
```bash
git log --oneline --decorate --graph --all
```

---

[← Manual Pages](05-manual-pages.md) · [Up: contents](index.md) · [Undoing a Mistake: checkout, reset, and revert →](07-undoing-a-mistake-checkout-reset-and-revert.md)
