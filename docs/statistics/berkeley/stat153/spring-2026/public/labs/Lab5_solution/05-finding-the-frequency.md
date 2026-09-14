---
title: Finding the frequency, $f$
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Finding the frequency, $f$

**Source:** [`public/labs/Lab5_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Let's assume we have received these data and we have no idea what the true $f$ is. We can find it with a grid search across a number of potential $f_hat$ values, then do OLS using the relationship that we discussed, which is that we can rewrite $y$ as:

$y = \beta_0 + \beta_1 \cos (2\pi \hat{f}t) + \beta_2 \sin (2\pi \hat{f}t ) + \epsilon_t$

Where $\beta_1=R\cos\phi$ and $\beta_2=-R\sin\phi$. We will still solve for these $\beta$ values with OLS, since we also don't know what $\phi$ or $R$ are.

We will start with a linearly spaced vector of values for the potential $f$. Looking at the graph above, we can count the peaks and narrow this down to probably ~3 peaks, so we don't actually have to test everything, though if we want to be exhaustive, we would test frequencies from $[0, \text{fs}/2]$.

We then fit the regression model using our $X$ matrix, defined as:

$$
  X_f = \begin{pmatrix}
    1 & \cos(2\pi \hat{f} t_0) & \sin(2\pi \hat{f} t_0) \\
    \vdots & \vdots & \vdots \\
    1 & \cos(2\pi \hat{f} t_n) & \sin(2\pi \hat{f} t_n) \\
    \end{pmatrix}
$$

and repeat this for every value of $\hat{f}$ and plot the residual sum of squares (RSS). We are looking for the minimum value of this plot. The number of values of $f$ we test in the grid allows us to be more accurate, so try varying the number of values `nf`.

```python
nf = 100  # Test this number of frequencies
f_grid = np.linspace(0,fs/2,nf)

RSS = np.zeros(len(f_grid))
for idx, f_hat in enumerate(f_grid):
    cos_col = np.cos(2 * np.pi * f_hat * t )
    sin_col = np.sin(2 * np.pi * f_hat * t )

    # create our X matrix
    X = np.column_stack([np.ones(len(t)), cos_col, sin_col])

    model = sm.OLS(y, X).fit()
    betas = model.params
    RSS[idx] = np.sum(model.resid **2)

plt.plot(f_grid, RSS,'-')
best_f = f_grid[RSS.argmin()] # Find the best f_hat
plt.axvline(best_f, color='r', linewidth=0.5, linestyle='--')
plt.text(best_f + 1, np.min(RSS), f'f={best_f:.3f}')
plt.xlabel('Frequency')
plt.ylabel('RSS')
```

```
Text(0, 0.5, 'RSS')
```

*(1 figure omitted — see the original notebook.)*

## Use our best f to calculate the other coefficients

From this we can choose the best $f$ and try fitting OLS again and looking at the parameters and performance of the model.

Again:
$$
  X_f = \begin{pmatrix}
    1 & \cos(2\pi \hat{f} t_0) & \sin(2\pi \hat{f} t_0) \\
    \vdots & \vdots & \vdots \\
    1 & \cos(2\pi \hat{f} t_n) & \sin(2\pi \hat{f} t_n) \\
    \end{pmatrix}
$$

but with only the best $\hat{f}$

```python
cos_col = np.cos(2 * np.pi * best_f * t )
sin_col = np.sin(2 * np.pi * best_f * t )
X = np.column_stack([np.ones(len(t)), cos_col, sin_col])

model = sm.OLS(y, X).fit()
betas = model.params
y_hat = model.fittedvalues

plt.figure()
plt.plot(y, label='y')
plt.plot(y_hat, label='yhat')
plt.legend()

plt.figure()
plt.plot(y, y_hat,'.')
plt.xlabel('y')
plt.ylabel('yhat')
```

```
Text(0, 0.5, 'yhat')
```

*(2 figures omitted — see the original notebook.)*

---

[← Let's plot it and our x and y origin lines](04-let-s-plot-it-and-our-x-and-y-origin-lines.md) · [Up: contents](index.md) · [Estimating the original parameters of the sinusoid →](06-estimating-the-original-parameters-of-the-sinusoid.md)
