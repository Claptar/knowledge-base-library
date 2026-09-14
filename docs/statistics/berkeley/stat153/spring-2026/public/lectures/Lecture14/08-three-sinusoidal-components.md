---
title: Three sinusoidal components
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Three sinusoidal components

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

f = [6, 10.5, 39.2]  # Frequencies of the sinusoids
x1 = 12*np.cos(2*math.pi*f[0]*t) + 13*np.sin(2*math.pi*f[0]*t)
x2 =  4*np.cos(2*math.pi*f[1]*t) +  5*np.sin(2*math.pi*f[1]*t)
x3 =  6*np.cos(2*math.pi*f[2]*t) +  7*np.sin(2*math.pi*f[2]*t)

---

[← Welch with decreasing segment sizes](07-welch-with-decreasing-segment-sizes.md) · [Up: contents](index.md) · [Clean signal →](09-clean-signal.md)
