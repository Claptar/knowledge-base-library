---
title: 5. Sparsity
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit5-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Sparsity

**Source:** [`units/unit5-bigData.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit5-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

Python, R, and MATLAB all have functionality for storing and computing
with sparse matrices. We'll see this a bit more in the linear algebra
unit.

Here's a [blog
post](http://blog.revolutionanalytics.com/2011/05/the-neflix-prize-big-data-svd-and-r.html)
describing the use of sparse matrix manipulations for analysis of the
Netflix Prize data.

---

[← 4. Recent tools and data storage formats](14-4-recent-tools-and-data-storage-formats.md) · [Up: contents](index.md) · [6. Using statistical concepts to deal with computational bottlenecks →](16-6-using-statistical-concepts-to-deal-with-computational-bott.md)
