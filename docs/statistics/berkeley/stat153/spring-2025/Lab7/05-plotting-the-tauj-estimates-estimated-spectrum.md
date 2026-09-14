---
title: Plotting the tauj estimates (estimated spectrum)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plotting the tauj estimates (estimated spectrum)

**Source:** [`Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

tau_opt_ridge = np.exp(alpha_opt_ridge)

plt.figure(figsize = (12, 6))
plt.plot(freq, tau_opt_ridge)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
def spectrum_n_even_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    n = len(y) # Length of original time series (assumed to be even here)
    m = (n // 2) - 1

    alpha = cp.Variable(n // 2)

    I_1_to_m = I[0:(m - 1)]
    I_m_plus_1 = I[m]

    neg_likelihood_term_1_to_m = cp.sum(cp.multiply((2 * I_1_to_m / n), cp.exp(-2 * alpha[0:(m - 1)])) + 2 * alpha[0:(m - 1)])
    neg_likelihood_term_m_plus_1 = cp.multiply((I_m_plus_1 / (2 * n)), cp.exp(-2 * alpha[m])) + alpha[m]
    neg_likelihood_term = neg_likelihood_term_1_to_m + neg_likelihood_term_m_plus_1

    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))

    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()

    return alpha.value, freq
```

```python
alpha_opt_lasso, freq = spectrum_n_even_estimator_lasso(y, 100)

---

[← This illustrates how the spectrum estimate can be viewed as a smoothing of the periodogram](04-this-illustrates-how-the-spectrum-estimate-can-be-viewed-as.md) · [Up: contents](index.md) · [I found lambda = 100 is reasonable here →](06-i-found-lambda-100-is-reasonable-here.md)
