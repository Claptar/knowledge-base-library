---
title: Frequentist Motivation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Frequentist Motivation

### Outline

1) Bayes risk, Bayes estimator
2) Examples
3) Conjugate priors

---

Model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ for data $X$

Loss $L(\theta, d)$, Risk $R(\theta, \delta) = \mathbb{E}_\theta[L(\theta, \delta(X))]$

The **Bayes risk** is the average-case risk, integrated wrt some measure $\Lambda$, called prior.

For now, assume $\Lambda(\Theta) = 1$ (prob. meas.)
Later we will allow to be improper ($\Lambda(\Theta) = \infty$)

Note:
* $\Lambda$ and $c\Lambda$ for $c > 0$ functionally equiv.
* avg risk makes sense even if we don't "believe" $\theta \sim \Lambda$

$$
\begin{aligned}
r_\Lambda(\delta) &= \int_\Theta R(\theta, \delta) \, d\Lambda(\theta) \\
&= \mathbb{E}_{\theta \sim \Lambda}[R(\theta, \delta)] \quad \text{where } \theta \sim \Lambda \quad \left(R(\theta, \delta) = \mathbb{E}[L(\theta, \delta(X)) \mid \theta]\right) \\
&= \mathbb{E}[L(\theta, \delta(X))] \quad \text{where } \theta \sim \Lambda, \, X \mid \theta \sim P_\theta
\end{aligned}
$$

$\mathbb{E}$ now means wrt joint distr. of $(\theta, X)$

An estimator $\delta$ minimizing $r_\Lambda(\cdot)$ is called **Bayes** (a **Bayes estimator**). Dep. on $\mathcal{P}, \Lambda, L$

$$
r_\Lambda(\delta) = \mathbb{E}\left[ \mathbb{E}[L(\theta, \delta(X)) \mid X] \right]
$$
*(minimize one $X$ at a time)*
*Note: we choose this after seeing $X$*

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
* **Joint density**: $\lambda(\theta) p_\theta(x)$
* **Marginal density**: $q(x) = \int_\Theta \lambda(\theta) p_\theta(x) \, d\theta$
* **Posterior density**: $\lambda(\theta \mid x) = \frac{\lambda(\theta) p_\theta(x)}{q(x)}$

Bayes estimator depends on posterior:
$$
\begin{aligned}
\delta_\Lambda(x) &= \arg\min_d \mathbb{E}[L(\theta, d) \mid X] \\
&= \arg\min_d \int_\Theta L(\theta, d) \lambda(\theta \mid x) \, d\theta
\end{aligned}
$$

Solve for Bayes estimator "one $x$ at a time"

---

---

[Up: contents](index.md) · [Bayes Estimator →](02-bayes-estimator.md)
