---
title: Cramér-Rao Lower Bound
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Cramér-Rao Lower Bound

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

The score function and Fisher information play critical roles in asymptotic statistics but they have finite-sample implications too. For example, they can be used to derive a lower bound on the variance of any unbiased estimator.

Let $\delta(X)$ be an unbiased estimator for the estimand $g(\theta)\in \RR$, so $g(\theta) = \int \delta p_\theta \,d\mu$. If we repeat the idea of differentiating $g(\theta) = \int \delta(x) e^{\ell(\theta;x)}\,d\mu(x)$ with respect to $\theta$, we obtain
$$
\frac{\partial g}{\partial\theta_j}(\theta) = \int \delta(x) \frac{\partial}{\partial \theta_j} \ell(\theta; x)e^{\ell(\theta;x)}\,d\mu(x),
$$
leading to
$$
\nabla g(\theta) = \EE_\theta\left[\delta(X) S_{\theta}(X)\right] = \Cov_\theta\left(\delta(X), S_{\theta}(X)\right).
$$
This covariance should be thought of as a $d$-vector like $S_\theta(X)$, since $\delta(X)$ is a scalar.

For the case $d=1$ ($\theta\in\RR$), we will write the derivative as $\dot g(\theta) = \frac{d}{d\theta}g(\theta)$. Then we can express the correlation of our estimator and $S_{\theta}(X)$ in terms of $\nabla g(\theta)$ and the Fisher information:
$$
\Corr_\theta^2\left(\delta(X),S_\theta(X) \right) \;=\; \frac{\Cov_\theta^2\left(\delta(X),S_\theta(X) \right)}{\Var_\theta(\delta(X))\Var_\theta(S_\theta(X))} \;=\; \frac{\dot g(\theta)^2}{\Var_\theta(\delta(X)) J(\theta)}.
$$
Rearranging and recalling that a squared correlation must be less than 1, we obtain the *Cram\'{e}r-Rao Lower Bound*  (CRLB)
$$
\Var_\theta(\delta(X)) = \frac{\dot g(\theta)^2}{J(\theta)\Corr_\theta^2(\delta,S_\theta)} \geq \frac{\dot g(\theta)^2}{J(\theta)}
$$
In particular, if $g(\theta)=\theta$, no unbiased estimator can have smaller variance than $1/J(\theta)$. In general, the bound depends on how rapidly the estimand changes with $\theta$.

Is it really "harder" to estimate $g(\theta) = 12\theta$ than it is to estimate $g(\theta) = \theta$? Yes and no: it's harder in the sense that we can expect the variance of an estimator to be $144$ times larger in the first case than the second. But what if this just reflects the fact that $\theta$ is denominated in inches and $g(\theta)$ is denominated in feet? Then we can see clearly that the $\dot{g}(\theta)$ is just keeping track of a unit conversion. Likewise, if $\theta$ has units of feet, we can think of $S_\theta(X)$ as having units of inverse feet, and $J(\theta)$ as having units of inverse square feet.

In finite samples it's typically the case that even the UMVU estimator will not attain the CRLB. An estimator that attains the CRLB is called *efficient*, and more generally the gap $\Corr_\theta^2(\delta,S_\theta)$ is called the *efficiency* of the estimator. Very roughly, if $S_\theta(X)$ is locally capturing all of the relevant information, but $\delta(X)$ has only a $50\%$ "R squared" with it, then $\delta(X)$ is only using $1/2$ of the available information, and we can roughly say that is what accounts for its inefficiency.

As $n\to\infty$ in i.i.d. sampling models, however, there typically will be estimators that achieve the CRLB in the limit (for example, in an asymptotically limiting sense the maximum likelihood estimator will typically be both unbiased and efficient).

For the multivariate case where $\theta$ has dimension $d>1$ (but $g(\theta)\in \RR$ still), we have more generally
$$
\Var_\theta(\delta(X) \geq \nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta).
$$

To derive this identity, note that for any $a \in \RR^d$, we have
$$
\Cov_\theta(\delta(X), a'S_\theta(X)) = a'\Cov_\theta(\delta(X), S_\theta(X)) = a'\nabla g(\theta)
$$
and $\Var_\theta(a'S_\theta(X)) = a'J(\theta)a$. Then we can repeat the derivation above to obtain
$$
\Var_\theta(\delta(X)) \geq \frac{a'\nabla g(\theta)\nabla g(\theta)'a}{a'J(\theta)a}.
$$
We obtain the CRLB $\nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta)$ by maximizing the right-hand side, which is a Rayleigh quotient maximized by $a^* = J(\theta)^{-1}\nabla g(\theta)$.

---

[← Differential Identities and the Fisher Information](04-differential-identities-and-the-fisher-information.md) · [Up: contents](index.md) · [Score fisher Part 06 — →](06-score-fisher-part-06.md)
