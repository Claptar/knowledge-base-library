---
title: Stein's Unbiased Risk Estimator (SURE)
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/empirical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/empirical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Stein's Unbiased Risk Estimator (SURE)

**Source:** [`reader/empirical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/empirical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Unbiased estimator of the MSE of any $\delta(X)$

Apply Stein's Lemma with $h(x) = X - \delta(x)$

Assume $\sigma^2 = 1$:

$$R(\theta, \delta) = \mathbb{E}_\theta\|\delta(X) - \theta\|^2 = \mathbb{E}_\theta\|X - \theta\|^2 + \mathbb{E}_\theta\|\delta(X) - X\|^2 - 2\mathbb{E}_\theta[(X-\theta)^T(X-\delta(X))]$$
$$= d + \mathbb{E}_\theta\|\delta(X) - X\|^2 - 2\mathbb{E}_\theta[\text{tr}(D(X-\delta(X)))]$$

$$\hat{R}(X) = d + \|\delta(X) - X\|^2 - 2\text{tr}(D\delta(X))$$

is unbiased for the MSE estimator $\delta(X)$

Only depends on X

Can also compute MSE via $R = \mathbb{E}_\theta[\hat{R}]$

$$\mathbb{E}_\theta[\|\delta(X) - h(X)\|^2] = \mathbb{E}_\theta[\|\delta(X) - \theta\|^2] + \mathbb{E}_\theta[\|h(X) - \theta\|^2] - 2\mathbb{E}_\theta[(\delta(X) - \theta)^T(h(X) - \theta)]$$

$$R = d + R(\theta, \delta) - 2\mathbb{E}_\theta[\text{tr}(D\delta(X))]$$

Example: $\delta(X) = (1-c)X$ for fixed $c$

$h(x) = cX$, $Dh = cI_d$

$\hat{R} = d + c^2\|X\|^2 - 2cd$

### Risk of James-Stein

$\delta_{JS}(X) = (1 - \frac{d-2}{\|X\|^2})X$

$h(X) = \frac{d-2}{\|X\|^2}X$,
$Dh(X) = \frac{d-2}{\|X\|^2}I_d - 2(d-2)\frac{XX^T}{\|X\|^4}$

$\|h(X)\|^2 = \frac{(d-2)^2}{\|X\|^2}$

$$\text{tr}(Dh(X)) = \frac{d(d-2)}{\|X\|^2} - \frac{2(d-2)}{\|X\|^2} = \frac{(d-2)^2}{\|X\|^2}$$

$$\hat{R} = d + \frac{(d-2)^2}{\|X\|^2} - 2\frac{(d-2)^2}{\|X\|^2} = d - \frac{(d-2)^2}{\|X\|^2}$$

$$R(\theta) = \mathbb{E}_\theta[\hat{R}] = d - (d-2)^2\mathbb{E}_\theta[\frac{1}{\|X\|^2}]$$

If $\theta = 0$ then $\mathbb{E}_0[\frac{1}{\|X\|^2}] = \frac{1}{d-2}$

$$R(0) = d - (d-2) = 2$$

Possibly surprising

If $\theta \neq 0$ then
$\mathbb{E}_\theta[\frac{1}{\|X\|^2}] < \frac{1}{\|\theta\|^2}$

$$R(\theta) < d - \frac{(d-2)^2}{\|\theta\|^2 + d}$$

Smaller and smaller advantage, but always better

Note: $\delta_{JS}(X)$ also inadmissible

$\delta_{+}(X) = (1 - \frac{d-2}{\|X\|^2})_+ X$ is strictly better

Practically more useful version:

$$\delta_{JS+}(X) = (1 - \frac{d-3}{\|X\|^2})_+ X$$

Dominates $\delta(X) = X$ for $d \geq 4$

Taken to logical extreme, suggestion seems dumb: should everyone at
Berkeley pool their estimates?

Note: $\mathbb{E}\|\hat{\theta}\|^2$ is improved, but
$\mathbb{E}[(\hat{\theta}_i - \theta_i)^2]$ may get worse for individual
coordinates.

---

[← Stein's Lemma](05-stein-s-lemma.md) · [Up: contents](index.md)
