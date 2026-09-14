---
title: Definitions
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Definitions

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Since introducing the basic problem in [Lecture 3](../estimation/index.md) of how to choose between estimators, we have studied two possible answers: First, to constrain our choice of estimator to be unbiased, which in the presence of a complete sufficient statistic narrows our choices to (at most) one good unbiased estimator for any estimand; and second, to summarize risk functions by their average-case risk, which leads us to Bayes estimators. In this lecture, we will consider another idea: to minimize the worst-case risk:
$$
\minimize_{\delta} \sup_{\theta\in\Theta} R(\theta;\delta)
$$
The (possibly unattainable) infimum of all estimators' sup-risks is called the **minimax risk** of the estimation problem
$$
r^* = \inf_\delta \sup_\theta R(\theta;\delta),
$$
and an estimator $\delta^*$ is called **minimax** if it achieves the minimax risk, i.e. if
$$
\sup_\theta R(\theta; \delta^*) = r^*.
$$
Whether or not a minimax estimator exists, or we want to use it, it can be informative to investigate a problem's minimax risk as a measure of how difficult the problem is, and in particular how it changes with the sample size, problem dimension, or other problem parameters. Thus, it is useful to be able to bound $r^*$ from above and below.

---

[Up: contents](index.md) · [Game theoretic interpretation →](02-game-theoretic-interpretation.md)
