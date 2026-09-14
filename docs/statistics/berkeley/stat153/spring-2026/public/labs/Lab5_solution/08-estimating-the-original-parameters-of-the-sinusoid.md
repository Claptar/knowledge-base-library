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

Let's get back the original parameters again with this (hopefully) improved regression:

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
B0=2	 B0_hat=1.9930655070550236
R=2.5	 R_hat=2.4680140137480113
phi=0	 phi_hat=-0.006247204538511174
f=3.2	 f_hat=3.201201201201201
```

---

[← or](07-or.md) · [Up: contents](index.md) · [How does this look now? →](09-how-does-this-look-now.md)
