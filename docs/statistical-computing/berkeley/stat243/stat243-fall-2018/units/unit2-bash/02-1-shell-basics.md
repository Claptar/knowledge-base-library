---
title: 1 Shell basics
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Shell basics

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The shell is the interface between you and the UNIX operating system. When you are working in a terminal window (i.e., a window with the command line interface), you’re interacting with a shell.

There are multiple shells ( _sh_ , _bash_ , _csh_ , _tcsh_ , _ksh_ ). We’ll assume usage of _bash_ , as this is a very commonly-used shell in Linux, plus it’s the default for Mac OS X, the SCF machines, and the UC Berkeley campus cluster (Savio).

UNIX shell commands are designed to each do a specific task really well and really fast. They are modular and composable, so you can build up complicated operations by combining the commands. These tools were designed decades ago, so using the shell might seem old-fashioned, but the shell still lies at the hard of modern scientific computing. By using the shell you can automate your work and make it reproducible.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Using the bash shell →](03-2-using-the-bash-shell.md)
