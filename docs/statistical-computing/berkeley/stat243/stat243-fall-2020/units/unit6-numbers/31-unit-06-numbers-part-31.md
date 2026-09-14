---
title: Unit 06 — numbers Part 31 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 31 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

15

### **2.5 Working with higher precision numbers**

The _Rmpfr_ package allows us to work with numbers in higher precision. (This code is not working with _knitr_ , so I’m just showing the code here, not the output.)

**require** (Rmpfr) piLong <- **Const** ("pi", prec = 260) _# pi "computed" to correct 260-bit_ piLong _# nicely prints 80 digits_ **mpfr** (".1234567812345678", 40) **mpfr** (".1234567812345678", 80) **mpfr** (".1234567812345678", 600)

_precision_

In contrast to R, Python has arbitrary precision integers. So, e.g., pow(3423333, 15) returns an integer. But floating points are handled in similar fashion to R.

---

[← Unit 06 — numbers Part 30 —](30-unit-06-numbers-part-30.md) · [Up: contents](index.md) · [3 Implications for calculations and comparisons →](32-3-implications-for-calculations-and-comparisons.md)
