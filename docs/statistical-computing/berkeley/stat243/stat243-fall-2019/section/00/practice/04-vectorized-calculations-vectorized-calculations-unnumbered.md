---
title: Vectorized calculations {#vectorized-calculations .unnumbered}
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/00/practice.tex
source_file: sources/berkeley-stat243/stat243-fall-2019/section/00/practice.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Vectorized calculations {#vectorized-calculations .unnumbered}

**Source:** [`section/00/practice.tex`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/00/practice.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

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

[← Subsetting datastructures {#subsetting-datastructures .unnumbered}](03-subsetting-datastructures-subsetting-datastructures-unnumber.md) · [Up: contents](index.md) · [Using apply, sapply, and lapply {#using-apply-sapply-and-lapply .unnumbered} →](05-using-apply-sapply-and-lapply-using-apply-sapply-and-lapply.md)
