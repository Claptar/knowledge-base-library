---
title: '[1] "language" ## [1] "{"'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "language" ## [1] "{"

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We’ll see more about objects relating to the R language and parsed code in Section 9. For now, just realize that the parsed code itself is treated as an object(s) with certain types and certain classes.

do.call()

The do.call() function will apply a function to the elements of a list. For example, we can rbind() together (if compatible) the elements of a list of vectors instead of having to loop over the elements or manually type them in:

myList <- **list** (a = 1:3, b = 11:13, c = 21:23) **args** (rbind) ## function (..., deparse.level = 1) ## NULL

**rbind** (myList$a, myList$b, myList$c)

---

[← 6 Functions, variable scope, and frames](40-6-functions-variable-scope-and-frames.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 42 — →](42-unit-04-programming-partial-part-42.md)
