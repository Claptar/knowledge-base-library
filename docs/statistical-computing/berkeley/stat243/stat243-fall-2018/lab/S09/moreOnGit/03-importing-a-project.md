---
title: Importing A Project
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S09/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Importing A Project

**Source:** [`lab/S09/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Assume you have a tarball linReg.tar.gz with your initial work. You can place it under Git revision control as follows.

```bash
tar xzf project.tar.gz
cd project
git init
```
Git will reply
```bash
Initialized empty Git repository in .git/
```

You've now initialized the working directory-you may notice a new directory created, named ".git".

Next, tell Git to take a snapshot of the contents of all files under the current directory (note the .), with git add:

```bash
git add .
```

This snapshot is now stored in a temporary staging area which Git calls the *index*. You can permanently store the contents of the index in the repository with `git commit`:

```bash
git commit -m "add"
```

This will prompt you for a commit message. You've now stored the first version of your project in Git.

---

[← Getting Help](02-getting-help.md) · [Up: contents](index.md) · [Making Changes →](04-making-changes.md)
