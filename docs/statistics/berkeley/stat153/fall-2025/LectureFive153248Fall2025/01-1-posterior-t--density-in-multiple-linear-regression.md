---
title: 1 Posterior t -density in Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Posterior t -density in Multiple Linear Regression

**Source:** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we saw the following formula for the posterior distribution in multiple linear regression:


Recall in multiple regression: the data is ( _xi_ 1 _, . . . , xim, yi_ ) _, i_ = 1 _, . . . , n_ , and the model is:


For doing calculations in regression, we use the matrix notation:


In terms of this notation, we can rewrite the model equation (2) as:


In (1), _S_ ( _β_<sup>ˆ</sup> ) denotes the sum of squares evaluated at the least squares estimator. It is the smallest possible value of the sum of squares, and it is also known as the Residual Sum of Squares (RSS).

(1) represents the joint density of ( _β_ 0 _, . . . , βm_ ) given the observed data. It turns out that the posterior distribution of each individual _βj_ is also given by a _t_ -density. This follows from properties of the multivariate _t_ -density which we go over next.

1

---

[Up: contents](index.md) · [2 t -density →](02-2-t--density.md)
