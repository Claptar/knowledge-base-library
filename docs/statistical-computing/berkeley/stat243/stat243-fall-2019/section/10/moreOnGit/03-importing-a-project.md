---
title: Importing A Project
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/10/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Importing A Project

**Source:** [`section/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

I __do not__ recommend this process for initiating a new project. These steps are simple,
until you get to creating the remote repository. Then, just like in the intro tutorial,
you have you setup a new repository on Github and link it to the local one.
It is easier to create the repo on Github, clone the empty repo locally, then put
files in it as desired.

Assume you have a tarball linReg.tar.gz with your initial work. You can place it
under Git revision control as follows.

```bash
tar xzf project.tar.gz
cd project
git init
```
Git will reply (something along the lines)
```bash
Initialized empty Git repository in .git/
```

You've now initialized the working directory-you may notice a new directory created,
named ".git".

Next, tell Git to take a snapshot of the contents of all files under the current
directory (note the .), with git add:

```bash
git add .
```

This snapshot is now stored in a temporary staging area which Git calls the *index*.
You can permanently store the contents of the index in the repository with `git commit`:

```bash
git commit -m "add"
```

This will prompt you for a commit message. You've now stored the first version of
your project in Git.

---

[← Manual Pages](02-manual-pages.md) · [Up: contents](index.md) · [Making Changes →](04-making-changes.md)
