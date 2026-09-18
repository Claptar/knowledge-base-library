---
title: 2. Version control
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit1-intro.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit1-intro.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit1-intro.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit1-intro.qmd) — berkeley-stat243 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2. Version control

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
    (`berkeley-stat243` is the organization and `fall-2026` is the
    repository):

    ```bash
    git clone https://github.com/berkeley-stat243/fall-2026
    ```

2.  To update a repository to reflect changes made in a remote copy of
    the repository:

    ```bash
    cd /to/any/directory/within/the/local/repository  ## e.g., cd fall-2026
    git pull
    ```

More information is available in the [Computing Skills Workshop](https://computing.stat.berkeley.edu/compute-skills-2026) as well as this [tutorial on the basics of using
Git](https://htmlpreview.github.io/?https://github.com/berkeley-scf/tutorial-git-basics/blob/master/git-intro.html), as well as lots
of information/tutorials online.
We'll see a lot more about Git in Section/Lab sessions, where you'll learn to set up
a repository, make changes to repositories and work with local and
remote versons of the repository. In particular, you'll have a chance to
work through the tutorial and practice with
Git in the first section/lab (September 4). During the course, you'll make use of Git for submitting problem sets. You should practice using it more generally while preparing your problem set solutions.

## 3. Parts of a computer

We won't spend a lot of time thinking about computer hardware, but we do
need to know some of the basics that relate to using a computer and
programming effectively. There are many layers of technical detail one
could get into, but the key things for now are to have a basic
understanding of these components of a computer:

-   CPU
    -   cache (limited fast memory easily accessible from the CPU)
-   main memory (RAM)
-   bus
-   disk

Depending on what your code is doing, the slow step in a computation might be:

   - doing the actual calculations on the CPU,
   - moving data back and forth from (main) memory (RAM) to the CPU, or
   - reading/writing (I/O) data to/from disk.

Please read [this overview](https://36-750.github.io/tools/computer-architecture/) from a
class at CMU that is similar to this class. Don't worry about too much
of the details in the "How Programs Run" section - just try to get the
main idea.

---

[← 1. UNIX command line basics](01-1-unix-command-line-basics.md) · [Up: contents](index.md) · [4. Connecting to other machines →](03-4-connecting-to-other-machines.md)
