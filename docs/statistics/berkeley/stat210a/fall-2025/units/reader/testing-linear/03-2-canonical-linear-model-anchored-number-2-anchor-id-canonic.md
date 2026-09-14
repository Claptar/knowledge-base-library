---
title: 2 Canonical Linear Model {.anchored number="2" anchor-id="canonical-linear-model"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-linear.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-linear.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Canonical Linear Model {.anchored number="2" anchor-id="canonical-linear-model"}

**Source:** [`units/reader/testing-linear.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-linear.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assume <span class="math inline">\$Z = \\begin{pmatrix} Z\_1 \\\\ Z\_2 \\end{pmatrix} \\sim N\\left(\\begin{pmatrix} \\mu \\\\ 0 \\end{pmatrix}, \\sigma^2 I\_d\\right)\$</span>, <span class="math inline">\$d = d\_0 + d\_1\$</span>, <span class="math inline">\$\\mu \\in \\mathbb{R}^{d\_0}\$</span>, <span class="math inline">\$\\sigma^2 &gt; 0\$</span>

Test <span class="math inline">\$H\_0: \\mu = 0\$</span> vs <span class="math inline">\$H\_1: \\mu \\neq 0\$</span> (or possibly one-sided if <span class="math inline">\$d\_0 = 1\$</span>)

Exponential Family:

<span class="math display">\\$$f(z) = f(z\_0, z\_1) = \\frac{1}{(2\\pi\\sigma^2)^{d/2}} \\exp\\left(-\\frac{\\\|z\_1\\\|^2 + \\\|z\_0 - \\mu\\\|^2}{2\\sigma^2}\\right)\\$$</span>

### <span class="header-section-number">2.1</span> Case 1: <span class="math inline">\$\\sigma^2\$</span> Known {.anchored number="2.1" anchor-id="case-1-sigma2-known"}

Condition on <span class="math inline">\$Z\_1\$</span>, reject for large/small/extreme <span class="math inline">\$Z\_0\$</span>

<span class="math inline">\$Z\_0 \\sim N(\\mu, \\sigma^2 I\_{d\_0})\$</span>

<span class="math inline">\$\\chi^2\$</span> test: Reject for large <span class="math inline">\$\\\|Z\_0\\\|^2\$</span>

t-test: If <span class="math inline">\$d\_0 = 1\$</span>, reject for large <span class="math inline">\$\|Z\_0\|\$</span>

### <span class="header-section-number">2.2</span> Case 2: <span class="math inline">\$\\sigma^2\$</span> Unknown {.anchored number="2.2" anchor-id="case-2-sigma2-unknown"}

Condition on <span class="math inline">\$Z\_1\$</span>, <span class="math inline">\$\\\|Z\_1\\\|^2\$</span>, <span class="math inline">\$\\\|Z\_0\\\|^2\$</span> sufficient

Reject for large/small/extreme <span class="math inline">\$Z\_0\$</span>

Reject for large <span class="math inline">\$\\frac{\\\|Z\_0\\\|^2/d\_0}{\\\|Z\_1\\\|^2/d\_1} \\sim F\_{d\_0,d\_1}\$</span> under <span class="math inline">\$H\_0\$</span>

F-test: <span class="math inline">\$d\_0 &gt; 1\$</span>, Reject for conditionally large <span class="math inline">\$\\\|Z\_0\\\|^2\$</span>

Reject for large <span class="math inline">\$\\frac{\\\|Z\_0\\\|^2/d\_0}{\\\|Z\_1\\\|^2/d\_1} \\sim F\_{d\_0,d\_1}\$</span>

t-test: <span class="math inline">\$d\_0 = 1\$</span>, Reject for conditionally large <span class="math inline">\$\|Z\_0\|\$</span>

Reject for large <span class="math inline">\$\\frac{\|Z\_0\|}{\\sqrt{\\\|Z\_1\\\|^2/d\_1}} \\sim t\_{d\_1}\$</span>

Here, <span class="math inline">\$\\frac{\\\|Z\_1\\\|^2}{d\_1}\$</span> functioning as estimator of <span class="math inline">\$\\sigma^2\$</span>: <span class="math inline">\$\\mathbb{E}$$\\frac{\\\|Z\_1\\\|^2}{d\_1}$$ = \\sigma^2\$</span>, <span class="math inline">\$\\text{Var}(\\frac{\\\|Z\_1\\\|^2}{d\_1}) = \\frac{2\\sigma^4}{d\_1}\$</span>

General case: <span class="math inline">\$Z \\sim N(\\mu, \\sigma^2 I\_d)\$</span>, <span class="math inline">\$\\mu \\not\\in \\mathbb{R}^{d\_0} \\times \\{0\\}^{d\_1}\$</span>

Translate problem:

<span class="math inline">\$Z\_0 \\sim N\_{d\_0}(\\mu\_0, \\sigma^2 I\_{d\_0})\$</span> <span class="math inline">\$Z\_1 \\sim N\_{d\_1}(\\mu\_1, \\sigma^2 I\_{d\_1})\$</span>

Can do some tests with <span class="math inline">\$Z - \\mu\_1\$</span> replacing <span class="math inline">\$Z\$</span>

Invert: <span class="math inline">\$1-\\alpha\$</span> CI: <span class="math inline">\$\\mu\_0 \\in Z\_0 \\pm \\sigma t\_{d\_1,1-\\alpha/2} \\sqrt{\\frac{\\\|Z\_1 - \\mu\_1\\\|^2}{d\_1}}\$</span>

<span class="math inline">\$1-\\alpha\$</span> confidence ellipsoid: <span class="math inline">\$\\\|\\mu\_0 - Z\_0\\\|^2 \\leq \\frac{d\_0}{d\_1} \\\|Z\_1 - \\mu\_1\\\|^2 F\_{d\_0,d\_1,1-\\alpha}\$</span>

<span class="math inline">\$1-\\alpha\$</span> prediction interval: <span class="math inline">\$Z\_{\\text{new}} \\in Z\_0 \\pm \\sigma t\_{d\_1,1-\\alpha/2} \\sqrt{1 + \\frac{\\\|Z\_1 - \\mu\_1\\\|^2}{d\_1}}\$</span>

---

[← 1 t and F Distributions {.anchored number="1" anchor-id="t-and-f-distributions"}](02-1-t-and-f-distributions-anchored-number-1-anchor-id-t-and-f.md) · [Up: contents](index.md) · [3 General Linear Model {.anchored number="3" anchor-id="general-linear-model"} →](04-3-general-linear-model-anchored-number-3-anchor-id-general-l.md)
