---
title: 3 Gaussian Hierarchical Model
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Gaussian Hierarchical Model

**Source:** [`units/reader/bayes-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

<span class="math inline">\$\\theta\_i \\sim N(\\mu, \\tau^2)\$</span>, <span class="math inline">\$X\_i\|\\theta\_i \\sim N(\\theta\_i, \\sigma^2)\$</span>

Posterior mean: <span class="math display">\\$$ \\mathbb{E}\[\\theta\_i\|X$$ = \\mathbb{E}$$\\mathbb{E}\[\\theta\_i\|X, \\mu, \\tau^2$$\|X\] = \\mathbb{E}$$\\frac{\\tau^2}{\\tau^2 + \\sigma^2}X\_i + \\frac{\\sigma^2}{\\tau^2 + \\sigma^2}\\mu\|X$$ \\\]</span>

Linear shrinkage estimator: - Bayes optimal shrinkage estimated from data - Likelihood for <span class="math inline">\$\\mu, \\tau^2\$</span> (marginalize over <span class="math inline">\$\\theta\_i\$</span>): - <span class="math inline">\$X\_i\|\\mu, \\tau^2 \\sim N(\\mu, \\tau^2 + \\sigma^2)\$</span> - <span class="math inline">\$\\bar{X} \\sim N(\\mu, \\frac{\\tau^2 + \\sigma^2}{n})\$</span> - <span class="math inline">\$S^2 = \\frac{1}{n-1}\\sum\_{i=1}^n (X\_i - \\bar{X})^2 \\sim \\frac{\\tau^2 + \\sigma^2}{n-1}\\chi^2\_{n-1}\$</span>

Define <span class="math inline">\$B = \\tau^2 + \\sigma^2\$</span>: <span class="math display">\\$$ \\delta(x) = \\mathbb{E}\[\\mathbb{E}\[\\theta\_i\|X, B$$\|X\] = \\mathbb{E}$$\\frac{B - \\sigma^2}{B}X\_i + \\frac{\\sigma^2}{B}\\bar{X}\|X$$ \\\]</span>

Conjugate prior: <span class="math display">\\$$ \\pi(B\|\\lambda, \\nu) \\propto B^{-\\nu/2-2}\\exp(-\\frac{\\lambda}{2B}) \\$$</span>

<span class="math display">\\$$ B\|X \\sim \\text{InvGamma}(\\frac{n+\\nu}{2}, \\frac{\\lambda + (n-1)S^2}{2}) \\$$</span>

<span class="math display">\\$$ \\mathbb{E}\[\\frac{1}{B}\|X$$ = \\frac{n+\\nu}{\\lambda + (n-1)S^2} \\\]</span>

<span class="math display">\\$$ \\delta\_i(x) = \\frac{(n-3)S^2}{(n-1)S^2 + \\lambda}X\_i + \\frac{\\lambda + 2S^2}{(n-1)S^2 + \\lambda}\\bar{X} \\$$</span>

Might want to truncate prior to <span class="math inline">\$\[\\sigma^2, \\infty)\$</span> if <span class="math inline">\$\\lambda\$</span> small.

---

[← 2 Where Does the Prior Come From?](03-2-where-does-the-prior-come-from.md) · [Up: contents](index.md)
