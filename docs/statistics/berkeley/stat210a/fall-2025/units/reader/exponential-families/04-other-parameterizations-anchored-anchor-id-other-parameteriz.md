---
title: Other parameterizations {.anchored anchor-id="other-parameterizations"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Other parameterizations {.anchored anchor-id="other-parameterizations"}

**Source:** [`units/reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Sometimes instead of parameterizing <span class="math inline">\$\\cP\$</span> by the natural parameter <span class="math inline">\$\\eta\$</span>, it is more convenient to parameterize the family by another parameter <span class="math inline">\$\\theta\$</span>. Then we can write the density in terms of this alternative parameterization as

<span class="math display">\\$$ p\_\\theta(x) = e^{\\eta(\\theta)'T(x) - B(\\theta)}h(x), \\quad \\text{ where } B(\\theta) = A(\\eta(\\theta)). \\$$</span>

The Poisson distribution, if indexed by the mean <span class="math inline">\$\\lambda\$</span>, is an example of such an alternative parameterization, with <span class="math inline">\$\\eta(\\lambda) = \\log\\lambda\$</span> and <span class="math inline">\$B(\\lambda) = \\lambda\$</span>. Another example is the normal family:

**Example (Normal):** Consider the model <span class="math inline">\$X\\sim \\cN(\\mu, \\sigma^2)\$</span>, for <span class="math inline">\$\\mu\\in\\RR\$</span> and <span class="math inline">\$\\sigma^2&gt;0\$</span>. The usual parameter vector for this problem is <span class="math inline">\$\\theta = (\\mu, \\sigma^2)\$</span>. The density in that parameterization is

<span class="math display">\\$$ p\_\\theta(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}} \\exp\\left\\{-(\\mu-x)^2/2\\sigma^2\\right\\}. \\$$</span>

Expanding the square and raising the <span class="math inline">\$\\sqrt{2\\pi\\sigma^2}\$</span> into the exponent, we can massage the density into the exponential family structure we are looking for:

<span class="math display">\\$$ p\_\\theta(x) = \\exp\\left\\{\\frac{\\mu}{\\sigma^2} x - \\frac{1}{2\\sigma^2}x^2 - \\frac{\\mu}{2\\sigma^2} - \\frac{1}{2}\\log\\left(2\\pi\\sigma^2\\right)\\right\\}, \\$$</span>

which we can recognize as an exponential family with sufficient statistic <span class="math inline">\$T(x) = (x,x^2)\$</span>, natural parameter <span class="math inline">\$\\eta(\\theta) = (\\mu/\\sigma^2,-1/2\\sigma^2)\$</span>, carrier density <span class="math inline">\$h(x)=1\$</span>, and log-partition function

<span class="math display">\\$$ B(\\theta) = \\frac{\\mu^2}{2\\sigma^2} + \\frac{1}{2}\\log\\left(2\\pi\\sigma^2\\right). \\$$</span>

We can rewrite the log-partition function in terms of <span class="math inline">\$\\eta\_1 = \\mu^2/2\\sigma^2\$</span> and <span class="math inline">\$\\eta\_2=-1/2\\sigma^2\$</span> to complete the natural parameterization:

<span class="math display">\\$$ p\_\\eta(x) = e^{\\eta'T(x) - A(\\eta)}, \\quad \\text{ for } A(\\eta) = \\frac{-\\eta\_1^2}{4\\eta\_2} + \\frac{1}{2}\\log(-\\pi/\\eta\_2) \\$$</span>

Hence, the Gaussian is the (only) exponential family with sufficient statistic <span class="math inline">\$T(x) = (x,x^2)\$</span>, and carrier density <span class="math inline">\$h(x)=1\$</span>, with respect to the Lebesgue measure on <span class="math inline">\$\\RR\$</span>.

**Example (Binomial):** Next, consider the model <span class="math inline">\$X \\sim \\text{Binom}(n,\\theta)\$</span>, which has pmf

<span class="math display">\\$$ p\_\\theta(x) = \\theta^x (1-\\theta)^{n-x}\\binom{n}{x}. \\$$</span>

We can again massage this into canonical form by raising the parameters into the exponent and collecting terms

<span class="math display">\\$$ \\begin{aligned} p\_\\theta(x) &= \\exp\\left\\{x\\log\\theta + (n-x)\\log(1-\\theta)\\right\\}\\binom{n}{x}\\\\ &= \\exp\\left\\{x\\log\\left(\\frac{\\theta}{1-\\theta}\\right)-n\\log(1-\\theta)\\right\\}\\binom{n}{x}, \\end{aligned} \\$$</span>

which we recognize as an exponential family structure with <span class="math inline">\$T(x)=x\$</span>, natural parameter <span class="math inline">\$\\eta=\\log\\left(\\frac{\\theta}{1-\\theta}\\right)\$</span> The natural parameter <span class="math inline">\$\\eta\$</span> is called the *log-odds* or *logit*, which is used in classification models such as logistic regression and the many extensions thereof.

**Example (Beta):** The Beta distribution is a common family of distributions on the unit interval. If <span class="math inline">\$X \\sim \\text{Beta}(\\alpha,\\beta)\$</span> then <span class="math inline">\$X\$</span> has pdf

<span class="math display">\\$$ \\begin{aligned} p\_{\\alpha,\\beta}(x) &= \\frac{x^{\\alpha-1}(1-x)^{\\beta-1}}{B(\\alpha,\\beta)}\\\\\[5pt$$ &= \\exp\\{\\alpha \\log x + \\beta\\log (1-x) - \\log B(\\alpha,\\beta)\\}\\cdot \\frac{1}{x(1-x)}, \\end{aligned} \\\]</span>

where <span class="math inline">\$B(\\alpha,\\beta) = \\int\_0^1 t^{\\alpha-1}(1-t)^{\\beta-1}\\td t\$</span> is called the *beta function*. We recognize this as an exponential family with <span class="math inline">\$T(x) = (\\log x, \\log(1-x))\$</span>, <span class="math inline">\$\\eta = (\\alpha,\\beta)\$</span>, and <span class="math inline">\$h(x) = \\frac{1}{x(1-x)}\$</span>, though as always there are other ways to decompose the density.

In addition to these examples, we could add most of the distributional families detailed on Wikipedia: the Gamma, multinomial, Dirichlet, Pareto, Wishart, and many others. We will see more exponential family examples throughout the course.

---

[← Differential identities {.anchored anchor-id="differential-identities"}](03-differential-identities-anchored-anchor-id-differential-iden.md) · [Up: contents](index.md) · [Exponential tilting {.anchored anchor-id="exponential-tilting"} →](05-exponential-tilting-anchored-anchor-id-exponential-tilting.md)
