---
title: Empirical Bayes
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/empirical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/empirical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Empirical Bayes

**Source:** [`reader/empirical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/empirical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

###

### Common Situation in Hierarchical Bayes Models

1.  $\theta \sim G$, one draw: hard to justify prior
2.  Lots of info: prior doesn't matter
3.  $\theta_i \sim G$, only $X_i$ informative: prior helps
4.  Many draws: can check fit

$$X_i \sim p_{\theta_i}(x), \quad i = 1,\ldots,d$$

### Hybrid Approach

Treat $G$ as fixed:

1.  Estimate $G$ based on observed data
2.  Plug in $\hat{G}$ as though known

### Example

$\theta_i \sim N(0, \tau^2)$, $\tau^2$ fixed unknown
$X_i|\theta_i \sim N(\theta_i, 1)$, $i = 1,\ldots,d$

Bayes estimator if we knew $\tau^2$ is:

$$\delta(X) = \frac{\tau^2}{\tau^2 + 1}X_i$$

$\tau^2$ is sufficient.

To estimate $\tau^2$, use $X \sim N(0, \tau^2 I_d + I_d)$:

$$\mathbb{E}\|X\|^2 = d(\tau^2 + 1)$$

$$\hat{\tau}^2 = \max\{\frac{1}{d}\|X\|^2 - 1, 0\}$$

Plug in: $\hat{\delta}(X) = (1 - \frac{d}{\|X\|^2})_+ X_i$

If $d$ large, should be near optimal.

---

[← Stein's Unbiased Risk Estimator](02-stein-s-unbiased-risk-estimator.md) · [Up: contents](index.md) · [James-Stein Estimator →](04-james-stein-estimator.md)
