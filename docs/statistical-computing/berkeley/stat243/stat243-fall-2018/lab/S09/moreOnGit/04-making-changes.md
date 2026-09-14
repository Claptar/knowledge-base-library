---
title: Making Changes
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S09/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Making Changes

**Source:** [`lab/S09/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```bash
git add file1 file2 file3
```

You are now ready to commit. You can see what is about to be committed using `git diff` with the `--cached` option:

```bash
git diff --cached
```

(Without --cached, git diff will show you any changes that you've made but not yet added to the index.)

You can also get a brief summary of the situation with `git status`:

```bash
git status
```

Alternatively, instead of running `git add` before `git commit`, you can use:

```bash
git commit -a
```

which will automatically notice any modified (but not new) files, add them to the index, and commit, all in one step.

---

[← Importing A Project](03-importing-a-project.md) · [Up: contents](index.md) · [Git Tracks Contents, Not Files →](05-git-tracks-contents-not-files.md)
