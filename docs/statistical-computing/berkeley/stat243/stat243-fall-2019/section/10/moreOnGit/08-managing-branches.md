---
title: Managing Branches
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/10/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Managing Branches

**Source:** [`section/10/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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
git commit -a "edit"
git checkout master
```

Alternatively, one can "stash" the changes using `git stash`.
This saves your changes for later, and then reverts the working tree to the last
HEAD (whatever the last commit was). This allows you to keep working without the
changes being applied to any files.
You can apply those changes later using `git stash pop`, which applies the changes
and removes them from your stash. Or, if you wish to apply the changes to multiple
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

If the changes don't conflict, you're done. If there are conflicts, markers will
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

This only removes the branch from your local machine.
To remove it from the remote repository, you use:
```bash
git push -d origin experimental
```


At some point before removing a branch, you may want to merge the branch back into
the master branch. The best way to do this is using a [pull request](https://www.atlassian.com/git/tutorials/making-a-pull-request), which I
will demonstrate on github. Pull requests tell the repository maintainers what changes
you are proposing, whether it can be directly merged in or if there are conflicts,
and cleanly wraps the log from the other branch into one statement. You can also
set a [default template](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/10/PULL_REQUEST_TEMPLATE.md) for your pull requests.

---

[← Viewing Project History](07-viewing-project-history.md) · [Up: contents](index.md) · [Using Git For Collaboration →](09-using-git-for-collaboration.md)
