---
title: FILL IN CODE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# FILL IN CODE

**Source:** [`public/homework/Stat248_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Q8. Sinusoidal regression and covariance of estimators

Consider the sinusoidal model:

$$y_t = \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t$$

for $t = 1, \ldots, n$, where $f$ is a known frequency and $\epsilon_t \sim N(0, \sigma^2)$ i.i.d.

Q8a. Show that as $n \to \infty$, the cosine and sine regressors become orthogonal:

$$\frac{1}{n}\sum_{t=1}^n \cos(2\pi f t)\sin(2\pi f t) \to 0$$

*Hint: use the product-to-sum identity $\cos(\theta)\sin(\theta) = \frac{1}{2}\sin(2\theta)$.*

What does this imply about $\text{Cov}(\hat{\beta_1}, \hat{\beta_2})$, the covariance between the OLS estimates of $\beta_1$ and $\beta_2$? Why is this a desirable property for regression? (2 points)

Q8b. The amplitude of the sinusoidal component is $R = \sqrt{\beta_1^2 + \beta_2^2}$. A natural estimator of $R^2$ is $\hat{R}^2 = \hat{\beta_1}^2 + \hat{\beta_2}^2$, where $\hat{\beta_1}$ and $\hat{\beta_2}$ are the OLS estimates. Derive an expression for $E[\hat{R}^2]$ in terms of $R^2$, $\text{Var}(\hat{a})$, and $\text{Var}(\hat{b})$. (2 poin

Q8c. Is $\hat{R}^2$ a biased estimator of $R^2$? If so, in what direction?

Under what conditions is the bias most severe? What happens when there is no true signal ($R^2 = 0$)?

*Hint: recall that for any estimator $\hat{\theta}$, we have $E[\hat{\theta}^2] = \text{Var}(\hat{\theta}) + (E[\hat{\theta}])^2$.*

---

[← FILL IN CODE](05-fill-in-code.md) · [Up: contents](index.md)
