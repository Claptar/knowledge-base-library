---
title: 8 Aliases
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Aliases

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Aliases allow you to use an abbreviation for a command, to create new functionality or to insure that certain options are always used when you call an existing command. For example, I’m lazy and would rather type q instead of exit to terminate a shell window. You could create the alias as follow

> alias q="exit"

As another example, suppose you find the _-F_ option of _ls_ (which displays **_/_** after directories, **_*_** after executable files and **_@_** after links) to be very useful. The command

> alias ls="ls -F"

will insure that the _-F_ option will be used whenever you use _ls_ . If you need to use the unaliased version of something for which you’ve created an alias, precede the name with a backslash ( **_\_** ). For example, to use the normal version of _ls_ after you’ve created the alias described above, just type

> \ls

The real power of aliases is only achieved when they are automatically set up whenever you log in to the computer or open a new shell window. To achieve that goal with aliases (or any other bash shell commands), simply insert the commands in the file _.bashrc_ in your home directory. See the _example.bashrc_ file in the repository for some of what’s in my _.bashrc_ file.

---

[← 7 Job Control](07-7-job-control.md) · [Up: contents](index.md) · [9 Shell Variables →](09-9-shell-variables.md)
