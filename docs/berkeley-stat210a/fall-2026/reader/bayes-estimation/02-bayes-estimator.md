---
title: Bayes estimator
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Bayes estimator

**Source:** [`reader/bayes-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Whatever our interpretation of the marginal expectation that defines $r_\Lambda$, the way to minimize it is the same: we simply choose $\delta(X)$ to minimize the *conditional* expectation of the loss given the data $X$.

**Theorem: Bayes estimation**

Assume $r_\Lambda(\delta_0) < \infty$ for some estimator $\delta_0$. Then $\delta_{\Lambda}$ is Bayes with $r_\Lambda(\delta_{\Lambda}) < \infty$, if and only if
$$
\delta_\Lambda(x) \in \argmin \EE[ L(\theta, d) \mid X=x], \quad \text{ for a.e. } x,
$$
meaning the marginal probability that $\delta(X)$ does not minimize the conditional expectation is 0.

*Proof:* First, we prove the reverse direction. If $\delta$ is any other estimator, then by assumption we have
$$
\EE[L(\theta, \delta_\Lambda(X)) \mid X] \;\stackrel{\text{a.s.}}{\leq}\; \EE[L(\theta, \delta(X)) \mid X],
$$
and marginalizing over $X$ gives the desired result. Taking $\delta = \delta_0$ establishes that $r_\Lambda(\delta_\Lambda) \leq r_\Lambda(\delta_0) < \infty$.

For the forward direction, assume $r_\Lambda(\delta_\Lambda) < \infty$; otherwise $\delta_0$ has better Bayes risk and there is nothing to prove. Define $E_x(d) = \EE[L(\theta; d) \mid X=x]$. By assumption, there is some $\varepsilon > 0$ with $\PP(X \in A_\varepsilon) > 0$, where
$$
A_\varepsilon = \left\{x:\; E_x(\delta_\Lambda(x)) - \inf_d E_x(d) > \varepsilon \right\}.
$$

For any $x \in A_\varepsilon$, we can find $\delta^*(x)$ such that
$$
E_x(\delta^*(x)) \leq \min\{E_x(\delta_\Lambda(x)) - \varepsilon, E_x(\delta_0(x))\},
$$
and for $x \in A_\varepsilon^C$ take $\delta^*(x)=\delta_\Lambda(x)$. Then
$$
E_x(\delta_\Lambda(x)) - E_x(\delta^*(x)) \geq \varepsilon 1\{x \in A_\varepsilon\}.
$$
Taking expectations gives
$$
r_\Lambda(\delta_\Lambda) - r_\Lambda(\delta^*) \geq \varepsilon \PP\{X \in A_\varepsilon\} > 0,
$$
so $\delta_\Lambda$ is not Bayes. $\blacksquare$

**Example: Squared error loss**

The form of the Bayes estimator is particularly nice in the case of the squared error loss $L(\theta, d) = (g(\theta)-d)^2$. Then, we can decompose the conditional expected loss as
$$
\begin{aligned}
\EE[(g(\theta)-d)^2 \mid X]
&\;=\; \EE\Big[\big(g(\theta) - \EE[g(\theta) \mid X] + \EE[g(\theta) \mid X] - d\big)^2 \mid X\Big]\\
&\;=\; \Var(g(\theta) \mid X) + (\EE[g(\theta) \mid X] - d)^2,
\end{aligned}
$$
noting that the cross-term $(g(\theta) - \EE[g(\theta) \mid X])\cdot(\EE[g(\theta) \mid X] - d)$ has zero conditional expectation.

The optimal choice of $d$ is $\EE[g(\theta) \mid X]$, which zeroes the second term, giving Bayes risk $\EE[\Var(g(\theta) \mid X)]$.


**Example: Weighted squared error loss**

An alternative loss is the *weighted* squared error loss, which gives more weight to some $\theta$ values than others:
$$
L(\theta, d) = w(\theta)(g(\theta) - d)^2.
$$
For example, we could care about the *relative* squared error $\left(\frac{g(\theta)-d}{g(\theta)}\right)^2$, in which case $w(\theta) = g(\theta)^{-2}$. Then, our Bayes estimator will minimize
$$
\EE[w(\theta)(g(\theta)-d)^2 \mid X] = d^2 \EE[w(\theta) \mid X] - 2d \EE[w(\theta)g(\theta) \mid X] + \EE[w(\theta)g(\theta)^2 \mid X].
$$
Minimizing this quadratic in $d$ gives the Bayes estimator
$$
\delta_\Lambda(X) = \frac{\EE[w(\theta)g(\theta) \mid X]}{\EE[ w(\theta) \mid X]}
$$

---

[← Frequentist motivation for a Bayes Estimator](01-frequentist-motivation-for-a-bayes-estimator.md) · [Up: contents](index.md) · [Conjugate priors →](03-conjugate-priors.md)
