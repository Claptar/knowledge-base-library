---
title: 10. Summary
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 10. Summary

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The different methods of optimization have different advantages and
disadvantages.

According to Lange, MM and EM are numerically stable and computationally
simple but can converge very slowly. Newton's method shows very fast
convergence but has the downsides we've discussed. Quasi-Newton methods
fall in between. Convex optimization generally comes up when optimizing
under constraints.

One caution about optimizing under constraints is that you just get a
point estimate; quantifying uncertainty in your estimator is more
difficult. One strategy is to ignore the inactive inequality constraints
and reparameterize (based on the active equality constraints) to get an
unconstrained problem in a lower-dimensional space. Then you can make
use of the Hessian in the usual fashion to estimate the information
matrix.

---

[← 9. Optimization under constraints](14-9-optimization-under-constraints.md) · [Up: contents](index.md)
