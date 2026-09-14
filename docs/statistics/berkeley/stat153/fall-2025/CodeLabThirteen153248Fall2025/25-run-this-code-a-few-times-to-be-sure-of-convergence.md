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
Epoch 0, Loss: -41205.1836
Epoch 1000, Loss: -41896.0898
Epoch 2000, Loss: -41904.6094
Epoch 3000, Loss: -41907.7344
Epoch 4000, Loss: -41907.7227
Epoch 5000, Loss: -41908.2969
Epoch 6000, Loss: -41906.9531
Epoch 7000, Loss: -41904.2344
Epoch 8000, Loss: -41908.1953
Epoch 9000, Loss: -41908.4688
Epoch 10000, Loss: -41907.9727
Epoch 11000, Loss: -41908.5391
Epoch 12000, Loss: -41908.3516
Epoch 13000, Loss: -41897.2539
Epoch 14000, Loss: -41908.6953
Epoch 15000, Loss: -41908.5977
Epoch 16000, Loss: -41908.5781
Epoch 17000, Loss: -41908.1875
Epoch 18000, Loss: -41907.3008
Epoch 19000, Loss: -41906.0352
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
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 1000)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram), color = 'lightblue')
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "CVXPy LASSO Estimate")
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now the two estimates are much closer to each other. This shows how tricky some optimization functions are. They depend sensitively on the initialization. Our estimate from Lectures 14-15 were based on convex optimization problems however which are more stable.

---

[← these knots are chosen to be roughly near the peaks and troughs](24-these-knots-are-chosen-to-be-roughly-near-the-peaks-and-trou.md) · [Up: contents](index.md)
