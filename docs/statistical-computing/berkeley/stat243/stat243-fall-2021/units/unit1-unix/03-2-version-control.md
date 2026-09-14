---
title: 2 Version control
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit1-unix.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Version control

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit1-unix.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A very popular and powerful tool for version control is Git. We’ll be using Git extensively to do version control.

More information is available in the tutorial on the basics of using Git. You’ll have a chance to work through the tutorial and practice with Git in the first section/lab. During the course, you’ll

1

make use of Git for submitting problem sets and for doing the final project. I recommend you practice using it more generally while preparing your problem set solutions.

Git stores the files for a project in a _repository_ . Here are some basic Git commands you can use to access the class materials from the command line. There are also graphical interfaces to Git that you can explore. That said, I recommend Github Desktop, available for Mac and Windows.

1. To clone (i.e., copy) a repository (in this case from Github) [ _berkeley-stat243_ is the project and _stat243-fall-2020_ is the repository]:

   - git clone https://github.com/berkeley-stat243/stat243-fall-2020

2. To update a repository to reflect changes made in a remote copy of the repository: > cd /to/any/directory/within/the/local/repository > git pull

We’ll see a lot more about Git in section, where you’ll learn to set up a repository, make changes to repositories and work with local and remote versons of the repository. The section material will follow our tutorial on the basics of Git, Github, and version control.

Some links to more resources:

- Git for Scientists: A Tutorial: http://nyuccl.org/pages/GitTutorial/

- Gitwash: workflow for scientific Python projects: http://matthew-brett.github.io/pydagogue/gitwash_build.html

- Git branching demo: http://pcottle.github.io/learnGitBranching/

---

[← 1 UNIX basics](02-1-unix-basics.md) · [Up: contents](index.md) · [3 Connecting to other machines →](04-3-connecting-to-other-machines.md)
