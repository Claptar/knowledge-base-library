---
title: Unit 04 — usingR Part 25 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 25 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Vectorized subsetting** We can subset vectors, matrices, and rows of data frames by index or by logical vectors.

**set.seed** (0) vec <- **rnorm** (8) mat <- **matrix** ( **rnorm** (9), 3) vec ## [1] 1.263 -0.326 1.330 1.272 0.415 -1.540 -0.929 ## [8] -0.295 mat ## [,1] [,2] [,3] ## [1,] -0.00577 -0.799 -0.299 ## [2,] 2.40465 -1.148 -0.412 ## [3,] 0.76359 -0.289 0.252 vec[vec < 0] ## [1] -0.326 -1.540 -0.929 -0.295

26

vec[vec < 0] <- 0 vec ## [1] 1.263 0.000 1.330 1.272 0.415 0.000 0.000 0.000 mat[mat[, 1] < 0, ] _# similarly for data frames_ ## [1] -0.00577 -0.79901 -0.29922 mat[mat[, 1] < 0, 2:3] _# similarly for data frames_ ## [1] -0.799 -0.299 mat[, mat[1, ] < 0] ## [,1] [,2] [,3] ## [1,] -0.00577 -0.799 -0.299 ## [2,] 2.40465 -1.148 -0.412 ## [3,] 0.76359 -0.289 0.252 mat[mat[, 1] < 0, 2:3] <- 0 **set.seed** (0) _# so we get the same vec as we had before_ vec <- **rnorm** (8) wh <- **which** (vec < 0) logicals <- vec < 0 logicals ## [1] FALSE TRUE FALSE FALSE FALSE TRUE TRUE TRUE wh ## [1] 2 6 7 8 **identical** (vec[wh], vec[logicals]) ## [1] TRUE vec <- **c** (1L, 2L, 1L) **is.integer** (vec) ## [1] TRUE vec[vec == 1L] _# in general, not safe with numeric vectors_ ## [1] 1 1 vec[vec != 3L] _# nor this_ ## [1] 1 2 1

27

Finally, we can also subset a matrix with a two-column matrix of {row,column} indices.

mat <- **matrix** ( **rnorm** (25), 5) rowInd <- **c** (1, 3, 5) colInd <- **c** (1, 1, 4) mat[ **cbind** (rowInd, colInd)] ## [1] -0.00577 0.76359 -0.69095

**Indexing and factors** Be careful of using factors as indices for subsetting:

students <- **factor** ( **c** ("basic", "proficient", "advanced", "basic", "advanced", "minimal")) score = **c** (minimal = 3, basic = 1, advanced = 13, proficient = 7) score["advanced"] ## advanced ## 13 score[students[3]] ## minimal ## 3 score[ **as.character** (students[3])] ## advanced ## 13

What has gone wrong?

**apply()** The _apply()_ function will apply a given function to either the rows or columns of a matrix or a set of dimensions of an array:

x <- **matrix** (1:6, nr = 2) x ## [,1] [,2] [,3]

28

---

[← [1] FALSE vec <- c (mat) mat2 <- matrix (vec, nr = 50) identical (mat, mat2) ## [1] TRUE](24-1-false-vec---c-mat-mat2---matrix-vec-nr-50-identical-mat-ma.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 26 — →](26-unit-04-usingr-part-26.md)
