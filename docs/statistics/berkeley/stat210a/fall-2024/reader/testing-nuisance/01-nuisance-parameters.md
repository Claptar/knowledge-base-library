---
title: Nuisance Parameters
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Nuisance Parameters

**Source:** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Common Setup

Extra unknown parameters which are not of direct interest:

$\cP = \{P_{\theta, \lambda}: \theta \in \Theta, \lambda \in \Lambda\}$

$H_0: \theta \in \Theta_0$ vs $H_1: \theta \in \Theta_1$

- $\theta$: parameter of interest
- $\lambda$: nuisance parameter

Issue: $\lambda$ unknown but might affect type I error or power of a given test

### Examples

1. $X_1, \ldots, X_n \sim \text{iid } N(\mu, \sigma^2)$, $Y_1, \ldots, Y_m \sim \text{iid } N(\nu, \sigma^2)$
   $\mu, \nu, \sigma^2$ unknown
   $H_0: \mu = \nu$ vs $H_1: \mu \neq \nu$
   $\theta = \mu - \nu$, $\lambda = (\mu + \nu, \sigma^2)$ or $(\mu, \sigma^2)$

2. $X \sim \text{Binom}(n_1, \pi_1)$, $X_2 \sim \text{Binom}(n_2, \pi_2)$
   $n_1, n_2$ known (not nuisance parameters)
   $H_0: \pi_1 = \pi_2$ vs $H_1: \pi_1 \neq \pi_2$

3. $X \sim N(\mu, \sigma^2)$, $\theta \in \mathbb{R}$, $\lambda \in \mathbb{R}$, both unknown
   How to test $H_0: \theta = 0$ vs $H_1: \theta \neq 0$?

### Idea: Condition on Sufficient Statistic for $\lambda$

Condition on $U(X)$ to eliminate dependence on $\lambda$

$$p_{\theta, \lambda}(t|u) = \frac{p_{\theta, \lambda}(t, u)}{p_{\lambda}(u)} = \frac{e^{\theta \cdot t} g_\lambda(t, u)}{\int e^{\theta \cdot s} g_\lambda(s, u) ds}$$

Evaluate $H_0: \theta \in \Theta_0$ vs $H_1: \theta \in \Theta_1$ in s-parameter model $\{p_\theta(\cdot|u): \theta \in \Theta\}$

Note: If $s=1$, this family has MLR in $T$. Even if $s>1$, we have still gotten rid of $\lambda$.

---

[Up: contents](index.md) · [Theorem (Informal) →](02-theorem-informal.md)
