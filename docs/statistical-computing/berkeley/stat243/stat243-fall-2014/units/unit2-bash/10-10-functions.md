---
title: 10 Functions
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 Functions

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can define your own utilities by creating a shell function. This allows you to automate things that are more complicated than you can do with an alias. One nice thing about shell functions is that the shell automatically takes care of function arguments for you. It places the arguments given by the user into local variables in the function called (in order): _$1 $2 $3_ etc. It also fills _$#_ with the number of arguments given by the user. Here’s an example of using arguments in a function that saves me some typing when I want to copy a file to the SCF filesystem:

10

function putscf() {

scp $1 paciorek@radagast.berkeley.edu:~/$2 }

To use this function, I just do the following to copy _unit1.pdf_ from the current directory on whatever non-SCF machine I’m on to the directory _~/teaching/243_ on SCF:

> putscf unit1-unix.pdf Desktop/.

Of course you’d want to put such functions in your _.bashrc_ file.

---

[← 9 Shell Variables](09-9-shell-variables.md) · [Up: contents](index.md) · [11 If/then/else →](11-11-if-then-else.md)
