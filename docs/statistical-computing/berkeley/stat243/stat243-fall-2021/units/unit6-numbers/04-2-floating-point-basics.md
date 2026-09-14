---
title: 2 Floating point basics
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit6-numbers.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Floating point basics

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Representing real numbers**

Reals (also called floating points) are stored on the computer as an approximation, albeit a very precise approximation. As an example, if we represent the distance from the earth to the sun using a double, the error is around a millimeter. However, we need to be very careful if we’re trying to do a calculation that produces a very small (or very large number) and particularly when we want to see if numbers are equal to each other.

0.3 - 0.2 == 0.1 ## [1] FALSE 0.3 ## [1] 0.3 0.2 ## [1] 0.2 0.1 _# Hmmm..._ ## [1] 0.1 0.75 - 0.5 == 0.25

5

---

[← Unit 06 — numbers Part 03 —](03-unit-06-numbers-part-03.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 05 — →](05-unit-06-numbers-part-05.md)
