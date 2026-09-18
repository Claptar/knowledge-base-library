---
title: Frequentist Motivation
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Frequentist Motivation

(for Frequentists!)

**Outline**

1) Bayes risk, Bayes estimator
2) Examples
3) Conjugate priors

---

Model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ for data $X$

Loss $L(\theta, d)$, Risk $R(\theta, \delta) = \mathbb{E}_\theta[L(\theta, \delta(X))]$

The **Bayes risk** is the average-case risk, integrated wrt some measure $\Lambda$, called **prior**

For now, assume $\Lambda(\Theta) = 1$ (prob. meas.)
Later we will allow to be improper ($\Lambda(\Theta) = \infty$)

Note:
* $\Lambda$ and $c\Lambda$ for $c > 0$ functionally equiv.
* avg risk makes sense even if we don't "believe" $\theta \sim \Lambda$

$$
r_\Lambda(\delta) &= \int_\Theta R(\theta, \delta) \, d\Lambda(\theta) \\
&= \mathbb{E}_{\theta \sim \Lambda}[R(\theta, \delta)] \quad \text{where } \theta \sim \Lambda \quad (\text{since } R(\theta, \delta) = \mathbb{E}[L(\theta, \delta(X)) \mid \theta]) \\
&= \mathbb{E}[L(\theta, \delta(X))] \quad \text{where } \theta \sim \Lambda, \, X \mid \theta \sim P_\theta
$$

$\mathbb{E}$ now means wrt joint distr. of $(\theta, X)$

An estimator $\delta$ minimizing $r_\Lambda(\cdot)$ is called **Bayes** (a **Bayes estimator**). Dep. on $\mathcal{P}, \Lambda, L$

$$
r_\Lambda(\delta) = \mathbb{E}\left[ \mathbb{E}[L(\theta, \delta(X)) \mid X] \right]
$$

Note: we choose this after seeing $X$

---

## Prior, Posterior

Usual interp. of $\Lambda$ is "prior belief about $\theta$ before seeing the data"

Conditional dist. $\Lambda(\theta \mid X)$ called **posterior dist.**
"belief after seeing the data"

**Epistemic uncertainty**:
"I think there is a 50% chance that..."
More on this next time

**Densities**:
* prior $\lambda(\theta)$, likelihood $p_\theta(x)$ or $p(x \mid \theta)$
* **Joint density** $\lambda(\theta) p_\theta(x)$
* **Marginal density** $q(x) = \int_\Theta \lambda(\theta) p_\theta(x) \, d\theta$
* **Posterior density** $\lambda(\theta \mid x) = \frac{\lambda(\theta) p_\theta(x)}{q(x)}$

Bayes estimator depends on posterior:

$$
\delta_\Lambda(x) &= \arg\min_d \mathbb{E}[L(\theta, d) \mid X] \\
&= \arg\min_d \int_\Theta L(\theta, d) \lambda(\theta \mid x) \, d\theta
$$

Solve for Bayes estimator "one $x$ at a time"

---

## Bayes Estimator

Suppose $X \mid \theta \sim P_\theta$, $L(\theta, d) \ge 0$
$r_\Lambda(\delta_0) < \infty$ for some $\delta_0(x)$

Then $\delta_\Lambda(x)$ is Bayes with $r_\Lambda(\delta_\Lambda) < \infty$
iff $\delta_\Lambda(x) \in \arg\min_d \mathbb{E}[L(\theta, d) \mid X=x]$ a.e. $x$
($\mathbb{P}(\delta_\Lambda(X) \notin \arg\min) = 0$)

**Proof**

$(\Rightarrow)$ Let $\delta$ be any other estimator

$$
r_\Lambda(\delta) &= \mathbb{E}\left[ \mathbb{E}[L(\theta, \delta(X)) \mid X=x] \right] \\
&\ge \mathbb{E}\left[ \mathbb{E}[L(\theta, \delta_\Lambda(X)) \mid X=x] \right] \\
&= r_\Lambda(\delta_\Lambda) \\
&< \infty \quad (\text{take } \delta = \delta_0)
$$

$(\Leftarrow)$ Define $E_x(d) = \mathbb{E}[L(\theta, d) \mid X=x]$

Let $\delta^*(x) = \begin{cases}
\delta_\Lambda(x) & \text{if } \delta_\Lambda(x) \in \arg\min E_x \\
\delta_0(x) & \text{if } E_x(\delta_0(x)) < E_x(\delta_\Lambda(x)) \\
d^*(x) & \text{otherwise, where } E_x(d^*) < E_x(\delta_\Lambda(x))
\end{cases}$

Then $E_x(\delta^*(x)) \le \min(E_x(\delta_0(x)), E_x(\delta_\Lambda(x))) \quad \forall x$
with ineq. strict on a set of measure $> 0$. $\boxtimes$

---

## Posterior Mean

If $L(\theta, d) = (g(\theta) - d)^2$ then the Bayes estimator is the **posterior mean**:

$$
\mathbb{E}\left[ (g(\theta) - d)^2 \mid X \right] &= \mathbb{E}\left[ \left( g(\theta) - \mathbb{E}[g(\theta) \mid X] + \mathbb{E}[g(\theta) \mid X] - d \right)^2 \mid X \right] \\
&= \operatorname{Var}(g(\theta) \mid X) + \left( \mathbb{E}[g(\theta) \mid X] - d \right)^2
$$

(why is the cross-term 0?)

$\Rightarrow \delta_\Lambda(x) = \mathbb{E}[g(\theta) \mid X=x]$

**Weighted sq. error**:

$L(\theta, d) = w(\theta) (g(\theta) - d)^2 \quad \text{e.g. } \left(\frac{\theta - d}{\theta}\right)^2 \text{ sq. rel. error}$

$$
\mathbb{E}\left[ (d - g(\theta))^2 w(\theta) \mid X \right] &= d^2 \mathbb{E}[w(\theta) \mid X] - 2d \mathbb{E}[w(\theta) g(\theta) \mid X] \\
&\quad + \mathbb{E}[w(\theta) g(\theta)^2 \mid X] \quad (\text{no dep. on } d)
$$

$\min$ at $d = \frac{\mathbb{E}[w(\theta) g(\theta) \mid X]}{\mathbb{E}[w(\theta) \mid X]} \quad (= \delta_\Lambda(x))$

---

---

[Up: contents](index.md) · [Example: Beta-Binomial →](02-example-beta-binomial.md)
