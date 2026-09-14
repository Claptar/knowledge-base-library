---
title: 5 UMVU estimators
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 UMVU estimators

**Source:** [`units/reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

In this section we will combine two key facts from this lecture and last concerning unbiased estimation of any estimand <span class="math inline">\$g(\\theta)\$</span>.

1.  If <span class="math inline">\$T(X)\$</span> is complete sufficient, there can be at most one unbiased estimator based on <span class="math inline">\$T(X)\$</span>.
2.  If the loss is convex, then we can restrict our attention only to estimators that are based on <span class="math inline">\$T(X)\$</span>.

Together these facts imply that, if any unbiased estimator exists at all, then there is a unique best unbiased estimator.

Not all estimands have unbiased estimators. We say <span class="math inline">\$g(\\theta)\$</span> is *U-estimable* if there exists any <span class="math inline">\$\\delta(X)\$</span> with <span class="math inline">\$\\EE\_\\theta \\delta(X) = g(\\theta)\$</span> for all <span class="math inline">\$\\theta\$</span>. This leads to the following theorem:

**Theorem:** For model <span class="math inline">\$\\mathcal{P} = \\{P\_\\theta : \\theta \\in \\Theta\\}\$</span>, assume <span class="math inline">\$T(X)\$</span> is a complete sufficient statistic. Then

1.  For any U-estimable <span class="math inline">\$g(\\theta)\$</span> there exists a unique unbiased estimator of the form <span class="math inline">\$\\delta(T(X))\$</span>.
2.  For a (strictly) convex loss, that estimator (strictly) dominates any other unbiased estimator <span class="math inline">\$\\tilde{\\delta}(X)\$</span> unless <span class="math inline">\$\\tilde{\\delta}(X) \\eqas \\delta(T(X))\$</span>.

As usual the “uniqueness” here is only up to <span class="math inline">\$\\eqPas\$</span>.

*Proof:*

$1$ Since <span class="math inline">\$g(\\theta)\$</span> is U-estimable, there exists some unbiased estimator <span class="math inline">\$\\delta\_0(X)\$</span>. Then its Rao-Blackwellization <span class="math inline">\$\\delta(T(X)) = \\EE$$\\delta\_0 \\mid T$$\$</span> is also unbiased, since

<span class="math display">\\$$ \\EE\_\\theta \\delta(T) = \\EE\_\\theta\[\\EE\[\\delta\_0 \| T$$\] = \\EE\_\\theta \\delta\_0 = g(\\theta). \\\]</span>

Any other estimator of the form <span class="math inline">\$\\tilde\\delta(T)\$</span> must be almost surely equal to <span class="math inline">\$\\delta(T)\$</span>, by completeness: if <span class="math inline">\$f(t) = \\delta(t)-\\tilde\\delta(t)\$</span>, then both estimators being unbiased means <span class="math inline">\$\\EE\_\\theta f(T) = g(\\theta)-g(\\theta) = 0\$</span>, so <span class="math inline">\$f(T(X)) \\eqas 0\$</span>. Thus, <span class="math inline">\$\\delta(T)\$</span> is unique.

$2$ The first result implies that every unbiased estimator has the same Rao-Blackwellization, namely <span class="math inline">\$\\delta(T)\$</span>. Thus, by the Rao-Blackwell theorem, <span class="math inline">\$\\delta(T)\$</span> (strictly) dominates every other unbiased estimator for any (strictly) convex loss function, unless the estimator is almost surely identical to <span class="math inline">\$\\delta\$</span>. <span class="math inline">\$\\blacksquare\$</span>

The estimator from this theorem is usually called the *UMVU (Uniformly Minimum Variance Unbiased) Estimator*. We say <span class="math inline">\$\\delta(X)\$</span> is UMVU if:

1.  <span class="math inline">\$\\delta(X)\$</span> is unbiased
2.  <span class="math inline">\$\\text{Var}\_\\theta \\,\\delta(X) \\leq \\text{Var}\_\\theta \\,\\tilde{\\delta}(X)\$</span> for all <span class="math inline">\$\\theta\$</span> and all unbiased <span class="math inline">\$\\tilde{\\delta}(X)\$</span>

Since <span class="math inline">\$\\text{MSE}(\\theta; \\delta) = \\text{Var}\_\\theta(\\delta(X))\$</span> for any unbiased estimator, and the squared error loss is strictly convex, Theorem XXX immediately implies the existence of a unique UMVU estimator for any U-estimable <span class="math inline">\$g(\\theta)\$</span>, whenever we have a complete sufficient statistic.

Note that in problems where no complete sufficient statistic exists, there can be multiple unbiased estimators based on the minimal sufficient statistic; for example, both the mean and the median are unbiased for the Laplace location parameter, but they are not almost surely equal to each other, and they do not have the same risk function.

---

[← 4 The Rao-Blackwell Theorem](05-4-the-rao-blackwell-theorem.md) · [Up: contents](index.md) · [6 Finding the UMVUE →](07-6-finding-the-umvue.md)
