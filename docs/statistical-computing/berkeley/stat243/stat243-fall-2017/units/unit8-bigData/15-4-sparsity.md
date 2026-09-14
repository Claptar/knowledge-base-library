---
title: 4 Sparsity
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Sparsity

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A lot of statistical methods are based on sparse matrices. These include:

- Matrices representing the neighborhood structure (i.e., conditional dependence structure) of networks/graphs.

- Matrices representing autoregressive models (neighborhood structure for temporal and spatial data)

- A statistical method called the _lasso_ is used in high-dimensional contexts to give sparse results (sparse parameter vector estimates, sparse covariance matrix estimates)

- There are many others (I’ve been lazy here in not coming up with a comprehensive list, but trust me!)

When storing and manipulating sparse matrices, there is no need to store the zeros, nor to do any computation with elements that are zero. A few of you exploited sparse matrices in PS4.

R, Matlab and Python all have functionality for storing and computing with sparse matrices. We’ll see this a bit more in the linear algebra unit.

**require** (spam) mat = **matrix** ( **rnorm** (1e8), 1e4) mat[mat > (-2)] <- 0 sMat <- **as.spam** (mat) **print** ( **object.size** (mat), units = 'Mb') _# 762.9 Mb_ **print** ( **object.size** (sMat), units = 'Mb') _# 26 Mb_ vec <- **rnorm** (1e4) **system.time** (mat %*% vec) _# 0.385 seconds_ **system.time** (sMat %*% vec) _# 0.015 seconds_

Here’s a blog post describing the use of sparse matrix manipulations for analysis of the Netflix Prize data.

---

[← 3 R and big data](14-3-r-and-big-data.md) · [Up: contents](index.md) · [5 Using statistical concepts to deal with computational bottlenecks →](16-5-using-statistical-concepts-to-deal-with-computational-bott.md)
