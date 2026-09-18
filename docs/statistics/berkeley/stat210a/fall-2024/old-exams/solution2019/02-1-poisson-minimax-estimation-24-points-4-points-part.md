---
title: 1. Poisson minimax estimation (24 points, 4 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Poisson minimax estimation (24 points, 4 points / part).

Some useful facts for this problem:
- For $\theta > 0$, the Poisson density for $X \sim \text{Pois}(\theta)$ is $\frac{\theta^x e^{-\theta}}{x!}$ on $x = 0, 1, \dots$. The mean and variance are both $\theta$.
- The Gamma density for $X \sim \text{Gamma}(k, \beta)$, where $\beta > 0$ is the rate parameter, is
  $$
  \frac{\beta^k}{\Gamma(k)} x^{k-1} e^{-\beta x}, \quad \text{on } x > 0,
  $$
  where $\Gamma(k) = \int_0^\infty z^{k-1} e^{-z} dz$. The mean and variance are $k/\beta$ and $k/\beta^2$, respectively.
- If $X \sim \text{Gamma}(k, \beta)$ (in the rate parameterization) with $k > 1$, then $\mathbb{E}[X^{-1}] = \beta/(k - 1)$.

Consider estimating $\theta$ given a single Poisson observation $X \sim \text{Pois}(\theta)$ using the loss function
$$
L(d, \theta) = \frac{(d - \theta)^2}{\theta}.
$$
Throughout this problem, unless otherwise specified, the risk of a given estimator is always calculated using this loss.

(a) Find the MLE and calculate its risk function.

(b) Show that $\theta \sim \text{Gamma}(k, \beta)$ is a conjugate prior for this problem and give the posterior distribution.

(c) Find the Bayes estimator for the prior from part (b) and the loss $L$ defined above.

(d) (*) Show that the Bayes risk of the Bayes estimator from part (c) is $1/(1 + \beta)$

(e) Show that the MLE is minimax relative to the loss $L$.

(f) Show that the minimax risk for the usual squared error loss — i.e., $L_{\text{SE}}(d, \theta) = (d - \theta)^2$ — is infinite (this motivates changing the loss function to our $L$, which "adjusts" for the hardness of the problem).

---

---

[← Final Examination: QUESTION BOOKLET](01-final-examination-question-booklet.md) · [Up: contents](index.md) · [1. Solution. →](03-1-solution.md)
