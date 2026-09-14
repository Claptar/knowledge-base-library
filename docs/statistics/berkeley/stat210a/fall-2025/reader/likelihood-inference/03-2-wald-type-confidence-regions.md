---
title: 2 Wald-Type Confidence Regions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/likelihood-inference.html
source_file: sources/berkeley-stat210a/fall-2025/reader/likelihood-inference.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Wald-Type Confidence Regions

**Source:** [`reader/likelihood-inference.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/likelihood-inference.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assume we have some estimator <span class="math inline">\$\\hat{\\theta}\_n\$</span> s.t. <span class="math inline">\$\\sqrt{n}(\\hat{\\theta}\_n - \\theta\_0) \\xrightarrow{d} N(0, J^{-1}(\\theta\_0))\$</span>. Then we can plug in:

If <span class="math inline">\$\\sqrt{n}(\\hat{\\theta}\_n - \\theta\_0) \\sim N\_d(0, J^{-1}(\\theta\_0))\$</span>, then <span class="math inline">\$nJ(\\theta\_0)(\\hat{\\theta}\_n - \\theta\_0) \\sim N\_d(0, I\_d)\$</span>

So <span class="math inline">\$n(\\hat{\\theta}\_n - \\theta\_0)^T J(\\theta\_0)(\\hat{\\theta}\_n - \\theta\_0) \\sim \\chi^2\_d\$</span> (Slutsky)

Leads to test of <span class="math inline">\$H\_0: \\theta = \\theta\_0\$</span> <span class="math inline">\$H\_1: \\theta \\neq \\theta\_0\$</span>: Reject if <span class="math inline">\$n(\\hat{\\theta}\_n - \\theta\_0)^T J(\\theta\_0)(\\hat{\\theta}\_n - \\theta\_0) &gt; \\chi^2\_{d,1-\\alpha}\$</span>

So <span class="math inline">\$\\mathbb{P}\_{\\theta\_0}(n(\\hat{\\theta}\_n - \\theta\_0)^T J(\\theta\_0)(\\hat{\\theta}\_n - \\theta\_0) \\leq \\chi^2\_{d,1-\\alpha}) = 1-\\alpha\$</span>

Note: we reject <span class="math inline">\$\\theta\_0\$</span> iff <span class="math inline">\$\\{\\theta\_n: n(\\hat{\\theta}\_n - \\theta)^T J(\\theta)(\\hat{\\theta}\_n - \\theta) \\leq \\chi^2\_{d,1-\\alpha}\\}\$</span> reject <span class="math inline">\$\\theta\_0\$</span> iff <span class="math inline">\$\\theta\_0 \\notin \\{\\theta: n(\\hat{\\theta}\_n - \\theta)^T J(\\theta)(\\hat{\\theta}\_n - \\theta) \\leq \\chi^2\_{d,1-\\alpha}\\}\$</span>

Region <span class="math inline">\$\\{\\theta: n(\\hat{\\theta}\_n - \\theta)^T J(\\theta)(\\hat{\\theta}\_n - \\theta) \\leq \\chi^2\_{d,1-\\alpha}\\}\$</span> is confidence ellipsoid

More info = smaller ellipse (shrinks like <span class="math inline">\$\\sqrt{n}\$</span>)

### <span class="header-section-number">2.1</span> Estimating <span class="math inline">\$J(\\theta)\$</span> {.anchored number="2.1" anchor-id="estimating-jtheta"}

Two options is to plug-in the MLE: 1. MLE for <span class="math inline">\$J\_n(\\theta)\$</span>: <span class="math inline">\$J\_n(\\hat{\\theta}\_n) = -\\frac{1}{n}\\nabla^2 \\ell\_n(\\hat{\\theta}\_n; X)\$</span> 2. <span class="math inline">\$\\hat{J}\_n(\\theta) = \\frac{1}{n}\\text{Var}\_\\theta$$\\nabla \\ell\_n(\\theta; X)$$ = \\frac{1}{n}\\sum\_{i=1}^n \\nabla \\ell\_\\theta(X\_i) \\nabla \\ell\_\\theta(X\_i)^T\$</span>

NB: <span class="math inline">\$\\text{Var}\_\\theta$$\\nabla \\ell\_n(\\theta; X)$$ = n\\text{Var}\_\\theta$$\\nabla \\ell\_\\theta(X)$$ = 0\$</span>

Or <span class="math inline">\$\\hat{J}\_n = \\mathbb{E}\_{\\hat{\\theta}\_n}$$-\\nabla^2 \\ell\_{\\hat{\\theta}\_n}(X)$$\$</span>

#### <span class="header-section-number">2.1.1</span> Remarks {.anchored number="2.1.1" anchor-id="remarks"}

- Both have <span class="math inline">\$\\hat{J}\_n \\xrightarrow{p} J(\\theta\_0)\$</span> in nice iid sampling setting
- Both make sense outside of iid setting
- Heuristically: plug-in measures info about <span class="math inline">\$\\theta\$</span> in typical data set, but obs info measures info about <span class="math inline">\$\\theta\$</span> in this data set

### <span class="header-section-number">2.2</span> Wald Interval for <span class="math inline">\$\\theta\_j\$</span> {.anchored number="2.2" anchor-id="wald-interval-for-theta_j"}

If <span class="math inline">\$\\sqrt{n}(\\hat{\\theta}\_n - \\theta\_0) \\sim N\_d(\\theta\_0, J\_n^{-1}(\\theta\_0))\$</span> then <span class="math inline">\$\\hat{\\theta}\_n \\sim N\_d(\\theta\_0, J\_n^{-1}(\\theta\_0)/n)\$</span>

Leads to univariate interval: <span class="math inline">\$s.e.(\\hat{\\theta}\_{n,j}) = \\sqrt{$$J\_n^{-1}(\\hat{\\theta}\_n)$$\_{jj}/n}\$</span>

<span class="math inline">\$C\_j = $$\\hat{\\theta}\_{n,j} \\pm z\_{1-\\alpha/2} \\cdot s.e.(\\hat{\\theta}\_{n,j})$$\$</span>

`glm` function in R uses these intervals/p-values with <span class="math inline">\$\\hat{J}\_n = J\_n(\\hat{\\theta}\_n)\$</span>

Conf ellipsoid for <span class="math inline">\$\\theta\_0\$</span>: <span class="math inline">\$\\{\\theta: n(\\hat{\\theta}\_n - \\theta)^T \\hat{J}\_n(\\hat{\\theta}\_n)(\\hat{\\theta}\_n - \\theta) \\leq \\chi^2\_{d,1-\\alpha}\\}\$</span>

More generally, if <span class="math inline">\$\\sqrt{n}(\\hat{\\theta}\_n - \\theta\_0) \\xrightarrow{d} N(0, \\Sigma(\\theta\_0))\$</span> and <span class="math inline">\$\\hat{\\Sigma}\_n(\\theta) \\xrightarrow{p} \\Sigma(\\theta\_0)\$</span> (not nec. MLE) then we can do the same things

### <span class="header-section-number">2.3</span> Example: Generalized Linear Model with Fixed Design {.anchored number="2.3" anchor-id="example-generalized-linear-model-with-fixed-design"}

<span class="math inline">\$X\_1, \\ldots, X\_n \\in \\mathbb{R}^d\$</span> fixed <span class="math inline">\$Y\_1, \\ldots, Y\_n \\sim p\_{\\eta\_i}(y)\$</span> indep, <span class="math inline">\$Y\_i \| X\_i \\sim p\_{\\eta\_i}(y)\$</span> <span class="math inline">\$\\eta\_i = \\beta^T X\_i\$</span> (canonical form)

Let <span class="math inline">\$\\mu\_i(\\beta) = \\mathbb{E}\_\\beta$$Y\_i$$ = \\psi'(\\eta\_i)\$</span>

More general: <span class="math inline">\$\\eta\_i = f(\\beta^T X\_i)\$</span> for <span class="math inline">\$f\$</span> monotone

Most common examples include: - Logistic regression: <span class="math inline">\$Y\_i \\sim \\text{Bern}(e^{\\eta\_i}/(1+e^{\\eta\_i}))\$</span> - Poisson log-linear model: <span class="math inline">\$Y\_i \\sim \\text{Pois}(e^{\\eta\_i})\$</span>

<span class="math inline">\$\\ell\_n(\\beta; Y) = \\sum\_{i=1}^n $$Y\_i \\eta\_i - \\psi(\\eta\_i) + \\log h(Y\_i)$$\$</span>

<span class="math inline">\$\\nabla \\ell\_n(\\beta; Y) = \\sum\_{i=1}^n (Y\_i - \\mu\_i(\\beta)) X\_i\$</span>

<span class="math inline">\$\\mathbb{E}\_\\beta$$Y\_i$$ = \\mu\_i(\\beta) = \\psi'(\\eta\_i)\$</span>

<span class="math inline">\$\\nabla^2 \\ell\_n(\\beta; Y) = -\\sum\_{i=1}^n \\psi''(\\eta\_i) X\_i X\_i^T\$</span>

<span class="math inline">\$\\text{Var}\_\\beta(Y\_i) = \\psi''(\\eta\_i)\$</span> (not random)

<span class="math inline">\$\\hat{\\beta} \\stackrel{\\cdot}{\\sim} N(\\beta, J\_n^{-1}(\\beta))\$</span> in finite samples <span class="math inline">\$\\xrightarrow{d} N(0, J^{-1})\$</span>

Under regularity cond. on <span class="math inline">\$X\$</span>: Taylor expansion of <span class="math inline">\$\\ell\_n\$</span> leads to <span class="math inline">\$\\sqrt{n}(\\hat{\\beta}\_n - \\beta) \\xrightarrow{d} N(0, J^{-1})\$</span>

#### <span class="header-section-number">2.3.1</span> Advantages of Wald Test {.anchored number="2.3.1" anchor-id="advantages-of-wald-test"}

1.  Easy to invert, simple conf regions
2.  Asymptotically correct

#### <span class="header-section-number">2.3.2</span> Disadvantages {.anchored number="2.3.2" anchor-id="disadvantages"}

1.  Have to compute MLE
2.  Depends on parameterization
3.  Relies on two approximations: <span class="math inline">\$\\ell\_n\$</span> Normal and <span class="math inline">\$\\ell\_n\$</span> quadratic
4.  Need MLE to be consistent
5.  Confidence interval/ellipsoid might go outside <span class="math inline">\$\\Theta\$</span>

---

[← 1 Likelihood-Based Inference](02-1-likelihood-based-inference.md) · [Up: contents](index.md) · [3 Score Test →](04-3-score-test.md)
