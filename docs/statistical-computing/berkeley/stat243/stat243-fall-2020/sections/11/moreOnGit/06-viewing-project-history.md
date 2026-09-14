---
title: Viewing Project History
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/11/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Viewing Project History

**Source:** [`sections/11/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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
