---
title: 4 Empirical Bayes
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Empirical Bayes

**Source:** [`units/reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Back to Gaussian hierarchical model:

<span class="math display">\\$$ \\begin{aligned} \\theta\_i &\\sim N(\\mu, \\tau^2) \\\\ X\_i \| \\theta\_i &\\sim N(\\theta\_i, \\sigma^2) \\end{aligned} \\$$</span>

<span class="math display">\\$$ \\mathbb{E}\[\\theta\_i \| X, B$$ = \\frac{B - \\sigma^2}{B}X\_i + \\frac{\\sigma^2}{B}\\bar{X}, \\quad B = \\tau^2 + \\sigma^2 \\\]</span>

For any reasonable prior: <span class="math inline">\$B \| X \\approx \\frac{1}{N}\\sum\_{i=1}^N (X\_i - \\bar{X})^2\$</span>

If prior doesn’t matter much, why use one? Could just estimate <span class="math inline">\$B\$</span> from data, however we want.

A minimax estimator is <span class="math inline">\$B = \\sigma^2 + \\frac{1}{N}\\sum\_{i=1}^N (X\_i - \\bar{X})^2\$</span>

Called Empirical Bayes: a hybrid approach in which hyperparameters are treated as fixed, others treated as random.

---

[← 3 Gibbs Sampler](04-3-gibbs-sampler.md) · [Up: contents](index.md)
