---
title: Signal + noise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Signal + noise

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.random.seed(42)
noise_std = 20.0
x_noisy = x_clean + noise_std * np.random.randn(len(t))

---

[← Clean signal](09-clean-signal.md) · [Up: contents](index.md) · [Theoretical power for each component →](11-theoretical-power-for-each-component.md)
