---
title: 1 Shell basics
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Shell basics

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The shell is the interface between you and the UNIX operating system. When you are working in a terminal window (i.e., a window with the command line interface), you’re interacting with a shell.

There are multiple shells ( _sh_ , _bash_ , _csh_ , _tcsh_ , _ksh_ ). We’ll assume usage of _bash_ , as this is the default for Mac OS X, the BCE VM, and on the SCF machines and is very common for Linux.

1. What is my default shell?

   - echo $SHELL

2. To change to bash on a one-time basis:

   - bash

3. To make it your default:

> chsh /bin/bash

_/bin/bash_ should be whatever the path to the bash shell is, which you can figure out using which bash

Shell commands can be saved in a file (with extension _.sh_ ) and this file can be executed as if it were a program. To run a shell script called _file.sh_ , you would type ./file.sh. Note that if you just typed file.sh, the operating system will generally have trouble finding the script and recognizing that it is executable. To be sure that the operating system knows what shell to use to interpret the script, the first line of the script should be #!/bin/bash (in the case that you’re using the bash shell). Also, _file.sh_ would need to be executable (i.e., to have the ’x’ flag set).

1

---

[Up: contents](index.md) · [2 Tab completion →](02-2-tab-completion.md)
