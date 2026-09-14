---
title: Or to see index-value pairs
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Or to see index-value pairs

**Source:** [`CodeLectureEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Fitting Smooth Trend Functions to Data

These models and the corresponding Ridge and LASSO estimators are useful for fitting trend functions to data.

The following two datasets are from [NOAA climate at a glance](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/tavg/land_ocean/1/1/1850-2025). They contain temperature anomalies for the months of January and June (for each year from 1850 to 2025). Anomalies are in celsius and are with respect to the 1901-2000 average.

```python
temp_jan = pd.read_csv('TempAnomalies_January.csv', skiprows=4)
temp_june = pd.read_csv('TempAnomalies_June.csv', skiprows=3)
print(temp_jan)
y_jan = temp_jan['Anomaly']
y_june = temp_june['Anomaly']
plt.plot(temp_jan['Year'], y_jan, label='January')
plt.plot(temp_jan['Year'], y_june, label='June')
plt.legend()
plt.xlabel('year')
plt.ylabel('Celsius')
plt.title('Temperature anomalies (from 1901-2000 average) for January')
plt.show()
```

```
Year  Anomaly
0    1850    -0.46
1    1851    -0.17
2    1852    -0.02
3    1853    -0.12
4    1854    -0.28
..    ...      ...
171  2021     0.83
172  2022     0.92
173  2023     0.89
174  2024     1.30
175  2025     1.33

[176 rows x 2 columns]
```

*(1 figure omitted — see the original notebook.)*

We shall fit a trend function to each of these two datasets. The first step is to create the $X$ matrix.

```python
n = len(y_jan) #both datasets have the same length, so the X matrix will be the same for both
x = np.arange(1, n+1)
Xfull = np.column_stack([np.ones(n), x-1])
for i in range(n-2):
    c = i+2
    xc = ((x > c).astype(float))*(x-c)
    Xfull = np.column_stack([Xfull, xc])
print(Xfull)
```

```
[[  1.   0.  -0. ...  -0.  -0.  -0.]
 [  1.   1.   0. ...  -0.  -0.  -0.]
 [  1.   2.   1. ...  -0.  -0.  -0.]
 ...
 [  1. 173. 172. ...   1.   0.  -0.]
 [  1. 174. 173. ...   2.   1.   0.]
 [  1. 175. 174. ...   3.   2.   1.]]
```

The ridge regression estimate is computed below. Start with some standard choice of $\lambda$ (e.g., $\lambda = 1$) and then increase or decrease it by factors of 10 until you get a fit that is visually nice (smooth while capturing patterns in the data).

```python
b_ridge_jan = solve_ridge(Xfull, y_jan, lambda_val = 1000)
ridge_fitted_jan = np.dot(Xfull, b_ridge_jan)

b_ridge_june = solve_ridge(Xfull, y_june, lambda_val = 1000)
ridge_fitted_june = np.dot(Xfull, b_ridge_june)

plt.figure(figsize = (10, 6))
#plt.plot(temp_jan['Year'], y_jan, color = 'lightgray')
plt.plot(temp_jan['Year'], ridge_fitted_jan, color = 'red', label = 'January Ridge')
plt.plot(temp_jan['Year'], ridge_fitted_june, color = 'blue', label = 'June Ridge')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We repeat the exercise with LASSO below.

```python
b_lasso_jan = solve_lasso(Xfull, y_jan, lambda_val = 10)
lasso_fitted_jan = np.dot(Xfull, b_lasso_jan)

b_lasso_june = solve_lasso(Xfull, y_june, lambda_val = 10)
lasso_fitted_june = np.dot(Xfull, b_lasso_june)

plt.figure(figsize = (10, 6))
#plt.plot(temp_jan['Year'], y, color = 'lightgray')
plt.plot(temp_jan['Year'], lasso_fitted_jan, color = 'red', label = 'January LASSO')
plt.plot(temp_jan['Year'], lasso_fitted_june, color = 'blue', label = 'June LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Cross-validation for picking $\lambda$

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
y = y_jan
lambda_candidates = np.array([0.1, 1, 10, 100, 1000, 10000, 100000])

best_lambda, cv_errors = ridge_cv(Xfull, y, lambda_candidates)
print(best_lambda)
for lamb, error in sorted(cv_errors.items()):
    print(f"Lambda = {lamb:.2f}, CV Error = {error:.6f}")
```

```
1000.0
Lambda = 0.10, CV Error = 11.850955
Lambda = 1.00, CV Error = 2.261767
Lambda = 10.00, CV Error = 0.513626
Lambda = 100.00, CV Error = 0.126082
Lambda = 1000.00, CV Error = 0.044625
Lambda = 10000.00, CV Error = 0.048169
Lambda = 100000.00, CV Error = 0.073446
```

```python
def lasso_cv(X, y, lambda_candidates):
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
            beta = solve_lasso(X_train, y_train, lambda_val=lamb)
            y_pred = np.dot(X_test, beta)
            squared_errors = (y_test - y_pred) ** 2
            cv_errors[lamb] += np.sum(squared_errors)

    for lamb in lambda_candidates:
        cv_errors[lamb] /= n

    best_lambda = min(cv_errors, key=cv_errors.get)
    return best_lambda, cv_errors
```

```python
y = y_june
lambda_candidates = np.array([0.1, 1, 10, 100, 1000, 10000, 100000])
best_lambda, cv_errors = lasso_cv(Xfull, y, lambda_candidates)
print(best_lambda)
for lamb, error in sorted(cv_errors.items()):
    print(f"Lambda = {lamb:.2f}, CV Error = {error:.6f}")
```

```
10.0
Lambda = 0.10, CV Error = 1.907423
Lambda = 1.00, CV Error = 0.072098
Lambda = 10.00, CV Error = 0.038189
Lambda = 100.00, CV Error = 0.078824
Lambda = 1000.00, CV Error = 0.165582
Lambda = 10000.00, CV Error = 0.165582
Lambda = 100000.00, CV Error = 0.165582
```

## Shrinkage and Sparsity

Let us compare the ridge regularized estimates of $\beta$ with the unregularized estimates (unregularized means $\lambda = 0$).

```python
y = y_jan
b_ridge_0 = solve_ridge(Xfull, y, lambda_val = 0)
b_ridge = solve_ridge(Xfull, y, lambda_val = 1000)
plt.scatter(b_ridge_0[2:], b_ridge[2:])
print(b_ridge_0[1], b_ridge[1])
print(b_ridge_0[0], b_ridge[0])
```

```
0.28999999999997206 0.003551957730090027
-0.4599999999999922 -0.18495721415398625
```

*(1 figure omitted — see the original notebook.)*

Note that the $y$-axis above has a much tighter range compared to the $x$-axis. This illustrates the **shrinkage** aspect of ridge regression. It shrinks the unregularized estimates towards zero.

```python
y = y_jan
b_lasso_0 = solve_lasso(Xfull, y, lambda_val = 0)
b_lasso = solve_lasso(Xfull, y, lambda_val = 10)
plt.scatter(b_lasso_0[2:], b_lasso[2:])
print(b_lasso_0[1], b_lasso[1])
print(b_lasso_0[0], b_lasso[0])
```

```
0.290000000008449 -0.00183578311693186
-0.46000000053282925 -0.14899519332692354
```

*(1 figure omitted — see the original notebook.)*

This plot clearly shows that the LASSO sets most coefficients exactly to zero. Compare this plot to the corresponding plot for the ridge estimator. This means that LASSO is setting most of the $\beta_j$'s to zero. This is referred to as **sparsity**.

Ridge estimation results in shrinkage and LASSO estimation results in sparsity.

## Simulated Data

I am simulating two time series datasets (of the same size $n = 1000$) using the code below.

```python
def smoothfun(x):
    ans = np.sin(15*x) + 3*np.exp(-(x ** 2)/2) + 0.5*((x - 0.5) ** 2) + 5 * np.log(x + 0.1) + 7
    return ans

n = 1000
xx = np.linspace(0, 1, n)
truth_1 = np.array([smoothfun(x) for x in xx])

sig_1 = 2
rng = np.random.default_rng(seed = 42)
errorsamples_1 = rng.normal(loc=0, scale = sig_1, size = n)
y_1 = truth_1 + errorsamples_1


xx = np.linspace(0, 1, n)
truth_2 = 0.8*truth_1

sig_2 = 3
errorsamples_2 = rng.normal(loc=0, scale = sig_2, size = n)
y_2 = truth_2 + errorsamples_2
```

Here are the two datasets plotted.

```python
fig, axes = plt.subplots(2, 1, figsize=(6, 4), sharex=True)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [First panel →](03-first-panel.md)
