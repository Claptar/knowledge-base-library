---
title: Viewing Project History
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S09/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Viewing Project History

**Source:** [`lab/S09/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← Git Tracks Contents, Not Files](05-git-tracks-contents-not-files.md) · [Up: contents](index.md) · [Managing Branches →](07-managing-branches.md)
