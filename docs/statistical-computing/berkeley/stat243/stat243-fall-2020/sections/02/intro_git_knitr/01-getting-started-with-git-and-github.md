---
title: Getting started with Git and GitHub
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/02/intro_git_knitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/02/intro_git_knitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Getting started with Git and GitHub

**Source:** [`sections/02/intro_git_knitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/02/intro_git_knitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

### Learning Objectives

 * Create a GitHub repository
 * Create a local Git repository
 * Practice adding, and committing changes to your (local) Git repo
 * Practice pushing commited changes to a remote repo

### Useful Links
- A nice tutorial is available on the [Berkeley SCF github repo](https://github.com/berkeley-scf/tutorial-git-basics)
- Save username and password ([Simple Answer](https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git), [Official Documentation](https://git-scm.com/docs/git-credential-store))

### Create a New GitHub Repository
There are two ways to start a repository:

- create the repository on GitHub using your browser and then use `git clone`
- use `git init` on your machine and then linking it to a remote server e.g. GitHub.

We're going to cover creating one online:

- Open your browser and Sign in to your GitHub account.
- Locate the `+` button (next to your avatar).
- Select the `New repository` option.
- Choose a name for your repository: e.g. `demo-repo`.
- In the __Description__ field add a brief description: e.g. "this is a demo repo"
- add a .gitignore for R files.  Stops items like .Rhistory files from being added to your repo.
- Click the green button __Create repository__.


### Adding a README file

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
Next, the changes need to __committed__ to the repository.

```r
git commit -m "Create README"
```

### Pushing changes to a remote repo

Now that you have linked your local repo with your remote repo, you can
start pushing (i.e. uploading) commits to GitHub.
As part of the basic workflow with Git and GitHub, you want to constantly
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

If you or a collaborator make changes on your remote repo you must __pull__ the remote repo into your local repo before you attempt to __push__ the changes you made locally.

```r
git pull
```

---

[Up: contents](index.md) · [knitr and R Markdown Files →](02-knitr-and-r-markdown-files.md)
