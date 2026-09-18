---
title: Bayesian regularization (from Lecture 12)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Bayesian regularization (from Lecture 12)

In the last lecture, we worked with the following prior (as a Bayesian method for regularization):
\begin{align*}
   \beta_0, \beta_1 \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C) ~~~ \beta_2, \dots, \beta_{n-1} \overset{\text{i.i.d}}{\sim} N(0, \tau^2),
\end{align*}
We also treat $\tau$ (and $\sigma$) as unknown parameters and used the prior:
\begin{align*}
    \log \tau, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C).
\end{align*}
With this prior, the posterior for $\beta, \tau, \sigma$ can be described as follows. The posterior of $\beta$ conditional on $\sigma$ and $\tau$ is given by:
\begin{align*}
   \beta \mid \text{data}, \sigma, \tau \sim N \left(\left(\frac{X^T
                          X}{\sigma^2} + Q^{-1}  \right)^{-1} \frac{X^T y}{\sigma^2},  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}\right).
\end{align*}
where $Q$ is the diagonal matrix with diagonal entries $C, C, \tau^2, \dots, \tau^2$. Further the posterior of $\tau$ and $\sigma$ is given by:
\begin{align*}
&  f_{\tau, \sigma \mid \text{data}}(\tau, \sigma) \\ &\propto
  \frac{\sigma^{-n-1} \tau^{-1}}{\sqrt{\det Q}}  \sqrt{\det
  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}} \exp \left(-\frac{y^T y}{2 \sigma^2} \right)\exp
  \left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T
  X}{\sigma^2} +
   Q^{-1} \right)^{-1} \frac{X^T y}{\sigma^2}  \right).
\end{align*}
We can simplify this formula slightly in order to avoid specifying $C$ explicitly using
\begin{align*}
   \det Q  = C \times C \times \tau^2 \times \dots \times \tau^2 = C^2 \tau^{2(n-2)} \propto \tau^{2(n-2)}.
\end{align*}
Also
\begin{align*}
   Q^{-1} = \text{diag}(1/C, 1/C, 1/\tau^2, \dots, 1/\tau^2) \approx \text{diag}(0, 0, 1/\tau^2, \dots, 1/\tau^2) = \frac{J}{\tau^2}
\end{align*}
where $J$ is the diagonal matrix with diagonals $0, 0, 1, \dots, 1$.

Let $Q^{-1}_{\text{approx}}$ be the above diagonal matrix with diagonal entries $0, 0, 1/\tau^2, \dots, 1/\tau^2$. We shall use $Q^{-1}_{\text{approx}}$ as our proxy for $Q^{-1}$. Note that $Q^{-1}_{\text{approx}}$ does not involve any specification of $C$. With this, we rewrite the posterior of $\tau, \sigma$ as:
\begin{align*}
&  f_{\tau, \sigma \mid \text{data}}(\tau, \sigma) \\ &\propto
  \sigma^{-n-1} \tau^{-n+1}   \sqrt{\det
  \left(\frac{X^T X}{\sigma^2} + \frac{J}{\tau^2} \right)^{-1}} \exp \left(-\frac{y^T y}{2 \sigma^2} \right)\exp
  \left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T
  X}{\sigma^2} + \frac{J}{\tau^2}
   \right)^{-1} \frac{X^T y}{\sigma^2}  \right).
\end{align*}
Below we compute this posterior on log-scale for each value in a grid chosen for $\tau$ and $\sigma$.

```python
tau_gr = np.logspace(np.log10(0.0001), np.log10(1), 100)
sig_gr = np.logspace(np.log10(0.1), np.log10(1), 100)

t, s = np.meshgrid(tau_gr, sig_gr)

g = pd.DataFrame({'tau': t.flatten(), 'sig': s.flatten()})

for i in range(len(g)):
    tau = g.loc[i, 'tau']
    sig = g.loc[i, 'sig']
    J_by_tausq = np.diag(np.concatenate([[0, 0], np.repeat(tau**(-2), n-2)]))
    Mat = J_by_tausq + (X.T @ X)/(sig ** 2)
    Matinv = np.linalg.inv(Mat)
    sgn, logcovdet = np.linalg.slogdet(Matinv)
    g.loc[i, 'logpost'] = (-n-1)*np.log(sig) + (-n+1)*np.log(tau) + 0.5 * logcovdet - ((np.sum(y ** 2))/(2*(sig ** 2))) + (y.T @ X @ Matinv @ X.T @ y)/(2 * (sig ** 4))
```

The posterior samples for all the parameters can be generated as follows.

```python
g['post'] = np.exp(g['logpost'] - np.max(g['logpost']))
g['post'] = g['post']/np.sum(g['post'])
```

```python
N = 1000
samples = g.sample(N, weights = g['post'], replace = True)
tau_samples = np.array(samples.iloc[:,0])
sig_samples = np.array(samples.iloc[:,1])
betahats = np.zeros((n, N))
muhats = np.zeros((n, N))
for i in range(N):
    tau = tau_samples[i]
    sig = sig_samples[i]
    J_by_tausq = np.diag(np.concatenate([[0, 0], np.repeat(tau**(-2), n-2)]))
    XTX = np.dot(X.T, X)
    TempMat = np.linalg.inv(J_by_tausq + (XTX/(sig ** 2)))
    XTy = np.dot(X.T, y)
    #generate betahat from the normal distribution with mean:
    norm_mean = np.dot(TempMat, XTy/(sig ** 2))
    #and covariance matrix:
    norm_cov = TempMat
    betahat = np.random.multivariate_normal(norm_mean, norm_cov)
    muhat = np.dot(X, betahat)
    betahats[:,i] = betahat
    muhats[:,i] = muhat
```

```python
beta_est = np.mean(betahats, axis = 1)
mu_est = np.mean(muhats, axis = 1) #these are the fitted values

plt.plot(y, label = 'Data')
plt.plot(mu_est, color = 'black', label = 'Posterior Mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting all the posterior fitted values:
plt.plot(y, label = 'Data')
for i in range(N):
    plt.plot(muhats[:,i], color = 'red')
plt.plot(mu_est, color = 'black', label = 'Posterior Mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The posterior samples of $\tau$ and $\sigma$ can be visualized by their histograms.

```python
# First histogram: tau_samples
plt.subplot(1, 2, 1)
plt.hist(tau_samples, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of tau samples')
plt.xlabel('tau')
plt.ylabel('Frequency')

# Second histogram: sig_samples
plt.subplot(1, 2, 2)
plt.hist(sig_samples, bins=30, color='lightcoral', edgecolor='black')
plt.title('Histogram of sigma samples')
plt.xlabel('sigma')
plt.ylabel('Frequency')

# Adjust layout and show both side by side
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Summary statistics of the $\tau$ and $\sigma$ samples can be obtained as follows.

```python
df_tau_sigma = pd.DataFrame({
    'tau_samples': tau_samples,
    'sig_samples': sig_samples
})

# Summary statistics
print(df_tau_sigma.describe())
```

```
tau_samples  sig_samples
count  1000.000000  1000.000000
mean      0.002407     0.173061
std       0.000984     0.009609
min       0.000705     0.148497
25%       0.001789     0.166810
50%       0.002154     0.170735
75%       0.002848     0.178865
max       0.010476     0.205651
```

---

[← Quick Recap: Ridge Regularization (Lecture 11)](02-quick-recap-ridge-regularization-lecture-11.md) · [Up: contents](index.md) · [Bayesian Regularization (with a slightly different prior) →](04-bayesian-regularization-with-a-slightly-different-prior.md)
