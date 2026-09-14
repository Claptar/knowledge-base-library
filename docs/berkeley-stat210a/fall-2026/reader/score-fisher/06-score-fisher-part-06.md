---
title: Score fisher Part 06 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Score fisher Part 06 —

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The score and Fisher information are both additive over i.i.d. observations. Assume $X_1, \ldots, X_n$ are sampled i.i.d. from a univariate density $p_\theta^{(1)}(x)$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that $p_\theta^{(1)}$ is "regular:" it has common support, and tame derivatives w.r.t. $\theta$.

The full data density is $p_\theta(x) = \prod_{i=1}^n p_\theta^{(1)}(x_i)$. Likewise, if we define the single-sample log-likelihood
$$
\ell_1(\theta;X_i) = \log p_\theta^{(1)}(X_i),
$$
then the log-likelihood for the full sample is $\ell(\theta;X) = \sum_{i=1}^n \ell_1(\theta;X_i)$. Hence, each sample gives us a random realization of the log-likelihood function on the parameter space, and we just add them up to obtain the log-likelihood function for the full sample.

If the score for a single observation is $S_\theta^{(1)}(X_i) = \nabla \ell(\theta; X_i)$, then the score for the full sample is $S_\theta(X) = \sum_i S_\theta^{(i)}(X_i)$, the sum of the single-observation scores. Because these are i.i.d., the variance of $S_\theta(X)$ for the full sample is just $n$ times the variance of $S_\theta^{(1)}(X_i)$, so we can write $J(\theta)=n J_1(\theta)$, where $J_1(\theta)$ is the Fisher information when $n=1$.

As one consequence, we see that the CRLB scales like $n^{-1}$ for regular families; in other words, the standard deviation of an estimator should scale roughly like $1/\sqrt{n}$.

---

[← Cramér-Rao Lower Bound](05-cramér-rao-lower-bound.md) · [Up: contents](index.md) · [Score fisher Part 07 — →](07-score-fisher-part-07.md)
