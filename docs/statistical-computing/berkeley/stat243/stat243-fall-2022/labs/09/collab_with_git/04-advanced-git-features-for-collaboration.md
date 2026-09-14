---
title: Advanced Git features for collaboration
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/09/collab_with_git.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/09/collab_with_git.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Advanced Git features for collaboration

**Source:** [`labs/09/collab_with_git.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/09/collab_with_git.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

With the review out of the way, let's jump into the main new features you'll
want to know about for collaboration.

## `git pull`

You already know how to use `git push` to update your remote repository on
GitHub, but to this point in the course `git pull` may not have been super
relevant.

When it comes to collaboration, however, `git pull` is the _very first_ command
you should run when you sit down to work on a local copy of a shared remote
repo.

Why? While you were doing other things, your collaborators could have worked on
their local copies, made commits, and pushed to the shared remote repo on
GitHub. So by using `git pull`, you will update your local copy with the changes
that they made _before_ you start making new changes.

Using `git pull` as a habit can help save some headaches down the line.

## `git log`

After running `git pull`, if there were updates then you'll want to get a quick
sense of what changed. You already know how to view the commit history using:

```bash
git log
```

If you also want to see complete diffs at each step, use

```bash
git log -p
```

However, the output using `-p` can at times be overwhelming. Often, a condensed
overview of the files changed in each commit is useful to get a feel for the
history:

```bash
git log --stat --summary
```

If you don't care about the files but just want a compact glance at the full
history, then the following command will give a pretty graph with information
about other branches in the repo's history:

```bash
git log --oneline --decorate --graph --all
```

There are many other ways to use `git log`, so take advantage of the docs if
there is something in particular that you'd like to see.

## `git branch`

To this point, I've been assuming that you and your collaborators are all
working on the same branch (typically `main`).

However, a single Git repository can maintain multiple branches of development.
A workflow where each collaborator works on their own branch and then work
together to merge their changes can be an effective way to collaborate and avoid
too many headaches in the case of code conflicts.

To see what branches are available, use:

```bash
git branch
```
You will probably only see `main` at this point.

To create a new branch named "experimental", use

```bash
git branch experimental
```

If you now run

```bash
git branch
```

The "experimental" branch is the one you just created, and the "main" branch
is a default branch that was created for you automatically. The asterisk marks
the branch you are currently on; type:

```bash
git checkout experimental
```

to switch to the experimental branch. Now edit a file, commit the change, and
switch back to the main branch:

```bash
git add file
git commit -m "edited file"
```

Alternatively, one can "stash" the changes using `git stash`. This saves your
changes for later, and then reverts the working tree to the last HEAD (whatever
the last commit was). This allows you to keep working without the changes being
applied to any files. You can apply those changes later using `git stash pop`,
which applies the changes and removes them from your stash. Or, if you wish to
apply the changes to multiple branches, you can use `git stash apply`, which
applies the changes but leaves them in your stash.

Now, you can switch back to the main branch.
```bash
git checkout main
```

Check that the change you made is no longer visible, since it was made on the
experimental branch and you're back on the main branch.

You can make a different change on the main branch and commit. At this point
the two branches have diverged, with different changes made in each. To merge
the changes made in experimental into main, run:

```bash
git merge experimental
```

If the changes don't conflict, then the merge was successful and you can add,
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

If you want to remove a branch without pulling the changes into the main branch,
the `-D` flag deletes it without checking any of the changes.

This only removes the branch from your local machine.  To remove it from the
remote repository, you use:

```bash
git push -d origin experimental
```

## Pull-requests

When working in a collaborative environment, instead of merging directly into
the main, it is best to create a pull-request. This
[link](https://www.atlassian.com/git/tutorials/making-a-pull-request) has a good
step-by-step explanation.

Pull requests tell repository maintainers the difference between the main
repository and an individual's branch. It will then allow maintainers to comment
on the pull request and get bugs fixed before the branch is merged to the main.

Pull requests are common practice in the software development in industry.

---

[← Some review of key commands you should already know](03-some-review-of-key-commands-you-should-already-know.md) · [Up: contents](index.md) · [Pair exercises →](05-pair-exercises.md)
