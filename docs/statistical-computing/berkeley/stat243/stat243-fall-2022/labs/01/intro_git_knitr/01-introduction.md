---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/01/intro_git_knitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`labs/01/intro_git_knitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(echo = TRUE)
```

[PDF](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/01/intro_git_knitr.pdf){.btn .btn-primary}

In this section we will learn and dicuss some tools that you will need to
complete your first problem set, namely git and knitr (either Quarto, R
Markdown, or Rtex). At the end there are also resources about code style and a
couple notes to keep in mind when turning in your problem sets.

## Getting started with Git and GitHub
### Learning Objectives

 * Create a __remote__ repository on GitHub
 * Create a __local__ Git repository on your machine
 * Practice adding, and committing changes to your (local) Git repo
 * Practice pushing commited changes to a remote repo

### Useful Links
- A nice tutorial is available on the [Berkeley SCF github repo](https://github.com/berkeley-scf/tutorial-git-basics)
- Using Git without having to enter your password over and over:
  - Option 1: Use [Git Credential Manager](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git#git-credential-manager) and HTTPS clone method, e.g.,

      ```bash
      git clone https://github.com/berkeley-scf/tutorial-git-basics.git
      ```

  - Option 2: Use [SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) and SSH clone method, e.g.,

      ```bash
      git clone git@github.com:berkeley-scf/tutorial-git-basics.git
      ```

  - Either way, be sure to follow the instructions for your OS (Mac, Windows, or Linux) by selecting it at the top of the page.

- [git-scm.com](https://git-scm.com) has a number useful resources for learning Git, including:

    - [Pro Git book](https://git-scm.com/book/en/v2)

    - [Command reference manual](https://git-scm.com/docs)

### Create a New GitHub Repository

There are two ways to start a repository:

1. Creating the repository on GitHub using your browser and then use `git clone`.
2. Using `git init` on your machine and then link it to a remote server, e.g. GitHub.

!!! warning "Warning"
## Option 1 is usually the right choice

Use option 2. only if you already have a local repo and later decide you want to
create a remote copy on a service such as GitHub. For this course, this won't be
necessary.

But if you do need to use `git init`, then when you first create a local repo on
your machine using `git init`, the default branch name is `master`. However, the
default branch when you create one on GitHub is called `main`, so if you later
decide to add a remote copy of your local repo to GitHub, you will need to
update the name of your default branch. After creating the blank repo on GitHub
(no `README.md` or `.gitignore`), run the commands that GitHub provides in your
local repo to change the default branch from `master` to `main`.

:::

Today, **we're going to cover option 1.** by creating one online using Berkeley's GitHub Enterprise instance:

- Open your browser and Sign in to your [github.berkeley.edu](https://github.berkeley.edu/) account.
- Locate the `+` button (next to your avatar).
- Select the `New repository` option.
- Choose a name for your repository: e.g. `demo-repo`.
- In the __Description__ field add a brief description: e.g. "this is a demo repo"
- Check "Add .gitignore" and type "R" to find one that is tailored to R projects. This stops items like `.Rhistory` files from being added to your repo.
- Click the green button __Create repository__.


### Adding a README file

Initially, your repo is located on GitHub. To set it up locally, you must clone
the repository from GitHub, e.g.:

```bash

---

[Up: contents](index.md) · [replace https://github.com/berkeley-scf/tutorial-git-basics with →](02-replace-https-github-com-berkeley-scf-tutorial-git-basics-wi.md)
