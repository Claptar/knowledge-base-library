---
title: Sunspots Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Sunspots Dataset

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

One aspect of the sunspots dataset (that we ignored previously) is the following. The data shows clear peaks (as well as troughs). Further the distance between successive peaks varies from cycle to cycle. The following is an illustration of this.

```python
#peaks of a time series dataset can be found by using the following function from the signal processing module of scipy
from scipy.signal import find_peaks
# Find peaks
peaks, _ = find_peaks(y)
gaps = np.diff(peaks)
print("Peaks:", peaks)
print("Gaps between peaks:", gaps)
```

```
Peaks: [  5  17  27  38  50  52  61  69  78  87 102 104 116 130 137 148 160 164
 170 177 183 193 198 205 207 217 228 237 247 257 268 272 279 289 291 300
 314]
Gaps between peaks: [12 10 11 12  2  9  8  9  9 15  2 12 14  7 11 12  4  6  7  6 10  5  7  2
 10 11  9 10 10 11  4  7 10  2  9 14]
```

The gaps between the peaks is usually around 11 (but it can be as large as 14 and as small as 8). Sometimes we see a gap between peaks really small (such as 2) but this is most likely because of random fluctuation.

Previously, for the sunspots dataset, we used the model:
\begin{equation*}
    y_t = \beta_0 + \sum_{j=1}^k \left( \beta_{1j} \cos(2 \pi f_j t) + \beta_{2j} \sin(2 \pi f_j t) \right) + \epsilon_t
\end{equation*}
for this dataset. We discussed methods for estimating the parameters $\beta, f, \sigma$. The key role in parameter estimation is played by the RSS function.

```python
#rss function:
#below f is a vector (consisting of the k frequencies f1, \dots, fk)
def rss(f):
    n = len(y)
    X = np.column_stack([np.ones(n)])
    x = np.arange(1, n+1)
    if np.isscalar(f):
        f = [f]
    for j in range(len(f)):
        f1 = f[j]
        xcos = np.cos(2 * np.pi * f1 * x)
        xsin = np.sin(2 * np.pi * f1 * x)
        X = np.column_stack([X, xcos, xsin])
    md = sm.OLS(y, X).fit()
    ans = np.sum(md.resid ** 2)
    return ans
```

The model for $k = 1$ (where there is a single sinusoid) can be fit as follows.

```python
ngrid = 10000
fvals = np.linspace(0, 0.5, ngrid)
rssvals = np.array([rss(f) for f in fvals])
plt.plot(fvals, rssvals) #plot rss and find f which minimizes rss
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#MLE of f:
fhat = fvals[np.argmin(rssvals)]
print(fhat)
print(1/fhat)
```

```
0.09090909090909091
11.0
```

The MLE of $f$ is basically $1/11$ (corresponding to the 11-year solar cycle). After estimating $f$, the other parameters ($\beta_0, \beta_1, \beta_2, \sigma$) are estimated as follows.

```python
#Estimates of beta and sigma:
x = np.arange(1, n+1)
f = fhat
xcos = np.cos(2 * np.pi * f * x)
xsin = np.sin(2 * np.pi * f * x)
X = np.column_stack([np.ones(n), xcos, xsin])
md = sm.OLS(y, X).fit()
print(md.params) #this gives estimates of beta_0, beta_1, beta_2
rss_fhat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_fhat/n)
sigma_unbiased = np.sqrt((rss_fhat)/(n-3))
print(np.array([sigma_mle, sigma_unbiased])) #sig is the true value of sigma which generated the data
```

```
[ 78.87599158 -38.28231622 -29.2786631 ]
[51.62376442 51.86369026]
```

While the single sinusoid model is useful (for example, it gives the period corresponding to the solar cycle), it ignores several important features of the sunspots dataset. One way to see this is to simulate synthetic data from the single sinusoid model and compare the synthetic data with the actual sunspots data. We will take the parameters $f, \beta, \sigma$ to be those estimated from the sunspots dataset to make the plots comparable to the actual sunspots data.

