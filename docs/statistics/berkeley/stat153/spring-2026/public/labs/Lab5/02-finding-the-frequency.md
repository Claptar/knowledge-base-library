---
title: Finding the frequency, $f$
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Finding the frequency, $f$

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
# FIND THE BEST F-HAT based on the RSS (don't hard code it, write an expression that will derive it for you)
# That is - we are looking for the frequency at which RSS is minimized.
best_f = # FILL IN
plt.axvline(best_f, color='r', linewidth=0.5, linestyle='--')
plt.text(best_f + 1, np.min(RSS), f'f={best_f:.3f}')
plt.xlabel('Frequency')
plt.ylabel('RSS')
```

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
cos_col = # FILL IN
sin_col = # FILL IN
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

---

← Stat153/248 - Lab 5 · [Up: contents](index.md) · [Estimating the original parameters of the sinusoid →](03-estimating-the-original-parameters-of-the-sinusoid.md)
