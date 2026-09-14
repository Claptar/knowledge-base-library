---
title: Unit 06 — numbers Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 04 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Finally note that the set of computer integers is not closed under arithmetic, with R reporting an overflow (i.e., a result that is too large to be stored as an integer):

a <- **as.integer** (3423333) _# 3423333L_ a * a ## Warning in a * a: NAs produced by integer overflow ## [1] NA

Real numbers (or _floating points_ ) use a minimum of 4 bytes, for single precision floating points. In general 8 bytes are used to represent real numbers on a computer and these are called _double precision floating points_ or _doubles_ . Let’s see some examples in R of how much space different types of variables take up.

Let’s see how this plays out in terms of memory use in R.

doubleVec <- **rnorm** (100000) intVec <- 1:100000 **set.seed** (0) charVec <- **sample** (letters, 100000, replace = TRUE) **object.size** (doubleVec)

3

---

[← Unit 06 — numbers Part 03 —](03-unit-06-numbers-part-03.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 05 — →](05-unit-06-numbers-part-05.md)
