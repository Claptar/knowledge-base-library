---
title: Unit 06 — numbers Part 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 08 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Notice that we can represent the result accurately only up to the 16th decimal place. This suggests no need to show more than 16 decimal places and no need to print out any more when writing to a file. And of course, often we don’t need anywhere near that many. _Machine epsilon_ is the term used for indicating the accuracy of real numbers and it is defined as the smallest float, _x_ , such that 1 + _x̸_ = 1:

**dg** (1e-16 + 1) ## [1] "1.00000000000000000000" **dg** (1e-15 + 1) ## [1] "1.00000000000000111022" **dg** (2e-16 + 1)

6

---

[← 2 Floating point basics](07-2-floating-point-basics.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 09 — →](09-unit-06-numbers-part-09.md)
