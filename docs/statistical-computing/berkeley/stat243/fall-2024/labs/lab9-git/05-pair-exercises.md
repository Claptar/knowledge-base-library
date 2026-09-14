---
title: Pair exercises
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab9-git.qmd
source_file: sources/berkeley-stat243/fall-2024/labs/lab9-git.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Pair exercises

**Source:** [`labs/lab9-git.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab9-git.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Whoever got here first should do the first two items below while your partner
finishes up.

1. Create a new repo (just one of you, doesn't matter who) on
   [github.berkeley.edu](https://github.berkeley.edu/)
2. Add your partner(s) as a collaborator. This can be done by clicking the
  Settings option in the upper right and then selecting Collaborators on the
  menu on the left.
3. Each person create a new branch (call them something different), add a file
  or two to your branch and practice merging to the `main` branch. You can do
  either merge on the command line or use a pull request. See section **Managing
  Branches** above for the commands. (Make sure to use `git pull` before pushing
  your merge to the remote repo if you do it through the command line to avoid
  merge conflicts.)
4. Test what happens when your remote repository is ahead of your local
  repository, but you already staged new changes.
  - Have one partner push a new commit to the remote repo
  - Have the other partner try to add, commit, and push new changes without pulling
  the most recent update and see what happens.
  - Resolve the merge conflict.  You can do this by calling `git pull` and merging
  the repositories or by using `git reset --soft` as described in the **Reset**
  section below.
5. Test what happens when a collaborator (or you on a different computer) edits
  the same file.
6. After all commits are pushed by your collaborator and you, check the git
  history via `git log` or on GitHub.

We are now going to configure Git to rebase a branch on top of the fetched
branch on `git pull`, instead of the default merging behavior, and to
automatically "stash" changes before every rebase and apply after the rebase is
complete. Recall the meaning of stashing in the [git branch](04-advanced-git-features-for-collaboration.md#git-branch)
section above.

1. Run `git config pull.rebase true` and `git config rebase.autoStash true`.
2. Test again what happens when your remote repository is ahead of your local
  repository, but you already staged new changes. Consider three cases, in which
  a collaborator pushed changes to: (a) a different file; (b) different lines of
  the same file; (c) and the same lines of the same file.
3. After all commits are pushed by your collaborator and you, check the git history.
4. Discuss all the differences compared to merging.

---

[← Advanced Git features for collaboration](04-advanced-git-features-for-collaboration.md) · [Up: contents](index.md) · [Appendix: More Useful Git Functionality →](06-appendix-more-useful-git-functionality.md)
