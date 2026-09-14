---
title: 3 The Rao-Blackwell Theorem {.anchored number="3" anchor-id="the-rao-blackwell-theorem"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 The Rao-Blackwell Theorem {.anchored number="3" anchor-id="the-rao-blackwell-theorem"}

**Source:** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Intuitively, convex losses punish us for using noisy estimators: we would always improve the risk if we could replace an estimator <span class="math inline">\$\\delta(X)\$</span> with its expectation: <span class="math display">\\$$L(\\theta, \\EE\_\\theta \[\\delta(X)$$) \\leq \\EE\_\\theta \\left$$L(\\theta, \\delta(X))\\right$$.\\\]</span>Generally, this is not feasible in real problems because <span class="math inline">\$\\EE\_\\theta $$\\delta(X)$$\$</span> depends on <span class="math inline">\$\\theta\$</span>, so it is not an estimator. But for any sufficient statistic <span class="math inline">\$T(X)\$</span>, the **conditional expectation** of <span class="math inline">\$\\delta(X)\$</span> given <span class="math inline">\$T(X)\$</span> really is an estimator, and it is always at least as good as <span class="math inline">\$\\delta(X\$</span>) if the loss is convex.

The next result formalizes this fact, and thereby gives decision-theoretic teeth to the sufficiency principle:

**Theorem (Rao-Blackwell):** Let <span class="math inline">\$T(X)\$</span> be sufficient for <span class="math inline">\$\\cP = \\{P\_\\theta:\\;\\theta\\in\\Theta\\}\$</span>, and let <span class="math inline">\$\\delta(X)\$</span> be any estimator for <span class="math inline">\$g(\\theta)\$</span>. Define the new estimator:

<span class="math display">\\$$\\bar{\\delta}(T(X)) = \\EE\[\\delta(X) \\mid T(X)$$\\\]</span>

Then for any convex loss <span class="math inline">\$L(\\theta, d)\$</span>, we have <span class="math inline">\$R(\\theta, \\bar{\\delta}) \\leq R(\\theta, \\delta)\$</span> for all <span class="math inline">\$\\theta\$</span>. If <span class="math inline">\$L\$</span> is strictly convex, <span class="math inline">\$\\bar{\\delta}\$</span> strictly dominates <span class="math inline">\$\\delta\$</span> as an estimator unless <span class="math inline">\$\\delta(X) \\eqPas \\bar{\\delta}(T(X))\$</span>.

*Proof:* Conditioning on <span class="math inline">\$T(X)\$</span>, we have

<span class="math display">\\$$\\begin{aligned} L(\\theta, \\bar{\\delta}(T(X)))\\;=\\;L(\\theta, \\;\\EE\[\\delta \\mid T(X)$$)\\;\\leq \\;\\EE$$L(\\theta, \\delta) \\mid T(X)$$, \\end{aligned}\\\]</span>

where we apply Jensen’s inequality in the last step. Marginalizing over <span class="math inline">\$T\$</span> gives the desired result. If we assume further that <span class="math inline">\$L\$</span> is strictly convex, the inequality becomes strict unless <span class="math inline">\$\\delta(X) = \\delta(T(X))\$</span> almost surely.

<span class="math inline">\$\\bar{\\delta}\$</span> is called a Rao-Blackwellization of <span class="math inline">\$\\delta\$</span>. Note that the condition <span class="math inline">\$\\delta(X) \\eqPas \\bar{\\delta}(T(X))\$</span> is equivalent to the condition that <span class="math inline">\$\\delta\$</span> depends only on <span class="math inline">\$X\$</span> through <span class="math inline">\$T(X)\$</span>.

Whenever we are dealing with a convex loss, the Rao-Blackwell theorem lets us restrict our attention only to estimators that run through <span class="math inline">\$T(X)\$</span>, because any other estimator could be improved (or at least not worsened) by Rao-Blackwellization. The theorem even gives us a recipe for **constructing** the improved estimator.

---

[← 2 Convex Loss Functions {.anchored number="2" anchor-id="convex-loss-functions"}](03-2-convex-loss-functions-anchored-number-2-anchor-id-convex-l.md) · [Up: contents](index.md) · [4 UMVU estimators {.anchored number="4" anchor-id="umvu-estimators"} →](05-4-umvu-estimators-anchored-number-4-anchor-id-umvu-estimator.md)
