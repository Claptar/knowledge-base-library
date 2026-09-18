---
title: 4 Score and Fisher information in an i.i.d. sample
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4 Score and Fisher information in an i.i.d. sample

The score and Fisher information are both additive over i.i.d. observations. Assume $X_1, \ldots, X_n$ are sampled i.i.d. from a univariate density $p_\theta^{(1)}(x)$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that $p_\theta^{(1)}$ is “regular:” it has common support, and tame derivatives w.r.t. $\theta$.

The full data density is $p_\theta(x) = \prod_{i=1}^n p_\theta^{(1)}(x_i)$. Likewise, if we define the single-sample log-likelihood

$$
\ell_1(\theta;X_i) = \log p_\theta^{(1)}(X_i),
$$

 then the log-likelihood for the full sample is $\ell(\theta;X) = \sum_{i=1}^n \ell_1(\theta;X_i)$. Hence, each sample gives us a random realization of the log-likelihood function on the parameter space, and we just add them up to obtain the log-likelihood function for the full sample.

If the score for a single observation is $S_\theta^{(1)}(X_i) = \nabla \ell(\theta; X_i)$, then the score for the full sample is $S_\theta(X) = \sum_i S_\theta^{(i)}(X_i)$, the sum of the single-observation scores. Because these are i.i.d., the variance of $S_\theta(X)$ for the full sample is just $n$ times the variance of $S_\theta^{(1)}(X_i)$, so we can write $J(\theta)=n J_1(\theta)$, where $J_1(\theta)$ is the Fisher information when $n=1$.

As one consequence, we see that the CRLB scales like $n^{-1}$ for regular families; in other words, the standard deviation of an estimator should scale roughly like $1/\sqrt{n}$.

---

[← 3 Cramér-Rao Lower Bound](03-3-cramér-rao-lower-bound.md) · [Up: contents](index.md) · [5 Score and Fisher information in (curved) exponential families →](05-5-score-and-fisher-information-in-curved-exponential-familie.md)
