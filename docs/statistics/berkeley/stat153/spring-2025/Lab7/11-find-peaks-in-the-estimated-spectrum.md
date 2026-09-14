---
title: Find peaks in the estimated spectrum
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks in the estimated spectrum

**Source:** [`Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks_lasso, _ = find_peaks(tau_opt_lasso)
peak_lasso_freqs = peaks_lasso / n
gaps_lasso = np.diff(peaks_lasso)

print("Peak frequencies:", peak_lasso_freqs)
print("Peak periods:", 1 / peak_lasso_freqs)
print("Gaps between peaks:", gaps_lasso)
```

```
Peak frequencies: [0.02358491 0.10613208 0.1658805  0.24921384 0.33254717 0.4158805 ]
Peak periods: [42.4         9.42222222  6.02843602  4.0126183   3.0070922   2.40453686]
Gaps between peaks: [105  76 106 106 106]
```

From the ridge estimate, the first peak corresponds to a period of 39.75 months (which is about 3.3125 years). This can be interpreted as a "business cycle frequency". The remaining peaks seem to correspond to seasonal and calendar effects. The lasso estimate can be interpreted similarly.

To eliminate these seasonal effects and to focus more on the business cycles, we can change the definition of $y$ slightly by defining it as the growth rate:
\begin{equation*}
   y_t = 100 \left(\log I_t - \log I_{t-12} \right)
\end{equation*}

```python
pind = prod_index['IPB50001N']
pind = pind.to_numpy()
y_diff = 100 * (np.log(pind[12:]) - np.log(pind[:-12]))

plt.figure(figsize = (12, 6))
plt.plot(y_diff)

n = len(y_diff)
print(n) # now n is odd

plt.show()
```

```
1261
```

*(1 figure omitted — see the original notebook.)*

Now $n$ is odd.

```python
def spectrum_n_odd_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y) # Length of original time series

    alpha = cp.Variable(m)

    likelihood_term = cp.sum(cp.multiply((2 * I / n), cp.exp(-2 * alpha)) + 2 * alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))

    objective = cp.Minimize(likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()

    return alpha.value, freq # Return estimated log spectral density and frequencies

def spectrum_n_odd_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y) # Length of original time series

    alpha = cp.Variable(m)

    likelihood_term = cp.sum(cp.multiply((2 * I / n), cp.exp(-2 * alpha)) + 2 * alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))

    objective = cp.Minimize(likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()

    return alpha.value, freq # Return estimated log spectral density and frequencies
```

```python
freq, pgram = periodogram(y_diff)
alpha_opt_ridge, freq = spectrum_n_odd_estimator_ridge(y_diff, 5000)

---

[← Find peaks in the estimated spectrum](10-find-peaks-in-the-estimated-spectrum.md) · [Up: contents](index.md) · [I found lambda = 5000 is reasonable here →](12-i-found-lambda-5000-is-reasonable-here.md)
