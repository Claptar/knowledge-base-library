---
title: the URL / clone method (HTTPS or SSH) for your new repo
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/01/intro_git_knitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# the URL / clone method (HTTPS or SSH) for your new repo

**Source:** [`labs/01/intro_git_knitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

git clone https://github.com/berkeley-scf/tutorial-git-basics
```

It is customary to add a `README.md` file at the top level (note that a blank
one was already added to your PS repo). This file must contain (at least) a
description of what the repository is about. The following command will create a
`README.md` file with some minimalist content:

```bash
echo "# Demo Repo" >> README.md
```

Now you have a "new" file in your local repo, but this change has not been
recorded by Git. You can confirm this by checking the status of the repo:

```bash
git status
```

Notice that Git knows that `README.md` is untracked, so let's add the changes to
Git's database:

```bash
git add README.md
```

Check the status of the repo again:

```bash
git status
```

Now Git is tracking the file `README.md`. Next, the changes need to _committed_
to the repository. You can use the `-m` option to write a message inline. It's
a good idea to keep your commit messages succinct but informative.

```bash
git commit -m "Add README"
```

In general, it is best to make frequent small commits rather than infrequent
large commits. For example, you might want to make a single commit for each
problem in a problem set, rather than a single commit for the full problem set.

!!! warning "Warning"
If you run `git commit` without `-m`, Git will launch a default text editor,
usually `vi` or `vim`. If you this happens unintentionally, you can quit by
typing `ESC` followed by `:` and then `q!` followed by `Enter`.

You can specify which editor Git should use using `git config`. Take a look at
this
[documentation](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config)
to learn how.

:::

### Examining changes while editing

Once you create a commit, it becomes a part of your repo's history. You can see
the history using `git log`:

```bash

---

[← replace https://github.com/berkeley-scf/tutorial-git-basics with](02-replace-https-github-com-berkeley-scf-tutorial-git-basics-wi.md) · [Up: contents](index.md) · [this usually opens in less →](04-this-usually-opens-in-less.md)
