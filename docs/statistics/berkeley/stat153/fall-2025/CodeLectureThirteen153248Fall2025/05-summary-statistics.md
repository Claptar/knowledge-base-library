---
title: Summary statistics
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Summary statistics

**Source:** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

### Bayesian Regularization (with a slightly different prior)

Now we work with the following prior:
\begin{align*}
   \beta_0, \beta_1 \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C) ~~~ \beta_2, \dots, \beta_{n-1} \overset{\text{i.i.d}}{\sim} N(0, \gamma^2 \sigma^2)
\end{align*}
We treat $\gamma$ and $\sigma$ also as unknown parameters and assign the prior:
\begin{align*}
    \log \gamma, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C).
\end{align*}
The only difference between this prior and the previous prior is that we are now parametrizing in terms of $(\gamma, \sigma)$ as opposed to $(\tau, \sigma)$ (the connection is $\tau = \sigma \gamma$). This is strictly a different prior however because under the assumption $\log \gamma, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C)$, the parameters $\gamma \times \sigma$ and $\sigma$ become dependent (under the prior) but the previous model assumes prior independence of $\tau$ and $\sigma$.

The posterior of $\gamma, \sigma, \beta$ can be described as follows.

The posterior of $\beta$ conditional on $\sigma$ and $\gamma$ is given by:
\begin{align*}
   \beta \mid \text{data}, \sigma, \tau \sim N \left(\left(\frac{X^T
                          X}{\sigma^2} + Q^{-1}  \right)^{-1} \frac{X^T y}{\sigma^2},  \left(\frac{X^T X}{\sigma^2} + Q^{-1} \right)^{-1}\right).
\end{align*}
where $Q$ is the diagonal matrix with diagonal entries $C, C, \gamma^2\sigma^2, \dots, \gamma^2\sigma^2$. This is the same as before. We shall again use the approximation $Q^{-1} \approx J/\tau^2 = J/(\gamma \sigma)^2$.

We next describe the posterior of $\gamma$ and $\sigma$. Unlike the case of the previous prior, the posterior of $\sigma$ conditional on $\gamma$ can be described in closed form as:

 \begin{equation*}
   \frac{1}{\sigma^2} \mid \text{data}, \gamma \sim \text{Gamma} \left(\frac{n}{2} - 1, \frac{y^T y - y^T X (X^T X + \gamma^{-2} J)^{-1} X^T y}{2} \right)
 \end{equation*}
 Finally the posterior of $\gamma$ is given by:

 \begin{align*}
   \gamma \mid \text{data} \sim \gamma^{-n+1} \sqrt{\det (X^T X + \gamma^{-2} J)^{-1}} \left(\frac{1}{y^T y - y^T X (X^T X + \gamma^{-2} J)^{-1} X^T y} \right)^{(n/2) - 1}
 \end{align*}

 We can compute this posterior on a grid of $\gamma$ values. Now we only need a 1D grid for $\gamma$ (unlike the previous model, where we needed two grids for $\tau$ and $\sigma$).

```python
gamma_gr = np.logspace(np.log10(1e-6), np.log10(1e4), 1000)
logpost_gamma = np.zeros(len(gamma_gr))

for i in range(len(gamma_gr)):
    gamma = gamma_gr[i]
    J_by_gammasq = np.diag(np.concatenate([[0, 0], np.repeat(gamma**(-2), n-2)]))
    Mat =  X.T @ X + J_by_gammasq
    Matinv = np.linalg.inv(Mat)
    sgn, logcovdet = np.linalg.slogdet(Matinv)
    logpost_gamma[i] =(-n+1)*np.log(gamma) + 0.5 * logcovdet - (n/2 - 1)*np.log(y.T @ y - y.T @ X @ Matinv @ X.T @ y)
```

```python
post_gamma  = np.exp(logpost_gamma - np.max(logpost_gamma))
post_gamma = post_gamma/np.sum(post_gamma)
```

```python
postmean_gamma = np.sum(gamma_gr * post_gamma)
print(postmean_gamma)
print(1/(postmean_gamma ** 2))
```

```
0.013881161336822876
5189.773404602882
```

The parameter $\gamma$ is nicely connected to the tuning parameter $\lambda$ used in ridge regression. The connection is given by $\gamma = 1/\sqrt{\lambda}$ or $\lambda = 1/\gamma^2$. This is because $\lambda = \sigma^2/\tau^2$ (as we saw in Lecture 12) and $\tau = \gamma \sigma$.

```python
b_ridge = solve_ridge(X, y, lambda_val = 1/(postmean_gamma ** 2))
plt.plot(y)
ridge_fitted = np.dot(X, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us draw posterior samples for all the parameters $\gamma, \sigma, \beta$.

```python
N = 1000
gamma_samples = np.random.choice(gamma_gr, size=N, p=post_gamma, replace=True)
plt.hist(gamma_samples, bins=30, color='lightgreen', edgecolor='black')
plt.title('Histogram of gamma samples')
plt.xlabel('gamma')
plt.ylabel('Frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Because of the connection between $\gamma$ and $\lambda$: $\lambda = 1/\gamma^2$, we can look at the histogram of values of $\lambda$:

```python
lambda_samples = 1/(gamma_samples ** 2)
plt.hist(lambda_samples, bins=100, color='lightgreen', edgecolor='black')
plt.title('Histogram of lambda samples')
plt.xlabel('lambda')
plt.ylabel('Frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here is the code for generating the samples from the other parameters.

```python
for i in range(N):
    gamma = gamma_samples[i]
    J_by_gammasq = np.diag(np.concatenate([[0, 0], np.repeat(gamma**(-2), n-2)]))
    Mat =  X.T @ X + J_by_gammasq
    Matinv = np.linalg.inv(Mat)
    gamma_dist_lambda_parameter = (y.T @ y - y.T @ X @ Matinv @ X.T @ y)/2
    gamma_dist_alpha_parameter = n/2 - 1
    sig = np.sqrt(1/np.random.gamma(gamma_dist_alpha_parameter, 1/gamma_dist_lambda_parameter))
    sig_samples[i] = sig
    XTX = np.dot(X.T, X)
    TempMat = np.linalg.inv((J_by_gammasq/(sig ** 2)) + (XTX/(sig ** 2)))
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
    plt.plot(muhats[:,i], color = 'lightcoral')
plt.plot(mu_est, color = 'black', label = 'Posterior Mean')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The following is the histogram of $\sigma$ values.

```python
plt.hist(sig_samples, bins=30, color='lightgreen', edgecolor='black')
plt.title('Histogram of sigma samples')
plt.xlabel('sigma')
plt.ylabel('Frequency')
plt.show()
```

```python
df_gamma_sigma = pd.DataFrame({
    'gamma_samples': gamma_samples,
    'sig_samples': sig_samples
})

---

[← Adjust layout and show both side by side](04-adjust-layout-and-show-both-side-by-side.md) · [Up: contents](index.md) · [Summary statistics →](06-summary-statistics.md)
