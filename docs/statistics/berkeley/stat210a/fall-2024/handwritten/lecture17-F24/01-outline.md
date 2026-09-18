---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture17-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

10/24/23

1) Testing with nuisance parameters
2) UMPU multivariate tests
3) Conditioning on null sufficient stat

---

## Nuisance Parameters

Common setup: Extra unknown parameters which are not of direct interest

$\mathcal{P} = \{ P_{\theta, \lambda} : (\theta, \lambda) \in \Omega \}$, $H_0 : \theta \in \Theta_0$ vs $H_1 : \theta \in \Theta_1$

$\theta$ **parameter of interest**

$\lambda$ **nuisance parameter**

**Issue:** $\lambda$ unknown but might affect type I error or power of a given test

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \quad Y_1, \dots, Y_m \overset{\text{iid}}{\sim} N(\nu, \sigma^2)$
$\mu, \nu, \sigma^2$ unknown
$H_0 : \mu = \nu \quad \text{vs} \quad H_1 : \mu \ne \nu$
$\theta = \mu - \nu \qquad \lambda = (\mu + \nu, \sigma^2) \quad \text{or} \quad (\mu, \sigma^2)$

**Ex** $X_1 \sim \text{Binom}(n_1, \pi_1) \quad X_2 \sim \text{Binom}(n_2, \pi_2)$
$n_1, n_2$ known $\Rightarrow$ **not** nuisance parameters
$H_0 : \pi_1 \le \pi_2 \quad \text{vs} \quad H_1 : \pi_1 > \pi_2$

---

## Multiparameter Exp. Families

Assume $X \sim p_{\theta, \lambda}(x) = e^{\theta^T t(x) + \lambda' u(x) - A(\theta, \lambda)} h(x)$

$\theta \in \mathbb{R}^s$, $\lambda \in \mathbb{R}^r$, both unknown

How to test $H_0 : \theta \in \Theta_0$ vs $H_1 : \theta \in \Theta_1$?

Idea: Condition on $U(X)$ to eliminate dep. on $\lambda$

1) **Sufficiency reduction:**
$$(T(X), U(X)) \sim q_{\theta, \lambda}(t, u) = e^{\theta' t + \lambda' u - A(\theta, \lambda)} g(t, u)$$
(density wrt e.g. Lebesgue on $\mathbb{R}^{s+r}$)

2) **Condition on $U(X)$:**
$$\begin{aligned}
q_\theta(t \mid u) &= \frac{q_{\theta, \lambda}(t, u)}{\int q_{\theta, \lambda}(z, u) \, dz} \\
&= \frac{e^{\theta' t + \lambda' u - A(\theta, \lambda)} g(t, u)}{e^{B_u(\theta)} \int e^{\theta' z + \lambda' u - A(\theta, \lambda)} g(z, u) \, dz} \\
&= e^{\theta' t - B_u(\theta)} g(t, u)
\end{aligned}$$

---

3) **Conditional test:**

Test $H_0 : \theta \in \Theta_0$ vs. $H_1 : \theta \in \Theta_1$ in $s$-parameter model $\mathcal{Q}_u = \{ q_\theta(t \mid u) : \theta \in \Theta \}$

**Note** if $s = 1$, this family has MLR in $T$

Even if $s > 1$, we still have gotten rid of $\lambda$

## Theorem (Informal)

---

---

[Up: contents](index.md) · [Theorem →](02-theorem.md)
