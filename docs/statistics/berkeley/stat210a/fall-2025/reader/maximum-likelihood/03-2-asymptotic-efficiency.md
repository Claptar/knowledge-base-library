---
title: 2 Asymptotic Efficiency
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/maximum-likelihood.html
source_file: sources/berkeley-stat210a/fall-2025/reader/maximum-likelihood.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Asymptotic Efficiency

**Source:** [`reader/maximum-likelihood.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/maximum-likelihood.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

In the exponential family case, generalizes to a much broader class of models

Setting: <span class="math inline">\$X\_1, \\ldots, X\_n \\stackrel{\\text{iid}}{\\sim} p\_\\theta(x)\$</span>, <span class="math inline">\$\\theta \\in \\mathbb{R}^d\$</span>

<span class="math inline">\$p\_\\theta\$</span> smooth in <span class="math inline">\$\\theta\$</span> (e.g., 2 cts integrable derives, can be relaxed)

Let <span class="math inline">\$\\ell\_i(\\theta; X) = \\log p\_\\theta(X\_i)\$</span>, <span class="math inline">\$\\ell\_n(\\theta; X) = \\sum\_{i=1}^n \\ell\_i(\\theta; X)\$</span>

<span class="math inline">\$S\_n(\\theta) = \\nabla\_\\theta \\ell\_n(\\theta; X)\$</span>, <span class="math inline">\$J\_n(\\theta) = \\text{Var}\_\\theta$$\\nabla\_\\theta \\ell\_n(\\theta; X)$$ = nJ\_1(\\theta)\$</span>

We say an estimator is asymptotically efficient if <span class="math inline">\$\\sqrt{n}(\\hat{\\theta}\_n - \\theta) \\xrightarrow{d} N(0, J\_1^{-1}(\\theta))\$</span>

Delta method for differentiable estimand <span class="math inline">\$g(\\theta)\$</span>:

<span class="math inline">\$\\sqrt{n}(g(\\hat{\\theta}\_n) - g(\\theta)) \\xrightarrow{d} N(0, \\nabla g(\\theta)^T J\_1^{-1}(\\theta) \\nabla g(\\theta))\$</span>

Also achieves CRLB if <span class="math inline">\$\\hat{\\theta}\_n\$</span> does, <span class="math inline">\$g\$</span> diff

---

[← 1 Maximum Likelihood Estimation](02-1-maximum-likelihood-estimation.md) · [Up: contents](index.md) · [3 Asymptotic Distribution of MLE →](04-3-asymptotic-distribution-of-mle.md)
