---
title: 'Appendix: More Useful Git Functionality'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/11/moreOnGit.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Appendix: More Useful Git Functionality

**Source:** [`sections/11/moreOnGit.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/11/moreOnGit.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

### Importing A Project

I __do not__ recommend this process for initiating a new project. These steps are simple,
until you get to creating the remote repository. Then, just like in the intro tutorial,
you have you setup a new repository on Github and link it to the local one.  It
is easier to create the repo on Github, clone the empty repo locally, then put
files in it as desired.

Assume you have a tarball linReg.tar.gz with your initial work. You can place it
under Git revision control as follows.

```bash
tar xzf project.tar.gz
cd project
git init
```

Git will reply (something along the lines)
```bash
Initialized empty Git repository in .git/
```

You've now initialized the working directory-you may notice a new directory created,
named ".git".

Next, tell Git to take a snapshot of the contents of all files under the current
directory (note the .), with git add:

```bash
git add .
```

This snapshot is now stored in a temporary staging area which Git calls the *index*.
You can permanently store the contents of the index in the repository with `git commit`:

```bash
git commit -m "add"
```

This will prompt you for a commit message. You've now stored the first version of
your project in Git.

### Making Changes
If we make changes to files `file1`, `file2` and `file3` we can add them to be commited with `git add` as we have discussed before:
```bash
git add file1 file2 file3
```

You are now ready to commit. You can see what is about to be committed using `git diff`
with the `--cached` option:

```bash
git diff --cached
```

(Without --cached, git diff will show you any changes that you've made but not
yet added to the index.)

You can also get a brief summary of the situation with `git status`:

```bash
git status
```

Alternatively, instead of running `git add` before `git commit`, you can use:

```bash
git commit -a
```

which will automatically notice any modified (but not new) files, add them to
the index, and commit, all in one step.

### Amending file to commit
What if, in the files you just commited, there was a file you forgot?  This
situation is handled via git's `amend` option in git commit.  Say we have added and
committed `file1`

```bash
git add file1
git commit -m "adding file1"
```

But we realize we also meant to commit `file2`.  We can do that by ammending the
original commit as follows:
```bash
git add file2
git commit --amend -m "adding second file"
```

This allows you to add more files to a commit and then update the message, while
keeping your original message/commmited-files there.

---

[← Pull-requests](09-pull-requests.md) · [Up: contents](index.md)
