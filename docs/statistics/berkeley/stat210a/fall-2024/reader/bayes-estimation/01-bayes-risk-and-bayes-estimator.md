---
title: Bayes Risk and Bayes Estimator
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/bayes-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/bayes-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Bayes Risk and Bayes Estimator

### Definitions

The Bayes risk is the average case risk:

$$
r(\pi, \delta) = \EE_\pi[R(\theta, \delta)] = \int R(\theta, \delta) \,d\pi(\theta)
$$

where $\pi(\theta)$ is a probability measure (for now, we assume it's proper; later we will allow it to be improper).

Note: $\pi$ and $\delta$ are functionally equivalent for average risk, which makes sense even if we don't believe $\pi$.

$$
r(\pi, \delta) = \EE_\pi[\EE_\theta[L(\theta, \delta(X))]] = \EE[L(\theta, \delta(X))]
$$

where $(\theta, X) \sim p(\theta, x) = p(x|\theta)\pi(\theta)$

An estimator $\delta$ minimizing $r_\text{Bayes}(\delta)$ is called a Bayes estimator. It depends on $\pi$ and $L$.

$$
\delta_\pi = \argmin_\delta \EE[L(\theta, \delta(X))]
$$

### Prior and Posterior

- The usual interpretation of $\pi$ is the prior belief about $\theta$ before seeing the data.
- The conditional distribution $\pi(\theta|X)$ is called the posterior distribution (belief after seeing the data).

Densities:
- Prior: $\pi(\theta)$
- Likelihood: $p(x|\theta)$
- Joint density: $p(\theta, x) = \pi(\theta)p(x|\theta)$
- Marginal density: $q(x) = \int p(\theta, x) \,d\theta$
- Posterior density: $\pi(\theta|x) = \frac{p(\theta, x)}{q(x)}$

The Bayes estimator depends on the posterior:

$$
\delta_\pi(x) = \argmin_d \EE[L(\theta, d)|X=x] = \argmin_d \int L(\theta, d) \pi(\theta|x) \,d\theta
$$

### Theorem: Characterization of Bayes Estimators

Suppose $X \sim p_\theta(x)$ and $\delta_\pi(x) = \delta(x)$ for some function $\delta$. Then $\delta$ is Bayes with respect to $\pi$ if and only if $\delta(x) \in \argmin_d \EE[L(\theta, d)|X=x]$ for almost every $x$.

Proof:
1. Let $\delta'$ be any other estimator.
2. $r(\pi, \delta') = \int \EE[L(\theta, \delta'(X))|X=x] q(x) \,dx$
3. $r(\pi, \delta) = \int \EE[L(\theta, \delta(X))|X=x] q(x) \,dx$
4. Define $E_x(d) = \EE[L(\theta, d)|X=x]$
5. If $\delta(x) \in \argmin_d E_x(d)$, then $E_x(\delta(x)) \leq E_x(\delta'(x))$ for all $x$
6. This implies $r(\pi, \delta) \leq r(\pi, \delta')$

## Special Cases and Examples

### Squared Error Loss

If $L(\theta, d) = (\theta - d)^2$, then the Bayes estimator is the posterior mean:

$$
\delta_\pi(x) = \EE[\theta|X=x]
$$

Proof:
$$
\begin{aligned}
\EE[(\theta - d)^2|X=x] &= \EE[\theta^2|X=x] - 2d\EE[\theta|X=x] + d^2 \\
&= \Var(\theta|X=x) + (\EE[\theta|X=x] - d)^2 + \EE[\theta|X=x]^2 - 2d\EE[\theta|X=x] + d^2
\end{aligned}
$$

The minimum occurs when $d = \EE[\theta|X=x]$.

### Weighted Squared Error

For $L(\theta, d) = w(\theta)(\theta - d)^2$ (e.g., squared relative error), the Bayes estimator is:

$$
\delta_\pi(x) = \frac{\EE[w(\theta)\theta|X=x]}{\EE[w(\theta)|X=x]}
$$

---

[Up: contents](index.md) · [Examples →](02-examples.md)
