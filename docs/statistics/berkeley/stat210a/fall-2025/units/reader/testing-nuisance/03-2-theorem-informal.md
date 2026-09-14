---
title: 2 Theorem (Informal)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Theorem (Informal)

**Source:** [`units/reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Let <span class="math inline">\$\\cP\$</span> be full rank exp. fam. with densities <span class="math inline">\$p\_{\\theta, \\lambda}(x) = e^{\\theta \\cdot T(x) + \\lambda \\cdot U(x) - A(\\theta, \\lambda)}h(x)\$</span>

<span class="math inline">\$\\theta \\in \\mathbb{R}^s\$</span>, <span class="math inline">\$\\lambda \\in \\mathbb{R}^r\$</span>, <span class="math inline">\$(\\theta\_0, \\lambda\_0)\$</span> possible

1.  To test <span class="math inline">\$H\_0: \\theta = \\theta\_0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq \\theta\_0\$</span>, there is a UMPU test <span class="math inline">\$\\phi(x) = \\psi(T(x), U(x))\$</span> where

    <span class="math display">\\$$\\psi(t, u) = \\begin{cases} 1 & \\text{if } t &gt; c\_2(u) \\\\ \\gamma\_2(u) & \\text{if } t = c\_2(u) \\\\ 0 & \\text{if } c\_1(u) &lt; t &lt; c\_2(u) \\\\ \\gamma\_1(u) & \\text{if } t = c\_1(u) \\\\ 1 & \\text{if } t &lt; c\_1(u) \\end{cases}\\$$</span>

    with <span class="math inline">\$\\gamma\_1, \\gamma\_2, c\_1, c\_2\$</span> chosen to make <span class="math inline">\$\\mathbb{E}\_{\\theta\_0}$$\\phi$$ = \\alpha\$</span> and <span class="math inline">\$\\mathbb{E}\_{\\theta\_0}$$T\\phi$$ = \\theta\_0\$</span>

2.  To test <span class="math inline">\$H\_0: \\theta \\leq \\theta\_0\$</span> vs <span class="math inline">\$H\_1: \\theta &gt; \\theta\_0\$</span>, there is a UMPU test <span class="math inline">\$\\phi(x) = \\psi(T(x), U(x))\$</span> where

    <span class="math display">\\$$\\psi(t, u) = \\begin{cases} 1 & \\text{if } t &gt; c(u) \\\\ \\gamma(u) & \\text{if } t = c(u) \\\\ 0 & \\text{if } t &lt; c(u) \\end{cases}\\$$</span>

    with <span class="math inline">\$\\gamma, c\$</span> chosen to make <span class="math inline">\$\\mathbb{E}\_{\\theta\_0}$$\\phi$$ = \\alpha\$</span>

Note: <span class="math inline">\$h\$</span> has disappeared from the problem.

### <span class="header-section-number">2.1</span> Example: Poisson Ratio {.anchored number="2.1" anchor-id="example-poisson-ratio"}

<span class="math inline">\$X\_i \\sim \\text{iid Poisson}(\\mu\_i)\$</span>, <span class="math inline">\$i=1,2\$</span>

<span class="math inline">\$H\_0: \\mu\_1 = \\mu\_2\$</span> vs <span class="math inline">\$H\_1: \\mu\_1 \\neq \\mu\_2\$</span>

<span class="math display">\\$$p(x) = \\frac{\\mu\_1^{x\_1} e^{-\\mu\_1}}{x\_1!} \\cdot \\frac{\\mu\_2^{x\_2} e^{-\\mu\_2}}{x\_2!} = e^{x\_1 \\log \\mu\_1 + x\_2 \\log \\mu\_2 - \\mu\_1 - \\mu\_2}\\$$</span>

Let <span class="math inline">\$\\theta = \\log \\frac{\\mu\_1}{\\mu\_2}\$</span>, <span class="math inline">\$\\lambda = \\log \\mu\_2\$</span>

<span class="math inline">\$H\_0: \\theta = 0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq 0\$</span>

Reject for conditionally large values of <span class="math inline">\$X\_1\$</span> given <span class="math inline">\$X\_1 + X\_2 = u\$</span>:

<span class="math display">\\$$P\_\\theta(X\_1 = x\_1 \| X\_1 + X\_2 = u) = \\frac{e^{\\theta x\_1}}{\\sum\_{i=0}^u e^{\\theta i}} = \\binom{u}{x\_1} \\left(\\frac{e^\\theta}{1+e^\\theta}\\right)^{x\_1} \\left(\\frac{1}{1+e^\\theta}\\right)^{u-x\_1}\\$$</span>

<span class="math inline">\$X\_1 \| X\_1 + X\_2 \\sim \\text{Binom}(u, \\frac{e^\\theta}{1+e^\\theta})\$</span>

So in the end, we do a Binomial test.

---

[← 1 Nuisance Parameters](02-1-nuisance-parameters.md) · [Up: contents](index.md) · [3 Proof Sketch →](04-3-proof-sketch.md)
