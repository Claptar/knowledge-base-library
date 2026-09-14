---
title: 3 General Linear Model {.anchored number="3" anchor-id="general-linear-model"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-linear.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-linear.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 General Linear Model {.anchored number="3" anchor-id="general-linear-model"}

**Source:** [`reader/testing-linear.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-linear.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Many problems can be put into canonical linear model after change of basis.

### <span class="header-section-number">3.1</span> Basic Setup {.anchored number="3.1" anchor-id="basic-setup"}

Observe <span class="math inline">\$Y \\sim N(X\\beta, \\sigma^2 I\_n)\$</span>, <span class="math inline">\$\\sigma^2\$</span> known or unknown Test <span class="math inline">\$\\beta \\in \\Theta\_0\$</span> vs <span class="math inline">\$\\beta \\in \\Theta\_1\$</span> where <span class="math inline">\$\\Theta\_0 \\subset \\Theta\_1\$</span> are subspaces of <span class="math inline">\$\\mathbb{R}^p\$</span> <span class="math inline">\$\\text{dim}(\\Theta\_0) = d\_0\$</span>, <span class="math inline">\$\\text{dim}(\\Theta\_1) = d = d\_0 + d\_1\$</span>

Idea: rotate into canonical form

<span class="math inline">\$d\_0\$</span>, <span class="math inline">\$d\_1\$</span>, <span class="math inline">\$n-d\$</span> <span class="math inline">\$\\Theta\_0\$</span>, <span class="math inline">\$\\Theta\_1 \\setminus \\Theta\_0\$</span>, <span class="math inline">\$\\mathbb{R}^n \\setminus \\Theta\_1\$</span>

<span class="math inline">\$Q = (Q\_0 \| Q\_1 \| Q\_2)\$</span> orthonormal basis for <span class="math inline">\$(\\Theta\_0 \| \\Theta\_1 \\setminus \\Theta\_0 \| \\mathbb{R}^n \\setminus \\Theta\_1)\$</span>

<span class="math inline">\$Z = Q'Y \\sim N\_n(Q'\\beta, \\sigma^2 I\_n)\$</span>

<span class="math inline">\$H\_0: Q\_1'\\beta = 0\$</span>

Do <span class="math inline">\$Z\$</span> <span class="math inline">\$\\chi^2\$</span> or <span class="math inline">\$F\$</span> test as appropriate

### <span class="header-section-number">3.2</span> Example 1: Linear Regression {.anchored number="3.2" anchor-id="example-1-linear-regression"}

<span class="math inline">\$Y\_i = X\_i'\\beta + \\epsilon\_i\$</span>, <span class="math inline">\$\\epsilon\_i \\sim N(0, \\sigma^2)\$</span> <span class="math inline">\$Y \\sim N\_n(X\\beta, \\sigma^2 I\_n)\$</span>, <span class="math inline">\$X \\in \\mathbb{R}^{n \\times p}\$</span>

Assume <span class="math inline">\$X\$</span> has full column rank <span class="math inline">\$\\Theta = X\\beta \\in \\Theta = \\text{Span}(X\_1, \\ldots, X\_p)\$</span>

<span class="math inline">\$H\_0: \\beta = (\\beta\_0', 0')' \\in \\Theta\_0 = \\text{Span}(X\_1, \\ldots, X\_q)\$</span> or <span class="math inline">\$\\beta\_q = 0\$</span> if <span class="math inline">\$d\_1 = 1\$</span>

<span class="math inline">\$\\\|\\hat{\\beta} - \\beta\\\|^2 = \\\|Y - \\text{Proj}\_\\Theta Y\\\|^2\$</span> <span class="math inline">\$\\hat{\\beta} = \\arg\\min\_\\beta \\\|Y - X\\beta\\\|^2 = (X'X)^{-1}X'Y\$</span>

<span class="math inline">\$\\hat{Y} = X\\hat{\\beta}\$</span>

Residual sum of squares (RSS): <span class="math inline">\$\\\|Y - \\hat{Y}\\\|^2 = \\\|Y - X\\hat{\\beta}\\\|^2\$</span> <span class="math inline">\$\\text{RSS}\_0 - \\text{RSS}\_1\$</span>

F-statistic is:

<span class="math display">\\$$F = \\frac{(\\text{RSS}\_0 - \\text{RSS}\_1)/d\_1}{\\text{RSS}\_1/(n-d)} \\sim F\_{d\_1,n-d}\\$$</span>

<span class="math inline">\$n-d\$</span> called residual degrees of freedom

Let <span class="math inline">\$X = (X\_0 \| X\_1)\$</span>, <span class="math inline">\$X \\in \\mathbb{R}^{n \\times p}\$</span> Let <span class="math inline">\$X\_1^\\perp = X\_1 - \\text{Proj}\_{X\_0} X\_1\$</span> <span class="math inline">\$X = (X\_0 \| X\_0^\\perp)\$</span>

Reparametrize: <span class="math inline">\$X\_1^\\perp \\beta\_1 = X\_1 \\beta\_1 - X\_0 \\beta\_0\$</span> <span class="math inline">\$\\Theta = X\\beta = X\_0 \\beta\_0 + X\_1^\\perp \\beta\_1\$</span>

<span class="math inline">\$\\hat{\\beta}\_1 = (X\_1^{\\perp'} X\_1^\\perp)^{-1} X\_1^{\\perp'} Y\$</span> <span class="math inline">\$\\\|\\hat{\\beta}\_1\\\|^2 = \\text{RSS}\_0 - \\text{RSS}\_1\$</span> <span class="math inline">\$\\text{SE}(\\hat{\\beta}\_1) = \\hat{\\sigma}^2 (X\_1^{\\perp'} X\_1^\\perp)^{-1}\$</span>

t-statistic: <span class="math inline">\$t = \\frac{\\hat{\\beta}\_1}{\\text{SE}(\\hat{\\beta}\_1)} \\sim t\_{n-d}\$</span>

### <span class="header-section-number">3.3</span> Example 2: Two-sample t-test (equal variance) {.anchored number="3.3" anchor-id="example-2-two-sample-t-test-equal-variance"}

<span class="math inline">\$Y\_1, \\ldots, Y\_n \\sim N(\\mu\_1, \\sigma^2)\$</span>, <span class="math inline">\$Y\_{n+1}, \\ldots, Y\_{n+m} \\sim N(\\mu\_2, \\sigma^2)\$</span>

<span class="math inline">\$Y = (Y\_1, \\ldots, Y\_{n+m})'\$</span>, <span class="math inline">\$\\mathbb{E}$$Y$$ = \\mu\_1 1\_n + \\mu\_2 1\_m\$</span> Model: <span class="math inline">\$\\Theta = \\text{Span}(1\_{n+m}, (1\_n', 0\_m')')\$</span>

<span class="math inline">\$H\_0: \\mu\_1 = \\mu\_2 \\implies \\Theta\_0 = \\text{Span}(1\_{n+m})\$</span>

<span class="math inline">\$d\_0 = 1\$</span>, <span class="math inline">\$d = 2\$</span>, <span class="math inline">\$d\_1 = n+m-2\$</span>

Orthogonalize <span class="math inline">\$1\_{n+m}\$</span>

Reject for large:

<span class="math display">\\$$t = \\frac{\\bar{Y}\_1 - \\bar{Y}\_2}{\\hat{\\sigma}\\sqrt{\\frac{1}{n} + \\frac{1}{m}}} \\sim t\_{n+m-2}\\$$</span>

where <span class="math inline">\$\\hat{\\sigma}^2 = \\frac{\\sum\_{i=1}^n (Y\_i - \\bar{Y}\_1)^2 + \\sum\_{i=1}^m (Y\_i - \\bar{Y}\_2)^2}{n+m-2}\$</span>

### <span class="header-section-number">3.4</span> Example 3: One-way ANOVA (fixed effects) {.anchored number="3.4" anchor-id="example-3-one-way-anova-fixed-effects"}

<span class="math inline">\$Y\_{ki} \\sim N(\\mu\_k, \\sigma^2)\$</span>, <span class="math inline">\$k=1,\\ldots,m\$</span>, <span class="math inline">\$i=1,\\ldots,n\$</span>

<span class="math inline">\$H\_0: \\mu\_1 = \\cdots = \\mu\_m\$</span>

<span class="math inline">\$Y\_{ki} = \\mu + \\alpha\_k + \\epsilon\_{ki}\$</span>, <span class="math inline">\$\\sum \\alpha\_k = 0\$</span>

<span class="math inline">\$\\bar{Y}\_{k\\cdot} = \\frac{1}{n} \\sum\_{i=1}^n Y\_{ki}\$</span>, \${Y} = \\frac{1}{mn

---

[← 2 Canonical Linear Model {.anchored number="2" anchor-id="canonical-linear-model"}](03-2-canonical-linear-model-anchored-number-2-anchor-id-canonic.md) · [Up: contents](index.md)
