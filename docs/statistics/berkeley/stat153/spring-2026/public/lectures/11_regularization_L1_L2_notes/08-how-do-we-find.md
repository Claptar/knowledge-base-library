---
title: How do we find $\lambda$?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# How do we find $\lambda$?

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

* Cross-validation! Typically, we will choose a range of values for $\lambda$, then fit models using cross-validation and select the parameter for which CV-error is smallest
* Remember for time series we *must* do cross validation that preserves the time series structure / autocorrelations in our stimulus!!
* You will see this in your lab!

---

[← A geometric comparison](07-a-geometric-comparison.md) · [Up: contents](index.md)
