---
title: 'To Do in Section: Using Git For Collaboration'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/11/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# To Do in Section: Using Git For Collaboration

**Source:** [`sections/11/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We will do this as a partner exercise to practice collaborating with git and
fixing issues that may arise during collaboration.

1) Create a new repo (just one of you, doesn't matter who)
2) Add your partner(s) as a collaborator.  This can be done by clicking the Settings
option in the upper right and then selecting Collaborators on the menu on the left.
3) Each person create a new branch (call them something different), add a file
or two to your branch and practice
merging to the `master` branch.  You can do either merge on the command line or
use a pull request.  See section **Managing Branches** below for the commands.  Make
sure to use `git pull` before pushing your merge to the remote repo if you
do it through the command line to avoid merge conflicts.
4) Test what happens when your remote repository is ahead of your local
repository, but you already staged new changes.
  * Have one partner push a new commit to the remote repo
  * Have the other partner try to add, commit, and push new changes without pulling
  the most recent update and see what happens.
  * Resolve the merge conflict.  You can do this by calling `git pull` and merging
  the repositories or by using `git reset --soft` as described in the **Reset**
  section below.
5) Test what happens when a collaborator (or you on a different computer) edits
the same file?

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Useful References →](03-useful-references.md)
