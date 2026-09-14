---
title: Likelihood-Based Inference
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/likelihood-inference.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/likelihood-inference.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Likelihood-Based Inference

**Source:** [`reader/likelihood-inference.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/likelihood-inference.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Setting

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} p_\theta(x)$, $p_\theta \in \cP$, smooth in $\theta$

Assume:
- $\mathbb{E}_\theta[\nabla \ell_\theta(X)] = 0$
- $\text{Var}_\theta[\nabla \ell_\theta(X)] = \mathbb{E}_\theta[-\nabla^2 \ell_\theta(X)] = J(\theta) > 0$
- MLE $\hat{\theta}$ Consistent

Then if $\theta = \theta_0$:
- $\nabla \ell_n(\theta_0; X) \sim N(0, nJ(\theta_0))$
- $-\nabla^2 \ell_n(\theta_0; X) \xrightarrow{p} nJ(\theta_0)$

Used $\theta = \hat{\theta} + J^{-1}(\theta_0) \nabla \ell_n(\theta_0; X)/n + o_p(n^{-1/2})$
to get $\sqrt{n}(\hat{\theta} - \theta_0) \sim N(0, J^{-1}(\theta_0))$

Can use this for inference on $\theta_0$

---

[Up: contents](index.md) · [Wald-Type Confidence Regions →](02-wald-type-confidence-regions.md)
