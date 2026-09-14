---
title: '@7f40dc8b7010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# @7f40dc8b7010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that in this example, if you use _address()_ instead of _.Internal(inspect())_ it’s not really clear what is going on.

In fact, this occurs outside function calls as well. Copies of objects are not made until one of the objects is actually modified. Initially, the copy points to the same memory location as the original object.

y <- **rnorm** (1e7) **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 781895 41.8 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 61410626 468.6 1.12e+08 855.5 1.31e+08 1002.4 **address** (y)

---

[← @7f40dc8b7010 14 REALSXP g1c7 [MARK,NAM(2)] (len=10000000, tl=0)](46-7f40dc8b7010-14-realsxp-g1c7-mark-nam-2-len-10000000-tl-0.md) · [Up: contents](index.md) · [[1] "0x7f40d7c6b010" x <- y gc () →](48-1-0x7f40d7c6b010-x---y-gc.md)
