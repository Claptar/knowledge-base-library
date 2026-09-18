---
title: 1 Nuisance Parameters
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Nuisance Parameters

Published

October 24, 2023

$$
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\td}{\,\textrm{d}}
\newcommand{\simiid}{\stackrel{\textrm{i.i.d.}}{\sim}}
\newcommand{\simind}{\stackrel{\textrm{ind.}}{\sim}}
\newcommand{\eqas}{\stackrel{\textrm{a.s.}}{=}}
\newcommand{\eqPas}{\stackrel{\cP\textrm{-a.s.}}{=}}
\newcommand{\eqmuas}{\stackrel{\mu\textrm{-a.s.}}{=}}
\newcommand{\eqD}{\stackrel{D}{=}}
\newcommand{\indep}{\perp\!\!\!\!\perp}
\DeclareMathOperator*{\minz}{minimize\;}
\DeclareMathOperator*{\maxz}{minimize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
$$

## 1 Nuisance Parameters {.anchored number="1" anchor-id="nuisance-parameters"}

### 1.1 Common Setup {.anchored number="1.1" anchor-id="common-setup"}

Extra unknown parameters which are not of direct interest:

$\cP = \{P_{\theta, \lambda}: \theta \in \Theta, \lambda \in \Lambda\}$

$H_0: \theta \in \Theta_0$ vs $H_1: \theta \in \Theta_1$

- $\theta$: parameter of interest
- $\lambda$: nuisance parameter

Issue: $\lambda$ unknown but might affect type I error or power of a given test

### 1.2 Examples {.anchored number="1.2" anchor-id="examples"}

1.  $X_1, \ldots, X_n \sim \text{iid } N(\mu, \sigma^2)$, $Y_1, \ldots, Y_m \sim \text{iid } N(\nu, \sigma^2)$ $\mu, \nu, \sigma^2$ unknown $H_0: \mu = \nu$ vs $H_1: \mu \neq \nu$ $\theta = \mu - \nu$, $\lambda = (\mu + \nu, \sigma^2)$ or $(\mu, \sigma^2)$

2.  $X \sim \text{Binom}(n_1, \pi_1)$, $X_2 \sim \text{Binom}(n_2, \pi_2)$ $n_1, n_2$ known (not nuisance parameters) $H_0: \pi_1 = \pi_2$ vs $H_1: \pi_1 \neq \pi_2$

3.  $X \sim N(\mu, \sigma^2)$, $\theta \in \mathbb{R}$, $\lambda \in \mathbb{R}$, both unknown How to test $H_0: \theta = 0$ vs $H_1: \theta \neq 0$?

### 1.3 Idea: Condition on Sufficient Statistic for $\lambda$ {#idea-condition-on-sufficient-statistic-for-math26 .anchored number="1.3" anchor-id="idea-condition-on-sufficient-statistic-for-lambda"}

Condition on $U(X)$ to eliminate dependence on $\lambda$

$$
p_{\theta, \lambda}(t|u) = \frac{p_{\theta, \lambda}(t, u)}{p_{\lambda}(u)} = \frac{e^{\theta \cdot t} g_\lambda(t, u)}{\int e^{\theta \cdot s} g_\lambda(s, u) ds}
$$

Evaluate $H_0: \theta \in \Theta_0$ vs $H_1: \theta \in \Theta_1$ in s-parameter model $\{p_\theta(\cdot|u): \theta \in \Theta\}$

Note: If $s=1$, this family has MLR in $T$. Even if $s>1$, we have still gotten rid of $\lambda$.

---

[Up: contents](index.md) · [2 Theorem (Informal) →](02-2-theorem-informal.md)
