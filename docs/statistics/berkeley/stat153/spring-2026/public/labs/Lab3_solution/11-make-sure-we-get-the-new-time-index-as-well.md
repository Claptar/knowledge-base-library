---
title: Make sure we get the new time index as well
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Make sure we get the new time index as well

**Source:** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

half_win = smoothing_win // 2
new_t = [chicken_data.index[a] for a in np.arange(half_win, len(chicken_data.index) - half_win)]

plt.figure()
plt.plot(new_t,residuals_smooth)
plt.axhline(0, color='k', linewidth=0.5) # Horizontal line at 0
plt.xlabel('Date')
plt.ylabel('Residual')

plt.figure(figsize=(10, 5))
plot_acf(residuals_smooth, lags=100, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show();
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

As it turns out, there are still pretty strong autocorrelations in these data, even when we apply the moving average, so probably we will want to do some differencing or other transformations first.

---

[← Now let's fit a regression to this](10-now-let-s-fit-a-regression-to-this.md) · [Up: contents](index.md) · [Lecture 6 review →](12-lecture-6-review.md)
