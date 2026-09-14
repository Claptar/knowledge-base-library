---
title: 'Create a test signal: sum of two sinusoids + noise'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Create a test signal: sum of two sinusoids + noise

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.random.seed(42)
n = 100
t = np.arange(1, n+1)
x = 3*np.cos(2*math.pi*t*5/n) + 2*np.sin(2*math.pi*t*12/n) + np.random.normal(0, 0.5, n)

---

[← Lab 7 - Power Spectral Analysis](01-lab-7---power-spectral-analysis.md) · [Up: contents](index.md) · [Compute using your function →](03-compute-using-your-function.md)
