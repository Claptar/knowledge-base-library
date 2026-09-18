---
title: 5 Ridge vs LASSO
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 Ridge vs LASSO

The LASSO estimator $\hat{\beta}^{\text{lasso}}(\lambda)$ is usually sparse which means that most of $\hat{\beta}_2^{\text{lasso}}(\lambda), \dots, \hat{\beta}_{n-1}^{\text{lasso}}(\lambda)$ are exactly (up to numerical precision) equal to zero. This implies that $\hat{\mu}_t^{\text{lasso}}(\lambda)$ is piecewise linear. On the other hand, $\hat{\beta}^{\text{ridge}}(\lambda)$ will not be sparse in that all the terms $\hat{\beta}_2^{\text{ridge}}(\lambda), \dots, \hat{\beta}_{n-1}^{\text{ridge}}(\lambda)$ will be nonzero (even though they may be small). This gives a smooth appearance to $\hat{\beta}^{\text{ridge}}(\lambda)$.

Some insight into the tendency of the LASSO regularization to yield exact zeroes in contrast to ridge regularization can be gained from the following two simple facts.

**Fact 5.1** (Simple Ridge). *Suppose $y$ is a real number and $\lambda > 0$. Then the minimizer of*
$$f(\beta) = (y - \beta)^2 + \lambda\beta^2$$
*is given by*
$$\hat{\beta} = \frac{y}{1 + \lambda}.$$

*Proof.* We just need to differentiate $f$ and set the derivative to zero:
$$f'(\beta) = 2(\beta - y) + 2\lambda\beta = 0 \implies \beta = \frac{y}{1 + \lambda}.$$
$\square$

**Fact 5.2** (Simple LASSO). *Suppose $y$ is a real number and $\lambda > 0$. Then the minimizer of*
$$f(\beta) = (y - \beta)^2 + \lambda|\beta|$$
*is given by*
$$\hat{\beta} = \begin{cases}
y - \lambda/2 & \text{if } y > \lambda/2 \\
y + \lambda/2 & \text{if } y < -\lambda/2 \\
0 & \text{if } -\lambda/2 \le y \le \lambda/2.
\end{cases}$$

*Proof.* The derivative of $f$ is given by:
$$f'(\beta) = \begin{cases}
2(\beta - y) + \lambda & \text{if } \beta > 0 \\
2(\beta - y) - \lambda & \text{if } \beta < 0.
\end{cases}$$
At $\beta = 0$, the function $|\beta|$ is not differentiable. We now need to set the derivative to zero. Setting to zero the expression for $f'(\beta)$ for $\beta > 0$, we get
$$2(\beta - y) + \lambda = 0 \implies \beta = y - \frac{\lambda}{2}.$$
Since this expression for $f'(\beta)$ is only valid when $\beta > 0$, we need to assume that $y > \lambda/2$.

Similarly setting to zero the expression for $f'(\beta)$ when $\beta < 0$, we get
$$2(\beta - y) - \lambda = 0 \implies \beta = y + \frac{\lambda}{2}$$
which is valid when $y + \lambda/2 < 0$ or $y < -\lambda/2$.

The above calculations show that $\hat{\beta}$ equals $y - \lambda/2$ when $y > \lambda/2$, and that $\hat{\beta}$ equals $y + \lambda/2$ when $y < -\lambda/2$. In the intermediate range $-\lambda/2 \le y \le \lambda/2$, check that $f'(\beta) < 0$ for $\beta < 0$ and $f'(\beta) > 0$ for $\beta > 0$. This means that $f$ is decreasing on $(-\infty, 0)$ and then increasing on $(0, \infty)$ which implies that the minimum of $f$ has to be achieved at 0. $\square$

From these facts, it is clear that when $y \neq 0$, the ridge minimizer will never be zero, while the lasso minimizer will equal exactly zero for all $y$-values in the range $[-\lambda/2, \lambda/2]$. The LASSO penalty therefore has a tendency to produce exact zeros unlike the ridge penalty.

---

[← 4 Regularized Estimates](02-4-regularized-estimates.md) · [Up: contents](index.md) · [6 Cross-validation for selecting $\lambda$ →](04-6-cross-validation-for-selecting.md)
