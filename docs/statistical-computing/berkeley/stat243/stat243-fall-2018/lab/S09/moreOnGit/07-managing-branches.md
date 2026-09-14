---
title: Managing Branches
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S09/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Managing Branches

**Source:** [`lab/S09/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S09/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

A single Git repository can maintain multiple branches of development. To create a new branch named "experimental", use

```bash
git branch experimental
```

If you now run
```bash
git branch
```

The "experimental" branch is the one you just created, and the "master" branch is a default branch that was created for you automatically. The asterisk marks the branch you are currently on; type

```bash
git checkout experimental
```

to switch to the experimental branch. Now edit a file, commit the change, and switch back to the master branch:

```bash
git commit -a "edit"
git checkout master
```

Check that the change you made is no longer visible, since it was made on the experimental branch and you're back on the master branch.

You can make a different change on the master branch and commit. At this point the two branches have diverged, with different changes made in each. To merge the changes made in experimental into master, run:

```bash
git merge experimental
```

If the changes don't conflict, you're done. If there are conflicts, markers will be left in the problematic files showing the conflict;

```bash
git diff
```

Do you have a clear idea now what changes cause conflicts?

will show this. Once you've edited the files to resolve the conflicts,

```bash
git commit -a
```

will commit the result of the merge. Finally,

```bash
gitk
```

will show a nice graphical representation of the resulting history.

At this point you could delete the experimental branch with

```bash
git branch -d experimental
```

This command ensures that the changes in the experimental branch are already in the current branch.

If you develop on a branch `secretions-of-a-sick-mind`, then regret it, you can always delete the branch with

```bash
git branch -D crazy-idea
```

---

[← Viewing Project History](06-viewing-project-history.md) · [Up: contents](index.md) · [Using Git For Collaboration →](08-using-git-for-collaboration.md)
