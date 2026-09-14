---
title: Plot sample ACF/PACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot sample ACF/PACF

**Source:** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(dt, lags=L, ax=ax1, title='Sample ACF')
plot_pacf(dt, lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

Second Example is $ARMA(0, 1) \times (1, 0)_{12}$ (which can also be written as $MA(1)) \times AR(1)_{12}$).

```python
th = 0.8
ma_coeffs = np.array([1, th])
ph = 0.8
ar_coeffs = np.zeros(13)
ar_coeffs[0] = 1
ar_coeffs[12] = -ph
#ar_coeffs = [1, -ph]
#ar_coeffs = [1, 0, 0, 0, -ph]
#th2 = 0.8
#ma_coeffs = [1, th, th2]
L = 50
corrs = arma_acf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
par_corrs = arma_pacf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
ax1.stem(range(L), corrs)
ax1.set(title = 'Theoretical ACF', xlabel = 'Lag h', ylabel = 'Autocorrelation')
ax1.axhline(0, lw = 0.5)
#ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

ax2.stem(range(L), par_corrs)
ax2.set(title = 'Theoretical PACF', xlabel = 'Lag h', ylabel = 'Partial Autocorrelation')
ax2.axhline(0, lw = 0.5)
#ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the PACF at the seasonal lags (12, 24, ...), there is only one spike (at lag 12) which suggests that the seasonal part is AR(1). Looking at the initial few lags (1, 2, 3, ...), the ACF reveals an MA(1) structure. The overall model can be guessed as $MA(1) \times AR(1)_{12}$.

```python

---

[← Plot simulated series](09-plot-simulated-series.md) · [Up: contents](index.md) · [Simulate data →](11-simulate-data.md)
