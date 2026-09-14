---
title: Lab12 Part 12 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab12 Part 12 —

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
-2364.494873895399 -2364.494873895399
-2344.72865722396 -2344.72865722396
```

```python
n = len(y)
mod2_aic_formula = -2 * mod2.llf + 2 * len(mod2.params)
mod2_bic_formula = -2 * mod2.llf + (np.log(n - 1)) * len(mod2.params)
print(mod2_aic_formula, mod2.aic)
print(mod2_bic_formula, mod2.bic)
```

```
-2354.933614650533 -2354.933614650533
-2339.120641313382 -2339.120641313382
```

```python
n = len(y)
mod3_aic_formula = -2 * mod3.llf + 2 * len(mod3.params)
mod3_bic_formula = -2 * mod3.llf + (np.log(n - 2)) * len(mod3.params)
print(mod3_aic_formula, mod3.aic)
print(mod3_bic_formula, mod3.bic)

---

[← Note that we have used (n - 1) for sample size in the calculation for BIC](11-note-that-we-have-used-n---1-for-sample-size-in-the-calculat.md) · [Up: contents](index.md) · [Now we are using (n - 2) for sample size in the calculation of BIC →](13-now-we-are-using-n---2-for-sample-size-in-the-calculation-of.md)
