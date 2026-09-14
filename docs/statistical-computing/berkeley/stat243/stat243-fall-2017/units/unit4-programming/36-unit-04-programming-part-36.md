---
title: Unit 04 — programming Part 36 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 36 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• A related approach is to wrap data with a function using _with()_ .

x <- **rnorm** (10)

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **rm** (x) **myFun2** (3) ## [1] -4.614 2.132 2.458 4.069 -3.814 3.707 -3.463 ## [8] 2.041 0.021 -2.204

x <- **rnorm** (1e7)

62

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **object.size** (myFun2)

---

[← [16] "/usr/lib/R/library/base"](35-16-usr-lib-r-library-base.md) · [Up: contents](index.md) · [1560 bytes →](37-1560-bytes.md)
