---
title: 3 The Rao-Blackwell Theorem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 The Rao-Blackwell Theorem

Intuitively, convex losses punish us for using noisy estimators: we would always improve the risk if we could replace an estimator $\delta(X)$ with its expectation:

$$
L(\theta, \EE_\theta [\delta(X)]) \leq \EE_\theta \left[L(\theta, \delta(X))\right].
$$

Generally, this is not feasible in real problems because $\EE_\theta [\delta(X)]$ depends on $\theta$, so it is not an estimator. But for any sufficient statistic $T(X)$, the **conditional expectation** of $\delta(X)$ given $T(X)$ really is an estimator, and it is always at least as good as $\delta(X$) if the loss is convex.

The next result formalizes this fact, and thereby gives decision-theoretic teeth to the sufficiency principle:

**Theorem (Rao-Blackwell):** Let $T(X)$ be sufficient for $\cP = \{P_\theta:\;\theta\in\Theta\}$, and let $\delta(X)$ be any estimator for $g(\theta)$. Define the new estimator:

$$
\bar{\delta}(T(X)) = \EE[\delta(X) \mid T(X)]
$$

Then for any convex loss $L(\theta, d)$, we have $R(\theta, \bar{\delta}) \leq R(\theta, \delta)$ for all $\theta$. If $L$ is strictly convex, $\bar{\delta}$ strictly dominates $\delta$ as an estimator unless $\delta(X) \eqPas \bar{\delta}(T(X))$.

*Proof:* Conditioning on $T(X)$, we have

$$
\begin{aligned}
L(\theta, \bar{\delta}(T(X)))\;=\;L(\theta, \;\EE[\delta \mid T(X)])\;\leq \;\EE[L(\theta, \delta) \mid T(X)],
\end{aligned}
$$

where we apply Jensen’s inequality in the last step. Marginalizing over $T$ gives the desired result. If we assume further that $L$ is strictly convex, the inequality becomes strict unless $\delta(X) = \delta(T(X))$ almost surely.

$\bar{\delta}$ is called a Rao-Blackwellization of $\delta$. Note that the condition $\delta(X) \eqPas \bar{\delta}(T(X))$ is equivalent to the condition that $\delta$ depends only on $X$ through $T(X)$.

Whenever we are dealing with a convex loss, the Rao-Blackwell theorem lets us restrict our attention only to estimators that run through $T(X)$, because any other estimator could be improved (or at least not worsened) by Rao-Blackwellization. The theorem even gives us a recipe for **constructing** the improved estimator.

---

[← 2 Convex Loss Functions](02-2-convex-loss-functions.md) · [Up: contents](index.md) · [4 UMVU estimators →](04-4-umvu-estimators.md)
