---
title: 5 Cramér-Rao Lower Bound
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 5 Cramér-Rao Lower Bound

Let $\delta(X)$ be any real-valued statistic. Let $g(\theta) = \EE_\theta[\delta]$, so $\delta$ is an unbiased estimator for $g(\theta)$. If we repeat the idea of differentiating $g(\theta) = \int \delta(x) e^{\ell(\theta;x)}\,d\mu(x)$ with respect to $\theta_j$ for each $j$, and collect the resulting partial derivatives into a vector, we obtain

$$
\nabla g(\theta) = \int \delta(x) \nabla \ell(\theta;x) e^{\ell(\theta;x)}\,d\mu(x) = \EE_\theta\left[\delta(X) \nabla\ell(\theta;X)\right] = \Cov_\theta\left(\delta(X), \nabla\ell(\theta;X)\right).
$$

 Combining these results with the Cauchy-Schwarz inequality gives us the *Cramér-Rao Lower Bound*, also known as the *Information lower bound*. For a single parameter ($d=1$), we have

$$
\Var_\theta(\delta(X)) \cdot \Var_\theta(\dot{\ell}(\theta;X)) \geq \Cov_\theta(\delta(X), \dot{\ell}(\theta; X))^2,
$$

 so after rearranging terms and applying identities,

$$
\Var_\theta(\delta(X)) \geq \frac{\dot{g}(\theta)^2}{J(\theta)}.
$$

For the multivariate case ($d>1$), we have more generally

$$
\Var_\theta(\delta(X) \geq \nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta).
$$

 The interpretation of this identity is that no unbiased estimator for $g(\theta)$ can have variance smaller than $\nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta)$. In particular, if $g(\theta) = \theta_j$, no estimator can have variance smaller than $(J(\theta)^{-1})_{jj}$.

$$
\Var_\theta(\delta) \geq \Var_\theta(\delta(X)) \Cov_\theta(\delta, \nabla l_\theta(X))I(\theta)^{-1}\Cov_\theta(\delta, \nabla l_\theta(X))' = g'(\theta)I(\theta)^{-1}g'(\theta)'
$$

Expand to see proof

For any $a \in \RR^d$, we can write

$$
\begin{aligned}
\Var_\theta(\delta(X)) \cdot a'J(\theta)a &= \Var_\theta(\delta)\Var_\theta(a'\nabla\ell(\theta;X))\\
&\geq \Cov_\theta(\delta(X), a'\nabla\ell(\theta;X))^2\\
&= \left(a'\nabla \Cov_\theta(\delta, \nabla\ell(\theta))\right)^2\\
&= (a'\nabla g(\theta))^2.
\end{aligned}
$$

Thus we obtain for all nonzero $a \in \RR^d$,

$$
\Var_\theta(\delta(X)) \geq \frac{(a'\nabla g(\theta))^2}{a'J(\theta)a}.
$$

We obtain the result by optimizing the bound, with $a = J(\theta)^{-1}\nabla g(\theta)$ (show this as an exercise).

---

[← 4 Differential Identities and the Fisher Information](02-4-differential-identities-and-the-fisher-information.md) · [Up: contents](index.md) · [6 Examples →](04-6-examples.md)
