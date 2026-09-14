---
title: Jamesstein Part 03 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/jamesstein.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/jamesstein.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Jamesstein Part 03 —

**Source:** [`units/reader/jamesstein.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/jamesstein.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">2.1</span> Stein’s Lemma {.anchored number="2.1" anchor-id="steins-lemma"}

The first ingredient in finding the MSE of <span class="math inline">\$\\delta\_\\text{JS}\$</span> is a lemma called *Stein’s Lemma*:

**Theorem (Stein’s lemma, univariate):** Suppose <span class="math inline">\$X \\sim N(\\theta, \\sigma^2)\$</span>, and that <span class="math inline">\$h:\\; \\RR \\to \\RR\$</span> is differentiable, with <span class="math inline">\$\\EE\|\\dot{h}(X)\| &lt; \\infty\$</span>. Then we have <span class="math display">\\$$\\Cov(X, h(X)) = \\EE\[(X-\\theta)h(X)$$ = \\sigma^2\\EE$$\\dot{h}(X)$$.\\\]</span>

*Proof*:

Next, we will do the calculation for <span class="math inline">\$\\theta = 0\$</span> and <span class="math inline">\$\\sigma^2 = 1\$</span>. Then <span class="math display">\\$$\\EE\[Xh(X)$$ = \\int\_{-\\infty}^\\infty xh(x)\\phi(x)\\,dx = \\int\_{-\\infty}^\\infty \\dot{h}(x)\\phi(x)\\,dx,\\\]</span> where we’ve used integration by parts: <span class="math display">\\$$\\dot{\\phi}(x) = \\frac{d}{dx} \\frac{1}{\\sqrt{2\\pi}}e^{-x^2/2} = -x \\frac{1}{\\sqrt{2\\pi}}e^{-x^2/2} = -x\\phi(x).\\$$</span> (A slightly more rigorous version is in the handwritten notes: we can assume wlog <span class="math inline">\$h(0) = 0\$</span> because otherwise we could center it by using <span class="math inline">\$k(X) = h(X) - h(0)\$</span>, which has the same covariance with <span class="math inline">\$X\$</span>. Then we can break up the integral into an integral from <span class="math inline">\$0\$</span> to <span class="math inline">\$\\infty\$</span> and another from <span class="math inline">\$-\\infty\$</span> to <span class="math inline">\$0\$</span>, and do integration by parts a bit more carefully for each.)

For more general <span class="math inline">\$\\theta\$</span>, we can write <span class="math inline">\$X = \\theta + \\sigma Z\$</span>, where <span class="math inline">\$Z \\sim N(0,1)\$</span>. Then applying the result for <span class="math inline">\$k(z) = h(\\theta + \\sigma z)\$</span>, we have

<span class="math display">\\$$\\EE\[(X-\\theta) h(X)$$ = \\sigma\\EE$$Zh(\\theta + \\sigma Z)$$ = \\sigma^2\\EE$$\\dot{h}(\\theta + \\sigma Z)$$ = \\sigma^2\\EE$$\\dot{h}(X)$$,\\\]</span> giving the general result.

We will need the multivariate version of Stein’s lemma. For a function <span class="math inline">\$h:\\; \\RR^d \\to \\RR^d\$</span>, define the Jacobian matrix <span class="math inline">\$Dh \\in \\RR^{d\\times d}\$</span> by <span class="math display">\\$$(Dh(x))\_{ij} = \\frac{\\partial h\_i}{\\partial x\_j}(x).\\$$</span>

Define the **Frobenius norm** <span class="math inline">\$A \\in \\RR^{d\\times d}\$</span> as <span class="math display">\\$$\\\|A\\\|\_F = \\left(\\sum\_{ij} A\_{ij}^2\\right)^{1/2}.\\$$</span>

Now we can state our theorem:

**Theorem (Stein’s lemma, multivariate):** Assume <span class="math inline">\$X \\sim N\_d(\\theta; \\sigma^2 I\_d)\$</span>, and <span class="math inline">\$h:\\;\\RR^d \\to \\RR^d\$</span> is differentiable with <span class="math inline">\$\\EE\\\|Dh(X)\\\|\_F &lt; \\infty\$</span>. Then <span class="math display">\\$$ \\EE\[(X-\\theta)'h(X)$$ = \\sigma^2 \\EE \\text{tr}(Dh(X)) = \\sigma^2 \\sum\_i \\EE \\frac{\\partial h\_i}{\\partial x\_i} (X).\\\]</span>

*Proof:* The proof follows from the proof of the univariate version if we observe that the distribution of <span class="math inline">\$X\_i\$</span> conditional on the other coordinates <span class="math inline">\$X\_{-i}\$</span> is <span class="math inline">\$N(\\theta, \\sigma^2)\$</span>. Then we have <span class="math display">\\$$ \\EE\\left\[(X\_i - \\theta\_i)h\_i(X) \\mid X\_{-i}\\right$$ = \\sigma^2 \\EE\\left$$\\frac{\\partial h\_i}{\\partial x\_i}(X\_i) \\mid X\_{-i} \\right$$.\\\]</span> Taking expectations gives <span class="math display">\\$$ \\EE\\left\[(X\_i - \\theta\_i)h\_i(X)\\right$$ = \\sigma^2 \\EE\\left$$\\frac{\\partial h\_i}{\\partial x\_i}(X\_i) \\right$$,\\\]</span> and summing over <span class="math inline">\$i\$</span> gives the result.

### <span class="header-section-number">2.2</span> Stein’s unbaised risk estimator (SURE) {.anchored number="2.2" anchor-id="steins-unbaised-risk-estimator-sure"}

We can obtain an unbiased estimator of the MSE for almost any differentiable estimator <span class="math inline">\$\\delta(X)\$</span> in the Gaussian sequence model, if we apply Stein’s lemma to the function <span class="math inline">\$h(x) = x - \\delta(x)\$</span>. We only need the derivative of <span class="math inline">\$h\$</span> to satisfy the condition of Stein’s lemma, which it does for most differentiable estimators.

Using the identity <span class="math inline">\$\\\|a - b\\\|^2 = \\\|a\\\|^2 + \\\|b\\\|^2 - 2a'b\$</span>, we have for <span class="math inline">\$h(x) = x - \\delta(x)\$</span>, <span class="math display">\\$$ \\begin{aligned} \\text{MSE}(\\theta; \\delta) &= \\EE\_\\theta\\\|\\delta(X) - \\theta\\\|^2\\\\ &= \\EE\_\\theta\\\|X - h(X) - \\theta\\\|^2\\\\ &= \\EE\_\\theta\\\|X - \\theta\\\|^2 + \\EE\_\\theta\\\|h(X)\\\|^2 - 2\\EE\_\\theta \\left\[(X - \\theta)'h(X)\\right$$\\\\ &= \\sigma^2 d + \\EE\_\\theta\\\|h(X)\\\|^2 - 2\\sigma^2 \\EE\_\\theta \\text{tr}(Dh(X)). \\end{aligned} \\\]</span> Thus, if <span class="math inline">\$\\sigma^2\$</span> is known, we obtain the unbiased estimator <span class="math display">\\$$ \\widehat{\\text{MSE}}(X) = \\sigma^2 d + \\\|h(X)\\\|^2 - 2 \\sigma^2 \\text{tr}(Dh(X)).\\$$</span>

### <span class="header-section-number">2.3</span> Example: shrinking toward <span class="math inline">\$\\overline{X}\$</span> {.anchored number="2.3" anchor-id="example-shrinking-toward-overlinex"}

As an example, we can estimate the MSE of an estimator that shrinks <span class="math inline">\$X\_i\$</span> partway toward the average estimate across the <span class="math inline">\$d\$</span> coordinates, <span class="math inline">\$\\overline{X} = \\frac{1}{d}\\sum\_i X\_i\$</span>: <span class="math display">\\$$ \\delta\_i^\\gamma(X) = (1-\\gamma) X\_i + \\gamma \\overline{X}. \\$$</span> We can think of this as making a bet that most of the <span class="math inline">\$\\theta\_i\$</span> values are close to <span class="math inline">\$\\bar{\\theta} = \\frac{1}{d}\\sum\_i \\theta\_i\$</span>. Then <span class="math display">\\$$ h(X) = X - \\delta^\\gamma(X) = \\gamma(X - \\overline{X} 1\_d), \\$$</span> and <span class="math display">\\$$ Dh(X)\_{ii} = \\frac{\\partial}{\\partial X\_i} \\gamma(X\_i - \\overline{X}) = \\gamma (1-1/d) \\Rightarrow \\text{tr}(Dh(X)) = (d-1)\\gamma \\$$</span> An unbiased estimator for the MSE of <span class="math inline">\$\\delta^\\gamma\$</span> is then <span class="math display">\\$$ \\widehat{\\text{MSE}}^\\gamma(X) = \\sigma^2 d + \\gamma^2(d-1)V^2 - 2(d-1) \\gamma \\sigma^2, \\$$</span> where <span class="math inline">\$V^2 = \\frac{1}{d-1}\\sum\_i (X\_i-\\overline{X})^2\$</span> is the sample variance. Take note that the <span class="math inline">\$X\_i\$</span> values are not assumed to be i.i.d. here, since their means are generically different.

We can use this estimator in two different ways. The simplest way would be to calculate the actual MSE by taking the estimator’s expectation, which we know is the actual MSE of <span class="math inline">\$\\delta^\\gamma\$</span>. The only random variable is <span class="math inline">\$V^2\$</span>. Write <span class="math inline">\$X\_i = \\theta\_i + Z\_i\$</span> where <span class="math inline">\$Z\_i \\sim N(0,\\sigma^2)\$</span>. Then we have <span class="math display">\\$$ \\frac{1}{d-1}\\sum\_i\\EE\_\\theta(X\_i-\\overline{X})^2 = \\frac{1}{d-1}\\sum\_i (\\theta\_i - \\bar{\\theta})^2 + \\frac{1}{d-1}\\sum\_i \\EE(Z\_i - \\overline{Z})^2 = \\beta^2 + \\sigma^2, \\$$</span> where <span class="math inline">\$\\beta^2 = \\frac{1}{d-1}\\sum\_i(\\theta\_i - \\bar{\\theta})^2\$</span> is the sample variance of the <span class="math inline">\$\\theta\_i\$</span> values. Plugging in this expectation and collecting terms, we obtain the MSE <span class="math display">\\$$ \\text{MSE}^\\gamma(\\theta) = \\EE\_\\theta\\left\[\\widehat{\\text{MSE}}^\\gamma(X)\\right$$ = \\sigma^2 + (d-1)(1-\\gamma)^2\\sigma^2 + (d-1)\\gamma^2\\beta^2. \\\]</span> We can solve for the optimal value <span class="math inline">\$\\gamma^\*(\\beta) = \\frac{\\sigma^2}{\\beta^2+\\sigma^2}\$</span>, which unsurprisingly depends on <span class="math inline">\$\\beta^2\$</span>. If <span class="math inline">\$\\beta^2 = 0\$</span> then all <span class="math inline">\$\\theta\_i\$</span> values are equal so we should set <span class="math inline">\$\\gamma = 1\$</span> (shrink fully to the sample mean), but if <span class="math inline">\$\\beta^2 \\gg \\sigma^2\$</span> we should take <span class="math inline">\$\\gamma \\to 0\$</span> (shrink very little).

We could also choose <span class="math inline">\$\\gamma\$</span> adaptively to minimize this estimator. That is, we could take <span class="math display">\\$$ \\hat\\gamma(X) = \\argmin\_\\gamma \\widehat{\\text{MSE}}^\\gamma(X) = \\sigma^2/V^2, \\$$</span> which we could think of as an estimator of <span class="math inline">\$\\gamma^\*(X)\$</span> since <span class="math inline">\$V^2\$</span> is unbiased for <span class="math inline">\$\\beta^2+\\sigma^2\$</span>. If we plug in <span class="math inline">\$\\hat\\gamma(X)\$</span> we get a new adaptive shrinkage estimator which is not the same as <span class="math inline">\$\\delta^\\gamma\$</span> for any fixed <span class="math inline">\$\\gamma\$</span>, and we could use the same idea to calculate its MSE, if we wanted to.

---

[← 1 Gaussian sequence model {.anchored number="1" anchor-id="gaussian-sequence-model"}](02-1-gaussian-sequence-model-anchored-number-1-anchor-id-gaussi.md) · [Up: contents](index.md) · [Jamesstein Part 04 — →](04-jamesstein-part-04.md)
