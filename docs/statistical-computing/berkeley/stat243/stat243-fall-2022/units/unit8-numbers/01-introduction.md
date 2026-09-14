---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit8-numbers.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit8-numbers.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

[PDF](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit8-numbers.pdf){.btn .btn-primary}


References:

-   Gentle, Computational Statistics, Chapter 2.
-   [http://www.lahey.com/float.htm](http://www.lahey.com/float.htm)
-   And for more gory detail, see Monahan, Chapter 2.

A quick note that, as we've already seen, R's version of scientific
notation is `XeY`, which means $X\cdot10^{Y}$.

A second note is that the concepts developed here apply outside of R,
but we'll illustrate the principles of computer numbers using R. R makes
use of the *double* and *int* types in C for the underlying
representation of R's numbers in C variables, so what we'll really be
seeing is how such types behave in C on most modern machines. The behavior
of real-valued numbers in Python is essentially the same, but
Python handles the integer type differently.

Videos (optional):

There are various videos from 2020 in the bCourses Media Gallery that you
can use for reference if you want to.

  - Video 1. Bits, bytes, and integers
  - Video 2. Double precision numbers: intro
  - Video 3. Double precision numbers: details
  - Video 4. Overflow and integers vs. doubles

---

[Up: contents](index.md) · [1. Basic representations →](02-1-basic-representations.md)
