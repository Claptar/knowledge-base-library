---
title: Moving average and filtering
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Moving average and filtering

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

In the examples given by Shumway and Stoffer in Chapter 1, the signals vary in terms of their smoothness. Sometimes this is due to underlying characteristics of the data, but sometimes this is due to sampling (in fact, sometimes undersampling a time series, such as a sound, will lead to unwanted "spikiness" in the data and distortions called "aliasing".

So what if we want to smooth our data? One way is to replace the white noise series $w_t$ by a moving average, e.g.:

$v_t = \frac{1}{3} (w_{t-1}+w_t+w_{t+1})$

This uses both the current data and the past and future neighbors, which can also be called lags `[-1, 0, 1]`. This is sometimes called an "acausal" moving average filter because it requires data from both the past and the future. On the other hand, a "causal" moving average filter would consider only nearest points in the past (negative or 0 lags only), for example:

$v_t = \frac{1}{3} (w_{t-2}+w_{t-1}+w_t)$

Let's compare what these do to our time series, starting with the white noise we made above.

```python
def moving_average(w, n=3):
    '''
    Create an acausal moving average of the time series `w` using an `n`-point moving average (default 3)
    '''
    v = np.zeros((len(w),)) * np.nan
    half_win = n // 2
    for t in np.arange(half_win, len(w) - half_win):
        v[t] = np.mean(w[t-half_win : t+half_win+1])
    return v
```

```python

---

[← Calculate the return](07-calculate-the-return.md) · [Up: contents](index.md) · [Plot the white noise and the moving average of the white noise on top →](09-plot-the-white-noise-and-the-moving-average-of-the-white-noi.md)
