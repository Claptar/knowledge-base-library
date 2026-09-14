---
title: 3 Empirical Bayes {.anchored number="3" anchor-id="empirical-bayes"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Empirical Bayes {.anchored number="3" anchor-id="empirical-bayes"}

**Source:** [`units/reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">3.1</span> {.anchored number="3.1" anchor-id="section"}

### <span class="header-section-number">3.2</span> Common Situation in Hierarchical Bayes Models {.anchored number="3.2" anchor-id="common-situation-in-hierarchical-bayes-models"}

1.  <span class="math inline">\$\\theta \\sim G\$</span>, one draw: hard to justify prior
2.  Lots of info: prior doesn’t matter
3.  <span class="math inline">\$\\theta\_i \\sim G\$</span>, only <span class="math inline">\$X\_i\$</span> informative: prior helps
4.  Many draws: can check fit

<span class="math display">\\$$X\_i \\sim p\_{\\theta\_i}(x), \\quad i = 1,\\ldots,d\\$$</span>

### <span class="header-section-number">3.3</span> Hybrid Approach {.anchored number="3.3" anchor-id="hybrid-approach"}

Treat <span class="math inline">\$G\$</span> as fixed:

1.  Estimate <span class="math inline">\$G\$</span> based on observed data
2.  Plug in <span class="math inline">\$\\hat{G}\$</span> as though known

### <span class="header-section-number">3.4</span> Example {.anchored number="3.4" anchor-id="example"}

<span class="math inline">\$\\theta\_i \\sim N(0, \\tau^2)\$</span>, <span class="math inline">\$\\tau^2\$</span> fixed unknown <span class="math inline">\$X\_i\|\\theta\_i \\sim N(\\theta\_i, 1)\$</span>, <span class="math inline">\$i = 1,\\ldots,d\$</span>

Bayes estimator if we knew <span class="math inline">\$\\tau^2\$</span> is:

<span class="math display">\\$$\\delta(X) = \\frac{\\tau^2}{\\tau^2 + 1}X\_i\\$$</span>

<span class="math inline">\$\\tau^2\$</span> is sufficient.

To estimate <span class="math inline">\$\\tau^2\$</span>, use <span class="math inline">\$X \\sim N(0, \\tau^2 I\_d + I\_d)\$</span>:

<span class="math display">\\$$\\mathbb{E}\\\|X\\\|^2 = d(\\tau^2 + 1)\\$$</span>

<span class="math display">\\$$\\hat{\\tau}^2 = \\max\\{\\frac{1}{d}\\\|X\\\|^2 - 1, 0\\}\\$$</span>

Plug in: <span class="math inline">\$\\hat{\\delta}(X) = (1 - \\frac{d}{\\\|X\\\|^2})\_+ X\_i\$</span>

If <span class="math inline">\$d\$</span> large, should be near optimal.

---

[← Empirical bayes Part 03 —](03-empirical-bayes-part-03.md) · [Up: contents](index.md) · [4 James-Stein Estimator {.anchored number="4" anchor-id="james-stein-estimator"} →](05-4-james-stein-estimator-anchored-number-4-anchor-id-james-st.md)
