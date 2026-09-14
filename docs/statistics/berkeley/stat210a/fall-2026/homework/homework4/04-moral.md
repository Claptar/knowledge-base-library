---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework4.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework4.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework4.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework4.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

At least for a finite parameter space, the Bayes estimator always converges to the right answer as long as we put positive mass on the right answer. This result can be generalized with more effort to continuous parameter spaces under some regularity conditions on the likelihood function, similar to the types of conditions we will use to guarantee the MLE is consistent.

The requirement that the prior density should be nonzero everywhere is sometimes called Cromwell’s Rule, after Oliver Cromwell’s famous plea to the Church of Scotland: “I beseech you, in the bowels of Christ, think it possible that you may be mistaken.”

**Problem 4** (Fisher information for location and scale families).

This problem considers the Fisher information for families with location or scale structure. Your verbal explanations for each part will be graded leniently.

1.  Consider a location family $$p_\theta(x) = p_0(x-\theta), \quad \text{ for } \theta \in \mathbb{R},$$ where $p_0$ is some fixed probability density function with respect to the Lebesgue measure.

    Show that the Fisher information for a single observation $X$ is given by $$J(\theta) = \int_{-\infty}^\infty \frac{\dot{p}_0(u)^2}{p_0(u)}\,d u.$$ Explain in your own words why it makes sense that there should be no dependence on $\theta$.

2.  Consider a scale family $$p_\theta(x) = \frac{1}{\theta}p_0\left(\frac{x}{\theta}\right),\quad \theta > 0.$$ where $p_0$ is some fixed probability density function with respect to the Lebesgue measure.

    Show that the Fisher information of a single observation $X$ is given by $$J(\theta) = \frac{1}{\theta^{2}}\int_{-\infty}^\infty\left[\frac{u \dot{p}_0(u)}{p_0(u)} + 1\right]^{2}p_0(u)\,d u.$$ Try to explain in your own words why it makes sense that the Fisher information should be proportional to $\theta^{-2}$.

3.  If we instead parameterize the scale family using $\zeta = \log\theta$, show that the Fisher information $J(\zeta)$ of a single observation $X$ does not depend on $\zeta$. Explain in your own words why this makes sense.

---

[← Moral](03-moral.md) · [Up: contents](index.md)
