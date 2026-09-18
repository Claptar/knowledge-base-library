---
title: Lecture Eleven
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEleven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEleven153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEleven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEleven153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Eleven

## High-Dimensional Linear Regression Model

$\{y_t\}$

$$y_t = \beta_0 + \beta_1(t-1) + \beta_2 \operatorname{ReLU}(t-2) + \beta_3 \operatorname{ReLU}(t-3) + \dots + \beta_{n-1} \operatorname{ReLU}(t-(n-1)) + \varepsilon_t$$

$$\varepsilon_t \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

$$# \text{ of beta parameters} = n = \text{Data size}$$

(1) $y_t = \mu_t + \varepsilon_t$
where $\mu_t$ is trend:
$$\mu_t = \beta_0 + \beta_1(t-1) + \beta_2 \operatorname{ReLU}(t-2) + \dots + \beta_{n-1} \operatorname{ReLU}(t-(n-1))$$

(2) $y = X\beta + \varepsilon$

$$\underset{n \times n}{X} = \begin{bmatrix}
1 & 0 & 0 & 0 & & 0 \\
1 & 1 & 0 & 0 & \dots & 0 \\
1 & 2 & 1 & 0 & & \vdots \\
\vdots & \vdots & 2 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & 2 & & 1 \\
1 & n-1 & n-2 & n-3 & & \vdots
\end{bmatrix}$$

**Least Squares Estimates**

$$\sum_{t=1}^n \left[ y_t - \beta_0 - \beta_1(t-1) - \beta_2 \operatorname{ReLU}(t-2) - \dots - \beta_{n-1} \operatorname{ReLU}(t-(n-1)) \right]^2$$

Minimize over all parameters $\beta_0, \beta_1, \dots, \beta_{n-1}$

---

$$\begin{cases}
\beta_0 = y_1, \quad \beta_1 = y_2 - y_1, \quad \beta_2 = (y_3 - y_2) - (y_2 - y_1) \\
\beta_t = (y_{t+1} - y_t) - (y_t - y_{t-1}), \quad t = 2, \dots, n-1
\end{cases}$$

**Regularized Estimation**

* **Ridge regularization**
* **LASSO regularization**

$$\|y - X\beta\|^2 = \sum_{t=1}^n \left[ y_t - \beta_0 - \beta_1(t-1) - \beta_2 \operatorname{ReLU}(t-2) - \dots - \beta_{n-1} \operatorname{ReLU}(t-(n-1)) \right]^2$$

$$\min_{\beta_0, \beta_1, \dots, \beta_{n-1}} \left[ \|y - X\beta\|^2 + \lambda (\beta_2^2 + \dots + \beta_{n-1}^2) \right] = \hat{\beta}^{\text{ridge}}(\lambda)$$

where $\lambda$ is the Tuning Parameter.

(1) $\hat{\beta}^{\text{ridge}}(0) = \text{unregularized least squares}$
$$(y_1, y_2 - y_1, (y_3 - y_2) - (y_2 - y_1), \dots)$$

(2) $\hat{\beta}^{\text{ridge}}(+\infty) = \text{linear regression}$
$$\left( \bar{y} - \hat{\beta}_1 \bar{x}, \, \frac{\sum (y_i - \bar{y})(x_i - \bar{x})}{\sum (x_i - \bar{x})^2}, \, 0, \dots, 0 \right)$$

---

**LASSO regularization**

$$\min_{\beta_0, \beta_1, \beta_2, \dots, \beta_{n-1}} \left[ \|y - X\beta\|^2 + \lambda (|\beta_2| + |\beta_3| + \dots + |\beta_{n-1}|) \right] = \hat{\beta}^{\text{LASSO}}(\lambda)$$

$$\lambda = 0 \longrightarrow \text{Unregularized}$$
$$\lambda = \infty \longrightarrow \text{linear regression}$$

**Fitted Values**

$$\hat{\mu}^{\text{ridge}}(\lambda) = X \hat{\beta}^{\text{ridge}}(\lambda)$$
$$\hat{\mu}^{\text{LASSO}}(\lambda) = X \hat{\beta}^{\text{LASSO}}(\lambda)$$

(1) **Ridge**

$$\|y - X\beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2$$

$$= \sum_{t=1}^n \left( y_t - \left[ \beta_0 + \beta_1(t-1) + \beta_2 \operatorname{ReLU}(t-2) + \dots + \beta_{n-1} \operatorname{ReLU}(t-(n-1)) \right] \right)^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2$$

---

