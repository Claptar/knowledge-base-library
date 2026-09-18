---
title: Inference in Sinusoid Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Inference in Sinusoid Models

In the last lab, we studied the following problem. Consider the following dataset simulated using the model:
\begin{equation*}
    y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin( 2 \pi f t) + \epsilon_t,
\end{equation*}
for $t = 1, \dots, n$ with some fixed values of $f, \beta_0, \beta_1, \beta_2$ and $\sigma$. The goal of this problem is to estimate $f$ along with associated uncertainty quantification.

Today we will start by addressing the problem of estimating the other parameters $\beta_0, \beta_1, \beta_2, \sigma$ also along with uncertainty quantification.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
f = 0.2035
#f = 1.8
n = 400
b0 = 0
b1 = 3
b2 = 5
sig = 10

rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sig, size = n)
t = np.arange(1, n + 1)

y = b0 * np.ones(n) + b1 * np.cos(2 * np.pi * f * t) + b2 * np.sin(2 * np.pi * f * t) + errorsamples
```

```python
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('A simulated dataset')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To obtain the MLEs of the parameters, we first obtain the MLE of $f$ (as before), then plug in $f = \hat{f}$, and run linear regression to estimate the other parameters.

```python
def rss(f):
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

```python
# We can minimize rss(f) over a fine grid of possible f values.
# Since n is not very big here, we can work with a dense grid.
ngrid = 100000
allfvals = np.linspace(0, 0.5, ngrid)
rssvals = np.array([rss(f) for f in allfvals])
fhat = allfvals[np.argmin(rssvals)]

print(fhat)

plt.plot(allfvals, rssvals)
plt.show()
```

```
0.2035520355203552
```

*(1 figure omitted — see the original notebook.)*

```python
# We can obtain an approximation to the MLE by working with Fourier frequencies and maximizing the periodogram.
fft_y = np.fft.fft(y)
m = n // 2 - 1
fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)
m = len(fourier_freqs)
pgram_y = (np.abs(fft_y[1:(m + 1)]) ** 2)/n

plt.plot(fourier_freqs, pgram_y)
plt.xlabel("Frequencies")
plt.title("Periodogram")
plt.show()

fhat_fft = fourier_freqs[np.argmax(pgram_y)]
print(fhat_fft)
```

```
0.2025
```

*(1 figure omitted — see the original notebook.)*

Except in rare cases where the true frequency is already a Fourier frequency, the MLE of $f$ computed on a fine grid will be closer to the truth compared to the MLE computed on the grid of Fourier frequencies. But the MLE computed on Fourier frequencies is much more computationally cheap.

After computing the MLE of $f$, we can do linear regression (where $f$ is fixed the MLE) to compute the MLEs of the coefficient parameters and $\sigma$.

```python
x = np.arange(1, n + 1)
xcos = np.cos(2 * np.pi * fhat * x)
xsin = np.sin(2 * np.pi * fhat * x)
Xfhat = np.column_stack([np.ones(n), xcos, xsin])

md = sm.OLS(y, Xfhat).fit()
print(md.params)
# this gives estimates of beta_0, beta_1, beta_2 (compare them to the true values which generated the data)

b0_est = md.params[0]
b1_est = md.params[1]
b2_est = md.params[2]
print(np.column_stack((np.array([b0_est, b1_est, b2_est]), np.array([b0, b1, b2]))))

rss_fhat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_fhat / n)
sigma_unbiased = np.sqrt((rss_fhat)/(n - 3))
print(np.array([sigma_mle, sigma_unbiased, sig]))
# sig is the true value of sigma which generated the data
```

```
[-0.05332889  3.00407151  5.63909328]
[[-0.05332889  0.        ]
 [ 3.00407151  3.        ]
 [ 5.63909328  5.        ]]
[ 9.50176964  9.53760297 10.        ]
```

Now let us use Bayesian inference for uncertainty quantification.  The Bayesian posterior for $f$ is:
\begin{equation*}
   I\{0 \leq f \leq 1/2\} \cdot |X_f^T X_f|^{-1/2} \cdot \left(\frac{1}{RSS(f)} \right)^{(n-p)/2}
\end{equation*}
where $p = 3$ and $|X_f^T X_f|$ denotes the determinant of $X_f^T X_f$.

It is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python
def logpost(f):
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])
    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X))
    # sgn gives the sign of the determinant (in our case, this should 1)
    # log_det gives the logarithm of the absolute value of the determinant

    logval = ((p - n)/2) * np.log(rss) - 0.5 * log_det
    return logval
```

