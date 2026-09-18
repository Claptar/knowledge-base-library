---
title: 4 James-Stein Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4 James-Stein Estimator

$$
\delta_{JS}(X) = (1 - \frac{d-2}{\|X\|^2})X
$$

Proof: If $Y \sim \text{Gamma}(\frac{d}{2}, \frac{1}{2})$, then:

$$
\mathbb{P}(Y > \frac{d-2}{2}) = 1
$$

Now use $f(x) = x - \frac{d-2}{x}$, $\frac{1}{2}\|X\|^2 \sim \text{Gamma}(\frac{d}{2}, \frac{1}{2})$

$$
\mathbb{E}[f(\frac{1}{2}\|X\|^2)] > f(\mathbb{E}[\frac{1}{2}\|X\|^2]) = \frac{d}{2} - \frac{d-2}{\frac{d}{2}} = 1
$$

## 4.1 James-Stein Paradox {.anchored number="4.1" anchor-id="james-stein-paradox-1"}

For $d \geq 3$, the sample mean $\bar{X} = \frac{1}{n}\sum X_i$ is inadmissible as an estimator of $\theta$ under squared error loss.

For $\delta_{JS}(X) = (1 - \frac{d-2}{\|X\|^2})X$:

$$
\text{MSE}(\theta, \delta_{JS}) < \text{MSE}(\theta, \bar{X}) \quad \forall \theta \in \mathbb{R}^d
$$

Notes: - $\bar{X}$ is UMVU, Minimax, objective Bayes - Might as well take $n=1$ (Sufficiency reduction) - This result holds without assumption of Bayes model on $\theta$: true for $\theta = (50, 10, 94, \ldots)$ - Nothing special about 0: for any $\theta_0 \in \mathbb{R}^d$, $\delta(X) = \theta_0 + (1 - \frac{d-2}{\|X-\theta_0\|^2})(X-\theta_0)$ also dominates $X$

Deep implication: shrinkage makes sense even without Bayes justification.

## 4.2 General Form {.anchored number="4.2" anchor-id="general-form"}

Let $\delta(X) = (1 - \frac{c}{\|X\|^2})X$, $c$ is tuning parameter

$$
R(\theta, \delta) = \mathbb{E}_\theta\|\delta(X) - \theta\|^2 = \mathbb{E}_\theta\|X - \theta\|^2 + \mathbb{E}_\theta[\frac{c^2}{\|X\|^2} - 2c]
$$

What is optimal $c$?

$$
R(\theta, \delta) = d + \mathbb{E}_\theta[\frac{c^2}{\|X\|^2}] - 2c
$$

$$
\frac{\partial R}{\partial c} = 2\mathbb{E}_\theta[\frac{c}{\|X\|^2}] - 2 = 0
$$

$$
c = \frac{\mathbb{E}_\theta[\|X\|^2]}{\mathbb{E}_\theta[\frac{1}{\|X\|^2}]}
$$

$c$ always > 0, but → 0 as $\|\theta\| → \infty$

What if we estimate $c$? How does adaptivity of $c(X)$ affect MSE?

---

[← 3 Empirical Bayes](03-3-empirical-bayes.md) · [Up: contents](index.md) · [5 Stein’s Lemma →](05-5-stein-s-lemma.md)
