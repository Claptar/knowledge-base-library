---
title: Differential Identities and the Fisher Information
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Differential Identities and the Fisher Information

Assuming enough regularity, we can arrive at some important differential identities by differentiating both sides of the equation

$$1 = \int_\cX e^{\ell(\theta;x)}\,d\mu(x).$$

Differentiating both sides with respect to $\theta_j$, we obtain $$0 = \int_\cX \frac{\partial}{\partial \theta_j} \ell(\theta; x) e^{\ell(\theta; x)}\,d\mu(x) = \EE_\theta \left[\frac{\partial}{\partial\theta_j}\ell(\theta;X)\right].$$ Collecting these identities into a vector, we obtain $$\EE_\theta [\nabla \ell(\theta; X)] = 0.$$ Importantly, note that this identity only holds if the $\theta$ in the subscript (defining the distribution with respect to which the expectation is taken) matches the $\theta$ at which the gradient is being evaluated.

If we differentiate the identity a second time with respect to $\theta_k$, we obtain $$0 = \int_\cX \left(\frac{\partial^2\ell}{\partial \theta_j\partial\theta_k} + \frac{\partial \ell}{\partial \theta_j}\frac{\partial \ell}{\partial\theta_k}\right) e^{\ell}\,d\mu = \EE_\theta\left[\frac{\partial^2\ell}{\partial \theta_j\partial\theta_k}\right] + \EE_\theta\left[\frac{\partial \ell}{\partial \theta_j}\frac{\partial \ell}{\partial \theta_k}\right]
%= \EE_\theta\left[\frac{\partial^2\ell}{\partial \theta_j\partial\theta_k}\right] + \Cov_\theta\left(\frac{\partial \ell}{\partial \theta_j},\frac{\partial \ell}{\partial \theta_k}\right).
$$ Again collecting these identities into a matrix, and noting that $$\EE_\theta\left[\frac{\partial \ell}{\partial \theta_j}\frac{\partial \ell}{\partial \theta_k}\right] = \Cov_\theta\left(\frac{\partial \ell}{\partial \theta_j},\frac{\partial \ell}{\partial \theta_k}\right),$$ we obtain $$\Var_\theta\left(\nabla\ell(\theta;X)\right) = \EE_\theta\left[-\nabla^2\ell(\theta;X)\right],$$ again with the important observation that the $\theta$ in both subscripts must match the $\theta$ where the first and second derivatives are evaluated.

The left-hand side of the last equation, the variance of the score, is called the *Fisher Information* matrix $$ J(\theta) := \Var_\theta(\nabla\ell(\theta;X)). $$ Note $J(\theta)$ is always positive semidefinite. It is possible to extend this definition to certain models where $\ell(\theta;x)$ is not differentiable with respect to $\theta$, such as the Laplace location family. However we will not explore these generalizations.

---

[← Under construction](01-under-construction.md) · [Up: contents](index.md) · [Cramér-Rao Lower Bound →](03-cramér-rao-lower-bound.md)
