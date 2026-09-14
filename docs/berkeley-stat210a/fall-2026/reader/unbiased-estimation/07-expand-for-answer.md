---
title: Expand for answer
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand for answer

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

A simple unbiased estimator for this probability is just the indicator of whether it happened, $1\{X \geq 500\}$. Since $X$ is complete sufficient, this must also be the UMVU estimator.

But this estimator makes no sense! If we see $X=499$ heads out of $1000$, we are estimating that if we repeated the experiment by flipping the coin $1000$ more times, there is no chance we'd get more heads than we got this time. There are perfectly good estimators for this problem; for example if we have any reasonable estimator $\hat\theta$ for $\theta$ (such as $X/n$) we can use the *plug-in estimator* $\PP_{\hat\theta}(X \geq 500)$, and this will increase gradually with $X$. But any such reasonable estimator cannot be unbiased, because all other unbiased estimators have to be worse than the UMVU estimator.

:::

While it may seem like we are beating up the unbiased estimation paradigm here, in fact there is no statistical paradigm that doesn't look a bit ridiculous on some examples. As we'll see later, in the multivariate Gaussian location model above, both the maximum likelihood estimator and the Bayes estimator using the "objective" Jeffreys prior are even worse than the UMVU estimator. Much of the art of applied statistics is to understand the limitations of the different paradigms and choose one that's appropriate for the problem at hand.

---

[← Doubts about unbiasedness](06-doubts-about-unbiasedness.md) · [Up: contents](index.md)
