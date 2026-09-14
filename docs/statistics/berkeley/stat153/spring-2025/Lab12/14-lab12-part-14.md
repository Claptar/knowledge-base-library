---
title: Lab12 Part 14 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab12 Part 14 —

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
-2357.3214233532403 -2357.3214233532403
-2349.420138248065 -2349.420138248065
```

```python
n = len(y)
mod4_aic_formula = -2 * mod4.llf + 2 * len(mod4.params)
mod4_bic_formula = -2 * mod4.llf + (np.log(n - 2)) * len(mod4.params)
print(mod4_aic_formula, mod4.aic)
print(mod4_bic_formula, mod4.bic)

---

[← Now we are using (n - 2) for sample size in the calculation of BIC](13-now-we-are-using-n---2-for-sample-size-in-the-calculation-of.md) · [Up: contents](index.md) · [Again we are using (n - 2) for sample size in the calculation of BIC →](15-again-we-are-using-n---2-for-sample-size-in-the-calculation.md)
