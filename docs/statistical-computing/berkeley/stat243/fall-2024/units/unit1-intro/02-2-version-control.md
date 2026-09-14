---
title: 2. Version control
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit1-intro.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit1-intro.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Version control

**Source:** [`units/unit1-intro.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit1-intro.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Version control refers to the process of keeping track of changes to
your materials on a computer, often code files but other files as well.
It generally works well with text files because version control operates
based on differences between two versions of a file, and those
differences are kept track of on a line-by-line basis. Version control
is a central concept/practice in modern scientific computing.

A very popular and powerful tool for version control is Git. We'll be
using Git extensively for version control.

Git stores the files for a project in a *repository*. Here are some
basic Git commands you can use to access the class materials from the
command line. There are also [graphical interfaces to
Git](https://git-scm.com/downloads) that you can explore. I've heard good things (albeit a few years ago) about [GitHub Desktop](https://desktop.github.com), available for
Mac and Windows.

1.  To clone (i.e., copy) a repository (in this case from GitHub)
    (`berkeley-stat243` is the organization and `fall-2024` is the
    repository):

    ```
    git clone https://github.com/berkeley-stat243/fall-2024
    ```

2.  To update a repository to reflect changes made in a remote copy of
    the repository:

    ```
    cd /to/any/directory/within/the/local/repository  ## e.g., cd fall-2024
    git pull
    ```

More information is available in the [Computing Skills Workshop](https://berkeley-scf.github.io/compute-skills-2024) as well as this [tutorial on the basics of using
Git](https://htmlpreview.github.io/?https://github.com/berkeley-scf/tutorial-git-basics/blob/master/git-intro.html), as well as lots
of information/tutorials online.
We'll see a lot more about Git in Section/Lab sessions, where you'll learn to set up
a repository, make changes to repositories and work with local and
remote versons of the repository. In particular, you'll have a chance to
work through the tutorial and practice with
Git in the first section/lab (September 6). During the course, you'll make use of Git for submitting problem sets and for doing the final project. You should practice using it more generally while preparing your problem set
solutions, and you'll need to use it extensively for the final group project.

---

[← 1. UNIX command line basics](01-1-unix-command-line-basics.md) · [Up: contents](index.md) · [3. Parts of a computer →](03-3-parts-of-a-computer.md)
