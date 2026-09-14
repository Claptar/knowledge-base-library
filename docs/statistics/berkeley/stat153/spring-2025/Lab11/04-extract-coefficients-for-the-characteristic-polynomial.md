---
title: Extract coefficients for the characteristic polynomial
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Extract coefficients for the characteristic polynomial

**Source:** [`Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

coeffs = [(-1) * armd_9.params[i] for i in range(9, 0, -1)]  # Reverse order: lags 9→1
coeffs.append(1)
roots = np.roots(coeffs)
magnitudes = np.abs(roots)
print(magnitudes)
```

```
[1.30855577 1.30855577 1.31416814 1.31416814 1.17555576 1.17555576
 1.07010924 1.02490237 1.02490237]
```

These magnitudes coincide with the values in the table although the order in which they are listed in the table may be different (there is no default ordering for displaying the roots).

---

[← characteristic polynomial](03-characteristic-polynomial.md) · [Up: contents](index.md)
