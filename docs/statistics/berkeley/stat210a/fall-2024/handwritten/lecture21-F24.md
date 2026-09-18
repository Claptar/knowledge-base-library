---
title: Lecture 21 — F24
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture21-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture21-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture21-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture21-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 21 — F24

11/4/2021

## Outline

1) Maximum Likelihood Estimator
2) Asymptotic Distribution of MLE
3) Consistency of MLE

---

## Maximum Likelihood Estimation

For a generic dominated family $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ with densities $p_\theta$, a simple estimator for $\theta$ is

$$
\hat{\theta}_{\text{MLE}}(X) = \operatorname{argmax}_{\theta \in \Theta} p_\theta(X)
$$
$$
= \operatorname{argmax}_{\theta \in \Theta} \ell(\theta; X)
$$

**Remark 1:** $\operatorname{argmax}$ may not exist, be unique, or be computable

**Remark 2:** doesn't depend on parameterization or base measure, MLE for $g(\theta)$ is $g(\hat{\theta}_{\text{MLE}})$

**Ex** $p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$

$$
\ell(\eta; x) = \eta' T(x) - A(\eta) + \log h(x)
$$
$$
\nabla \ell(\eta; x) = T(x) - \mathbb{E}_\eta T(X)
$$
$$
\Rightarrow \hat{\eta}_{\text{MLE}} \text{ solves } T = \mathbb{E}_{\hat{\eta}} T \quad \text{if such } \eta \text{ exists}
$$

Because $\ddot{\ell}(\eta; x) = -\operatorname{Var}_\eta(T)$ is negative definite unless $v' T \overset{\text{a.s.}}{=} 0$ (in which case param. redundant)
$\Rightarrow$ at most 1 solution exists

Let $\mu = \dot{A}(\eta) = \nabla A(\eta)$, $\hat{\eta} = \dot{A}^{-1}(T)$

---

**Ex** $X_i \overset{\text{iid}}{\sim} e^{\eta T(x) - A(\eta)} h(x) \qquad \eta \in \Xi \subseteq \mathbb{R}$

$\hat{\eta} = \dot{A}^{-1}(\bar{T}), \quad \bar{T} = \frac{1}{n} \sum T(X_i)$

Assume $\eta \in \Xi^\circ$. $\dot{\psi}(\eta) = \ddot{A}(\eta) > 0 \quad \forall \eta \in \Xi^\circ$
so $\dot{\psi}^{-1}$ cts, $(\dot{\psi}^{-1})'(\mu) = \frac{1}{\dot{\psi}(\dot{\psi}^{-1}(\mu))} = \frac{1}{\ddot{A}(\eta)}$

**Consistency:** $\bar{T} \xrightarrow{P_\eta} \mu$
**Cts mapping:** $\dot{\psi}^{-1}(\bar{T}) \xrightarrow{P_\eta} \dot{\psi}^{-1}(\mu) = \eta$

Since $\sqrt{n}(\bar{T} - \mu) \Rightarrow \mathcal{N}(0, \operatorname{Var}_\eta(T(X_1)))$
$$= \mathcal{N}(0, \ddot{A}(\eta))$$
$(\text{Recall } J_1(\mu) = \operatorname{Var}(T)^{-1} = \ddot{A}(\eta)^{-1})$

**Delta method:**
$$
\sqrt{n}(\hat{\eta} - \eta) = \sqrt{n}(\dot{\psi}^{-1}(\bar{T}) - \eta)
$$
$$
\Rightarrow \mathcal{N}\left(0, \frac{1}{\ddot{A}(\eta)^2} \cdot \ddot{A}(\eta)\right)
$$
$$
= \mathcal{N}\left(0, \frac{1}{\ddot{A}(\eta)}\right)
$$

Recall $J_1(\eta) = \operatorname{Var}_\eta(T(X_i)) = \ddot{A}(\eta)$
$= \text{Fisher info from 1 obs}$

$$
\hat{\eta} \approx \mathcal{N}\left(\eta, \frac{1}{n J_1(\eta)}\right)
$$

Asymptotically unbiased, Gaussian, achieves CRLB
$(\operatorname{corr}(\bar{T}, \hat{\eta}) \to 1)$

---

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} \operatorname{Pois}(\theta), \quad \eta = \log \theta$

$\hat{\eta} = \log \bar{X}, \quad \sqrt{n}(\bar{X} - \theta) \Rightarrow \mathcal{N}(0, \theta)$

$$
\sqrt{n}(\hat{\eta} - \eta) = \sqrt{n}(\log \bar{X} - \log \theta)
$$
$$
\Rightarrow \mathcal{N}\left(0, \theta \cdot \frac{1}{\theta^2}\right) \qquad (\text{Delta method})
$$
$$
= \mathcal{N}(0, \theta^{-1})
$$

**But** $\forall$ finite $n$, $\forall \theta > 0$:
$$
\mathbb{P}_\theta(\hat{\eta} = -\infty) = \mathbb{P}_\theta(X_1 = 0)^n
$$
$$
= e^{-\theta n} > 0
$$

$$
\Rightarrow \mathbb{E}\hat{\eta} = -\infty \qquad \operatorname{Var}(\hat{\eta}) = \infty
$$

[MLE can have embarrassing finite-sample performance despite being asy. optimal!]

**Prop:** If $\mathbb{P}(B_n) \to 0$, $X_n \Rightarrow X$, $Z_n$ arbitrary
then $X_n \mathbf{1}_{B_n^c} + Z_n \mathbf{1}_{B_n} \Rightarrow X$

**Proof** $\mathbb{P}(\|Z_n \mathbf{1}_{B_n}\| > \varepsilon) \le \mathbb{P}(B_n) \to 0$ so $Z_n \mathbf{1}_{B_n} \xrightarrow{P} 0$
Also $\mathbf{1}_{B_n^c} \xrightarrow{P} 1$, apply Slutsky $\boxtimes$

[So zany behavior has no effect on cvg. in dist]

---

## Asymptotic Efficiency

[The nice behavior of MLE we found in the exponential family case generalizes to a much broader class of models]

**Setting** $X_1, \dots, X_n \overset{\text{iid}}{\sim} p_\theta(x) \qquad \theta \in \Theta \subseteq \mathbb{R}^d$
$p_\theta$ "smooth" in $\theta$, e.g. 2 cts integrable derivs (can be relaxed)

Let $\ell_1(\theta; X_i) = \log p_\theta(X_i), \quad \ell_n(\theta; X) = \sum_{i=1}^n \ell_1(\theta; X_i)$

$$
J_1(\theta) = \operatorname{Var}_\theta(\nabla \ell_1(\theta; X_i)) = -\mathbb{E}\left[\nabla^2 \ell_1(\theta; X_i)\right]
$$
$$
J_n(\theta) = \operatorname{Var}_\theta(\nabla \ell_n(\theta; X)) = n J_1(\theta)
$$

We say an estimator $\hat{\theta}_n$ is **

---

[Up: contents](../index.md)
