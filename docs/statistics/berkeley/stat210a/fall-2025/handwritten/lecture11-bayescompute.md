---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture11-bayescompute.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture11-bayescompute.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture11-bayescompute.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture11-bayescompute.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Hierarchical Bayes
2) Markov Chain Monte Carlo
3) Gibbs Sampler

---

## Hierarchical Bayes

[Full power of Bayes is realized in large, complex problems with repeat structure, allowing us to pool information across many observations.]

$\underline{\text{Ex}}$ Predict a batter's "true" batting average from $n_i$ at-bats. $X_i = \text{# of hits} \sim \text{Binom}(n_i, \theta_i)$

Pool info across players $i = 1, \dots, m$ via **hierarchical model**

$$\alpha, \beta \sim \lambda_0(\alpha, \beta)$$

$$\theta_i \mid \alpha, \beta \overset{\text{iid}}{\sim} \text{Beta}(\alpha, \beta) \quad i \le m$$

$$X_i \mid \theta_i \overset{\text{indep}}{\sim} \text{Binom}(n_i, \theta_i) \quad i \le m$$

\$\$\begin{aligned}
\mathbb{E}[\theta_i \mid X] &= \mathbb{E}\left[\mathbb{E}[\theta_i \mid X, \alpha, \beta] \mid X\right] \\
&= \mathbb{E}\left

---

[Up: contents](../index.md)
