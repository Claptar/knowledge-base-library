---
title: Data from Time Series Analysis and Its Applications
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Data from Time Series Analysis and Its Applications

For this lab, we will give some practical examples for concepts related to time series characteristics discussed in Lectures 1 and 2. This will include the following concepts:

1. Loading data from the `astsa` library (from your Time Series book)
2. Generating white noise
3. Computing moving averages
4. Generating data from an autoregressive process
5. Random walks and random walks + drift

For this lab, you will fill in the aspects of the code marked `...` or with the comment `# FILL IN`

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
!pip install astsa # Only need to do this if you don't have it installed already
import astsa

# Set the random seed, this is so you will generate the same answers
# each time (for example, when generating white noise)
np.random.seed(42)
```

First, we will use the `astsa` library to load and plot some of the data from Chapter 1. You can use this library yourself if you are interested in looking further at any of the examples.

As we go on, you can think about how to fit models to these data or test assumptions about these data.

```python
# Let's print all the possible datasets we could load from the book
# These are functions named `load_X`

dir(astsa.datasets)
```

## Dow Jones Industrial Average Data

```python
import matplotlib.dates as mdates
locator = mdates.AutoDateLocator(minticks=7, maxticks=10)

djia_data = astsa.load_djia()
# Calculate the return
djia_return = np.diff(np.log(djia_data['Close']))

plt.figure()
plt.subplot(2,1,1)
plt.plot(djia_data['Date'],djia_data['Close'])
plt.gca().xaxis.set_major_locator(locator)
plt.gca().set_xticklabels([]) # Hide labels since they're the same for both subplots
plt.ylabel('Returns')
plt.gca().grid(True)

plt.subplot(2,1,2)
plt.plot(djia_data['Date'][1:],djia_return)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().tick_params(axis='x', labelrotation=45)
plt.ylabel('Returns')
plt.gca().grid()

plt.tight_layout()
```

## fMRI data

```python
fmri_data = astsa.load_fmri1()

print(fmri_data)

plt.subplot(3,1,1)
plt.plot(fmri_data['cort1'])
plt.plot(fmri_data['cort2'])
plt.ylabel('BOLD')

plt.subplot(3,1,2)
plt.plot(fmri_data['thal1'])
plt.plot(fmri_data['thal2'])
plt.ylabel('BOLD')

plt.subplot(3,1,3)
plt.plot(fmri_data['cere1'])
plt.plot(fmri_data['cere2'])
plt.xlabel('Time (s)')
plt.ylabel('BOLD')

plt.tight_layout()
```

## White Noise

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

---

[Up: contents](index.md) · [Moving average and filtering →](02-moving-average-and-filtering.md)
