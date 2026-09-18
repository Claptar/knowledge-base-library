---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture11-bayescompute.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture11-bayescompute.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture11-bayescompute.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture11-bayescompute.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Hierarchical Bayes
2) Markov Chain Monte Carlo
3) Gibbs Sampler

---

## Hierarchical Bayes

[Full power of Bayes is realized in large, complex problems with repeat structure, allowing us to pool information across many observations.]

**Ex** Predict a batter's "true" batting average from $n_i$ at-bats. $X_i = \text{# of hits} \sim \text{Binom}(n_i, \theta_i)$

Pool info across players $i=1,\dots, m$ via **hierarchical model**

$$
\begin{aligned}
\alpha, \beta &\sim \lambda_0(\alpha, \beta) \\
\theta_i \mid \alpha, \beta &\overset{\text{iid}}{\sim} \text{Beta}(\alpha, \beta) \quad i \le m \\
X_i \mid \theta_i &\overset{\text{indep}}{\sim} \text{Binom}(n_i, \theta_i) \quad i \le m
\end{aligned}
$$

$$
\begin{aligned}
\mathbb{E}[\theta_i \mid X] &= \mathbb{E}\Big[ \mathbb{E}[\theta_i \mid X, \alpha, \beta] \mid X \Big] \\
&= \mathbb{E}\left[ \left( \frac{X_i + \alpha}{n_i + \alpha + \beta} \right) \mid X \right]
\end{aligned}
$$

*(Note above fraction: $X_i, n_i$ are fixed; $\alpha, \beta$ are sampled $\sim \lambda(\alpha, \beta \mid X)$)*

**Intuition:** Use all $X_1, \dots, X_m$ to learn good prior on $\theta_i$

[**Note:** there is always an equivalent model where we marginalize over $\alpha, \beta$ and just write a more complicated prior on $\Theta$. Hierarchical version may give better intuition or computational strategies]

---

## Gaussian Hierarchical Model:

\$\$
\begin{aligned}
\tau^2 &\sim \lambda_0 \\
\theta_i \mid \tau^2 &\overset{\text{iid}}{\sim} N(0, \tau^2) \quad i \le d \\

---

[Up: contents](../index.md)
