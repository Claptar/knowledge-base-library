---
title: 2 Special Cases and Examples {.anchored number="2" anchor-id="special-cases-and-examples"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Special Cases and Examples {.anchored number="2" anchor-id="special-cases-and-examples"}

**Source:** [`units/reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">2.1</span> Squared Error Loss {.anchored number="2.1" anchor-id="squared-error-loss"}

If <span class="math inline">\$L(\\theta, d) = (\\theta - d)^2\$</span>, then the Bayes estimator is the posterior mean:

<span class="math display">\\$$ \\delta\_\\pi(x) = \\EE\[\\theta\|X=x$$ \\\]</span>

Proof: <span class="math display">\\$$ \\begin{aligned} \\EE\[(\\theta - d)^2\|X=x$$ &= \\EE$$\\theta^2\|X=x$$ - 2d\\EE$$\\theta\|X=x$$ + d^2 \\\\ &= \\Var(\\theta\|X=x) + (\\EE$$\\theta\|X=x$$ - d)^2 + \\EE$$\\theta\|X=x$$^2 - 2d\\EE$$\\theta\|X=x$$ + d^2 \\end{aligned} \\\]</span>

The minimum occurs when <span class="math inline">\$d = \\EE$$\\theta\|X=x$$\$</span>.

### <span class="header-section-number">2.2</span> Weighted Squared Error {.anchored number="2.2" anchor-id="weighted-squared-error"}

For <span class="math inline">\$L(\\theta, d) = w(\\theta)(\\theta - d)^2\$</span> (e.g., squared relative error), the Bayes estimator is:

<span class="math display">\\$$ \\delta\_\\pi(x) = \\frac{\\EE\[w(\\theta)\\theta\|X=x$$}{\\EE$$w(\\theta)\|X=x$$} \\\]</span>

---

[← Bayes estimation Part 02 —](02-bayes-estimation-part-02.md) · [Up: contents](index.md) · [3 Examples {.anchored number="3" anchor-id="examples"} →](04-3-examples-anchored-number-3-anchor-id-examples.md)
