---
title: Alternative fitting procedures
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Alternative fitting procedures

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

So what do we do in these cases where we have potentially many parameters and few observations, but we want an accurate and interpretable model? We can constrain or *shrink* the coefficients to reduce the variance of our estimates at the cost of slightly increasing bias. This also can allow for improved model interpretability - by forcing some coefficients to be very small or to zero, we can more easily interpret our model by removing irrelevant covariates. We will discuss two major ways:

1. Ridge regression (L2 regularization)
2. LASSO regression (L1 regularization)

---

[← Cross-validation](01-cross-validation.md) · [Up: contents](index.md) · [Ridge regression →](03-ridge-regression.md)
