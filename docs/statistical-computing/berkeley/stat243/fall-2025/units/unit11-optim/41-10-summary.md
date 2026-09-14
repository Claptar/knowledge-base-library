---
title: 10. Summary
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 10. Summary

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← 9. Optimization under constraints](40-9-optimization-under-constraints.md) · [Up: contents](index.md)
