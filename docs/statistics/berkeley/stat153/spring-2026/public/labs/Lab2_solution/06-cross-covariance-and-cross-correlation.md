---
title: Cross-covariance and cross-correlation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab2_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Cross-covariance and cross-correlation

Many times, we don't just want to describe the relationship between time points in the same series, we want to describe the relationship between multiple time series. For example, how does the time course of reported cases of a disease relate to time course of reported deaths? How do the numbers of lynx and hare pelts relate to each other in our prior example?

In this case, we can use cross-correlation (or look at cross-covariance) of the two time series.

```python
#plot_ccf(lynx_data['Value'], hare_data['Value'], lags=len(lynx_data['Value'])-1, negative_lags=True)

x = lynx_data['Value'].values
y = hare_data['Value'].values

max_lag = 30   # Let's choose some value here explicitly

# Positive lags: lynx data leads hare data
ccf_xy = ccf(x, y, adjusted=False)[:max_lag+1]

# Negative lags: hare data leads lynx data
ccf_yx = ccf(y, x, adjusted=False)[:max_lag+1]

# Build symmetric lag axis
lags = np.arange(-max_lag, max_lag+1)

# Combine (exclude duplicate lag 0)
ccf_full = np.r_[ccf_yx[1:][::-1], ccf_xy]

plt.stem(lags, ccf_full)
plt.axvline(0, color='r')
plt.xlabel('Lag')
plt.ylabel('CCF')
plt.title('positive: lynx leads hare, negative: hare leads lynx');
plt.grid()
```

*(1 figure omitted — see the original notebook.)*

## Interpreting cross correlation

One point of caution is that with these real data examples presented here, they are not usually weakly stationary, so interpreting the cross-correlation analysis can be problematic. In the future, we will use other tools such as prewhitening, and detrending to help before we run the cross-correlation analysis. See Example 1.29 and 1.30 in your book (SS pages 34-35) to read more about this.

---

[← A Practical use of autocorrelation](05-a-practical-use-of-autocorrelation.md) · [Up: contents](index.md)
