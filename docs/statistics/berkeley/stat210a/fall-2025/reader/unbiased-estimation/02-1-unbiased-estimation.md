---
title: 1 Unbiased Estimation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Unbiased Estimation

**Source:** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Recall from [Lecture 2](../estimation/index.md) that we had two primary strategies to choose an estimator:

1.  Summarize the risk function by a scalar (average or supremum)
2.  Restrict attention to a smaller class of estimators

Today we’ll discuss *unbiased estimation*, which is an example of the second strategy. That is, if <span class="math inline">\$g(\\theta)\$</span> is our estimand, we will require that <span class="math inline">\$\\EE\_\\theta \\delta = g(\\theta)\$</span> for all <span class="math inline">\$\\theta\$</span>

Unbiased estimation is especially convenient in models with a complete sufficient statistic <span class="math inline">\$T(X)\$</span>. In that case:

- There is at most one unbiased estimator of the form <span class="math inline">\$\\delta(T(X))\$</span>, because if <span class="math inline">\$\\delta\_1, \\delta\_2(T)\$</span> are both unbiased, then <span class="math inline">\$\\delta\_1 \\eqas \\delta\_2\$</span>
- If an unbiased estimator exists, it **uniformly minimizes** risk for any convex loss function

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Convex Loss Functions →](03-2-convex-loss-functions.md)
