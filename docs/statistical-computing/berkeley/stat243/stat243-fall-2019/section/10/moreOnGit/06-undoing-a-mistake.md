---
title: Undoing a Mistake
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/10/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Undoing a Mistake

**Source:** [`section/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

What if, in the files you just commited, there was a file you forgot?
This situation is handled via git's `amend` option in git commit.

```bash
man git-commit
```

This allows you to add more files to a commit and then update the message, while
keeping your original message/commmited-files there.

However, if you added something that shouldn't be commited, then you need to use
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

[← Git Tracks Contents, Not Files](05-git-tracks-contents-not-files.md) · [Up: contents](index.md) · [Viewing Project History →](07-viewing-project-history.md)