$$\mu_t = \beta_0 + \beta_1(t-1) + \beta_2 \operatorname{ReLU}(t-2) + \dots + \beta_{n-1} \operatorname{ReLU}(t-(n-1))$$
$$t = 1, \dots, n$$

$$\beta_0 = \mu_1, \quad \beta_1 = \mu_2 - \mu_1$$
$$\beta_2 = (\mu_3 - \mu_2) - (\mu_2 - \mu_1)$$
$$\beta_t = (\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})$$

$$\hat{\beta}^{\text{ridge}}(\lambda) = \operatorname{argmin} \left[ \|y - X\beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2 \right]$$

$$\hat{\mu}^{\text{ridge}}(\lambda) = \operatorname{argmin}_{\{\mu_t\}} \left[ \sum (y_t - \mu_t)^2 + \lambda \sum_{j=2}^{n-1} \left( (\mu_{j+1} - \mu_j) - (\mu_j - \mu_{j-1}) \right)^2 \right]$$

$$\{y_t\} \quad \{\mu_t\}$$

$$\mu_{t+1} - \mu_t \approx \mu_t - \mu_{t-1} \quad \text{for all } t \text{ on average}$$

Smooth Trend Estimation
(Hodrick-Prescott Filter)
Cubic spline smoothing

$$\hat{\mu}^{\text{LASSO}}(\lambda) = \operatorname{argmin}_{\{\mu_t\}} \left[ \sum (y_t - \mu_t)^2 + \lambda \sum_{j=2}^{n-1} |(\mu_{j+1} - \mu_j) - (\mu_j - \mu_{j-1})| \right]$$
(Trend Filtering)

`cvxpy`

**Selection of $\lambda$ by CV**

---

$$\sum_{t=1}^n \left[ y_t - \beta_0 - \beta_1(t-1) - \beta_2 \operatorname{ReLU}(t-2) - \dots - \beta_{n-1} \operatorname{ReLU}(t-(n-1)) \right]^2 + \lambda (\beta_2^2 + \dots + \beta_{n-1}^2)$$

minimize to get $\hat{\beta}^{\text{ridge}}(\lambda)$

$$t = 1, \dots, n$$

$$T_{\text{train}}, \quad T_{\text{test}} \longrightarrow \text{SPLIT}$$

e.g.: last $20\% \to T_{\text{test}}$
first $80\% \to T_{\text{train}}$

$$\hat{\beta}_{\text{train}}^{\text{ridge}}(\lambda) = \operatorname{minimize}_{\beta_0, \beta_1, \dots, \beta_{n-1}} \left[ \sum_{t \in T_{\text{train}}} (\quad)^2 + \lambda (\beta_2^2 + \dots + \beta_{n-1}^2) \right]$$

For every $t \in T_{\text{test}}$, calculate

$$\hat{y}_t(\lambda) = \hat{\beta}_0^{\text{ridge, train}}(\lambda) + \hat{\beta}_1^{\text{ridge, train}}(\lambda)(t-1) + \hat{\beta}_2^{\text{ridge, train}}(\lambda) \operatorname{ReLU}(t-2) + \dots + \hat{\beta}_{n-1}^{\text{ridge, train}} \operatorname{ReLU}(t-(n-1))$$

$$\operatorname{MSE}(\lambda, \text{split}) = \sum_{t \in T_{\text{test}}} (y_t - \hat{y}_t(\lambda))^2$$

---

$$\text{split}_1, \, \text{split}_2, \, \dots, \, \text{split}_S$$

$$\operatorname{MSE}(\lambda, \text{all splits}) = \sum_{i=1}^S \operatorname{MSE}(\lambda, \text{split}_i)$$

Candidate $\lambda$s: $\{10^{-6}, 10^{-5}, \dots, 10^5, 10^6, 10^7\}$

**Shrinkage (Ridge) vs Sparsity (LASSO)**

$y \in \mathbb{R}$

$$\min_\beta \left[ (y - \beta)^2 + \lambda \beta^2 \right] \longrightarrow \hat{\beta} = \frac{y}{1 + \lambda}$$

$$\lambda > 0$$

$$\min_\beta \left[ (y - \beta)^2 + \lambda |\beta| \right] \longrightarrow \text{Proof in notes}$$

Ans:
$$\hat{\beta} = \begin{cases}
y - \frac{\lambda}{2} & y > \frac{\lambda}{2} \\
y + \frac{\lambda}{2} & y < -\frac{\lambda}{2} \\
0 & -\frac{\lambda}{2} \le y \le \frac{\lambda}{2}
\end{cases}$$

**SOFT-THRESHOLDING**
$S_{\frac{\lambda}{2}}(y)$ (Sparse)

---

[Up: contents](index.md)
