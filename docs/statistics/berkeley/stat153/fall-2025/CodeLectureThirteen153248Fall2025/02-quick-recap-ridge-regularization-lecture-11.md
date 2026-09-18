---
title: 'Quick Recap: Ridge Regularization (Lecture 11)'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Quick Recap: Ridge Regularization (Lecture 11)

The estimator is given by the minimizer of:
\begin{align*}
   \|y - X \beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2
\end{align*}
where $\lambda$ is the tuning parameter. Small $\lambda$ leads to fitted values close to the data (overfitting) and large $\lambda$ leads to fitted values coming from a straight line (underfitting). We used the following code for computing the ridge estimator for fixed $\lambda$ (note that, instead of using this code, we can also use the formula derived in Lecture 12: $(X^T X + \lambda J)^{-1} X^T y$ to compute the ridge estimator).

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

```python
b_ridge = solve_ridge(X, y, lambda_val = 1e4) #also try 1e-4, 1e8 etc.
plt.plot(y)
ridge_fitted = np.dot(X, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To choose $\lambda$, we use cross-validation (CV). Here is the code for CV.

```python
def ridge_cv(X, y, lambda_candidates):
    n = len(y)
    k = 5
    fold_size = n // k
    folds = []

    for i in range(k):
        start = i * fold_size
        end = (i + 1) * fold_size if i < k - 1 else n  # last fold includes remainder
        test_indices = np.arange(start, end)
        train_indices = np.concatenate([np.arange(0, start), np.arange(end, n)])
        folds.append((train_indices, test_indices))

    cv_errors = {lamb: 0 for lamb in lambda_candidates}

    for train_index, test_index in folds:
        X_train = X[train_index]
        X_test = X[test_index]
        y_train = y[train_index]
        y_test = y[test_index]

        for lamb in lambda_candidates:
            beta = solve_ridge(X_train, y_train, lambda_val=lamb)
            y_pred = np.dot(X_test, beta)
            squared_errors = (y_test - y_pred) ** 2
            cv_errors[lamb] += np.sum(squared_errors)

    for lamb in lambda_candidates:
        cv_errors[lamb] /= n

    best_lambda = min(cv_errors, key=cv_errors.get)
    return best_lambda, cv_errors
```

```python
lambda_candidates = np.array([1e-2, 1e-1, 1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8])

best_lambda, cv_errors = ridge_cv(X, y, lambda_candidates)
print(best_lambda)
for lamb, error in sorted(cv_errors.items()):
    print(f"Lambda = {lamb:.2f}, CV Error = {error:.6f}")
```

```
1000.0
Lambda = 0.01, CV Error = 20.473188
Lambda = 0.10, CV Error = 11.850955
Lambda = 1.00, CV Error = 2.261767
Lambda = 10.00, CV Error = 0.513626
Lambda = 100.00, CV Error = 0.126082
Lambda = 1000.00, CV Error = 0.044625
Lambda = 10000.00, CV Error = 0.048169
Lambda = 100000.00, CV Error = 0.073446
Lambda = 1000000.00, CV Error = 0.105209
Lambda = 10000000.00, CV Error = 0.155146
Lambda = 100000000.00, CV Error = 0.167589
```

Below we calculate the ridge estimator for $\lambda$ chosen to be the best $\lambda$ given by CV:

```python
b_ridge = solve_ridge(X, y, lambda_val = best_lambda)
plt.plot(y)
ridge_fitted = np.dot(X, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Bayesian regularization (from Lecture 12) →](03-bayesian-regularization-from-lecture-12.md)
