---
title: Visualizing Uncertainty
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Visualizing Uncertainty

**Source:** [`Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

It was showed in Lecture 4 that the posterior distribution of $\beta$ (this is the vector of coefficients) is given by
\begin{equation*}
   \beta \mid \text{data} \sim t_{n-4, 4} \left(\hat{\beta}, \hat{\sigma}^2 (X^T X)^{-1} \right)
\end{equation*}
From the definition of the $t$-distribution above, we also know that the distribution above coincides with the distribution of
\begin{equation*}
    \hat{\beta} + \frac{Z}{\sqrt{V/(n-4)}}
\end{equation*}
where $Z \sim N(0, \hat{\sigma}^2 (X^T X)^{-1})$ and $V \sim \chi^2_{n-4}$ are independent. Using this, we can generate vectors $\beta$ from their posterior distribution and then plot the regression curves corresponding to the different generated $\beta$ vectors. This will give us an idea of the uncertainty underlying the coefficients.

```python
N = 200 # this the number of posterior samples that we shall draw
Sigma_mat = (rse ** 2) * (XTX_inverse)
#print(Sigma_mat)

rng = np.random.default_rng()
chi_samples = rng.chisquare(df = len(y) - 4, size = N)
chi_samples = chi_samples.reshape((-1, 1))
norm_samples = rng.multivariate_normal(mean = np.zeros(4), cov = Sigma_mat, size = N)

#post_samples = np.tile(betahat, (N, 1)) + norm_samples / np.sqrt(chi_samples / (len(y) - 4))
post_samples = betahat + norm_samples / np.sqrt(chi_samples / (len(y) - 4))
#print(post_samples)

plt.figure(figsize = (10, 6))
plt.plot(y, linewidth = 1, color = 'black')
for k in range(N):
    fvalsnew = np.dot(X, post_samples[k])
    plt.plot(fvalsnew, color = 'red', linewidth = 1)
plt.xlabel('Time (quarterly)')
plt.ylabel('Billions of dollars')
plt.title('GDP data with Fitted values along with uncertainty')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Even though $N = 200$ regression curves have been plotted, they are still fairly clustered together. This suggests that the uncertainty in these estimates is fairly small.

---

[← t-statistic and confidence intervals for the coefficients](09-t-statistic-and-confidence-intervals-for-the-coefficients.md) · [Up: contents](index.md) · [Other comments →](11-other-comments.md)
