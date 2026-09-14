---
title: Overview
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit8-numbers.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit8-numbers.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Overview

**Source:** [`units/unit8-numbers.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit8-numbers.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

References:

-   Gentle, Computational Statistics, Chapter 2.
-   [http://www.lahey.com/float.htm](http://www.lahey.com/float.htm)
-   And for more gory detail, see Monahan, Chapter 2.

A quick note that, as we've already seen, Python's version of scientific
notation is `XeY`, which means $X\cdot10^{Y}$.

A second note is that the concepts developed here apply outside of Python,
but we'll illustrate the principles of computer numbers using Python.
Python usually makes use of the *double* type (8 bytes) in C for the underlying
representation of real-valued numbers in C variables, so what we'll really be
seeing is how such types behave in C on most modern machines.
It's actually a bit more complicated in that one can use real-valued numbers
that use something other than 8 bytes in numpy by specifying a `dtype`.

The handling of integers is even more complicated. In numpy, the default
is 8 byte integers, but other integer dtypes are available. And in Python
itself, integers can be arbitrarily large.

---

[Up: contents](index.md) · [1. Basic representations →](02-1-basic-representations.md)
