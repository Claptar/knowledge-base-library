---
title: Ridge with time series CV
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Ridge with time series CV

**Source:** [`public/labs/Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ridge_search = GridSearchCV(
    Ridge(),
    param_grid={'alpha': alphas},
    cv=tscv,
    scoring='neg_mean_squared_error'
)
ridge_search.fit(X, y)

print(f"Best ridge lambda: {ridge_search.best_params_['alpha']}")
y_hat_ridge = ridge_search.predict(X)

best_ridge = ridge_search.best_estimator_
print(f"Ridge intercept: {best_ridge.intercept_}")

plt.plot(t, y)
plt.plot(t, y_hat_ridge)
```

## Plot the ridge coefficients

Next we'll inspect what the actual coefficients look like for each of our frequencies in the grid search

```python

---

[← Ridge regression with cross validation](02-ridge-regression-with-cross-validation.md) · [Up: contents](index.md) · [Lab6 Part 04 — →](04-lab6-part-04.md)
