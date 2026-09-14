---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-nuisance.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

# Nuisance Parameters

One-parameter families are the exception in statistics, not the rule. In most testing problems, there are additional unknown quantities which are not of direct interest, but which will generically affect the rejection probability of any test we choose. Formally, we will consider a general setup where we observe $X \sim P_{\theta,\lambda}$ from a statistical model
$$
\cP = \{P_{\theta,\lambda}:\; (\theta,\lambda) \in \Omega\},
$$
where as usual $\theta$ and $\lambda$ could be real vectors or could represent infinite-dimensional parameters such as unknown distributions.

We will assume the null and alternative hypotheses concern $\theta$ only; that is, we still want to test $H_0:\;\theta\in\Theta_0$ vs $H_1:\;\theta\in\Theta_1$. We call $\theta$ the **parameter of interest**, and $\lambda$ the **nuisance parameter**.

**Example (Two-sample Gaussian problem):** We observe $X_1,\ldots,X_n \simiid N(\mu,\sigma^2)$ and $Y_1,\ldots,Y_m \simiid N(\nu,\sigma^2)$. All three parameters $\mu,\nu\in\RR$ and $\sigma^2>0$ are unknown, and we wish to test $H_0:\;\mu = \nu$ vs $H_1:\;\mu \neq \nu$. We can express our hypothesis in terms of a parameter of interest $\theta = \mu - \nu$, in which case our nuisance parameter is $\lambda = (\mu + \nu, \sigma^2)$, or $\lambda = (\mu, \sigma^2)$, or any other representation of the remaining unknown information besides $\theta$.

**Example (Comparing two Poissons):** We observe $X\sim \text{Pois}(\mu)$ and $Y\sim\text{Pois}(\nu)$ and want to test $H_0:\;\mu\leq \nu$ vs $H_1:\;\mu>\nu$. Here, we could call $\mu-\nu$ the parameter of interest, but as we will see shortly it is somewhat more natural to think about the ratio $\frac{\mu}{\nu}$, or $\theta = \frac{\mu}{\mu+\nu}$.


**Example (Two-sample binomial problem):** We might observe $X_1\sim \text{Binom}(n_1,\pi_1)$ and $X_2\sim\text{Binom}(n_2,\pi_2)$ and want to test $H_0:\;\pi_1\leq \pi_2$ vs $H_1:\;\pi_1>\pi_2$. The sample sizes $n_1$ and $n_2$ are typically *known* (so they are not nuisance parameters). Here, we could call $\pi_1-\pi_2$ the parameter of interest, but it is somewhat more natural to think about the **odds ratio** $\rho = \frac{\pi_1}{1-\pi_1}/\frac{\pi_2}{1-\pi_2}$, whose log is the difference between the two natural parameters.

---

[Up: contents](index.md) · [Conditional testing →](02-conditional-testing.md)
