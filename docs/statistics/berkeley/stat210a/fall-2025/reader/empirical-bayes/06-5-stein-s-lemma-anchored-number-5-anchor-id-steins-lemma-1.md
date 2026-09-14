---
title: 5 Stein’s Lemma {.anchored number="5" anchor-id="steins-lemma-1"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 Stein’s Lemma {.anchored number="5" anchor-id="steins-lemma-1"}

**Source:** [`reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Useful tool for computing/estimating risk in Gaussian estimation problems.

### <span class="header-section-number">5.1</span> Theorem (Stein’s Lemma - Univariate) {.anchored number="5.1" anchor-id="theorem-steins-lemma---univariate"}

Suppose <span class="math inline">\$X \\sim N(\\theta, \\sigma^2)\$</span> <span class="math inline">\$h: \\mathbb{R} → \\mathbb{R}\$</span> differentiable, <span class="math inline">\$\\mathbb{E}\|h'(X)\| &lt; \\infty\$</span>

Then <span class="math inline">\$\\mathbb{E}$$(X-\\theta)h(X)$$ = \\sigma^2\\mathbb{E}$$h'(X)$$\$</span>

<span class="math inline">\$\\text{Cov}(X, h(X)) = \\sigma^2\\mathbb{E}$$h'(X)$$\$</span>

Proof: Note we can assume w.l.o.g. <span class="math inline">\$h(0) = 0\$</span> (why?) First assume <span class="math inline">\$\\theta = 0\$</span>, <span class="math inline">\$\\sigma^2 = 1\$</span>

<span class="math display">\\$$\\mathbb{E}\[Xh(X)$$ = \\int xh(x)\\phi(x)dx = \\int xh(x)\\phi(x)dx - \\int h(x)\\phi'(x)dx = \\int h'(x)\\phi(x)dx\\\]</span>

In the last step we have used <span class="math inline">\$\\phi'(x) = -x\\phi(x)\$</span>

Similar argument shows <span class="math inline">\$\\int h(x)\\phi(x)dx = \\int h'(x)\\phi(x)dx\$</span>

Result holds for <span class="math inline">\$\\theta = 0\$</span>, <span class="math inline">\$\\sigma^2 = 1\$</span>

General <span class="math inline">\$\\theta\$</span>, <span class="math inline">\$\\sigma^2 \\neq 1\$</span>: write <span class="math inline">\$X = \\theta + \\sigma Z\$</span>, <span class="math inline">\$Z \\sim N(0,1)\$</span>

<span class="math display">\\$$\\mathbb{E}\[(X-\\theta)h(X)$$ = \\sigma\\mathbb{E}$$Zh(\\theta+\\sigma Z)$$ = \\sigma^2\\mathbb{E}$$h'(\\theta+\\sigma Z)$$ = \\sigma^2\\mathbb{E}$$h'(X)$$\\\]</span>

### <span class="header-section-number">5.2</span> Multivariate Version {.anchored number="5.2" anchor-id="multivariate-version"}

Define Frobenius norm: <span class="math inline">\$\\\|A\\\|\_F^2 = \\sum\_{i,j} A\_{ij}^2 = \\text{tr}(A^TA)\$</span>

### <span class="header-section-number">5.3</span> Theorem (Stein’s Lemma - Multivariate) {.anchored number="5.3" anchor-id="theorem-steins-lemma---multivariate"}

<span class="math inline">\$X \\sim N\_d(\\theta, \\sigma^2 I\_d)\$</span>, <span class="math inline">\$\\theta \\in \\mathbb{R}^d\$</span> <span class="math inline">\$h: \\mathbb{R}^d → \\mathbb{R}^d\$</span> differentiable, <span class="math inline">\$\\mathbb{E}\\\|Dh(X)\\\|\_F &lt; \\infty\$</span>

Then <span class="math inline">\$\\mathbb{E}$$(X-\\theta)^Th(X)$$ = \\sigma^2\\mathbb{E}$$\\text{tr}(Dh(X))$$\$</span>

<span class="math inline">\$\\mathbb{E}$$(X-\\theta)h(X)^T$$ = \\sigma^2\\mathbb{E}$$Dh(X)$$\$</span>

Proof:

<span class="math display">\\$$\\mathbb{E}\[(X\_i-\\theta\_i)h\_i(X)$$ = \\mathbb{E}$$\\mathbb{E}\[(X\_i-\\theta\_i)h\_i(X)\|X\_{-i}$$\]\\\]</span> <span class="math display">\\$$= \\sigma^2\\mathbb{E}\[\\frac{\\partial h\_i}{\\partial x\_i}(X)$$\\\]</span>

---

[← 4 James-Stein Estimator {.anchored number="4" anchor-id="james-stein-estimator"}](05-4-james-stein-estimator-anchored-number-4-anchor-id-james-st.md) · [Up: contents](index.md) · [Empirical bayes Part 07 — →](07-empirical-bayes-part-07.md)
