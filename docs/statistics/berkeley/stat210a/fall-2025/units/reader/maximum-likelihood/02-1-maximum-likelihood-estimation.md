---
title: 1 Maximum Likelihood Estimation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/maximum-likelihood.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/maximum-likelihood.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Maximum Likelihood Estimation

**Source:** [`units/reader/maximum-likelihood.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/maximum-likelihood.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

For a generic dominated family <span class="math inline">\$\\cP = \\{P\_\\theta: \\theta \\in \\Theta\\}\$</span> with densities <span class="math inline">\$f\_\\theta\$</span>, a simple estimator for <span class="math inline">\$\\theta\$</span> is:

<span class="math display">\\$$\\hat{\\theta}\_{\\text{MLE}}(X) = \\arg\\max\_{\\theta \\in \\Theta} p\_\\theta(X) = \\arg\\max\_{\\theta \\in \\Theta} \\prod\_{i=1}^n f\_\\theta(X\_i) = \\arg\\max\_{\\theta \\in \\Theta} \\ell\_n(\\theta; X)\\$$</span>

Remarks: 1. <span class="math inline">\$\\arg\\max\$</span> may not exist, be unique, or be computable 2. Doesn’t depend on parameterization or base measure; MLE for <span class="math inline">\$g(\\theta)\$</span> is <span class="math inline">\$g(\\hat{\\theta}\_{\\text{MLE}})\$</span>

### <span class="header-section-number">1.1</span> Example: Exponential Family {.anchored number="1.1" anchor-id="example-exponential-family"}

<span class="math display">\\$$\\ell(\\eta; X) = \\eta^T T(X) - A(\\eta) + \\log h(X)\\$$</span>

<span class="math inline">\$T(\\bar{X}) = \\mathbb{E}\_\\eta$$T(X)$$\$</span> if such <span class="math inline">\$\\eta\$</span> exists

Because <span class="math inline">\$\\ell''(\\eta; X) = -\\text{Var}\_\\eta$$T(X)$$\$</span> is negative definite unless <span class="math inline">\$\\eta \\to T(\\eta)\$</span> constant, in which case param redundant

At most 1 solution exists

Let <span class="math inline">\$m(X) = \\mathbb{E}\_\\eta$$T(X)$$ = \\nabla A(\\eta)\$</span>

### <span class="header-section-number">1.2</span> Example: Normal Distribution {.anchored number="1.2" anchor-id="example-normal-distribution"}

<span class="math inline">\$X\_i \\sim \\text{iid } N(\\theta, \\sigma^2)\$</span>, <span class="math inline">\$h(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} e^{-x^2/(2\\sigma^2)}\$</span>, <span class="math inline">\$\\eta \\in \\mathbb{R}\$</span>

<span class="math inline">\$T(X) = \\frac{X}{\\sigma^2}\$</span>, <span class="math inline">\$A(\\eta) = \\frac{\\eta^2}{2\\sigma^2}\$</span>

Assume <span class="math inline">\$\\eta = \\theta/\\sigma^2\$</span>, <span class="math inline">\$\\sigma^2\$</span> known

<span class="math inline">\$m(\\eta) = \\eta\\sigma^2 = \\theta\$</span>, <span class="math inline">\$m^{-1}(\\theta) = \\theta/\\sigma^2\$</span>

Consistency: <span class="math inline">\$\\bar{X} \\xrightarrow{p} \\theta\$</span> (LLN)

Cts mapping: <span class="math inline">\$\\hat{\\eta} = m^{-1}(\\bar{X}) \\xrightarrow{p} \\theta/\\sigma^2\$</span>

Since <span class="math inline">\$\\sqrt{n}(\\bar{X} - \\theta) \\xrightarrow{d} N(0, \\text{Var}\_\\eta$$T(X)$$)\$</span>:

<span class="math inline">\$N(0, \\sigma^2)\$</span>

Recall: <span class="math inline">\$J(\\eta) = \\text{Var}\_\\eta$$T(X)$$\$</span>

Delta method: <span class="math inline">\$\\sqrt{n}(\\hat{\\eta} - \\eta) \\xrightarrow{d} N(0, $$m^{-1'}(\\theta)$$^2 \\sigma^2)\$</span>

<span class="math inline">\$N(0, 1/\\sigma^2)\$</span>

Recall: <span class="math inline">\$J(\\eta) = \\text{Var}\_\\eta$$T(X)$$ = \\sigma^2\$</span>

<span class="math inline">\$N(0, J^{-1})\$</span>

Asymptotically unbiased Gaussian, achieves CRLB

### <span class="header-section-number">1.3</span> Example: Poisson Distribution {.anchored number="1.3" anchor-id="example-poisson-distribution"}

<span class="math inline">\$X\_i \\sim \\text{iid Poisson}(\\theta)\$</span>, <span class="math inline">\$\\eta = \\log \\theta\$</span>

<span class="math inline">\$T(X) = X\$</span>, <span class="math inline">\$\\mathbb{E}$$X$$ = \\theta\$</span>, <span class="math inline">\$N(0, \\theta)\$</span>

<span class="math inline">\$\\hat{\\eta}\_n = \\log \\bar{X}\$</span>, <span class="math inline">\$\\sqrt{n}(\\log \\bar{X} - \\log \\theta) \\xrightarrow{d} N(0, \\theta^{-1})\$</span> (Delta method)

<span class="math inline">\$N(0, \\theta^{-1})\$</span>

But for finite <span class="math inline">\$n\$</span>, <span class="math inline">\$\\mathbb{P}(\\bar{X} = 0) = \\mathbb{P}(X\_1 = 0)^n = e^{-n\\theta} &gt; 0\$</span>

MLE can have embarrassing finite sample performance despite being asymptotically optimal

### <span class="header-section-number">1.4</span> Proof: Convergence in Distribution with Probability Approaching 1 {.anchored number="1.4" anchor-id="proof-convergence-in-distribution-with-probability-approaching-1"}

If <span class="math inline">\$\\mathbb{P}(B\_n) \\to 1\$</span>, <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>, <span class="math inline">\$Z\_n\$</span> arbitrary, then <span class="math inline">\$X\_n 1\_{B\_n} + Z\_n 1\_{B\_n^c} \\xrightarrow{d} X\$</span>

Proof: <span class="math inline">\$\\mathbb{P}(\\\|Z\_n 1\_{B\_n^c}\\\| &gt; \\epsilon) \\leq \\mathbb{P}(B\_n^c) \\to 0\$</span>, so <span class="math inline">\$Z\_n 1\_{B\_n^c} \\xrightarrow{p} 0\$</span> Also, <span class="math inline">\$1\_{B\_n} \\xrightarrow{p} 1\$</span>, apply Slutsky

Any zany behavior has no effect on convergence in distribution

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Asymptotic Efficiency →](03-2-asymptotic-efficiency.md)
