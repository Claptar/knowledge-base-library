---
title: Moving average and filtering
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

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
        v[t] = ... # FILL IN
    return v
```

```python
# Plot the white noise and the moving average of the white noise on top
plt.plot(w)
plt.plot(moving_average(w))
```

```python
# How does this change on the number of points included in the average? What happens? Try some
# other values of n
plt.plot(w)
plt.plot(moving_average(w))
plt.plot(moving_average(w, n=...)) # FILL IN, try several...
```

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
    ... # FILL IN
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

## Autoregression

The smoothed moving average data we generated here still doesn't have a lot of the quasiperiodic characteristics of time series like the speech series and fMRI series examples from lecture (Fig. 1.3 and 1.7 in SS). Instead, we can generate time series with oscillatory behavior in a few ways, one of which is to use the concept of autoregression, where we predict the current value $x_t$ of a time series as a function of past values, e.g.

$x_t = 1.5x_{t-1} + 0.75x_{t-2} + w_t $

We will start with some initial values for the first two values of $x$ so that $x_0=x_1=0$

```python
def generate_autoreg(w, nt=250):
    '''
    Generate some autocorrelated data starting with white noise
    time series `w`, for `nt` time points.
    Inputs:
        w [np.array] : white noise time series
        nt [int] : number of time points to generate
    Output:
        x [np.array] : autocorrelated time series
    '''
    x = np.zeros((nt,))

    x[0] = w[0]
    x[1] = w[1]
    for t in np.arange(2,nt):
        x[t] = ... # FILL IN
    return x
```

```python
x = generate_autoreg(w)
plt.plot(x)
```

## Data as signal plus white noise

Many datasets can be modeled as $v_t = s_t + w_t$, where $s_t$ is some signal of interest and $w_t$ is white noise. We will talk later about how we might find $s_t$ or other components of the signal. But for now, let's look at a few examples generating these types of data.

---

[← Data from Time Series Analysis and Its Applications](01-data-from-time-series-analysis-and-its-applications.md) · [Up: contents](index.md) · Random walk →
