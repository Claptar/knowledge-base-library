---
title: 'Appendix: More Useful Git Functionality'
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab9-git.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab9-git.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Appendix: More Useful Git Functionality

**Source:** [`labs/lab9-git.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab9-git.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Importing a Project

I __do not__ recommend this process for initiating a new project. These steps are simple,
until you get to creating the remote repository. Then, just like in the intro tutorial,
you have you setup a new repository on Github and link it to the local one.  It
is easier to create the repo on Github, clone the empty repo locally, then put
files in it as desired.

Assume you have a tarball linReg.tar.gz with your initial work. You can place it
under Git revision control as follows.

```sh
tar xzf project.tar.gz
cd project
git init
```

Git will reply (something along the lines)
```sh
Initialized empty Git repository in .git/
```

You've now initialized the working directory-you may notice a new directory created,
named ".git".

Next, tell Git to take a snapshot of the contents of all files under the current
directory (note the .), with git add:

```sh
git add .
```

This snapshot is now stored in a temporary staging area which Git calls the *index*.
You can permanently store the contents of the index in the repository with `git commit`:

```sh
git commit -m "add"
```

This will prompt you for a commit message. You've now stored the first version of
your project in Git.

## Making Changes

If we make changes to files `file1`, `file2` and `file3` we can add them to be
committed with `git add` as we have discussed before:

```sh
git add file1 file2 file3
```

You are now ready to commit. You can see what is about to be committed using `git diff`
with the `--cached` option:

```sh
git diff --cached
```

(Without --cached, git diff will show you any changes that you've made but not
yet added to the index.)

You can also get a brief summary of the situation with `git status`:

```sh
git status
```

Alternatively, instead of running `git add` before `git commit`, you can use:

```sh
git commit -a
```

which will automatically notice any modified (but not new) files, add them to
the index, and commit, all in one step.

## Amending file to commit

What if, in the files you just committed, there was a file you forgot?  This
situation is handled via git's `amend` option in git commit.  Say we have added and
committed `file1`

```sh
git add file1
git commit -m "adding file1"
```

But we realize we also meant to commit `file2`.  We can do that by amending the
original commit as follows:

```sh
git add file2
git commit --amend -m "adding second file"
```

This allows you to add more files to a commit and then update the message, while
keeping your original message/committed-files there.

## Undoing mistakes: `checkout`, `reset`, and `revert`

!!! important "Important"
## Danger zone

Some of the commands below can get you into trouble if you aren't 100% sure of
what you're doing. Use them with extreme caution.

:::

### Checkout

`git checkout` can be used to look at a previous commit. It can also be used to
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
git checkout main # or replacing main with whatever branch you are on
```

### Revert

`git revert` is used when you want to undo the changes made in a previous
commit. It will undo a commit by creating a new commit. Consider using `git
revert HEAD~1`, this will remove the changes that were added in the
previous commit.

```bash
git revert HEAD~1
git revert HEAD~2
git revert <commit_hash>
```

### Reset

If you added something that shouldn't be committed or you want to reset your repo
to what it looked like at a previous commit, then you need to use
the `git reset` feature.

```bash
man git-reset

---

[← Pair exercises](05-pair-exercises.md) · [Up: contents](index.md) · [e.g. →](07-e-g.md)
