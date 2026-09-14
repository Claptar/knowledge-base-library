---
title: UMVU estimators
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# UMVU estimators

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In this section we will combine two key facts from this lecture and last concerning unbiased estimation of any estimand $g(\theta)$.

1.  If $T(X)$ is complete sufficient, there can be at most one unbiased estimator based on $T(X)$.
2.  If the loss is convex, then we can restrict our attention only to estimators that are based on $T(X)$.

Together these facts imply that, if any unbiased estimator exists at all, then there is a unique best unbiased estimator.

Not all estimands have unbiased estimators. We say $g(\theta)$ is *U-estimable* if there exists any $\delta(X)$ with $\EE_\theta \delta(X) = g(\theta)$ for all $\theta$. This leads to the following theorem:

**Theorem:** For model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$, assume $T(X)$ is a complete sufficient statistic. Then

1.  For any U-estimable $g(\theta)$ there exists a unique unbiased estimator of the form $\delta(T(X))$.
2.  For a (strictly) convex loss, that estimator (strictly) dominates any other unbiased estimator $\tilde{\delta}(X)$ unless $\tilde{\delta}(X) \eqas \delta(T(X))$.

As usual the "uniqueness" here is only up to $\eqPas$.

*Proof:*

$1$ Since $g(\theta)$ is U-estimable, there exists some unbiased estimator $\delta_0(X)$. Then its Rao-Blackwellization $\delta(T(X)) = \EE[\delta_0 \mid T]$ is also unbiased, since

$$
\EE_\theta \delta(T) = \EE_\theta[\EE[\delta_0 | T]] = \EE_\theta \delta_0 = g(\theta).
$$

Any other estimator of the form $\tilde\delta(T)$ must be almost surely equal to $\delta(T)$, by completeness: if $f(t) = \delta(t)-\tilde\delta(t)$, then both estimators being unbiased means $\EE_\theta f(T) = g(\theta)-g(\theta) = 0$, so $f(T(X)) \eqas 0$. Thus, $\delta(T)$ is unique.

$2$ The first result implies that every unbiased estimator has the same Rao-Blackwellization, namely $\delta(T)$. Thus, by the Rao-Blackwell theorem, $\delta(T)$ (strictly) dominates every other unbiased estimator for any (strictly) convex loss function, unless the estimator is almost surely identical to $\delta$. $\blacksquare$

The estimator from this theorem is usually called the *UMVU (Uniformly Minimum Variance Unbiased) Estimator*. We say $\delta(X)$ is UMVU if:

1.  $\delta(X)$ is unbiased
2.  $\text{Var}_\theta \,\delta(X) \leq \text{Var}_\theta \,\tilde{\delta}(X)$ for all $\theta$ and all unbiased $\tilde{\delta}(X)$

Since $\text{MSE}(\theta; \delta) = \text{Var}_\theta(\delta(X))$ for any unbiased estimator, and the squared error loss is strictly convex, Theorem XXX immediately implies the existence of a unique UMVU estimator for any U-estimable $g(\theta)$, whenever we have a complete sufficient statistic.

Note that in problems where no complete sufficient statistic exists, there can be multiple unbiased estimators based on the minimal sufficient statistic; for example, both the mean and the median are unbiased for the Laplace location parameter, but they are not almost surely equal to each other, and they do not have the same risk function.

---

[← The Rao-Blackwell Theorem](05-the-rao-blackwell-theorem.md) · [Up: contents](index.md) · [Finding the UMVUE →](07-finding-the-umvue.md)
