---
title: 'Source: FRED series GASREGW'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Source: FRED series GASREGW

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

gas = pd.read_csv('GASREGW.csv', parse_dates=['observation_date'], index_col='observation_date').dropna()
y_gas = gas['GASREGW'].values
log_change = np.diff(np.log(y_gas))

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(gas.index, y_gas, linewidth=0.8)
ax.set(xlabel='Date', ylabel='$ per gallon',
       title='US Regular All Formulations Gas Price')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(gas.index[1:], log_change, linewidth=0.8)
ax.set(xlabel='Date', ylabel='Difference of log $',
       title='Gas Price Change')
plt.tight_layout()
plt.show()

print(f"Series length: {len(y_gas)} observations")
print(f"Mean: {np.mean(y_gas):.2f}, Std: {np.std(y_gas):.2f}")
```

```
Series length: 1853 observations
Mean: 2.26, Std: 0.95
```

*(2 figures omitted — see the original notebook.)*

### Predict (1 min)

1. Based on the plot, do you expect the ACF to decay faster or slower than sunspots?
2. Will the PACF cut off as cleanly as it did for sunspots?

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(y_gas, lags=40, ax=axes[0], title='ACF - Gas Prices')
plot_pacf(y_gas, lags=40, ax=axes[1], title='PACF - Gas Prices', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))
plot_acf(log_change, lags=40, ax=axes[0], title='ACF - Change in Gas Prices')
plot_pacf(log_change, lags=40, ax=axes[1], title='PACF - Change in Gas Prices', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Results

The ACF decays very slowly for the original series — this series has high persistence (almost unit-root behavior). The PACF shows a strong spike at lag 1, smaller spike at lag 2, and then starts to cut off. When we difference the signal, the ACF falls off more quickly.

Let's try fitting AR models of increasing order and see what the residuals look like.

```python

---

[← US Regular All Formulations Gas Price](08-us-regular-all-formulations-gas-price.md) · [Up: contents](index.md) · [Fit AR(1), AR(2), AR(4) and compare →](10-fit-ar-1-ar-2-ar-4-and-compare.md)
