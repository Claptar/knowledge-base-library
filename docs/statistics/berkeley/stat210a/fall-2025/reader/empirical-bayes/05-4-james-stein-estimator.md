---
title: 4 James-Stein Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 James-Stein Estimator

**Source:** [`reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

<span class="math display">\\$$\\delta\_{JS}(X) = (1 - \\frac{d-2}{\\\|X\\\|^2})X\\$$</span>

Proof: If <span class="math inline">\$Y \\sim \\text{Gamma}(\\frac{d}{2}, \\frac{1}{2})\$</span>, then:

<span class="math display">\\$$\\mathbb{P}(Y &gt; \\frac{d-2}{2}) = 1\\$$</span>

Now use <span class="math inline">\$f(x) = x - \\frac{d-2}{x}\$</span>, <span class="math inline">\$\\frac{1}{2}\\\|X\\\|^2 \\sim \\text{Gamma}(\\frac{d}{2}, \\frac{1}{2})\$</span>

<span class="math display">\\$$\\mathbb{E}\[f(\\frac{1}{2}\\\|X\\\|^2)$$ &gt; f(\\mathbb{E}$$\\frac{1}{2}\\\|X\\\|^2$$) = \\frac{d}{2} - \\frac{d-2}{\\frac{d}{2}} = 1\\\]</span>

### <span class="header-section-number">4.1</span> James-Stein Paradox {.anchored number="4.1" anchor-id="james-stein-paradox-1"}

For <span class="math inline">\$d \\geq 3\$</span>, the sample mean <span class="math inline">\$\\bar{X} = \\frac{1}{n}\\sum X\_i\$</span> is inadmissible as an estimator of <span class="math inline">\$\\theta\$</span> under squared error loss.

For <span class="math inline">\$\\delta\_{JS}(X) = (1 - \\frac{d-2}{\\\|X\\\|^2})X\$</span>:

<span class="math display">\\$$\\text{MSE}(\\theta, \\delta\_{JS}) &lt; \\text{MSE}(\\theta, \\bar{X}) \\quad \\forall \\theta \\in \\mathbb{R}^d\\$$</span>

Notes: - <span class="math inline">\$\\bar{X}\$</span> is UMVU, Minimax, objective Bayes - Might as well take <span class="math inline">\$n=1\$</span> (Sufficiency reduction) - This result holds without assumption of Bayes model on <span class="math inline">\$\\theta\$</span>: true for <span class="math inline">\$\\theta = (50, 10, 94, \\ldots)\$</span> - Nothing special about 0: for any <span class="math inline">\$\\theta\_0 \\in \\mathbb{R}^d\$</span>, <span class="math inline">\$\\delta(X) = \\theta\_0 + (1 - \\frac{d-2}{\\\|X-\\theta\_0\\\|^2})(X-\\theta\_0)\$</span> also dominates <span class="math inline">\$X\$</span>

Deep implication: shrinkage makes sense even without Bayes justification.

### <span class="header-section-number">4.2</span> General Form {.anchored number="4.2" anchor-id="general-form"}

Let <span class="math inline">\$\\delta(X) = (1 - \\frac{c}{\\\|X\\\|^2})X\$</span>, <span class="math inline">\$c\$</span> is tuning parameter

<span class="math display">\\$$R(\\theta, \\delta) = \\mathbb{E}\_\\theta\\\|\\delta(X) - \\theta\\\|^2 = \\mathbb{E}\_\\theta\\\|X - \\theta\\\|^2 + \\mathbb{E}\_\\theta\[\\frac{c^2}{\\\|X\\\|^2} - 2c$$\\\]</span>

What is optimal <span class="math inline">\$c\$</span>?

<span class="math display">\\$$R(\\theta, \\delta) = d + \\mathbb{E}\_\\theta\[\\frac{c^2}{\\\|X\\\|^2}$$ - 2c\\\]</span>

<span class="math display">\\$$\\frac{\\partial R}{\\partial c} = 2\\mathbb{E}\_\\theta\[\\frac{c}{\\\|X\\\|^2}$$ - 2 = 0\\\]</span>

<span class="math display">\\$$c = \\frac{\\mathbb{E}\_\\theta\[\\\|X\\\|^2$$}{\\mathbb{E}\_\\theta$$\\frac{1}{\\\|X\\\|^2}$$}\\\]</span>

<span class="math inline">\$c\$</span> always &gt; 0, but → 0 as <span class="math inline">\$\\\|\\theta\\\| → \\infty\$</span>

What if we estimate <span class="math inline">\$c\$</span>? How does adaptivity of <span class="math inline">\$c(X)\$</span> affect MSE?

---

[← 3 Empirical Bayes](04-3-empirical-bayes.md) · [Up: contents](index.md) · [5 Stein’s Lemma →](06-5-stein-s-lemma.md)
