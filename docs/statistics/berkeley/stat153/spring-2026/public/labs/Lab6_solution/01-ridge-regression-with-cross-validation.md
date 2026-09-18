---
title: Ridge regression with cross validation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab6_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Ridge regression with cross validation

In this lab we will go over ridge and lasso regularization with cross-validation using some of the libraries from scikit learn (sklearn).

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
```

Recall that the ridge regression solution minimizes the following function:

$$\displaystyle\sum_{i=1}^n \left(y_i - \beta_0 - \displaystyle\sum_{j=1}^p \beta_j x_{ij}\right)^2 + \lambda \displaystyle\sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \displaystyle\sum_{j=1}^p \beta_j^2$$

We will now try this for the star dataset from ASTSA (loaded here as a csv file that can also be downloaded from the course github: https://github.com/berkeley-stat153/spring-2026/blob/main/public/labs/star.csv

The data reflect the magnitude of a star taken at midnight for 600 consecutive days. The data are taken from the classic text, The Calculus of Observations, a Treatise on Numerical Mathematics, by E.T. Whittaker and G. Robinson, (1923, Blackie and Son, Ltd.).

```python
star=pd.read_csv('star.csv')
t = star['index']
y = star['value']

plt.plot(t, y)
plt.xlabel('index')
plt.ylabel('value')
```

```
Text(0, 0.5, 'value')
```

*(1 figure omitted — see the original notebook.)*

### Ridge model from scikitlearn

We can use scikitlearn's `Ridge`, `GridSearchCV`, and `TimeSeriesSplit` to perform ridge regression along with cross-validation, and specifically ensuring that we use a time-series safe split.

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

fs = 600
nf = 200

f_grid = np.linspace(1/len(y), 0.5, nf)

cols = [np.ones(len(t))]  # intercept
for f2 in f_grid:
    cols.append(np.cos(2 * np.pi * f2 * t))
    cols.append(np.sin(2 * np.pi * f2 * t))

X = np.column_stack(cols)

alphas = np.logspace(-3, 4, 30)
tscv = TimeSeriesSplit(n_splits=5)

# Ridge with time series CV
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

```
Best ridge lambda: 22.122162910704503
Ridge intercept: 17.0844703800242
[<matplotlib.lines.Line2D at 0x330f463b0>]
```

*(1 figure omitted — see the original notebook.)*

### Plot the ridge coefficients

Next we'll inspect what the actual coefficients look like for each of our frequencies in the grid search

```python
# Plot the ridge coefficients, note that the intercept is stored as a different parameter here
plt.figure()
plt.plot(best_ridge.coef_)
print(best_ridge.intercept_)
```

```
17.0844703800242
```

*(1 figure omitted — see the original notebook.)*

What do you notice about the coefficients here?  Can you make this more interpretable by including the frequencies somehow?

## Coefficient paths

Another point we briefly touched on is that you can look at the beta estimates as a function of your regularization parameter. Here we can refit our coefficients in a loop, then plot the coefficients vs. the alpha values to observe how greater values of alpha more strongly shrink the coefficients.

```python
coef_matrix = np.zeros((len(alphas), X[:, 1:].shape[1]))

for i, a in enumerate(alphas):
    coef_matrix[i] = Ridge(alpha=a, fit_intercept=True).fit(X[:, 1:], y).coef_
```

```python
plt.semilogx(alphas,coef_matrix);
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
```

```
Text(0, 0.5, 'Coefficient')
```

*(1 figure omitted — see the original notebook.)*

## How ridge regularization affects predictions

We have observed how changing our regularization parameter affects the parameters, but what about the predictions themselves? Here we will plot the estimates from ridge on top of the original data. What do you notice?

Also try some other values of alpha (or go back and change your X parameters to add fewer or more frequencies in the grid search).

```python
for alpha in [0.1, 100, 1000]:
    model = Ridge(alpha=alpha).fit(X, y)
    y_hat_ridge = model.predict(X)
    plt.plot(t, y_hat_ridge, label=f'λ={alpha}')

plt.legend()
```

```
<matplotlib.legend.Legend at 0x332065150>
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Compare to the Lasso model →](02-compare-to-the-lasso-model.md)
