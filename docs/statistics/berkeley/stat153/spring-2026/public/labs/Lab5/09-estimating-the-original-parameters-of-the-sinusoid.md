---
title: Estimating the original parameters of the sinusoid
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimating the original parameters of the sinusoid

**Source:** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Let's get back the original parameters again with this (hopefully) improved regression:

$$R=\sqrt{\beta_1^2+ \beta_2^2}, \quad \phi = \arctan\left(-\frac{\beta_2}{\beta_1}\right)$$

Let's see what we get.

```python
B0_hat = #FILL IN
R_hat = #FILL IN
phi_hat = #FILL IN

print(f'B0={B0}\t B0_hat={B0_hat}')
print(f'R={R}\t R_hat={R_hat}')
print(f'phi={phi}\t phi_hat={phi_hat}')
print(f'f={f}\t f_hat={best_f}')
```

---

[← Estimating the original parameters of the sinusoid](08-estimating-the-original-parameters-of-the-sinusoid.md) · [Up: contents](index.md) · [How does this look now? →](10-how-does-this-look-now.md)
