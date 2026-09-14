---
title: White Noise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# White Noise

**Source:** [`public/labs/Lab1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

In Lecture 2, we talked about _white noise_, which is a special case of a time series generated from uncorrelated random variables, $w_t$ with mean 0 and finite variance $\sigma^2_w$. The name comes from the analogy with white light, indicating that all possible periodic oscillations are present with equal strength (we will see later how this looks in power spectral analysis).

Let's create function that returns `nt` samples of independent/iid Gaussian white noise, that is, where $w_t \sim \mbox{iid } \mathcal{N}(0,\sigma^2_w)$.

```python
def white_noise(nt, var=1):
    '''
    Generate a time series with uncorrelated random variables, `w_t`, with mean 0 and finite variance `var`.
    If var=1 this is the standard normal distribution.
    Inputs:
        nt [int] : number of time points
        var [float] : variance
    Output:
        w [np.array] = array of length nt
    '''
    w = ... # fill this in
    return w
```

Now let's plot some white noise data for 250 time points, as in Fig. 1.9 (SS)

```python
nt = 250
w = white_noise(nt)
plt.plot(w)
plt.xlabel('Time')
plt.ylabel('w')
plt.title('White noise');
```

Since we are drawing the data randomly at each time point, we will get a different time series if we repeat this process to generate another white noise sample. Next, let's create a matrix of `nt` by `nsamps`, where `nsamps = 100` and `nt=250`. Then plot these time series on top of one another. What do you notice about the expected mean and variance over time?

```python
nsamps = 100
w_matrix = np.zeros((nt, nsamps))
for n in np.arange(nsamps):
    w_matrix[:,n] = white_noise(nt)

plt.plot(w_matrix);
# Plot the mean across time as a line on top of this plot
...
# Plot the variance across time as a line on top of this plot
...
```

You see here that, as expected, the mean and variance don't change over time, and are pretty close to $0$ and $1$, respectively.

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

# Autoregression

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

# Data as signal plus white noise

Many datasets can be modeled as $v_t = s_t + w_t$, where $s_t$ is some signal of interest and $w_t$ is white noise. We will talk later about how we might find $s_t$ or other components of the signal. But for now, let's look at a few examples generating these types of data.

# Random walk

A _random walk_ is the term for a time series in which the value of the time series at time $t$ is the value of the series at time $t-1$ plus a random movement determined by $w_t$ (white noise). This is a classic example of a _nonstationary_ process (which we'll get into later). Let's first generate a function for this:

```python
def random_walk(nt, x0=0):
    '''
    Generate a random walk `x` for `nt` time points using initial value `x0=0`
    Inputs:
        nt (int) : number of time points
        x0 (float) :
    '''
    x = np.zeros((nt,))
    x[0] = x0
    # Loop through remaining time points and fill in x[t] values
    for ...
        x[t] = ...
    return x
```

```python
# Let's plot the random walk for `nt=250` time points
nt = 250
x0 = 0
x = random_walk(nt, x0=x0)
plt.plot(x)

# What do you notice about the data? Try running this cell a few times..
```

```python
# Let's now look at what happens if we simulate 100 random walks for
# 1500 time points and plot them on top of one another.
# What do you see about how the mean and variance
# of the signals change over time? How does this differ from white noise?

nwalks = 100
nt=1500
all_r = np.zeros((nt, nwalks))
for n in np.arange(nwalks):
    all_r[:,n]=random_walk(nt)
    plt.plot(all_r[:,n])
    plt.xlabel('Time')

plt.figure()
# Plot the mean across time of your `all_r` matrix:
... # FILL IN
plt.ylabel('Mean')

plt.figure()
# Plot the variance across time of your `all_r` matrix:
... # FILL IN
plt.ylabel('Variance')
```

# Random Walk with Drift

A _random walk with drift_ is a specific modification of the _random walk_ model in which we add a constant $\delta>0$ to our _random walk_:

$x_t = \delta + x_{t-1} + w_t$

which can also be written:

$x_t = \delta t + \displaystyle\sum_{j=1}^t w_j$

Let's now write a function for this:

```python
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
        x[n] = # FILL IN
    return x
```

```python
# Now let's plot a single example of the random walk. Try running a few times
# with different parameters. How does the `drift` parameter influence what
# you get? What about the properties of the white noise itself (if you go
# back...?)
nt = ... # FILL IN
drift = ... # FILL IN
plt.figure()
plt.plot(random_walk_drift(nt, drift))
```

```python
# Let's compare the mean and variance of the random
# walk with drift to our example above. Let's create
# a matrix of random walks with drift - `nwalks` samples
# and `nt` time points for drift `drift`.
nwalks = ... # FILL IN
nt = ... # FILL IN
drift = ... # FILL IN
all_r_drift = np.zeros((nt, nwalks))
for n in np.arange(nwalks):
    all_r_drift[:,n]=random_walk_drift(nt, drift)
    plt.plot(all_r_drift[:,n])
    plt.xlabel('Time')
```

```python
# Now plot the mean and variance over time. How do these change compare
# to the other graphs you created?

plt.figure()
plt.plot(all_r_drift.mean(1))

plt.figure()
plt.plot(all_r_drift.var(1))
```

# Load some data from Shumway and Stoffer examples
Next we will load some data from Shumway and Stoffer and try applying some of these functions to see how smoothing and noise might affect real world datasets.

```python
# Try applying the moving average to the DJIA data
# (where each sample is from one day). What happens
# when you apply the average over a month, a year, etc?
# Does this change how you might interpret the data?
n = 30
plt.plot(djia_data['Close'])
plt.plot(moving_average(djia_data['Close'], n=n))
```

```python
# Let's do the same thing with the speech data
speech_data = astsa.load_speech()
speech_data
```

```python
plt.plot(speech_data['Value'])
# Plot the smoothed speech data
n=... # Try some numbers here to see how they influence the original signal
plt.plot(moving_average(speech_data['Value'],n))
```

```python
# Try adding white noise to some of the datasets. If we just
# add the white noise with the default variance, it may not affect our signal
# that much, so try changing the `var` parameter in our `white_noise`
# function

noise_variance = ... # FILL IN
plt.figure()
plt.subplot(2,1,1)
plt.plot(speech_data['Value'])
plt.subplot(2,1,2)
plt.plot(speech_data['Value'] + white_noise(len(speech_data['Value']), var=noise_variance))
```

```python
# Extra: Try adding some drift to any of these datasets
```

---

[← fMRI data](03-fmri-data.md) · [Up: contents](index.md)