```python
rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
sim_data = md.fittedvalues + errorsamples
plt.figure(figsize = (10, 6))
plt.plot(sim_data)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To facilitate comparison with the actual sunspots dataset, let us plot a bunch of these simulated datasets along with the real sunspots data (just to see if the sunspots dataset can be spotted as the "odd one out" from these plots).

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(5):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[i].plot(sim_data)
axes[5].plot(y)
for i, idx in enumerate(range(6, 9)):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear from the above plot-grid that the sunspots dataset sticks out as the odd one out. This shows that the simulated datasets (which are too wiggly and do not have well-defined peaks) are generated from a model that ignores many aspects of the sunspots dataset.

The model does not get much better if we fit two (or even three) sinusoids. For two sinusoids, we saw previously (see Lecture 8) that the best frequencies are $f_1 = 0.0908$ and $f_2 = 0.0099$. The estimates of the other parameters is obtained as follows.

```python
f1 = 0.0908
f2 = 0.0099
#Estimates of other parameters:
x = np.arange(1, n+1)
xcos = np.cos(2 * np.pi * f1 * x)
xsin = np.sin(2 * np.pi * f1 * x)
X = np.column_stack([np.ones(n), xcos, xsin])
xcos = np.cos(2 * np.pi * f2 * x)
xsin = np.sin(2 * np.pi * f2 * x)
X = np.column_stack([X, xcos, xsin])
md = sm.OLS(y, X).fit()
print(md.params) #this gives estimates of beta_0, beta_1, beta_2
rss_fhat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_fhat/n)
sigma_unbiased = np.sqrt((rss_fhat)/(n-5))
print(np.array([sigma_mle, sigma_unbiased])) #sig is the true value of sigma which generated the data
```

```
[ 80.44664774 -41.7696879  -23.78505115 -19.26881092 -16.42834923]
[48.32168827 48.69773821]
```

Let us now plot synthetic data from this model, and then compare them to the actual data.

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(2):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[i].plot(sim_data)
axes[2].plot(y)
for i, idx in enumerate(range(3, 9)):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Again one can easily spot the sunspots data from this plot-grid. Let us now repeat this exercise with three frequency components (whose frequencies are fixed to the values that we previously obtained in the code of Lecture 8).

```python
f1 = 0.0907
f2 = 0.01
f3 = 0.0998
#Estimates of other parameters:
x = np.arange(1, n+1)
xcos = np.cos(2 * np.pi * f1 * x)
xsin = np.sin(2 * np.pi * f1 * x)
X = np.column_stack([np.ones(n), xcos, xsin])
xcos = np.cos(2 * np.pi * f2 * x)
xsin = np.sin(2 * np.pi * f2 * x)
X = np.column_stack([X, xcos, xsin])
xcos = np.cos(2 * np.pi * f3 * x)
xsin = np.sin(2 * np.pi * f3 * x)
X = np.column_stack([X, xcos, xsin])
md = sm.OLS(y, X).fit()
print(md.params) #this gives estimates of beta_0, beta_1, beta_2
rss_fhat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_fhat/n)
sigma_unbiased = np.sqrt((rss_fhat)/(n-5))
print(np.array([sigma_mle, sigma_unbiased])) #sig is the true value of sigma which generated the data
```

```
[ 80.73881952 -43.5304532  -18.85510543 -17.48956354 -18.1002145
  30.36818441 -10.61894438]
[42.78339616 43.1163459 ]
```

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(6):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[i].plot(sim_data)
axes[6].plot(y)
for i, idx in enumerate(range(7, 9)):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The plots now look closer to the actual sunspots data, but still are quite a bit more wiggly (without clearly defined peaks) compared to the actual data.

---

← Introduction · [Up: contents](index.md) · [Ridge and LASSO regression with sinusoids →](03-ridge-and-lasso-regression-with-sinusoids.md)
