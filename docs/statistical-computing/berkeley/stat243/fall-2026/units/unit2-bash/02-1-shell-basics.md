---
title: 1. Shell basics
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-bash.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit2-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Shell basics

**Source:** [`units/unit2-bash.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit2-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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
version of bash on MacOS, or zsh on MacOS (or Linux) are fine.
Don't use Git Bash - it doesn't have the full functionality of a regular bash shell.
I'll demo everything using bash on a Linux machine.

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

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [2. Using the bash shell →](03-2-using-the-bash-shell.md)
