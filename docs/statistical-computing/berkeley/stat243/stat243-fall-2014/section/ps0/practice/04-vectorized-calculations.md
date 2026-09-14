---
title: Vectorized calculations
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/ps0/practice.tex
source_file: sources/berkeley-stat243/stat243-fall-2014/section/ps0/practice.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Vectorized calculations

**Source:** [`section/ps0/practice.tex`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/ps0/practice.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

1.  Create a vector of values $e^{2x} x^{\sqrt{x}}$ for $x = 1, 1.1, 1.2, ..., 2.9, 3.0$.

2.  Create the following:

    1.  A $5\times5$ matrix of zeros called `x`

    2.  See what `row(x)` and `col(x)` return

    3.  Using `row(x)` and `col(x)` create the following matrix: $$\left( \begin{array}{ccccc}
              0 & 1 & 0 & 0 & 0 \\
              1 & 0 & 1 & 0 & 0 \\
              0 & 1 & 0 & 1 & 0 \\
              0 & 0 & 1 & 0 & 1 \\
              0 & 0 & 0 & 1 & 0 \end{array} \right)$$

    4.  Using `row(x)` and `col(x)` create the following matrix: $$\left( \begin{array}{ccccc}
              0 & 1 & 2 & 3 & 4 \\
              1 & 0 & 1 & 2 & 3 \\
              2 & 1 & 0 & 1 & 2 \\
              3 & 2 & 1 & 0 & 1 \\
              4 & 3 & 2 & 1 & 0 \end{array} \right)$$

3.  Create the following matrices:

    1.  Using the R `outer` function (hint: look at its `FUN` argument) $$\left( \begin{array}{ccccc}
              0 & 1 & 2 & 3 & 4 \\
              1 & 2 & 3 & 4 & 5 \\
              2 & 3 & 4 & 5 & 6 \\
              3 & 4 & 5 & 6 & 7 \\
              4 & 5 & 6 & 7 & 8 \end{array} \right)$$

    2.  Modify what you did above $$\left( \begin{array}{ccccc}
              0 & 1 & 2 & 3 & 4 \\
              1 & 2 & 3 & 4 & 0 \\
              2 & 3 & 4 & 0 & 1 \\
              3 & 4 & 0 & 1 & 2 \\
              4 & 0 & 1 & 2 & 3 \end{array} \right)$$

---

[← Subsetting datastructures](03-subsetting-datastructures.md) · [Up: contents](index.md) · [Using apply, sapply, and lapply →](05-using-apply-sapply-and-lapply.md)
