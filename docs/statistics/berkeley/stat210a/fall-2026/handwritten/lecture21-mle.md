---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture21-mle.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture21-mle.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture21-mle.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture21-mle.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Maximum Likelihood Estimator
2) Asymptotic Distribution of MLE
3) Consistency of MLE

---

## Maximum Likelihood Estimation

For a generic dominated family $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ with densities $p_\theta$, a simple estimator for $\theta$ is

$$\hat{\theta}_{\text{MLE}}(X) = \operatorname*{argmax}_{\theta \in \Theta} p_\theta(X)$$
$$= \operatorname*{argmax}_{\theta \in \Theta} \ell(\theta; X)$$

**Remark 1:** $\operatorname*{argmax}$ may not exist, be unique, or be computable

**Remark 2:** doesn't depend on parameterization or base measure, MLE for $g(\theta)$ is $g(\hat{\theta}_{\text{MLE}})$

**Ex** $p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$

$$\ell(\eta; X) = \eta' T(X) - A(\eta) + \log h(X)$$

$$\nabla \ell(\eta; X) = T(X) - \mathbb{E}_\eta T(X)$$

$$\implies \hat{\eta}_{\text{MLE}} \quad \text{solves} \quad T = \mathbb{E}_{\hat{\eta}} T \quad \text{if such } \eta \text{ exists}$$

Because $\nabla^2 \ell(\eta; X) = -\operatorname{Var}_\eta(T)$ is negative definite unless $v' T \stackrel{\text{a.s.}}{=} 0$ (in which case param. redundant)
$\implies$ at most 1 solution exists

Let $\mu = \dot{\psi}(\eta) = \nabla A(\eta)$, $\hat{\eta} = \dot{\psi}^{-1}(T)$

---

**Ex** $X_i \stackrel{\text{iid}}{\sim} e^{\eta T(x) - A(\eta)} h(x) \qquad \eta \in \Xi \subseteq \mathbb{R}$

$\hat{\eta} = \dot{\psi}^{-1}(\bar{T}), \quad \bar{T} = \frac{1}{n}\sum T(X_i)$

Assume $\eta \in \Xi^\circ$. $\dot{\psi}(\eta) = \ddot{A}(\eta) > 0 \quad \forall\, \eta \in \Xi^\circ$

so $\dot{\psi}^{-1} \text{ cts}$, $(\dot{\psi}^{-1})'(\mu) = \frac{1}{\dot{\psi}(\dot{\psi}^{-1}(\mu))} = \frac{1}{\ddot{A}(\eta)}$

**Consistency:** $\bar{T} \xrightarrow{P_\eta} \mu$

**Cts mapping:** $\dot{\psi}^{-1}(\bar{T}) \xrightarrow{P_\eta} \dot{\psi}^{-1}(\mu) = \eta$

Since $\sqrt{n}(\bar{T} - \mu) \Rightarrow N(0, \operatorname{Var}_\eta(T(X_1)))$
$$= N(0, \ddot{A}(\eta))$$
$(\text{Recall } J_1(\mu) = \operatorname{Var}(T)^{-1} = \ddot{A}(\eta)^{-1})$

**Delta method:**

$$\sqrt{n}(\hat{\eta} - \eta) = \sqrt{n}(\dot{\psi}^{-1}(\bar{T}) - \eta)$$

$$\Rightarrow N\left(0, \frac{1}{\ddot{A}(\eta)^2} \cdot \ddot{A}(\eta)\right)$$

$$= N\left(0, \frac{1}{\ddot{A}(\eta)}\right)$$

Recall $J_1(\eta) = \operatorname{Var}_\eta(T(X_i)) = \ddot{A}(\eta)$
$$= \text{Fisher info from 1 obs}$$

$$\hat{\eta} \approx N\left(\eta, \frac{1}{n J_1(\eta)}\right)$$

Asymptotically unbiased, Gaussian, achieves CRLB
$(\operatorname{corr}(\bar{T}, \hat{\eta}) \to 1)$

---

**Ex** $X_1, \dots, X_n \stackrel{\text{iid}}{\sim} \text{Pois}(\theta)$, $\eta = \log \theta$

$\hat{\eta} = \log \bar{X}$, $\sqrt{n}(\bar{X} - \theta) \Rightarrow N(0, \theta)$

$$\sqrt{n}(\hat{\eta} - \eta) = \sqrt{n}(\log \bar{X} - \log \theta)$$

$$\Rightarrow N\left(0, \theta \cdot \frac{1}{\theta^2}\right) \qquad (\text{Delta method})$$

$$= N(0, \theta^{-1})$$

But $\forall \text{ finite } n, \quad \forall \theta > 0$:
$$P_\theta(\hat{\eta} = -\infty) = P_\theta(X_1 = 0)^n$$
$$= e^{-\theta n} > 0$$

$$\implies \mathbb{E}\hat{\eta} = -\infty \qquad \operatorname{Var}(\hat{\eta}) = \infty$$

[MLE can have embarrassing finite-sample performance despite being asy. optimal!]

**Prop:** If $P(B_n) \to 0$, $X_n \Rightarrow X$, $Z_n$ arbitrary then $X_n \mathbf{1}_{B_n^c} + Z_n \mathbf{1}_{B_n} \Rightarrow X$

**Proof** $P(\|Z_n \mathbf{1}_{B_n}\| > \varepsilon) \le P(B_n) \to 0 \implies Z_n \mathbf{1}_{B_n} \xrightarrow{P} 0$

Also $\mathbf{1}_{B_n^c} \xrightarrow{P} 1$, apply Slutsky $\boxtimes$

[So zany behavior has no effect on cvg. in dist]

---

## Asymptotic Efficiency

[The nice behavior of MLE we found in the exponential family case generalizes to a much broader class of models]

**Setting** $X_1, \dots, X_n \stackrel{\text{iid}}{\sim} p_\theta(x) \qquad \theta \in \Theta \subseteq \mathbb{R}^d$

$p_\theta$ "smooth" in $\theta$, e.g.: 2 cts integrable derivs (can be relaxed)

Let $\ell_1(\theta; X_i) = \log p_\theta(X_i)$, $\ell_n(\theta; X) = \sum_{i=1}^n \ell_1(\theta; X_i)$

$$J_1(\theta) = \operatorname{Var}_\theta(\nabla \ell_1(\theta; X_i)) = -\mathbb{E}\left[\nabla^2 \ell_1(\theta; X_i)\right]$$

\$\$J_n(\theta) = \operatorname{Var}_\theta(\nabla \ell_n(\theta; X)) = n J_

---

[Up: contents](../index.md)
