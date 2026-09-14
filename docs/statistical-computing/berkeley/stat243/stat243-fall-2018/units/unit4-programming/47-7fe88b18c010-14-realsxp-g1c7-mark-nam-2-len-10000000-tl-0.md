---
title: '@7fe88b18c010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# @7fe88b18c010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that in this example, if you use _address()_ instead of _.Internal(inspect())_ it’s not really clear what is going on.

In fact, this occurs outside function calls as well. Copies of objects are not made until one of the objects is actually modified. Initially, the copy points to the same memory location as the original object.

y <- **rnorm** (1e7) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 850196 45.5 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 61497017 469.2 1.12e+08 856.1 1.31e+08 1003.1 **address** (y)

85

---

[← @7fe88b18c010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)](46-7fe88b18c010-14-realsxp-g1c7-mark-nam-2-len-10000000-tl-0.md) · [Up: contents](index.md) · [Unit 04 — programming Part 48 — →](48-unit-04-programming-part-48.md)
