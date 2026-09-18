---
title: Change of Slope (or Broken Stick Regression)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Change of Slope (or Broken Stick Regression)

Now consider the model:
\begin{equation*}
  y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t
\end{equation*}
Here $(t - c)_+ = \max(t-c, 0)$ denotes the positive part function (also known as the ReLU function). This model has parameters $\beta_, \beta_1, \beta_2$ **and** $c$ (as well as $\sigma$). This is a nonlinear regression model because of the presence of the parameter $c$. If a known value is plugged in for $c$, we would revert to a linear regression model.

This model states that, until the time point $c$, the slope parameter equals $\beta_1$. After $c$, the slope parameter becomes $\beta_1 + \beta_2$.

Let us fit this model to the US population dataset that we previously used in the class.

```python
uspop = pd.read_csv("POPTHM-Jan2025FRED.csv")
y = uspop['POPTHM']
n = len(y)

plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

For obtaining the MLEs, we proceed exactly as before. The RSS is now given by:
\begin{equation*}
    RSS(c) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t - \beta_2 (t - c)_+ \right)^2
\end{equation*}

```python
def rss(c):
    x = np.arange(1, n + 1)
    xc = ((x > c).astype(float)) * (x - c)
    X = np.column_stack([np.ones(n), x, xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

```python
allcvals = np.arange(5, n - 4) # we are ignoring a few points at the beginning and at the end
rssvals = np.array([rss(c) for c in allcvals])

plt.plot(allcvals, rssvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
c_hat = allcvals[np.argmin(rssvals)]
print(c_hat)
```

```
298
```

```python
# Estimates of other parameters:
x = np.arange(1, n + 1)
c = c_hat
xc = ((x > c).astype(float)) * (x - c)
X = np.column_stack([np.ones(n), x, xc])

md = sm.OLS(y, X).fit()
print(md.params)
# this gives estimates of beta_0, beta_1, beta_2 (this is a real dataset so there are no true parameters)

rss_chat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_chat / n)
sigma_unbiased = np.sqrt((rss_chat) / (n - 3))
print(np.array([sigma_mle, sigma_unbiased]))
# sig is the true value of sigma which generated the data
```

```
const    178331.892380
x1          191.173841
x2           32.346330
dtype: float64
[2214.41969096 2218.63095249]
```

```python
# Plot fitted values
X_linmod = np.column_stack([np.ones(n), x])
linmod = sm.OLS(y, X_linmod).fit()

plt.figure(figsize = (15, 6))
# Plot this broken regression fitted values along with linear model fitted values
plt.plot(y, color = 'None')
plt.plot(md.fittedvalues, color = 'red')
plt.plot(linmod.fittedvalues, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
# Bayesian log posterior
def logpost(c):
    x = np.arange(1, n + 1)
    xc = ((x > c).astype(float)) * (x - c)
    X = np.column_stack([np.ones(n), x, xc])
    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) #sgn gives the sign of the determinant (in our case, this should 1)
    # log_det gives the logarithm of the absolute value of the determinant

    logval = ((p - n) / 2) * np.log(rss) - 0.5 * log_det
    return logval
```

```python
allcvals = np.arange(5, n - 4)
logpostvals = np.array([logpost(c) for c in allcvals])

plt.plot(allcvals, logpostvals)
plt.xlabel('Changepoint')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
# this plot looks similar to the RSS plot
```

*(1 figure omitted — see the original notebook.)*

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized / (np.sum(postvals_unnormalized))

plt.plot(allcvals, postvals)
plt.xlabel('Changepoint')
plt.ylabel('Probability')
plt.title('Posterior distribution of change points')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
# Drawing posterior samples:
N = 2000
cpostsamples = rng.choice(allcvals, N, replace = True, p = postvals)

post_samples = np.zeros(shape = (N, 5))
post_samples[:, 0] = cpostsamples
for i in range(N):
    f = cpostsamples[i]
    x = np.arange(1, n + 1)
    xc = ((x > c).astype(float)) * (x - c)
    X = np.column_stack([np.ones(n), x, xc])
    p = X.shape[1]

    md_c = sm.OLS(y, X).fit()
    chirv = rng.chisquare(df = n - p)
    sig_sample = np.sqrt(np.sum(md_c.resid ** 2) / chirv) # posterior sample from sigma
    post_samples[i, (p + 1)] = sig_sample

    covmat = (sig_sample ** 2) * np.linalg.inv(np.dot(X.T, X))
    beta_sample = rng.multivariate_normal(mean = md_c.params, cov = covmat, size = 1)
    post_samples[i, 1:(p + 1)] = beta_sample

print(post_samples)
```

```
[[3.02000000e+02 1.78679868e+05 1.89836033e+02 3.42169717e+01
  2.22133894e+03]
 [2.85000000e+02 1.78325271e+05 1.91295418e+02 3.24809108e+01
  2.25595672e+03]
 [2.83000000e+02 1.78395919e+05 1.90801617e+02 3.30139821e+01
  2.25832125e+03]
 ...
 [2.90000000e+02 1.78563273e+05 1.90179251e+02 3.33837727e+01
  2.15566567e+03]
 [2.90000000e+02 1.78292844e+05 1.91629020e+02 3.21929322e+01
  2.29143430e+03]
 [3.04000000e+02 1.78581825e+05 1.90525611e+02 3.27431913e+01
  2.21071767e+03]]
```

```python
# Let us plot the posterior samples for c on the original plot:
plt.plot(y)

for i in range(N):
    plt.axvline(x = cpostsamples[i], color = 'gray')

plt.plot(y, color = 'blue')
plt.axvline(x = c_hat, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
# Plot the fitted values for the different posterior draws:
x = np.arange(1, n + 1)
plt.figure(figsize = (15, 6))
plt.plot(y)

for i in range(N):
    c = cpostsamples[i]
    b0 = post_samples[i, 1]
    b1 = post_samples[i, 2]
    b2 = post_samples[i, 3]

    ftdval = b0 + b1 * x + b2 * ((x > c).astype(float)) * (x - c)

    plt.plot(ftdval, color = 'red')
plt.plot(y, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Summary of the posterior samples:
pd.DataFrame(post_samples).describe()
```

```
0              1            2            3            4
count  2000.000000    2000.000000  2000.000000  2000.000000  2000.000000
mean    297.426500  178341.563897   191.135089    32.379440  2221.533224
std       9.176748     236.325641     1.082882     1.523587    56.259513
min     262.000000  177418.875703   187.952460    27.840629  2029.175952
25%     291.000000  178179.981065   190.371263    31.358716  2182.856960
50%     297.000000  178349.875769   191.128412    32.388153  2219.748677
75%     304.000000  178505.520157   191.874330    33.446580  2260.256411
max     323.000000  179087.623121   194.646661    37.195418  2429.107218
```

---

[← Change-point Model](02-change-point-model.md) · [Up: contents](index.md)
