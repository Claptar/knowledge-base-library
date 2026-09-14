---
title: 3 Score Test {.anchored number="3" anchor-id="score-test"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/likelihood-inference.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Score Test {.anchored number="3" anchor-id="score-test"}

**Source:** [`units/reader/likelihood-inference.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Test <span class="math inline">\$H\_0: \\theta = \\theta\_0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq \\theta\_0\$</span>

We can bypass quadratic approximation entirely by using score as test stat:

<span class="math inline">\$\\nabla \\ell\_n(\\theta\_0; X) \\sim N(0, nJ(\\theta\_0))\$</span> or <span class="math inline">\$J\_n^{-1/2}(\\theta\_0)\\nabla \\ell\_n(\\theta\_0; X) \\stackrel{\\cdot}{\\sim} N\_d(0, I\_d)\$</span>

So we can reject <span class="math inline">\$H\_0: \\theta = \\theta\_0\$</span> if <span class="math inline">\$\\\|\\hat{J}\_n^{-1/2}(\\theta\_0)\\nabla \\ell\_n(\\theta\_0; X)\\\|^2 &gt; \\chi^2\_{d,1-\\alpha}\$</span>

<span class="math inline">\$\\nabla \\ell\_n(\\theta\_0; X)^T \\hat{J}\_n^{-1}(\\theta\_0) \\nabla \\ell\_n(\\theta\_0; X) \\sim \\chi^2\_d\$</span>

Can do 1-sided tests

### <span class="header-section-number">3.1</span> Remarks {.anchored number="3.1" anchor-id="remarks-1"}

- No quadratic approx, no MLE
- No need to estimate Fisher info at <span class="math inline">\$\\theta\_0\$</span>
- Can be generalized to case with nuisance params
- Typically estimate via MLE on <span class="math inline">\$\\Theta\_0\$</span>

### <span class="header-section-number">3.2</span> Score Test is Invariant to Reparameterization {.anchored number="3.2" anchor-id="score-test-is-invariant-to-reparameterization"}

Assume <span class="math inline">\$\\Theta \\subset \\mathbb{R}^d\$</span>, <span class="math inline">\$\\eta = g(\\theta)\$</span>, <span class="math inline">\$\\Psi = g(\\Theta)\$</span>

<span class="math inline">\$q\_\\eta(x) = p\_{g^{-1}(\\eta)}(x)\$</span>

<span class="math inline">\$\\ell\_\\eta(x) = \\log q\_\\eta(x) = \\ell\_\\theta(x)\$</span>

<span class="math inline">\$\\nabla\_\\eta \\ell\_\\eta(x) = \\nabla\_\\theta \\ell\_\\theta(x) \\cdot \\nabla g^{-1}(\\eta)\$</span>

<span class="math inline">\$J\_\\eta(\\eta) = J\_\\theta(g^{-1}(\\eta)) \\cdot \\nabla g^{-1}(\\eta) \\cdot \\nabla g^{-1}(\\eta)^T\$</span>

So <span class="math inline">\$\\nabla\_\\eta \\ell\_\\eta(x)^T J\_\\eta^{-1}(\\eta) \\nabla\_\\eta \\ell\_\\eta(x) = \\nabla\_\\theta \\ell\_\\theta(x)^T J\_\\theta^{-1}(\\theta) \\nabla\_\\theta \\ell\_\\theta(x)\$</span>

if <span class="math inline">\$\\eta\_0 = g(\\theta\_0)\$</span>

### <span class="header-section-number">3.3</span> Example: 1-Parameter Exponential Family {.anchored number="3.3" anchor-id="example-1-parameter-exponential-family"}

<span class="math inline">\$X\_1, \\ldots, X\_n \\stackrel{\\text{iid}}{\\sim} e^{\\eta T(x) - A(\\eta)} h(x)\$</span>

<span class="math inline">\$\\nabla \\ell\_n(\\eta; X) = \\sum T(X\_i) - n\\mu(\\eta)\$</span>

<span class="math inline">\$\\ell\_n''(\\eta; X) = -n\\text{Var}\_\\eta$$T(X)$$\$</span>

<span class="math inline">\$\\hat{\\eta}\_n = \\text{MLE} = A'^{-1}(\\bar{T})\$</span>

<span class="math inline">\$\\frac{\\sum T(X\_i) - n\\mu(\\eta\_0)}{\\sqrt{n\\text{Var}\_{\\eta\_0}$$T(X)$$}} \\sim N(0,1)\$</span>

### <span class="header-section-number">3.4</span> Example: <span class="math inline">\$X\_1, \\ldots, X\_n \\stackrel{\\text{iid}}{\\sim} \\text{Laplace}(\\theta, 2\\sqrt{2})\$</span> {.anchored number="3.4" anchor-id="example-x_1-ldots-x_n-stackreltextiidsim-textlaplacetheta-2sqrt2"}

Test <span class="math inline">\$H\_0: \\theta = 0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq 0\$</span> (two-tailed)

<span class="math inline">\$\\ell\_n(\\theta; X) = \\sum \|X\_i - \\theta\| - n\\log(4\\sqrt{2})\$</span>

<span class="math inline">\$\\nabla \\ell\_n(\\theta; X) = \\sum \\text{sgn}(\\theta - X\_i) = \\sum $$\\mathbb{I}(X\_i &lt; \\theta) - \\mathbb{I}(X\_i &gt; \\theta)$$\$</span>

<span class="math inline">\$\\nabla \\ell\_n(0; X) = \\sum $$\\mathbb{I}(X\_i &lt; 0) - \\mathbb{I}(X\_i &gt; 0)$$ = \\sum \\text{sgn}(-X\_i)\$</span>

<span class="math inline">\$J\_n(0) = n/2\$</span>

<span class="math inline">\$\\sqrt{2/n} \\sum \\text{sgn}(-X\_i) \\sim N(0,1)\$</span> (sign test)

Note: this test is the exact NP/UMP test for <span class="math inline">\$H\_0: \\theta = 0\$</span> vs <span class="math inline">\$H\_0: \|\\theta\| = \\epsilon\$</span> for <span class="math inline">\$\\epsilon &gt; 0\$</span>

Intuition: Maximize power for nearby alternatives since we’ll have power for <span class="math inline">\$\\theta \\gg 0\$</span>

More generally, one-sided score test is almost UMP for nearby alternatives

<span class="math inline">\$p\_\\theta(x) \\approx p\_0(x)$$1 + \\epsilon \\ell'\_0(X)$$\$</span> for small <span class="math inline">\$\\epsilon &gt; 0\$</span>

### <span class="header-section-number">3.5</span> Example: Pearson’s <span class="math inline">\$\\chi^2\$</span> Test (Goodness of Fit) {.anchored number="3.5" anchor-id="example-pearsons-chi2-test-goodness-of-fit"}

<span class="math inline">\$N = (N\_1, \\ldots, N\_d) \\sim \\text{Multi}(n, \\pi)\$</span>, <span class="math inline">\$\\pi\_i \\geq 0\$</span>, <span class="math inline">\$\\sum \\pi\_i = 1\$</span>

<span class="math inline">\$\\ell\_n(\\pi; N) = \\sum N\_i \\log \\pi\_i\$</span>

Note <span class="math inline">\$\\mathbb{E}$$\\pi$$ = 1\$</span> so this is a full rank <span class="math inline">\$d-1\$</span> parameter exp family e.g. <span class="math inline">\$T\_j = \\mathbb{I}(\\text{category} = j)\$</span>, <span class="math inline">\$j=1,\\ldots,d-1\$</span>

<span class="math inline">\$\\nabla \\ell\_n(\\pi; N) = (N\_1/\\pi\_1, \\ldots, N\_d/\\pi\_d)^T - n1\_d\$</span>

<span class="math inline">\$\\hat{\\pi} = \\text{MLE} = (N\_1/n, \\ldots, N\_d/n)\$</span>

\$J\_n() = n\[(\_1^{-1}, , \_d^{-1})

---

[← Likelihood inference Part 03 —](03-likelihood-inference-part-03.md) · [Up: contents](index.md)
