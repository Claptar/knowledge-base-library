---
title: 6 Finding the UMVUE {.anchored number="6" anchor-id="finding-the-umvue"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 6 Finding the UMVUE {.anchored number="6" anchor-id="finding-the-umvue"}

**Source:** [`units/reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Theorem XXX suggests two strategies for finding the UMVUE:

1.  Solve directly for an unbiased estimator based on <span class="math inline">\$T\$</span>
2.  Find any unbiased estimator at all, then Rao-Blackwellize it

We give examples of both strategies below:

**Example (Poisson):** Let <span class="math inline">\$X\_1, \\ldots, X\_n \\sim \\text{Pois}(\\theta)\$</span>, <span class="math inline">\$g(\\theta) = e^{-\\theta}\$</span> and consider unbiased estimation for <span class="math inline">\$g(\\theta) = \\theta^2\$</span>.

The complete sufficient statistic for the model is

<span class="math display">\\$$T(X) = \\sum X\_i \\sim \\text{Pois}(n\\theta),\\$$</span> and its probability mass function for <span class="math inline">\$t \\geq 0\$</span> is <span class="math display">\\$$ p\_\\theta(t) = \\frac{e^{-n\\theta} (n\\theta)^t}{t!} \\$$</span> **Strategy 1**

If there is some unbiased estimator <span class="math inline">\$\\delta(t)\$</span>, we can try to solve for it by setting its expectation equal to <span class="math inline">\$\\theta^2\$</span>: <span class="math display">\\$$ \\theta^2 = \\EE\_\\theta \\delta(T) = \\sum\_{t=0}^\\infty \\delta(t) \\frac{e^{-n\\theta} (n\\theta)^t}{t!}. \\$$</span> Rearranging factors, we obtain matching power series: <span class="math display">\\$$ \\sum\_{t=0}^\\infty \\delta(t) \\frac{n^t \\theta^t}{t!} = e^{n\\theta}\\theta^2 = \\sum\_{k=0}^\\infty \\frac{n^k\\theta^{k+2}}{k!}. \\$$</span> We will choose the coefficients on the left-hand side to match terms. First, change the index for the left-hand sum to <span class="math inline">\$t = k+2\$</span>: <span class="math display">\\$$ \\sum\_{t=0}^\\infty \\delta(t) \\frac{n^t \\theta^t}{t!} = e^{n\\theta}\\theta^2 = \\sum\_{t=2}^\\infty \\frac{n^{t-2}\\theta^{t}}{(t-2)!}. \\$$</span> To match the terms, we can set <span class="math inline">\$\\delta(0)=\\delta(1)=0\$</span>, and for <span class="math inline">\$t\\geq 2\$</span>, set <span class="math inline">\$\\delta(t)=\\frac{t!}{n^2(t-2)!}=\\frac{t(t-1)}{n^2}\$</span>. The same expression works for both, so we obtain the estimator <span class="math display">\\$$ \\delta(T) = \\frac{T(T-1)}{n^2} \\$$</span>

**Strategy 2:**

Alternatively, we can find an unbiased estimator and Rao-Blackwellize it. If \$n\$, we can use the fact that

<span class="math display">\\$$ \\EE\_\\theta \[X\_1 X\_2$$ = \\EE\_\\theta $$X\_1$$ \\;\\cdot\\; \\EE\_\\theta $$X\_2$$ = \\theta^2 \\\]</span> to obtain an initial unbiased estimator <span class="math inline">\$\\delta\_0(X) = X\_1X\_2\$</span>, which we will Rao-Blackwellize.

Conditional on \$

to match the terms

<span class="math inline">\$\\delta(T) = (1 - 1/n)^T\$</span> unbiased:

<span class="math display">\\$$\\begin{aligned} \\EE\_\\theta \\delta(T) &= \\sum\_{t=0}^\\infty (1-1/n)^t e^{-n\\theta} (n\\theta)^t / t! \\\\ &= e^{-n\\theta} \\sum\_{t=0}^\\infty ((n-1)\\theta)^t / t! \\\\ &= e^{-n\\theta} e^{(n-1)\\theta} = e^{-\\theta} \\end{aligned}\\$$</span>

Alternatively, we could Rao-Blackwellize <span class="math inline">\$\\delta\_0(X) = I(X\_1 = 0)\$</span>:

<span class="math display">\\$$\\begin{aligned} \\EE\[I(X\_1 = 0) \| T$$ &= \\PP(X\_1 = 0 \| T) \\\\ &= \\frac{\\PP(X\_1 = 0, X\_2 + \\cdots + X\_n = T)}{\\PP(X\_2 + \\cdots + X\_n = T-1) + \\PP(X\_2 + \\cdots + X\_n = T)} \\\\ &= \\frac{\\binom{n-1}{T} (1/n)^0 (1-1/n)^T}{\\binom{n-1}{T-1} (1/n) (1-1/n)^{T-1} + \\binom{n-1}{T} (1-1/n)^T} \\\\ &= \\frac{(1-1/n)^T}{T/n + (1-1/n)^T} \\\\ &= (1-1/n)^T \\end{aligned}\\\]</span>

**Example:** <span class="math inline">\$X\_1, \\ldots, X\_n \\sim U$$0, \\theta$$\$</span>, <span class="math inline">\$\\theta &gt; 0\$</span>

<span class="math inline">\$T = X\_{(n)}\$</span> complete sufficient

<span class="math inline">\$p\_\\theta(t) = n t^{n-1} / \\theta^n \\cdot I(0 &lt; t &lt; \\theta)\$</span>

<span class="math inline">\$\\EE\_\\theta$$T$$ = \\frac{n}{n+1} \\theta\$</span>

<span class="math inline">\$T \\cdot \\frac{n+1}{n}\$</span> is UMVUE

Alternatively, <span class="math inline">\$2X\_1\$</span> is unbiased:

<span class="math display">\\$$\\EE\[2X\_1 \| T$$ = 2T \\cdot \\frac{n+1}{2n} = T \\cdot \\frac{n+1}{n}\\\]</span>

Actually, <span class="math inline">\$T\$</span> is inadmissible too! Keener shows <span class="math inline">\$\\frac{n-1}{n} T\$</span> has better MSE for any estimator <span class="math inline">\$c \\cdot T\$</span>.

This raises the question: why do we require zero bias?

The UMVUE is often inefficient, inadmissible, or just dumb in cases where another approach makes much more sense.

**Example:** <span class="math inline">\$X \\sim \\text{Bin}(1000, \\theta)\$</span>

Estimate <span class="math inline">\$g(\\theta) = I(\\theta &gt; 0.5)\$</span>

UMVUE is <span class="math inline">\$I(X &gt; 500)\$</span>. Why?

- <span class="math inline">\$X = 500\$</span>: Conclude <span class="math inline">\$g(\\theta) = 1\$</span>
- <span class="math inline">\$X = 499\$</span>: Conclude <span class="math inline">\$g(\\theta) = 0\$</span>

This is not epistemically reasonable. Could do much better with e.g. MLE or a Bayes estimator.

In fact, our theorem should make us suspicious of UMVUEs: every idiotic function of <span class="math inline">\$T\$</span> is a UMVUE of its own expectation!

**Example:** <span class="math inline">\$X\_1, \\ldots, X\_n \\sim N(\\mu, 1)\$</span>, estimate <span class="math inline">\$g(\\mu) = \\\|\\mu\\\|\$</span>

<span class="math inline">\$\\bar{X}\$</span> is complete sufficient

<span class="math inline">\$\\\|\\bar{X}\\\|\$</span> is unbiased: <span class="math inline">\$\\EE$$\\\|\\bar{X}\\\|$$ = \\EE$$\\\|N(\\mu, 1/n)\\\|$$ = \\\|\\mu\\\|\$</span>

So <span class="math inline">\$\\\|\\bar{X}\\\|\$</span> is UMVUE

If <span class="math inline">\$\\mu = 0\$</span>, <span class="math inline">\$\\delta(\\bar{X}) = 0\$</span> about half the time

<span class="math inline">\$\\\|\\bar{X}\\\| + d \\cdot \\max(0, \\\|\\bar{X}\\\| - d)\$</span> strictly dominates UMVUE

---

[← 5 UMVU estimators {.anchored number="5" anchor-id="umvu-estimators"}](06-5-umvu-estimators-anchored-number-5-anchor-id-umvu-estimator.md) · [Up: contents](index.md)
