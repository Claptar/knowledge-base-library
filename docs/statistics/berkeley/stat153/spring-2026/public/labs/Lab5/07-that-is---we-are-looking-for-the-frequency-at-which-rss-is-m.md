---
title: That is - we are looking for the frequency at which RSS is minimized.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# That is - we are looking for the frequency at which RSS is minimized.

**Source:** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

[← Lab5 Part 06 —](06-lab5-part-06.md) · [Up: contents](index.md) · [Estimating the original parameters of the sinusoid →](08-estimating-the-original-parameters-of-the-sinusoid.md)
