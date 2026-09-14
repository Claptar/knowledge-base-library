---
title: 2 Family-wise Error Rate (FWER)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Family-wise Error Rate (FWER)

**Source:** [`reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Problem: Even if all <span class="math inline">\$H\_{0i}\$</span> true, might have:

<span class="math inline">\$\\mathbb{P}(\\text{any } H\_{0i} \\text{ rejected}) \\leq 1 - (1-\\alpha)^m \\approx m\\alpha\$</span>

Example: <span class="math inline">\$X\_i \\sim N(\\theta\_i, 1)\$</span> iid, <span class="math inline">\$i = 1,\\ldots,m\$</span>, <span class="math inline">\$H\_{0i}: \\theta\_i = 0\$</span>

<span class="math inline">\$\\mathbb{P}\_0(\\text{any } H\_{0i} \\text{ rejected}) = 1 - (1-\\alpha)^m \\approx m\\alpha\$</span>

Is this a problem? Yes, if all attention will be focused on the false rejections and none on the correct non-rejections.

Classical solution is to control the family-wise error rate (FWER):

FWER = <span class="math inline">\$\\mathbb{P}\_\\theta(\\text{any false rejections}) = \\mathbb{P}\_\\theta(R \\cap H\_{0c} \\neq \\emptyset)\$</span>

Want: <span class="math inline">\$\\sup\_\\theta \\text{FWER}(\\theta) \\leq \\alpha\$</span>

Typically achieved by correcting marginal p-values: <span class="math inline">\$p\_1(X), \\ldots, p\_m(X)\$</span>, <span class="math inline">\$p\_i \\sim U(0,1)\$</span>

e.g., <span class="math inline">\$\\phi\_i = 1\\{\\alpha/(2m)\|X\_i\| &gt; \\Phi^{-1}(1-\\alpha/(2m))\\}\$</span> for Gaussian

---

[← 1 Multiple Testing](02-1-multiple-testing.md) · [Up: contents](index.md) · [3 Bonferroni Correction →](04-3-bonferroni-correction.md)
