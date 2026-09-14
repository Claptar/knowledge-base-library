---
title: (since we are dealing with a pure AR process, there is no theta coefficient)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# (since we are dealing with a pure AR process, there is no theta coefficient)

**Source:** [`CodeLabTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

AR2_process = ArmaProcess(ar, ma)
nlags = 40

ma_infinity = AR2_process.arma2ma(lags = nlags)

---

[← these are the theta-coefficients of the ARMA process](02-these-are-the-theta-coefficients-of-the-arma-process.md) · [Up: contents](index.md) · [this gives \psij, j = 0, \dots, lags-1 →](04-this-gives-psij-j-0-dots-lags-1.md)
