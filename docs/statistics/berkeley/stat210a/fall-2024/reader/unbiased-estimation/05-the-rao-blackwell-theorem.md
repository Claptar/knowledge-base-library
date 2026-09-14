---
title: The Rao-Blackwell Theorem
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The Rao-Blackwell Theorem

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Intuitively, convex losses punish us for using noisy estimators: we would always improve the risk if we could replace an estimator $\delta(X)$ with its expectation: $$L(\theta, \EE_\theta [\delta(X)]) \leq \EE_\theta \left[L(\theta, \delta(X))\right].$$Generally, this is not feasible in real problems because $\EE_\theta [\delta(X)]$ depends on $\theta$, so it is not an estimator. But for any sufficient statistic $T(X)$, the **conditional expectation** of $\delta(X)$ given $T(X)$ really is an estimator, and it is always at least as good as $\delta(X$) if the loss is convex.

The next result formalizes this fact, and thereby gives decision-theoretic teeth to the sufficiency principle:

**Theorem (Rao-Blackwell):** Let $T(X)$ be sufficient for $\cP = \{P_\theta:\;\theta\in\Theta\}$, and let $\delta(X)$ be any estimator for $g(\theta)$. Define the new estimator:

$$\bar{\delta}(T(X)) = \EE[\delta(X) \mid T(X)]$$

Then for any convex loss $L(\theta, d)$, we have $R(\theta, \bar{\delta}) \leq R(\theta, \delta)$ for all $\theta$. If $L$ is strictly convex, $\bar{\delta}$ strictly dominates $\delta$ as an estimator unless $\delta(X) \eqPas \bar{\delta}(T(X))$.

*Proof:*

$$\begin{aligned}
R(\theta, \bar{\delta}) &= \EE_\theta\left[\,L(\theta, \;\EE[\delta \mid T])\,\right]\\[5pt]
&\leq \EE_\theta\left[\,\EE[L(\theta, \delta) \mid T]\,\right]\\[5pt]
&= \EE_\theta[\,L(\theta, \delta)\,] \\[5pt]
&= R(\theta, \bar{\delta})
\end{aligned}$$

$\bar{\delta}$ is called the Rao-Blackwellization of $\delta$. Note that the condition \$\\delta(X) \\eqPas \\bar{\\delta}(T(X))\$ is equivalent to the condition that $\delta$ depends only on $X$ through $T(X)$.

Whenever we are dealing with a convex loss, the Rao-Blackwell theorem lets us restrict our attention only to estimators that run through $T(X)$, because any other estimator could be improved (or at least not worsened) by Rao-Blackwellization. The theorem even gives us a recipe for \*\*constructing\*\* the improved estimator.

---

[← Convex Loss Functions](04-convex-loss-functions.md) · [Up: contents](index.md) · [UMVU estimators →](06-umvu-estimators.md)
