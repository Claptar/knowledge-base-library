---
title: Creating datastructures
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/00/practice.tex
source_file: sources/berkeley-stat243/stat243-fall-2019/section/00/practice.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Creating datastructures

**Source:** [`section/00/practice.tex`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/00/practice.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

1.  Create the following vectors:

    1.  `1, 2, 3, ..., 49, 50`

    2.  a logical vector that is `TRUE` exactly when the corresponding element of the above vector is even

    3.  `50, 49, ..., 3, 2, 1`

    4.  `1, 2, 3, ..., 49, 50, 49, ..., 3, 2, 1`

    5.  `-10, -9, -8, ..., 8, 9, 10`

    6.  `3, 6, 9, ..., 45, 48`

    7.  `"3", "6", "9", ..., "45", "48"` (Hint: use the previous vector)

    8.  `"a", "a", "a", "a", "b", "b", "b", "c", "c", "d"` (Hint: use `rep`)

    9.  turn the above character vector into a factor vector

    10. 200 numbers between -1 and 1 (inclusive) (Hint: use `seq`)

2.  Create a data frame through the following steps:

    1.  Create a vector `1, 2, 3, ..., 49, 50` and call it `x`

    2.  Create a vector by taking the cosine of x and call it `y`

    3.  Create a vector by taking the tagent of y and call it `z`

    4.  Create a vector by multiplying the elements of y and z and call it `w`

    5.  Create a logical vector that is TRUE exactly when `x` is between 10 and 29 inclusively and call it `f`

    6.  Create a data frame with column names `x, y, z, w, f` in that order with the obvious content and call it `df1`

    7.  How would you change the names of `df1` to uppercase letters?

    8.  What would you have done differently if you wanted to use `x` as the row names instead of making it a column? Would you have needed to use `x`?

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Subsetting datastructures →](03-subsetting-datastructures.md)
