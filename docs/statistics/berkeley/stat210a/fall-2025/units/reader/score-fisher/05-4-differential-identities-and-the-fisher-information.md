---
title: 4 Differential Identities and the Fisher Information
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Differential Identities and the Fisher Information

**Source:** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Assuming enough regularity, we can arrive at some important differential identities by differentiating both sides of the equation

<span class="math display">\\$$1 = \\int\_\\cX e^{\\ell(\\theta;x)}\\,d\\mu(x).\\$$</span>

Differentiating both sides with respect to <span class="math inline">\$\\theta\_j\$</span>, we obtain <span class="math display">\\$$0 = \\int\_\\cX \\frac{\\partial}{\\partial \\theta\_j} \\ell(\\theta; x) e^{\\ell(\\theta; x)}\\,d\\mu(x) = \\EE\_\\theta \\left\[\\frac{\\partial}{\\partial\\theta\_j}\\ell(\\theta;X)\\right$$.\\\]</span> Collecting these identities into a vector, we obtain <span class="math display">\\$$\\EE\_\\theta \[\\nabla \\ell(\\theta; X)$$ = 0.\\\]</span> Importantly, note that this identity only holds if the <span class="math inline">\$\\theta\$</span> in the subscript (defining the distribution with respect to which the expectation is taken) matches the <span class="math inline">\$\\theta\$</span> at which the gradient is being evaluated.

If we differentiate the identity a second time with respect to <span class="math inline">\$\\theta\_k\$</span>, we obtain <span class="math display">\\$$0 = \\int\_\\cX \\left(\\frac{\\partial^2\\ell}{\\partial \\theta\_j\\partial\\theta\_k} + \\frac{\\partial \\ell}{\\partial \\theta\_j}\\frac{\\partial \\ell}{\\partial\\theta\_k}\\right) e^{\\ell}\\,d\\mu = \\EE\_\\theta\\left\[\\frac{\\partial^2\\ell}{\\partial \\theta\_j\\partial\\theta\_k}\\right$$ + \\EE\_\\theta\\left$$\\frac{\\partial \\ell}{\\partial \\theta\_j}\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right$$ %= \\EE\_\\theta\\left$$\\frac{\\partial^2\\ell}{\\partial \\theta\_j\\partial\\theta\_k}\\right$$ + \\Cov\_\\theta\\left(\\frac{\\partial \\ell}{\\partial \\theta\_j},\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right). \\\]</span> Again collecting these identities into a matrix, and noting that <span class="math display">\\$$\\EE\_\\theta\\left\[\\frac{\\partial \\ell}{\\partial \\theta\_j}\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right$$ = \\Cov\_\\theta\\left(\\frac{\\partial \\ell}{\\partial \\theta\_j},\\frac{\\partial \\ell}{\\partial \\theta\_k}\\right),\\\]</span> we obtain <span class="math display">\\$$\\Var\_\\theta\\left(\\nabla\\ell(\\theta;X)\\right) = \\EE\_\\theta\\left\[-\\nabla^2\\ell(\\theta;X)\\right$$,\\\]</span> again with the important observation that the <span class="math inline">\$\\theta\$</span> in both subscripts must match the <span class="math inline">\$\\theta\$</span> where the first and second derivatives are evaluated.

The left-hand side of the last equation, the variance of the score, is called the *Fisher Information* matrix <span class="math display">\\$$ J(\\theta) := \\Var\_\\theta(\\nabla\\ell(\\theta;X)). \\$$</span> Note <span class="math inline">\$J(\\theta)\$</span> is always positive semidefinite. It is possible to extend this definition to certain models where <span class="math inline">\$\\ell(\\theta;x)\$</span> is not differentiable with respect to <span class="math inline">\$\\theta\$</span>, such as the Laplace location family. However we will not explore these generalizations.

---

[← 3 Score Function](04-3-score-function.md) · [Up: contents](index.md) · [5 Cramér-Rao Lower Bound →](06-5-cramér-rao-lower-bound.md)
