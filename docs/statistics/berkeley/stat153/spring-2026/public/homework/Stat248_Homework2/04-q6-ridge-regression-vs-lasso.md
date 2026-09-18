---
title: Q6. Ridge regression vs. LASSO
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q6. Ridge regression vs. LASSO

**Q6a. Suppose you are modeling sunspot counts (from Q3) as a sum of $K=100$ sinusoidal components (200 regressors: a cosine and sine for each frequency). Without running any models yet, describe why OLS is likely to overfit this model, and how ridge regression and lasso would each address this differently. What happens to the 200 coefficients, and how would they look (qualitatively) different? (3 points)**

**Q6b. Now fit the OLS model using statsmodels with 100 frequencies, and plot the result for y vs t (the original data) and y_hat (OLS) vs t. In another plot, plot the $\beta$ coefficients and comment on their structure (are they positive, negative, mostly zero? Anything notable?). (4 points)**

```python
# FILL IN CODE
```

**Q6c. Fit the ridge model using cross-validation. Be sure to use a method for cross-validation that preserves auto-correlations in your stimulus, which is required when doing time series regression. (2 points)**

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

# FILL IN CODE
```

**Q6d. Fit the LASSO model using cross-validation. Use the same X and y matrices, just change to using an L1 penalty. You can use sklearn.linear_model.Lasso here along with the same cross-validation scheme you used above. Plot the LASSO prediction on top of the original data and comment on what you see. (2 points)**

```python
from sklearn.linear_model import Lasso

# FILL IN CODE
```

**Q6e. Re-fit the Ridge model using three different regularization values `alpha = [0.1, 100, 1000]`, and plot the resulting predictions on top of one another and on top of the original data (on the same plot), with each labeled. What do you notice about how the prediction changes as alpha varies? What about the coefficients? (3 points)**

```python
for alpha in [0.1, 100, 1000]:
    # FILL IN CODE
```

**Q6f. Repeat Q6e but with LASSO, using `alpha = [0.1, 5, 10]`. Plot the resulting predictions for each of these `alpha` values on top of the true data and comment on how this differs from ridge (or not). What about the coefficients? (3 points)**

```python
for alpha in [0.1, 5, 10]:
    # FILL IN CODE
```

## Q7. Cross-validation for time series

Above, you used time series cross-validation to select regularization parameter `alpha` for both ridge and lasso. Explain why the optimal `alpha` values will generally differ by orders of magnitude for ridge and lasso, and why this does not mean one method is "more regularized" than the other. (2 points)

---

[← Q3. Sinusoidal regression](03-q3-sinusoidal-regression.md) · [Up: contents](index.md) · [Q8. Sinusoidal regression and covariance of estimators →](05-q8-sinusoidal-regression-and-covariance-of-estimators.md)
