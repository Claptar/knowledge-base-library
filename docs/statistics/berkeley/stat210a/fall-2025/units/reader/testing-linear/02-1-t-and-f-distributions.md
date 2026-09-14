---
title: 1 t and F Distributions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-linear.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-linear.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 t and F Distributions

**Source:** [`units/reader/testing-linear.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-linear.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">1.1</span> Definitions and Properties {.anchored number="1.1" anchor-id="definitions-and-properties"}

1.  <span class="math inline">\$\\chi^2\_d\$</span>: If <span class="math inline">\$X\_i \\sim N(0,1)\$</span> iid, then <span class="math inline">\$V = \\sum\_{i=1}^d X\_i^2 \\sim \\chi^2\_d\$</span>

    - <span class="math inline">\$\\mathbb{E}$$V$$ = d\$</span>, <span class="math inline">\$\\text{Var}(V) = 2d\$</span>
    - CLT: <span class="math inline">\$V \\approx N(d, 2d)\$</span> for large <span class="math inline">\$d\$</span>

2.  <span class="math inline">\$t\_d\$</span>: If <span class="math inline">\$Z \\sim N(0,1)\$</span> and <span class="math inline">\$V \\sim \\chi^2\_d\$</span> independent, then <span class="math inline">\$T = \\frac{Z}{\\sqrt{V/d}} \\sim t\_d\$</span>

    - Informally: <span class="math inline">\$Y \\sim N(\\mu, 1)\$</span>, <span class="math inline">\$\\hat{\\sigma}^2 \\sim \\frac{\\chi^2\_d}{d}\$</span>, <span class="math inline">\$\\frac{Y - \\mu}{\\hat{\\sigma}} \\sim t\_d\$</span>

3.  If <span class="math inline">\$Z \\sim N(0,1)\$</span> and <span class="math inline">\$V \\sim \\chi^2\_d\$</span>, <span class="math inline">\$Z/\\sqrt{V} \\sim t\_d\$</span> as <span class="math inline">\$d \\to \\infty\$</span>

4.  If <span class="math inline">\$V \\sim \\chi^2\_d\$</span> and <span class="math inline">\$V\_2 \\sim \\chi^2\_{d\_2}\$</span> independent, <span class="math inline">\$V/V\_2 \\sim F\_{d,d\_2}\$</span>, then:

    <span class="math inline">\$\\frac{V/d}{V\_2/d\_2} \\sim F\_{d,d\_2}\$</span> as <span class="math inline">\$d,d\_2 \\to \\infty\$</span>

Note: If <span class="math inline">\$T \\sim t\_d\$</span>, then <span class="math inline">\$T^2 \\sim F\_{1,d}\$</span>

Recall: <span class="math inline">\$Z \\sim N\_d(\\mu, \\Sigma)\$</span> iff <span class="math inline">\$A Z + b \\sim N\_d(A\\mu + b, A\\Sigma A^T)\$</span>

### <span class="header-section-number">1.2</span> Geometric Interpretation {.anchored number="1.2" anchor-id="geometric-interpretation"}

Let <span class="math inline">\$X \\sim N\_n(\\mu, I\_n)\$</span>, <span class="math inline">\$\\mu = \\alpha e\_1\$</span>, where <span class="math inline">\$\\{e\_1, \\ldots, e\_n\\}\$</span> is a complete orthonormal basis (e.g., via Gram-Schmidt)

<span class="math inline">\$X = \\sum\_{i=1}^n \\langle X, e\_i \\rangle e\_i = \\alpha e\_1 + \\sum\_{i=1}^n Z\_i e\_i\$</span>, <span class="math inline">\$Z\_i \\sim N(0,1)\$</span> iid

New basis: <span class="math inline">\$Z = Q'X\$</span>, <span class="math inline">\$\\\|X\\\|^2 = \\\|Z\\\|^2\$</span>

<span class="math inline">\$\\begin{pmatrix} Z\_1 \\\\ Z\_{2:n} \\end{pmatrix} = \\begin{pmatrix} Q\_1' \\\\ Q\_{2:n}' \\end{pmatrix} X \\sim N\\left(\\begin{pmatrix} \\alpha \\\\ 0 \\end{pmatrix}, I\_n\\right)\$</span>

<span class="math inline">\$Z\_1 = Q\_1' X \\sim N(\\alpha, 1)\$</span> <span class="math inline">\$Z\_{2:n} = Q\_{2:n}' X \\sim N(0, I\_{n-1})\$</span>

<span class="math inline">\$S^2 = \\\|Z\_{2:n}\\\|^2 = \\sum\_{i=2}^n Z\_i^2\$</span> and <span class="math inline">\$Z\_1\$</span> independent (we already knew from Basu)

### <span class="header-section-number">1.3</span> Geometric Interpretation (continued) {.anchored number="1.3" anchor-id="geometric-interpretation-continued"}

Independent of total magnitude under <span class="math inline">\$H\_0\$</span>:

- <span class="math inline">\$n\\bar{X}^2 = \\alpha^2 \\sim \\text{Gamma}(\\frac{1}{2}, \\frac{2}{n})\$</span>
- <span class="math inline">\$\\sum\_{i=1}^n (X\_i - \\bar{X})^2 \\sim \\text{Gamma}(\\frac{n-1}{2}, 2)\$</span>
- <span class="math inline">\$\\\|X\\\|^2 = n\\bar{X}^2 + \\sum\_{i=1}^n (X\_i - \\bar{X})^2 \\sim \\text{Gamma}(\\frac{n}{2}, 2)\$</span>

<span class="math inline">\$\\frac{n\\bar{X}^2}{\\sum\_{i=1}^n (X\_i - \\bar{X})^2} \\sim \\text{Beta}(\\frac{1}{2}, \\frac{n-1}{2})\$</span> independent of <span class="math inline">\$\\\|X\\\|^2\$</span>

<span class="math inline">\$F\_{1,n-1}\$</span> related to <span class="math inline">\$\\text{Beta}(\\frac{1}{2}, \\frac{n-1}{2})\$</span>: If <span class="math inline">\$U \\sim \\text{Beta}(\\frac{a}{2}, \\frac{b}{2})\$</span>, then <span class="math inline">\$\\frac{b}{a} \\cdot \\frac{U}{1-U} \\sim F\_{a,b}\$</span>

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Canonical Linear Model →](03-2-canonical-linear-model.md)
