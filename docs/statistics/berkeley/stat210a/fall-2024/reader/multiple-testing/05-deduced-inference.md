---
title: Deduced Inference
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Deduced Inference

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Given any joint confidence region $C(X)$ for $\theta \in \Theta$, we may freely assume $\theta \in C(X)$ and deduce any and all implied conclusions without any FWER inflation:

$\mathbb{P}_\theta(\text{any deduced inference is wrong}) \leq \mathbb{P}_\theta(\theta \notin C(X)) \leq \alpha$

Deduction is often a good paradigm for deriving simultaneous intervals

We say $C_1(X),\ldots,C_m(X)$ are simultaneous $1-\alpha$ confidence intervals for $g_1(\theta),\ldots,g_m(\theta)$ if:

$\mathbb{P}_\theta(g_i(\theta) \in C_i(X) \text{ for all } i = 1,\ldots,m) \geq 1-\alpha$

### Example: Simultaneous Intervals for Multivariate Gaussian

Assume $X \sim N_d(\theta, \Sigma)$, $\Sigma$ known, $\Sigma_{ii} = 1$

Let $t_\alpha$ be upper $\alpha$ quantile of $\|X - \theta\|_\Sigma = \sqrt{(X-\theta)^T \Sigma^{-1}(X-\theta)}$

$C_i(X) = [\theta_i: |X_i - \theta_i| \leq t_\alpha \sqrt{\Sigma_{ii}}]$ for all $i$

$\mathbb{P}(C(X) \ni \theta_i \text{ for any } i) = \mathbb{P}(\|X - \theta\|_\Sigma \leq t_\alpha) = 1-\alpha$

$t_\alpha = \sqrt{\chi^2_{d,1-\alpha}}$ if $\Sigma = I_d$

Note: we could have instead constructed an elliptical conf. region, but then the intervals would be conservative:

$\mathbb{P}(\|X - \theta\|_\Sigma^2 \leq \chi^2_{d,1-\alpha}) = 1-\alpha$

### Example: Linear Regression (n obs, d variables)

$X \in \mathbb{R}^{n \times d}$ design, $\beta \in \mathbb{R}^d$, $Y \sim N(X\beta, \sigma^2 I_n)$

Estimate $\hat{\beta} = (X^T X)^{-1} X^T Y$

where $\hat{\beta} \sim N(\beta, \sigma^2 (X^T X)^{-1})$

$S^2 = \|Y - X\hat{\beta}\|^2/(n-d)$, $V = RS^2$, $R = (X^T X)^{-1}$

Distr. of $\hat{\beta}_j/\sqrt{V_{jj}}$ fully known

Assume w.l.o.g. $X^T X = I_d$

Let $t_\alpha$ denote upper $\alpha$ quantile of $\|\hat{\beta} - \beta\|/\sqrt{S^2}$

Then $C_j = \hat{\beta}_j \pm t_\alpha \sqrt{V_{jj}}$ are simultaneous CIs for $\beta_j$, $j = 1,\ldots,d$ (compute $t_\alpha$ by simulation)

$\mathbb{P}(|\hat{\beta}_j - \beta_j| \leq t_\alpha \sqrt{V_{jj}} \text{ for all } j) = 1-\alpha$

---

[← Testing with Dependence](04-testing-with-dependence.md) · [Up: contents](index.md) · [False Discovery Rate (FDR) →](06-false-discovery-rate-fdr.md)
