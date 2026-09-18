---
title: 'Unit 3: The bash shell and UNIX utilities'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit3-bash.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Unit 3: The bash shell and UNIX utilities

September 9, 2021

Note that it can be difficult to distinguish what is shell-specific and what is just part of the operating system (i.e., a UNIX-style operating system). Some of the material here is not bash-specific but general to UNIX. I'll use 'UNIX' to refer to a family of operating systems that descend from the path-breaking UNIX operating system developed at AT&T's Bell Labs in the 1970s. These include MacOS and various flavors of Linux (e.g., Ubuntu, Debian, CentOS, Fedora).

For your work on this unit, either bash on a Linux machine, the older version of bash on MacOS, or zsh on MacOS (or Linux) is fine. I'll probably demo everything using bash on a Linux machine, and there are some annoying differences from the older bash on MacOS that may be occasionally confusing.

Any tutorials mentioned below are available at http://statistics.berkeley.edu/computing/training/tutorials.

Reference: Newham and Rosenblatt, Learning the bash Shell, 2nd ed.

## 1 Shell basics

The shell is the interface between you and the UNIX operating system. When you are working in a terminal window (i.e., a window with the command line interface), you're interacting with a shell.

There are multiple shells (*sh*, *bash*, *zsh*, *csh*, *tcsh*, *ksh*). We'll assume usage of *bash*, as this is a very commonly-used shell in Linux, plus it's the default for Mac OS X (until Catalina, for which *zsh* is the default), the SCF machines, and the UC Berkeley campus cluster (Savio).

UNIX shell commands are designed to each do a specific task really well and really fast. They are modular and composable, so you can build up complicated operations by combining the commands. These tools were designed decades ago, so using the shell might seem old-fashioned, but the shell still lies at the heart of modern scientific computing. By using the shell you can automate your work and make it reproducible.

---

[Up: contents](index.md) · [2 Using the bash shell →](02-2-using-the-bash-shell.md)
