---
title: Git Tracks Contents, Not Files
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/10/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Git Tracks Contents, Not Files

**Source:** [`section/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Many revision control systems provide an `add` command that tells the system to
start tracking changes to a new file. Git's `add` command does something simpler
and more powerful: `git add` is used both for new and newly modified files, and
in both cases it takes a snapshot of the given files and stages that content in
the index, ready for inclusion in the next commit.

---

[← Making Changes](04-making-changes.md) · [Up: contents](index.md) · [Undoing a Mistake →](06-undoing-a-mistake.md)
