---
title: Multiplicative Seasonal ARMA models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Multiplicative Seasonal ARMA models

Next we look at the ACF and PACF of Multiplicative Seasonal ARMA models. These have aspects of both the usual ARMA models as well as the Seasonal ARMA models. It is a challenge to look at the ACF and PACF functions and guess the form of the model based on those plots. One can try the following heuristic strategy. First look at the ACF and PACF only at the seasonal lags $h = 0, s, 2s, 3s, \dots$. From here, try to guess the order of the seasonal part of the ARMA model. For example, if ACF(hs) seems to be negligible for $h > Q$, then the seasonal part could be MA(Q). If PACF(hs) seems negligible for $h > P$, then seasonal part could be AR(P). Next look at only the initial few non-seasonal lags ($h = 0, 1, 2, 3, \dots, s-1$). From here, attempt to guess the orders of the regular part of the model.

First example is $ARMA(0, 0, 1) X (0, 0, 1)_{12}$ (which can be also written as $MA(1) \times MA(1)_{12}$).

```python
th = -0.8
Th = 0.7
ma_coeffs = np.zeros(14)
ma_coeffs[0] = 1
ma_coeffs[1] = th
ma_coeffs[12] = Th
ma_coeffs[13] = th*Th
#ma_coeffs = [1, 0, 0, 0, th]
#ma_coeffs = [1]
#ma_coeffs = [1, th]
#ph = 0.8
ar_coeffs = [1]
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

From the ACF at seasonal lags, it is clear that the seasonal part is $MA(1)_{12}$. From the ACF at the initial few lags, it is clear that the regular part is also $MA(1)$, leading to the overall model $MA(1) \times MA(1)_{12}$.

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

Example Three is $MA(2) \times AR(1)_{12}$.

```python
th1 = 0.8
th2 = 0.6
ma_coeffs = np.array([1, th1, th2])
ph = 0.8
ar_coeffs = np.zeros(13)
ar_coeffs[0] = 1
ar_coeffs[12] = -ph
#ar_coeffs = [1, -ph]
#ar_coeffs = [1, 0, 0, 0, -ph]
#th2 = 0.8
#ma_coeffs = [1, th, th2]
L = 60
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

Looking at the seasonal lags (12, 24, 36, ...) in the PACF, we can clearly see only one spike suggesting $AR(1)_{12}$. Looking at lags 1, 2, 3, ... in the ACF, we see two spikes suggesting $MA(2)$. The overall model can be guessed as $MA(2) \times AR(1)_{12}$.

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

Example Four is $AR(1) \times AR(1)_{12}$.

```python
ph = -0.8
Ph = 0.7
ar_coeffs = np.zeros(14)
ar_coeffs[0] = 1
ar_coeffs[1] = -ph
ar_coeffs[12] = -Ph
ar_coeffs[13] = ph*Ph
ma_coeffs = [1]
L = 60
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
ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

At the seasonal lags 12, 24, 36, ..., the PACF has one spike suggesting $AR(1)_{12}$. At lags 1, 2, 3, ..., there is also one spike in the PACF suggesting $AR(1)$. The overall model is therefore guessed as $AR(1) \times AR(1)_{12}$.

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

In all the examples, it is much harder (due to noise) to guess the models from the sample ACF and PACFs (from data generated according to the model) compared to the  theoretical ACF and PACF of the model.

---

[← Seasonal ARMA models](03-seasonal-arma-models.md) · [Up: contents](index.md) · [Back to co2 dataset →](05-back-to-co2-dataset.md)
