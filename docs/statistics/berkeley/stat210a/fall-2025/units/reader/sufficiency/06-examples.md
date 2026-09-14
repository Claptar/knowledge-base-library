---
title: Examples
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Examples

**Source:** [`units/reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Some initial examples:

**Example: Normal location family** Assume we observe an i.i.d. sample from a normal distribution with unit variance and unknown mean:

<span class="math display">\\$$ X\_1,\\ldots,X\_n \\simiid N(\\theta,1) = \\frac{1}{\\sqrt{2\\pi}} e^{-(x-\\theta)^2/2} = \\frac{1}{\\sqrt{2\\pi}} e^{-x^2/2 + \\theta x - \\theta^2/2} \\$$</span>

The joint density function for the full data set <span class="math inline">\$X = (X\_1,\\ldots,X\_n)\$</span> over <span class="math inline">\$\\RR^n\$</span> is

<span class="math display">\\$$ \\begin{aligned} p\_\\theta(x) &= (2\\pi)^{-n/2} \\cdot \\prod\_{i=1}^n e^{-x\_i^2/2 + \\theta x\_i - \\theta^2/2}\\\\\[7pt$$ &= \\underbrace{e^{\\theta \\left(\\sum\_i x\_i\\right) -n\\theta^2/2}}\_{g\_\\theta\\left(\\sum\_i x\_i\\right)}\\cdot \\underbrace{\\frac{\\prod\_{i=1}^n e^{-x\_i^2/2}}{(2\\pi)^{-n/2}}}\_{h(x)}, \\end{aligned} \\\]</span> which by the factorization theorem shows that <span class="math inline">\$\\sum\_i X\_i\$</span> is sufficient.

**Example: Poisson family** Next assume we observe an i.i.d. sample from a Poisson distribution with unknown mean <span class="math inline">\$\\theta\$</span>:

<span class="math display">\\$$ X\_1,\\ldots,X\_n \\simiid \\text{Pois}(\\theta) = \\frac{\\theta^x e^{-\\theta}}{x!}, \\quad \\text{ for } x = 0,1,\\ldots \\$$</span> The joint pmf for the full data set <span class="math inline">\$X = (X\_1,\\ldots,X\_n)\$</span> over <span class="math inline">\$\\{0,1,\\ldots\\}^n\$</span> is

<span class="math display">\\$$ \\begin{aligned} p\_\\theta(x) &= \\prod\_{i=1}^n \\frac{\\theta^{x\_i}e^{-\\theta}}{x\_i!}\\\\\[7pt$$ &= \\underbrace{e^{\\theta \\left(\\sum\_i x\_i\\right) -n\\theta}}\_{g\_\\theta\\left(\\sum\_i x\_i\\right)}\\cdot \\underbrace{\\left(\\prod\_{i=1}^n x\_i!\\right)^{-1}}\_{h(x)}, \\end{aligned} \\\]</span> Showing once again that <span class="math inline">\$T(X) = \\sum\_i X\_i\$</span> is sufficient. As we’ll find out in the next lecture, there is a good reason why these calculations turned out so similarly: both of these models have what is called an *exponential family* structure.

**Example: Uniform location family** As a third example, suppose we observe an i.i.d. sample from a uniform distribution on the interval <span class="math inline">\$$$\\theta, \\theta + 1$$\$</span>:

<span class="math display">\\$$ X\_1,\\ldots, X\_n \\simiid U\[\\theta, \\theta+1$$ = 1\\{\\theta \\leq x \\leq \\theta + 1\\}. \\\]</span> The joint density function for the full data set is

<span class="math display">\\$$ p\_\\theta(x) = \\prod\_{i=1}^n 1\\{\\theta \\leq x \\leq \\theta + 1} = 1\\{\\theta \\leq \\min\_i x\_i\\} 1\\{\\max\_i x\_i \\leq \\theta + 1\\}, \\$$</span> so <span class="math inline">\$T(X) = (\\min\_i X\_i, \\max\_i X\_i)\$</span> is sufficient.

---

[← Statement for general \$\\cX\$](05-statement-for-general.md) · [Up: contents](index.md) · [Interpretations of sufficiency →](07-interpretations-of-sufficiency.md)
