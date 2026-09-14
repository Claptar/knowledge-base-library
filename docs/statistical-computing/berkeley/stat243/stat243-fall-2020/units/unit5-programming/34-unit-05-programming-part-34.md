---
title: Unit 05 — programming Part 34 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 34 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Comprehension problem** Here’s a case where something I tried failed and I had to think more carefully about scoping to understand why.

**set.seed** (1) **rnorm** (1) ## [1] -0.626 **save** (.Random.seed, file = 'tmp.Rda') **rnorm** (1) ## [1] 0.184 tmp <- **function** () { **load** ('tmp.Rda') **print** ( **rnorm** (1)) } **tmp** () ## [1] -0.836

Question: what was I hoping that code to do, and why didn’t it work?

58

**Detecting non-local variables** We can use _codetools::findGlobals_ to detect non-local variables when we are programming.

**library** (codetools) f <- **function** () { y <- 3 **print** (x + y) } **findGlobals** (f)

---

[← Unit 05 — programming Part 33 —](33-unit-05-programming-part-33.md) · [Up: contents](index.md) · [[1] "{" "+" "<-" "print" "x" →](35-1---print-x.md)
