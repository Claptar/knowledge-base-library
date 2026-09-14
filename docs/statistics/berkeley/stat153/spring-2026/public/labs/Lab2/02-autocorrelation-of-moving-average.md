---
title: Autocorrelation of moving average
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Autocorrelation of moving average

**Source:** [`public/labs/Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now let's look at the autocorrelation function of a moving average with different window lengths `n`. Note that we have to drop the first `n-1` samples, which are not defined (stored as NaNs). You do *not* want to set these NaN values to 0 as this can induce artificial correlation structure in your data.

Is the moving average (weakly) stationary? If it is, you should notice that the autocorrelation and autocovariance functions decay as a function of lag.

Try changing the window length `win` and the number of time points `nt`. How do these affect what you observe?

```python
win = # FILL IN
nt = # FILL IN
w = white_noise(nt, var=#FILL IN)
ma_data = moving_average(w, n=win)

plot_acf(ma_data[~np.isnan(ma_data)], lags=100);
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Autocorrelation of random walk with drift →](03-autocorrelation-of-random-walk-with-drift.md)
