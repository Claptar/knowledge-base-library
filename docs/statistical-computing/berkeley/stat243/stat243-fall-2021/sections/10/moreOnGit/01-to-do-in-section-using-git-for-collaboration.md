---
title: 'To Do in Section: Using Git For Collaboration'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/10/moreOnGit.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# To Do in Section: Using Git For Collaboration

```r
knitr::opts_chunk$set(echo = TRUE)
knitr::opts_chunk$set(eval = FALSE)
```
In our very first section of the semester, we discussed how to use Git and GitHub. Now that you have a semester's worth of experience pulling from and committing to a remote repository, we will explore some of the more advanced functionally of Git and
GitHub. We will practice a number of the tools that are useful when collaborating
with others on a GitHub repository, which could prove useful when working on your final project.  There is additional information about using Git for collaboration and various other features in the appendix at the end for
those of you that are curious.

In section we will split into groups of 2 (or 3 if necessary) to practice creating
branches and merging.

We will do this as a partner exercise to practice collaborating with git and
fixing issues that may arise during collaboration.
Please read the sections on advanced Git functionality first and then do the following exercises:

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

## Useful References

[Berkeley SCF Git Basics](https://htmlpreview.github.io/?https://github.com/berkeley-scf/tutorial-git-basics/blob/master/git-intro.html)
[Software Carpentry Collection of Information on Git](https://swcarpentry.github.io/git-novice/)
[Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts)
[Interactive Branching Tutorial](https://learngitbranching.js.org/)
[Advanced Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_advanced_merging)
[Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things)

## Git Tracks Contents, Not Files

Many revision control systems provide an `add` command that tells the system to
start tracking changes to a new file. Git's `add` command does something simpler
and more powerful: `git add` is used both for new and newly modified files, and
in both cases it takes a snapshot of the given files and stages that content in
the index, ready for inclusion in the next commit.

## Manual Pages

You can get documentation for a command such as `git log --graph` with:

```bash
man git-log
```
or
```bash
git help log
```

## Viewing Project History
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

[Up: contents](index.md) · [Undoing a Mistake: checkout, reset, and revert →](02-undoing-a-mistake-checkout-reset-and-revert.md)
