---
title: 6 Doubts about unbiasedness
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 6 Doubts about unbiasedness

The last example raises the question: why should we require zero bias? There can be good reasons for this: it’s nice to be able to say your estimator is correct on average, especially if the estimand is strongly contested by different parties. But we shouldn’t take this constraint too seriously because in some cases the UMVUE can be inadmissible, or even ridiculous in cases where other approaches work well.

**Example:** Suppose we observe a multivariate Gaussian vector with an unknown location parameter, $X \sim N_d(\mu, I_d)$ for $\mu \in \RR^d$, where $I_d$ is the identity matrix, and we want to estimate $g(\mu) = \|\mu\|^2$.

Since $X$, the complete sufficient statistic for this family, is a natural estimator for $\mu$, we can start with $\|X\|^2$ and try to make it unbiased. If we write $X = \mu + Z$ where $Z \sim N_d(0,I_d)$, then we have

$$
\begin{aligned}
\EE_\mu \|X\|^2 &= \sum_j \EE (Z_j + \mu_j)^2\\
&= \sum_j \mu_j^2 + 2\mu_j\EE Z_j + \EE Z_j^2\\
&= \|\mu\|^2 + d,
\end{aligned}
$$

 since each cross-term is zero and $\EE Z_j^2 = \Var(Z_j) = 1$. As a result, we can get an unbiased estimator by subtracting off the bias, namely $\delta(X) = \|X\|^2-d$. But this estimator has the very odd property that it can be negative: if $d=10$ and $\|X\|^2=5$, which can happen, we are giving the estimate $-5$ for the non-negative estimand $\|\mu\|^2$. This may not seem like a big deal when we are just doing frequentist calculations, but imagine the authors’ embarrassment if such an estimate actually found its way into a journal paper!

From a dry decision theory perspective, we can also recognize this estimator as inadmissible for any reasonable loss function: whenever the estimate is zero, we will always be getting closer to the estimand if we replace it with zero; that is, $\delta_+(X) = (\|X\|^2-d)_+$ will strictly dominate $\delta(X)$, for any reasonable loss function.

There are even sillier examples of UMVU estimators, as we see next.

**Example:** Suppose we observe $X \sim \text{Bin}(1000, \theta)$, and want to estimate $g(\theta) = \PP_\theta(X \geq 500)$. What is the UMVU estimator?

Expand for answer

A simple unbiased estimator for this probability is just the indicator of whether it happened, $1\{X \geq 500\}$. Since $X$ is complete sufficient, this must also be the UMVU estimator.

But this estimator makes no sense! If we see $X=499$ heads out of $1000$, we are estimating that if we repeated the experiment by flipping the coin $1000$ more times, there is no chance we’d get more heads than we got this time. There are perfectly good estimators for this problem; for example if we have any reasonable estimator $\hat\theta$ for $\theta$ (such as $X/n$) we can use the *plug-in estimator* $\PP_{\hat\theta}(X \geq 500)$, and this will increase gradually with $X$. But any such reasonable estimator cannot be unbiased, because all other unbiased estimators have to be worse than the UMVU estimator.

While it may seem like we are beating up the unbiased estimation paradigm here, in fact there is no statistical paradigm that doesn’t look a bit ridiculous on some examples. As we’ll see later, in the multivariate Gaussian location model above, both the maximum likelihood estimator and the Bayes estimator using the “objective” Jeffreys prior are even worse than the UMVU estimator. Much of the art of applied statistics is to understand the limitations of the different paradigms and choose one that’s appropriate for the problem at hand.

---

[← 5 Finding the UMVUE](05-5-finding-the-umvue.md) · [Up: contents](index.md)
