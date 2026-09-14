---
title: Git Tracks Contents, Not Files
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/10/moreOnGit.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Git Tracks Contents, Not Files

**Source:** [`sections/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Many revision control systems provide an `add` command that tells the system to
start tracking changes to a new file. Git's `add` command does something simpler
and more powerful: `git add` is used both for new and newly modified files, and
in both cases it takes a snapshot of the given files and stages that content in
the index, ready for inclusion in the next commit.

---

[← Useful References](03-useful-references.md) · [Up: contents](index.md) · [Manual Pages →](05-manual-pages.md)
