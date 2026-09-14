---
title: Pair exercises
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/09/collab_with_git.md
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/09/collab_with_git.md
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Pair exercises

**Source:** [`labs/09/collab_with_git.md`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/09/collab_with_git.md) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.md` (lossless)

Whoever got here first should do the first two items below while your partner
finishes up.

1. Create a new repo (just one of you, doesn't matter who) on
   [github.berkeley.edu](https://github.berkeley.edu/)
1. Add your partner(s) as a collaborator. This can be done by clicking the
  Settings option in the upper right and then selecting Collaborators on the
  menu on the left.
1. Each person create a new branch (call them something different), add a file
  or two to your branch and practice merging to the `main` branch. You can do
  either merge on the command line or use a pull request. See section **Managing
  Branches** above for the commands. (Make sure to use `git pull` before pushing
  your merge to the remote repo if you do it through the command line to avoid
  merge conflicts.)
1. Test what happens when your remote repository is ahead of your local
  repository, but you already staged new changes.
  - Have one partner push a new commit to the remote repo
  - Have the other partner try to add, commit, and push new changes without pulling
  the most recent update and see what happens.
  - Resolve the merge conflict.  You can do this by calling `git pull` and merging
  the repositories or by using `git reset --soft` as described in the **Reset**
  section below.
1. Test what happens when a collaborator (or you on a different computer) edits
  the same file?

---

[← Advanced Git features for collaboration](04-advanced-git-features-for-collaboration.md) · [Up: contents](index.md) · [Appendix: More Useful Git Functionality →](06-appendix-more-useful-git-functionality.md)
