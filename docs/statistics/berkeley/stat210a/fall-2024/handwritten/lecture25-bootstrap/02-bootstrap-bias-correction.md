---
title: Bootstrap Bias Correction
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bootstrap Bias Correction

$\hat{\theta}_n$ some estimator. What is its bias?

$$\text{Bias}_P(\hat{\theta}_n) = \mathbb{E}_P \left[ \hat{\theta}_n - \theta(P) \right]$$

Idea: plug in $\hat{P}_n$ for $P$:

$$\text{Bias}_{\hat{P}_n}(\hat{\theta}_n^*) = \mathbb{E}_{\hat{P}_n} \left[ \hat{\theta}_n^* - \theta(\hat{P}_n) \right]$$
(NB)

Monte Carlo:
For $b = 1, \dots, B$:
$$\text{Sample } X_1^{*b}, \dots, X_n^{*b} \overset{\text{iid}}{\sim} \hat{P}_n$$
$$\hat{\theta}^{*b} = \hat{\theta}(X^{*b})$$

$$\overline{\theta^*} = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$$

$$\widehat{\text{Bias}}(\hat{\theta}_n) = \overline{\theta^*} - \theta(\hat{P}_n)$$

We can use this to correct bias:
$$\hat{\theta}_n^{\text{BC}} = \hat{\theta}_n - \widehat{\text{Bias}}(\hat{\theta}_n)$$

**Note**: while $\hat{\theta}_n - \text{Bias}(\hat{\theta}_n)$ is always better than $\hat{\theta}_n$, $\hat{\theta}_n - \widehat{\text{Bias}}(\hat{\theta}_n)$ may not be! Might be adding var.

---

[Diagram comparing Real World and Bootstrap World distributions: Real World on the left with center $\mathbb{E}_P \hat{\theta}$ offset from $\theta$ by $\text{Bias}_P(\hat{\theta})$, spread given by $\text{s.e.}_P(\hat{\theta})$; Bootstrap World on the right centered at $\mathbb{E}_{\hat{P}_n} \hat{\theta}^*$ offset from $\theta(\hat{P}_n)$ by $\text{Bias}_{\hat{P}_n}(\hat{\theta}^*)$, spread given by $\text{s.e.}_{\hat{P}_n}(\hat{\theta}^*)$.]

| | "Real World" | "Bootstrap World" |
| :--- | :--- | :--- |
| **Sampling dist.** | $P =$ [smooth curve] (hidden) | $\hat{P}_n(X) =$ [jagged empirical curve] |
| **Parameter** | $\theta(P)$ | $\theta(\hat{P}_n(X))$ |
| **Data set** | $X_1, \dots, X_n \overset{\text{iid}}{\sim} P$ | $X_1^*, \dots, X_n^* \overset{\text{iid}}{\sim} \hat{P}_n(X)$ |
| **Estimator** | $\hat{\theta}(X)$ (observed once) | $\hat{\theta}^* = \hat{\theta}(X^*)$ (generated at will) |
| **Sampling dist. of estimator** | [distribution centered near $\theta(P)$] | [distribution centered near $\theta(\hat{P}_n(X))$] |

---

---

[← Nonparametric Estimation](01-nonparametric-estimation.md) · [Up: contents](index.md) · [Bootstrap Confidence Interval →](03-bootstrap-confidence-interval.md)
