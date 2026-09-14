---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`public/labs/Lab2_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

# Lab 2 - Stat 153/248

This lab will go into concepts from Lectures 3 and 4 (covering measures of dependence). This includes:

1. Calculating mean functions
2. Calculating autocovariance for white noise, moving average, and random walk data
3. Calculating autocorrelation
4. Calculating cross-covariance
5. Calculating cross-correlation

For this lab, you will fill in the aspects of the code marked `...` or with the comment `# FILL IN`

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import acf, acovf, ccf
from statsmodels.graphics.tsaplots import plot_acf, plot_ccf
#!pip install astsa
import astsa # You should have pip installed this for Lab 1.. if not, uncomment line above

# Set the random seed, this is so you will generate the same answers
# each time (for example, when generating white noise)
np.random.seed(42)
```

```python
# Let's use the `moving_average`, `white_noise`, and `random_walk_drift` functions from Lab 1
# Here we also extend the white_noise function so it returns a matrix
# with `nt` time points and `nobs` observations.
def white_noise(nt, nobs=1, var=1):
    '''
    Generate a time series with uncorrelated random variables, `w_t`,
    with mean 0 and finite variance `var`.
    If var=1 this is the standard normal distribution.
    Inputs:
        nt [int] : number of time points
        nobs [int] : number of white noise time series to generate
        var [float] : variance
    Output:
        w [np.array] = array of length nt
    '''
    w = np.sqrt(var) * np.random.randn(nt,nobs)
    return w


def moving_average(w, n=3):
    '''
    Create an acausal moving average of the time series `w`
    using an `n`-point moving average (default 3).
    '''
    w = np.asarray(w)
    if w.ndim != 2:
        w = np.atleast_2d(w).T
    nt, nobs = w.shape
    v = np.zeros((nt, nobs)) * np.nan
    half_win = n // 2
    for t in np.arange(half_win, nt - half_win):
        v[t,:] = np.mean(w[t-half_win : t+half_win+1,:], axis=0)
    return v


def random_walk_drift(nt, drift, x0=0):
    '''
    Create a random walk with drift for `nt` time points, `drift` drift, and
    with initial value `x0`.
    Inputs:
        nt (int) : number of time points
        drift (float) : constant drift
        x0 (float) : initial value
    '''
    x = np.zeros((nt,))
    x[0] = x0
    for n in np.arange(1,nt):
        x[n] = x[n-1] + white_noise(1).item() + drift
    return x
```

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

---

[Up: contents](index.md) · [Autocorrelation of moving average →](02-autocorrelation-of-moving-average.md)
