---
title: Minimax Risk Estimator
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Minimax Risk Estimator

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Definition of Minimax Risk

The last idea for choosing an estimator: worst-case risk.

Minimize $\sup_\theta R(\theta, \delta)$

The minimum achievable sup risk is called the minimax risk of the estimation problem:

$$r = \inf_\delta \sup_\theta R(\theta, \delta)$$

An estimator $\delta$ is called minimax if it achieves the minimax risk, i.e.,

$$\sup_\theta R(\theta, \delta) = r$$

### Game Theory Interpretation

1. Analyst chooses estimator $\delta$
2. Nature chooses parameter $\theta$ to maximize risk

Note: Nature chooses $\theta$ adversarially, not $X$.

Compare to Bayes where Nature chooses prior from a known distribution (Nature plays a specific mixed strategy).

We will look for Nature's Nash equilibrium strategy.

---

[Up: contents](index.md) · [Least Favorable Priors →](02-least-favorable-priors.md)
