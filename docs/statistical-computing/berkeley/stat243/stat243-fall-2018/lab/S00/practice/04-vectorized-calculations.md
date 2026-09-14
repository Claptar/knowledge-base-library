---
title: Vectorized calculations
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S00/practice.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S00/practice.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Vectorized calculations

**Source:** [`lab/S00/practice.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S00/practice.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Create a vector of values _e_<sup>2</sup><sup>_x_</sup> _x_ _~~√~~ x_ for _x_ = 1 _,_ 1 _._ 1 _,_ 1 _._ 2 _, ...,_ 2 _._ 9 _,_ 3 _._ 0.

2. Create the following:

   - (a) A 5 _×_ 5 matrix of zeros called `x`

   - (b) See what `row(x)` and `col(x)` return

   - (c) Create the following matrix (you could use part (c) for this):


- (d) Using `row(x)` and `col(x)` , create the following matrix:


3. Create the following matrices:

   - (a) (Hint: `outer` works well here)


- (b) (Hint: Modify what you did above)


4. Normalize rows and columns

   - (a) Create a 5 _×_ 6 matrix of numbers uniformly drawn from the interval (1 _,_ 100) call it `m1` .

   - (b) Normalize the rows of `m1` so that they sum to 1. Call this matrix `m2`

   - (c) Use `apply` on `m2` to verify that the rows sum to 1. Now use `rowSums` to do the same thing. Which is better? `rowSums` or `apply` ?.

   - (d) Repeat the last two steps but normalize the columns.

5. Linear model

   - (a) Create a vector `x` containing `1, 1.1, 1.2, ..., 9.9, 10.0`

   - (b) Create a vector y that is twice `x` but with standard Gaussian noise added

   - (c) Create a scatterplot

   - (d) Create an `lm` object where `y` depends on `x` called `my lm`

   - (e) Use `lapply` to find the classes of the elements of `my` ~~`l`~~ `m`

   - (f) Use `sapply` to find the classes of the elements of `my` ~~`l`~~ `m`

   - (g) Do they differ? Why or why not? When would they differ and when would they be the same?

2

---

[← Subsetting datastructures](03-subsetting-datastructures.md) · [Up: contents](index.md) · [Functions →](05-functions.md)
