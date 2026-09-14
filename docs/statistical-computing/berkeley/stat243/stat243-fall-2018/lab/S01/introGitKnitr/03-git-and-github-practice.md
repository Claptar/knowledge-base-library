---
title: Git and GitHub Practice
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Git and GitHub Practice

**Source:** [`lab/S01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

> ### Learning Objectives
>
> * Create a GitHub repository
> * Create a local Git repository
> * Practice adding, and committing changes to your (local) Git repo
> * Practice pushing commited changes to a remote repo


A nice tutorial is available on the
[Berkeley SCF github
repo](https://github.com/berkeley-scf/tutorial-git-basics).

```
git clone https://github.com/berkeley-scf/tutorial-git-basics
```

There are two ways to start a repository:

- create the repository on Github using your browser and then use `git clone`
- use `git init` on your machine and then linking it to a remote server e.g. github.

### 1) Create a New GitHub Repository

- Open your browser and Sign in to your github account.
- Locate the `+` button (next to your avatar).
- Select the `New repository` option.
- Choose a name for your repository: e.g. `demo-repo`.
- In the __Description__ field add a brief description: e.g. "this is a demo repo"
- Use the default settings, and click the green button __Create repository__.

Let's go through the following code chunk in detail.

```bash
echo "# Demo Repo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/osolari/demo-repo.git
git push -u origin master
```

### 2) Create a local Git Repository

- Open the terminal (Mac Terminal, or Git-Bash for Windows users).
- Optional: change directory to your preferred location
e.g. your `Desktop`
```bash
cd Desktop
```
- Create a directory with the name of your github repo
```bash
mkdir demo-repo
```
- Change to the directory you just created
```bash
cd demo-repo
```
- Initialize the directory as a git repository
```bash
git init
```

It's possible that you encounter some error message, e.g. Mac users may get a
message related with a missing component for `CommandLineTools`. If this your
case, then type in the terminal console:

```bash

---

[← the option is the letter O (Not the number 0)](02-the-option-is-the-letter-o-not-the-number-0.md) · [Up: contents](index.md) · [Mac users may need to run this command →](04-mac-users-may-need-to-run-this-command.md)
