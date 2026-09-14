---
title: 'Source: FRED series GDPC1'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Source: FRED series GDPC1

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

gdp = pd.read_csv('GDPC1.csv', parse_dates=['observation_date'], index_col='observation_date').dropna()
y_gdp = np.log(gdp['GDPC1'].values)
log_change = np.diff(y_gdp)

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(gdp.index, y_gdp, linewidth=0.8)
ax.set(xlabel='Date', ylabel='Billions of Chained 2017 $',
       title='US GDP')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(gdp.index[1:], log_change, linewidth=0.8)
ax.set(xlabel='Date', ylabel='Percent change',
       title='Rate of change')
plt.tight_layout()
plt.show()

print(f"Series length: {len(y_gdp)} observations")
print(f"Mean: {np.mean(y_gdp):.2f}, Std: {np.std(y_gdp):.2f}")
```

```
Series length: 316 observations
Mean: 9.02, Std: 0.70
```

*(2 figures omitted — see the original notebook.)*

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(y_gdp, lags=40, ax=axes[0], title='ACF - GDP')
plot_pacf(y_gdp, lags=40, ax=axes[1], title='PACF - GDP', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))
plot_acf(log_change, lags=40, ax=axes[0], title='ACF - Percent change GDP')
plot_pacf(log_change, lags=40, ax=axes[1], title='PACF - Percent change GDP', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← US GDP (seasonally adjusted)](03-us-gdp-seasonally-adjusted.md) · [Up: contents](index.md) · [Fitting the model →](05-fitting-the-model.md)
