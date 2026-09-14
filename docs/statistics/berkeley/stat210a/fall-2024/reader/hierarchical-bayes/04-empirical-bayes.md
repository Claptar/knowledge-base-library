---
title: Empirical Bayes
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/hierarchical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Empirical Bayes

**Source:** [`reader/hierarchical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Back to Gaussian hierarchical model:

$$
\begin{aligned}
\theta_i &\sim N(\mu, \tau^2) \\
X_i | \theta_i &\sim N(\theta_i, \sigma^2)
\end{aligned}
$$

$$
\mathbb{E}[\theta_i | X, B] = \frac{B - \sigma^2}{B}X_i + \frac{\sigma^2}{B}\bar{X}, \quad B = \tau^2 + \sigma^2
$$

For any reasonable prior: $B | X \approx \frac{1}{N}\sum_{i=1}^N (X_i - \bar{X})^2$

If prior doesn't matter much, why use one? Could just estimate $B$ from data, however we want.

A minimax estimator is $B = \sigma^2 + \frac{1}{N}\sum_{i=1}^N (X_i - \bar{X})^2$

Called Empirical Bayes: a hybrid approach in which hyperparameters are treated as fixed, others treated as random.

---

[← Gibbs Sampler](03-gibbs-sampler.md) · [Up: contents](index.md)
