---
title: Viewing Project History
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/10/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Viewing Project History

**Source:** [`section/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

[← Undoing a Mistake](06-undoing-a-mistake.md) · [Up: contents](index.md) · [Managing Branches →](08-managing-branches.md)
