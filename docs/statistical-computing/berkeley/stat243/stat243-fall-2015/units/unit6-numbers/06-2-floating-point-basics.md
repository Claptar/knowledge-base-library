---
title: 2 Floating point basics
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Floating point basics

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Representing real numbers**

Reals (also called floating points) are stored on the computer as an approximation, albeit a very precise approximation. As an example, with a double, the error in the distance from the earth to the sun is around a millimeter. However, we need to be very careful if we’re trying to do a calculation that produces a very small (or very large number) and particularly when we want to see if numbers are equal to each other.

0.3 - 0.2 == 0.1 ## [1] FALSE 0.3 ## [1] 0.3 0.2 ## [1] 0.2 0.1 _# Hmmm..._ ## [1] 0.1 **options** (digits=22) _# on some machines this may not have # have any effect in showing more digits... # should work on BCE_ a <- 0.3 b <- 0.2 a ## [1] 0.2999999999999999888978 b ## [1] 0.2000000000000000111022 a - b

5

---

[← Unit 06 — numbers Part 05 —](05-unit-06-numbers-part-05.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 07 — →](07-unit-06-numbers-part-07.md)
