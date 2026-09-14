---
title: Unit 04 — programming Part 33 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 33 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• A related approach is to wrap data with a function using _with()_ .

x <- **rnorm** (10)

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **rm** (x) **myFun2** (3) ## [1] -2.085 5.469 1.227 3.698 -2.488 0.293 3.856 ## [8] 1.083 -0.768 2.271

x <- **rnorm** (1e7)

61

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **object.size** (myFun2)

---

[← Unit 04 — programming Part 32 —](32-unit-04-programming-part-32.md) · [Up: contents](index.md) · [1560 bytes →](34-1560-bytes.md)
