---
title: 6 Examples
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 6 Examples

**Example: i.i.d. sample**

Assume $X_1, \ldots, X_n \simiid p_\theta^{(1)}(x)$, for $\theta \in \Theta \subseteq \RR^d$.

Assume additionally that $p_\theta^{(1)}$ is “regular:” it has common support, and finite derivative w.r.t. $\theta$.

Then the full data density is $p_\theta(x) = \prod_i p_\theta^{(1)}(x_i)$.

Define the single-sample log-likelihood $\ell_1(\theta;x_i) = \log p_\theta^{(1)}(x_i)$; then we have $\ell(\theta;x) = \sum_i \ell_1(\theta;x_i)$.

Then the Fisher information for the full sample is

$$
J(\theta) = \Var_\theta(\nabla \ell(\theta; X)) = \sum_{i=1}^n \Var_\theta(\nabla \ell_1(\theta; X_i)) = n J_1(\theta),
$$

 where $J_1(\theta) = \Var_\theta(\nabla\ell(\theta; X_1))$ is the Fisher information for a single sample.

As a result, we see that the Information bound scales like $n^{-1}$ for regular families; in other words, the standard deviation of an estimator should scale roughly like $1/\sqrt{n}$.

**Example: exponential family**

Suppose we have an exponential family of the form

$$
p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x).
$$

The log-likelihood is $\ell(\eta;X) = \eta'T(X) - A(\eta) + \log h(X)$, and its gradient (the score) is

$$
\nabla \ell(\eta;X) = T(X) - \nabla A(\eta) = T(X) - \EE_\eta T(X).
$$

 Since $\EE_\eta T(X)$ is nonrandom, the variance is

$$
J(\eta) = \Var_\eta (T(X)) = \nabla^2 A(\eta).
$$

We could alternatively derive the Fisher information from taking a second derivative with respect to $\eta$, giving

$$
\nabla^2\ell(\eta;X) = -\nabla^2 A(\eta),
$$

 which is deterministically equal to $-\Var_\eta(T(X))$, so we have confirmed the identity $J(\eta) = -\EE_\eta[\nabla^2 \ell(\eta;X)]$.

**Example: Curved exponential family**

Next, consider a curved version of the previous family, parameterized by $\theta \in \RR$:

$$
p_\theta(x) = e^{\eta(\theta)'T(x) - B(\theta)}h(x),\quad \text{ with } B(\theta) = A(\eta(\theta))
$$

 Again, the log-likelihood is

$$
\ell(\theta;X) = \eta(\theta)'T(x) - B(\theta)  + \log h(x),
$$

 and its first derivative is

$$
\begin{aligned}
\dot{\ell}(\theta;X) &= \dot{\eta}(\theta)'T(X) - \dot{\eta}(\theta)'\nabla_\eta A(\eta(\theta))\\
&= \dot{\eta}(\theta) '\left(T(X) - \nabla_\eta A(\eta(\theta))\right)\\
&= \dot{\eta}(\theta)'(T(X) - \EE_\theta T(X)).\end{aligned}
$$

As a result, the Fisher information is

$$
J(\theta) = \Var_\theta(\dot{\eta}(\theta)'T(X)) =  \dot{\eta}(\theta)'\Var_\theta(T(X))\dot{\eta}(\theta).
$$

 Note in this model $\dot{\eta}'T(X)$ is a “local complete sufficient statistic” for the model near $\theta$.

## 7 Efficiency {.anchored number="7" anchor-id="efficiency"}

The CRLB is not necessarily attainable.

We define the efficiency of an unbiased estimator as:

$$
\text{eff}_\delta(\theta) = \frac{\text{CRLB}(\theta)}{\Var_\theta(\delta)} \leq 1,
$$

We say $\delta(X)$ is *efficient* if $\text{eff}_\delta(\theta) = 1$ for all $\theta$.

For $g(\theta)=\theta\in \RR$, the efficiency depends on how correlated $\delta(X)$ is with the score:

$$
\begin{aligned}\text{eff}_\delta(\theta) &= \frac{\Cov_\theta(\delta(X), \dot{\ell}(\theta;X))^2}{\Var_\theta(\delta(X)) \cdot \Var_\theta(\dot{\ell}(\theta;X))}\\
&= \Corr_\theta(\delta,\dot{\ell}(\theta))^2
\end{aligned}
$$

Thus, an efficient estimator for $\theta$ is one that is perfectly correlated with the score. This is rarely achieved in finite samples, but we can often approach it asymptotically as $n \to \infty$.

---

[← 5 Cramér-Rao Lower Bound](03-5-cramér-rao-lower-bound.md) · [Up: contents](index.md)
