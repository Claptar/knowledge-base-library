---
title: Maximum likelihood Part 04 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/maximum-likelihood.html
source_file: sources/berkeley-stat210a/fall-2025/reader/maximum-likelihood.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Maximum likelihood Part 04 —

**Source:** [`reader/maximum-likelihood.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/maximum-likelihood.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Under mild conditions, <span class="math inline">\$\\hat{\\theta}\_n\$</span> is asymptotically Gaussian efficient

We will be interested in <span class="math inline">\$\\ell\_n(\\theta; X)\$</span> as a function of <span class="math inline">\$\\theta\$</span> Notate true value as <span class="math inline">\$\\theta\_0\$</span>: <span class="math inline">\$X \\sim P\_{\\theta\_0}\$</span>

Derivatives of <span class="math inline">\$\\ell\_n\$</span> at <span class="math inline">\$\\theta\_0\$</span>: <span class="math inline">\$S\_0\$</span>, <span class="math inline">\$S\_1\$</span>

<span class="math inline">\$S\_n(\\theta\_0; X) = \\sum\_{i=1}^n \\nabla \\ell\_i(\\theta\_0; X\_i) \\sim N(0, J\_n(\\theta\_0))\$</span>

<span class="math inline">\$\\mathbb{E}$$S\_n(\\theta; X)$$ = n\\mathbb{E}$$\\nabla \\ell\_i(\\theta\_0; X\_i)$$ = 0\$</span>

<span class="math inline">\$\\mathbb{E}$$-\\nabla^2 \\ell\_n(\\theta; X)$$ = \\mathbb{E}$$\\sum\_{i=1}^n -\\nabla^2 \\ell\_i(\\theta\_0; X\_i)$$ = J\_n(\\theta\_0)\$</span>

### <span class="header-section-number">3.1</span> Informal Proof {.anchored number="3.1" anchor-id="informal-proof"}

Taylor expansion between <span class="math inline">\$\\theta\_0\$</span>, <span class="math inline">\$\\hat{\\theta}\_n\$</span>:

<span class="math inline">\$S\_n(\\hat{\\theta}\_n; X) = S\_n(\\theta\_0; X) + S\_n'(\\theta\_0; X)(\\hat{\\theta}\_n - \\theta\_0)\$</span>

<span class="math inline">\$\\sqrt{n}(\\hat{\\theta}\_n - \\theta\_0) = J\_n^{-1}(\\theta\_0) S\_n(\\theta\_0; X)/\\sqrt{n}\$</span>

<span class="math inline">\$\\xrightarrow{d} N(0, J\_1^{-1}(\\theta\_0))\$</span>

More rigorous proof later, but note we need consistency of <span class="math inline">\$\\hat{\\theta}\_n\$</span> first to even justify Taylor expansion

### <span class="header-section-number">3.2</span> Quadratic Approximation {.anchored number="3.2" anchor-id="quadratic-approximation"}

Quadratic approximation near <span class="math inline">\$\\theta\_0\$</span>:

<span class="math inline">\$\\ell\_n(\\theta) \\approx \\ell\_n(\\theta\_0) + (\\theta - \\theta\_0)^T S\_n(\\theta\_0) - \\frac{1}{2}(\\theta - \\theta\_0)^T J\_n(\\theta\_0)(\\theta - \\theta\_0)\$</span>

<span class="math inline">\$N(J\_n^{-1}(\\theta\_0)S\_n(\\theta\_0), J\_n^{-1}(\\theta\_0))\$</span>

Gaussian linear term + Deterministic curvature

<span class="math inline">\$\\ell\_n(\\theta) - \\ell\_n(\\theta\_0) \\approx -\\frac{n}{2}(\\theta - \\hat{\\theta}\_n)^T J\_1(\\theta\_0)(\\theta - \\hat{\\theta}\_n) + \\text{const}\$</span>

---

[← 2 Asymptotic Efficiency {.anchored number="2" anchor-id="asymptotic-efficiency"}](03-2-asymptotic-efficiency-anchored-number-2-anchor-id-asymptot.md) · [Up: contents](index.md) · [4 Consistency of MLE {.anchored number="4" anchor-id="consistency-of-mle"} →](05-4-consistency-of-mle-anchored-number-4-anchor-id-consistency.md)
