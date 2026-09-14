---
title: James-Stein Estimator
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/empirical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/empirical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# James-Stein Estimator

**Source:** [`reader/empirical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/empirical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

$$\delta_{JS}(X) = (1 - \frac{d-2}{\|X\|^2})X$$

Proof: If $Y \sim \text{Gamma}(\frac{d}{2}, \frac{1}{2})$, then:

$$\mathbb{P}(Y > \frac{d-2}{2}) = 1$$

Now use $f(x) = x - \frac{d-2}{x}$,
$\frac{1}{2}\|X\|^2 \sim \text{Gamma}(\frac{d}{2}, \frac{1}{2})$

$$\mathbb{E}[f(\frac{1}{2}\|X\|^2)] > f(\mathbb{E}[\frac{1}{2}\|X\|^2]) = \frac{d}{2} - \frac{d-2}{\frac{d}{2}} = 1$$

### James-Stein Paradox

For $d \geq 3$, the sample mean $\bar{X} = \frac{1}{n}\sum X_i$ is
inadmissible as an estimator of $\theta$ under squared error loss.

For $\delta_{JS}(X) = (1 - \frac{d-2}{\|X\|^2})X$:

$$\text{MSE}(\theta, \delta_{JS}) < \text{MSE}(\theta, \bar{X}) \quad \forall \theta \in \mathbb{R}^d$$

Notes: - $\bar{X}$ is UMVU, Minimax, objective Bayes - Might as well
take $n=1$ (Sufficiency reduction) - This result holds without
assumption of Bayes model on $\theta$: true for
$\theta = (50, 10, 94, \ldots)$ - Nothing special about 0: for any
$\theta_0 \in \mathbb{R}^d$,
$\delta(X) = \theta_0 + (1 - \frac{d-2}{\|X-\theta_0\|^2})(X-\theta_0)$
also dominates $X$

Deep implication: shrinkage makes sense even without Bayes
justification.

### General Form

Let $\delta(X) = (1 - \frac{c}{\|X\|^2})X$, $c$ is tuning parameter

$$R(\theta, \delta) = \mathbb{E}_\theta\|\delta(X) - \theta\|^2 = \mathbb{E}_\theta\|X - \theta\|^2 + \mathbb{E}_\theta[\frac{c^2}{\|X\|^2} - 2c]$$

What is optimal $c$?

$$R(\theta, \delta) = d + \mathbb{E}_\theta[\frac{c^2}{\|X\|^2}] - 2c$$

$$\frac{\partial R}{\partial c} = 2\mathbb{E}_\theta[\frac{c}{\|X\|^2}] - 2 = 0$$

$$c = \frac{\mathbb{E}_\theta[\|X\|^2]}{\mathbb{E}_\theta[\frac{1}{\|X\|^2}]}$$

$c$ always \> 0, but → 0 as $\|\theta\| → \infty$

What if we estimate $c$? How does adaptivity of $c(X)$ affect MSE?

---

[← Empirical Bayes](03-empirical-bayes.md) · [Up: contents](index.md) · [Stein's Lemma →](05-stein-s-lemma.md)
