---
title: 13 How much shell scripting should I learn?
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 13 How much shell scripting should I learn?

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can do a fair amount of what you need from within R using the _system()_ function. This will enable you to avoid dealing with a lot of shell programming syntax (but you’ll still need to know how to use UNIX utilities, wildcards, and pipes to be effective). Example: a fellow student when I was in grad school programmed a tool in R to extract concert information from the web for bands appearing in her iTunes library. Not the most elegant solution, but it got the job done.

11

For more extensive shell programming, it’s probably worth learning Python and doing it there rather than using a shell script. In particular iPython makes it very easy to interact with the operating system.

---

[← 12 For loops](12-12-for-loops.md) · [Up: contents](index.md) · [14 Version Control →](14-14-version-control.md)
