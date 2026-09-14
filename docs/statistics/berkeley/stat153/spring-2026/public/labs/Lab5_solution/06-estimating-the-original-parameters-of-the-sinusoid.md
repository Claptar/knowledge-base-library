---
title: Estimating the original parameters of the sinusoid
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimating the original parameters of the sinusoid

**Source:** [`public/labs/Lab5_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Recall we can get back the original parameters through their relationship to the $\beta$ values:

$$R=\sqrt{\beta_1^2+ \beta_2^2}, \quad \phi = \arctan\left(-\frac{\beta_2}{\beta_1}\right)$$

Let's see what we get.

```python
B0_hat = betas[0]
R_hat = np.sqrt(betas[1]**2 + betas[2]**2)
phi_hat = np.arctan(-betas[2]/betas[1])

print(f'B0={B0}\t B0_hat={B0_hat}')
print(f'R={R}\t R_hat={R_hat}')
print(f'phi={phi}\t phi_hat={phi_hat}')
print(f'f={f}\t f_hat={best_f}')
```

```
B0=2	 B0_hat=2.029404412553876
R=2.5	 R_hat=0.4737475535789633
phi=0	 phi_hat=1.0137021097636343
f=3.2	 f_hat=2.525252525252525
```

How does this look? It's okay, but not quite right. Try redoing the grid search again below in a way that you think will make this more accurate.

```python
nf = 10000  # Test this number of frequencies
f_grid = np.linspace(0,fs/2,nf)

---

[← Finding the frequency, $f$](05-finding-the-frequency.md) · [Up: contents](index.md) · [or →](07-or.md)
