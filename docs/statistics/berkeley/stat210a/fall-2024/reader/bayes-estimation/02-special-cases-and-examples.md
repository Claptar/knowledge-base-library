---
title: Special Cases and Examples
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/bayes-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Special Cases and Examples

**Source:** [`reader/bayes-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Squared Error Loss

If $L(\theta, d) = (\theta - d)^2$, then the Bayes estimator is the posterior mean:

$$
\delta_\pi(x) = \EE[\theta|X=x]
$$

Proof:
$$
\begin{aligned}
\EE[(\theta - d)^2|X=x] &= \EE[\theta^2|X=x] - 2d\EE[\theta|X=x] + d^2 \\
&= \Var(\theta|X=x) + (\EE[\theta|X=x] - d)^2 + \EE[\theta|X=x]^2 - 2d\EE[\theta|X=x] + d^2
\end{aligned}
$$

The minimum occurs when $d = \EE[\theta|X=x]$.

### Weighted Squared Error

For $L(\theta, d) = w(\theta)(\theta - d)^2$ (e.g., squared relative error), the Bayes estimator is:

$$
\delta_\pi(x) = \frac{\EE[w(\theta)\theta|X=x]}{\EE[w(\theta)|X=x]}
$$

---

[← Bayes Risk and Bayes Estimator](01-bayes-risk-and-bayes-estimator.md) · [Up: contents](index.md) · [Examples →](03-examples.md)
