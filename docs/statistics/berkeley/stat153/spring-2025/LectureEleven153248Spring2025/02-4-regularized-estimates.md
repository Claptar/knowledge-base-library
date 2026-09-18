---
title: 4 Regularized Estimates
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Regularized Estimates

We discussed two estimates of $\beta_0, \dots, \beta_{n-1}$ based on the idea of regularization. The first is the ridge estimate $\hat{\beta}^{\text{ridge}}(\lambda)$ defined as the minimizer of:
$$\sum_{t=1}^n (y_t - \beta_0 - \beta_1(t - 1) - \beta_2\text{ReLU}(t - 2) - \dots - \beta_{n-1}\text{ReLU}(t - (n - 1)))^2 + \lambda (\beta_2^2 + \beta_3^2 + \dots + \beta_{n-1}^2). \tag{3}$$

The second is the LASSO estimate $\hat{\beta}^{\text{lasso}}(\lambda)$ given by the minimizer of:
$$\sum_{t=1}^n (y_t - \beta_0 - \beta_1(t - 1) - \beta_2\text{ReLU}(t - 2) - \dots - \beta_{n-1}\text{ReLU}(t - (n - 1)))^2 + \lambda (|\beta_2| + |\beta_3| + \dots + |\beta_{n-1}|). \tag{4}$$

$\lambda$ denotes a parameter which can be tuned to change the behavior of $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$. When $\lambda = 0$, both $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$ coincide with the unregularized least squares estimator. When $\lambda$ is very large, both $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$ coincide with the linear regression estimator (i.e., the first two components of $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$ coincide with linear regression while the last $n - 2$ components are simply set to zero).

Based on the alternative representations of Section 2, we can rewrite the optimization objectives (9) and (10) as
$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} ((\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1}))^2 \tag{5}$$
and
$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} |(\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})| \tag{6}$$

We denote the minimizer of (5) by $\hat{\mu}_t^{\text{ridge}}(\lambda)$ and the minimizer of (6) by $\hat{\mu}_t^{\text{lasso}}(\lambda)$. The relation between $\hat{\mu}_t^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{ridge}}(\lambda)$ is given by
$$\hat{\mu}_t^{\text{ridge}}(\lambda) = \hat{\beta}_0^{\text{ridge}}(\lambda) + \hat{\beta}_1^{\text{ridge}}(\lambda)(t - 1) + \sum_{j=2}^{n-1} \hat{\beta}_j^{\text{ridge}}(\lambda)\text{ReLU}(t - j).$$
Similarly the relation between $\hat{\mu}_t^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{ridge}}(\lambda)$ is given by
$$\hat{\mu}_t^{\text{lasso}}(\lambda) = \hat{\beta}_0^{\text{lasso}}(\lambda) + \hat{\beta}_1^{\text{lasso}}(\lambda)(t - 1) + \sum_{j=2}^{n-1} \hat{\beta}_j^{\text{lasso}}(\lambda)\text{ReLU}(t - j).$$

The estimator $\hat{\mu}_t^{\text{ridge}}(\lambda)$ is actually known by the name Hodrick-Prescott filter in the econometrics literature (see e.g., https://en.wikipedia.org/wiki/Hodrick\OT1\textendashPrescott_filter), and it is closely related to the cubic spline smoother (see e.g., https://en.wikipedia.org/wiki/Smoothing_spline).

The estimator $\hat{\mu}_t^{\text{lasso}}(\lambda)$ is known by the name $\ell_1$ trend filter (see https://stanford.edu/~boyd/papers/l1_trend_filter.html).

Both the objective functions (5) and (6) ensure good fit to the data (because of the term $\sum_{t=1}^n (y_t - \mu_t)^2$) while also ensuring that neighboring slopes $\mu_{t+1} - \mu_t$ and $\mu_t - \mu_{t-1}$ are close to each other (this is because of the terms $\lambda \sum_{t=2}^{n-1} ((\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1}))^2$ and $\lambda \sum_{t=2}^{n-1} |(\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})|$). Closeness of neighboring slopes $\mu_{t+1} - \mu_t$ and $\mu_t - \mu_{t-1}$ gives a smooth appearance to $\{\mu_t\}$. These can therefore be seen as methods for trying to fit a smooth trend function $\mu_t$ to the observed time series $y_t$.

---

← STAT 153 & 248 - Time Series · [Up: contents](index.md) · [5 Ridge vs LASSO →](03-5-ridge-vs-lasso.md)
