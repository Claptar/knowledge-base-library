---
title: Maximum Likelihood Estimation
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/maximum-likelihood.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/maximum-likelihood.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Maximum Likelihood Estimation

**Source:** [`reader/maximum-likelihood.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/maximum-likelihood.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

For a generic dominated family $\cP = \{P_\theta: \theta \in \Theta\}$ with densities $f_\theta$, a simple estimator for $\theta$ is:

$$\hat{\theta}_{\text{MLE}}(X) = \arg\max_{\theta \in \Theta} p_\theta(X) = \arg\max_{\theta \in \Theta} \prod_{i=1}^n f_\theta(X_i) = \arg\max_{\theta \in \Theta} \ell_n(\theta; X)$$

Remarks:
1. $\arg\max$ may not exist, be unique, or be computable
2. Doesn't depend on parameterization or base measure; MLE for $g(\theta)$ is $g(\hat{\theta}_{\text{MLE}})$

### Example: Exponential Family

$$\ell(\eta; X) = \eta^T T(X) - A(\eta) + \log h(X)$$

$T(\bar{X}) = \mathbb{E}_\eta[T(X)]$ if such $\eta$ exists

Because $\ell''(\eta; X) = -\text{Var}_\eta[T(X)]$ is negative definite unless $\eta \to T(\eta)$ constant, in which case param redundant

At most 1 solution exists

Let $m(X) = \mathbb{E}_\eta[T(X)] = \nabla A(\eta)$

### Example: Normal Distribution

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

### Example: Poisson Distribution

$X_i \sim \text{iid Poisson}(\theta)$, $\eta = \log \theta$

$T(X) = X$, $\mathbb{E}[X] = \theta$, $N(0, \theta)$

$\hat{\eta}_n = \log \bar{X}$, $\sqrt{n}(\log \bar{X} - \log \theta) \xrightarrow{d} N(0, \theta^{-1})$ (Delta method)

$N(0, \theta^{-1})$

But for finite $n$, $\mathbb{P}(\bar{X} = 0) = \mathbb{P}(X_1 = 0)^n = e^{-n\theta} > 0$

MLE can have embarrassing finite sample performance despite being asymptotically optimal

### Proof: Convergence in Distribution with Probability Approaching 1

If $\mathbb{P}(B_n) \to 1$, $X_n \xrightarrow{d} X$, $Z_n$ arbitrary, then $X_n 1_{B_n} + Z_n 1_{B_n^c} \xrightarrow{d} X$

Proof: $\mathbb{P}(\|Z_n 1_{B_n^c}\| > \epsilon) \leq \mathbb{P}(B_n^c) \to 0$, so $Z_n 1_{B_n^c} \xrightarrow{p} 0$
Also, $1_{B_n} \xrightarrow{p} 1$, apply Slutsky

Any zany behavior has no effect on convergence in distribution

---

[Up: contents](index.md) · [Asymptotic Efficiency →](02-asymptotic-efficiency.md)
