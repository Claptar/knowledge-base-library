---
title: Repeated sampling from exponential families
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/exponential-families.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Repeated sampling from exponential families

**Source:** [`reader/exponential-families.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/exponential-families.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

One of the most important properties of exponential families is that a large sample can be summarized by a low-dimensional statistic. Suppose we observe a vector of observations $X = (X_1,\ldots,X_n)$ representing an independent and identically distributed (i.i.d.) sample from an exponential family. Let $p_\eta^{(1)$ denote the density for a single observation:

$$
X_1\ldots,X_n \simiid p_\eta^{(1)}(x) = e^{\eta'T(x) - A(\eta)}h(x).
$$

Then the random vector $X = (X_1,\ldots,X_n)$ follows another closely related exponential family:

$$
\begin{aligned}
p_\eta(x)
&= \prod_{i=1}^n e^{\eta'T(x_i) - A(\eta)}h(x_i)\\[7pt]
&= \exp\left\{\eta'\sum_{i=1}^n T(x_i) - nA(\eta)\right\} \prod_{i=1}^n h(x_i).
\end{aligned}
$$

This new density $p_\eta$, which governs the distribution of the entire sample, is an exponential family with the same natural parameter as before, sufficient statistic $\sum_i T(X_i)$, carrier density $\prod_i h(x_i)$, and log-partition function $nA(\eta)$.

For reasons that will become clearer in the next lecture, it is very significant that the sufficient statistic does not increase in dimension as the sample size grows. This means that the $s$-dimensional vector $\sum_i T(X_i)$ is for all intents and purposes a complete summary of the entire sample, no matter how large $n$ is.

---

[← Visualization of exponential tilting](05-visualization-of-exponential-tilting.md) · [Up: contents](index.md)
