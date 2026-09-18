---
title: 1 Maximum Likelihood Estimation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/maximum-likelihood.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/maximum-likelihood.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/maximum-likelihood.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/maximum-likelihood.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Maximum Likelihood Estimation

Published

November 14, 2023

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

## 1 Maximum Likelihood Estimation {.anchored number="1" anchor-id="maximum-likelihood-estimation"}

For a generic dominated family $\cP = \{P_\theta: \theta \in \Theta\}$ with densities $f_\theta$, a simple estimator for $\theta$ is:

$$
\hat{\theta}_{\text{MLE}}(X) = \arg\max_{\theta \in \Theta} p_\theta(X) = \arg\max_{\theta \in \Theta} \prod_{i=1}^n f_\theta(X_i) = \arg\max_{\theta \in \Theta} \ell_n(\theta; X)
$$

Remarks: 1. $\arg\max$ may not exist, be unique, or be computable 2. Doesn’t depend on parameterization or base measure; MLE for $g(\theta)$ is $g(\hat{\theta}_{\text{MLE}})$

### 1.1 Example: Exponential Family {.anchored number="1.1" anchor-id="example-exponential-family"}

$$
\ell(\eta; X) = \eta^T T(X) - A(\eta) + \log h(X)
$$

$T(\bar{X}) = \mathbb{E}_\eta[T(X)]$ if such $\eta$ exists

Because $\ell''(\eta; X) = -\text{Var}_\eta[T(X)]$ is negative definite unless $\eta \to T(\eta)$ constant, in which case param redundant

At most 1 solution exists

Let $m(X) = \mathbb{E}_\eta[T(X)] = \nabla A(\eta)$

### 1.2 Example: Normal Distribution {.anchored number="1.2" anchor-id="example-normal-distribution"}

$X_i \sim \text{iid } N(\theta, \sigma^2)$, $h(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-x^2/(2\sigma^2)}$, $\eta \in \mathbb{R}$

$T(X) = \frac{X}{\sigma^2}$, $A(\eta) = \frac{\eta^2}{2\sigma^2}$

Assume $\eta = \theta/\sigma^2$, $\sigma^2$ known

$m(\eta) = \eta\sigma^2 = \theta$, $m^{-1}(\theta) = \theta/\sigma^2$

Consistency: $\bar{X} \xrightarrow{p} \theta$ (LLN)

Cts mapping: $\hat{\eta} = m^{-1}(\bar{X}) \xrightarrow{p} \theta/\sigma^2$

Since $\sqrt{n}(\bar{X} - \theta) \xrightarrow{d} N(0, \text{Var}_\eta[T(X)])$:

$N(0, \sigma^2)$

Recall: $J(\eta) = \text{Var}_\eta[T(X)]$

Delta method: $\sqrt{n}(\hat{\eta} - \eta) \xrightarrow{d} N(0, [m^{-1'}(\theta)]^2 \sigma^2)$

$N(0, 1/\sigma^2)$

Recall: $J(\eta) = \text{Var}_\eta[T(X)] = \sigma^2$

$N(0, J^{-1})$

Asymptotically unbiased Gaussian, achieves CRLB

### 1.3 Example: Poisson Distribution {.anchored number="1.3" anchor-id="example-poisson-distribution"}

$X_i \sim \text{iid Poisson}(\theta)$, $\eta = \log \theta$

$T(X) = X$, $\mathbb{E}[X] = \theta$, $N(0, \theta)$

$\hat{\eta}_n = \log \bar{X}$, $\sqrt{n}(\log \bar{X} - \log \theta) \xrightarrow{d} N(0, \theta^{-1})$ (Delta method)

$N(0, \theta^{-1})$

But for finite $n$, $\mathbb{P}(\bar{X} = 0) = \mathbb{P}(X_1 = 0)^n = e^{-n\theta} > 0$

MLE can have embarrassing finite sample performance despite being asymptotically optimal

### 1.4 Proof: Convergence in Distribution with Probability Approaching 1 {.anchored number="1.4" anchor-id="proof-convergence-in-distribution-with-probability-approaching-1"}

If $\mathbb{P}(B_n) \to 1$, $X_n \xrightarrow{d} X$, $Z_n$ arbitrary, then $X_n 1_{B_n} + Z_n 1_{B_n^c} \xrightarrow{d} X$

Proof: $\mathbb{P}(\|Z_n 1_{B_n^c}\| > \epsilon) \leq \mathbb{P}(B_n^c) \to 0$, so $Z_n 1_{B_n^c} \xrightarrow{p} 0$ Also, $1_{B_n} \xrightarrow{p} 1$, apply Slutsky

Any zany behavior has no effect on convergence in distribution

## 2 Asymptotic Efficiency {.anchored number="2" anchor-id="asymptotic-efficiency"}

In the exponential family case, generalizes to a much broader class of models

Setting: $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} p_\theta(x)$, $\theta \in \mathbb{R}^d$

$p_\theta$ smooth in $\theta$ (e.g., 2 cts integrable derives, can be relaxed)

Let $\ell_i(\theta; X) = \log p_\theta(X_i)$, $\ell_n(\theta; X) = \sum_{i=1}^n \ell_i(\theta; X)$

$S_n(\theta) = \nabla_\theta \ell_n(\theta; X)$, $J_n(\theta) = \text{Var}_\theta[\nabla_\theta \ell_n(\theta; X)] = nJ_1(\theta)$

We say an estimator is asymptotically efficient if $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, J_1^{-1}(\theta))$

Delta method for differentiable estimand $g(\theta)$:

$\sqrt{n}(g(\hat{\theta}_n) - g(\theta)) \xrightarrow{d} N(0, \nabla g(\theta)^T J_1^{-1}(\theta) \nabla g(\theta))$

Also achieves CRLB if $\hat{\theta}_n$ does, $g$ diff

---

[Up: contents](index.md) · [3 Asymptotic Distribution of MLE →](02-3-asymptotic-distribution-of-mle.md)
