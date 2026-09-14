---
title: Compare to the Lasso model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Compare to the Lasso model

**Source:** [`public/labs/Lab6_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here we will compare to the Lasso model, which minimizes

$$\displaystyle\sum_{i=1}^n \left( y_i -\beta_0 - \displaystyle\sum_{j=1}^{p} \beta_j x_{ij}\right)^2 + \lambda \displaystyle\sum_{j=1}^p |\beta_j| = \text{RSS} + \lambda \displaystyle\sum_{j=1}^p |\beta_j|$$

```python
from sklearn.linear_model import Lasso

lasso_search = GridSearchCV(
    Lasso(max_iter=20000),
    param_grid={'alpha': alphas},
    cv=tscv,
    scoring='neg_mean_squared_error'
)
lasso_search.fit(X, y)

print(f"Best lasso lambda: {lasso_search.best_params_['alpha']}")
best_lasso = lasso_search.best_estimator_
print(f"Lasso intercept: {best_lasso.intercept_}")
#print(f"Lasso coefficients: {best_lasso.coef_}")
print(f"Lasso nonzero coefficients: {np.sum(best_lasso.coef_ != 0)}")

y_hat_lasso = lasso_search.predict(X)

plt.plot(t, y)
plt.plot(t, y_hat_lasso)

plt.figure()
print(y_hat_lasso.shape)

plt.figure()
plt.plot(best_lasso.coef_)
```

```
Best lasso lambda: 0.2592943797404667
Lasso intercept: 17.088178880939797
Lasso nonzero coefficients: 4
(600,)
[<matplotlib.lines.Line2D at 0x332280790>]
<Figure size 640x480 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

What do you notice here about the coefficients compared to ridge regression? Does one seem to work better over the other?

---

[← How ridge regularization affects predictions](06-how-ridge-regularization-affects-predictions.md) · [Up: contents](index.md) · [Test specific alpha parameters →](08-test-specific-alpha-parameters.md)
