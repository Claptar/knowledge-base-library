---
title: Bootstrap Bias Correction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bootstrap Bias Correction

$\hat{\theta}_n$ some estimator. What is its bias?
$$\text{Bias}_P(\hat{\theta}_n) = \mathbb{E}_P \left[\hat{\theta}_n - \theta(P)\right]$$

Idea: plug in $\hat{P}_n$ for $P$:
$$\text{Bias}_{\hat{P}_n}(\hat{\theta}_n^*) = \mathbb{E}_{\hat{P}_n} \left[\hat{\theta}_n^* - \theta(\hat{P}_n)\right] \quad (\text{NB})$$

Monte Carlo:
For $b = 1, \dots, B$:
$$\text{Sample } X_1^{*b}, \dots, X_n^{*b} \overset{iid}{\sim} \hat{P}_n$$
$$\hat{\theta}^{*b} = \hat{\theta}(X^{*b})$$

$$\bar{\theta}^* = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$$
$$\widehat{\text{Bias}}(\hat{\theta}_n) = \bar{\theta}^* - \theta(\hat{P}_n)$$

We can use this to correct bias:
$$\hat{\theta}_n^{\text{BC}} = \hat{\theta}_n - \widehat{\text{Bias}}(\hat{\theta}_n)$$

**Note:** while $\hat{\theta}_n - \text{Bias}(\hat{\theta}_n)$ is always better than $\hat{\theta}_n$, $\hat{\theta}_n - \widehat{\text{Bias}}(\hat{\theta}_n)$ may not be! Might be adding var.

---

$$\text{s.e.}_P(\hat{\theta}) \quad\quad \text{s.e.}_{\hat{P}_n}(\hat{\theta}^*)$$
$$\theta \qquad \mathbb{E}_P \hat{\theta} \qquad \theta(\hat{P}_n) \qquad \mathbb{E}_{\hat{P}_n} \hat{\theta}^*$$
$$\text{Bias}_P(\hat{\theta}) \qquad\qquad \text{Bias}_{\hat{P}_n}(\hat{\theta}^*)$$

| | "Real World" | "Bootstrap World" |
| :--- | :--- | :--- |
| **Sampling dist.** | $P =$ (hidden) | $\hat{P}_n(X) =$ |
| **Parameter** | $\theta(P)$ | $\theta(\hat{P}_n(X))$ |
| **Data set** | $X_1, \dots, X_n \overset{iid}{\sim} P$ (observed once) | $X_1^*, \dots, X_n^* \overset{iid}{\sim} \hat{P}_n(X)$ |
| **Estimator** | $\hat{\theta}(X)$ | $\hat{\theta}^* = \hat{\theta}(X^*)$ (generated at will) |
| **Sampling dist of estimator** | centered around $\theta(P)$ | centered around $\theta(\hat{P}_n(X))$ |

---

---

[← Bootstrap standard errors](02-bootstrap-standard-errors.md) · [Up: contents](index.md) · [Bootstrap Confidence Interval →](04-bootstrap-confidence-interval.md)
