---
title: Empirical bayes Part 07 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Empirical bayes Part 07 —

**Source:** [`units/reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Unbiased estimator of the MSE of any <span class="math inline">\$\\delta(X)\$</span>

Apply Stein’s Lemma with <span class="math inline">\$h(x) = X - \\delta(x)\$</span>

Assume <span class="math inline">\$\\sigma^2 = 1\$</span>:

<span class="math display">\\$$R(\\theta, \\delta) = \\mathbb{E}\_\\theta\\\|\\delta(X) - \\theta\\\|^2 = \\mathbb{E}\_\\theta\\\|X - \\theta\\\|^2 + \\mathbb{E}\_\\theta\\\|\\delta(X) - X\\\|^2 - 2\\mathbb{E}\_\\theta\[(X-\\theta)^T(X-\\delta(X))$$\\\]</span> <span class="math display">\\$$= d + \\mathbb{E}\_\\theta\\\|\\delta(X) - X\\\|^2 - 2\\mathbb{E}\_\\theta\[\\text{tr}(D(X-\\delta(X)))$$\\\]</span>

<span class="math display">\\$$\\hat{R}(X) = d + \\\|\\delta(X) - X\\\|^2 - 2\\text{tr}(D\\delta(X))\\$$</span>

is unbiased for the MSE estimator <span class="math inline">\$\\delta(X)\$</span>

Only depends on X

Can also compute MSE via <span class="math inline">\$R = \\mathbb{E}\_\\theta$$\\hat{R}$$\$</span>

<span class="math display">\\$$\\mathbb{E}\_\\theta\[\\\|\\delta(X) - h(X)\\\|^2$$ = \\mathbb{E}\_\\theta$$\\\|\\delta(X) - \\theta\\\|^2$$ + \\mathbb{E}\_\\theta$$\\\|h(X) - \\theta\\\|^2$$ - 2\\mathbb{E}\_\\theta$$(\\delta(X) - \\theta)^T(h(X) - \\theta)$$\\\]</span>

<span class="math display">\\$$R = d + R(\\theta, \\delta) - 2\\mathbb{E}\_\\theta\[\\text{tr}(D\\delta(X))$$\\\]</span>

Example: <span class="math inline">\$\\delta(X) = (1-c)X\$</span> for fixed <span class="math inline">\$c\$</span>

<span class="math inline">\$h(x) = cX\$</span>, <span class="math inline">\$Dh = cI\_d\$</span>

<span class="math inline">\$\\hat{R} = d + c^2\\\|X\\\|^2 - 2cd\$</span>

### <span class="header-section-number">6.1</span> Risk of James-Stein {.anchored number="6.1" anchor-id="risk-of-james-stein-1"}

<span class="math inline">\$\\delta\_{JS}(X) = (1 - \\frac{d-2}{\\\|X\\\|^2})X\$</span>

<span class="math inline">\$h(X) = \\frac{d-2}{\\\|X\\\|^2}X\$</span>, <span class="math inline">\$Dh(X) = \\frac{d-2}{\\\|X\\\|^2}I\_d - 2(d-2)\\frac{XX^T}{\\\|X\\\|^4}\$</span>

<span class="math inline">\$\\\|h(X)\\\|^2 = \\frac{(d-2)^2}{\\\|X\\\|^2}\$</span>

<span class="math display">\\$$\\text{tr}(Dh(X)) = \\frac{d(d-2)}{\\\|X\\\|^2} - \\frac{2(d-2)}{\\\|X\\\|^2} = \\frac{(d-2)^2}{\\\|X\\\|^2}\\$$</span>

<span class="math display">\\$$\\hat{R} = d + \\frac{(d-2)^2}{\\\|X\\\|^2} - 2\\frac{(d-2)^2}{\\\|X\\\|^2} = d - \\frac{(d-2)^2}{\\\|X\\\|^2}\\$$</span>

<span class="math display">\\$$R(\\theta) = \\mathbb{E}\_\\theta\[\\hat{R}$$ = d - (d-2)^2\\mathbb{E}\_\\theta$$\\frac{1}{\\\|X\\\|^2}$$\\\]</span>

If <span class="math inline">\$\\theta = 0\$</span> then <span class="math inline">\$\\mathbb{E}\_0$$\\frac{1}{\\\|X\\\|^2}$$ = \\frac{1}{d-2}\$</span>

<span class="math display">\\$$R(0) = d - (d-2) = 2\\$$</span>

Possibly surprising

If <span class="math inline">\$\\theta \\neq 0\$</span> then <span class="math inline">\$\\mathbb{E}\_\\theta$$\\frac{1}{\\\|X\\\|^2}$$ &lt; \\frac{1}{\\\|\\theta\\\|^2}\$</span>

<span class="math display">\\$$R(\\theta) &lt; d - \\frac{(d-2)^2}{\\\|\\theta\\\|^2 + d}\\$$</span>

Smaller and smaller advantage, but always better

Note: <span class="math inline">\$\\delta\_{JS}(X)\$</span> also inadmissible

<span class="math inline">\$\\delta\_{+}(X) = (1 - \\frac{d-2}{\\\|X\\\|^2})\_+ X\$</span> is strictly better

Practically more useful version:

<span class="math display">\\$$\\delta\_{JS+}(X) = (1 - \\frac{d-3}{\\\|X\\\|^2})\_+ X\\$$</span>

Dominates <span class="math inline">\$\\delta(X) = X\$</span> for <span class="math inline">\$d \\geq 4\$</span>

Taken to logical extreme, suggestion seems dumb: should everyone at Berkeley pool their estimates?

Note: <span class="math inline">\$\\mathbb{E}\\\|\\hat{\\theta}\\\|^2\$</span> is improved, but <span class="math inline">\$\\mathbb{E}$$(\\hat{\\theta}\_i - \\theta\_i)^2$$\$</span> may get worse for individual coordinates.

---

[← 5 Stein’s Lemma {.anchored number="5" anchor-id="steins-lemma-1"}](06-5-stein-s-lemma-anchored-number-5-anchor-id-steins-lemma-1.md) · [Up: contents](index.md)
