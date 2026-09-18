---
title: Empirical Bayes
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-jamesstein.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture12-jamesstein.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-jamesstein.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-jamesstein.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Empirical Bayes

Common situation in hierarchical Bayes models:

$$\zeta \sim \lambda(\zeta) \leftarrow \text{one draw } \Rightarrow \text{hard to justify prior}$$
$$\text{lots of info } \Rightarrow \text{prior doesn't matter}$$

$$\theta_i \mid \zeta \overset{iid}{\sim} \pi_\zeta(\theta) \leftarrow \text{only } X_i \text{ informative } \Rightarrow \text{prior helps}$$
$$\text{many draws } \Rightarrow \text{can check fit}$$

$$X_i \mid \zeta, \theta \overset{ind.}{\sim} P_{\theta_i}(x) \quad i = 1, \ldots, d$$

Hybrid approach: treat $\zeta$ as fixed
- Estimate $\zeta$ based on observed data
- Plug in $\hat{\zeta}$ as though known

Ex.
$$\theta_i \sim N(0, \tau^2) \quad \tau^2 \text{ fixed, unknown}$$
$$X_i \mid \theta \sim N(\theta_i, 1) \quad i = 1, \ldots, d$$

Bayes estimator if we knew $\tau^2$ is
$$\delta_i(X) = (1 - \zeta) X_i, \quad \zeta = \frac{1}{1 + \tau^2}$$

To estimate $\zeta$, use $X \sim N_d(0, \zeta^{-1} I_d) = \left(\frac{\zeta}{2\pi}\right)^{d/2} e^{-\zeta \|X\|^2 / 2} \quad \text{(}\downarrow \text{sufficient)}$

$$\|X\|^2 \sim \zeta^{-1} \chi_d^2 \implies \hat{\zeta}_{\text{MLE}}^{-1} = d / \|X\|^2$$

Plug in: $\delta_i(X) = (1 - d / \|X\|^2) X_i$

If $d$ large, should be near-optimal

---

## James-Stein Estimator

James & Stein proposed instead ($d \ge 3$):

$$\delta_{\text{JS}, i}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right) X_i$$

**Emp Bayes Motivation:** $\frac{d-2}{\|X\|^2}$ is UMVUE of $\zeta$

**Prop:** If $Y \sim \chi_d^2 = \text{Gamma}(\frac{d}{2}, 2)$, $d \ge 3$ then
$$\mathbb{E}[1/Y] = \frac{1}{d-2}$$

**Proof:**
$$\mathbb{E}\left[\frac{1}{Y}\right] = \int_0^\infty \frac{1}{y} \frac{1}{2^{d/2}\Gamma(\frac{d}{2})} \cdot y^{\frac{d}{2}-1} e^{-y/2}\,dy$$

$$= \frac{2^{\frac{(d-2)}{2}}\Gamma(\frac{d-2}{2})}{2^{d/2}\Gamma(\frac{d}{2})} \int_0^\infty \underbrace{\frac{1}{2^{\frac{(d-2)}{2}}\Gamma(\frac{d-2}{2})} y^{\frac{(d-2)}{2}-1} e^{-y/2}}_{\chi_{d-2}^2 \text{ density}}\,dy$$

Now, use $\Gamma(x) = (x-1)\Gamma(x-1) \quad \forall\, x > 0$

$$\cdots = \frac{1}{2} \cdot \frac{1}{\frac{(d-2)}{2}} = \frac{1}{d-2} \quad \boxtimes$$

$$\zeta \|X\|^2 \sim \chi_d^2 \implies \zeta^{-1} \mathbb{E}_\zeta\left[\frac{1}{\|X\|^2}\right] = \frac{1}{d-2}$$

$$\implies \hat{\zeta} = \frac{d-2}{\|X\|^2} \quad \text{UMVUE}$$

---

## James-Stein Paradox

Back to non-Bayesian Gaussian seq. model:
$$X_i \overset{iid}{\sim} N_d(\theta, \sigma^2 I_d), \quad \underset{i=1,\ldots,n}{\theta \in \mathbb{R}^d \text{ (fixed)},} \quad \sigma^2 > 0 \text{ known}$$

Shocking result of James & Stein (1956):

For $d \ge 3$, the sample mean $\bar{X} = \frac{1}{n} \sum X_i$ is **inadmissible** as an estimator of $\theta$ under squared error loss:

