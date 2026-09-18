---
title: Bootstrap standard errors
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bootstrap standard errors

Suppose $\hat{\theta}_n(X)$ is an estimator for $\theta(P)$ (maybe plug-in, maybe not)

What is its standard error? Use plug-in:
$$\widehat{\text{s.e.}}(\hat{\theta}_n) = \sqrt{\text{Var}_{\hat{P}_n}(\hat{\theta}_n^*)} \quad \left[\text{use } \hat{\theta}_n^* \text{ to indicate new sample } X^*, \text{ not } X\right]$$
$$\text{Var}_{\hat{P}_n}(\hat{\theta}_n^*) = \text{Var}_{X_1^*, \dots, X_n^* \overset{iid}{\sim} \hat{P}_n}(\hat{\theta}_n(X_1^*, \dots, X_n^*))$$

How to compute? Monte Carlo:

For $b = 1, \dots, B$:
$$\begin{array}{|l}
\text{Sample } X_1^{*b}, \dots, X_n^{*b} \overset{iid}{\sim} \hat{P}_n \quad \leftarrow \left[\begin{array}{l} \text{Sample } n \text{ points} \\ \text{with replacement} \\ \text{from original sample} \end{array}\right] \\
\hat{\theta}^{*b} = \hat{\theta}(X_1^{*b}, \dots, X_n^{*b})
\end{array}$$

$$\bar{\theta}^* = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$$
$$\widehat{\text{s.e.}}(\hat{\theta}_n) = \sqrt{\frac{1}{B} \sum_b (\hat{\theta}^{*b} - \bar{\theta}^*)^2}$$

Note this is a Monte Carlo numerical approx. to the idealized Bootstrap estimator, which we could compute by iterating over all $n^n$ possible $X^* = (X_1^*, \dots, X_n^*)$ vectors.

---

---

[← Nonparametric Estimation](01-nonparametric-estimation.md) · [Up: contents](index.md) · [Bootstrap Bias Correction →](03-bootstrap-bias-correction.md)
