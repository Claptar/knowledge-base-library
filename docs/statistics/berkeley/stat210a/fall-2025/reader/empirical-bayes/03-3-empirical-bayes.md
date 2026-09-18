---
title: 3 Empirical Bayes
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Empirical Bayes

## 3.1 {.anchored number="3.1" anchor-id="section"}

## 3.2 Common Situation in Hierarchical Bayes Models {.anchored number="3.2" anchor-id="common-situation-in-hierarchical-bayes-models"}

1.  $\theta \sim G$, one draw: hard to justify prior
2.  Lots of info: prior doesn’t matter
3.  $\theta_i \sim G$, only $X_i$ informative: prior helps
4.  Many draws: can check fit

$$
X_i \sim p_{\theta_i}(x), \quad i = 1,\ldots,d
$$

## 3.3 Hybrid Approach {.anchored number="3.3" anchor-id="hybrid-approach"}

Treat $G$ as fixed:

1.  Estimate $G$ based on observed data
2.  Plug in $\hat{G}$ as though known

## 3.4 Example {.anchored number="3.4" anchor-id="example"}

$\theta_i \sim N(0, \tau^2)$, $\tau^2$ fixed unknown $X_i|\theta_i \sim N(\theta_i, 1)$, $i = 1,\ldots,d$

Bayes estimator if we knew $\tau^2$ is:

$$
\delta(X) = \frac{\tau^2}{\tau^2 + 1}X_i
$$

$\tau^2$ is sufficient.

To estimate $\tau^2$, use $X \sim N(0, \tau^2 I_d + I_d)$:

$$
\mathbb{E}\|X\|^2 = d(\tau^2 + 1)
$$

$$
\hat{\tau}^2 = \max\{\frac{1}{d}\|X\|^2 - 1, 0\}
$$

Plug in: $\hat{\delta}(X) = (1 - \frac{d}{\|X\|^2})_+ X_i$

If $d$ large, should be near optimal.

---

[← 2 Stein’s Unbiased Risk Estimator](02-2-stein-s-unbiased-risk-estimator.md) · [Up: contents](index.md) · [4 James-Stein Estimator →](04-4-james-stein-estimator.md)
