---
title: Creating datastructures
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S00/practice.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S00/practice.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Creating datastructures

**Source:** [`lab/S00/practice.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S00/practice.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Create the following vectors as tersely as possible:

   - (a) `1, 2, 3, ..., 49, 50`

   - (b) a logical vector that is `TRUE` exactly when the corresponding element of the above vector is even (c) `50, 49, ..., 3, 2, 1`

(d) `1, 2, 3, ..., 49, 50, 49, ..., 3, 2, 1` (e) `-10, -9, -8, ..., 8, 9, 10` (f) `3, 6, 9, ..., 45, 48` (g) `"3", "6", "9", ..., "45", "48"` (Hint: use the previous vector) (h) `"a", "a", "a", "a", "b", "b", "b", "c", "c", "d"` (Hint: use `rep` )

- (i) turn the above character vector into a factor vector

- (j) 200 evenly spaced numbers between -1 and 1 (inclusive)

2. Create a data frame through the following steps:

- (a) Create a vector `1, 2, 3, ..., 49, 50` and call it `x`

- (b) Create a vector by taking the cosine of x and call it `y`

- (c) Create a vector by taking the tagent of y and call it `z`

- (d) Create a vector by multiplying the elements of y and z and call it `w`

- (e) Create a logical vector that is TRUE exactly when `x` is between 10 and 29 inclusively and call it `f`

- (f) Create a data frame with column names `x, y, z, w, f` in that order with the obvious content and call it `df1`

- (g) Change the names of `df1` to uppercase letters.

- (h) What would you have done differently if you wanted to use `x` as the row names instead of making it a column? Would you have needed to use `x` ?

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Subsetting datastructures →](03-subsetting-datastructures.md)
