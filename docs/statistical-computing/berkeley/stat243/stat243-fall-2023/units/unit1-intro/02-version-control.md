---
title: Version control
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit1-intro.md
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit1-intro.md
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Version control

**Source:** [`units/unit1-intro.md`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit1-intro.md) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.md` (lossless)

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
    (*berkeley-stat243* is the organization and *stat243-fall-2022* is the
    repository):

    ```
    git clone https://github.com/berkeley-stat243/stat243-fall-2023
    ```

2.  To update a repository to reflect changes made in a remote copy of
    the repository:

    ```
    cd /to/any/directory/within/the/local/repository
    git pull
    ```

More information is available in the [tutorial on the basics of using
Git](https://htmlpreview.github.io/?https://github.com/berkeley-scf/tutorial-git-basics/blob/master/git-intro.html), as well as lots
of information/tutorials online.
We'll see a lot more about Git in Section sessions, where you'll learn to set up
a repository, make changes to repositories and work with local and
remote versons of the repository. In particular, you'll have a chance to
work through the tutorial and practice with
Git in the first section/lab (September 2). During the course, you'll make use of Git for submitting problem sets and for doing the final project. You should practice using it more generally while preparing your problem set
solutions, and you'll need to use it extensively for the final group project.

---

[← UNIX command line basics](01-unix-command-line-basics.md) · [Up: contents](index.md) · [Parts of a computer →](03-parts-of-a-computer.md)
