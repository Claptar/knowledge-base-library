---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Unit 6: Computer numbers

October 1, 2015

References:

- Gentle, Computational Statistics, Chapter 2.

- http://www.lahey.com/float.htm

- And for more gory detail, see Monahan, Chapter 2.

A quick note that, as we’ve already seen, R’s version of scientific notation is _XeY_ , which means _X ·_ 10<sup>_Y_</sup> .

A second note is that the concepts developed here apply outside of R, but we’ll illustrate the principles of computer numbers using R. R makes use of the _double_ and _int_ types in C for the underlying representation of R’s numbers in C variables, so what we’ll really be seeing is how such types behave in C on most modern machines.

---

[Up: contents](index.md) · [1 Basic representations →](02-1-basic-representations.md)
