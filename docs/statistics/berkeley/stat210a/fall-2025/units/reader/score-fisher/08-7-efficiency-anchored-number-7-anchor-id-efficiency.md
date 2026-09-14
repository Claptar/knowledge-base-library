---
title: 7 Efficiency {.anchored number="7" anchor-id="efficiency"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 7 Efficiency {.anchored number="7" anchor-id="efficiency"}

**Source:** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

The CRLB is not necessarily attainable.

We define the efficiency of an unbiased estimator as:

<span class="math display">\\$$\\text{eff}\_\\delta(\\theta) = \\frac{\\text{CRLB}(\\theta)}{\\Var\_\\theta(\\delta)} \\leq 1,\\$$</span>

We say <span class="math inline">\$\\delta(X)\$</span> is *efficient* if <span class="math inline">\$\\text{eff}\_\\delta(\\theta) = 1\$</span> for all <span class="math inline">\$\\theta\$</span>.

For <span class="math inline">\$g(\\theta)=\\theta\\in \\RR\$</span>, the efficiency depends on how correlated <span class="math inline">\$\\delta(X)\$</span> is with the score: <span class="math display">\\$$\\begin{aligned}\\text{eff}\_\\delta(\\theta) &= \\frac{\\Cov\_\\theta(\\delta(X), \\dot{\\ell}(\\theta;X))^2}{\\Var\_\\theta(\\delta(X)) \\cdot \\Var\_\\theta(\\dot{\\ell}(\\theta;X))}\\\\ &= \\Corr\_\\theta(\\delta,\\dot{\\ell}(\\theta))^2 \\end{aligned}\\$$</span>

Thus, an efficient estimator for <span class="math inline">\$\\theta\$</span> is one that is perfectly correlated with the score. This is rarely achieved in finite samples, but we can often approach it asymptotically as <span class="math inline">\$n \\to \\infty\$</span>.

---

[← 6 Examples {.anchored number="6" anchor-id="examples"}](07-6-examples-anchored-number-6-anchor-id-examples.md) · [Up: contents](index.md)
