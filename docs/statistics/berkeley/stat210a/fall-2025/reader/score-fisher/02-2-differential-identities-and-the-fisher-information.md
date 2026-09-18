---
title: 2 Differential Identities and the Fisher Information
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Differential Identities and the Fisher Information

Assuming enough regularity, we can arrive at some important differential identities by differentiating both sides of the equation

$$
1 = \int_\cX e^{\ell(\theta;x)}\,d\mu(x).
$$

Differentiating both sides with respect to $\theta_j$, we obtain

$$
0 = \int_\cX \frac{\partial}{\partial \theta_j} \ell(\theta; x) e^{\ell(\theta; x)}\,d\mu(x) = \EE_\theta \left[\frac{\partial}{\partial\theta_j}\ell(\theta;X)\right].
$$

 Collecting these identities into a vector, we obtain

$$
\EE_\theta [S_\theta(X)] = 0.
$$

 Importantly, note that this identity only holds if the two values of $\theta$ in the above expression match each other. So if the analyst calculates the score function at some reference value $\theta_0$, but the true parameter is some other value $\theta \neq \theta_0$, we typically would have $\EE_\theta[S_{\theta_0}(X)] \neq 0$.

If we differentiate the identity a second time with respect to $\theta_k$, we obtain

$$
0 = \int_\cX \left(\frac{\partial^2\ell}{\partial \theta_j\partial\theta_k} + \frac{\partial \ell}{\partial \theta_j}\frac{\partial \ell}{\partial\theta_k}\right) e^{\ell}\,d\mu = \EE_\theta\left[\frac{\partial^2\ell}{\partial \theta_j\partial\theta_k}\right] + \EE_\theta\left[\frac{\partial \ell}{\partial \theta_j}\frac{\partial \ell}{\partial \theta_k}\right]
%= \EE_\theta\left[\frac{\partial^2\ell}{\partial \theta_j\partial\theta_k}\right] + \Cov_\theta\left(\frac{\partial \ell}{\partial \theta_j},\frac{\partial \ell}{\partial \theta_k}\right).
$$

Again collecting these identities into a matrix, and noting that

$$
\EE_\theta\left[\frac{\partial \ell}{\partial \theta_j}\frac{\partial \ell}{\partial \theta_k}\right] = \Cov_\theta\left(S_{\theta,j}(X),S_{\theta,k}(X)\right),
$$

 we obtain

$$
\Var_\theta\left(S_{\theta}(X)\right) = \EE_\theta\left[-\nabla^2\ell(\theta;X)\right],
$$

 again with the important observation that the equality holds only if the $\theta$ in both subscripts matches the $\theta$ where we are calculating derivatives.

The left-hand side of the last equation, the variance of the score, is called the *Fisher Information* matrix

$$
J(\theta) := \Var_\theta(S_\theta(X)).
$$

 Note $J(\theta)$ is always positive semidefinite.

We will not discuss in detail the regularity conditions on $\ell$ (basically, one or two “tame” derivatives) that make these identities work; the correct regularity conditions are complicated. But the score function is useful even certain models where $\ell(\theta;x)$ is not differentiable with respect to $\theta$, such as the Laplace location family.

---

[← 1 Score Function](01-1-score-function.md) · [Up: contents](index.md) · [3 Cramér-Rao Lower Bound →](03-3-cramér-rao-lower-bound.md)
