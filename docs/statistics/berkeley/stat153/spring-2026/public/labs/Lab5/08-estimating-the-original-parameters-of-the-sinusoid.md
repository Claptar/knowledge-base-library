---
title: Estimating the original parameters of the sinusoid
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimating the original parameters of the sinusoid

**Source:** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Recall we can get back the original parameters through their relationship to the $\beta$ values:

$$R=\sqrt{\beta_1^2+ \beta_2^2}, \quad \phi = \arctan\left(-\frac{\beta_2}{\beta_1}\right)$$

Let's see what we get.

```python
B0_hat = # FILL IN
R_hat = # FILL IN
phi_hat = # FILL IN

print(f'B0={B0}\t B0_hat={B0_hat}')
print(f'R={R}\t R_hat={R_hat}')
print(f'phi={phi}\t phi_hat={phi_hat}')
print(f'f={f}\t f_hat={best_f}')
```

How does this look? It's okay, but not quite right. Try redoing the grid search again below in a way that you think will make this more accurate.

```python
nf = # FILL IN
f_grid = # FILL IN

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
```

## Compare $y$ and $\hat{y}$ directly

We can also just plot our actual data versus the estimate. If our linear model is perfect, we should see the unity line $\hat{y}=y$

```python
plt.figure()
plt.plot(y, y_hat,'.')
plt.plot(y,y,'-')
plt.xlabel('y')
plt.ylabel('yhat');
```

---

[← That is - we are looking for the frequency at which RSS is minimized.](07-that-is---we-are-looking-for-the-frequency-at-which-rss-is-m.md) · [Up: contents](index.md) · [Estimating the original parameters of the sinusoid →](09-estimating-the-original-parameters-of-the-sinusoid.md)
