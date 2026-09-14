---
title: Some terminology
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab9-git.qmd
source_file: sources/berkeley-stat243/fall-2024/labs/lab9-git.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Some terminology

**Source:** [`labs/lab9-git.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab9-git.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

First, so we're all on the same page, let's get familiar with some terminology
that will appear in the materials today.

!!! note "Note"
## Tracked and untracked files

In a given repository, you may have files that are in version control (tracked)
alongside files that are not yet added (untracked). Typically, you track a
previously untracked file by using `git add`. Once a file is tracked, it will
remain in that state unless you explicitly tell Git to no longer track the file.

Note that the `.gitignore` file helps us de-clutter Git outputs by letting Git
know that what files or directories we _never_ intend to track. But after you've
tracked a file, if you later add it to `.gitignore`

:::

!!! note "Note"
## Staging

When you first track a file using `git add`, it also goes into the "staged"
state, meaning that the file will be included in the next snapshot of your
repo (AKA, the next "commit").

This is also the case when you modify a tracked file and then use `git add`. If,
however, you make additional changes to the file before committing, those
__additional changes__ will be unstaged (but the previously added changes are
still staged!).

:::

!!! note "Note"
## The index

How does Git know what changes are staged or unstaged? By adding those changes
to its index! This is what Git does when you use `git add`, allowing it prepare
for the next commit and to notice any further changes you make before
committing.

So the index can be thought of as a collection of staged changes, which is
converted to a commit when you use `git commit`.

:::

!!! note "Note"
## modified and unmodified files

After you commit changes to a file, the file in question switches to the
"unmodified" state, and the index with staged changes is added to the commit
history. In this state, using `git add` on the file has no effect.

If you later edit that file, it goes into the "modified" state, and `git add`
will do what you expect it to.

:::

The below diagram comes from the Pro Git book section [2.2 Git Basics -
Recording Changes to the
Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
and demonstrates how the interplay of the concepts above.

![The cycle of Git life.](https://raw.githubusercontent.com/berkeley-stat243/fall-2024/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab9-git/lifecycle.png)

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [Some review of key commands you should already know →](03-some-review-of-key-commands-you-should-already-know.md)
