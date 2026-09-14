---
title: Ridge regression with cross validation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Ridge regression with cross validation

**Source:** [`public/labs/Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Ridge model from scikitlearn

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

---

[← Lab 6](01-lab-6.md) · [Up: contents](index.md) · [Ridge with time series CV →](03-ridge-with-time-series-cv.md)
