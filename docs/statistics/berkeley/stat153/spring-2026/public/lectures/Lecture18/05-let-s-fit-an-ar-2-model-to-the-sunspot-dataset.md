---
title: Let's fit an AR(2) model to the sunspot dataset
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's fit an AR(2) model to the sunspot dataset

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

y_sun = sunspots['sunspots'].dropna().values

ar2_model = ARIMA(y_sun, order=(2, 0, 0)).fit()
print(ar2_model.summary().tables[1])
print(f"\nAR(2) coefficients: φ₁ = {ar2_model.params[1]:.4f}, φ₂ = {ar2_model.params[2]:.4f}")

---

[← What do we see?](04-what-do-we-see.md) · [Up: contents](index.md) · [Check the characteristic roots →](06-check-the-characteristic-roots.md)
