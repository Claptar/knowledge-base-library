---
title: 3 Examples {.anchored number="3" anchor-id="examples"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Examples {.anchored number="3" anchor-id="examples"}

**Source:** [`units/reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">3.1</span> Beta-Binomial {.anchored number="3.1" anchor-id="beta-binomial"}

- <span class="math inline">\$X\|\\theta \\sim \\text{Binomial}(n, \\theta)\$</span>, <span class="math inline">\$\\theta \\in $$0,1$$\$</span>
- <span class="math inline">\$\\theta \\sim \\text{Beta}(\\alpha, \\beta)\$</span>, <span class="math inline">\$\\alpha, \\beta &gt; 0\$</span>

The marginal distribution of <span class="math inline">\$X\$</span> is called Beta-Binomial.

Posterior: <span class="math display">\\$$ \\pi(\\theta\|x) \\propto \\theta^x (1-\\theta)^{n-x} \\cdot \\theta^{\\alpha-1}(1-\\theta)^{\\beta-1} \\propto \\theta^{x+\\alpha-1}(1-\\theta)^{n-x+\\beta-1} \\$$</span>

Therefore, <span class="math inline">\$\\theta\|X \\sim \\text{Beta}(x+\\alpha, n-x+\\beta)\$</span>

<span class="math display">\\$$ \\EE\[\\theta\|X$$ = \\frac{x+\\alpha}{n+\\alpha+\\beta} \\\]</span>

Interpret <span class="math inline">\$\\alpha+\\beta\$</span> as pseudo-trials and <span class="math inline">\$\\alpha\$</span> as pseudo-successes.

### <span class="header-section-number">3.2</span> Normal Mean {.anchored number="3.2" anchor-id="normal-mean"}

- <span class="math inline">\$X\_i\|\\theta \\sim N(\\theta, \\sigma^2)\$</span>, <span class="math inline">\$\\sigma^2\$</span> known
- <span class="math inline">\$\\theta \\sim N(\\mu, \\tau^2)\$</span>

Posterior: <span class="math display">\\$$ \\pi(\\theta\|x) \\propto \\exp\\left(-\\frac{1}{2\\sigma^2}\\sum\_{i=1}^n(x\_i-\\theta)^2\\right) \\exp\\left(-\\frac{1}{2\\tau^2}(\\theta-\\mu)^2\\right) \\$$</span>

Complete the square:

<span class="math display">\\$$ \\theta\|X \\sim N\\left(\\frac{\\frac{n}{\\sigma^2}\\bar{x} + \\frac{1}{\\tau^2}\\mu}{\\frac{n}{\\sigma^2} + \\frac{1}{\\tau^2}}, \\frac{1}{\\frac{n}{\\sigma^2} + \\frac{1}{\\tau^2}}\\right) \\$$</span>

<span class="math display">\\$$ \\EE\[\\theta\|X$$ = \\frac{\\frac{n}{\\sigma^2}\\bar{x} + \\frac{1}{\\tau^2}\\mu}{\\frac{n}{\\sigma^2} + \\frac{1}{\\tau^2}} = w\\bar{x} + (1-w)\\mu \\\]</span>

where <span class="math inline">\$w = \\frac{n\\tau^2}{n\\tau^2 + \\sigma^2}\$</span>

If <span class="math inline">\$\\frac{1}{\\tau^2} = k\$</span>, interpret as <span class="math inline">\$k\$</span> pseudo-observations with mean <span class="math inline">\$\\mu\$</span>.

---

[← 2 Special Cases and Examples {.anchored number="2" anchor-id="special-cases-and-examples"}](03-2-special-cases-and-examples-anchored-number-2-anchor-id-spe.md) · [Up: contents](index.md) · [4 Conjugate Priors {.anchored number="4" anchor-id="conjugate-priors"} →](05-4-conjugate-priors-anchored-number-4-anchor-id-conjugate-pri.md)
