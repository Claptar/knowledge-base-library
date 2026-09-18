---
title: Autocovariance and Autocorrelation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab2_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Autocovariance and Autocorrelation

In our lectures we also talked about _autocovariance_, which is the _linear_ dependence between two points of the same series observed at different times $s$ and $t$. We can define a function for autocovariance as:

$\gamma_x(s,t) =\text{cov}(x_s,x_t) = \text{E}[(x_s-\mu_s)(x_t-\mu_t)]$

Where $\mu_s$ and $\mu_t$ are the expected values of $x_s$ and $x_t$.

_Autocorrelation_ is the normalized form of autocovariance:

$\gamma_x(s,t) =\frac{\text{cov}(x_s,x_t)}{\text{cov}(x_s,x_s)\text{cov}(x_t,x_t)}$

Most commonly we will use built-in functions, for example from the `statsmodels` package, we have the `acf` (autocorrelation) and `acovf` (autocovariance) functions. `acf` also has a built-in plotting tool `plot_acf`, which can plot confidence intervals.

```python
# Autocovariance and autocorrelation of white noise
nt = 10000
w = white_noise(nt)

# Now let's try using the statsmodels package
acf_values = acf(w, nlags=100)
acovf_values = acovf(w, nlag=100)

# Use statsmodels plot_acf, which also calculates the acf values:
plot_acf(w, lags=100, alpha=0.05)
plt.title('Autocorrelation Function (ACF) Plot')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()

# The acovf doesn't have a separate plotting function, so we
# will just use a stem plot.
plt.stem(acovf_values)
plt.title('Autocovariance Function Plot')
plt.xlabel('Lags')
plt.ylabel('Autocovariance')
plt.show();
```

*(2 figures omitted — see the original notebook.)*

Why are the autocovariance and autocorrelation the same here? What if we multiply our white noise series `w` by a constant? What happens to the values at `lag=0`? Does this white noise time series satisfy the contraints for weak and strict stationarity?

```python
# Make a new white noise
c = 10
v = white_noise(nt, var=1)*c # New scaled white noise time series

acf_values = acf(v, nlags=100)
acovf_values = acovf(v, nlag=100)

plot_acf(v, lags=100, alpha=0.05)
plt.title('Autocorrelation Function (ACF) Plot')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()

# The acovf doesn't have a separate plotting function...
plt.stem(acovf_values)
plt.title('Autocovariance Function Plot')
plt.xlabel('Lags')
plt.ylabel('Autocovariance')
plt.show();
```

*(2 figures omitted — see the original notebook.)*

## Autocorrelation of moving average

Now let's look at the autocorrelation function of a moving average with different window lengths `n`. Note that we have to drop the first `n-1` samples, which are not defined (stored as NaNs). You do *not* want to set these NaN values to 0 as this can induce artificial correlation structure in your data.

Is the moving average (weakly) stationary? If it is, you should notice that the autocorrelation and autocovariance functions decay as a function of lag.

Try changing the window length `win` and the number of time points `nt`. How do these affect what you observe?

```python
win = 6
nt = 1000
w = white_noise(nt, var=2)
ma_data = moving_average(w, n=win)

plot_acf(ma_data[~np.isnan(ma_data)], lags=100);
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
```

```
Text(0, 0.5, 'Autocorrelation')
```

*(1 figure omitted — see the original notebook.)*

## Autocorrelation of random walk with drift

Now try plotting the autocorrelation for the random walk with drift, generating several examples of the random walk time series. What do you notice? Is it stationary? What changes if you change the scale of the drift (positive, negative, zero, large, small)?

```python
nt = 100
rwd = random_walk_drift(nt, drift=0.01)
plot_acf(rwd, lags=len(rwd)-1);
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
```

```
Text(0, 0.5, 'Autocorrelation')
```

*(1 figure omitted — see the original notebook.)*

---

[← Mean and Variance Function of a Moving Average Series](02-mean-and-variance-function-of-a-moving-average-series.md) · [Up: contents](index.md) · [Real data →](04-real-data.md)
