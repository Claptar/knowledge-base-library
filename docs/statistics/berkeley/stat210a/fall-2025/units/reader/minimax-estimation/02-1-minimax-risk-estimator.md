---
title: 1 Minimax Risk Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Minimax Risk Estimator

**Source:** [`units/reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">1.1</span> Definition of Minimax Risk {.anchored number="1.1" anchor-id="definition-of-minimax-risk"}

The last idea for choosing an estimator: worst-case risk.

Minimize <span class="math inline">\$\\sup\_\\theta R(\\theta, \\delta)\$</span>

The minimum achievable sup risk is called the minimax risk of the estimation problem:

<span class="math display">\\$$r = \\inf\_\\delta \\sup\_\\theta R(\\theta, \\delta)\\$$</span>

An estimator <span class="math inline">\$\\delta\$</span> is called minimax if it achieves the minimax risk, i.e.,

<span class="math display">\\$$\\sup\_\\theta R(\\theta, \\delta) = r\\$$</span>

### <span class="header-section-number">1.2</span> Game Theory Interpretation {.anchored number="1.2" anchor-id="game-theory-interpretation"}

1.  Analyst chooses estimator <span class="math inline">\$\\delta\$</span>
2.  Nature chooses parameter <span class="math inline">\$\\theta\$</span> to maximize risk

Note: Nature chooses <span class="math inline">\$\\theta\$</span> adversarially, not <span class="math inline">\$X\$</span>.

Compare to Bayes where Nature chooses prior from a known distribution (Nature plays a specific mixed strategy).

We will look for Nature’s Nash equilibrium strategy.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Least Favorable Priors →](03-2-least-favorable-priors.md)
