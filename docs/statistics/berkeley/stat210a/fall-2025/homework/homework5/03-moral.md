---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework5.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework5.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework5.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework5.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Minimizing average-case risk is closely related to admissibility, though the general relationship is not quite as tight as what we’ve shown in this problem for finite parameter spaces. In more general parameter spaces, there is a more general result which roughly states that all admissible estimators are limits of Bayes estimators, under relatively mild conditions.

**Problem 3** (Other loss functions).

Assume for each problem below that there exists an estimator with finite Bayes risk.

1.  Consider a Bayesian model with a discrete parameter $\theta$. What is the Bayes estimator for the loss $L(\theta, d) = 1\{\theta \neq d\}$?

2.  Next consider a Bayesian model with a single real parameter $\theta$, and assume that the posterior distribution of $\theta$ given $X=x$ is absolutely continuous (with respect to the Lebesgue measure) for all $x$. What is the Bayes estimator for the *absolute error loss* $L(\theta, d) = |\theta-d|$?

3.  Under the same assumptions as part (b), what loss function $L_\gamma(\theta, d)$ would give the posterior $\gamma$ quantile as its Bayes estimator; that is, the estimator $\delta_\gamma(X)$ has $\mathbb{P}(\theta < \delta_\gamma(X) \mid X) = \gamma$.

---

[← Moral](02-moral.md) · [Up: contents](index.md) · [Moral →](04-moral.md)
