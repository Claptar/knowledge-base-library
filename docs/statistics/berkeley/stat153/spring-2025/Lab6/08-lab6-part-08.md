---
title: Lab6 Part 08 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab6 Part 08 —

**Source:** [`Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

b_ridge = solve_ridge(X, y, lambda_val = 1000)
ridge_fitted = np.dot(X, b_ridge)

plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(ridge_fitted, color = 'red', label = 'Ridge')
plt.plot(truth, color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
b_lasso = solve_lasso(X, y, lambda_val = 100)
lasso_fitted = np.dot(X, b_lasso)

plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(lasso_fitted, color = 'red', label = 'LASSO')
plt.plot(truth, color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The LASSO fit is piecewise constant while the ridge fit is smoother (unless $\lambda$ is too small). Since the true function is also piecewise constant, LASSO gives better estimates in this problem compared to ridge regression.

Let us now use 5-fold cross validation as in class to pick the tuning parameter $\lambda$.

```python
def ridge_cv(X, y, lambda_candidates):
    n = len(y)
    folds = []
    for i in range(5):
        test_indices = np.arange(i, n, 5)
        train_indices = np.array([j for j in range(n) if j % 5 != i])
        folds.append((train_indices, test_indices))
    cv_errors = {lamb: 0 for lamb in lambda_candidates}

    for train_index, test_index in folds:
        X_train = X[train_index]
        X_test = X[test_index]
        y_train = y[train_index]
        y_test = y[test_index]

        for lamb in lambda_candidates:
            beta = solve_ridge(X_train, y_train, lambda_val = lamb)
            y_pred = np.dot(X_test, beta)
            squared_errors = (y_test - y_pred) ** 2
            cv_errors[lamb] += np.sum(squared_errors)
    for lamb in lambda_candidates:
        cv_errors[lamb] /= n

    best_lambda = min(cv_errors, key = cv_errors.get)

    return best_lambda, cv_errors
```

```python
lambda_candidates = np.array([0.1, 1, 10, 100, 1000, 10000, 100000])
print(lambda_candidates)

best_lambda, cv_errors = ridge_cv(X, y, lambda_candidates)
print(best_lambda)
print("CV errors for each lambda:")
for lamb, error in sorted(cv_errors.items()):
    print(f"Lambda = {lamb:.2f}, CV Error = {error:.6f}")
```

```
[1.e-01 1.e+00 1.e+01 1.e+02 1.e+03 1.e+04 1.e+05]
10.0
CV errors for each lambda:
Lambda = 0.10, CV Error = 35.016886
Lambda = 1.00, CV Error = 30.595315
Lambda = 10.00, CV Error = 28.126842
Lambda = 100.00, CV Error = 29.269337
Lambda = 1000.00, CV Error = 36.342592
Lambda = 10000.00, CV Error = 48.464228
Lambda = 100000.00, CV Error = 66.791586
```

The best $\lambda$ given by CV for ridge is 10. This value is small enough for the method to pick up the jumps well. But unfortunately the estimate will be too wiggly in the constant parts.

```python
b_ridge = solve_ridge(X, y, lambda_val = 10)
ridge_fitted = np.dot(X, b_ridge)

plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(ridge_fitted, color = 'red', label = 'Ridge')
plt.plot(truth, color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
def lasso_cv(X, y, lambda_candidates):
    n = len(y)
    folds = []
    for i in range(5):
        test_indices = np.arange(i, n, 5)
        train_indices = np.array([j for j in range(n) if j % 5 != i])
        folds.append((train_indices, test_indices))
    cv_errors = {lamb: 0 for lamb in lambda_candidates}

    for train_index, test_index in folds:
        X_train = X[train_index]
        X_test = X[test_index]
        y_train = y[train_index]
        y_test = y[test_index]

        for lamb in lambda_candidates:
            beta = solve_lasso(X_train, y_train, lambda_val = lamb)
            y_pred = np.dot(X_test, beta)
            squared_errors = (y_test - y_pred) ** 2
            cv_errors[lamb] += np.sum(squared_errors)
    for lamb in lambda_candidates:
        cv_errors[lamb] /= n

    best_lambda = min(cv_errors, key = cv_errors.get)

    return best_lambda, cv_errors
```

```python
lambda_candidates = np.array([0.1, 1, 10, 100, 1000, 10000, 100000])
print(lambda_candidates)

best_lambda, cv_errors = lasso_cv(X, y, lambda_candidates)
print(best_lambda)
print("CV errors for each lambda:")
for lamb, error in sorted(cv_errors.items()):
    print(f"Lambda = {lamb:.2f}, CV Error = {error:.6f}")
```

```
[1.e-01 1.e+00 1.e+01 1.e+02 1.e+03 1.e+04 1.e+05]
100.0
CV errors for each lambda:
Lambda = 0.10, CV Error = 36.683225
Lambda = 1.00, CV Error = 35.473742
Lambda = 10.00, CV Error = 29.134453
Lambda = 100.00, CV Error = 27.146439
Lambda = 1000.00, CV Error = 45.607291
Lambda = 10000.00, CV Error = 76.963133
Lambda = 100000.00, CV Error = 76.963133
```

The best $\lambda$ chosen by cross validation is 100; which seems a good choice for this dataset.

```python
b_lasso = solve_lasso(X, y, lambda_val = 100)
lasso_fitted = np.dot(X, b_lasso)

plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(lasso_fitted, color = 'red', label = 'LASSO')
plt.plot(truth, color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

What happens when we try the same model (with ReLU functions) as in class for this dataset?

```python
n = len(y)
x = np.arange(1, n + 1)
Xfull = np.column_stack([np.ones(n), x - 1])
for i in range(n - 2):
    c = i + 2
    xc = ((x > c).astype(float)) * (x - c)
    Xfull = np.column_stack([Xfull, xc])

print(Xfull)
```

```
[[ 1.000e+00  0.000e+00 -0.000e+00 ... -0.000e+00 -0.000e+00 -0.000e+00]
 [ 1.000e+00  1.000e+00  0.000e+00 ... -0.000e+00 -0.000e+00 -0.000e+00]
 [ 1.000e+00  2.000e+00  1.000e+00 ... -0.000e+00 -0.000e+00 -0.000e+00]
 ...
 [ 1.000e+00  2.045e+03  2.044e+03 ...  1.000e+00  0.000e+00 -0.000e+00]
 [ 1.000e+00  2.046e+03  2.045e+03 ...  2.000e+00  1.000e+00  0.000e+00]
 [ 1.000e+00  2.047e+03  2.046e+03 ...  3.000e+00  2.000e+00  1.000e+00]]
```

Let us try the LASSO estimator.

```python
b_lasso = solve_lasso(Xfull, y, lambda_val = 100)
lasso_fitted = np.dot(Xfull, b_lasso)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(lasso_fitted, color = 'red', label = 'LASSO')
plt.plot(truth, label = 'True trend', color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
b_lasso = solve_lasso(Xfull, y, lambda_val = 1000)
lasso_fitted = np.dot(Xfull, b_lasso)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(lasso_fitted, color = 'red', label = 'LASSO')
plt.plot(truth, label = 'True trend', color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

When $\lambda$ is small, this estimator will be too wiggly in the constant parts. On the other hand, when $\lambda$ is large, it will not be able to sharply detect the jumps.

---

[← note that penaltystart is now set to 1 (instead of 2 as in the model used in class)](07-note-that-penaltystart-is-now-set-to-1-instead-of-2-as-in-th.md) · [Up: contents](index.md)
