---
title: Moving average and filtering
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Moving average and filtering

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
# Plot the white noise and the moving average of the white noise on top
plt.plot(w)
plt.plot(moving_average(w))
```

```
[<matplotlib.lines.Line2D at 0x12ebb39a0>]
```

*(1 figure omitted — see the original notebook.)*

```python
# How does this change on the number of points included in the average? What happens? Try some
# other values of n
plt.plot(w)
plt.plot(moving_average(w))
plt.plot(moving_average(w, n=10)) # FILL IN, try several...
```

```
[<matplotlib.lines.Line2D at 0x12ec48b50>]
```

*(1 figure omitted — see the original notebook.)*

Below let's create the moving average function assuming negative lags (a __causal__ filter) $v_t = \frac{1}{3} (w_{t-2}+w_{t-1}+w_t)$

```python
def moving_average_causal(w, n=3):
    '''
    Create a causal moving average of the time series `w` using an `n`-point moving average (default 3)
    Inputs:
        w (np.array) : original time series
        n (int) : number of points incorporated in the moving average
    Output:
        v (np.array) : smoothed time series
    '''
    v = np.zeros((len(w),)) * np.nan
    for t in np.arange(n, len(w) - n):
        v[t] = np.mean(w[t-n : t])
    return v
```

Now let's look at how this causal filtering compares to the original centered n-point moving average. What do you notice?

```python
n = 3
plt.figure(figsize=(12,3))
#plt.plot(w, label='original')
plt.plot(moving_average(w, n), label='centered n-point MA')
plt.plot(moving_average_causal(w, n), label='causal n-point MA')
plt.legend()
```

```
<matplotlib.legend.Legend at 0x12ec9c820>
```

*(1 figure omitted — see the original notebook.)*

---

[← Data from Time Series Analysis and Its Applications](02-data-from-time-series-analysis-and-its-applications.md) · [Up: contents](index.md) · [Autoregression →](04-autoregression.md)
