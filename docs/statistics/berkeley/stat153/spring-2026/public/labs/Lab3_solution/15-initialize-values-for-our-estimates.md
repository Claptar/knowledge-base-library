---
title: Initialize values for our estimates
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Initialize values for our estimates

**Source:** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

beta0_hat = np.zeros(nsamps,)
beta1_hat = np.zeros(nsamps,)
sigma2_hat = np.zeros(nsamps,)
sigma2_hat_unbiased = np.zeros(nsamps,)

for i in np.arange(nsamps):
    beta1_hat[i] = np.sum((y[i,:]-y[i,:].mean())*(x-x.mean()))/np.sum((x-x.mean())**2)
    beta0_hat[i] = y[i,:].mean() - beta1_hat[i] * x.mean()
    sigma2_hat[i] = 1/n*np.sum((y[i,:] - beta0_hat[i] - beta1_hat[i]*x)**2)
    sigma2_hat_unbiased[i] = sigma2_hat[i]*n/(n-2)
```

```python
plt.figure(figsize=(10,3))
plt.plot(y.T);
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize=(10,3))
plt.subplot(1,3,1)
plt.hist(beta0_hat, bins=50, alpha=0.5);
plt.axvline(beta0, color='r')
plt.axvline(beta0_hat.mean(), color='blue', linestyle='--')
plt.title('beta0 estimate')

plt.subplot(1,3,2)
plt.hist(beta1_hat, bins=50, alpha=0.5);
plt.axvline(beta1, color='r')
plt.axvline(beta1_hat.mean(), color='blue', linestyle='--')
plt.title('beta1 estimate')

plt.subplot(1,3,3)
plt.hist(sigma2_hat, bins=50, alpha=0.5);
plt.axvline(sigma2_hat.mean(), color='blue', linestyle='--')
plt.hist(sigma2_hat_unbiased, bins=50, alpha=0.5);
plt.axvline(sigma2, color='r')
plt.axvline(sigma2_hat_unbiased.mean(), color='m', linestyle='--')
plt.title('sigma2 estimate')
```

```
Text(0.5, 1.0, 'sigma2 estimate')
```

*(1 figure omitted — see the original notebook.)*

```python
print(np.mean(sigma2_hat), np.std(sigma2_hat))
print(np.mean(sigma2_hat_unbiased), np.std(sigma2_hat_unbiased))
print(sigma2)
```

```
17.726358503291888 8.794352684562693
22.157948129114857 10.992940855703367
22.2
```

```python

---

[← how many times to repeat the simulation](14-how-many-times-to-repeat-the-simulation.md) · [Up: contents](index.md) · [Lab3 solution Part 16 — →](16-lab3-solution-part-16.md)
