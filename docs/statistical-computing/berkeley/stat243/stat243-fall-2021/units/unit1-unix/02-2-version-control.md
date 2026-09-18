---
title: 2 Version control
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit1-unix.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit1-unix.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Version control

A very popular and powerful tool for version control is Git. We'll be using Git extensively to do version control.

More information is available in the tutorial on the basics of using Git. You'll have a chance to work through the tutorial and practice with Git in the first section/lab. During the course, you'll make use of Git for submitting problem sets and for doing the final project. I recommend you practice using it more generally while preparing your problem set solutions.

Git stores the files for a project in a *repository*. Here are some basic Git commands you can use to access the class materials from the command line. There are also graphical interfaces to Git that you can explore. That said, I recommend Github Desktop, available for Mac and Windows.

1. To clone (i.e., copy) a repository (in this case from Github) [*berkeley-stat243* is the project and *stat243-fall-2020* is the repository]:
```
> git clone https://github.com/berkeley-stat243/stat243-fall-2020
```

2. To update a repository to reflect changes made in a remote copy of the repository:
```
> cd /to/any/directory/within/the/local/repository
> git pull
```

We'll see a lot more about Git in section, where you'll learn to set up a repository, make changes to repositories and work with local and remote versons of the repository. The section material will follow our tutorial on the basics of Git, Github, and version control.

Some links to more resources:

* Git for Scientists: A Tutorial: http://nyuccl.org/pages/GitTutorial/
* Gitwash: workflow for scientific Python projects: http://matthew-brett.github.io/pydagogue/gitwash_build.html
* Git branching demo: http://pcottle.github.io/learnGitBranching/

## 3 Connecting to other machines

To connect to a remote machine, you need to use SSH. SSH is available as `ssh` when you are on the UNIX command line. There are also SSH clients for Windows. For more information on SSH client programs and on using SSH, please see this webpage. Here's an example of connecting to one of the SCF machines (this assumes you have an SCF account, which you may, and that your user name is paciorek, which it is not).

```
> ssh paciorek@radagast.berkeley.edu
```

To copy files between machines, we can use `scp`, which has similar options to `cp`. The first command here copies a local file to a remote machine. The second copies from a remote machine to the machine you are on. You can use relative paths to refer to locations on the local machine. On the remote machine all paths need to be absolute or to be relative to your home directory on that machine. Again, this assumes you have an SCF account.

```
> scp file.txt paciorek@radagast.berkeley.edu:~/research/.
> scp paciorek@radagast.berkeley.edu:/data/file.txt ~/research/renamed.txt
```

There are also client programs for file transfer; see this webpage.

---

[← Unit 1: Basics of UNIX](01-unit-1-basics-of-unix.md) · [Up: contents](index.md) · [4 Editors →](03-4-editors.md)
