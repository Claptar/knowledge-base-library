---
title: 4 The Rao-Blackwell Theorem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 The Rao-Blackwell Theorem

**Source:** [`units/reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Intuitively, convex losses punish us for using noisy estimators: we would always improve the risk if we could replace an estimator <span class="math inline">\$\\delta(X)\$</span> with its expectation: <span class="math display">\\$$L(\\theta, \\EE\_\\theta \[\\delta(X)$$) \\leq \\EE\_\\theta \\left$$L(\\theta, \\delta(X))\\right$$.\\\]</span>Generally, this is not feasible in real problems because <span class="math inline">\$\\EE\_\\theta $$\\delta(X)$$\$</span> depends on <span class="math inline">\$\\theta\$</span>, so it is not an estimator. But for any sufficient statistic <span class="math inline">\$T(X)\$</span>, the **conditional expectation** of <span class="math inline">\$\\delta(X)\$</span> given <span class="math inline">\$T(X)\$</span> really is an estimator, and it is always at least as good as <span class="math inline">\$\\delta(X\$</span>) if the loss is convex.

The next result formalizes this fact, and thereby gives decision-theoretic teeth to the sufficiency principle:

**Theorem (Rao-Blackwell):** Let <span class="math inline">\$T(X)\$</span> be sufficient for <span class="math inline">\$\\cP = \\{P\_\\theta:\\;\\theta\\in\\Theta\\}\$</span>, and let <span class="math inline">\$\\delta(X)\$</span> be any estimator for <span class="math inline">\$g(\\theta)\$</span>. Define the new estimator:

<span class="math display">\\$$\\bar{\\delta}(T(X)) = \\EE\[\\delta(X) \\mid T(X)$$\\\]</span>

Then for any convex loss <span class="math inline">\$L(\\theta, d)\$</span>, we have <span class="math inline">\$R(\\theta, \\bar{\\delta}) \\leq R(\\theta, \\delta)\$</span> for all <span class="math inline">\$\\theta\$</span>. If <span class="math inline">\$L\$</span> is strictly convex, <span class="math inline">\$\\bar{\\delta}\$</span> strictly dominates <span class="math inline">\$\\delta\$</span> as an estimator unless <span class="math inline">\$\\delta(X) \\eqPas \\bar{\\delta}(T(X))\$</span>.

*Proof:*

<span class="math display">\\$$\\begin{aligned} R(\\theta, \\bar{\\delta}) &= \\EE\_\\theta\\left\[\\,L(\\theta, \\;\\EE\[\\delta \\mid T$$)\\,\\right\]\\\\$$5pt$$ &\\leq \\EE\_\\theta\\left$$\\,\\EE\[L(\\theta, \\delta) \\mid T$$\\,\\right\]\\\\$$5pt$$ &= \\EE\_\\theta$$\\,L(\\theta, \\delta)\\,$$ \\\\$$5pt$$ &= R(\\theta, \\bar{\\delta}) \\end{aligned}\\\]</span>

<span class="math inline">\$\\bar{\\delta}\$</span> is called the Rao-Blackwellization of <span class="math inline">\$\\delta\$</span>. Note that the condition \$\\delta(X) \\eqPas \\bar{\\delta}(T(X))\$ is equivalent to the condition that <span class="math inline">\$\\delta\$</span> depends only on <span class="math inline">\$X\$</span> through <span class="math inline">\$T(X)\$</span>.

Whenever we are dealing with a convex loss, the Rao-Blackwell theorem lets us restrict our attention only to estimators that run through <span class="math inline">\$T(X)\$</span>, because any other estimator could be improved (or at least not worsened) by Rao-Blackwellization. The theorem even gives us a recipe for \*\*constructing\*\* the improved estimator.

---

[← 3 Convex Loss Functions](04-3-convex-loss-functions.md) · [Up: contents](index.md) · [5 UMVU estimators →](06-5-umvu-estimators.md)
