---
title: Is the score a statistic?
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Is the score a statistic?

It depends. Sometimes the reference point $\theta_0$ is generic, or it might be specified by the analyst without knowing whether it is the true value of $\theta$; for example, we could be testing the null hypothesis $H_0:\;\theta = \theta_0$, without knowing whether the null is true. In that case, it is a statistic (and we'll often call it a "score statistic").

On the other hand, for many theoretical calculations, including most of the calculations in this section, we will be specifically interested in $S_\theta(X)$ for the *true* value of $\theta$ that is govering the sampling distribution $P_\theta$ of the data. In that case, the score is *not* a statistic.

:::

When we study asymptotic statistics, local models like these will be natural objects of study, because a large data set will commonly allow us to rule out most $\theta$ values and only focus on values in a small neighborhood of the true parameter.

Or, writing it a different way, we have
$$
p_{\theta_0+\eta}(x) = e^{\ell(\theta_0 + \eta; x)} \approx e^{\eta'\nabla \ell(\theta_0;x)}p_{\theta_0}(x).
$$

This evokes some analogies between the score in a generic parametric family and the sufficient statistic in an exponential family. We'll begin by looking at differential identities.

---

[← Wait! Didn't we say a statistic can't be a function of $\theta$?](01-wait-didn-t-we-say-a-statistic-can-t-be-a-function-of.md) · [Up: contents](index.md) · [Differential Identities and the Fisher Information →](03-differential-identities-and-the-fisher-information.md)
