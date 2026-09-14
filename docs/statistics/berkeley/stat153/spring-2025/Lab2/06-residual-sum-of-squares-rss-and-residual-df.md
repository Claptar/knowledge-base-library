---
title: Residual Sum of Squares (RSS) and Residual df
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Residual Sum of Squares (RSS) and Residual df

**Source:** [`Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Two other commonly used terms (in connection with residuals) are the Residual Sum of Squares (RSS) and the Residual Degrees of Freedom. The RSS is simply the sum of the squares of the residuals:
\begin{equation*}
   \text{RSS} = \sum_{i=1}^n e_i^2 = \sum_{t=1}^n \left(y_t - \hat{\beta}_0 - \hat{\beta}_1 t - \hat{\beta}_2 t^2 - \hat{\beta}_3 t^3 \right)^2
\end{equation*}
RSS is simply equal to the smallest possible of the sum of squares criterion $S(\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3)$ (recall from lecture that $S(\beta_0, \beta_1, \beta_2, \beta_3) = \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2 t^2 - \beta_3 t^3)^2$).

The vector of residuals has the following important property: $X^T e = 0$. This can be proved as follows:
\begin{equation*}
   X^T e = X^T (y - \hat{y}) = X^T (y - X \hat{\beta}) = X^T (y - X (X^T X)^{-1} X^T y) = X^T y - X^T X (X^T X)^{-1} X^T y = X^T y - X^T y = 0.
\end{equation*}
$X^T e = 0$ means that the dot product between every column of $X$ and $e$ equals 0. In our regression model for GDP, $X^T e = 0$ is equivalent to:
\begin{equation*}
   \sum_{t = 1}^n e_t = 0 ~~~~  \sum_{t = 1}^n t e_t = 0 ~~~~  \sum_{t = 1}^n t^2 e_t = 0 ~~~~  \sum_{t = 1}^n t^3 e_t = 0
\end{equation*}
Even though there are $n$ residuals $e_1, \dots, e_n$, they have to satisfy the above four equality constraints. Therefore, the effective number of 'free' residuals is $n-4$. Thus, the residual degrees of freedom equals $n-4$.

More generally, the residual df equals the number of observations ($n$) minus the number of columns in the $X$ matrix.

---

[← ACF Plot](05-acf-plot.md) · [Up: contents](index.md) · [Estimate of $\sigma$: the residual standard error →](07-estimate-of-the-residual-standard-error.md)
