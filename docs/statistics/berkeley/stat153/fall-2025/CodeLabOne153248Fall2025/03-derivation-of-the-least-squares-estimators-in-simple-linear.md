---
title: Derivation of the Least Squares Estimators in Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Derivation of the Least Squares Estimators in Simple Linear Regression

**Source:** [`CodeLabOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The least squares estimators $\hat{\beta}_0$ and $\hat{\beta}_1$ minimize $$S(\beta_0, \beta_1) := \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$$ over all values of $\beta_0$ and $\beta_1$. In class, the following formulae were stated:
\begin{equation*}
   \hat{\beta}_1 = \frac{\sum_{i=1}^n (y_i - \bar{y})(x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2} \text{ and } \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}.
\end{equation*}
Here is how to prove it. We need to take the derivative of $S(\beta_0, \beta_1)$ with respect to $\beta_0$ and $\beta_1$ and equate them to zero. This gives:
\begin{align*}
   &\frac{\partial}{\partial \beta_0} S(\beta_0, \beta_1) = 0 \implies \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i) = 0 \\
   &\frac{\partial}{\partial \beta_1} S(\beta_0, \beta_1) = 0 \implies \sum_{i=1}^n x_i(y_i - \beta_0 - \beta_1 x_i) = 0
\end{align*}
Clearly the first equation is the same as:
\begin{equation*}
   \beta_0 = \bar{y} - \beta_1 \bar{x}.
\end{equation*}
Plugging this value of $\beta_0$ in the second equation, we get
\begin{equation*}
    0 = \sum_{i=1}^n x_i (y_i - \bar{y} - \beta_1 (x_i - \bar{x})) \implies \beta_1 = \frac{\sum_{i=1}^n x_i (y_i - \bar{y})}{\sum_{i=1}^n x_i (x_i - \bar{x})} = \frac{\sum_{i=1}^n (y_i - \bar{y})(x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2}.
\end{equation*}
There is a slightly different way of solving the equations. Use the vector matrix notation:
\begin{align*}
   y = \begin{pmatrix} y_1 \\ y_2 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} ~~ X = \begin{pmatrix}1 & x_1 \\ 1 & x_2 \\ \cdot & \cdot \\ \cdot & \cdot \\ \cdot & \cdot \\ 1 & x_n \end{pmatrix} ~~ \beta = \begin{pmatrix}\beta_0 \\ \beta_1 \end{pmatrix}.
\end{align*}
The two equations corresponding to $\frac{\partial}{\partial \beta_0} S(\beta_0, \beta_1) = 0$ and $\frac{\partial}{\partial \beta_1} S(\beta_0, \beta_1) = 0$ can be written using this notation as:
\begin{align*}
  X^T (y - X \beta) = 0 \implies X^T X \beta = X^T y \implies \beta = (X^T X)^{-1} X^T y.
\end{align*}
Writing out $(X^T X)^{-1}$ and multiplying out the product above, we can deduce the formulae for $\hat{\beta}_0$ and $\hat{\beta}_1$.

---

[← Google Trends Dataset for the query Amazon](02-google-trends-dataset-for-the-query-amazon.md) · [Up: contents](index.md)
