---
title: Efficiency
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Efficiency

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The CRLB is not necessarily attainable.

We define the efficiency of an unbiased estimator as:

$$\text{eff}_\delta(\theta) = \frac{\text{CRLB}(\theta)}{\Var_\theta(\delta)} \leq 1,$$

We say $\delta(X)$ is *efficient* if $\text{eff}_\delta(\theta) = 1$ for all $\theta$.

For $g(\theta)=\theta\in \RR$, the efficiency depends on how correlated $\delta(X)$ is with the score:
$$\begin{aligned}\text{eff}_\delta(\theta) &= \frac{\Cov_\theta(\delta(X), \dot{\ell}(\theta;X))^2}{\Var_\theta(\delta(X)) \cdot \Var_\theta(\dot{\ell}(\theta;X))}\\
&= \Corr_\theta(\delta,\dot{\ell}(\theta))^2
\end{aligned}$$

Thus, an efficient estimator for $\theta$ is one that is perfectly correlated with the score. This is rarely achieved in finite samples, but we can often approach it asymptotically as $n \to \infty$.

---

[← Examples](08-examples.md) · [Up: contents](index.md)
