---
title: Empirical bayes Part 03 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Empirical bayes Part 03 —

**Source:** [`reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">2.1</span> Stein’s Lemma {.anchored number="2.1" anchor-id="steins-lemma"}

The first ingredient in finding the MSE of <span class="math inline">\$\\delta\_\\text{JS}\$</span> is a lemma called *Stein’s Lemma*:

**Theorem (Stein’s lemma, univariate):** Suppose <span class="math inline">\$X \\sim N(\\theta, \\sigma^2)\$</span>, and that <span class="math inline">\$h:\\; \\RR \\to \\RR\$</span> is differentiable, with <span class="math inline">\$\\EE\|\\dot{h}(X)\| &lt; \\infty\$</span>. Then we have <span class="math display">\\$$\\Cov(X, h(X)) = \\EE\[(X-\\theta)h(X)$$ = \\sigma^2\\EE$$\\dot{h}(X)$$.\\\]</span>

*Proof*:

Next, we will do the calculation for <span class="math inline">\$\\theta = 0\$</span> and <span class="math inline">\$\\sigma^2 = 1\$</span>. Then <span class="math display">\\$$\\EE\[Xh(X)$$ = \\int\_{-\\infty}^\\infty xh(x)\\phi(x)\\,dx = \\int\_{-\\infty}^\\infty \\dot{h}(x)\\phi(x)\\,dx,\\\]</span> where we’ve used integration by parts: <span class="math display">\\$$\\dot{\\phi}(x) = \\frac{d}{dx} \\frac{1}{\\sqrt{2\\pi}}e^{-x^2/2} = -x \\frac{1}{\\sqrt{2\\pi}}e^{-x^2/2} = -x\\phi(x).\\$$</span> (A slightly more rigorous version is in the handwritten notes: we can assume wlog <span class="math inline">\$h(0) = 0\$</span> because otherwise we could center it by using <span class="math inline">\$k(X) = h(X) - h(0)\$</span>, which has the same covariance with <span class="math inline">\$X\$</span>. Then we can break up the integral into an integral from <span class="math inline">\$0\$</span> to <span class="math inline">\$\\infty\$</span> and another from <span class="math inline">\$-\\infty\$</span> to <span class="math inline">\$0\$</span>, and do integration by parts a bit more carefully for each.)

For more general <span class="math inline">\$\\theta\$</span>, we can write <span class="math inline">\$X = \\theta + \\sigma Z\$</span>, where <span class="math inline">\$Z \\sim N(0,1)\$</span>. Then applying the result for <span class="math inline">\$k(z) = h(\\theta + \\sigma z)\$</span>, we have

<span class="math display">\\$$\\EE\[(X-\\theta) h(X)$$ = \\sigma\\EE$$Zh(\\theta + \\sigma Z)$$ = \\sigma^2\\EE$$\\dot{h}(\\theta + \\sigma Z)$$ = \\sigma^2\\EE$$\\dot{h}(X)$$,\\\]</span> giving the general result.

We will need the multivariate version of Stein’s lemma. For a function <span class="math inline">\$h:\\; \\RR^d \\to \\RR^d\$</span>, define the Jacobian matrix <span class="math inline">\$Dh \\in \\RR^{d\\times d}\$</span> by <span class="math display">\\$$(Dh(x))\_{ij} = \\frac{\\partial h\_i}{\\partial x\_j}(x).\\$$</span>

Define the **Frobenius norm** <span class="math inline">\$A \\in \\RR^{d\\times d}\$</span> as <span class="math display">\\$$\\\|A\\\|\_F = (\\sum\_{ij} A\_{ij}^2)^{1/2}.\\$$</span>

Now we can state our theorem:

**Theorem (Stein’s lemma, multivariate):** Assume <span class="math inline">\$X \\sim N\_d(\\theta; \\sigma^2 I\_d)\$</span>, and <span class="math inline">\$h:\\;\\RR^d \\to \\RR^d\$</span> is differentiable with <span class="math inline">\$\\EE\\\|Dh(X)\\\|\_F &lt; \\infty\$</span>. Then <span class="math display">\\$$ \\EE\[(X-\\theta)'h(X)$$ = \\sigma^2 \\EE \\text{tr}(Dh(X)) = \\sigma^2 \\sum\_i \\EE \\frac{\\partial h\_i}{\\partial x\_i} (X).\\\]</span>

The proof follows easily from the proof of the univariate version, and appears in the handwritten notes.

### <span class="header-section-number">2.2</span> Stein’s unbaised risk estimator (SURE) {.anchored number="2.2" anchor-id="steins-unbaised-risk-estimator-sure"}

### <span class="header-section-number">2.3</span> Risk of James-Stein {.anchored number="2.3" anchor-id="risk-of-james-stein"}

---

[← 1 Gaussian sequence model {.anchored number="1" anchor-id="gaussian-sequence-model"}](02-1-gaussian-sequence-model-anchored-number-1-anchor-id-gaussi.md) · [Up: contents](index.md) · [3 Empirical Bayes {.anchored number="3" anchor-id="empirical-bayes"} →](04-3-empirical-bayes-anchored-number-3-anchor-id-empirical-baye.md)
