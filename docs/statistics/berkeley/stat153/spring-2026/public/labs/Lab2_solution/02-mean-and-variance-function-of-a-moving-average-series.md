---
title: Mean and Variance Function of a Moving Average Series
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab2_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Mean and Variance Function of a Moving Average Series

We showed in class that applying a moving average to our time series does not change the mean function, but that it does reduce the variance. Here, let's define a matrix of observations of white noise time series `w_matrix` and apply the `moving_average` function to it to get `w_matrix_ma`.

Unlike Lab 1, we're going to initialize both of these variables as matrices so we don't have to loop through the individual observations. This will make our code much more efficient.

```python
nt = 150
nobs = 1000
moving_average_win = 3

# Initialize white noise matrix `nt` time points and `nobs` observations
w_matrix = white_noise(nt, nobs)

# Initialize moving average version of w
w_matrix_ma = moving_average(w_matrix, n=moving_average_win)
```

```python
# Now let's plot the mean functions of the white noise time
# series, the moving average noise series, and their variance
# functions.

# Try also changing the `moving_average_win` above
# to see how it affects the mean and variance
plt.figure()
plt.subplot(1,2,1)
plt.plot(w_matrix.mean(1))
plt.plot(w_matrix_ma.mean(1))
plt.gca().set_ylim([-1,1])
plt.xlabel('Time')
plt.ylabel('Mean')

plt.subplot(1,2,2)
plt.plot(w_matrix.var(1))
plt.plot(w_matrix_ma.var(1))
plt.xlabel('Time')
plt.ylabel('Variance');

plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

As we showed in class, theoretically the mean function should not change when applying a moving average to a white noise time series, and should just continue to be 0.

$\mu_{vt} = \mathbb{E}(v_t) = \frac{1}{3}[\mathbb{E}(w_{t-1})+\mathbb{E}(w_{t})+\mathbb{E}(w_{t+1})] = 0$

So why, in practice, did we get means that were slightly different? (Hint: try changing `nobs`).

On the other hand, the variance does indeed change when we smooth the data - notice how it changes as you increase the number of points in the moving average (change the value for `moving_average_win`). The value should hover around $\frac{1}{n}$.

---

← Lab 2 - Stat 153/248 · [Up: contents](index.md) · [Autocovariance and Autocorrelation →](03-autocovariance-and-autocorrelation.md)
