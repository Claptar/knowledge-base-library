---
title: Estimating the original parameters of the sinusoid
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab5_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Estimating the original parameters of the sinusoid

Recall we can get back the original parameters through their relationship to the $\beta$ values:

$$R=\sqrt{\beta_1^2+ \beta_2^2}, \quad \phi = \arctan\left(-\frac{\beta_2}{\beta_1}\right)$$

Let's see what we get.

```python
B0_hat = betas[0]
R_hat = np.sqrt(betas[1]**2 + betas[2]**2)
phi_hat = np.arctan(-betas[2]/betas[1])

print(f'B0={B0}\t B0_hat={B0_hat}')
print(f'R={R}\t R_hat={R_hat}')
print(f'phi={phi}\t phi_hat={phi_hat}')
print(f'f={f}\t f_hat={best_f}')
```

```
B0=2	 B0_hat=2.029404412553876
R=2.5	 R_hat=0.4737475535789633
phi=0	 phi_hat=1.0137021097636343
f=3.2	 f_hat=2.525252525252525
```

How does this look? It's okay, but not quite right. Try redoing the grid search again below in a way that you think will make this more accurate.

```python
nf = 10000  # Test this number of frequencies
f_grid = np.linspace(0,fs/2,nf)
# or
nf = 1000
f_grid = np.linspace(2,4,nf)

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

```
<matplotlib.legend.Legend at 0x300079ea0>
```

*(2 figures omitted — see the original notebook.)*

### Compare $y$ and $\hat{y}$ directly

We can also just plot our actual data versus the estimate. If our linear model is perfect, we should see the unity line $\hat{y}=y$

```python
plt.figure()
plt.plot(y, y_hat,'.')
plt.plot(y,y,'-')
plt.xlabel('y')
plt.ylabel('yhat');
```

*(1 figure omitted — see the original notebook.)*

Let's get back the original parameters again with this (hopefully) improved regression:

$$R=\sqrt{\beta_1^2+ \beta_2^2}, \quad \phi = \arctan\left(-\frac{\beta_2}{\beta_1}\right)$$

Let's see what we get.

```python
B0_hat = betas[0]
R_hat = np.sqrt(betas[1]**2 + betas[2]**2)
phi_hat = np.arctan(-betas[2]/betas[1])

print(f'B0={B0}\t B0_hat={B0_hat}')
print(f'R={R}\t R_hat={R_hat}')
print(f'phi={phi}\t phi_hat={phi_hat}')
print(f'f={f}\t f_hat={best_f}')
```

```
B0=2	 B0_hat=1.9930655070550236
R=2.5	 R_hat=2.4680140137480113
phi=0	 phi_hat=-0.006247204538511174
f=3.2	 f_hat=3.201201201201201
```

## How does this look now?

---

[← Finding the frequency, $f$](02-finding-the-frequency.md) · [Up: contents](index.md) · [What about new data? →](04-what-about-new-data.md)
