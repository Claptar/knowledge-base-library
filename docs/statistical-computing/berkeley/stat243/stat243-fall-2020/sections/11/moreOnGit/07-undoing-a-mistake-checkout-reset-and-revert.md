---
title: 'Undoing a Mistake: checkout, reset, and revert'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/11/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Undoing a Mistake: checkout, reset, and revert

**Source:** [`sections/11/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

### Checkout
`git checkout` can be used to look at a previous commit.  It can also be used to
move to a different branch, which we will look at in the next section. Here we
can look at code from a previous commit with:
```bash
git checkout HEAD~1 # moves back 1 commit
git checkout HEAD~2 # moves back 2 commits
git checkout <commit_hash> # move back to a specific commit
```

To find commit IDs you can use `git log` or `git reflog`.  You can also find
commit IDs on GitHub.

Once you have looked at the commit you can go back to the most recent update using
```bash
git checkout master # or replacing master with whatever branch you are on
```

### Revert
`git revert` is used when you want to undo the changes made in a previous
commit. It will undo a commit by creating a new commit.  Consider using
`git revert HEAD~1`, this will remove the changes that were added in the
previous commit.

```bash
git revert HEAD~1
git revert HEAD~2
git revert <commit_hash>
```

### Reset
If you added something that shouldn't be commited or you want to reset your repo
to what it looked like at a previous commit, then you need to use
the `git reset` feature.

```bash
man git-reset

# e.g.
git reset --soft HEAD~1
git reset --hard HEAD~1
```

Git reset moves the tip of your working tree back to the specified revision (here,
we go back one revision). The `--soft` flag means that the changes in the
files are presevered, so all that was done was to undo the commit. If you use the
`--hard` flag, then all changes are reverted to the specified time.

If you have done something more complex, like commiting and attempting to push a
large file, the command below may be useful.

```bash
git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch <PATH/TO/FILE>' HEAD
```

This deletes everything in the commit history.

---

[← Viewing Project History](06-viewing-project-history.md) · [Up: contents](index.md) · [Managing Branches →](08-managing-branches.md)
