---
title: Estimate of sigma
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimate of sigma

**Source:** [`Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

rss = np.sum(md.resid ** 2)
sigmahat = np.sqrt(rss / (n - 3))

print(sigmahat)
```

```
9.495940890783043
```

Next we look at Bayesian inference which will yield similar results but will additionally provide uncertainty intervals for $f$. We use the following formula for the Bayesian posterior that we derived in class:
\begin{equation*}
   I\{0 \leq f \leq 1/2\} \cdot |X_f^T X_f|^{-1/2} \cdot \left(\frac{1}{S(\hat{\beta}(f), f)} \right)^{(n-p)/2}
\end{equation*}
where $p = 3$ and $|X_f^T X_f|$ denotes the determinant of $X_f^T X_f$.

It is better to compute the logarithm of the posterior (as opposed to the posterior directly) because of numerical issues.

```python
def logpost(f):
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    p = X.shape[1]

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) # sgn gives the sign of the determinant (in our case, this should 1)
    # log_det gives the logarithm of the absolute value of the determinant
    logval = ((p - n) / 2) * np.log(rss) - 0.5 * log_det

    return logval
```

While evaluating the log posterior on a grid, it is important to make sure that we do not include frequencies $f$ for which $X_f^T X_f$ is singular. This will be the case for $f = 0$ and $f = 1/2$. When $f$ is very close to 0 or $0.5$, the term $|X_f^T X_f|^{-1/2}$ will be very large because of near-singularity of $X_f^T X_f$. We will therefore exclude frequencies very close to 0 and 0.5 from the grid while calculating posterior probabilities.

```python
logpostvals = np.array([logpost(f) for f in allfvals])
```

```python
plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
allfvals = allfvals[100:(ngrid - 100)]

print(np.min(allfvals), np.max(allfvals))

logpostvals = np.array([logpost(f) for f in allfvals])
```

```
0.0005000050000500005 0.49949999499995
```

```python
plt.plot(allfvals, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Value')
plt.title('Logarithm of (unnormalized) posterior density')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we exponentiate the log posterior to obtain posterior. Here we again need to be mindful of numerical issues. If we directly take the exponent of numbers, we might get 0 or $\infty$. So we first subtract a constant so that the values are somewhat closer to 0 before taking the exponent.

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized / (np.sum(postvals_unnormalized))
```

```python
plt.plot(allfvals, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals_density = postvals_unnormalized / (np.sum(postvals_unnormalized))

postvals_density = postvals_density * (ngrid - 200) / 0.5
```

```python
plt.plot(allfvals, postvals_density)
plt.xlabel('Frequency')
plt.ylabel('Density')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Using the posterior distribution, we can calculate posterior mean etc. and obtain credible intervals for $f$.

```python
#Posterior mean of f:
fpostmean = np.sum(postvals * allfvals)

#Posterior mode of f:
fpostmode = allfvals[np.argmax(postvals)]

print(fpostmean, fpostmode, fhat)
```

```
0.19989514344518863 0.1998969989699897 0.1998969989699897
```

Note that the posterior mode coincides with the MLE. Let us now compute a credible interval for $f$. A 95\% credible interval is an interval for which the posterior probability is about 95\%. The following function takes an input value $m$ and compute the posterior probability assigned to the interval $\hat{f} - m*\delta, \hat{f} + m*\delta$ where $\delta$ is the grid resolution that we used for computing the posterior.

```python
def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind - m):(est_ind + m)])

    return(ans)
```

We now start with a small value of $m$ (say $m = 0$) and keep increasing it until the posterior probability reaches 0.95.

```python
m = 0
while PostProbAroundMax(m) <= 0.95:
    m = m + 1

print(m)
```

```
65
```

The credible interval for $f$ can then be computed in the following way.

```python
est_ind = np.argmax(postvals)
f_est = allfvals[est_ind]

---

[← the MLE of f is now calculated as](02-the-mle-of-f-is-now-calculated-as.md) · [Up: contents](index.md) · [95% credible interval for f →](04-95-credible-interval-for-f.md)
