---
title: Bootstrap Confidence Interval
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bootstrap Confidence Interval

How do we get a CI for $\theta(P)$?

**Idea**: What if we knew the distribution of $R_n(X, P) = \hat{\theta}_n(X) - \theta(P)$?

Define cdf $G_{n, P}(r) = \mathbb{P}_P(\hat{\theta}(X) - \theta(P) \le r)$
$$\text{Lower } \alpha/2 \text{ quantile } r_1 = G_{n, P}^{-1}(\alpha/2)$$
$$\text{Upper } " \quad r_2 = G_{n, P}^{-1}(1 - \alpha/2)$$

$$1 - \alpha = \mathbb{P}_P(r_1 \le \hat{\theta}_n - \theta \le r_2)$$
$$= \mathbb{P}_P(\theta \in [\hat{\theta}_n - r_2, \ \hat{\theta}_n - r_1])$$

Usually we don't know $G_{n, P}$ -- so bootstrap!

$$G_{n, \hat{P}_n}(r) = \mathbb{P}_{\hat{P}_n}(\hat{\theta}(X^*) - \theta(\hat{P}_n) \le r)$$

$G_{n, \hat{P}_n}(r)$ is a function only of $X$ (not of $P$)

Can use $C_{n, \alpha} = [\hat{\theta}_n - \hat{r}_2, \ \hat{\theta}_n - \hat{r}_1]$
$$\text{with } \hat{r}_1 = G_{n, \hat{P}_n}^{-1}(\alpha/2), \quad \hat{r}_2 = G_{n, \hat{P}_n}^{-1}(1 - \alpha/2)$$

---

**Bootstrap algo**:
For $b = 1, \dots, B$:
$$X_1^{*b}, \dots, X_n^{*b} \overset{\text{iid}}{\sim} \hat{P}_n$$
$$R_n^{*b} = \hat{\theta}(X^{*b}) - \theta(\hat{P}_n)$$
Return ecdf of $R_n^{*b}$

The quantity $R_n(X, P) = \hat{\theta}_n(X) - \theta(P)$ is called a **root** (function of data + dist., used to make CIs)

Other examples:
$$R_n(X, P) = \frac{\hat{\theta}_n(X) - \theta(P)}{\hat{\sigma}(X)} \quad \left[\text{where } \hat{\sigma}(X) \text{ is some estimate of s.e.}(\hat{\theta}_n)\right]$$
$$R_n(X, P) = \hat{\theta}_n(X) / \theta(P)$$

Want to choose $R_n$ so its sampling dist. $G_{n, P}$ changes slowly with $P$ (so $G_{n, \hat{P}_n} \approx G_{n, P}$)

**Studentized root** $\frac{\hat{\theta}_n - \theta}{\hat{\sigma}}$ usually works better than $\hat{\theta}_n - \theta$, then we get
$$C_{n, \alpha} = [\hat{\theta}_n - \hat{r}_2 \hat{\sigma}, \ \hat{\theta}_n - \hat{r}_1 \hat{\sigma}]$$

---

---

[← Bootstrap Bias Correction](02-bootstrap-bias-correction.md) · [Up: contents](index.md) · [Double Bootstrap →](04-double-bootstrap.md)
