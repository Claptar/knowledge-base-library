---
title: Unit 06 — numbers Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 06 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Notice that we can represent the result accurately only up to the 16th decimal place. This suggests no need to show more than 16 decimal places and no need to print out any more when writing to a file. And of course, often we don’t need anywhere near that many. _Machine epsilon_ is the term used for indicating the accuracy of real numbers and it is defined as the smallest float, _x_ , such that 1 + _x̸_ = 1:

**dg** (1e-16 + 1) ## [1] "1.00000000000000000000"

**dg** (1e-15 + 1)

6

---

[← 2 Floating point basics](05-2-floating-point-basics.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 07 — →](07-unit-06-numbers-part-07.md)
