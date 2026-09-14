---
title: Using apply , sapply , and lapply
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/practice.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/ps/practice.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using apply , sapply , and lapply

**Source:** [`ps/practice.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/practice.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Normalize rows and columns

   - (a) Create a 5 _×_ 6 matrix of numbers uniformly drawn from the interval (1 _,_ 100) call it `m1` .

   - (b) Create a new matrix `m2` using `apply` to normalize the rows so that they sum to 1. You will need to write a little function to use inside of the `apply` call. Check the dimensions of `m2` . Are they the same as `m1` ? Why?

   - (c) Use `apply` on `m2` to verify that the rows sum to 1. Now use `rowSums` to do the same thing. Why would you use `rowSums` instead of `apply` .

   - (d) Repeat the last two steps but normalize the columns.

2. Linear model

   - (a) Create a vector `x` containing 1, 1.1, 1.2, ..., 9.9, 10.0

   - (b) Create a vector y that is twice `x` but with standard Gaussian noise added

2

- (c) Create a scatterplot

- (d) Create an `lm` object where `y` depends on `x` called `my lm`

- (e) Use `lapply` to find the classes of the elements of `my` ~~`l`~~ `m`

- (f) Use `sapply` to find the classes of the elements of `my` ~~`l`~~ `m`

- (g) Do they differ? Why or why not? When would they differ and when would they be the same?

---

[← Vectorized calculations](04-vectorized-calculations.md) · [Up: contents](index.md) · [Functions →](06-functions.md)
