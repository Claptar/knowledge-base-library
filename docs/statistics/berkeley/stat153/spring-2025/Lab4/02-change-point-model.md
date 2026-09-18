---
title: Change-point Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Change-point Model

The same method can be used for inference in other nonlinear models. For example, consider the following model:
\begin{equation*}
   y_t = \beta_0 + \beta_1 I\{t > c\} + \epsilon_t.
\end{equation*}
This is known as a change-point model. The parameter $c$ is called the change-point. $I\{t > c\}$ is the **indicator** function which takes the value 1 if $t > c$ and 0 otherwise. The function $\beta_0 + \beta_1 I\{t > c\}$ equals $\beta_0$ for times $t \leq c$ and equals $\beta_0 + \beta_1$ for times $t > c$. Therefore this model states that the level of the time series equals $\beta_0$ until a time $c$ at which point it switches to $\beta_0 + \beta_1$. The value of $c$ is therefore called the changepoint. From the given data $y_1, \dots, y_n$, we need to infer the parameter $c$ as well as $\beta_0, \beta_1, \sigma$. The unknown parameter $c$ makes it a nonlinear model. If $c$ were known, this will become a linear regression model with $X$-matrix given by
\begin{equation*}
    X_c = \begin{pmatrix} 1 & I\{1 > c\} \\ 1 & I\{2 > c\} \\ 1 & I\{3 > c\} \\ \cdot & \cdot \\ \cdot & \cdot \\ \cdot & \cdot \\ 1 & I\{n > c\} \end{pmatrix}
\end{equation*}

Inference for the parameter $c$ proceeds just like before. We first compute RSS($c$):
\begin{equation*}
    RSS(c) := \min_{\beta_0, \beta_1} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 I\{t > c\})^2
\end{equation*}
and then minimize over $c$ to obtain the MLE of $\hat{c}$. After finding $\hat{c}$, we can find the MLEs of the other parameters as in linear regression with known $c$.

```python
# Here is a simulated dataset having a change point:
n = 10000
mu1 = 0
mu2 = 0.4
dt = np.concatenate([np.repeat(mu1, n / 2), np.repeat(mu2, n / 2)])

sig = 1
errorsamples = rng.normal(loc = 0, scale = sig, size = n)

y = dt + errorsamples
```

```python
plt.figure(figsize = (15, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
def rss(c):
    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

```python
allcvals = np.arange(5, n - 4)
# we are ignoring a few points at the beginning and at the end
rssvals = np.array([rss(c) for c in allcvals])
```

```python
plt.plot(allcvals, rssvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
c_hat = allcvals[np.argmin(rssvals)]
print(c_hat)
```

```
4981
```

```python
# Estimates of other parameters:
x = np.arange(1, n + 1)
xc = (x > c_hat).astype(float)
X = np.column_stack([np.ones(n), xc])

md = sm.OLS(y, X).fit()
print(md.params)
# this gives estimates of beta_0, beta_1 (compare them to the true values which generated the data)

b0_est = md.params[0]
b1_est = md.params[1]

b0_true = mu1
b1_true = mu2 - mu1
print(np.column_stack((np.array([b0_est, b1_est]), np.array([b0_true, b1_true]))))

rss_chat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_chat / n)
sigma_unbiased = np.sqrt((rss_chat)/(n - 2))
print(np.array([sigma_mle, sigma_unbiased, sig]))
#sig is the true value of sigma which generated the data
```

```
[0.01969268 0.40873694]
[[0.01969268 0.        ]
 [0.40873694 0.4       ]]
[1.00274789 1.00284818 1.        ]
```

Bayesian uncertainty quantification also works exactly as before.  The Bayesian posterior for $c$ is:
\begin{equation*}
 |X_c^T X_c|^{-1/2} \cdot \left(\frac{1}{RSS(c)} \right)^{(n-p)/2}
\end{equation*}
where $p = 2$ and $|X_c^T X_c|$ denotes the determinant of $X_c^T X_c$.

As before, it is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python
# Plot the fitted values:
plt.plot(y)
plt.plot(md.fittedvalues, color = 'red')
```

```
[<matplotlib.lines.Line2D at 0x16a9f9090>]
```

*(1 figure omitted — see the original notebook.)*

```python
def logpost(c):
    x = np.arange(1, n+1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])
    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X))
    # sgn gives the sign of the determinant (in our case, this should 1)
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

Let us exponentiate the log-posterior values to get the posterior.

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

We draw posterior samples exactly as before.

```python
N = 1000
cpostsamples = rng.choice(allcvals, N, replace = True, p = postvals)

post_samples = np.zeros(shape = (N, 4))
post_samples[:, 0] = cpostsamples
for i in range(N):
    c = cpostsamples[i]
    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])
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
[[5.01400000e+03 1.61186008e-02 4.15836357e-01 9.94694854e-01]
 [5.07500000e+03 2.21172885e-02 4.02259427e-01 9.96874208e-01]
 [4.93100000e+03 6.69816740e-03 4.29948362e-01 9.91129525e-01]
 ...
 [5.03000000e+03 1.52941625e-02 4.27556266e-01 1.00020949e+00]
 [5.01400000e+03 2.52471690e-02 3.94416060e-01 9.92312337e-01]
 [4.99600000e+03 1.99135692e-02 3.90096091e-01 1.00377472e+00]]
```

These posterior samples can be used to visualize the uncertainty in the fitted functions.

```python
x = np.arange(1, n + 1)
plt.figure(figsize = (15, 6))
plt.plot(y)

for i in range(N):
    c = cpostsamples[i]
    b0 = post_samples[i, 1]
    b1 = post_samples[i, 2]
    ftdval = b0 + b1 * (x > c).astype(float)

    plt.plot(ftdval, color = 'red')
```

*(1 figure omitted — see the original notebook.)*

```python
# Summary of the posterior samples:
pd.DataFrame(post_samples).describe()
```

```
0            1            2            3
count  1000.000000  1000.000000  1000.000000  1000.000000
mean   4990.655000    -0.007485     0.413230     1.002923
std      10.042451     0.014443     0.020551     0.007168
min    4931.000000    -0.053492     0.353096     0.978639
25%    4986.000000    -0.017177     0.399384     0.998240
50%    4989.000000    -0.007820     0.413441     1.002838
75%    4993.000000     0.002567     0.425842     1.007765
max    5104.000000     0.038280     0.483661     1.027721
```

---

[← Inference in Sinusoid Models](01-inference-in-sinusoid-models.md) · [Up: contents](index.md) · [Change of Slope (or Broken Stick Regression) →](03-change-of-slope-or-broken-stick-regression.md)
