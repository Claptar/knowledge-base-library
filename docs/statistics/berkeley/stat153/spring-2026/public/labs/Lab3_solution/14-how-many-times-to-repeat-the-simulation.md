---
title: how many times to repeat the simulation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# how many times to repeat the simulation

**Source:** [`public/labs/Lab3_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

nsamps = 10000
y = beta0 + beta1*x + np.random.randn(nsamps,n)*np.sqrt(sigma2)

print('y is of shape', y.shape)
```

```
y is of shape (10000, 10)
```

Now we will use the MLE solutions for estimating each of these parameters from our sampled data.

```python

---

[← n is the number of time points](13-n-is-the-number-of-time-points.md) · [Up: contents](index.md) · [Initialize values for our estimates →](15-initialize-values-for-our-estimates.md)
