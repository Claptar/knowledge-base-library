---
title: Run this code a few times to be sure of convergence.
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Run this code a few times to be sure of convergence.

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
Epoch 0, Loss: -35967.2383
Epoch 1000, Loss: -41305.5781
Epoch 2000, Loss: -41314.9375
Epoch 3000, Loss: -41330.3047
Epoch 4000, Loss: -41352.2773
Epoch 5000, Loss: -41381.5039
Epoch 6000, Loss: -41415.5938
Epoch 7000, Loss: -41448.9766
Epoch 8000, Loss: -41475.8164
Epoch 9000, Loss: -41494.0078
Epoch 10000, Loss: -41500.9023
Epoch 11000, Loss: -41510.1602
Epoch 12000, Loss: -41519.8242
Epoch 13000, Loss: -41525.5430
Epoch 14000, Loss: -41531.9727
Epoch 15000, Loss: -41537.0273
Epoch 16000, Loss: -41540.6719
Epoch 17000, Loss: -41543.7500
Epoch 18000, Loss: -41545.9062
Epoch 19000, Loss: -41547.5859
```

```python
#alpha_est = md_PiecewiseLinear(x_torch).detach().numpy() + np.log(np.std(pgram))
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram', color = 'lightblue')
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
import cvxpy as cp
import mosek

def spectrum_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    #problem.solve()
    problem.solve(solver = cp.MOSEK)
    return alpha.value, freq
```

```python
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 1000)
power_lasso = (2/n) * (np.exp(2 * alpha_opt_lasso))

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram), color = 'lightblue')
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "CVXPy LASSO Estimate")
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The PyTorch is not able to figure out the three main peaks in the log power spectrum. This is probably because of the poor quality of the initialization. Note that the main peaks are all near the initial frequencies so that is where the knots need to be. If we find the peaks and troughs from our spectrum estimate from Lecture 15, and then initialize the PyTorch algorithm using knots near the peaks-troughs, then it will work better.

```python
from scipy.signal import find_peaks

---

[← Run this code a few times to be sure of convergence.](21-run-this-code-a-few-times-to-be-sure-of-convergence.md) · [Up: contents](index.md) · [Find peaks →](23-find-peaks.md)
