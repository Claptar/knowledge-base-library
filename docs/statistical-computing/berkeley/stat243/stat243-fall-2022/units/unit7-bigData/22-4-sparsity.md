---
title: 4. Sparsity
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Sparsity

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

A lot of statistical methods are based on sparse matrices. These
include:

-   Matrices representing the neighborhood structure (i.e., conditional
    dependence structure) of networks/graphs.
-   Matrices representing autoregressive models (neighborhood structure
    for temporal and spatial data)
-   A statistical method called the *lasso* is used in high-dimensional
    contexts to give sparse results (sparse parameter vector estimates,
    sparse covariance matrix estimates)
-   There are many others (I've been lazy here in not coming up with a
    comprehensive list, but trust me!)

When storing and manipulating sparse matrices, there is no need to store
the zeros, nor to do any computation with elements that are zero.

R, Python, and MATLAB all have functionality for storing and computing
with sparse matrices. We'll see this a bit more in the linear algebra
unit.

```r
require(spam)
mat = matrix(rnorm(1e8), 1e4)
mat[mat > (-2)] <- 0
sMat <- as.spam(mat)
print(object.size(mat), units = 'Mb') # 762.9 Mb
print(object.size(sMat), units = 'Mb') # 26 Mb

vec <- rnorm(1e4)
system.time(mat %*% vec)  # 0.385 seconds
system.time(sMat %*% vec) # 0.015 seconds
```

Here's a [blog
post](http://blog.revolutionanalytics.com/2011/05/the-neflix-prize-big-data-svd-and-r.html)
describing the use of sparse matrix manipulations for analysis of the
Netflix Prize data.

---

[← simple query to get 5 rows from a table](21-simple-query-to-get-5-rows-from-a-table.md) · [Up: contents](index.md) · [5. Using statistical concepts to deal with computational bottlenecks →](23-5-using-statistical-concepts-to-deal-with-computational-bott.md)
