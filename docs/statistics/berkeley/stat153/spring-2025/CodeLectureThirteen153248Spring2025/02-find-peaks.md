---
title: Find peaks
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Ridge and LASSO regression with sinusoids

Let us now try the high-dimensional version of the sinusoidal model where we use sinusoids at all the Fourier frequencies:
\begin{equation*}
   y_t = \beta_0 + \sum_{j = 1}^{(n-1)/2} \left( \beta_{1j} \cos(2 \pi (j/n) t) + \beta_{2j} \sin (2 \pi (j/n) t) \right) + \epsilon_t
\end{equation*}
Here $n = 325$ is odd. If $n$ were even, we will add another term for $\cos (\pi t)$.

We would need to use some kind of regularization for meaningful estimation in this high-dimensional regression model. It is natural to try ridge or LASSO regularization. These will make the size of the coefficients $\beta_{1j}, \beta_{2j}$ small but this may not produce anything useful in this dataset. Let us illustrate this below.

The first step for implementing ridge or LASSO regularization is to create the $X$ matrix.

```python
#Creating the X matrix
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
m = (n-1)//2
for j in range(m):
    f = j/n
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([X, xcos, xsin])
```

We will use the same code for ridge and LASSO regression that we used last week.

```python
#note that penalty_start is now set to 1 (instead of 2 as in the model used in class)
def solve_ridge(X, y, lambda_val, penalty_start=1):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

```python
#note that penalty_start is now set to 1 (instead of 2 as in the model used in class)
def solve_lasso(X, y, lambda_val, penalty_start=1):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.norm1(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

```python
b_ridge = solve_ridge(X, y, lambda_val = 200)
ridge_fitted = np.dot(X, b_ridge)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'gray')
plt.plot(ridge_fitted, color = 'red', label = 'Ridge')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fitted values produced by ridge regression appear to be very similar to the original data values but shrunk towards the overall mean of the data. The extent of shrinkage is controlled by the value of $\lambda$ (when $\lambda$ is small, these fitted values will be very close to the actual observations) It is unclear how these fitted values may be interpreted or how may they be useful. We can also estimate $\sigma$ and plot simulated datasets, and compare with the original dataset.

```python
sig_ridge = np.sqrt((np.sum((y - ridge_fitted) ** 2))/n)
print(sig_ridge)
```

```
34.13721232125516
```

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(6):
    errorsamples = rng.normal(loc = 0, scale = sig_ridge, size = n)
    sim_data = ridge_fitted + errorsamples
    axes[i].plot(sim_data)
axes[6].plot(y)
for i, idx in enumerate(range(7, 9)):
    errorsamples = rng.normal(loc = 0, scale = sig_ridge, size = n)
    sim_data = ridge_fitted + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

As before, one can easily spot the sunspots data from this plot-grid.

```python
#To illustrate the shrinkage effect of the ridge coefficients, below we compare the ridge coefficients with the unregularized estimates of the coefficients
#the unregularized estimates correspond to lambda equaling 0
b_ridge_0 = solve_ridge(X, y, lambda_val = 0)
plt.figure(figsize = (10, 6))
plt.plot(b_ridge_0[1:], color = 'lightgray')
plt.plot(b_ridge[1:])
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next let us use LASSO regularization.

```python
b_lasso = solve_lasso(X, y, lambda_val = 2000)
lasso_fitted = np.dot(X, b_lasso)
plt.figure(figsize = (10, 6))
plt.plot(y, color = 'lightgray')
plt.plot(lasso_fitted, color = 'red', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These fitted values look similar to the fitted values for the model with three sinusoidal components. This is unsurprising as the LASSO zeroes out many of the components so that the fitted model will be a sum of a small (but probably more than 3) sinusoidal components. This model might be useful for prediction. But data simulated from it (with $\sigma$ estimated as below) will still be wiggly without clearly defined peaks.

```python
sig_lasso = np.sqrt((np.sum((y - lasso_fitted) ** 2))/n)
print(sig_lasso)
```

```
33.54702098714371
```

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(6):
    errorsamples = rng.normal(loc = 0, scale = sig_lasso, size = n)
    sim_data = lasso_fitted + errorsamples
    axes[i].plot(sim_data)
axes[6].plot(y)
for i, idx in enumerate(range(7, 9)):
    errorsamples = rng.normal(loc = 0, scale = sig_lasso, size = n)
    sim_data = lasso_fitted + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#To illustrate the sparsity nature of LASSO coefficients, below we compare the LASSO coefficients with the unregularized estimates of the coefficients
#the unregularized estimates correspond to lambda equaling 0
b_lasso_0 = solve_lasso(X, y, lambda_val = 0)
plt.figure(figsize = (10, 6))
plt.plot(b_lasso_0[1:], color = 'lightgray')
plt.plot(b_lasso[1:])
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear from the above plot that most of the small unregularized coefficients are set to exactly zero by LASSO.

## The Spectrum Model

To obtain the spectrum model, we shall first remove the $\epsilon_t$ and write:
\begin{equation*}
   y_t = \beta_0 + \sum_{j = 1}^{m} \left( \beta_{1j} \cos(2 \pi (j/n) t) + \beta_{2j} \sin (2 \pi (j/n) t) \right)
\end{equation*}
where $m := (n-1)/2$. We further assume that
\begin{equation*}
    \beta_{1j}, \beta_{2j} \overset{\text{i.i.d}}{\sim} N(0, \tau_j^2)
\end{equation*}
The variances $\tau_1^2, \dots, \tau_m^2$ denote the unknown parameters in the model (collectively, they are known as the spectrum of the model).

The variance parameter $\tau_j^2$ represents how much contribution the corresponding frequency $j/n$ has in the overall variance structure of $y_t$. If $\tau_j^2$ is large for a specific $j$, the corresponding frequency $j/n$ has a strong contribution to the data. If $\tau_j^2$ is small, the contribution of that frequency is small.

The total variance of $y_t$ is given by:
\begin{equation*}
   \text{var}(y_t) = \sum_{j=1}^m \tau_j^2.
\end{equation*}
This reflects how the variance of the signal is distributed across different frequency components.

The sequence $\{\tau_j^2\}$ provides a **spectral representation** of the time series, in the sense that it describes the distribution of variance across frequencies.

Below we take some fixed spectrum i.e., we fix $\tau_j^2, j = 1, \dots, m$ and simulate data from the spectrum model. The goal is to get a sense of the kind of data we would get for different spectra.

### Example One

The first example corresponds to the case where $\tau_j^2$ takes a constant value when $j/n$ lies between $1/13$ and $1/9$ and then zero for other values of $j/n$. Frequencies between $1/13$ and $1/9$ contributed equally to this data while no other frequency has any contribution. Let us see how the data looks.

```python
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
m = (n-1)//2
for j in range(m):
    f = j/n
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([X, xcos, xsin])

tau_t = np.zeros(m)
lf = n // 13
uf = n // 9
y = sunspots.iloc[:,1].values
tau_t[lf:uf] = np.sqrt(np.var(y)/(uf - lf))

b_coeff = np.zeros(n)
b_coeff[0] = np.mean(y) #we are using the mean of the sunspots dataset for b0
for j in range(m):
    tauval = tau_t[j]
    aj = rng.normal(loc = 0, scale = tauval, size = 1)
    bj = rng.normal(loc = 0, scale = tauval, size = 1)
    b_coeff[(2*j)+1] = aj.item()
    b_coeff[(2*j)+2] = bj.item()
simvals = np.dot(X, b_coeff)
plt.figure(figsize = (10, 6))
plt.plot(simvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The data looks quite smooth (without any seemingly random fluctuation). Let us look at the peaks and the gaps between them.

```python

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Find peaks →](03-find-peaks.md)
