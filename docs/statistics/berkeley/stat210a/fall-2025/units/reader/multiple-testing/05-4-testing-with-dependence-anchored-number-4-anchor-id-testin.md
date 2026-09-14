---
title: 4 Testing with Dependence {.anchored number="4" anchor-id="testing-with-dependence"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Testing with Dependence {.anchored number="4" anchor-id="testing-with-dependence"}

**Source:** [`units/reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Bonferroni isn’t much worse than Šidák e.g., <span class="math inline">\$\\alpha = 0.05\$</span>, <span class="math inline">\$m = 20\$</span>: <span class="math inline">\$0.0025\$</span> vs <span class="math inline">\$0.00256\$</span>

But when tests are highly dependent, can often do much better

### <span class="header-section-number">4.1</span> Example: Scheffé’s S-method {.anchored number="4.1" anchor-id="example-scheffés-s-method"}

<span class="math inline">\$X \\sim N(\\theta, I\_d)\$</span>, <span class="math inline">\$\\theta \\in \\mathbb{R}^d\$</span> <span class="math inline">\$H\_0: a\_j^T \\theta = 0\$</span> for <span class="math inline">\$j = 1,\\ldots,m\$</span>, <span class="math inline">\$\\\|a\_j\\\| = 1\$</span>

Reject <span class="math inline">\$H\_{0j}\$</span> if <span class="math inline">\$\|a\_j^T X\| &gt; \\sqrt{d F\_{d,\\infty,1-\\alpha}}\$</span>

Controls FWER:

<span class="math inline">\$\\mathbb{P}(\\\|X - \\theta\\\|^2 \\leq dF\_{d,\\infty,1-\\alpha}) = 1-\\alpha\$</span>

Can view as deduction from confidence region: <span class="math inline">\$C(X) = \\{\\theta: \\\|X - \\theta\\\|^2 \\leq dF\_{d,\\infty,1-\\alpha}\\}\$</span>

---

[← 3 Bonferroni Correction {.anchored number="3" anchor-id="bonferroni-correction"}](04-3-bonferroni-correction-anchored-number-3-anchor-id-bonferro.md) · [Up: contents](index.md) · [5 Deduced Inference {.anchored number="5" anchor-id="deduced-inference"} →](06-5-deduced-inference-anchored-number-5-anchor-id-deduced-infe.md)
