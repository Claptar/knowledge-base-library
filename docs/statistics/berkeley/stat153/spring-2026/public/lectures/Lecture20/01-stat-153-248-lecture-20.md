---
title: Stat 153/248 Lecture 20
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stat 153/248 Lecture 20

In this lecture, we will discuss a specific application of time-lagged regression models to understand speech processing in the brain. Here, we are relating our input sound stimulus $x$ at different time lags to our output neural time series $y$. This is typically written as:

$$y_t = \sum_{\tau} \beta_\tau x_{t-\tau}$$

where $\tau$ is the time delay.

These models have been used to show which stimulus features may drive neural activity in different brain areas - for example, frequency features from a spectrogram, phoneme features, word onsets, visual features, and more.

In the case of using a spectrogram as the input $x$, these are sometimes also called a spectrotemporal receptive field (STRF) model. In neuroscience, the "STRF" itself refers to the $\beta$ coefficients of this regression model, which can be thought of as a linear filter that describes which spectrotemporal features of a stimulus will increase or decrease activity in a given brain area. This technique has been applied widely to various types of brain related time series data, including scalp electroencephalography (EEG), intracranial EEG, magnetoencephalography (MEG), and functional magnetic resonance imaging (fMRI). Other terms used for the $\beta$ coefficients are "TRF weights" or "mTRF" weights (for multivariate temporal receptive field or multivariate temporal response function).

**References:**

