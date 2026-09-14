---
title: Score fisher Part 03 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Score fisher Part 03 —

**Source:** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assuming enough regularity, we can arrive at some important differential identities by differentiating both sides of the equation

<span class="math display">\\$$1 = \\int\_\\cX e^{\\ell(\\theta;x)}\\,d\\mu(x).\\$$</span>

Differentiating both sides with respect to <span class="math inline">\$\\theta\_j\$</span>, we obtain <span class="math display">\\$$0 = \\int\_\\cX \\frac{\\partial}{\\partial \\theta\_j} \\ell(\\theta; x) e^{\\ell(\\theta; x)}\\,d\\mu(x) = \\EE\_\\theta \\left\[\\frac{\\partial}{\\partial\\theta\_j}\\ell(\\theta;X)\\right$$.\\\]</span> Collecting these identities into a vector, we obtain <span class="math display">\\$$ \\EE\_\\theta \[S\_\\theta(X)$$ = 0. \\\]</span> Importantly, note that this identity only holds if the two values of <span class="math inline">\$\\theta\$</span> in the above expression match each other. So if the analyst calculates the score function at some reference value <span class="math inline">\$\\theta\_0\$</span>, but the true parameter is some other value <span class="math inline">\$\\theta \\neq \\theta\_0\$</span>, we typically would have <span class="math inline">\$\\EE\_\\theta$$S\_{\\theta\_0}(X)$$ \\neq 0\$</span>.

If we differentiate the identity a second time with respect to <span class="math inline">\$\\theta\_k\$</span>, we obtain <span class="math display">\\$$ 0 = \\int\_\\cX \\left(\\frac{\\partial^2\\ell}{\\partial \\theta\_j\\partial\\theta\_k} + \\frac{\\partial \\ell}{\\partial \\theta\_j}\\frac{\\partial \\ell}{\\partial\\theta\_k}\\right) e^{\\ell}\\,d\\mu = \\EE\_\\theta\\left\[\\frac{\\partial^2\\ell}{\\partial \\theta\_j\\partial\\theta\_k}\\right$$ + \\EE\_\\theta\\left$$\\frac{\\partial \\ell}{\\partial \\theta\_j}\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right$$ %= \\EE\_\\theta\\left$$\\frac{\\partial^2\\ell}{\\partial \\theta\_j\\partial\\theta\_k}\\right$$ + \\Cov\_\\theta\\left(\\frac{\\partial \\ell}{\\partial \\theta\_j},\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right). \\\]</span>

Again collecting these identities into a matrix, and noting that <span class="math display">\\$$ \\EE\_\\theta\\left\[\\frac{\\partial \\ell}{\\partial \\theta\_j}\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right$$ = \\Cov\_\\theta\\left(S\_{\\theta,j}(X),S\_{\\theta,k}(X)\\right), \\\]</span> we obtain <span class="math display">\\$$ \\Var\_\\theta\\left(S\_{\\theta}(X)\\right) = \\EE\_\\theta\\left\[-\\nabla^2\\ell(\\theta;X)\\right$$, \\\]</span> again with the important observation that the equality holds only if the <span class="math inline">\$\\theta\$</span> in both subscripts matches the <span class="math inline">\$\\theta\$</span> where we are calculating derivatives.

The left-hand side of the last equation, the variance of the score, is called the *Fisher Information* matrix <span class="math display">\\$$ J(\\theta) := \\Var\_\\theta(S\_\\theta(X)). \\$$</span> Note <span class="math inline">\$J(\\theta)\$</span> is always positive semidefinite.

We will not discuss in detail the regularity conditions on <span class="math inline">\$\\ell\$</span> (basically, one or two “tame” derivatives) that make these identities work; the correct regularity conditions are complicated. But the score function is useful even certain models where <span class="math inline">\$\\ell(\\theta;x)\$</span> is not differentiable with respect to <span class="math inline">\$\\theta\$</span>, such as the Laplace location family.

---

[← 1 Score Function {.anchored number="1" anchor-id="score-function"}](02-1-score-function-anchored-number-1-anchor-id-score-function.md) · [Up: contents](index.md) · [3 Cramér-Rao Lower Bound {.anchored number="3" anchor-id="cramér-rao-lower-bound"} →](04-3-cramér-rao-lower-bound-anchored-number-3-anchor-id-cramér.md)