For $\delta_{\text{JS}}(X) = \left(1 - \frac{(d-2)\sigma^2/n}{\|\bar{X}\|^2}\right) \bar{X}$

$$\text{MSE}(\theta, \delta_{\text{JS}}) < \text{MSE}(\theta, \bar{X}) \quad \forall\,\theta \in \mathbb{R}^d \quad (!!!)$$

$\bar{X}$ is UMVU, Minimax, objective Bayes, ....

Note: Might as well take $n=1$ (suff. reduction) $\implies (1 - \frac{d-2}{\|X\|^2})X$

Note this result holds **without** assumption of Bayes model on $\theta$: true for $\theta = (500, -10^{10}, 4)$

Nothing special about $0$: for any $\theta_0 \in \mathbb{R}^d$
$$\delta(X) = \theta_0 + \left(1 - \frac{d-2}{\|X - \theta_0\|^2}\right)(X - \theta_0)$$
also dominates $X$

Deep implication: shrinkage makes sense even without Bayes justification.

---

## Linear shrinkage w/o Bayesian assumptions

Gaussian seq. model: $X \sim N_d(\theta, I_d)$, fixed $\theta \in \mathbb{R}^d$

Let $\delta_\zeta(X) = (1 - \zeta) X$, $\zeta$ is tuning parameter

$$\begin{aligned}
\underset{\uparrow \\ \text{(MSE)}}{R(\theta; \delta_\zeta)} &= \|\theta - \mathbb{E} \delta_\zeta(X)\|^2 + \sum_i \text{Var}((1-\zeta)X_i) \\
&= \underbrace{\zeta^2 \|\theta\|^2}_{\text{bias}^2} + \underbrace{d(1-\zeta)^2}_{\text{variance}}
\end{aligned}$$

What is optimal $\zeta$?

$$\frac{d}{d\zeta} R(\theta; \delta_\zeta) = 2\zeta \|\theta\|^2 - 2(1-\zeta)d$$

$$\implies \text{minimizer } = \zeta^*(\theta) = \frac{d}{d + \|\theta\|^2} = \frac{1}{1 + \|\theta\|^2 / d}$$

$\zeta^*$ always $> 0$, but $\to 0$ as $\theta \to \infty$

What if we estimate $\zeta^*(\theta)$?
How does adaptivity of $\hat{\zeta}^*(X)$ affect MSE?

---

## Stein's Lemma

Useful tool for computing / estimating risk in Gaussian estimation problems

**Theorem (Stein's Lemma, univariate):**

Suppose $X \sim N(\theta, \sigma^2)$
$h(x): \mathbb{R} \to \mathbb{R}$ differentiable, $\mathbb{E}|h'(x)| < \infty$
Then
$$\mathbb{E}[(X - \theta) h(X)] = \sigma^2 \mathbb{E}[h'(X)]$$
$$\overset{//}{\text{Cov}(X, h(X))}$$

**Proof** Note we can assume wlog $h(0) = 0$ (why?)

First assume $\theta = 0$, $\sigma^2 = 1$:

Note $\mathbb{E}[X h(X)] = \int_0^\infty x h(x) \phi(x)\,dx + \int_{-\infty}^0 x h(x) \phi(x)\,dx$

$$\begin{aligned}
\int_0^\infty x h(x) \phi(x)\,dx &= \int_0^\infty x \left[\int_0^x h'(y)\,dy\right] \phi(x)\,dx \\
&= \int_0^\infty \int_0^\infty \mathbf{1}_{\{y < x\}} x h'(y) \phi(x)\,dx\,dy \\
&= \int_0^\infty h'(y) \left[\int_y^\infty x \phi(x)\,dx\right] dy \\
&= \int_0^\infty h'(y) \phi(y)\,dy
\end{aligned}$$

---

In the last step we have used:
$$\frac{d}{dx} \left[\frac{1}{\sqrt{2\pi}} e^{-x^2/2}\right] = -x \cdot \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

Similar argument shows $\int_{-\infty}^0 x h(x) \phi(x)\,dx = \int_{-\infty}^0 h'(x) \phi(x)\,dx$

\$\$\implies \

---

[← Empirical Bayes, James-Stein](01-empirical-bayes-james-stein.md) · [Up: contents](index.md)
