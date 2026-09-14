---
title: Check the characteristic roots
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Check the characteristic roots

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ar_poly = np.array([1, -ar2_model.params[1], -ar2_model.params[2]])
roots = np.roots(ar_poly)
print(f"\nCharacteristic roots: {roots}")
print(f"Modulus: {np.abs(roots)}")
if np.any(np.iscomplex(roots)):
    period = 2 * np.pi / np.abs(np.angle(roots[0]))
    print(f"Implied period: {period:.1f} years  (actual sunspot cycle ≈ 11 years)")
```

```
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         49.7462      3.938     12.631      0.000      42.027      57.465
ar.L1          1.3906      0.037     37.694      0.000       1.318       1.463
ar.L2         -0.6886      0.036    -19.363      0.000      -0.758      -0.619
sigma2       274.7272     18.897     14.538      0.000     237.689     311.765
==============================================================================

AR(2) coefficients: φ₁ = 1.3906, φ₂ = -0.6886

Characteristic roots: [0.69531643+0.45288847j 0.69531643-0.45288847j]
Modulus: [0.82980293 0.82980293]
Implied period: 10.9 years  (actual sunspot cycle ≈ 11 years)
```

## Check residuals

We can now look at the residuals for the AR(2) model to determine whether we've fully captured the periodic activity in our time series. If the residuals look like white noise and have ACF and PACF peaking only at 0 (indicating no further correlation structure), then our model has done a good job.

```python

---

[← Let's fit an AR(2) model to the sunspot dataset](05-let-s-fit-an-ar-2-model-to-the-sunspot-dataset.md) · [Up: contents](index.md) · [Residual diagnostics for AR(2) →](07-residual-diagnostics-for-ar-2.md)
