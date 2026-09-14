---
title: Unit 05 — programming Part 28 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 28 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We’ll see more about objects relating to the R language and parsed code in Section 9. For now, just realize that the parsed code itself is treated as an object(s) with certain types and certain classes.

#### **_do.call()_**

The _do.call()_ function will apply a function to the elements of a list. For example, we can _rbind()_ together (if compatible) the elements of a list of vectors instead of having to loop over the elements or manually type them in:

myList <- **list** (a = 1:3, b = 11:13, c = 21:23) **args** (rbind) ## function (..., deparse.level = 1) ## NULL **rbind** (myList$a, myList$b, myList$c) ## [,1] [,2] [,3]

44

---

[← Unit 05 — programming Part 27 —](27-unit-05-programming-part-27.md) · [Up: contents](index.md) · [Unit 05 — programming Part 29 — →](29-unit-05-programming-part-29.md)
