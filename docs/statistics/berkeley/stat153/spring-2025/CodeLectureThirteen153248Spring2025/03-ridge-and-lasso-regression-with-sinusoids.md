---
title: Ridge and LASSO regression with sinusoids
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Ridge and LASSO regression with sinusoids

Let us now try the high-dimensional version of the sinusoidal model where we use sinusoids at all the Fourier frequencies:
\begin{equation*}
   y_t = \beta_0 + \sum_{j = 1}^{(n-1)/2} \left( \beta_{1j} \cos(2 \pi (j/n) t) + \beta_{2j} \sin (2 \pi (j/n) t) \right) + \epsilon_t
\end{equation*}
Here $n = 325$ is odd. If $n$ were even, we will add another term for $\cos (\pi t)$.

We would need to use some kind of regularization for meaningful estimation in this high-dimensional regression model. It is natural to try ridge or LASSO regularization. These will make the size of the coefficients $\beta_{1j}, \beta_{2j}$ small but this may not produce anything useful in this dataset. Let us illustrate this below.

The first step for implementing ridge or LASSO regularization is to create the $X$ matrix.

```python
#Creating the X matrix
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
m = (n-1)//2
for j in range(m):
    f = j/n
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([X, xcos, xsin])
```

We will use the same code for ridge and LASSO regression that we used last week.

```python
#note that penalty_start is now set to 1 (instead of 2 as in the model used in class)
def solve_ridge(X, y, lambda_val, penalty_start=1):
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
#note that penalty_start is now set to 1 (instead of 2 as in the model used in class)
def solve_lasso(X, y, lambda_val, penalty_start=1):
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

```python
b_ridge = solve_ridge(X, y, lambda_val = 200)
ridge_fitted = np.dot(X, b_ridge)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'gray')
plt.plot(ridge_fitted, color = 'red', label = 'Ridge')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fitted values produced by ridge regression appear to be very similar to the original data values but shrunk towards the overall mean of the data. The extent of shrinkage is controlled by the value of $\lambda$ (when $\lambda$ is small, these fitted values will be very close to the actual observations) It is unclear how these fitted values may be interpreted or how may they be useful. We can also estimate $\sigma$ and plot simulated datasets, and compare with the original dataset.

```python
sig_ridge = np.sqrt((np.sum((y - ridge_fitted) ** 2))/n)
print(sig_ridge)
```

```
34.13721232125516
```

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(6):
    errorsamples = rng.normal(loc = 0, scale = sig_ridge, size = n)
    sim_data = ridge_fitted + errorsamples
    axes[i].plot(sim_data)
axes[6].plot(y)
for i, idx in enumerate(range(7, 9)):
    errorsamples = rng.normal(loc = 0, scale = sig_ridge, size = n)
    sim_data = ridge_fitted + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

As before, one can easily spot the sunspots data from this plot-grid.

```python
#To illustrate the shrinkage effect of the ridge coefficients, below we compare the ridge coefficients with the unregularized estimates of the coefficients
#the unregularized estimates correspond to lambda equaling 0
b_ridge_0 = solve_ridge(X, y, lambda_val = 0)
plt.figure(figsize = (10, 6))
plt.plot(b_ridge_0[1:], color = 'lightgray')
plt.plot(b_ridge[1:])
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next let us use LASSO regularization.

```python
b_lasso = solve_lasso(X, y, lambda_val = 2000)
lasso_fitted = np.dot(X, b_lasso)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(lasso_fitted, color = 'red', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These fitted values look similar to the fitted values for the model with three sinusoidal components. This is unsurprising as the LASSO zeroes out many of the components so that the fitted model will be a sum of a small (but probably more than 3) sinusoidal components. This model might be useful for prediction. But data simulated from it (with $\sigma$ estimated as below) will still be wiggly without clearly defined peaks.

```python
sig_lasso = np.sqrt((np.sum((y - lasso_fitted) ** 2))/n)
print(sig_lasso)
```

```
33.54702098714371
```

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(6):
    errorsamples = rng.normal(loc = 0, scale = sig_lasso, size = n)
    sim_data = lasso_fitted + errorsamples
    axes[i].plot(sim_data)
axes[6].plot(y)
for i, idx in enumerate(range(7, 9)):
    errorsamples = rng.normal(loc = 0, scale = sig_lasso, size = n)
    sim_data = lasso_fitted + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#To illustrate the sparsity nature of LASSO coefficients, below we compare the LASSO coefficients with the unregularized estimates of the coefficients
#the unregularized estimates correspond to lambda equaling 0
b_lasso_0 = solve_lasso(X, y, lambda_val = 0)
plt.figure(figsize = (10, 6))
plt.plot(b_lasso_0[1:], color = 'lightgray')
plt.plot(b_lasso[1:])
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear from the above plot that most of the small unregularized coefficients are set to exactly zero by LASSO.

---

[← Sunspots Dataset](02-sunspots-dataset.md) · [Up: contents](index.md) · [The Spectrum Model →](04-the-spectrum-model.md)
