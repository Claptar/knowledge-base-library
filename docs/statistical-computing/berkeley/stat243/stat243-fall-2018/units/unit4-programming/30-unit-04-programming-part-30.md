---
title: Unit 04 — programming Part 30 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 30 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**rbind** (myList) ## a b c ## myList Integer,3 Integer,3 Integer,3 **do.call** (rbind, myList) ## [,1] [,2] [,3] ## a 1 2 3 ## b 11 12 13 ## c 21 22 23

41

Why couldn’t we just use _rbind()_ directly? Basically we’re using _do.call()_ to use functions that take “...” as input (i.e., functions accepting an arbitrary number of arguments) and to use the list as the input instead (i.e., to use the list elements).

More generally do.call() is a way to pass arguments to a function where the arguments are a list:

**do.call** (mean, **list** (1:10, na.rm = TRUE)) ## [1] 5.5

### **6.2 Inputs**

Arguments can be specifed in the correct order, or given out of order by specifying _name = value_ . R first tries to match arguments by name and then by position. In general the more important arguments are specified first. You can see the arguments and defaults for a function using _args()_ :

**args** (lm)

---

[← 6 Functions, variable scope, and frames](29-6-functions-variable-scope-and-frames.md) · [Up: contents](index.md) · [Unit 04 — programming Part 31 — →](31-unit-04-programming-part-31.md)