While evaluating the log posterior on a grid, it is important to make sure that we do not include frequencies $f$ for which $X_f^T X_f$ is singular. This will be the case for $f = 0$ and $f = 1/2$. When $f$ is very close to 0 or $0.5$, the term $|X_f^T X_f|^{-1/2}$ will be very large because of near-singularity of $X_f^T X_f$. We will therefore exclude frequencies very close to 0 and 0.5 from the grid while calculating posterior probabilities.

From the Periodogram plotted above, it is clear that the maximizing frequency is around 0.2. So we will take a grid that around 0.2 (such as 0.05 to 0.35)

```python
ngrid = 10000
allfvals = np.linspace(0.05, 0.35, ngrid)
print(np.min(allfvals), np.max(allfvals))

logpostvals = np.array([logpost(f) for f in allfvals])

plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

```
0.05 0.35
```

*(1 figure omitted — see the original notebook.)*

Note that the logarithm of the posterior looks similar to the periodogram. But the posterior itself will have only one peak (which dominates all other peaks).

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized / (np.sum(postvals_unnormalized))

plt.plot(allfvals, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can draw posterior samples from f as follows.

```python
N = 2000
fpostsamples = rng.choice(allfvals, N, replace = True, p = postvals)
```

Given a posterior sample of $f$, a posterior sample of $\sigma$ can be drawn (this result was proved in Problem 4 of Homework one):
\begin{equation*}
   \frac{RSS(\hat{f})}{\sigma^2} \mid \text{data}, f \sim \chi^2_{n-3}
\end{equation*}
Further, given posterior samples from $f$ and $\sigma$, a posterior sample from $\beta = (\beta_0, \beta_1, \beta_2)$ is drawn using:
\begin{equation*}
   \beta \mid \text{data}, \sigma, f \sim N_3 \left(\hat{\beta}, \sigma^2 (X_f^T X_f)^{-1} \right)
\end{equation*}
This is done in code as follows.

```python
post_samples = np.zeros(shape = (N, 5))
post_samples[:,0] = fpostsamples
for i in range(N):
    f = fpostsamples[i]
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])
    p = X.shape[1]

    md_f = sm.OLS(y, X).fit()
    chirv = rng.chisquare(df = n - p)
    sig_sample = np.sqrt(np.sum(md_f.resid ** 2) / chirv) # posterior sample from sigma
    post_samples[i, (p + 1)] = sig_sample

    covmat = (sig_sample ** 2) * np.linalg.inv(np.dot(X.T, X))
    beta_sample = rng.multivariate_normal(mean = md_f.params, cov = covmat, size = 1)
    post_samples[i, 1:(p + 1)] = beta_sample

print(post_samples)
```

```
[[ 0.20340534 -0.56189444  3.28165364  5.35964685  9.18963362]
 [ 0.20367537 -1.22669044  3.16545782  6.3549404   9.63517389]
 [ 0.20343534 -0.18052831  3.81020787  5.08243908  9.38448971]
 ...
 [ 0.20355536 -0.24135565  2.17378505  5.44757671  9.50053706]
 [ 0.20355536 -0.37830076  2.90179999  6.50300091  9.49852951]
 [ 0.20337534 -0.52307159  4.11483084  4.68294379  9.84908592]]
```

Let us plot the posterior functions along with the original data to visualize uncertainty.

```python
x = np.arange(1, n + 1)
plt.figure(figsize = (15, 6))
plt.plot(y)

for i in range(N):
    f = fpostsamples[i]
    b0 = post_samples[i, 1]
    b1 = post_samples[i, 2]
    b2 = post_samples[i, 3]

    ftdval = b0 + b1 * np.cos(2 * np.pi * f * x) + b2 * np.sin(2 * np.pi * f * x)
    plt.plot(ftdval, color = 'red')
```

*(1 figure omitted — see the original notebook.)*

A simple summary of the posterior samples can be obtained as follows.

```python
pd.DataFrame(post_samples).describe()
# note that the true value of f is 0.2035, b0 is 0, b1 is 3, b2 is 5 and sigma is 10
```

```
0            1            2            3            4
count  2000.000000  2000.000000  2000.000000  2000.000000  2000.000000
mean      0.203554    -0.048116     2.926668     5.487344     9.567343
std       0.000154     0.479084     1.240482     0.894120     0.337935
min       0.203045    -2.282401    -1.430247     1.670873     8.564508
25%       0.203435    -0.359168     2.134556     4.928442     9.343711
50%       0.203555    -0.061192     3.009265     5.519098     9.567323
75%       0.203645     0.268955     3.769393     6.097100     9.787657
max       0.204095     1.614744     6.128241     8.477974    10.710101
```

---

[Up: contents](index.md) · [Change-point Model →](02-change-point-model.md)
