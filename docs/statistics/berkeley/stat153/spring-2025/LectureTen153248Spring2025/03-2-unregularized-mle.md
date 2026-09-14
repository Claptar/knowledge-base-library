---
title: 2 (Unregularized) MLE
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 (Unregularized) MLE

**Source:** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Since (1) is a linear regression model, we can estimate the coefficients in the usual way by the MLE, or equivalently, least squares by minimizing


over all _β_ 0 _, . . . , βn−_ 1. The smallest value achievable in the above minimization will be the RSS. The MLE of _σ_ is then given by


Since there are as many coefficients as there are data points, this approach will give a perfect fit to the data leading to _RSS_ = 0. In fact, from the work done in the previous section, the values of _β_ 0 _, . . . , βn−_ 1 which minimize the sum of squares are given by:


for _j_ = 2 _, . . . , n −_ 1. This will lead to the estimated trend function _µt_ = _yt_ for all _t_ . Also the MLE of _σ_ will be zero. The unbiased estimate of _σ_ <u>(that</u> we previousy used in linear regression) will not exist because it will equal ~~�~~ _RSS/_ ( _n − p_ ) with _p_ = _n_ .

To summarize, these estimates will overfit the data, and will not produce a trend estimate that is simpler than the observed data.

---

[← 1 Parameter Interpretation in (1)](02-1-parameter-interpretation-in-1.md) · [Up: contents](index.md) · [3 Regularization →](04-3-regularization.md)
