---
title: 1. Shell basics
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit3-bash.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1. Shell basics

Reference:

- Newham and Rosenblatt, [Learning the bash Shell](https://learning.oreilly.com/library/view/learning-the-bash/0596009658/?ar=), 2nd ed.
- Damien Irving, Kate Hertweck, Luke Johnston, Joel Ostblom, Charlotte
Wickham, and Greg Wilson. [Research Software Engineering with Python](https://third-bit.com/py-rse/)
- [SCF Bash tutorial](https://computing.stat.berkeley.edu/tutorial-using-bash)

The shell is the interface between you and the (UNIX-style) operating system.

I'll use 'UNIX' to refer to the family of operating systems that
descend from the path-breaking UNIX operating system developed at AT&T's
Bell Labs in the 1970s. These include MacOS and various flavors of Linux
(e.g., Ubuntu, Debian, CentOS, Fedora).

When you are working in a terminal window (i.e., a window providing the
command line interface), you're interacting with a shell. From the shell
you can run UNIX commands such as `cp`, `ls`, `grep`, etc. (as well as
start various applications).

Here's a [graphical representation](https://technoinfo360.com/explain-what-is-kernel-and-shell-in-unix/) of how the shell relates to various
programs, commands, and the operating system.

There are multiple shells (`sh`, `bash`, `zsh`, `csh`, `tcsh`, `ksh`).
We'll assume usage of `bash`, as this is a very commonly-used shell in
Linux, plus was the default for Mac OS X until Catalina (`zsh`, very similar to bash, is now the default), the SCF machines, and the UC Berkeley campus
cluster (Savio). All of the various shells allow you to run
UNIX commands.

For your work on this unit, either bash on a Linux machine, the older
version of bash on MacOS, or zsh on MacOS (or Linux) are fine. I'll
probably demo everything using bash on a Linux machine.

!!! note "Danger"
Note that the UNIX utilities on Linux have some annoying, but usually minor,
differences from those on MacOS that may be
occasionally confusing (in particular the options to various commands
can differ on MacOS).

For example, you can use `ls --all` in Linux but not MacOS.

:::

The Windows PowerShell and old cmd.exe/DOS command interpreter both provide
a command-line interface on Windows, but not a UNIX-based one. We won't consider
them here.

UNIX shell commands are designed to each do a specific task really well
and really fast. They are modular and composable, so you can build up
complicated operations by combining the commands. These tools were
designed decades ago, so using the shell might seem old-fashioned, but
the shell still lies at the heart of modern scientific computing. By
using the shell you can automate your work and make it reproducible.
And once you know how to use it, you'll find that enter commands
quickly and without a lot of typing.

## 2. Using the bash shell

For this Unit, we'll rely on [the bash shell tutorial](https://computing.stat.berkeley.edu/tutorial-using-bash)
for the details of how to use the shell. We won't cover the page on Managing Processes.
For the moment, we won't cover the page on Regular Expressions, but when we talk about string processing and regular expressions in Unit 5, we'll come back to that material.

---

[Up: contents](index.md) · [3. bash shell examples →](02-3-bash-shell-examples.md)
