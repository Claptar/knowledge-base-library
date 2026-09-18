---
title: 2 Wald-Type Confidence Regions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/likelihood-inference.html
source_file: sources/berkeley-stat210a/fall-2025/reader/likelihood-inference.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/likelihood-inference.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/likelihood-inference.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Wald-Type Confidence Regions

Assume we have some estimator $\hat{\theta}_n$ s.t. $\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} N(0, J^{-1}(\theta_0))$. Then we can plug in:

If $\sqrt{n}(\hat{\theta}_n - \theta_0) \sim N_d(0, J^{-1}(\theta_0))$, then $nJ(\theta_0)(\hat{\theta}_n - \theta_0) \sim N_d(0, I_d)$

So $n(\hat{\theta}_n - \theta_0)^T J(\theta_0)(\hat{\theta}_n - \theta_0) \sim \chi^2_d$ (Slutsky)

Leads to test of $H_0: \theta = \theta_0$ $H_1: \theta \neq \theta_0$: Reject if $n(\hat{\theta}_n - \theta_0)^T J(\theta_0)(\hat{\theta}_n - \theta_0) > \chi^2_{d,1-\alpha}$

So $\mathbb{P}_{\theta_0}(n(\hat{\theta}_n - \theta_0)^T J(\theta_0)(\hat{\theta}_n - \theta_0) \leq \chi^2_{d,1-\alpha}) = 1-\alpha$

Note: we reject $\theta_0$ iff $\{\theta_n: n(\hat{\theta}_n - \theta)^T J(\theta)(\hat{\theta}_n - \theta) \leq \chi^2_{d,1-\alpha}\}$ reject $\theta_0$ iff $\theta_0 \notin \{\theta: n(\hat{\theta}_n - \theta)^T J(\theta)(\hat{\theta}_n - \theta) \leq \chi^2_{d,1-\alpha}\}$

Region $\{\theta: n(\hat{\theta}_n - \theta)^T J(\theta)(\hat{\theta}_n - \theta) \leq \chi^2_{d,1-\alpha}\}$ is confidence ellipsoid

More info = smaller ellipse (shrinks like $\sqrt{n}$)

## 2.1 Estimating $J(\theta)$ {#estimating-math32 .anchored number="2.1" anchor-id="estimating-jtheta"}

Two options is to plug-in the MLE: 1. MLE for $J_n(\theta)$: $J_n(\hat{\theta}_n) = -\frac{1}{n}\nabla^2 \ell_n(\hat{\theta}_n; X)$ 2. $\hat{J}_n(\theta) = \frac{1}{n}\text{Var}_\theta[\nabla \ell_n(\theta; X)] = \frac{1}{n}\sum_{i=1}^n \nabla \ell_\theta(X_i) \nabla \ell_\theta(X_i)^T$

NB: $\text{Var}_\theta[\nabla \ell_n(\theta; X)] = n\text{Var}_\theta[\nabla \ell_\theta(X)] = 0$

Or $\hat{J}_n = \mathbb{E}_{\hat{\theta}_n}[-\nabla^2 \ell_{\hat{\theta}_n}(X)]$

### 2.1.1 Remarks {.anchored number="2.1.1" anchor-id="remarks"}

- Both have $\hat{J}_n \xrightarrow{p} J(\theta_0)$ in nice iid sampling setting
- Both make sense outside of iid setting
- Heuristically: plug-in measures info about $\theta$ in typical data set, but obs info measures info about $\theta$ in this data set

## 2.2 Wald Interval for $\theta_j$ {#wald-interval-for-math41 .anchored number="2.2" anchor-id="wald-interval-for-theta_j"}

If $\sqrt{n}(\hat{\theta}_n - \theta_0) \sim N_d(\theta_0, J_n^{-1}(\theta_0))$ then $\hat{\theta}_n \sim N_d(\theta_0, J_n^{-1}(\theta_0)/n)$

Leads to univariate interval: $s.e.(\hat{\theta}_{n,j}) = \sqrt{[J_n^{-1}(\hat{\theta}_n)]_{jj}/n}$

$C_j = [\hat{\theta}_{n,j} \pm z_{1-\alpha/2} \cdot s.e.(\hat{\theta}_{n,j})]$

`glm` function in R uses these intervals/p-values with $\hat{J}_n = J_n(\hat{\theta}_n)$

Conf ellipsoid for $\theta_0$: $\{\theta: n(\hat{\theta}_n - \theta)^T \hat{J}_n(\hat{\theta}_n)(\hat{\theta}_n - \theta) \leq \chi^2_{d,1-\alpha}\}$

More generally, if $\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} N(0, \Sigma(\theta_0))$ and $\hat{\Sigma}_n(\theta) \xrightarrow{p} \Sigma(\theta_0)$ (not nec. MLE) then we can do the same things

## 2.3 Example: Generalized Linear Model with Fixed Design {.anchored number="2.3" anchor-id="example-generalized-linear-model-with-fixed-design"}

$X_1, \ldots, X_n \in \mathbb{R}^d$ fixed $Y_1, \ldots, Y_n \sim p_{\eta_i}(y)$ indep, $Y_i | X_i \sim p_{\eta_i}(y)$ $\eta_i = \beta^T X_i$ (canonical form)

Let $\mu_i(\beta) = \mathbb{E}_\beta[Y_i] = \psi'(\eta_i)$

More general: $\eta_i = f(\beta^T X_i)$ for $f$ monotone

Most common examples include: - Logistic regression: $Y_i \sim \text{Bern}(e^{\eta_i}/(1+e^{\eta_i}))$ - Poisson log-linear model: $Y_i \sim \text{Pois}(e^{\eta_i})$

$\ell_n(\beta; Y) = \sum_{i=1}^n [Y_i \eta_i - \psi(\eta_i) + \log h(Y_i)]$

$\nabla \ell_n(\beta; Y) = \sum_{i=1}^n (Y_i - \mu_i(\beta)) X_i$

$\mathbb{E}_\beta[Y_i] = \mu_i(\beta) = \psi'(\eta_i)$

$\nabla^2 \ell_n(\beta; Y) = -\sum_{i=1}^n \psi''(\eta_i) X_i X_i^T$

$\text{Var}_\beta(Y_i) = \psi''(\eta_i)$ (not random)

$\hat{\beta} \stackrel{\cdot}{\sim} N(\beta, J_n^{-1}(\beta))$ in finite samples $\xrightarrow{d} N(0, J^{-1})$

Under regularity cond. on $X$: Taylor expansion of $\ell_n$ leads to $\sqrt{n}(\hat{\beta}_n - \beta) \xrightarrow{d} N(0, J^{-1})$

### 2.3.1 Advantages of Wald Test {.anchored number="2.3.1" anchor-id="advantages-of-wald-test"}

1.  Easy to invert, simple conf regions
2.  Asymptotically correct

### 2.3.2 Disadvantages {.anchored number="2.3.2" anchor-id="disadvantages"}

1.  Have to compute MLE
2.  Depends on parameterization
3.  Relies on two approximations: $\ell_n$ Normal and $\ell_n$ quadratic
4.  Need MLE to be consistent
5.  Confidence interval/ellipsoid might go outside $\Theta$

---

[← 1 Likelihood-Based Inference](01-1-likelihood-based-inference.md) · [Up: contents](index.md) · [3 Score Test →](03-3-score-test.md)
