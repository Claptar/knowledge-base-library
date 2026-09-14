---
title: Unbiased Estimation
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unbiased Estimation

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Recall from [Lecture 2](../estimation/index.md) that we had two primary strategies to choose an estimator:

1.  Summarize the risk function by a scalar (average or supremum)
2.  Restrict attention to a smaller class of estimators

Today we'll discuss *unbiased estimation*, which is an example of the second strategy. That is, if $g(\theta)$ is our estimand, we will require that $\EE_\theta \delta = g(\theta)$ for all $\theta$

Unbiased estimation is especially convenient in models with a complete sufficient statistic $T(X)$. In that case:

-   There is at most one unbiased estimator of the form $\delta(T(X))$, because if $\delta_1, \delta_2(T)$ are both unbiased, then $\delta_1 \eqas \delta_2$
-   If an unbiased estimator exists, it **uniformly minimizes** risk for any convex loss function

---

[Up: contents](index.md) · [Convex Loss Functions →](02-convex-loss-functions.md)
