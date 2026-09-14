---
title: '[1] FALSE vec <- c (mat) mat2 <- matrix (vec, nr = 50) identical (mat, mat2)
  ## [1] TRUE'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] FALSE vec <- c (mat) mat2 <- matrix (vec, nr = 50) identical (mat, mat2) ## [1] TRUE

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If you want to fill a matrix row-wise:

**matrix** (1:4, 2, byrow = TRUE) ## [,1] [,2] ## [1,] 1 2 ## [2,] 3 4

Column-major ordering is also used in Matlab and Fortran, while row-major ordering is used in C.

**Identifying elements by index** You can figure out the indices of elements having a given characteristic using _which()_ :

x <- **c** (1, 10, 2, 9, 3, 8) **which** (x < 3) ## [1] 1 3 x <- **matrix** (1:6, nrow = 2) **which** (x < 3, arr.ind = TRUE) ## row col ## [1,] 1 1 ## [2,] 2 1

_which.max()_ and _which.min()_ have similar sort of functionality.

We can determine which elements match those in another set with _%in%_ (to return logicals) or _match()_ (to return indices that describe the mapping):

25

set <- **c** ("Mazda RX4", "Merc 240D", "Fiat 128") **row.names** (mtcars) %in% set

---

[← Unit 04 — usingR Part 23 —](23-unit-04-usingr-part-23.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 25 — →](25-unit-04-usingr-part-25.md)
