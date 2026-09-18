---
title: Ridge and LASSO regularized estimation
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Ridge and LASSO regularized estimation

We now compute the ridge and lasso regularized estimators using the optimization library `cvxpy`. `cvxpy` is a library for formulating and solving convex optimization problems. It is widely used in Machine Learning, Statistics, Engineering etc.

```python
import cvxpy as cp
```

Here is the function for solving the ridge optimization problem. Given $y_{n \times 1}$, $X_{n  \times m}$ and $\lambda$, this code solves the problem:
\begin{align*}
    \text{Minimize} ~ \left[\|y - X \beta\|^2 + \lambda (\beta_s^2 + \dots + \beta_m^2) \right]
\end{align*}
Here $s$ denotes `penalty_start` in the code (the penalty does not involve $\beta_j$ for $j < s$).

```python
def solve_ridge(X, y, lambda_val, penalty_start=2):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

Below is the code for computing the ridge estimator with a fixed value of $\lambda$. We also plot the fitted values (these are the values $\hat{\mu}^{\text{ridge}}(\lambda) = X \hat{\beta}^{\text{ridge}}(\lambda)$) corresponding to the Ridge estimate.

Play around with  different values of $\lambda$ and see how the estimator changes.

```python
b_ridge = solve_ridge(Xfull, y, lambda_val = 10000) #lambda = 10000 seems to work well
#print(b_ridge)
plt.plot(y)
ridge_fitted = np.dot(Xfull, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here is the function for minimizing the LASSO objective function. Given $y_{n \times 1}$, $X_{n  \times m}$ and $\lambda$, this code solves the problem:
\begin{align*}
    \text{Minimize} ~ \left[\|y - X \beta\|^2 + \lambda (|\beta_s| + \dots + |\beta_m|) \right]
\end{align*}
Here $s$ denotes `penalty_start` in the code (the penalty does not involve $\beta_j$ for $j < s$).

```python
def solve_lasso(X, y, lambda_val, penalty_start=2):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.norm1(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

Below is the code for computing the ridge estimator with a fixed value of $\lambda$. We also plot the fitted values (these are the values $\hat{\mu}^{\text{lasso}}(\lambda) = X \hat{\beta}^{\text{lasso}}(\lambda)$) corresponding to the Ridge estimate.

Play around with  different values of $\lambda$ and see how the estimator changes.

```python
b_lasso = solve_lasso(Xfull, y, lambda_val = 25) #10 seems to work well
#print(b_lasso)
plt.plot(y)
lasso_fitted = np.dot(Xfull, b_lasso)
plt.plot(lasso_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The LASSO estimator is typically sparse. This can be checked by the code below where we only display the estimated coefficients which cross a threshold in absolute value.

```python
threshold = 1e-6
significant_idx = np.where(np.abs(b_lasso) > threshold)[0]
print(b_lasso[significant_idx])
# Or to see index-value pairs:
for idx in significant_idx:
    print(f"Index {idx}: {b_lasso[idx]}")
```

```
[ 7.40101781e+00  3.90266732e-02 -6.92496253e-04 -1.95497046e-03
 -1.41763312e-02 -3.62292248e-03 -6.37795834e-03]
Index 0: 7.401017811074355
Index 1: 0.03902667316754264
Index 29: -0.0006924962529493638
Index 30: -0.001954970458737117
Index 64: -0.01417633117574186
Index 65: -0.003622922481167155
Index 91: -0.006377958342345468
```

Below we plot both the ridge and LASSO fits.

```python
plt.plot(y, color = 'None')
ridge_fitted = np.dot(Xfull, b_ridge)
plt.plot(ridge_fitted, color = 'red')
lasso_fitted = np.dot(Xfull, b_lasso)
plt.plot(lasso_fitted, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The two fitted values seem quite similar.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Fitting Smooth Trend Functions to Data →](03-fitting-smooth-trend-functions-to-data.md)
