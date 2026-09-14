---
title: 1 Likelihood-Based Inference
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/likelihood-inference.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Likelihood-Based Inference

**Source:** [`units/reader/likelihood-inference.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">1.1</span> Setting {.anchored number="1.1" anchor-id="setting"}

<span class="math inline">\$X\_1, \\ldots, X\_n \\stackrel{\\text{iid}}{\\sim} p\_\\theta(x)\$</span>, <span class="math inline">\$p\_\\theta \\in \\cP\$</span>, smooth in <span class="math inline">\$\\theta\$</span>

Assume: - <span class="math inline">\$\\mathbb{E}\_\\theta$$\\nabla \\ell\_\\theta(X)$$ = 0\$</span> - <span class="math inline">\$\\text{Var}\_\\theta$$\\nabla \\ell\_\\theta(X)$$ = \\mathbb{E}\_\\theta$$-\\nabla^2 \\ell\_\\theta(X)$$ = J(\\theta) &gt; 0\$</span> - MLE <span class="math inline">\$\\hat{\\theta}\$</span> Consistent

Then if <span class="math inline">\$\\theta = \\theta\_0\$</span>: - <span class="math inline">\$\\nabla \\ell\_n(\\theta\_0; X) \\sim N(0, nJ(\\theta\_0))\$</span> - <span class="math inline">\$-\\nabla^2 \\ell\_n(\\theta\_0; X) \\xrightarrow{p} nJ(\\theta\_0)\$</span>

Used <span class="math inline">\$\\theta = \\hat{\\theta} + J^{-1}(\\theta\_0) \\nabla \\ell\_n(\\theta\_0; X)/n + o\_p(n^{-1/2})\$</span> to get <span class="math inline">\$\\sqrt{n}(\\hat{\\theta} - \\theta\_0) \\sim N(0, J^{-1}(\\theta\_0))\$</span>

Can use this for inference on <span class="math inline">\$\\theta\_0\$</span>

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Wald-Type Confidence Regions →](03-2-wald-type-confidence-regions.md)
