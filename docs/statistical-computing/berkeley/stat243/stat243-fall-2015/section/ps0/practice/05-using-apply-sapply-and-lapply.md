---
title: Using apply, sapply, and lapply
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/ps0/practice.tex
source_file: sources/berkeley-stat243/stat243-fall-2015/section/ps0/practice.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Using apply, sapply, and lapply

**Source:** [`section/ps0/practice.tex`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/ps0/practice.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

1.  Normalize rows and columns

    1.  Create a $5\times 6$ matrix of numbers uniformly drawn from the interval $(1,\ 100)$ call it `m1`.

    2.  Create a new matrix `m2` using `apply` to normalize the rows so that they sum to 1. You will need to write a little function to use inside of the `apply` call. Check the dimensions of `m2`. Are they the same as `m1`? Why?

    3.  Use `apply` on `m2` to verify that the rows sum to 1. Now use `rowSums` to do the same thing. Why would you use `rowSums` instead of `apply`.

    4.  Repeat the last two steps but normalize the columns.

2.  Linear model

    1.  Create a vector `x` containing `1, 1.1, 1.2, ..., 9.9, 10.0`

    2.  Create a vector y that is twice `x` but with standard Gaussian noise added

    3.  Create a scatterplot

    4.  Create an `lm` object where `y` depends on `x` called `my_lm`

    5.  Use `lapply` to find the classes of the elements of `my_lm`

    6.  Use `sapply` to find the classes of the elements of `my_lm`

    7.  Do they differ? Why or why not? When would they differ and when would they be the same?

---

[← Vectorized calculations](04-vectorized-calculations.md) · [Up: contents](index.md) · [Functions →](06-functions.md)