* Aertsen & Johannesma (1981). [The spectro-temporal receptive field](http://hearingbrain.org/docs/AertsenSTRF_1981.pdf).  Biological Cybernetics 42, 133-143.
* Theunissen, David, Singh et al. (2001). [Estimating spatio-temporal receptive fields of auditory and visual neurons from their responses to natural stimuli.](http://www.maths.tcd.ie/~mnl/store/TheunissenEtAl2001a.pdf) Network 2001, 12:3 289-316.
* Wu, David, Gallant (2006). [Complete functional characterization of sensory neurons by system identification.  Annu Rev Neurosci 29: 477-505. ](http://suns.mit.edu/2006.Wu.David.Gallant.pdf)
* Holgraf et al. (2017). [Encoding and Decoding Models in Cognitive Electrophysiology.](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2017.00061/full) Frontiers in Systems Neuroscience.

### The STRF as a time-lagged regression

For a single time point $t$, single output, $F$ frequency features, and $D$ delays:

$$
y_t = \sum_{f=1}^{F} \sum_{d=0}^{D-1} \beta_{f,d}\, x_{f,\, t-d}
$$

The response at time $t$ is a weighted sum over all (frequency, delay) pairs of the spectrogram values at the corresponding earlier time points. The weight $\beta_{f,d}$ is the STRF — it tells you how much frequency $f$ at delay $d$ contributes to the response.

#### Predicting one response time point

Collect the weights into a matrix $B \in \mathbb{R}^{F \times D}$ and the relevant slice of stimulus history into a matrix $X_t \in \mathbb{R}^{F \times D}$:

$$
B = \begin{bmatrix} \beta_{1,0} & \beta_{1,1} & \cdots & \beta_{1,D-1} \\ \beta_{2,0} & \beta_{2,1} & \cdots & \beta_{2,D-1} \\ \vdots & & & \vdots \\ \beta_{F,0} & \beta_{F,1} & \cdots & \beta_{F,D-1} \end{bmatrix}, \quad X_t = \begin{bmatrix} x_{1,t} & x_{1,t-1} & \cdots & x_{1,t-D+1} \\ x_{2,t} & x_{2,t-1} & \cdots & x_{2,t-D+1} \\ \vdots & & & \vdots \\ x_{F,t} & x_{F,t-1} & \cdots & x_{F,t-D+1} \end{bmatrix}
$$

Then:

$$
y_t = \sum_{f,d} B_{f,d}\, (X_t)_{f,d} = \langle B, X_t \rangle_F
$$

where $\langle \cdot, \cdot \rangle_F$ is the Frobenius inner product (sum of elementwise products). This is the "STRF as a 2D filter" view — the response is the inner product of the STRF kernel with the recent stimulus history.

#### Vectorize and stack across time

Flatten $B$ into a column vector $\beta \in \mathbb{R}^{FD}$ and flatten each $X_t$ into a row vector.

$$
\beta = \mathrm{vec}(B) = \begin{bmatrix} \beta_{1,0} \\ \beta_{1,1} \\ \vdots \\ \beta_{1,D-1} \\ \beta_{2,0} \\ \vdots \\ \beta_{F,D-1} \end{bmatrix}, \quad \mathbf{x}_t^T = \begin{bmatrix} x_{1,t} & x_{1,t-1} & \cdots & x_{1,t-D+1} & x_{2,t} & \cdots & x_{F,t-D+1} \end{bmatrix}
$$

Then for each time point:

$$
y_t = \mathbf{x}_t^T \beta
$$

Stack the $\mathbf{x}_t^T$ as rows of a design matrix $\mathbf{X} \in \mathbb{R}^{T \times FD}$:

$$
\mathbf{X} = \begin{bmatrix} \mathbf{x}_1^T \\ \mathbf{x}_2^T \\ \vdots \\ \mathbf{x}_T^T \end{bmatrix}
$$

and you get the standard linear regression form:

$$
\mathbf{y} = \mathbf{X} \beta
$$

with $\mathbf{y} \in \mathbb{R}^T$, $\mathbf{X} \in \mathbb{R}^{T \times FD}$, $\beta \in \mathbb{R}^{FD}$.

#### STRFs and linear regression

A STRF is fundamentally a linear regression. The "spectrotemporal" part is for interpretation, and just involves reshaping the $\beta$ matrix so we can better interpret it in terms of the multiple features (frequencies in a spectrogram) and time delays, even though we actually estimate the regression with everything flattened.

#### Multi-electrode version

In many cases in real world problems, we have multiple electrodes we are trying to fit from the brain. If you have $E$ electrodes, replace $\mathbf{y}$ with $\mathbf{Y} \in \mathbb{R}^{T \times E}$ and $\beta$ with $\mathbf{B} \in \mathbb{R}^{FD \times E}$:

$$
\mathbf{Y} = \mathbf{X} \mathbf{B}
$$

Same design matrix, just solving $E$ regressions in parallel.

```python
import numpy as np
import sys
import os
import h5py
import scipy.io
import glob
from matplotlib import pyplot as plt
import re

from matplotlib import cm
plt.ion()

from ridge.utils import make_delayed
from ridge.ridge import cv_ridge
import logging
logging.basicConfig(level=logging.INFO)
```

```python
# Define a z-scoring function
zs = lambda x: (x-x.mean(0))/x.std(0)
```

### Get the data!

Here we will load in the data from our experiment. We have neural data `ytrain` and `ytest`, which are matrices of dimension `[time points x electrodes]`, where each electrode is taken from a session where a patient with epilepsy was listening to a set of movie clips. Here we will look at data from 3 example electrodes from one patient listening to movie clips.

```python
data_file = 'MTdata_TCH28.hf5'

# Here we will read in the contents of the file
xtrain = {}
xtest = {}
with h5py.File(data_file, 'r') as hf:
    # This is neural data [time points x electrodes]
    ytrain = hf['ytrain'][:]
    ytest = hf['ytest'][:]

    # This is the spectrogram of the sounds the person heard
    xtrain['spec'] = hf['xtrain_spec'][:]
    xtest['spec'] = hf['xtest_spec'][:]

    # These are the phoneme features for the words the person heard
    xtrain['phn'] = hf['xtrain_phn'][:]
    xtest['phn'] = hf['xtest_phn'][:]

    # Sampling rate of the data
    fs = hf.attrs['fs']
```

```python
print(ytrain.shape, ytest.shape)

# Show whether the data have been z-scored
print(ytrain.mean(), ytrain.std())
print(ytest.mean(), ytest.std())
print(xtrain['spec'].mean(), xtrain['spec'].std())
print(xtest['spec'].mean(), xtest['spec'].std())
```

```
(161034, 3) (13563, 3)
1.8826142342050505e-18 0.9999999999999961
1.1176174172048075e-17 1.0000000000000016
2.188539047263371e-15 1.0
-1.2874952646199382e-15 0.9999999999999996
```

```python
# Let's look at what we're using for our xtrain matrices

stim_types = ['spec', 'phn']

for stim_type in stim_types:
    ntimes, nfeats = xtest[stim_type].shape
    print(f'{ntimes} time points, {nfeats} {stim_type} features')
    nsec_to_show = 20

    plt.figure(figsize=(10,3))
    plt.imshow(xtest[stim_type].T, aspect='auto', cmap=cm.magma, interpolation='nearest')
    plt.gca().invert_yaxis()
    ticks = np.arange(0, ntimes, fs*10)
    plt.gca().set_xticks(ticks)
    plt.gca().set_xticklabels((ticks / fs).astype(int))
    plt.gca().set_xlim([0,nsec_to_show*fs])
    plt.title(f'xtest - {stim_type}')
    plt.colorbar()

    plt.xlabel('Time (s)')
    plt.ylabel('Feature (bin)')
```

```
13563 time points, 80 spec features
13563 time points, 14 phn features
```

*(2 figures omitted — see the original notebook.)*

```python
# Let's show the response data that goes with this test set:

ntimes,nelecs = ytest.shape
print(f'{ntimes} time points, {nelecs} electrodes')

plt.figure(figsize=(10,3))
for ch in np.arange(nelecs):
    plt.subplot(nelecs,1,ch+1)
    plt.plot(ytest[:,ch]+ch)
    ticks = np.arange(0, ntimes, fs*10)
    plt.gca().set_xticks(ticks)
    plt.gca().set_xlim([0,nsec_to_show*fs])
    #plt.colorbar(label='z-score')
    if ch == nelecs-1:
        plt.xlabel('Time (s)')
        plt.ylabel('Z')
        plt.gca().set_xticklabels((ticks / fs).astype(int))
    else:
        plt.gca().set_xticklabels([])
```

```
13563 time points, 3 electrodes
```

*(1 figure omitted — see the original notebook.)*

## How do we choose the lags?

If we want to fit a lagged regression model, we first have to choose what lags we want to consider in our model. Usually, we do this based on prior knowledge about a particular brain area (say, if we know that most responses occur within 500 milliseconds, we probably don't need to search beyond that). However, we can also use the cross-correlation function to look at where our peak lead-lag relationships lie between $x$ and $y$. We'll do that here, using a maximum possible lag between the sound features and the neural recordings of 0.6 seconds, which is reasonable based on prior literature.

```python
from scipy.signal import correlate

stim_type = 'spec'

ntimes, nelecs = ytrain.shape
ntimes, nfeats = xtrain[stim_type].shape

max_lag_sec = 0.6 # seconds
max_lag = int(max_lag_sec * fs)

lags = np.arange(-max_lag, max_lag + 1)
ccf = np.zeros((nelecs, nfeats, len(lags)))

for e in range(nelecs):
    for f in range(nfeats):
        full = correlate(ytrain[:, e], xtrain[stim_type][:, f], mode='full') / ntimes
        mid = len(full) // 2
        ccf[e, f] = full[mid - max_lag : mid + max_lag + 1]
```

---

[Up: contents](index.md) · [Plotting lag relationships →](02-plotting-lag-relationships.md)
