---
title: Seasonal ARMA models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Seasonal ARMA models

Seasonal ARMA models are given by $\phi(B^s) (y_t - \mu) = \theta(B^s) \epsilon_t$. These are special cases of regular ARMA models with lots of zeros in the AR and MA coefficients. For example, the seasonal MA(1) model with period $s = 4$ is $y_t = \mu + \epsilon_t + \theta \epsilon_{t-4}$ which is also a regular MA(4) model with coefficients $\theta_1 = \theta_2 = \theta_3 = 0$ and $\theta_4 = \theta$. The following code is the same as that used previously to compute the ACF and PACF of ARMA processes. By inputting a bunch of zeros in ma_coeffs and ar_coeffs, we can obtain the ACF and PACF of seasonal ARMA models.

```python
#AR(1)
th = 0.8
ma_coeffs = [1, 0, 0, 0, th] #this corresponds to seasonal MA with period = 4
#ma_coeffs = [1]
#ma_coeffs = [1, th]
ph = 0.8
#ar_coeffs = [1]
#ar_coeffs = [1, -ph]
ar_coeffs = [1, 0, 0, 0, -ph] #this corresponds to seasonal AR with period = 4
#th2 = 0.8
#ma_coeffs = [1, th, th2]
L = 20
corrs = arma_acf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
par_corrs = arma_pacf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
ax1.stem(range(L), corrs)
ax1.set(title = 'Theoretical ACF', xlabel = 'Lag h', ylabel = 'Autocorrelation')
ax1.axhline(0, lw = 0.5)
ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

ax2.stem(range(L), par_corrs)
ax2.set(title = 'Theoretical PACF', xlabel = 'Lag h', ylabel = 'Partial Autocorrelation')
ax2.axhline(0, lw = 0.5)
ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The ACF and PACF of a seasonal ARMA model is non-zero only at the seasonal lags $h = 0, s, 2s, 3s, 4s, \dots$. At these seasonal lags, the ACF and PACF exactly equal those of the non-seasonal ARMA.

```python
# Simulate data
arma_process = ArmaProcess(ar_coeffs, ma_coeffs)
dt = arma_process.generate_sample(nsample=400)

# Plot simulated series
plt.figure(figsize=(10, 4))
plt.plot(dt, 'o-', markersize=4)
plt.title("Simulated Data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# Plot sample ACF/PACF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(dt, lags=L, ax=ax1, title='Sample ACF')
plot_pacf(dt, lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

---

[← co2 dataset (Motivation for Multiplicative Seasonal ARMA models)](02-co2-dataset-motivation-for-multiplicative-seasonal-arma-mode.md) · [Up: contents](index.md) · [Multiplicative Seasonal ARMA models →](04-multiplicative-seasonal-arma-models.md)
