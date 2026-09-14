---
title: 2 Confidence Regions {.anchored number="2" anchor-id="confidence-regions"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Confidence Regions {.anchored number="2" anchor-id="confidence-regions"}

**Source:** [`units/reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Definition: <span class="math inline">\$C: \\cX \\to \\cP(\\Theta)\$</span> is a <span class="math inline">\$1-\\alpha\$</span> confidence set for <span class="math inline">\$g(\\theta)\$</span> if:

<span class="math display">\\$$\\mathbb{P}\_\\theta(C(X) \\ni g(\\theta)) \\geq 1-\\alpha \\quad \\forall \\theta \\in \\Theta\\$$</span>

We say <span class="math inline">\$C(x)\$</span> covers <span class="math inline">\$g(\\theta)\$</span> if <span class="math inline">\$C(x) \\ni g(\\theta)\$</span>

Coverage probability: <span class="math inline">\$\\mathbb{P}\_\\theta(C(X) \\ni g(\\theta))\$</span>

<span class="math inline">\$\\inf\_\\theta \\mathbb{P}\_\\theta(C(X) \\ni g(\\theta))\$</span> is confidence level

Note: <span class="math inline">\$C(X)\$</span> is random, not <span class="math inline">\$g(\\theta)\$</span>

Often misinterpreted as Bayesian guarantee Say “<span class="math inline">\$C(x)\$</span> has a 95% chance of covering” Not “<span class="math inline">\$g(\\theta)\$</span> has a 95% chance of being in <span class="math inline">\$C\$</span>” NEVER “95% chance <span class="math inline">\$g(\\theta) \\in $$0.5, 1.5$$\$</span>” e.g.

### <span class="header-section-number">2.1</span> Duality of Tests/Confidence Sets {.anchored number="2.1" anchor-id="duality-of-testsconfidence-sets"}

Suppose we have a level <span class="math inline">\$\\alpha\$</span> test <span class="math inline">\$\\phi(\\cdot, a)\$</span> of <span class="math inline">\$H\_0: g(\\theta) = a\$</span> vs <span class="math inline">\$H\_1: g(\\theta) \\neq a\$</span>, <span class="math inline">\$\\forall a \\in \\Theta\$</span>

We can use it to make a confidence set for <span class="math inline">\$g(\\theta)\$</span>:

Let <span class="math inline">\$C(X) = \\{a: \\phi(X, a) = 0\\}\$</span> (all non-rejected values of <span class="math inline">\$a\$</span>)

Then <span class="math inline">\$\\mathbb{P}\_\\theta(C(X) \\ni g(\\theta)) = \\mathbb{P}\_\\theta(\\phi(X, g(\\theta)) = 0) \\geq 1-\\alpha\$</span>

Alternatively, suppose <span class="math inline">\$C(X)\$</span> is a <span class="math inline">\$1-\\alpha\$</span> confidence set for <span class="math inline">\$g(\\theta)\$</span>

We can use <span class="math inline">\$C\$</span> to construct a test <span class="math inline">\$\\phi\$</span> of <span class="math inline">\$H\_0: g(\\theta) = a\$</span> vs <span class="math inline">\$H\_1: g(\\theta) \\neq a\$</span>:

<span class="math inline">\$\\phi(x) = 1\\{a \\notin C(x)\\}\$</span>

For <span class="math inline">\$\\theta\$</span> s.t. <span class="math inline">\$g(\\theta) = a\$</span>:

<span class="math display">\\$$\\mathbb{E}\_\\theta\[\\phi(X)$$ = \\mathbb{P}\_\\theta(a \\notin C(X)) = \\mathbb{P}\_\\theta(C(X) \\not\\ni g(\\theta)) \\leq \\alpha\\\]</span>

This is called inverting a test.

### <span class="header-section-number">2.2</span> Confidence Intervals/Bounds {.anchored number="2.2" anchor-id="confidence-intervalsbounds"}

If <span class="math inline">\$C(X) = $$C\_L(X), C\_U(X)$$\$</span>, we say: - <span class="math inline">\$C(X)\$</span> is a confidence interval (CI) - <span class="math inline">\$C\_L(X)\$</span> is a lower confidence bound (LCB) - <span class="math inline">\$C\_U(X)\$</span> is an upper confidence bound (UCB)

We usually get LCB, UCB by inverting a one-sided test in appropriate direction Called uniformly most accurate (UMA) if test UMP

Get CI by inverting a two-sided test Called UMAU if test is UMPU

Example: <span class="math inline">\$X \\sim \\text{Exp}(\\theta)\$</span>, <span class="math inline">\$n=1\$</span>, <span class="math inline">\$\\mathbb{E}$$X$$ = \\frac{1}{\\theta}\$</span>, <span class="math inline">\$\\theta &gt; 0\$</span>

CDF: <span class="math inline">\$\\mathbb{P}\_\\theta(X \\leq x) = 1 - e^{-\\theta x}\$</span>

LCB: Invert test for <span class="math inline">\$H\_0: \\theta \\leq \\theta\_0\$</span> Solve <span class="math inline">\$\\alpha = 1 - \\mathbb{P}\_{\\theta\_0}(X \\leq x) = e^{-\\theta\_0 x}\$</span>

<span class="math inline">\$\\theta\_0 = -\\frac{1}{x}\\log(\\alpha)\$</span>

<span class="math inline">\$C\_L(X) = -\\frac{1}{X}\\log(\\alpha)\$</span>, <span class="math inline">\$\\mathbb{P}\_\\theta(\\theta \\geq C\_L(X)) = 1-\\alpha\$</span>

UCB: Similar <span class="math inline">\$C\_U(X) = -\\frac{1}{X}\\log(1-\\alpha)\$</span>

Equal-tailed: Invert equal-tailed test of <span class="math inline">\$H\_0: \\theta = \\theta\_0\$</span>

<span class="math inline">\$\\theta\_0 e^{-\\theta\_0 x} = \\frac{\\alpha}{2}\$</span>, <span class="math inline">\$1 - e^{-\\theta\_0 x} = 1 - \\frac{\\alpha}{2}\$</span>

<span class="math inline">\$C(X) = $$\\frac{-\\log(\\alpha/2)}{X}, \\frac{-\\log(\\alpha/2)}{X}$$\$</span>

Similar for UMPU 2-sided test

---

[← 1 p-Values {.anchored number="1" anchor-id="p-values"}](02-1-p-values-anchored-number-1-anchor-id-p-values.md) · [Up: contents](index.md) · [Testing interpretation Part 04 — →](04-testing-interpretation-part-04.md)
