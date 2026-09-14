---
title: Managing Branches
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/10/moreOnGit.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Managing Branches

**Source:** [`sections/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/10/moreOnGit.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

A single Git repository can maintain multiple branches of development. To create
a new branch named "experimental", use

```bash
git branch experimental
```

If you now run
```bash
git branch
```

The "experimental" branch is the one you just created, and the "master" branch
is a default branch that was created for you automatically. The asterisk marks
the branch you are currently on; type

```bash
git checkout experimental
```

to switch to the experimental branch. Now edit a file, commit the change, and
switch back to the master branch:

```bash
git add file
git commit -m "edited file"
```

Alternatively, one can "stash" the changes using `git stash`.  This saves your
changes for later, and then reverts the working tree to the last
HEAD (whatever the last commit was). This allows you to keep working without the
changes being applied to any files.  You can apply those changes later
using `git stash pop`, which applies the changes and removes them from your
stash. Or, if you wish to apply the changes to multiple
branches, you can use `git stash apply`, which applies the changes but leaves them
in your stash.

Now, you can switch back to the master branch.
```bash
git checkout master
```

Check that the change you made is no longer visible, since it was made on the
experimental branch and you're back on the master branch.

You can make a different change on the master branch and commit. At this point
the two branches have diverged, with different changes made in each. To merge
the changes made in experimental into master, run:

```bash
git merge experimental
```

If the changes don't conflict, then the merge was succesful and you can add,
commit and push to the remote repository. If there are conflicts, markers will
be left in the problematic files showing the conflict;

```bash
git diff
```

will show this. Once you've edited the files to resolve the conflicts,

```bash
git commit -a
```

will commit the result of the merge. Finally,

At this point you could delete the experimental branch with

```bash
git branch -d experimental
```

This command ensures that the changes in the experimental branch are already in
the current branch.

If you want to remove a branch without pulling the changes into the master branch,
the `-D` flag deletes it without checking any of the changes.

This only removes the branch from your local machine.  To remove it from the
remote repository, you use:
```bash
git push -d origin experimental
```

---

[← Undoing a Mistake: checkout, reset, and revert](07-undoing-a-mistake-checkout-reset-and-revert.md) · [Up: contents](index.md) · [Pull-requests →](09-pull-requests.md)
