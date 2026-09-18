---
title: 5 Deduced Inference
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 5 Deduced Inference

Given any joint confidence region $C(X)$ for $\theta \in \Theta$, we may freely assume $\theta \in C(X)$ and deduce any and all implied conclusions without any FWER inflation:

$\mathbb{P}_\theta(\text{any deduced inference is wrong}) \leq \mathbb{P}_\theta(\theta \notin C(X)) \leq \alpha$

Deduction is often a good paradigm for deriving simultaneous intervals

We say $C_1(X),\ldots,C_m(X)$ are simultaneous $1-\alpha$ confidence intervals for $g_1(\theta),\ldots,g_m(\theta)$ if:

$\mathbb{P}_\theta(g_i(\theta) \in C_i(X) \text{ for all } i = 1,\ldots,m) \geq 1-\alpha$

### 5.1 Example: Simultaneous Intervals for Multivariate Gaussian {.anchored number="5.1" anchor-id="example-simultaneous-intervals-for-multivariate-gaussian"}

Assume $X \sim N_d(\theta, \Sigma)$, $\Sigma$ known, $\Sigma_{ii} = 1$

Let $t_\alpha$ be upper $\alpha$ quantile of $\|X - \theta\|_\Sigma = \sqrt{(X-\theta)^T \Sigma^{-1}(X-\theta)}$

$C_i(X) = [\theta_i: |X_i - \theta_i| \leq t_\alpha \sqrt{\Sigma_{ii}}]$ for all $i$

$\mathbb{P}(C(X) \ni \theta_i \text{ for any } i) = \mathbb{P}(\|X - \theta\|_\Sigma \leq t_\alpha) = 1-\alpha$

$t_\alpha = \sqrt{\chi^2_{d,1-\alpha}}$ if $\Sigma = I_d$

Note: we could have instead constructed an elliptical conf. region, but then the intervals would be conservative:

$\mathbb{P}(\|X - \theta\|_\Sigma^2 \leq \chi^2_{d,1-\alpha}) = 1-\alpha$

### 5.2 Example: Linear Regression (n obs, d variables) {.anchored number="5.2" anchor-id="example-linear-regression-n-obs-d-variables"}

$X \in \mathbb{R}^{n \times d}$ design, $\beta \in \mathbb{R}^d$, $Y \sim N(X\beta, \sigma^2 I_n)$

Estimate $\hat{\beta} = (X^T X)^{-1} X^T Y$

where $\hat{\beta} \sim N(\beta, \sigma^2 (X^T X)^{-1})$

$S^2 = \|Y - X\hat{\beta}\|^2/(n-d)$, $V = RS^2$, $R = (X^T X)^{-1}$

Distr. of $\hat{\beta}_j/\sqrt{V_{jj}}$ fully known

Assume w.l.o.g. $X^T X = I_d$

Let $t_\alpha$ denote upper $\alpha$ quantile of $\|\hat{\beta} - \beta\|/\sqrt{S^2}$

Then $C_j = \hat{\beta}_j \pm t_\alpha \sqrt{V_{jj}}$ are simultaneous CIs for $\beta_j$, $j = 1,\ldots,d$ (compute $t_\alpha$ by simulation)

$\mathbb{P}(|\hat{\beta}_j - \beta_j| \leq t_\alpha \sqrt{V_{jj}} \text{ for all } j) = 1-\alpha$

## 6 False Discovery Rate (FDR) {.anchored number="6" anchor-id="false-discovery-rate-fdr"}

Problem: With 10K independent test statistics, all at level $\alpha = 0.001$, we expect 10 rejections just by chance. What if we get 50? Probably only ~20 of them are false rejections.

Can we accept 10 false rejections as long as most rejections are valid?

Benjamini-Hochberg (1995) proposed a more liberal error control criterion called FDR:

$R(X) = |R(X)|$ = rejections (“discoveries”) $V(X) = |R(X) \cap H_{0c}|$ = false discoveries

The FDP is: $\text{FDP} = \begin{cases} V(X)/R(X) & \text{if } R(X) > 0 \\ 0 & \text{if } R(X) = 0 \end{cases}$

The FDR is $\mathbb{E}[\text{FDP}]$

## 7 Benjamini-Hochberg Procedure {.anchored number="7" anchor-id="benjamini-hochberg-procedure"}

B-H also proposed a method to control FDR given ordered p-values $p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$:

$R(X) = \max\{r: p_{(r)} \leq \alpha r/m\}$ (called step-up procedure)

Reject $H_{0(1)},\ldots,H_{0(R)}$

This is much more liberal than Bonferroni procedure: When $\alpha = 0.05$, B-H rejects at least $r$ p-values if $p_{(r)} \leq 0.05r/m$

### 7.1 B-H as Empirical Bayes {.anchored number="7.1" anchor-id="b-h-as-empirical-bayes"}

Equivalent formulation for $R(t) = #\{p_i \leq t\}$: Let $\hat{F}(t) = R(t)/m$ = estimate of CDF of p-values

B-H rejects $H_i$ if $p_i \leq T(X) = \max\{t: \hat{F}(t) \geq t/\alpha\}$

When $\hat{F}(t)$ is continuously increasing in $t$ except at jump values where it jumps down:

$\hat{F}(T(X)) = T(X)/\alpha$

$$
Insert graph showing $\hat{F}(t)$ vs $t/\alpha$
$$

Only values of $t$ that matter for the algorithm are $t = p_i$ where $\hat{F}(t) = t/\alpha$, i.e., $\alpha i/m = p_{(i)}$

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [8 FDR Control →](03-8-fdr-control.md)
