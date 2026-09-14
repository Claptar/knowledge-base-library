---
title: 5 Deduced Inference
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 Deduced Inference

**Source:** [`reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Given any joint confidence region <span class="math inline">\$C(X)\$</span> for <span class="math inline">\$\\theta \\in \\Theta\$</span>, we may freely assume <span class="math inline">\$\\theta \\in C(X)\$</span> and deduce any and all implied conclusions without any FWER inflation:

<span class="math inline">\$\\mathbb{P}\_\\theta(\\text{any deduced inference is wrong}) \\leq \\mathbb{P}\_\\theta(\\theta \\notin C(X)) \\leq \\alpha\$</span>

Deduction is often a good paradigm for deriving simultaneous intervals

We say <span class="math inline">\$C\_1(X),\\ldots,C\_m(X)\$</span> are simultaneous <span class="math inline">\$1-\\alpha\$</span> confidence intervals for <span class="math inline">\$g\_1(\\theta),\\ldots,g\_m(\\theta)\$</span> if:

<span class="math inline">\$\\mathbb{P}\_\\theta(g\_i(\\theta) \\in C\_i(X) \\text{ for all } i = 1,\\ldots,m) \\geq 1-\\alpha\$</span>

### <span class="header-section-number">5.1</span> Example: Simultaneous Intervals for Multivariate Gaussian {.anchored number="5.1" anchor-id="example-simultaneous-intervals-for-multivariate-gaussian"}

Assume <span class="math inline">\$X \\sim N\_d(\\theta, \\Sigma)\$</span>, <span class="math inline">\$\\Sigma\$</span> known, <span class="math inline">\$\\Sigma\_{ii} = 1\$</span>

Let <span class="math inline">\$t\_\\alpha\$</span> be upper <span class="math inline">\$\\alpha\$</span> quantile of <span class="math inline">\$\\\|X - \\theta\\\|\_\\Sigma = \\sqrt{(X-\\theta)^T \\Sigma^{-1}(X-\\theta)}\$</span>

<span class="math inline">\$C\_i(X) = $$\\theta\_i: \|X\_i - \\theta\_i\| \\leq t\_\\alpha \\sqrt{\\Sigma\_{ii}}$$\$</span> for all <span class="math inline">\$i\$</span>

<span class="math inline">\$\\mathbb{P}(C(X) \\ni \\theta\_i \\text{ for any } i) = \\mathbb{P}(\\\|X - \\theta\\\|\_\\Sigma \\leq t\_\\alpha) = 1-\\alpha\$</span>

<span class="math inline">\$t\_\\alpha = \\sqrt{\\chi^2\_{d,1-\\alpha}}\$</span> if <span class="math inline">\$\\Sigma = I\_d\$</span>

Note: we could have instead constructed an elliptical conf. region, but then the intervals would be conservative:

<span class="math inline">\$\\mathbb{P}(\\\|X - \\theta\\\|\_\\Sigma^2 \\leq \\chi^2\_{d,1-\\alpha}) = 1-\\alpha\$</span>

### <span class="header-section-number">5.2</span> Example: Linear Regression (n obs, d variables) {.anchored number="5.2" anchor-id="example-linear-regression-n-obs-d-variables"}

<span class="math inline">\$X \\in \\mathbb{R}^{n \\times d}\$</span> design, <span class="math inline">\$\\beta \\in \\mathbb{R}^d\$</span>, <span class="math inline">\$Y \\sim N(X\\beta, \\sigma^2 I\_n)\$</span>

Estimate <span class="math inline">\$\\hat{\\beta} = (X^T X)^{-1} X^T Y\$</span>

where <span class="math inline">\$\\hat{\\beta} \\sim N(\\beta, \\sigma^2 (X^T X)^{-1})\$</span>

<span class="math inline">\$S^2 = \\\|Y - X\\hat{\\beta}\\\|^2/(n-d)\$</span>, <span class="math inline">\$V = RS^2\$</span>, <span class="math inline">\$R = (X^T X)^{-1}\$</span>

Distr. of <span class="math inline">\$\\hat{\\beta}\_j/\\sqrt{V\_{jj}}\$</span> fully known

Assume w.l.o.g. <span class="math inline">\$X^T X = I\_d\$</span>

Let <span class="math inline">\$t\_\\alpha\$</span> denote upper <span class="math inline">\$\\alpha\$</span> quantile of <span class="math inline">\$\\\|\\hat{\\beta} - \\beta\\\|/\\sqrt{S^2}\$</span>

Then <span class="math inline">\$C\_j = \\hat{\\beta}\_j \\pm t\_\\alpha \\sqrt{V\_{jj}}\$</span> are simultaneous CIs for <span class="math inline">\$\\beta\_j\$</span>, <span class="math inline">\$j = 1,\\ldots,d\$</span> (compute <span class="math inline">\$t\_\\alpha\$</span> by simulation)

<span class="math inline">\$\\mathbb{P}(\|\\hat{\\beta}\_j - \\beta\_j\| \\leq t\_\\alpha \\sqrt{V\_{jj}} \\text{ for all } j) = 1-\\alpha\$</span>

---

[← 4 Testing with Dependence](05-4-testing-with-dependence.md) · [Up: contents](index.md) · [6 False Discovery Rate (FDR) →](07-6-false-discovery-rate-fdr.md)
