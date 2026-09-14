---
title: What do we see?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# What do we see?

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Notice that we have the following behavior:

- **ACF**: Slowly decaying, oscillatory. The 11-year cycle shows up as a damped sinusoid in the ACF.
- **PACF**: Drops sharply after lag 2. This is the signature of an **AR(2)** process.

The remarkable thing: just **two coefficients** are enough to generate quasi-periodic behavior. Let's fit it.

```python

---

[← Sunspot data is in the statsmodels package (as well as astsa, but here we don't need it!)](03-sunspot-data-is-in-the-statsmodels-package-as-well-as-astsa.md) · [Up: contents](index.md) · [Let's fit an AR(2) model to the sunspot dataset →](05-let-s-fit-an-ar-2-model-to-the-sunspot-dataset.md)
