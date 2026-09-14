---
title: Sufficiency
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Sufficiency

**Source:** [`units/reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/sufficiency.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Sufficiency is a central concept in statistics that allows us to focus on the essential aspects of the data set while ignoring details that are irrelevant to the inference problem. If <span class="math inline">\$X\\sim P\_\\theta\$</span> represents the entire data set, drawn from a model <span class="math inline">\$\\cP = \\{P\_\\theta:\\; \\theta \\in \\Theta\\}\$</span>, then this lecture will concern the idea of a *sufficient statistic* <span class="math inline">\$T(X)\$</span> that carries all of the information in the data that can help us learn about <span class="math inline">\$\\theta\$</span>.

A *statistic* <span class="math inline">\$T(X)\$</span> is any random variable which is a function of the data <span class="math inline">\$X\$</span>, and which does **not** depend on the unknown parameter <span class="math inline">\$\\theta\$</span>. We say the statistic <span class="math inline">\$T(X)\$</span> is *sufficient* for the model <span class="math inline">\$\\cP\$</span> if <span class="math inline">\$P\_\\theta(X \\mid T)\$</span> does not depend on <span class="math inline">\$\\theta\$</span>. This lecture will be devoted to interpreting this definition and giving examples.

**Example (Independent Bernoulli sequence):** We introduced the binomial example from Lecture 2 by telling a story about an investigator who flips a biased coin <span class="math inline">\$n\$</span> times and records the total number of heads, which has a binomial distribution. All of the estimators we considered were functions only of the (binomially-distributed) count of heads.

But if the investigator had actually performed this experiment, they would have observed more than just the total number of heads: they would have observed the entire sequence of <span class="math inline">\$n\$</span> heads and tails. If we let <span class="math inline">\$X\_i\$</span> denote a binary indicator of whether the <span class="math inline">\$i\$</span>th throw is heads, for <span class="math inline">\$i=1,\\ldots,n\$</span>, then we have assumed that these indicators are i.i.d. Bernoulli random variables:

<span class="math display">\\$$ X\_1,\\ldots,X\_n \\simiid \\text{Bern}(\\theta). \\$$</span>

Let <span class="math inline">\$T(X) = \\sum\_i X\_i \\sim \\text{Binom}(n,\\theta)\$</span> denote the summary statistic that we previously used to represent the entire data set. It is undeniable that we have lost some information by only recording <span class="math inline">\$T(X)\$</span> instead of the entire sequence <span class="math inline">\$X = (X\_1,\\ldots,X\_n)\$</span>. As a result, we might wonder whether we could have improved the estimator by considering all functions of <span class="math inline">\$X\$</span>, not just functions of <span class="math inline">\$T(X)\$</span>.

The answer is that, no, we did not really lose anything by summarizing the data by <span class="math inline">\$T(X)\$</span> because <span class="math inline">\$T(X)\$</span> is sufficient. The joint pmf of the data set <span class="math inline">\$X \\in \\{0,1\\}^n\$</span> (i.e., the density wrt the counting measure on <span class="math inline">\$\\{0,1\\}^n\$</span>) is

<span class="math display">\\$$ p\_\\theta(x) = \\prod\_{i=1}^n \\theta^{x\_i}(1-\\theta)^{1-x\_i} = \\theta^{\\sum\_i x\_i}(1-\\theta)^{n-\\sum\_i x\_i}. \\$$</span>

Note that this pmf depends only on <span class="math inline">\$T(x)\$</span>: it assigns probability <span class="math inline">\$\\theta^t (1-\\theta)^{n-t}\$</span> to every sequence with <span class="math inline">\$T(X)=t\$</span> total heads. As a result, the conditional distribution given <span class="math inline">\$T(X)=t\$</span> should be uniform on all of the <span class="math inline">\$\\binom{n}{t}\$</span> sequences with <span class="math inline">\$t\$</span> heads. We can confirm this by calculating the conditional pmf directly:

<span class="math display">\\$$ \\begin{aligned} \\PP\_\\theta(X = x \\mid T(X) = t) &= \\frac{\\PP\_\\theta(X=x, \\sum\_i X\_i = t)}{\\PP\_\\theta(T(X) = t)} \\\\\[7pt$$ &= \\frac{\\theta^t (1-\\theta)^{n-t}1\\{\\sum\_i x\_i = t\\}}{\\theta^t(1-\\theta)^{n-t}\\binom{n}{t}}\\\\$$5pt$$ &= \\binom{n}{t}^{-1}1\\{T(x) = t\\}. \\end{aligned} \\\]</span>

Since the conditional distribution does not depend on <span class="math inline">\$\\theta\$</span>, <span class="math inline">\$T(X)\$</span> is sufficient for the model <span class="math inline">\$\\cP\$</span>.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Visualization of sufficiency for two binomials →](03-visualization-of-sufficiency-for-two-binomials.md)
