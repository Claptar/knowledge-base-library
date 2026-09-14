---
title: Mac users may need to run this command
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Mac users may need to run this command

**Source:** [`lab/S01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

xcode-select --install
```

The command `git init` will set-up your directory `demo-repo` as a Git
repository (NOT to confuse with your GitHub repository). This is basically
your __local__ repository.


### 3) Adding a README file

- It is customary to add a `README.md` file at the top level. This file must
contain (at least) a description of what the repository is about. The following
command will create a `README.md` file with some minimalist content:
```bash
echo "# Demo Repo" >> README.md
```
- So far there you have a "new" file in your local repo, but this change has
not been recorded by Git. You can confirm this by checking the status of the repo:
```bash
git status
```
- Notice that Git knows that `README.md` is untracked. So let's add the
changes to Git's database:
```bash
git add README.md
```
- Check the status of the repo again:
```bash
git status
```
- Now Git is tracking the file `README.md`.
- Next thing consists of __committing__ the changes
```bash
git commit -m "first commit"
```

### 4) Adding a remote

Right now you have a (local) Git repository in your computer. And you also have
a GitHub repository in your GitHub account. Both repositories should have the
same name, and the goal is to link them. To do this, you need to tell Git that
a _remote_ repository (i.e. the one in GitHub) will be added:

- To add a remote repository use the command below __with your own username__:
```bash
git remote add origin https://github.com/username/demo-repo.git
```
- Verify your new remote
```bash
git remote -v
```
- If everything is okay, you should be able to see a message
(with your own username) like this:
```

---

[← Git and GitHub Practice](03-git-and-github-practice.md) · [Up: contents](index.md) · [Verify new remote →](05-verify-new-remote.md)
