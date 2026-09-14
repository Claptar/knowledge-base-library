---
title: 1 Nuisance Parameters
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Nuisance Parameters

**Source:** [`units/reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">1.1</span> Common Setup {.anchored number="1.1" anchor-id="common-setup"}

Extra unknown parameters which are not of direct interest:

<span class="math inline">\$\\cP = \\{P\_{\\theta, \\lambda}: \\theta \\in \\Theta, \\lambda \\in \\Lambda\\}\$</span>

<span class="math inline">\$H\_0: \\theta \\in \\Theta\_0\$</span> vs <span class="math inline">\$H\_1: \\theta \\in \\Theta\_1\$</span>

- <span class="math inline">\$\\theta\$</span>: parameter of interest
- <span class="math inline">\$\\lambda\$</span>: nuisance parameter

Issue: <span class="math inline">\$\\lambda\$</span> unknown but might affect type I error or power of a given test

### <span class="header-section-number">1.2</span> Examples {.anchored number="1.2" anchor-id="examples"}

1.  <span class="math inline">\$X\_1, \\ldots, X\_n \\sim \\text{iid } N(\\mu, \\sigma^2)\$</span>, <span class="math inline">\$Y\_1, \\ldots, Y\_m \\sim \\text{iid } N(\\nu, \\sigma^2)\$</span> <span class="math inline">\$\\mu, \\nu, \\sigma^2\$</span> unknown <span class="math inline">\$H\_0: \\mu = \\nu\$</span> vs <span class="math inline">\$H\_1: \\mu \\neq \\nu\$</span> <span class="math inline">\$\\theta = \\mu - \\nu\$</span>, <span class="math inline">\$\\lambda = (\\mu + \\nu, \\sigma^2)\$</span> or <span class="math inline">\$(\\mu, \\sigma^2)\$</span>

2.  <span class="math inline">\$X \\sim \\text{Binom}(n\_1, \\pi\_1)\$</span>, <span class="math inline">\$X\_2 \\sim \\text{Binom}(n\_2, \\pi\_2)\$</span> <span class="math inline">\$n\_1, n\_2\$</span> known (not nuisance parameters) <span class="math inline">\$H\_0: \\pi\_1 = \\pi\_2\$</span> vs <span class="math inline">\$H\_1: \\pi\_1 \\neq \\pi\_2\$</span>

3.  <span class="math inline">\$X \\sim N(\\mu, \\sigma^2)\$</span>, <span class="math inline">\$\\theta \\in \\mathbb{R}\$</span>, <span class="math inline">\$\\lambda \\in \\mathbb{R}\$</span>, both unknown How to test <span class="math inline">\$H\_0: \\theta = 0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq 0\$</span>?

### <span class="header-section-number">1.3</span> Idea: Condition on Sufficient Statistic for <span class="math inline">\$\\lambda\$</span> {.anchored number="1.3" anchor-id="idea-condition-on-sufficient-statistic-for-lambda"}

Condition on <span class="math inline">\$U(X)\$</span> to eliminate dependence on <span class="math inline">\$\\lambda\$</span>

<span class="math display">\\$$p\_{\\theta, \\lambda}(t\|u) = \\frac{p\_{\\theta, \\lambda}(t, u)}{p\_{\\lambda}(u)} = \\frac{e^{\\theta \\cdot t} g\_\\lambda(t, u)}{\\int e^{\\theta \\cdot s} g\_\\lambda(s, u) ds}\\$$</span>

Evaluate <span class="math inline">\$H\_0: \\theta \\in \\Theta\_0\$</span> vs <span class="math inline">\$H\_1: \\theta \\in \\Theta\_1\$</span> in s-parameter model <span class="math inline">\$\\{p\_\\theta(\\cdot\|u): \\theta \\in \\Theta\\}\$</span>

Note: If <span class="math inline">\$s=1\$</span>, this family has MLR in <span class="math inline">\$T\$</span>. Even if <span class="math inline">\$s&gt;1\$</span>, we have still gotten rid of <span class="math inline">\$\\lambda\$</span>.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Theorem (Informal) →](03-2-theorem-informal.md)
