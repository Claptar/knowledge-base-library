---
title: git Basics
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# git Basics

**Source:** [`section/01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

> ### Learning Objectives
>
> * Create a GitHub repository
> * Create a local Git repository
> * Practice adding, and committing changes to your (local) Git repo
> * Practice pushing commited changes to a remote repo

### 0) Useful Links
- A nice tutorial is available on the [Berkeley SCF github repo](https://github.com/berkeley-scf/tutorial-git-basics)
- Show git branch in [command prompt](https://askubuntu.com/questions/730754/how-do-i-show-the-git-branch-with-colours-in-bash-prompt)
- Setup git password manager
	- [Simple Answer](https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git)
	- [Official Documentation](https://git-scm.com/docs/git-credential-store)


### 1) Create a New GitHub Repository
There are two ways to start a repository:

- create the repository on Github using your browser and then use `git clone`
- use `git init` on your machine and then linking it to a remote server e.g. github.

We're going to cover creating one online:

- Open your browser and Sign in to your github account.
- Locate the `+` button (next to your avatar).
- Select the `New repository` option.
- Choose a name for your repository: e.g. `demo-repo`.
- In the __Description__ field add a brief description: e.g. "this is a demo repo"
- add a .gitignore for R files.
- Click the green button __Create repository__.


### 2) Adding a README file

Initially, your repo is located on GitHub. To set it up locally, you must clone
the repository from GitHub.

```r
git clone https://github.com/berkeley-scf/tutorial-git-basics
```


It is customary to add a `README.md` file at the top level. This file must
contain (at least) a description of what the repository is about. The following
command will create a `README.md` file with some minimalist content:

```r
echo "# Demo Repo" >> README.md
```

So far there you have a "new" file in your local repo, but this change has
not been recorded by Git. You can confirm this by checking the status of the repo:

```r
git status
```

Notice that Git knows that `README.md` is untracked. So let's add the
changes to Git's database:

```r
git add README.md
```

Check the status of the repo again:

```r
git status
```

Now Git is tracking the file `README.md`.
Next thing consists of __committing__ the changes

```r
git commit -m "Create README"
```

### 3) Pushing changes to a remote repo

Now that you have linked your local repo with your remote repo, you can
start pushing (i.e. uploading) commits to GitHub.
As part of the basic workflow with git and github, you want to constantly
check the status of your repo

```r
git status
```

Now let's push your recent commit to the remote branch (`origin`) from
the local branch (`master`):

```r
git push origin master
```

Go to your Github repository and refresh the browser. If everything went fine,  you should be able to see the contents of your customized `README.md` file.

---

[Up: contents](index.md) · [knitr and R Markdown Files →](02-knitr-and-r-markdown-files.md)
